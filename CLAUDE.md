# CLAUDE.md — 形态匹配 ETF 策略 pybind11 重构 | Pattern Matching ETF Strategy pybind11 Refactor

> **模型来源 Model provenance**: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> **审查 Review**: Kimi-K2.7-Code (魔鬼代言人 Devil's Advocate + 代码改进 code improvements) + GPT-5.5 via Codex CLI (完备性 completeness), 2026-07-03 / 2026-07-04

## 项目定位 | Project Positioning

从 `形态匹配ETF策略/V3.3.py`（3836 行纯 Python 量化策略）提取纯计算模块，使用 pybind11 + C++20 加速。**算法逻辑不变**，目标是提升 Python+C++ 混合编程熟练度，而非改进回测表现。
Pure computation modules were extracted from `形态匹配ETF策略/V3.3.py` (a 3,836-line pure Python quantitative strategy) and accelerated using pybind11 + C++20. **The algorithm logic is unchanged**: the goal is to improve proficiency in Python+C++ hybrid programming, not to improve backtest performance.

- 原始项目 Original project：CLOSED（V3.3 第 4 轮为归档基线），回测不可重跑；CLOSED (V3.3 Round 4 is the archived baseline), backtests must not be rerun
- 本项目 This project：独立编程实践仓库，与原始项目明确分离；an independent programming practice repository, clearly separated from the original project
- 纯计算模块 Pure computation modules：零掘金 SDK 依赖，仅需 NumPy；zero JuE SDK (掘金 SDK) dependencies, requiring only numpy

## 快速开始 | Quick Start

```bash
# 编译 C++ 模块 | Compile C++ module
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release

# 验证 | Verify
python verify_etf_core.py

# 测试 | Test
PYTHONIOENCODING=utf-8 python -m pytest tests/ -v
```

## 项目结构 | Project Structure

```
├── src/core/                  # Python 纯计算模块（无掘金 SDK 依赖）
│   │                          # Python pure computation modules (no JuE SDK dependency)
│   ├── dtw.py                 # DTW 距离 + 序列预处理 | DTW distance + sequence preprocessing
│   ├── technical.py           # ADX / ATR / 板块轮动 | ADX / ATR / sector rotation
│   ├── pattern_match.py       # 形态匹配引擎（15 维特征）| Pattern matching engine (15-dim features)
│   ├── market_features.py     # F16-F21 市场环境特征 | F16-F21 market environment features
│   ├── risk_controls.py       # 风控规则（纯计算）| Risk control rules (pure computation)
│   └── metrics.py             # Sortino / Calmar / IC 统计 | Sortino / Calmar / IC statistics
├── src/cpp/
│   ├── etf_core.cpp           # 统一 C++ 模块（7 函数）| Unified C++ module (7 functions)
│   └── pyi/etf_core.pyi       # 类型存根 | Type stubs
├── tests/                     # 54 项测试，0 失败 | 54 tests, 0 failures
├── docs/
│   ├── file-index.md           # 关键文件索引 | Key file index
│   └── reviews/                # 设计文档（中文）| Design documents (zh-CN)
├── .github/workflows/ci.yml    # CI（Windows + MSVC）
├── verify_etf_core.py         # C++ vs Python 一致性验证 | C++ vs Python consistency verification
├── CMakeLists.txt
└── CLAUDE.md
```

## 构建 | Build

### 依赖 | Dependencies
- Python 3.12.7 + numpy
- pybind11 3.0.4 (`pip install pybind11`)
- MSVC 19.51 (Visual Studio 2026 Community) + CMake 3.20+

### 编译选项 | Compilation Options
- MSVC Release: `/O2 /utf-8 /wd4819`
- Python 路径通过 `-DPython_EXECUTABLE=...` 注入，非硬编码 | Python path is injected via `-DPython_EXECUTABLE=...`, not hardcoded
- C++20 标准 | C++20 standard

### ABI 排错 | ABI Troubleshooting
```bash
# 1. Python ABI 标签 | Python ABI tag
python -c "import sys; print(f'cp{sys.version_info.major}{sys.version_info.minor}-{sys.platform}')"

# 2. .pyd 文件名必须与 PYBIND11_MODULE 名称一致 | .pyd filename must match PYBIND11_MODULE name
ls build/Release/Release/*.cp312-win_amd64.pyd

# 3. 勿混用 Release/Debug | Do not mix Release/Debug
```

## 性能（相对原始 V3.3.py，MSVC /O2）| Performance (relative to the original V3.3.py, MSVC /O2)

| 函数 Function | Python | C++ | 加速比 Speedup |
|------|--------|-----|--------|
| DTW (L=19) | 124.8 µs | 2.9 µs | **43.3x** |
| pattern_match_single | 15.3 ms | 0.3 ms | **58.4x** |
| pattern_match_batch (100 T_idx) | 50.0 ms | 22.8 ms | **2.2x** |

## pybind11 关键经验 | Key pybind11 Lessons

### py::arg() 数量 = 函数参数数量 ★★★★★ | Number of py::arg() Entries = Number of Function Parameters ★★★★★
带默认值的参数也必须声明，与 pybind11-demo 一致。
Parameters with default values must also be declared, consistent with pybind11-demo.

### GIL 释放 ★★★★★ | GIL Release ★★★★★
- `dtw_distance` / `compute_adx` / `pattern_match_single` / `pattern_match_batch`：4 个长耗时计算函数均在纯 C++ 计算段显式释放 GIL（`py::gil_scoped_release`），返回值前重新获取
- `pattern_match_single` 使用 `std::optional` + lambda 模式解决 early return 与 GIL 释放的冲突：所有 `py::none()` 返回发生在持有 GIL 时，`py::dict` 构造发生在持有 GIL 时
- `compute_atr` / `standardize_returns` 返回 Python 对象（`ArrD`），GIL 管理由 pybind11 调用边界自动处理
- 确保构造 Python 返回值前持有 GIL
- `dtw_distance` / `compute_adx` / `pattern_match_single` / `pattern_match_batch`: all 4 long-running computation functions explicitly release the GIL (`py::gil_scoped_release`) inside the pure C++ computation section and reacquire it before returning values
- `pattern_match_single` uses a `std::optional` + lambda pattern to resolve conflicts between early returns and GIL release: all `py::none()` returns happen while holding the GIL, and `py::dict` construction happens while holding the GIL
- `compute_atr` / `standardize_returns` return Python objects (`ArrD`), with GIL management handled automatically by the pybind11 call boundary
- Ensure the GIL is held before constructing Python return values

### dtype 契约 ★★★★★ | dtype Contract ★★★★★
```cpp
using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
```
- `forcecast` 自动转换非严格匹配的 dtype | `forcecast` automatically converts non-strictly matching dtypes
- `py::ssize_t` 索引（MSVC 兼容）| `py::ssize_t` indexing (MSVC-compatible)

### 稳定返回结构 ★★★★★ | Stable Return Structure ★★★★★
- `pattern_match_single` 返回 `py::dict` 或 `py::none()` | returns `py::dict` or `py::none()`
- 15 个 key 固定顺序，与 Python 版本完全一致 | The 15 keys have a fixed order, fully matching the Python version
- `n_matches_above_thresh` 返回 int（与 Python 版本一致）| returns int (same as the Python version)
- `pattern_match_batch` 返回 `(features_X15, valid_mask)`（v4 收敛：feature_keys 提升为模块常量 `etf_core.FEATURE_KEYS`）| returns `(features_X15, valid_mask)` (v4 convergence: feature_keys promoted to module constant `etf_core.FEATURE_KEYS`)

### 参数校验 ★★★★ | Parameter Validation ★★★★
- `match_step <= 0` → `std::invalid_argument`，防止死循环 | preventing infinite loops
- `t_indices` 必须严格递增且通过范围校验 | must be strictly increasing and pass range validation
- `high/low/close` 长度一致性校验（`compute_atr` / `compute_adx`）| length consistency validation

### CMake 友好错误 ★★★ | CMake-Friendly Errors ★★★
- 未设置 `Python_EXECUTABLE` 时输出 WARNING + 示例命令 | If not set, output a WARNING + example command
- 未找到 `pybind11` 时输出 FATAL_ERROR + 安装/配置指引，替代原始 CMake 错误 | If not found, output FATAL_ERROR + installation/configuration guidance instead of raw CMake errors

### 浮点容差 ★★★★ | Floating-Point Tolerances ★★★★
| 对象 Object | 容差 Tolerance |
|------|------|
| standardize_returns | 1e-10 |
| cosine_similarity | 1e-10 |
| DTW 距离 DTW Distance | 1e-8 |
| 形态匹配得分 pattern_match score | 1e-6 |
| ADX | 1e-10 |

### UTF-8 ★★★ | UTF-8 ★★★
- 源码保存为 UTF-8 | Source code is saved as UTF-8
- 首选编译选项 `/utf-8`，`/wd4819` 为后备 | Prefer compilation option `/utf-8`, with `/wd4819` as fallback

## 审查追溯 | Review Traceability

| 轮次 Round | 模型 Model | 角度 Angle | 关键发现 Key Findings |
|------|------|------|---------|
| R1 | Kimi-K2.7-Code | 魔鬼代言人 Devil's Advocate | 加速比高估→修正；三模块合并；整体 Amdahl 加速 1.6-2.5x |
| | | | Speedup overestimated → revised; three modules merged; overall Amdahl speedup 1.6-2.5x |
| R2 | GPT-5.5 via Codex | 完备性 Completeness | 缺 pattern_match_batch；dtype/异常契约；F12-F15 测试；CLAUDE.md 规格 |
| | | | Missing pattern_match_batch; dtype/exception contracts; F12-F15 tests; CLAUDE.md specification |
| R3 | Kimi-K2.7-Code | 代码改进 Code Improvements | 全量 GIL 覆盖 + batch 契约收敛 + CMake 友好错误 + match_step 守卫 + 边界测试（52→54） |
| | | | Full GIL coverage + batch contract convergence + CMake-friendly errors + match_step guard + boundary tests (52→54) |

## 关联项目 | Related Projects

- 父项目 Parent project（形态匹配ETF策略 V3.3）— 归档基线 archived baseline (CLOSED)
- pybind11-demo — pybind11 经验来源 source of pybind11 experience (CLOSED)
