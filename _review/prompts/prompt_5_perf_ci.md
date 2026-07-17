You are adding a performance regression CI workflow for the "etf-pattern-match-pybind11" project at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read these files to understand the existing setup:
- benchmarks/run_benchmark.py (the existing benchmark script)
- benchmarks/results/ (baseline JSON files)
- .github/workflows/ci.yml (main CI structure)

## Task: Add performance regression detection to CI

### What to create

**New file: `.github/workflows/benchmark.yml`** — A CI workflow that:

1. **Runs on push to master** (not PRs — only detect regressions after merge)
2. Builds the C++ module (same as main CI)
3. Runs the existing `benchmarks/run_benchmark.py` script
4. **Compares against the BASELINE in the same CI job** (not archived results from previous runs):
   - The baseline is the current `benchmarks/results/` JSON file in the repo
   - The CI run produces a new result
   - Compare median speedup values

5. **One-sided threshold: FAIL if slowdown > 15%** (speedup is always OK):
   - For each function: `if current_median > baseline_median * 1.15 → WARN`
   - For each function: `if current_median > baseline_median * 1.25 → FAIL`
   - Speedups (current_median < baseline_median) are always OK — never fail on improvements

6. **Output a summary table** in the CI log:
```
Function              Baseline    Current     Change
dtw_distance          2.8 us      3.1 us      +10.7% WARN
pattern_match_single  264.6 us    270.1 us    +2.1%  OK
```

7. **Update the baseline** after successful runs: if no regressions detected, commit the new JSON as the new baseline. Use `git config` and `git push` within the workflow (set `contents: write` permission).

### Requirements

- Use `ubuntu-latest` (most consistent CPU for benchmarking)
- Python 3.12, numpy, pybind11 (same as main CI)
- Build in Release mode
- Run benchmark with `--repeat 50` (fewer runs for CI speed; production benchmarks use 100)
- Provenance comment at top: "GPT-5.6-Sol (via Codex CLI), 2026-07-17"
- Add `permissions: contents: write` for baseline auto-update

### What NOT to do

- Don't add this to the main ci.yml — it's a SEPARATE workflow
- Don't block PRs — only run on push to master
- Don't create new benchmark scripts — reuse `benchmarks/run_benchmark.py`
- Don't run the CI

### Output

Write the complete new workflow file.
