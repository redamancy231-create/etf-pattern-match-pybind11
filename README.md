# Pattern Matching ETF Strategy — Python+C++ Hybrid Programming Refactor

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-20-00599C)](https://en.cppreference.com/)
[![pybind11](https://img.shields.io/badge/pybind11-3.0.4-green)](https://github.com/pybind/pybind11)
[![tests](https://img.shields.io/badge/tests-54%20passed-brightgreen)](tests/)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Pure computation modules were extracted from a 3,836-line pure Python quantitative strategy, with core algorithms accelerated using **pybind11 + C++20**. The algorithm logic is unchanged: the goal is to practice Python+C++ hybrid programming, not to improve backtest performance.

## Quick Start

```bash
# Compile C++ module
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release

# Verify C++ vs Python consistency
python verify_etf_core.py

# Run tests
python -m pytest tests/ -v
```

## Acceleration Results

| Function | Python | C++ | Speedup |
|------|--------|-----|--------|
| DTW Distance (L=19) | 125 µs | 2.9 µs | **43x** |
| Pattern Matching (single ETF at one timestamp) | 15.3 ms | 0.3 ms | **58x** |
| Batch Pattern Matching (100 timestamps) | 50 ms | 23 ms | **2.2x** |

## Project Structure

```
├── src/core/                  # Python pure computation layer (6 modules, zero JuE SDK dependency)
│   ├── dtw.py                  # DTW distance + sequence standardization
│   ├── pattern_match.py        # Pattern matching engine (15-dimensional features)
│   ├── technical.py            # ADX / ATR / sector rotation
│   ├── market_features.py      # Market environment features (F16-F21)
│   ├── risk_controls.py        # Risk control rules (pure computation)
│   └── metrics.py              # Sortino / Calmar / IC statistics
├── src/cpp/
│   ├── etf_core.cpp            # Unified C++ acceleration module (7 functions, ~1,000 lines)
│   └── pyi/etf_core.pyi        # Type stubs
├── tests/                      # 54 unit tests
├── verify_etf_core.py          # C++ vs Python consistency verification
├── verify_batch.py             # Batch pattern matching verification
└── CLAUDE.md                   # Full project documentation
```

## Original Source

Extracted from Pattern Matching ETF Strategy V3.3 (archived baseline, 3,836 lines). The original strategy is a weekly ETF long-only rotation strategy (DTW + cosine pattern matching → RF/SVM Stacking → multi-layer risk controls), backtested on the JuE platform over 2020-2026.

## Toolchain

- Python 3.12.7 + NumPy
- pybind11 3.0.4
- MSVC 19.51 (Visual Studio 2026 Community) + CMake 3.20
- C++20

## Model Responsibilities and Review

| Author | Delivery | Review |
|------|------|------|
| DeepSeek-V4-Pro | 6 Python modules + C++ skeleton + tests + documentation | Kimi + GPT-5.5 |
| Kimi-K2.7-Code | C++ `pattern_match_batch` + full GIL coverage + batch contract convergence + boundary tests | GPT-5.5 |

All source files are annotated with model provenance.

## Detailed Documentation

See [CLAUDE.md](CLAUDE.md): build details, pybind11 lessons learned, ABI troubleshooting, GIL management, floating-point tolerances, and review traceability.
