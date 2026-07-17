# Quickstart example for etf_core — pip install etf-pattern-match-pybind11 && python examples/quickstart.py
# Provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17

import etf_core
import numpy as np

rng = np.random.default_rng(42)
prices = rng.standard_normal(100).cumsum() + 100.0

dtw = etf_core.dtw_distance(prices[10:20], prices[20:30])
feature_a = np.array([0.5, -0.2, 1.0])
feature_b = np.array([0.4, -0.1, 0.8])
cosine = etf_core.cosine_similarity(feature_a, feature_b)

params = {"k": 5, "L_query": 10, "T_back": 60, "M_forward": 3}
single = etf_core.pattern_match_single(prices, T_idx=80, **params)
t_indices = np.array([70, 80, 90], dtype=np.int64)
batch, valid = etf_core.pattern_match_batch(prices, t_indices, **params)

print(f"DTW distance: {dtw:.4f}")
print(f"Cosine similarity: {cosine:.4f}")
print("Single-match features:", single)
print("Batch feature matrix:", batch)
print("Batch valid mask:", valid)
