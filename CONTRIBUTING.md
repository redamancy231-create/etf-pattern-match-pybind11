# Contributing

Thanks for your interest! This is a programming practice project — contributions that improve reproducibility, documentation, or cross-platform support are welcome.

## Scope

**In scope:**
- Reproducibility improvements (build system, CI, benchmark methodology)
- Documentation fixes and translations
- New tests for edge cases
- Cross-platform build support

**Out of scope:**
- Strategy performance optimization (this is a sealed baseline extraction)
- Live trading features
- New factors or signals (the algorithm is frozen from V3.3)

## Development Setup

```bash
# Install from source
git clone https://github.com/redamancy231-create/etf-pattern-match-pybind11.git
cd etf-pattern-match-pybind11
pip install -e .

# Or via CMake directly
cmake -B build -DPython_EXECUTABLE="<path-to-python.exe>"
cmake --build build --config Release
```

## Testing

```bash
# Run all tests (54 tests, ~0.3s)
python -m pytest tests/ -v

# Verify C++ vs Python output equivalence
python verify_etf_core.py
python verify_batch.py

# Run reproducible benchmarks
python benchmarks/run_benchmark.py
```

## Pull Request Checklist

- [ ] `pytest tests/` passes (54 tests)
- [ ] `python verify_etf_core.py` passes (5/5 equivalence checks)
- [ ] New code follows existing style (C++20, snake_case Python, bilingual comments)
- [ ] No algorithmic changes to `src/core/` or `src/cpp/etf_core.cpp` (sealed baseline)
- [ ] Build works on your platform (document any platform-specific notes)

## Supported Platforms

| Platform | Python | Compiler | Status |
|----------|--------|----------|--------|
| Windows 11 x64 | 3.10–3.12 | MSVC 19.51+ | ✅ Primary |
| Ubuntu/Linux x64 | 3.10–3.12 | GCC 11+ / Clang 16+ | ⚠️ Best effort |
| macOS | — | — | ❌ Not tested |

## License

MIT. By contributing, you agree that your contributions will be licensed under the same terms.
