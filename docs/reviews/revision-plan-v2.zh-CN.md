# 形态匹配ETF策略 — Python+C++混合编程重构优化计划 v2

> **模型 provenance**: DeepSeek-V4-Pro (via Claude Code CLI)，2026-07-03
> **状态**: 经异后端双审修订
> **审查**: Kimi-K2.7-Code（魔鬼代言人）+ GPT-5.5 via Codex CLI（完备性），2026-07-03

---

## v2 修订摘要（相对 v1）

| # | 来源 | 修订内容 |
|---|------|---------|
| 1 | Kimi | 加速比预期全面下调（DTW单次 10-30x→3-8x，ADX 3-5x→1.5-3x，整体训练 1.6-2.5x） |
| 2 | Kimi+GPT | 三个独立pybind11模块合并为**一个**`etf_core`模块 |
| 3 | GPT | 新增`pattern_match_batch`批量接口——训练样本生成的核心加速点 |
| 4 | GPT | 新增滚动窗口收益率预计算优化 |
| 5 | Kimi+GPT | 新增强制pybind11契约（dtype/layout/返回结构/异常语义/NaN策略） |
| 6 | Kimi | 浮点容差分两层：距离<1e-8，综合得分<1e-6 |
| 7 | GPT | 测试扩展：F12-F15固定样例、真实NaN边界、全量generate_training_samples一致性 |
| 8 | Kimi | 修复V3.3.py第3316行语法错误（`for`循环缺冒号） |
| 9 | GPT | 标记不可加速部分（Grid Search/sklearn依赖），修正Amdahl预期 |
| 10 | GPT | CLAUDE.md规格明确（含ABI排查/GIL规则/NumPy校验/返回契约/UTF-8/provenance） |
| 11 | GPT | C++使用`py::ssize_t`索引，`forcecast`策略处理dtype，优先`/utf-8` |

---

## 一、修订后的加速比预期

| 模块 | v1计划值 | v2修订值 | 理由 |
|------|---------|---------|------|
| DTW单次 (L=19) | 10-30x | **3-8x** | 仅209个有效矩阵单元，调用开销占比大 |
| DTW批量 (100×750) | 30-50x | **15-30x** | 摊平开销但standardize_returns等仍占时间 |
| 形态匹配 (单ETF全扫描) | 5-10x | **5-10x** | 合理（前提：全部内联进C++） |
| ADX | 3-5x | **1.5-3x** | 已高度NumPy向量化，C++收益有限 |
| **训练样本生成（整体）** | 未估算 | **1.6-2.5x** | Amdahl定律：Grid Search(sklearn)不可加速 |
| pattern_match_batch (新增) | — | **额外2-5x** | 消除Python往返+候选窗口预计算复用 |

---

## 二、修订后的目录结构

```
形态匹配ETF策略-pybind11/
├── src/
│   ├── core/                        # 纯计算模块（无掘金依赖）
│   │   ├── __init__.py
│   │   ├── dtw.py                   # DTW距离计算 (Python参考实现)
│   │   ├── pattern_match.py         # 形态匹配引擎 (Python参考实现)
│   │   ├── technical.py             # 技术指标 (Python参考实现)
│   │   ├── market_features.py       # 市场环境特征
│   │   ├── risk_controls.py         # 风控规则（纯计算部分）
│   │   └── metrics.py               # 绩效指标计算
│   ├── cpp/
│   │   ├── CMakeLists.txt
│   │   ├── etf_core.cpp             # ★ 统一C++模块（合并原三个）
│   │   └── pyi/
│   │       └── etf_core.pyi         # 类型存根
│   └── strategy/
│       └── strategy_v3.3.py         # 引用etf_core的策略主文件
├── tests/
│   ├── test_dtw.py
│   ├── test_technical.py
│   ├── test_pattern_match.py        # 含F12-F15固定样例
│   └── test_consistency.py          # ★ 新增：全量训练样本生成一致性
├── CLAUDE.md                        # ★ 完整规格
├── README.md
├── CMakeLists.txt
├── setup.py
└── .git/hooks/pre-push
```

---

## 三、统一C++模块 `etf_core` 接口契约

### 3.1 模块结构

```cpp
PYBIND11_MODULE(etf_core, m) {
    m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)";

    // DTW
    m.def("dtw_distance", &dtw_distance, ...);
    m.def("dtw_distance_batch", &dtw_distance_batch, ...);

    // 序列预处理
    m.def("standardize_returns", &standardize_returns, ...);
    m.def("cosine_similarity", &cosine_similarity, ...);

    // 形态匹配
    m.def("pattern_match_single", &pattern_match_single, ...);  // 单点
    m.def("pattern_match_batch", &pattern_match_batch, ...);    // ★ 批量

    // 技术指标
    m.def("compute_adx", &compute_adx, ...);
    m.def("compute_atr", &compute_atr, ...);
}
```

### 3.2 P0 硬性契约

**dtype/layout**:
```cpp
using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
```

**返回结构稳定性**:
- `pattern_match_single`返回`py::dict`或Python `None`（数据不足时）
- 15维key固定顺序：`top1_sim`, `top5_avg_sim`, ..., `n_matches_above_thresh`
- `pattern_match_batch`返回`(X15: ndarray, valid_mask: ndarray)`，形状`(N,15)`和`(N,)`

**异常语义**:
- C++ `std::invalid_argument`→Python `ValueError`
- Python包装层保留`try/except: return None`容错
- GIL释放区**禁止**创建`py::object`、访问Python回调

**NaN/长度策略**:
- `standardize_returns`结果长度可能≠`L_QUERY-1`（NaN被过滤）
- 接口不假设固定长度
- `cosine_similarity`近零判断：`norm < 1e-12`（与Python一致）

### 3.3 `pattern_match_batch` 接口

```cpp
// 批量形态匹配——训练样本生成的核心加速点
// 在C++内部完成：候选窗口预计算、standardize_returns复用、余弦预筛选、DTW精排
py::tuple pattern_match_batch(
    ArrD prices,              // shape (n_days,) 完整价格序列
    ArrI64 t_indices,         // shape (n_samples,) 查询时点索引
    int L_query = 20,
    int T_back = 750,
    int match_step = 1,
    int M_forward = 5,
    int K_matches = 10,
    int dtw_window = 5,
    int cos_prefilter_top = 50
);
// Returns: (features_X15: ndarray shape (n_valid,15), valid_mask: ndarray shape (n_samples,) bool)
// 无效样本对应valid_mask[i]=False，不包含在features_X15中
```

**核心优化**：候选窗口的`standardize_returns`结果在多个t_idx之间高度重叠——相邻t_idx的查询窗口仅差一天，其候选窗口也仅差一天。C++内部一次性预计算所有窗口的标准化收益率，避免Python往返+重复计算。

---

## 四、修订后的浮点容差

| 对象 | v1 | v2 | 理由 |
|------|----|----|------|
| DTW距离 | <1e-10 | **<1e-8** | DTW路径非唯一，min-cost选择可能不同 |
| pattern_match 综合得分 | <1e-10 | **<1e-6** | sigma_fast→exp非线性放大微小差异 |
| standardize_returns | <1e-10 | <1e-10 | 确定性运算，零歧义 |
| cosine_similarity | <1e-10 | <1e-10 | 确定性运算 |
| ADX | <1e-10 | <1e-10 | Wilder平滑确定性 |

---

## 五、扩展测试计划

### 5.1 F12-F15固定样例（GPT P0）

```python
def test_pattern_features_f12_f15():
    """固定输入验证F12-F15的确定性"""
    top_end_indices = np.array([100, 120, 160, 220], dtype=np.int64)
    top_scores = np.array([0.81, 0.80, 0.79, 0.90])
    top_k = 4
    T_back = 750
    # F12: time_span = 220-100 = 120
    # F13: time_span_ratio = 120/750 = 0.16
    # F14: cluster_ratio: searchsorted(100+60)=searchsorted(160)→ indices 0,1,2 → count=3, ratio=3/4=0.75
    # F15: n_matches_above_thresh: >0.8 → [0.81, 0.90] → 2 (0.80不计入)
```

### 5.2 真实NaN边界（GPT P1）

```python
def test_standardize_returns_nan():
    assert len(standardize_returns(np.array([100.0, np.nan, 101.0]))) == 1
    assert len(standardize_returns(np.array([np.nan, np.nan]))) == 0
    assert len(standardize_returns(np.array([100.0]))) == 0
```

### 5.3 全量训练样本一致性（GPT P0）

用合成价格数据跑完整的`generate_training_samples`，分别使用Python `pattern_match_single`和C++ `pattern_match_fast`，验证`X/y/dates/symbols`一致。

---

## 六、不可加速部分（显式标记）

以下函数**不纳入C++加速范围**，在Amdahl估算中全部归入Python串行部分：

| 函数 | 行号范围 | 不可加速原因 |
|------|---------|------------|
| `_grid_search_rf_rolling` | 1416-1457 | 依赖sklearn RandomForestClassifier |
| `_grid_search_svm_rolling` | 1460-1514 | 依赖sklearn SVC+CalibratedClassifierCV |
| `train_models` (LR内层CV) | 1534-1755 | 依赖sklearn LogisticRegression+TimeSeriesSplit |
| `update_ece_monitor` | 2467-2551 | 数据访问+cache查找为主，非纯计算 |
| `update_ic_monitor` (部分) | 2361-2465 | Spearman相关已有scipy/numpy fallback |
| `apply_risk_controls` (波动率) | 2076-2101 | pandas rolling+percentile已向量化 |

**修正后的整体加速预期**：训练阶段 1.6-2.5x，信号计算阶段 3-6x，综合约 **2-3x**。

---

## 七、V3.3.py第3316行语法错误修复

Kimi发现原文件`weekly_rebalance`中`for sym, feat in pattern_features.items()`后缺冒号。重构后的策略文件必须修复此问题（不影响纯计算模块）。

---

## 八、修订后执行顺序

```
Step 0: 项目基础设施 (✅ 已完成)
Step 1: core/dtw.py 提取+测试 (✅ 已完成，需补NaN边界测试)
Step 2: core/technical.py 提取+测试 (✅ 已完成)
Step 3: core/pattern_match.py 提取+测试 (含F12-F15固定样例)
Step 4: 其余core模块提取 (market_features, risk_controls, metrics)
Step 5: C++ etf_core 统一模块实现
  Step 5a: dtw_distance + standardize_returns + cosine_similarity
  Step 5b: compute_adx + compute_atr
  Step 5c: pattern_match_single
  Step 5d: pattern_match_batch (含滚动窗口预计算)
Step 6: Python包装层 (异常语义+fallback)
Step 7: 全量一致性测试 + 性能基准
Step 8: CLAUDE.md + README + pyi 类型存根
```

---

## 九、审查覆盖确认

| 审查发现 | v2是否覆盖 |
|----------|-----------|
| Kimi: 加速比下调 | ✅ §一 |
| Kimi: 三模块合并 | ✅ §三 |
| Kimi: Amdahl整体估算 | ✅ §六 |
| Kimi: sigma_fast分层容差 | ✅ §四 |
| Kimi: 第3316行语法错误 | ✅ §七 |
| GPT: pattern_match_batch | ✅ §3.3 |
| GPT: 滚动窗口预计算 | ✅ §3.3 |
| GPT: dtype/返回/异常契约 | ✅ §3.2 |
| GPT: F12-F15测试 | ✅ §5.1 |
| GPT: NaN边界测试 | ✅ §5.2 |
| GPT: 全量一致性测试 | ✅ §5.3 |
| GPT: 不可加速标记 | ✅ §六 |
| GPT: CLAUDE.md规格 | ✅ (执行Step 8时落实) |
| GPT: py::ssize_t+forcecast | ✅ §3.2 |
| GPT: /utf-8优先 | ✅ (CMake中实现) |
