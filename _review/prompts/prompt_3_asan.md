You are adding ASAN/UBSAN configuration for the "etf-pattern-match-pybind11" project at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the existing CI file at .github/workflows/ci.yml and the CMakeLists.txt to understand the current setup.

## Task: Add sanitizer build job to CI

### What to create/modify

1. **New file: `.github/workflows/sanitizer.yml`** — A separate CI workflow (not modifying the main ci.yml) that:
   - Runs on `ubuntu-latest` only (sanitizers are best supported on Linux/GCC)
   - Installs g++, cmake, and Python 3.12
   - Installs numpy, pybind11, pytest
   - Builds with sanitizer flags: `-fsanitize=address,undefined -fno-omit-frame-pointer`
   - Runs Python tests under the sanitized build
   - Uses `ASAN_OPTIONS=detect_leaks=1:halt_on_error=1` env var
   - Trigger: on push to master and pull requests (same as main CI)
   - Name: "Sanitizer (ASAN+UBSAN)"

2. **Optionally modify `CMakeLists.txt`** to accept a `-DUSE_SANITIZERS=ON` flag that adds the sanitizer compiler flags. If modifying CMakeLists.txt is too complex, just set CXXFLAGS in the workflow YAML directly.

### Requirements

- Don't modify the main ci.yml — this is a SEPARATE workflow file
- Don't add sanitizer tests that duplicate the existing Python tests
- The sanitizer job should run the existing Python test suite under the sanitized build
- Provenance comment at top: "GPT-5.6-Sol (via Codex CLI), 2026-07-17"

### What NOT to do

- Don't add to the main ci.yml
- Don't create new test files
- Don't run the CI

### Output

Write the complete new files.
