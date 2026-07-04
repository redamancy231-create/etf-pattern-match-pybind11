# 形态匹配ETF策略 — Python+C++混合编程重构优化计划

> **模型 provenance**: DeepSeek-V4-Pro (via Claude Code CLI)，2026-07-03
> **状态**: 计划阶段，待异后端审查

---

## 一、项目理解总结

### V3.3.py 代码画像（3837行纯Python）

| 维度 | 现状 |
|------|------|
| **架构** | 三层：形态匹配引擎 → RF+SVM Stacking → 组合优化+7级风控 |
| **计算瓶颈** | DTW距离（Python双层循环O(n²)）、`pattern_match_single`（每ETF每时点~750次DTW）、`generate_training_samples`（两遍全ETF扫描） |
| **依赖耦合** | 深度绑定掘金SDK（`gm.api`），无法脱离平台独立运行 |
| **代码质量** | 8个正式BUGFIX记录，`except: pass`静默吞异常的历史教训，已修复 |
| **项目状态** | CLOSED，不可重跑回测，仅作方法论参考 |

### pybind11-demo 可迁移经验

| 经验 | 适用性 |
|------|--------|
| `py::arg()` 数量=函数参数数量 | ★★★★★ 所有binding |
| GIL释放（`py::gil_scoped_release`） | ★★★★★ 长时间纯C++计算 |
| ABI对齐（Python版本×平台） | ★★★★★ 编译产物 |
| NumPy数组校验（ndim/shape） | ★★★★ 批量接口 |
| 样本方差公式正确性 | ★★★ 统计分析 |
| CMake多配置生成器（MSVC） | ★★★★★ 构建系统 |

---

## 二、总体方案

### 阶段划分

```
阶段0: 项目提取与基础设施
阶段1: 重构（纯Python层面解耦，不改算法）
阶段2: C++加速（pybind11绑定计算热点）
阶段3: 验证与文档
```

### 目标目录结构

```
形态匹配ETF策略-pybind11/
├── src/
│   ├── core/                    # 纯计算模块（无掘金依赖）
│   │   ├── __init__.py
│   │   ├── dtw.py               # DTW距离计算（Python参考实现）
│   │   ├── pattern_match.py     # 形态匹配引擎
│   │   ├── technical.py         # 技术指标（ADX等）
│   │   ├── market_features.py   # 市场环境特征
│   │   ├── risk_controls.py     # 风控规则（纯计算部分）
│   │   └── metrics.py           # 绩效指标计算
│   ├── cpp/                     # C++ pybind11扩展
│   │   ├── CMakeLists.txt
│   │   ├── dtw_fast.cpp         # DTW C++加速
│   │   ├── pattern_match_fast.cpp # 形态匹配批量加速
│   │   ├── technical_fast.cpp   # 技术指标C++实现
│   │   └── pyi/                 # Python类型存根
│   └── strategy/                # 策略层（保留掘金依赖）
│       └── strategy_v3.3.py     # 重构后的策略主文件
├── tests/
│   ├── test_dtw.py
│   ├── test_pattern_match.py
│   └── test_technical.py
├── notebooks/                   # 验证notebook
├── CLAUDE.md
├── README.md
├── CMakeLists.txt               # 顶层CMake
├── setup.py / pyproject.toml
└── .git/hooks/pre-push          # Git pre-push hook
```

### 关键设计决策

1. **不修改算法逻辑**：V3.3是封存基线，重构只改结构和实现语言，不改数学
2. **core/包零外部依赖**：只用numpy/scipy，不依赖掘金SDK
3. **C++只加速纯计算**：DTW、ADX、形态匹配的循环体——不改策略逻辑
4. **双层实现**：每个C++模块保留Python fallback，确保可移植性

---

## 三、阶段1：重构（Python层面解耦）

### 1.1 提取DTW模块 (`src/core/dtw.py`)
- 从V3.3.py剥离 `dtw_distance()`, `standardize_returns()`, `cosine_similarity()`
- 无掘金依赖，纯numpy
- 增加批量接口 `dtw_distance_batch()`

### 1.2 提取形态匹配引擎 (`src/core/pattern_match.py`)
- 剥离 `pattern_match_single()` 的核心计算
- 将掘金数据获取与纯计算分离
- 15维特征提取保持原逻辑

### 1.3 提取技术指标 (`src/core/technical.py`)
- `_compute_adx_from_df()` → `compute_adx(high, low, close, n=14)`
- 行业轮动速度 → `compute_sector_rotation(returns_dict)`

### 1.4 提取市场特征 (`src/core/market_features.py`)
- 6维市场特征的纯计算版本
- 去掉缓存层依赖

### 1.5 提取风控规则 (`src/core/risk_controls.py`)
- 7级风控的纯计算规则
- 去掉context依赖，改为函数式接口

### 1.6 提取绩效指标 (`src/core/metrics.py`)
- Sortino, Calmar, 跟踪误差, IC统计等
- 自包含，无平台依赖

---

## 四、阶段2：C++加速（pybind11绑定）

### 2.1 DTW C++加速 (`src/cpp/dtw_fast.cpp`)
**加速目标：10-50x**

```cpp
// 核心函数
double dtw_distance_fast(const double* x, size_t n, 
                         const double* y, size_t m, int window);
// 批量版本
py::array_t<double> dtw_distance_batch(
    py::array_t<double> queries,    // shape (n_queries, L)
    py::array_t<double> candidates  // shape (n_candidates, L)
);
```

**关键技术点**：
- GIL释放（`py::gil_scoped_release`）
- 栈分配DTW矩阵（对L_QUERY=20可用局部数组，避免堆分配）
- Sakoe-Chiba band约束优化
- 批量版本减少Python↔C++调用开销

### 2.2 形态匹配批量加速 (`src/cpp/pattern_match_fast.cpp`)
**加速目标：5-15x**

```cpp
// 单ETF单时点的形态匹配（C++完成余弦预筛选+DTW精排）
py::dict pattern_match_fast(
    py::array_t<double> prices,     // 完整价格序列
    int T_idx,                      // 查询时点
    int L_QUERY, int T_BACK, int MATCH_STEP,
    int M_FORWARD, int K_MATCHES,
    int DTW_WINDOW, int COS_PREFILTER_TOP
);
```

**关键技术点**：
- C++内部完成`standardize_returns`（避免Python往返）
- 余弦预筛选在C++层完成
- DTW精排仅对top-K候选
- 返回15维特征字典

### 2.3 技术指标C++ (`src/cpp/technical_fast.cpp`)
**加速目标：3-5x**

```cpp
double compute_adx_fast(
    py::array_t<double> high,
    py::array_t<double> low,
    py::array_t<double> close,
    int n = 14
);
```

### 2.4 构建系统
```cmake
# 顶层 CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(etf_pattern_match LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)

# 三个pybind11模块
pybind11_add_module(dtw_fast src/cpp/dtw_fast.cpp)
pybind11_add_module(pattern_match_fast src/cpp/pattern_match_fast.cpp)
pybind11_add_module(technical_fast src/cpp/technical_fast.cpp)
```

**复用pybind11-demo经验**：
- MSVC多配置生成器：`--config Release`
- Python路径注入：`-DPython_EXECUTABLE=...`
- pybind11自动检测
- `/utf-8` 和 `/wd4819` 编译选项
- 产物输出到`src/cpp/`目录

---

## 五、阶段3：验证与文档

### 3.1 正确性验证
- 对每个C++模块，用原始Python实现的输出作为ground truth
- 容忍误差：浮点运算<1e-10，DTW距离<1e-8（路径不同可能导致微小差异）
- 批量测试：随机生成100组输入，全量对比

### 3.2 性能基准

| 模块 | 预期加速比 | 验证方法 |
|------|-----------|---------|
| DTW单次 | 10-30x | L=20序列，1000次计时 |
| DTW批量 | 30-50x | 100查询×750候选 |
| 形态匹配 | 5-10x | 单ETF全历史扫描 |
| ADX | 3-5x | 1000日序列 |

### 3.3 Git Pre-push Hook
```bash
#!/bin/bash
# .git/hooks/pre-push
# 推送前运行测试套件
echo "[pre-push] Running tests..."
PYTHONIOENCODING=utf-8 python -m pytest tests/ -v
if [ $? -ne 0 ]; then
    echo "[pre-push] Tests failed, push aborted."
    exit 1
fi
echo "[pre-push] All tests passed."
```

### 3.4 CLAUDE.md
- 按照五步协议编写
- 记录构建步骤、模块依赖、已知限制
- 标注模型provenance

---

## 六、执行顺序

```
Step 0: 项目提取（创建目录结构、复制核心文件、git init + pre-push hook）
Step 1: core/dtw.py 提取 + 测试
Step 2: core/technical.py 提取 + 测试
Step 3: core/pattern_match.py 提取 + 测试
Step 4: core/market_features.py + risk_controls.py + metrics.py 提取
Step 5: C++ dtw_fast 实现 + 验证
Step 6: C++ technical_fast 实现 + 验证
Step 7: C++ pattern_match_fast 实现 + 验证
Step 8: 集成测试 + 性能基准
Step 9: 文档（CLAUDE.md + README）
```

---

## 七、风险与边界

| 风险 | 缓解 |
|------|------|
| 掘金SDK深度耦合 | 仅提取纯计算，策略层保留原依赖，不试图"可独立运行" |
| C++编译环境差异 | 复用pybind11-demo已验证的MSVC配置 |
| DTW结果微小差异 | 设定容忍阈值，记录在文档中 |
| 项目已CLOSED不可回测 | 所有验证用合成数据，不尝试连接掘金平台 |

---

**关键声明**：
- 算法逻辑零改动（不对回测结果产生任何影响）
- 目的是**提高Python+C++混合编程熟练度**，不是改进策略
- C++模块保留Python fallback，确保在没有C++编译环境时仍可运行
- 新项目作为**独立的编程练习仓库**发布到GitHub，与原项目明确区分
