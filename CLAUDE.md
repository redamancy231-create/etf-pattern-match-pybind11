# CLAUDE.md — Pattern Matching ETF Strategy pybind11 Refactor

> **Model provenance**: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> **Review**: Kimi-K2.7-Code (Devil's Advocate + code improvements) + GPT-5.5 via Codex CLI (completeness), 2026-07-03 / 2026-07-04

## Project Positioning

Pure computation modules were extracted from `形态匹配ETF策略/V3.3.py` (a 3,836-line pure Python quantitative strategy) and accelerated using pybind11 + C++20. **The algorithm logic is unchanged**: the goal is to improve proficiency in Python+C++ hybrid programming, not to improve backtest performance.

- Original project: CLOSED (V3.3 Round 4 is the archived baseline), backtests must not be rerun
- This project: an independent programming practice repository, clearly separated from the original project
- Pure computation modules: zero JuE SDK (掘金 SDK) dependencies, requiring only numpy

## Quick Start

```bash
# Compile C++ module
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release

# Verify
python verify_etf_core.py

# Test
PYTHONIOENCODING=utf-8 python -m pytest tests/ -v
```

## Project Structure

```
├── src/core/                  # Python pure computation modules (no JuE SDK dependency)
│   ├── dtw.py                 # DTW distance + sequence preprocessing
│   ├── technical.py           # ADX / ATR / sector rotation
│   ├── pattern_match.py       # Pattern matching engine (15-dimensional features)
│   ├── market_features.py     # F16-F21 market environment features
│   ├── risk_controls.py       # Risk control rules (pure computation)
│   └── metrics.py             # Sortino / Calmar / IC statistics
├── src/cpp/
│   ├── etf_core.cpp           # Unified C++ module (7 functions)
│   └── pyi/etf_core.pyi       # Type stubs
├── tests/                     # 54 tests, 0 failures
├── verify_etf_core.py         # C++ vs Python consistency verification
├── CMakeLists.txt
└── CLAUDE.md
```

## Build

### Dependencies
- Python 3.12.7 + numpy
- pybind11 3.0.4 (`pip install pybind11`)
- MSVC 19.51 (Visual Studio 2026 Community) + CMake 3.20+

### Compilation Options
- MSVC Release: `/O2 /utf-8 /wd4819`
- Python path is injected via `-DPython_EXECUTABLE=...`, not hardcoded
- C++20 standard

### ABI Troubleshooting
```bash
# 1. Python ABI tag
python -c "import sys; print(f'cp{sys.version_info.major}{sys.version_info.minor}-{sys.platform}')"

# 2. .pyd filename must match PYBIND11_MODULE name
ls build/Release/Release/*.cp312-win_amd64.pyd

# 3. Do not mix Release/Debug
```

## Performance (relative to the original V3.3.py, MSVC /O2)

| Function | Python | C++ | Speedup |
|------|--------|-----|--------|
| DTW (L=19) | 124.8 µs | 2.9 µs | **43.3x** |
| pattern_match_single | 15.3 ms | 0.3 ms | **58.4x** |
| pattern_match_batch (100 T_idx) | 50.0 ms | 22.8 ms | **2.2x** |

## Key pybind11 Lessons

### Number of py::arg() Entries = Number of Function Parameters ★★★★★
Parameters with default values must also be declared, consistent with pybind11-demo.

### GIL Release ★★★★★
- `dtw_distance` / `compute_adx` / `pattern_match_single` / `pattern_match_batch`: all 4 long-running computation functions explicitly release the GIL (`py::gil_scoped_release`) inside the pure C++ computation section and reacquire it before returning values
- `pattern_match_single` uses a `std::optional` + lambda pattern to resolve conflicts between early returns and GIL release: all `py::none()` returns happen while holding the GIL, and `py::dict` construction happens while holding the GIL
- `compute_atr` / `standardize_returns` return Python objects (`ArrD`), with GIL management handled automatically by the pybind11 call boundary
- Ensure the GIL is held before constructing Python return values

### dtype Contract ★★★★★
```cpp
using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;
```
- `forcecast` automatically converts non-strictly matching dtypes
- `py::ssize_t` indexing (MSVC-compatible)

### Stable Return Structure ★★★★★
- `pattern_match_single` returns `py::dict` or `py::none()`
- The 15 keys have a fixed order, fully matching the Python version
- `n_matches_above_thresh` returns int (same as the Python version)
- `pattern_match_batch` returns `(features_X15, valid_mask)` (v4 convergence: feature_keys promoted to module constant `etf_core.FEATURE_KEYS`)

### Parameter Validation ★★★★
- `match_step <= 0` → `std::invalid_argument`, preventing infinite loops
- `t_indices` must be strictly increasing and pass range validation
- `high/low/close` length consistency validation (`compute_atr` / `compute_adx`)

### CMake-Friendly Errors ★★★
- If `Python_EXECUTABLE` is not set, output a WARNING + example command
- If `pybind11` is not found, output FATAL_ERROR + installation/configuration guidance instead of raw CMake errors

### Floating-Point Tolerances ★★★★
| Object | Tolerance |
|------|------|
| standardize_returns | 1e-10 |
| cosine_similarity | 1e-10 |
| DTW Distance | 1e-8 |
| pattern_match score | 1e-6 |
| ADX | 1e-10 |

### UTF-8 ★★★
- Source code is saved as UTF-8
- Prefer compilation option `/utf-8`, with `/wd4819` as fallback

## Review Traceability

| Round | Model | Angle | Key Findings |
|------|------|------|---------|
| R1 | Kimi-K2.7-Code | Devil's Advocate | Speedup overestimated → revised; three modules merged; overall Amdahl speedup 1.6-2.5x |
| R2 | GPT-5.5 via Codex | Completeness | Missing pattern_match_batch; dtype/exception contracts; F12-F15 tests; CLAUDE.md specification |
| R3 | Kimi-K2.7-Code | Code Improvements | Full GIL coverage + batch contract convergence + CMake-friendly errors + match_step guard + boundary tests (52→54) |

## Related Projects

- Parent project (形态匹配ETF策略 V3.3) — archived baseline (CLOSED)
- pybind11-demo — source of pybind11 experience (CLOSED)
