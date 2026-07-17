You are adding multi-platform CI for the "etf-pattern-match-pybind11" project. Source code is at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the existing CI file at .github/workflows/ci.yml to understand the current setup, then modify it.

## Task: Add Linux and macOS to CI matrix

### What to change

Edit `.github/workflows/ci.yml`:

1. Add `ubuntu-latest` and `macos-latest` to the `os` matrix (currently only `windows-latest`)
2. Handle compiler differences:
   - Linux: use GCC or Clang via `apt-get install g++ cmake`
   - macOS: use AppleClang via `brew install cmake` (Xcode CLT provides clang)
   - Windows: keep existing MSVC setup
3. Install pybind11 on all platforms (`pip install pybind11` is cross-platform)
4. Keep all existing steps: build, test, verify_etf_core.py, verify_batch.py
5. Ensure PYTHONIOENCODING=utf-8 is set on all platforms

### Requirements

- Use `fail-fast: false` (already set — keep it)
- Don't add new Python versions — keep 3.12 only
- Don't add artifact publishing or wheel building — just compilation + test + verify
- Add provenance comment: "GPT-5.6-Sol (via Codex CLI), 2026-07-17" at top of file

### What NOT to do

- Don't change the existing Windows setup
- Don't add new test files
- Don't run the CI

### Output

Write the complete updated ci.yml file.
