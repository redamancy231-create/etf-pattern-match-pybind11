# etf-pattern-match-pybind11 Fork 修改方向全景分析

> 生成日期: 2026-07-20 · 修订: 2026-07-21
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI) · 审查: GPT-5.6-Sol (via Codex CLI)
> 基于: 项目 README/CLAUDE.md/src 全量源码 + project_status.md
> 审查报告: `_review/conclusions/GPT-5.6-Sol_fork-directions-review_2026-07-21.md`
>
> 📖 **其他语言版本**: [正體中文](../zh-Hant/fork-modification-directions.md) | [English](../en/fork-modification-directions.md)

## 项目现状速览

- **核心**: 从 3836 行 ETF 形态匹配策略 V3.3 提取纯计算模块，pybind11 + C++20 加速
- **加速**: DTW 单次 34× (96µs→2.8µs) / 形态匹配单次 53× (14.0ms→0.26ms) / 批量接口开销缩减 2.2× (100 次 C++ 单次调用 → 1 次 C++ 批量调用)；Python batch vs C++ batch 端到端约 93×（见 benchmark JSON）
- **算法**: 余弦预筛选 → DTW 精排 → 综合得分(0.5×norm_dtw + 0.5×norm_cos) → 15 维特征
- **模块**: 6 个 Python 纯计算模块 + 1 个 C++ 统一加速模块(8 函数，~1100 行)
- **测试**: 54 单元测试 + 2 验证脚本 + 交互 Notebook
- **工具链**: MSVC 19.51 + pybind11 3.0.4 + C++20 + CMake 3.20+
- **许可证**: MIT（仅覆盖本仓库发布的代码；外部 SDK、数据源、第三方模型须单独核查许可）
- **明确排除**: 实盘交易代码、掘金 SDK 绑定、回测结果/绩效声明（本仓库不提供这些结论；fork 可新增相关功能，但须独立标注数据来源、样本区间、交易成本假设和验证方法）

---

## 前置知识假设

本文档假设 fork 贡献者：
- 熟悉 Python/NumPy 和 C++ 基础
- 了解 pybind11 的基本概念（GIL 管理、`py::array_t`、`py::object`）
- 能阅读 CMake 构建配置
- 对量化金融中"前视偏差""时序交叉验证""交易成本"有基本认知

对于标注"需要外部资料"或"需要平台访问"的方向，文档会显式列出阻塞项。**开工前请先阅读各方向的前置条件——标注为"低"或"中"改动量的方向也可能有未解决的前置依赖。**

---

## 一、算法内核方向

### 1.1 DTW 变体替换

当前使用标准 DTW + Sakoe-Chiba band(window=5)。`dtw_distance_span()` 是纯函数，接口清晰——替换距离度量是最低门槛的 fork。

| 变体 | 适用场景 | 实现复杂度 | 关键风险 |
|------|---------|-----------|---------|
| **Derivative DTW (DDTW)** | 匹配形态"形状"而非绝对水平，先对序列差分再 DTW | 低(预处理即可) | 差分放大噪声；需验证短序列(L≈19)上的数值稳定性 |
| **Weighted DTW** | 对近期数据点加权，匹配"近期更重要"的市场直觉 | 低(DP 递推式加权重因子) | 权重衰减率是额外超参；窗口边界处权重不连续 |
| **Soft-DTW** | 数值可微（数学上）；但**当前 pybind11 函数返回 NumPy/float，不携带自动微分图**——若要用于训练，需额外实现 PyTorch custom autograd、JAX custom VJP 或采用现有可微 DTW 库 | 中(需改 DP 递推式为 softmin + 微分框架适配) | 可微性 ≠ 训练就绪；需梯度数值验证；γ 参数敏感 |
| **ShapeDTW** | 先提取局部形状描述符(subsequence→descriptor)再 DTW | 中(需新增描述符提取模块) | 描述符选择无通用标准；L_query=20 下子序列极短 |
| **FastDTW** | 近似线性时间 O(L)；**适用于 L_query 本身较长(数百点以上)的场景**；若仅增加 T_back(候选数量增多)，应优先评估候选索引和剪枝，而非替换 DTW 算法 | 中(粗化→投影→细化三层递归) | 近似误差 vs Top-K 稳定性需单独 benchmark；当前 L_query=20 时 FastDTW 优势有限 |

**入口点**: C++ `src/cpp/etf_core.cpp` `dtw_distance_span()`(行 ~150-180)；Python 参考 `src/core/dtw.py`。改动算法后须同步 Python 参考实现并通过 `verify_etf_core.py` 一致性验证。

**验收标准**: (a) `verify_etf_core.py` 全 PASS；(b) 新增 DTW 变体的独立单元测试；(c) benchmark 比较变体与标准 DTW 的速度和 Top-K 召回率。

### 1.2 综合得分公式重设计

当前: `combined_score = 0.5 × norm_dtw + 0.5 × norm_cos`，等权 min-max 归一化后合并。

可替换为:
- **自适应权重**: 根据 cos 候选分布(如基尼系数)动态调整 DTW/Cos 权重
- **秩聚合**: 用 Spearman footrule 距离或 Borda count 替代加权平均
- **帕累托前沿**: 不合并，保留 DTW 和 Cos 两个维度，在二维空间中选取非支配解
- **概率校准**: 用历史匹配的**历史后续收益统计**校准相似度得分（注意：此为统计特征而非预测概率——详见 §关键约束与注意点 术语说明）

**入口点**: C++ `src/cpp/etf_core.cpp:551–707`（`pattern_match_core()`，其中 `Scored` 结构体和综合得分位于 680–690 行）；Python 参考 `src/core/pattern_match.py:192–200`。

### 1.3 多变量形态匹配

当前仅基于标准化收益率序列(1 维)做匹配。扩展为多维:
- 同时匹配: 价格趋势 + 成交量模式 + 波动率形态 + ADX 方向
- DTW 从一维扩展到多维: `cost = Σⱼ wⱼ × (x[i][j] - y[i][j])²`
- 距离聚合策略: 加权和 / Pareto 前沿 / 马氏距离归一化各维度后再 DTW

**入口点**: `dtw_distance_span()` 当前只接受 `const double*`，改为多维需同时修改函数签名和 DP 递推式。需新增 C++ 多维数组输入接口和 Python 端数据组装逻辑。

### 1.4 候选检索加速

当前余弦预筛选是全量扫描(`for hist_end in range(search_start, search_end+1, match_step)`)。可用:
- **k-NN 索引**: FLANN / HNSW / FAISS 对历史窗口收益率向量建索引——有可证明的召回率保证
- **近似索引(LSH)**: 明确标注召回率与速度的 trade-off，附带 Top-K 召回率测试
- **分块点积上界剪枝**: 预先计算范数，使用部分累积点积上界安全剪枝——**不同于简单的"找到满意结果就停止"**（后者会改变 Top-K 结果，属于近似搜索而非安全剪枝）

每种检索方式均应测试: Top-K 召回率、综合得分变化、15 维特征稳定性、端到端速度。

**入口点**: `pattern_match_core()` 中"第 1 遍: 余弦相似度"的 for 循环

---

## 二、加速平台方向

### 2.1 GPU 加速(CUDA/ROCm)

DTW 的批量计算天然适合 GPU: `dtw_distance_batch` 将一个 query 对 N 个 candidate 做一对多循环，可映射到 CUDA kernel。

- **CUDA C++**: 替换 `pattern_match_core` 的 CPU 循环为手写 kernel
- **cuBLAS**: 余弦相似度计算可转为矩阵乘法(candidates × query = batched dot product)
- **性能预期**: 批量场景下端到端加速比**待验证**——需在明确 n_samples、候选数、序列长度的条件下分别测量 host→device 传输、余弦、DTW、排序、特征聚合各阶段耗时，以当前 Python 版本为数值和结果基线
- **挑战**: `pattern_match_core` 中的控制流(`if cos_s > 0`, `if fut_end < T_idx`)在 GPU 上需要 warp-level 分支处理；host-device 数据传输和 Python API 边界可能成为主导开销

**入口点**: `dtw_distance_batch()` 和 `pattern_match_core()` 中的循环段。

**验收标准**: (a) 与当前 Python/C++ 参考实现数值一致(浮点容差 1e-6)；(b) 分阶段 benchmark 报告；(c) CPU fallback 路径；(d) Top-K 和 15 维特征一致性测试。

### 2.2 SIMD 向量化

当前 C++ 代码无显式 SIMD。SIMD 友好热点:
- `cosine_similarity_vec()` 的点积循环 → `_mm512_fmadd_pd`
- `dtw_distance_span()` 内层循环 → 可向量化但受限于 DP 的数据依赖
- `standardize_returns_cpp()` 的 `std::accumulate` → SIMD reduce
- 需调整数据结构为 **SoA**(Structure of Arrays)以获得连续内存访问

**关键——CPU 能力分发**: 直接以 `/arch:AVX512` 编译会导致无 AVX512 的 CPU 无法运行。应实现:
- CPUID 运行时检测
- AVX512 / AVX2 / 标量多级 fallback
- 不同 CPU 的分别 benchmark
- SIMD 与标量结果误差测试（FMA 和 reduction 顺序可能导致浮点差异，需验证是否在 1e-8/1e-6 容差内）

**编译选项**: MSVC `/arch:AVX512`（仅 AVX512 路径）/ GCC `-mavx512f` / 手写 intrinsics with runtime dispatch。

### 2.3 多线程批量处理

当前 `pattern_match_batch` 对多个 T_idx 的循环是串行的(GIL 已释放但无多线程)。

**推荐安全模式**（避免数据竞争和结果顺序错乱）:
1. 工作线程只写 C++ 数据，不创建 Python 对象
2. 为每个 sample 预分配固定位置（如 `features[n_samples][15]`）
3. 每个线程只写自己的 sample 槽位
4. `valid_mask` 与特征矩阵按输入 `t_indices` 顺序保持一致
5. 主线程重新获取 GIL 后**统一**创建 NumPy 返回对象
6. 增加并发正确性、输出顺序稳定性和异常安全测试

**不推荐模式**: 在工作线程中 `gil_scoped_acquire` + 直接创建 Python 对象——会引入生命周期、线程安全、异常传播和 Python allocator 竞争问题。

**入口点**: `pattern_match_batch()` 中 `for (py::ssize_t s = 0; s < n_samples; ++s)` 循环。

### 2.4 pandas → Arrow 零拷贝

当前 `py::array_t<double>` 对 **float64、C-contiguous** 的 NumPy 数组可避免额外复制。但以下情况可能触发拷贝:
- dtype 不匹配时 `forcecast` 转换
- 非连续数组（Fortran-contiguous、slice/strided view）
- pandas DataFrame → NumPy 的隐式转换（取决于底层数据布局和 dtype）

Arrow 集成需新增适配层，不是仅替换调用入口。建议: 先 benchmark 验证当前方案中数据搬运占总耗时的比例，再决定是否值得引入 Arrow 依赖。

---

## 三、策略系统方向

### 3.1 接回回测框架

**前置条件**: 当前项目是"纯计算模块，不含平台绑定"。**开工前需明确以下阻塞项**:
- 原始 V3.3.py 完整文件**不在本仓库内**
- 原始训练数据、模型文件、标签定义**不在本仓库内**
- 原始回测配置（时间范围、交易成本、滑点、停牌规则）**不在本仓库内**

Fork 可在满足前置条件后接入:

| 框架 | 方式 | 难度 | 关键挑战 |
|------|------|------|---------|
| **backtrader** | 将 `pattern_match_single` 封装为 `bt.Indicator` 子类 | **中¹** | T_idx 与框架 bar 索引映射、warm-up 阶段、周频调仓 vs 日频 bar、严格因果性验证 |
| **vnpy** | 实现 `CtaTemplate`，在 `on_bar()` 中调用 C++ 模块 | 中 | 需平台 API 文档和测试环境 |
| **zipline-reloaded** | 实现 `CustomFactor`，pipeline API 风格 | 中 | pipeline 语义与 15 维特征的适配 |
| **bt**(Python) | `Algo` 子类，固定周期调用 `pattern_match_batch` | **中¹** | 同上 backtrader 挑战 |
| **掘金平台** | 逆向补回平台绑定层，恢复原始 V3.3 的完整可运行策略 | **高**(需外部资料) | 原始文件不在仓库内；需掘金 SDK 和平台账号 |

> ¹ 原稿标为"低"，审查指出需处理 GIL + C++ 对象生命周期 + 多 ETF 数据组织 + 无前视测试，实际为中。

核心价值: 让 "C++ 加速的计算核心" 从独立 demo 变成可回测、可评估的策略。**输出应标注"具备接入回测框架的能力"，而非"可投产"。** 完整投产需补齐执行层、交易成本建模和样本外验证。

### 3.2 多 ETF 截面轮动

原始 V3.3 是"多头轮动策略"——在 ETF 池中根据形态信号选最优。当前项目只提供单 ETF 的特征提取。Fork 需分两阶段:

**阶段一（可并行）**: 每个 ETF 独立生成 15 维特征。当前 `pattern_match_batch()` 只接受单个 ETF 的一维 `prices` 和一组 `t_indices`——需新增多 ETF 批量输入接口（不同 ETF 可能有不同序列长度和缺失值策略）。

**阶段二（不可简单并行）**: 收集所有 ETF 特征后，做截面 rank/z-score 标准化、排序和持仓决策。此阶段依赖全部 ETF 的结果，不是各 ETF 间独立任务。

- **截面可比性**: 不同 ETF 的 15 维特征在截面上 rank / z-score 标准化
- **排序层**: LambdaRank / XGBoost ranker 学习 F1-F15 到持仓权重的映射
- **轮动周期**: 周频再平衡(与原始策略一致)
- **交易成本建模**: 冲击成本 + 佣金 + 印花税

### 3.3 风控执行层

当前项目中的风控相关代码分布在多个模块——**不是单一风控系统**:

| 功能 | 实际位置 | 当前状态 |
|------|---------|---------|
| 滚动波动率风控(分位数减仓) | `src/core/risk_controls.py` | ✅ 已实现 |
| MA 趋势过滤 | `src/core/risk_controls.py` | ✅ 已实现 |
| 仓位上限约束 | `src/core/risk_controls.py` | ✅ 已实现 |
| ATR | `src/core/technical.py` / C++ 模块 | ✅ 已实现 |
| 最大回撤 | `src/core/metrics.py` | ✅ 已实现 |
| VaR | — | ❌ 未实现 |
| 止损/止盈触发 | — | ❌ 未实现 |
| 仓位再平衡调度器 | — | ❌ 未实现 |
| 最大回撤熔断(账户+ETF双层) | — | ❌ 未实现 |

Fork 可添加的**执行层**（区别于现有的**计算层**）:
- 止损/止盈触发: trailing stop / time stop / volatility stop
- 仓位再平衡调度器: 偏离目标权重超过阈值 → 触发调仓
- 黑名单: 连续 N 次形态匹配失败 → 该 ETF 暂停交易
- 最大回撤熔断: 账户级别和 ETF 级别双层限制

### 3.4 信号服务器(微服务化)

建议拆为两层——当前 `etf_core` 输出的是 15 维特征，不是交易信号:

**计算服务**（与当前模块直接对应）:
- HTTP/gRPC 接收价格数据 → 返回 15 维特征 + 版本信息
- Redis 缓存预计算窗口和中间结果
- 定义 API schema、参数版本、数据时间戳、缓存失效策略

**策略服务**（需额外实现）:
- 输入多个 ETF 的特征 → 执行排序、风控和调仓规则 → 输出信号及解释
- 信号阈值、持仓规则、调仓周期、交易成本、执行状态

**技术选型**: FastAPI + uvicorn 即可快速原型；任何语言可通过 HTTP/gRPC 调用(Python/C++/Go/Rust)。

---

## 四、语言生态拓展方向

### 4.1 Rust + PyO3 重写

保持相同 Python API，用 Rust 实现计算核心:
- `numpy` crate 零拷贝互操作(对标 `py::array_t`)
- 所有权系统避免 C++ 的内存管理陷阱
- `rayon` crate 替代 OpenMP 做并行
- 对比 pybind11 vs PyO3 的 DX(Developer Experience)差异

### 4.2 Numba/Cython 纯 Python 加速

为不想装 C++ 编译器的用户提供替代方案:
- **Numba CPU JIT**: `@jit(nopython=True)` 装饰核心循环，加速 CPU 端计算
- **Numba CUDA**: 需显式使用 `@cuda.jit` 和 CUDA Array API，重新设计 kernel、线程布局和内存访问——**不是 `@jit` 自动获得 GPU 加速**
- **Cython**: 在 `.pyx` 中声明 C 类型，构建更简单(无需 CMake)但性能接近 C++
- 与 C++ 版本的性能对比需在相同硬件和输入下分别 benchmark

### 4.3 其他语言绑定

**前置条件——当前 C++ 核心不是独立于 Python 的纯 C++ 库。** 它大量直接依赖 pybind11 类型: `py::array_t`、`py::object`、`py::dict`、`py::tuple`、`py::gil_scoped_release` 等。因此不能"只需新绑定层"。

**阶段一: 核心抽象**（先决条件）:
- 抽取不依赖 pybind11 的 C++ 算法库
- 使用 `std::span`、裸指针+长度或独立 C ABI
- 定义错误码、内存所有权和线程安全规则
- 保留现有 pybind11 作为 Python 适配层

**阶段二: 语言绑定**（在阶段一完成后）:
- **R 绑定**(Rcpp): 量化金融领域 R 用户群大，`Rcpp::NumericVector` ↔ C ABI 概念对应
- **Node.js**(node-addon-api): Web 量化平台常用 Node 后端
- **WASM**(Emscripten): 浏览器内运行，配合 Streamlit/Observable 前端
- **Go**(cgo): 高性能微服务场景

> 注意: R/Node/WASM/Go 四条路径的工作量和风险独立且差异大，不建议合并为单一"中等"项目评估。

---

## 五、特征工程方向

### 5.1 F16-F21 特征集成

**当前实际实现状态**（非文档声称的"6 个市场环境特征"）:

| 特征 | 功能 | 位置 | 状态 |
|------|------|------|------|
| F16 | 近 20 日市场波动率 | `src/core/market_features.py` `compute_market_volatility()` | ✅ 已实现 |
| F17 | 大小盘相对强度 | `src/core/market_features.py` `compute_size_relative_strength()` | ✅ 已实现 |
| F18 | — | — | ❌ 未实现 |
| F19 | — | — | ❌ 未实现 |
| F20 | 成交量异常 | `src/core/market_features.py` `compute_volume_anomaly()` | ✅ 已实现 |
| F21 | 波动率变化 | `src/core/market_features.py` `compute_vol_change()` | ✅ 已实现 |

板块轮动逻辑位于 `src/core/technical.py`（`compute_sector_rotation()`），独立于 `market_features.py`。"市场宽度"和"资金流"在当前代码中无对应实现。

因此将 15 维扩展为 21 维不是简单拼接，而是至少包含:
1. F18/F19 的定义或恢复（需确定指标含义和数据源）
2. 各模块特征 ID 的对齐
3. 外部数据输入设计（部分特征依赖非价格数据）
4. Python 与 C++ 双端实现
5. 21 维输出契约和 `FEATURE_KEYS` 更新

**前置条件**: 确定 F18/F19 的定义、数据源、频率和时间对齐规则。

### 5.2 新增特征类别

| 类别 | 示例特征 | 数据依赖 |
|------|---------|---------|
| 波动率曲面 | ATM IV、偏度、期限结构斜率 | 期权数据（需数据源+许可） |
| 宏观因子 | 利率期限结构、信用利差、VIX、美元指数 | 多源宏观数据（频率/时区/交易日历各不同） |
| 资金流 | ETF 净流入/流出、大单资金流向 | 资金流数据（商业数据源，许可限制） |
| 相关性 | 与基准 ETF(如 SPY/510050)的滚动相关性 | 基准 ETF 价格数据 |
| 流动性 | Amihud 非流动性指标、买卖价差 | 日内数据（频率远高于日频） |

**数据契约要求**（每个数据相关方向均应明确）:

| 字段 | 说明 |
|------|------|
| 数据源 | 具体服务或文件格式 |
| 频率 | 日频/分钟/实时 |
| 时区 | UTC/北京时间等 |
| 可用时间 | 收盘后/盘中/T+1（防止前视偏差） |
| 缺失策略 | 丢弃/前值/插值 |
| 许可 | 是否允许商业使用和再分发 |
| 防前视 | 数据实际可获得时间 vs 信号生成时间 |

### 5.3 特征交互与自动选择

- **交互项**: F1×F6(高相似度 + 高历史后续收益的联合信号)、F3×F12(相似度衰减 × 时间跨度)
- **Boruta / SHAP**: 特征重要性分析和约简
- **RFE**(递归特征消除): 找到最小有效特征子集
- **遗传编程**: 自动生成非线性特征组合

---

## 六、ML 增强方向

### 6.1 恢复原始 ML Stacking

**前置条件（阻塞项）**:
- 原始 V3.3 的 RF/SVM 训练代码、模型参数和训练数据**不在本仓库内**
- 原始标签定义、特征工程步骤和交叉验证方案需从归档基线恢复
- 时序交叉验证(purged k-fold)的具体实现需独立设计

原始 V3.3 做了 RF/SVM Stacking → 15 维特征 → 综合信号。在满足前置条件后，Fork 可:
- 恢复 RF+SVM 两层 Stacking
- 升级为 XGBoost + LightGBM + CatBoost Stacking(三模型投票)
- 添加深度学习层(LSTM/Transformer 替代 DTW 做序列匹配)
- **关键**: 时序交叉验证(purged k-fold)防止前视偏差
- **验收**: 样本外测试集上的风险调整后收益 + 与原始 V3.3 的对比（如有原始结果）

> 标注为"需要外部资料"——不完全依赖外部不代表可以忽略前置条件。此方向的实际开工门槛远高于"高改动量"的标签。

### 6.2 参数自适应/在线学习

当前所有参数(L_query=20, T_back=750, M_forward=5, k=10, cos_prefilter_top=50)硬编码。
- **Walk-forward 优化**: Optuna/Hyperopt 在滚动窗口上做超参搜索
- **在线自适应**: EWMA 更新 `cos_prefilter_top`(市场波动大 → 减少候选，波动小 → 增加候选)
- **Regime 切换**: 检测波动率 Regime → 切换参数集(高波动参数组 vs 低波动参数组)

### 6.3 强化学习持仓管理

将形态匹配作为状态编码器，强化学习做持仓决策:
- **State**: 15 维特征 + 当前持仓 + 账户状态
- **Action**: 调仓方向(增加/减少/清仓 ETF)
- **Reward**: 风险调整后收益 + 交易成本惩罚
- 形态匹配提供特征提取，RL 提供决策规则——两个系统的接口是 15 维特征向量

---

## 七、资产类别扩展

### 7.1 加密货币

加密市场与 ETF 有截然不同的微观结构:
- 24/7 交易、无涨跌停 → 需调整 M_forward 和 T_back 参数(更高频)
- 永续合约 → funding rate 可作为额外特征（注意数据源许可）
- 缺失数据处理: 交易所宕机 / 数据源不连续

### 7.2 A 股个股

从 ETF 扩展到个股需额外处理:
- 停牌/涨跌停/ST 导致的缺失数据 → 需增强 `standardize_returns_cpp` 的健壮性
- 除权除息 → 前复权价格处理
- 行业中性化 → 个股形态相似性可能仅是行业 β，需截面去均值

### 7.3 跨资产类别

- **商品期货**: 期限结构特征 + contango/backwardation
- **外汇**: 利差 + 央行政策日历
- **可转债**: 转股溢价率 + 纯债价值

> 以上方向均涉及外部数据源——参照 §5.2 数据契约要求。

---

## 八、基础设施方向

### 8.1 预编译 Wheel 分发

**前置条件（开工前须解决）**:
1. **Python 版本矛盾**: `pyproject.toml` 声明 `requires-python = ">=3.10"`，但顶层 `CMakeLists.txt` 使用 `find_package(Python 3.12 REQUIRED ...)`——Python 3.10/3.11 无法通过 CMake 构建。须统一: 要么限制为 Python 3.12+，要么修改 CMake 兼容声明版本矩阵。
2. **包布局**: `wheel.packages = ["src/cpp"]` 未显式包含 `src/core`（Python 参考实现），需明确打包范围。
3. **验证**: 在 clean virtualenv 中验证 `pip install dist/*.whl && python -c "import etf_core"`。

Fork 可在解决前置条件后:
- **cibuildwheel**: 构建 Windows/Linux/macOS × x86_64/ARM64 全平台 wheel（注意: 当前 CI 虽覆盖三平台但仅测 Python 3.12，不等于已验证全矩阵）
- **PyPI 发布**: `pip install etf-core` 一行安装
- **conda-forge**: conda 生态分发

**验收条件**: 构建成功 + 安装成功 + `import etf_core` 通过 + `import core` 可导入 + 类型 stub 可用 + 至少 smoke test 通过。

### 8.2 实时数据管线

从"离线批量跑特征"变成"每日自动信号生成":
- WebSocket 实时数据(AKShare/Tushare/Binance)——注意各数据源的许可和再分发限制
- Redis 缓存预计算窗口(避免重复标准化)
- Cron/Airflow 定时任务: 每日收盘后自动生成 signals
- 消息推送: Slack/DingTalk/企业微信

**数据契约**: 参照 §5.2 数据契约要求——频率、时区、可用时间、缺失策略、防前视。

### 8.3 性能回归监控

在现有 `benchmarks/` 框架上扩展:
- CI 中自动比较不同 commit 的 benchmark JSON
- 单边减速阈值 → 自动告警
- 多硬件基线(不同 CPU 世代的参考值)

---

## 九、学术/教育方向

### 9.1 交互式可视化平台

**前置条件**: 当前 `pattern_match_single()` 主要返回 15 维聚合特征字典——没有稳定的公开接口返回候选窗口索引、每个候选的 cosine/DTW/综合得分/历史后续收益/DTW 对齐路径。可视化 Top-5 匹配和 DTW path 需先新增可选 debug/trace API。

将 Jupyter Notebook 扩展为完整体验:
- **Streamlit/Gradio Web App**: 选 ETF → 调参数 → 看历史 Top-5 匹配 → 看后续表现
- **Plotly 可视化**: 查询窗口与匹配窗口叠加图 + DTW 对齐路径热力图
- **参数沙盒**: 实时调整 L_query/T_back/k 等参数并观察结果变化

**前置 API 需求**（建议先于可视化工作完成）:
```python
pattern_match_single(..., return_details=True)
# 返回: query_range, candidate_ranges, cosine_scores,
#        dtw_distances, combined_scores, future_returns, dtw_paths
```
同步更新 `src/cpp/pyi/etf_core.pyi`、Python 参考实现、C++ 实现和测试。

### 9.2 DTW 变体系统基准测试

纯学术 fork:
- 在统一数据集上跑标准 DTW / Soft-DTW / DDTW / Weighted DTW / ShapeDTW / FastDTW
- 比较维度: **历史匹配窗口后续收益统计** + 计算速度 + 参数敏感性
- 现有 `benchmarks/run_benchmark.py` + JSON 结果格式天然支持多算法对比
- 产出: 一篇方法论比较文章或技术报告

### 9.3 算法可视化教材

将 15 维特征(F1-F15)每个维度做成独立可视化:
- 高相似度→高收益的 case vs 高相似度→低收益的 case，形成对比教学
- DTW 对齐路径的动态演示(animations)
- "形态匹配失败"的典型案例分析

---

## 十、方法论改进方向

### 10.1 复现原始 V3.3 性能

**⚠️ 外部资料阻塞——开工前必须获得**:
- [ ] 原始 V3.3.py 完整文件（含掘金平台绑定和策略逻辑）
- [ ] 原始训练数据（或等效数据集 + 数据版本）
- [ ] RF/SVM 模型超参数和序列化文件（如有）
- [ ] 原始回测配置（时间范围、交易成本、滑点、停牌规则）
- [ ] 原始回测结果统计口径（用于对比验证）
- [ ] 掘金 SDK 和平台账号

当前项目明确说"不能重跑原始回测，不含完整平台绑定策略"。在获得上述资料前，此方向无法独立开工。一旦获得资料，这是典型的学术复现研究——对理解策略真实有效性有方法论价值。

### 10.2 审查方法论泛化

本项目的核心方法学价值在于其**审查流程**(多轮跨后端审查 + 0 回归)。Fork 将这套 SOP 应用于:
- 其他量化策略的 C++ 加速 → 通用框架: 提取纯计算 → pybind11 加速 → 跨后端一致性验证
- 不同加速方式之间的对比审查(C++ vs Rust vs Numba vs 纯 NumPy)
- 建立 "AI 辅助量化策略代码审查 checklist"

### 10.3 与原始策略的差异量化

定量分析提取前后的差异:
- 在相同输入下，C++ 版本的输出与 Python 版本的浮点级差异分布
- 这些差异在策略层面的累积效应(是否影响最终的持仓决策?)
- 这是 "AI 辅助代码迁移保真度" 研究的一个案例

---

## 十一、正确性与跨后端契约验证

> 此方向由 GPT-5.6-Sol 审查提出——项目的独特优势不仅是 C++ 加速，还包括 Python 参考实现 + 严格一致性验证 + 54 测试 + 多后端审查流程。当前方向列表偏重性能和功能，遗漏了正确性验证这条独立线索。

将本项目的验证体系泛化为可复用的 fork 方向:
- **Property-based testing**: 使用 Hypothesis 生成随机输入(含 NaN/Inf/零长度/常数序列/非连续数组/dtype 变化)，验证 Python/C++/替代后端在数值、异常和返回结构上的一致性
- **模糊测试**: 随机输入 + 固定种子，跨后端差分测试
- **边界输入目录**: 零长度序列、单元素、常数序列、全 NaN、极大/极小值、非连续布局
- **跨后端一致性矩阵**: Python vs C++ vs Rust vs Numba vs Cython——统一的数值容差(距离 1e-8, 得分 1e-6)、异常语义和返回结构契约
- **回归测试自动化**: 每次算法改动自动触发全量一致性验证

**关联文件**: `src/core/dtw.py`、`src/core/pattern_match.py`、`src/cpp/etf_core.cpp`、`src/cpp/pyi/etf_core.pyi`、`verify_etf_core.py`、`verify_batch.py`、`tests/`

---

## 按实现门槛与外部依赖排序的 Fork 方向

> 排序逻辑: 先按"可直接开工"分组，组内按改动量排序。"可直接开工" = 所有入口文件和数据在本仓库内可用 + 无需外部平台/账号。

### 可直接开工

| 方向 | 改动量 | 技术风险 | 验收清晰度 | 独立价值 | 入口文件 |
|------|--------|---------|-----------|---------|---------|
| DTW 变体替换(DDTW/Weighted DTW) | 低 | 中 | 高 | 中 | `src/cpp/etf_core.cpp` `dtw_distance_span()` |
| 候选检索加速(剪枝/索引) | 低-中 | 中 | 中 | 中 | `pattern_match_core()` 余弦循环 |
| 得分公式重设计 | 低-中 | 中 | 中 | 中 | `etf_core.cpp:680–690` |
| 多线程并行化批量 | 中 | 高(数据竞争) | 高 | 中 | `pattern_match_batch()` 循环 |
| 正确性与跨后端契约验证 | 中 | 中 | 高 | 高 | `verify_etf_core.py` + `tests/` |

### 需要外部资料或平台

| 方向 | 改动量 | 外部依赖 | 技术风险 | 独立价值 | 阻塞项 |
|------|--------|---------|---------|---------|--------|
| Streamlit 可视化 Web App | **中¹** | 无 | 中 | 高 | 需先实现 debug/trace API(§9.1) |
| 预编译 Wheel + PyPI 发布 | **中¹** | 无 | 中 | 高 | Python 版本矛盾 + 包布局(§8.1) |
| 接回回测框架 | 中 | 回测框架 | 中 | 高 | 原始数据/配置不在仓库内 |
| 扩展到加密货币/A股个股 | 中 | 新市场数据源+许可 | 中 | 中 | 数据契约待确定 |
| 风控执行层(止损/熔断/调度) | 中 | 无 | 中 | 中 | 需先明确与计算层的接口 |
| 信号服务器(计算服务层) | 中 | 无 | 中 | 中 | 需定义 API schema |
| F16-F21 完整集成 | 中-高 | F18/F19 定义+数据源 | 中 | 中 | 缺失特征定义和数据 |
| 多 ETF 截面轮动 | 高 | 回测框架+交易成本模型 | 高 | 高 | 需多 ETF 批量接口 + 截面排序层 |
| 多语言绑定(R/Node/WASM/Go) | **高¹** | 无 | 高 | 中 | 需先抽取不依赖 pybind11 的 C ABI 核心(§4.3) |
| GPU 加速(CUDA) | 高 | CUDA 工具链+硬件 | 高 | 高 | 无;但 10-20× 为待验证假设 |
| ML Stacking 恢复 | 高 | 原始代码/数据/模型 | 高 | 高 | 原始文件不在仓库内 |
| SIMD 向量化 + SoA | 高 | 无 | 高 | 中 | CPU 分发+数值一致性待设计 |
| 复现原始 V3.3 完整策略 | 高 | 原始文件+掘金 SDK+数据 | 很高 | 高 | **外部资料阻塞——无法独立开工** |
| 强化学习持仓管理 | 高 | RL 框架+回测环境 | 高 | 中 | 需回测框架就绪 |
| 实时数据管线 | 中-高 | 数据源+消息推送服务 | 中 | 中 | 数据源许可+可用时间待确认 |

> ¹ 原稿标为"低"或"中-"，审查后上调（Streamlit 需前置 debug API，Wheel 有构建配置矛盾，多语言绑定需架构重构）。

### 纯学术/教育方向（独立价值以学术意义为主）

| 方向 | 改动量 | 外部依赖 | 产出类型 |
|------|--------|---------|---------|
| Numba/Cython 加速对比 | 中 | 无 | 技术报告/博客 |
| DTW 变体系统基准测试 | 中 | 无 | 方法论比较文章 |
| Rust + PyO3 重写对比 | 高 | 无 | 工程对比报告 |
| 算法可视化教材 | 中 | 需 debug API | 教学材料 |
| 审查方法论泛化 | 低(文档为主) | 无 | SOP 框架 |
| 与原始策略差异量化 | 中 | 原始 V3.3 归档 | 保真度研究 |

---

## 关键约束与注意点

### 许可证与外部依赖边界

1. **MIT 许可证**仅覆盖本仓库发布的代码。以下不在 MIT 覆盖范围内，须单独核查许可:
   - 掘金 SDK 及平台服务条款
   - AKShare / Tushare / Binance 等外部数据源（含商业使用限制）
   - 历史行情数据的再分发权利
   - 原始策略中不属于本仓库的文件
   - 第三方模型（如 XGBoost/LightGBM 训练出的模型文件）和依赖库

2. **无掘金 SDK**: 原始平台绑定不在仓库内，任何"恢复完整策略"的 fork 需自行处理平台适配和许可。

3. **单平台基准测试**: 当前 benchmark 数值(34×/53×/2.2×/93×)来自 Windows + MSVC，不同平台/编译器需重新校准。

### 术语约定

为避免从"历史统计特征"到"策略预测能力"的过度推断，本文档使用以下术语区分:

| 术语 | 含义 | 不等于 |
|------|------|--------|
| **历史匹配片段后续收益** | 历史匹配窗口在其后 M_forward 个时间点的收益统计（即当前 F6-F11 的本质） | 未来收益 / 策略收益 |
| **历史统计特征** | 基于历史数据计算的描述性指标 | 预测信号 |
| **模型预测** | 经时序交叉验证和样本外测试的 ML 模型输出 | 未经校准的统计值 |
| **回测实现收益** | 在明确交易成本、滑点和执行规则下的回测结果 | 实盘收益 |
| **交易后净收益** | 扣除全部成本后的实现收益 | 回测模拟收益 |

"可投产""策略提升""验证原始性能"等表述在本文档中均指**在补齐执行层、交易成本建模和样本外验证后的可能性**，非对当前仓库代码的绩效声明。

### 浮点与契约

4. **15 维特征顺序**: `etf_core.FEATURE_KEYS` 已固定为模块常量，修改特征须同步更新该常量 + 所有引用处。

5. **GIL 释放边界**: 添加新函数时注意 `py::gil_scoped_release/acquire` 的正确位置。**工作线程不应直接创建 Python 对象**——详见 §2.3 和 CLAUDE.md。

6. **浮点容差**: C++ vs Python 一致性验证的容差标准(距离 1e-8, 得分 1e-6)，改动算法后需重新验证。**SIMD/GPU 等改变计算顺序的优化可能破坏此容差**——性能验收和数值验收须分开。

---

## 关联文件

### 源码
- `src/cpp/etf_core.cpp` — 全部 C++ 加速逻辑(~1100 行，注释详细)
- `src/cpp/pyi/etf_core.pyi` — C++ 类型存根(API 契约)
- `src/core/dtw.py` — DTW 距离 + 序列标准化(Python 参考)
- `src/core/pattern_match.py` — 形态匹配引擎 15 维特征(Python 参考)
- `src/core/technical.py` — ADX / ATR / 板块轮动
- `src/core/market_features.py` — F16/F17/F20/F21 市场环境特征
- `src/core/risk_controls.py` — 滚动波动率分位数 / MA 趋势 / 仓位上限
- `src/core/metrics.py` — Sortino / Calmar / 最大回撤 / IC 统计

### 构建与 CI
- `pyproject.toml` — Python 构建配置(scikit-build-core)
- `CMakeLists.txt` — 项目构建配置(顶层)
- `src/cpp/CMakeLists.txt` — C++ 模块构建配置
- `.github/workflows/ci.yml` — 三平台 CI(Windows/Linux/macOS, Python 3.12)
- `.github/workflows/benchmark.yml` — 性能回归 CI
- `.github/workflows/sanitizer.yml` — ASAN+UBSAN CI

### 测试与验证
- `tests/test_dtw.py` — DTW 模块测试(27 项)
- `tests/test_pattern_match.py` — 形态匹配测试(15 项)
- `tests/test_technical.py` — 技术指标测试(12 项)
- `tests/test_etf_core.cpp` — C++ 原生测试(58 cases)
- `verify_etf_core.py` — C++ vs Python 一致性验证
- `verify_batch.py` — 批量形态匹配验证

### 文档
- `CLAUDE.md` — pybind11 实战经验、GIL 管理、ABI 排错
- `project_status.md` — 审查链谱系、会话历史
- `benchmarks/run_benchmark.py` — 可复现基准测试
- `benchmarks/results/` — 历史 benchmark JSON
