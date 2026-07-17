You are adding C++ native tests for the "etf-pattern-match-pybind11" project. Source code is at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the C++ source file src/cpp/etf_core.cpp to understand the 8 core functions, then implement the following.

## Task: Add doctest-based C++ native tests

### What to create

1. **`tests/test_etf_core.cpp`** — doctest test file with tests for all 8 C++ functions:

   Required test cases for each function:
   - empty input (return value, no crash)
   - single-element input
   - NaN/Inf inputs (verify policy: rejection or propagation)
   - extreme values (very large/small numbers)
   - known-answer case (compute expected result by hand or from existing Python verify script)
   - For DTW: tie behavior, boundary window behavior
   - For pattern_match_single: invalid T_idx (out of bounds)

2. **`tests/CMakeLists.txt`** — CMake config for building and running the test:
   - Link against doctest (header-only, download or use FetchContent)
   - Link against the existing etf_core library
   - Add a `test_native` target

### Requirements

- Use `doctest` framework
- Test algorithmic correctness, not Python binding layer (that's tested elsewhere)
- Document the expected NaN/Inf policy explicitly in comments
- Include provenance comment: "GPT-5.6-Sol (via Codex CLI), 2026-07-17"
- Match existing code style (C++20, same includes/conventions as etf_core.cpp)

### What NOT to do

- Don't modify etf_core.cpp or CMakeLists.txt in project root
- Don't run the tests
- Don't add Python test files

### Output

Write the complete new files.
