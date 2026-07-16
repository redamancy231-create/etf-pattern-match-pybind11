# Changelog

## [1.0.0] — 2026-07-04 (revised 2026-07-12)

### 2026-07-12 Refactor

- GPT-5.6-Sol full code review: 32 findings (9 P0 + 4 P1 + 8 P2 + 5 P3 + 6 P4) — all fixed
- Kimi-K2.7-Code adversarial regression audit: 0 regressions, 7/7 high-risk changes verified
- Key fixes: DTW rolling array `prev[0]` bug, shared `pattern_match_core`, GIL release coverage, NaN window-level checks, ADX initialization alignment
- scipy → pure NumPy `rankdata` (resolved CI dependency failure)
- Performance numbers re-benchmarked and synced across all 8 references (README, CLAUDE.md, notebook, social preview, etc.)
- Review prompt archive in `审查提示词/` (excluded from published repo per `.gitignore`)

### Initial Release

- pybind11/C++20 acceleration of ETF pattern-matching core
- DTW distance: 98µs → 2.7µs (37x speedup)
- Pattern match: 14.3ms → 0.23ms (61x speedup)
- Batch pattern match: 2.2x end-to-end (100 calls)
- 6 extracted pure-computation Python modules (`src/core/`)
- 8-function unified C++ acceleration module (`src/cpp/etf_core.cpp`, ~1,100 lines)
- 54 unit tests + 2 verification scripts
- Interactive Jupyter demo notebook (31 cells, GPT-5.6-Sol reviewed)
- Performance analysis article (`docs/performance-analysis.md`, bilingual)
- 4-round Kimi + GPT-5.5 cross-backend independent review
- CI: GitHub Actions (Windows, MSVC Release)
- Bilingual README (Chinese + English)
