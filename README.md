# 形态匹配 ETF 策略 — Python+C++ 混合编程重构 | Pattern Matching ETF Strategy — Python+C++ Hybrid Refactor

[![CI](https://github.com/redamancy231-create/etf-pattern-match-pybind11/actions/workflows/ci.yml/badge.svg)](https://github.com/redamancy231-create/etf-pattern-match-pybind11/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-20-00599C)](https://en.cppreference.com/)
[![CMake](https://img.shields.io/badge/CMake-3.20+-064F8C)](https://cmake.org/)
[![pybind11](https://img.shields.io/badge/pybind11-3.0.4-green)](https://github.com/pybind/pybind11)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Featured](https://img.shields.io/badge/featured-chinese--independent--developer-orange)](https://github.com/1c7/chinese-independent-developer)

## English | English Summary

Pure computation modules were extracted from a 3,836-line Chinese ETF pattern-matching strategy (V3.3) and accelerated with **pybind11 + C++20**. The algorithm logic is unchanged.

**For:** pybind11/C++ acceleration practice, quant engineering reference, Python/C++ parity testing.

**Not for:** live trading, investment advice, new backtest claims, or strategy performance optimization.

<details>
<summary><b>中文简介</b></summary>

本项目从 3836 行中文 ETF 形态匹配策略 V3.3 中提取纯计算核心，并使用 **pybind11 + C++20** 进行加速。算法逻辑不变，目标是验证 Python/C++ 混合工程实践——**不是实盘交易系统、不是投资建议、不是策略收益优化**。

**适用场景：** pybind11/C++ 加速实践、量化工程参考、Python/C++ 一致性检验。

**不适用场景：** 实盘交易、投资建议、回测收益声明、策略绩效优化。

</details>

## 加速结果 | Acceleration Results

Core single-call speedups reach 37x–61x, while batch matching (C++ single ×100 → C++ batch ×1) reaches 2.2x because Python/C++ orchestration and data movement dominate the end-to-end workload.

<details>
<summary>中文</summary>

核心函数单次调用加速 37x–61x，批量匹配（C++ 单次 ×100 → C++ 批量 ×1）因 Python/C++ 编排和数据搬运占主导，端到端加速 2.2x。

</details>

| 函数 Function | Python | C++ | 加速比 Speedup |
|------|--------|-----|--------|
| DTW 距离 DTW Distance (L=19) | 98 µs | 2.7 µs | **37x** |
| 形态匹配（单 ETF 单时间点）Pattern Match (single ETF, one timestamp) | 14.3 ms | 0.23 ms | **61x** |
| 批量形态匹配（100 时间点）Batch Pattern Match (100 timestamps) | 50 ms¹ | 23 ms | **2.2x¹** |

> ¹ Batch row compares 100 C++ single calls vs 1 C++ batch call — a measure of batch-interface overhead reduction, not Python-vs-C++ speedup.

> **详细分析**：单次调用 61× 加速落到批量场景只剩 2.2×——这不是 bug，是 Amdahl's Law。见 [性能分析短文](docs/performance-analysis.md)（中英双语）。
> **Detailed analysis**: why 61× single-call speedup becomes 2.2× in batch workloads — not a bug, it's Amdahl's Law. See [performance analysis article](docs/performance-analysis.md) (bilingual).

### 基准测试范围 | Benchmark Scope

- Platform：Windows 11, MSVC Release `/O2`
- Python: 3.12.7
- C++: C++20, pybind11 3.0.4
- Verification：`python verify_etf_core.py` and `python verify_batch.py`
- Scope：compute-kernel acceleration only, not a claim about trading performance

<details>
<summary>中文</summary>

- 平台：Windows 11, MSVC Release `/O2`
- 验证：`python verify_etf_core.py` 与 `python verify_batch.py`
- 范围：仅计算核心加速，非交易性能声明

</details>

## 快速开始 | Quick Start

**▶️ [Interactive Demo Notebook](notebooks/etf_pattern_matching_demo.ipynb)** — 在 Jupyter 中逐步体验完整算法流程 | walk through the full algorithm step-by-step in Jupyter.

```bash
# 编译 C++ 模块 | Compile C++ module
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release

# 验证 C++ 与 Python 一致性 | Verify C++ vs Python consistency
python verify_etf_core.py

# 运行测试 | Run tests
python -m pytest tests/ -v

# 启动交互演示 | Launch interactive demo
jupyter notebook notebooks/etf_pattern_matching_demo.ipynb
```

## 项目结构 | Project Structure

```
├── src/core/                  # Python pure computation layer (6 modules, zero JuE SDK dependency)
│   ├── dtw.py                  # DTW distance + sequence standardization
│   ├── pattern_match.py        # Pattern matching engine (15-dim features)
│   ├── technical.py            # ADX / ATR / sector rotation
│   ├── market_features.py      # Market environment features (F16-F21)
│   ├── risk_controls.py        # Risk control rules (pure computation)
│   └── metrics.py              # Sortino / Calmar / IC statistics
├── src/cpp/
│   ├── etf_core.cpp            # Unified C++ acceleration module (8 functions, ~1,100 lines)
│   └── pyi/etf_core.pyi        # Type stubs
├── tests/                      # 54 unit tests
├── notebooks/
│   └── etf_pattern_matching_demo.ipynb  # Interactive demo (GPT-5.6-Sol reviewed)
├── verify_etf_core.py          # C++ vs Python consistency verification
├── verify_batch.py             # Batch pattern matching verification
└── CLAUDE.md                   # Development notes and pybind11 lessons
```

```mermaid
flowchart LR
    A["Archived V3.3.py"] --> B["src/core: Pure Python computation"]
    B --> C["src/cpp: pybind11 C++20 Acceleration"]
    B --> D["tests: Python behavior tests"]
    C --> E["verify_etf_core.py: C++ vs Python Parity"]
    C --> F["verify_batch.py: Batch parity + performance"]
```

## 常见问题 | FAQ

### 这是交易系统吗？| Is this a trading system?

No. This repository is a programming practice project for extracting pure computation modules and accelerating them with pybind11 + C++20.

<details>
<summary>中文</summary>

不是。本仓库是一个编程实践项目：从量化策略中提取纯计算模块，用 pybind11 + C++20 加速，验证一致性。

</details>

### 为什么批量加速（2.2x）远低于单次调用加速（61x）？| Why is batch speedup (2.2x) much lower than single-call speedup (61x)?

Single-call pattern matching measures the hot compute kernel in isolation. Batch matching includes orchestration, data movement, validation, and Python/C++ boundary costs. The precomputed window cache helps, but end-to-end throughput is bounded by these overheads.

<details>
<summary>中文</summary>

单次形态匹配测量的是纯计算热路径。批量匹配包含编排、数据搬运、验证和 Python/C++ 边界开销。预计算窗口缓存有帮助，但端到端吞吐量受这些开销限制。

</details>

### 是否依赖掘金 SDK？| Does it depend on the JuE (掘金) SDK?

No. The extracted `src/core` modules are pure computation modules and only require NumPy.

<details>
<summary>中文</summary>

不依赖。提取出的 `src/core` 是纯计算模块，仅需 NumPy。

</details>

### 原始 V3.3.py 在哪里？| Where is the original V3.3.py?

The original strategy is an archived baseline from the parent Chinese project. This repository keeps the extracted computation layer, tests, and C++ acceleration module — not the full platform-bound strategy.

<details>
<summary>中文</summary>

原始策略是父项目的归档基线，本仓库仅保留提取出的计算层、测试和 C++ 加速模块——不含完整平台绑定策略。

</details>

### 能否重跑原始回测？| Can I rerun the original backtest?

No. The original V3.3 is a sealed baseline that depends on the JuE platform and is outside this repository's scope. This project focuses on engineering extraction, C++ acceleration, and parity verification.

<details>
<summary>中文</summary>

不能。原始 V3.3 是封存基线，依赖掘金平台，不在本仓库范围内。本项目聚焦工程提取、C++ 加速和一致性验证。

</details>

## 原始来源与范围 | Original Source and Scope

Extracted from **Pattern Matching ETF Strategy V3.3** (archived baseline, 3,836 lines). The original strategy is a weekly ETF long-only rotation strategy (DTW + cosine pattern matching → RF/SVM Stacking → multi-layer risk controls), backtested on the JuE platform over 2020–2026.

<details>
<summary>中文</summary>

提取自**形态匹配 ETF 策略 V3.3**（归档基线，3836 行）。原始策略为周频 ETF 多头轮动策略（DTW + 余弦形态匹配 → RF/SVM Stacking → 多层风控），在掘金平台回测，覆盖 2020-2026 年。

</details>

**What this repository contains:**

- Extracted pure-computation Python modules `src/core/`
- pybind11/C++20 acceleration module `src/cpp/`
- 54 unit tests + 2 verification scripts
- Build configuration and development documentation

<details>
<summary>包含内容（中文）</summary>

- 提取的纯计算 Python 模块 `src/core/`
- pybind11/C++20 加速模块 `src/cpp/`
- 54 项单元测试 + 2 个验证脚本
- 构建配置与开发文档

</details>

**What this repository does NOT contain:**

- The original platform-bound strategy file
- JuE SDK bindings or live trading code
- Backtest results or strategy performance claims

<details>
<summary>不包含内容（中文）</summary>

- 原始平台绑定策略文件
- 掘金 SDK 绑定或实盘交易代码
- 回测结果或策略绩效声明

</details>

## 工具链 | Toolchain

- Python 3.12.7 + NumPy
- pybind11 3.0.4
- MSVC 19.51 (Visual Studio 2026 Community) + CMake 3.20
- C++20

## 模型分工与审查 | Model Responsibilities and Review

| Author | Delivery | Review |
|------|------|------|
| DeepSeek-V4-Pro | 6 Python modules + C++ skeleton + tests + documentation | Kimi + GPT-5.5 |
| Kimi-K2.7-Code | C++ `pattern_match_batch` + full GIL coverage + batch contract convergence + boundary tests | GPT-5.5 |

All source files are annotated with model provenance.

<details>
<summary>中文</summary>

| 作者 | 交付 | 审查 |
|------|------|------|
| DeepSeek-V4-Pro | 6 个 Python 模块 + C++ 骨架 + 测试 + 文档 | Kimi + GPT-5.5 |
| Kimi-K2.7-Code | C++ `pattern_match_batch` + 全量 GIL 覆盖 + batch 契约收敛 + 边界测试 | GPT-5.5 |

所有源文件均标注模型来源。

</details>

## 关联项目 | Related Projects

| Project | Relationship |
|------|------|
| [**AI Collaboration Framework**](https://github.com/redamancy231-create/ai-collaboration-framework) | **Methodology upstream** — multi-model review, passive observation, and project closure protocols originate from this framework |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **Review methodology source** — the four-round Kimi + GPT-5.5 cross-backend review followed this toolkit's SOP |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **Sibling project** — controlled experiment methodology for prompt engineering; this project applies similar methodological rigor to pybind11/C++ hybrid programming |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **Sibling project** — multi-model academic production pipeline; shares emphasis on methodology portability and cross-backend verification |

<details>
<summary>中文</summary>

| 项目 | 关系 |
|------|------|
| [**AI 协作框架**](https://github.com/redamancy231-create/ai-collaboration-framework) | **方法论上游**——本项目的多后端审查、被动观测记录、项目闭合协议均源自该框架 |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **审查方法来源**——本项目的 Kimi + GPT-5.5 四轮异后端审查使用了该工具包的 SOP |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **同级项目**——将对照实验方法论应用于 prompt 工程；本项目在 pybind11/C++ 混合编程方向上应用了类似的方法学严谨性 |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **同级项目**——多模型学术生产流水线；同样强调方法的可移植性和跨后端验证 |

</details>

## 详细文档 | Detailed Documentation

Development notes and pybind11 lessons: [CLAUDE.md](CLAUDE.md) — build details, ABI troubleshooting, GIL management, floating-point tolerances, and review traceability.

<details>
<summary>中文</summary>

开发笔记与 pybind11 实战经验：[CLAUDE.md](CLAUDE.md) — 构建细节、ABI 排错、GIL 管理、浮点容差、审查追溯。

</details>
