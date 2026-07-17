You are adding a minimal usage example for the "etf-pattern-match-pybind11" project at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the existing code to understand the API (especially the C++ bindings in src/cpp/etf_core.cpp PYBIND11_MODULE section and the .pyi stub), then create a quickstart example.

## Task: Create `examples/quickstart.py`

A 15-25 line Python script that demonstrates the core workflow for a user who just ran `pip install`:

### What the script should do

1. Import `etf_core`
2. Generate a small random price series (e.g., `np.random.randn(100).cumsum() + 100`)
3. Call `dtw_distance` with two sub-series
4. Call `cosine_similarity` with two feature vectors
5. Call `pattern_match_single` with a price series and a T_idx
6. Call `pattern_match_batch` with a price series and multiple T_idx values
7. Print results with labels (e.g., "DTW distance: 12.34")
8. Include a comment at top: "# Quickstart example for etf_core — pip install etf-pattern-match-pybind11 && python examples/quickstart.py"

### Requirements

- No external data files needed — generate random data inline
- Use `numpy` for data generation
- Include the provenance comment: "# Provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17"
- Create `examples/` directory if it doesn't exist
- PEP 8, UTF-8 encoding

### What NOT to do

- Don't create a notebook
- Don't import from src/ (only from installed etf_core package)
- Don't run the script
- Don't require external data files

### Output

Write the complete new file.
