# ETF Pattern-Matching Strategy — A Python/C++ Hybrid Refactor

[![CI](https://github.com/redamancy231-create/etf-pattern-match-pybind11/actions/workflows/ci.yml/badge.svg)](https://github.com/redamancy231-create/etf-pattern-match-pybind11/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-20-00599C)](https://en.cppreference.com/)
[![CMake](https://img.shields.io/badge/CMake-3.20+-064F8C)](https://cmake.org/)
[![pybind11](https://img.shields.io/badge/pybind11-3.0.4-green)](https://github.com/pybind/pybind11)
[![license](https://img.shields.io/badge/license-MIT-blue)](../LICENSE)
[![Featured](https://img.shields.io/badge/featured-Chinese_Independent_Developer-orange)](https://github.com/1c7/chinese-independent-developer)

**Languages**: English · [简体中文](../README.md) · [正體中文](../zh-Hant/README.md)

[![English](https://img.shields.io/badge/lang-English-blue)]()
[![中文](https://img.shields.io/badge/lang-中文-red)](../README.md)
[![正體中文](https://img.shields.io/badge/lang-正體中文-green)](../zh-Hant/README.md)

> ⚡ DTW 96µs→2.8µs (34x) | Pattern Matching 14.0ms→0.26ms (53x) | pybind11+C++20 | pip install ready

## Summary

Compute-only modules were extracted from a 3,836-line Chinese ETF pattern-matching strategy (V3.3) and accelerated with **pybind11 + C++20**. The algorithms are unchanged.

**Best suited for:** learning pybind11/C++ acceleration, studying quantitative-engineering implementation patterns, and testing Python/C++ parity.

**Not intended for:** live trading, investment advice, claims about backtest performance, or optimization of strategy returns.

## Acceleration Results

Core functions achieve 34×–53× per-call speedups (the median of 100 timed runs after five warm-up runs). Replacing 100 individual C++ calls with one batched C++ call yields a 2.2× speedup by reducing interface overhead. See [reproducible benchmarks](../benchmarks/) for methodology and raw data.

| Function | Python | C++ | Speedup |
|------|--------|-----|--------|
| DTW Distance (L=19) | 96 µs | 2.8 µs | **34×** |
| Pattern Matching (single ETF, one timestamp) | 14.0 ms | 0.26 ms | **53×** |
| Batch Pattern Matching (100 timestamps) | 50 ms¹ | 23 ms | **2.2×¹** |

> ¹ The batch row compares 100 individual C++ calls with one batched C++ call — a measure of the reduction in batch-interface overhead, not of the Python-to-C++ speedup.

> **Detailed analysis**: A 53× single-call speedup falls to 2.2× in batch workloads. This is not a bug; it is Amdahl's law in action. See [performance analysis article](../docs/performance-analysis.md). Reproducible benchmark methodology: [benchmarks/](../benchmarks/).

### Benchmark Scope

- Platform: Windows 11, MSVC Release `/O2`
- Python: 3.12.7
- C++: C++20, pybind11 3.0.4
- Verification: `python verify_etf_core.py` and `python verify_batch.py`
- Scope: compute-kernel acceleration only, not a claim about trading performance

## Quick Start

**▶️ [Interactive Demo Notebook](../notebooks/etf_pattern_matching_demo.ipynb)** — walk through the full algorithm step-by-step in Jupyter.

### pip install (recommended)
```bash
pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git
```

### Build from source (CMake)
```bash
# Compile C++ module
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release

# Verify C++ vs Python consistency
python verify_etf_core.py

# Run tests
python -m pytest tests/ -v

# Launch interactive demo
jupyter notebook notebooks/etf_pattern_matching_demo.ipynb
```

## Project Structure

```
├── src/core/                  # compute-only Python layer (6 modules, no dependency on the JuE SDK)
│   ├── dtw.py                  # DTW distance + sequence standardization
│   ├── pattern_match.py        # Pattern matching engine (15-dimensional feature vector)
│   ├── technical.py            # ADX / ATR / sector rotation
│   ├── market_features.py      # Market environment features (F16-F21)
│   ├── risk_controls.py        # Risk control rules (compute-only)
│   └── metrics.py              # Sortino / Calmar / IC statistics
├── src/cpp/
│   ├── etf_core.cpp            # Unified C++ acceleration module (8 functions, ~1,100 lines)
│   └── pyi/etf_core.pyi        # Type stubs
├── tests/                      # 54 unit tests
├── notebooks/
│   └── etf_pattern_matching_demo.ipynb  # Interactive demo (GPT-5.6-Sol reviewed)
├── verify_etf_core.py          # Python/C++ parity verification
├── verify_batch.py             # Batch pattern matching verification
└── CLAUDE.md                   # Development notes and pybind11 lessons
```

```mermaid
flowchart LR
    A["Archived V3.3.py"] --> B["src/core: compute-only Python"]
    B --> C["src/cpp: pybind11 C++20 Acceleration"]
    B --> D["tests: Python behavior tests"]
    C --> E["verify_etf_core.py: C++ vs Python Parity"]
    C --> F["verify_batch.py: Batch parity + performance"]
```

## FAQ

### Is this a trading system?

No. This repository demonstrates extracting compute-only modules from a quantitative strategy and accelerating them with pybind11 and C++20.

### Why is batch speedup (2.2x) much lower than single-call speedup (53x)?

Single-call pattern matching measures the hot compute kernel in isolation. Batch matching includes orchestration, data movement, validation, and Python/C++ boundary costs. The precomputed window cache helps, but end-to-end throughput is bounded by these overheads.

### Does it depend on the JuE (掘金) SDK?

No. The extracted `src/core` modules contain only computational logic and require only NumPy.

### Where is the original V3.3.py?

The original strategy is an archived baseline from the parent Chinese-language project. This repository keeps the extracted computation layer, tests, and C++ acceleration module — not the full platform-bound strategy.

### Can I rerun the original backtest?

No. The original V3.3 is a frozen baseline that depends on the JuE platform and is outside this repository's scope. This project focuses on code extraction and refactoring, C++ acceleration, and parity verification.

## Original Source and Scope

This project was extracted from **Pattern Matching ETF Strategy V3.3** (an archived 3,836-line baseline). The original strategy is a weekly, long-only ETF rotation strategy (DTW + cosine pattern matching → RF/SVM stacking → multi-layer risk controls), and was backtested on the JuE platform from 2020 to 2026.

**What this repository contains:**

- Extracted compute-only Python modules `src/core/`
- pybind11/C++20 acceleration module `src/cpp/`
- 54 unit tests + 2 verification scripts
- Build configuration and development documentation

**What this repository does NOT contain:**

- The original platform-bound strategy file
- JuE SDK bindings or live trading code
- Backtest results or strategy performance claims

## Toolchain

- Python 3.12.7 + NumPy
- pybind11 3.0.4
- MSVC 19.51 (Visual Studio 2026 Community) + CMake 3.20
- C++20

## Model Responsibilities and Review

| Author | Contributions | Reviewed by |
|------|------|------|
| DeepSeek-V4-Pro | 6 Python modules + C++ skeleton + tests + documentation | Kimi + GPT-5.5 |
| Kimi-K2.7-Code | C++ `pattern_match_batch` + comprehensive GIL-release coverage + batch API contract consolidation + edge-case tests | GPT-5.5 |

All source files are annotated with model provenance.

## Related Projects

| Project | Relationship |
|------|------|
| [**AI Collaboration Framework**](https://github.com/redamancy231-create/ai-collaboration-framework) | **Upstream methodology** — multi-model review, passive observation, and project closure protocols originate from this framework |
| [**Independent Review Toolkit**](https://github.com/redamancy231-create/independent-review-toolkit) | **Source of the review methodology** — the four-round Kimi + GPT-5.5 cross-backend review followed this toolkit's SOP |
| [**Prompt-TDD Methodology**](https://github.com/redamancy231-create/prompt-tdd-methodology) | **Sibling project** — controlled experiment methodology for prompt engineering; this project applies similar methodological rigor to pybind11/C++ hybrid programming |
| [**M&A Case Study Pipeline**](https://github.com/redamancy231-create/ma-case-study-pipeline) | **Sibling project** — multi-model academic production pipeline; it likewise emphasizes the transferability of the methodology and cross-backend verification |
| [**DOCX Pipeline**](https://github.com/redamancy231-create/docx-pipeline) | **Sibling project** — Chinese-language DOCX pipeline with dual-backend processing and Mermaid rendering |
| [**Claude Skills**](https://github.com/redamancy231-create/claude-skills) | **Sibling project** — 3 battle-tested Claude Code Skills extracted from real project workflows |

## Detailed Documentation

Development notes and pybind11 lessons: [CLAUDE.md](../CLAUDE.md) — build details, ABI troubleshooting, GIL management, floating-point tolerances, and review traceability.
