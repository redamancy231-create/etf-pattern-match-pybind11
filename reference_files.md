# Key File Index

> Last updated: 2026-07-04

## Code
- [dtw.py](src/core/dtw.py) — DTW distance + sequence standardization
- [pattern_match.py](src/core/pattern_match.py) — pattern matching engine (15-dimensional features)
- [technical.py](src/core/technical.py) — ADX / ATR / sector rotation
- [market_features.py](src/core/market_features.py) — F16-F21 market environment features
- [risk_controls.py](src/core/risk_controls.py) — risk control rules (pure computation)
- [metrics.py](src/core/metrics.py) — Sortino / Calmar / IC statistics
- [etf_core.cpp](src/cpp/etf_core.cpp) — unified C++ acceleration module (7 functions)
- [etf_core.pyi](src/cpp/pyi/etf_core.pyi) — C++ type stubs

## Verification
- [test_dtw.py](tests/test_dtw.py) — DTW module tests (27 tests)
- [test_technical.py](tests/test_technical.py) — technical indicator tests (12 tests)
- [test_pattern_match.py](tests/test_pattern_match.py) — pattern matching tests (15 tests)
- [verify_etf_core.py](verify_etf_core.py) — C++ vs Python consistency verification
- [verify_batch.py](verify_batch.py) — batch pattern matching verification

## Build
- [CMakeLists.txt](CMakeLists.txt) — top-level CMake configuration
- [src/cpp/CMakeLists.txt](src/cpp/CMakeLists.txt) — C++ subdirectory CMake

## Documentation
- [CLAUDE.md](CLAUDE.md) — complete project documentation
- [README.md](README.md) — GitHub homepage
- [project_status.md](project_status.md) — project status
- [修订方案_v2.md](修订方案_v2.md) — implementation plan revised after dual review
- [初始方案.md](初始方案.md) — initial design plan

## Original Sources
- V3.3.py — original strategy (archived baseline)
- V3.6-Decoupled.py — decoupled architecture reference
