# Performance Analysis Article — Independent Review (Kimi)

**Reviewer:** Kimi (zero-involvement, adversarial)  
**Article reviewed:** `docs/performance-analysis.md`  
**Date:** 2026-07-12

---

## Review Verdict

**Overall:** NEEDS REVISION

The article is structurally sound and mostly accurate, but it contains a material rounding-chain error in the Amdahl ceiling calculation and an inaccurate feature-range claim (F16–F21) that contradicts the actual code. These need to be fixed before publication.

---

## A: Mathematical Correctness

- **A1: PASS** — `S = 1 / ((1-p) + p/s)` is the standard Amdahl’s Law form and is stated correctly.

- **A2: PASS** — The rearrangement `p = (S-1) × s / ((s-1) × S)` is algebraically correct. With S=2.2, s=58:
  - `p = (1.2 × 58) / (57 × 2.2) = 69.6 / 125.4 = 0.5550239...`
  - Rounds to `0.56`. Subsequent use of 56% / 44% is consistent with this rounded value.

- **A3: FAIL** — The ceiling is overstated because of a rounding chain.
  - From the **exact** `p = 0.5550239...`, `S_max = 1 / (1-p) = 1 / 0.4449761... ≈ 2.2473`.
  - Rounded to one decimal place this is **2.2×**, not 2.3×.
  - The article obtains 2.3× by first rounding `p` up to 0.56, then computing `1 / 0.44 ≈ 2.27...` and rounding again. This double-rounding inflates the apparent ceiling.
  - **Quote:** "S_max = 1 / (1-p) = 1 / 0.44 ≈ 2.3×"
  - **Why it’s wrong:** It substitutes the rounded fraction `0.44` for the exact `(1-p)`, making the ceiling look ~4.5% higher than the value implied by the raw S=2.2, s=58 inputs.
  - **Suggested fix:** Compute the ceiling from the unrounded `p`: `S_max ≈ 2.25×` (or, if rounding to one decimal, `2.2×`). Then revise the "close to the approximately 2.3× ceiling" wording accordingly.

- **A4: PASS** — Solving `10 = 1 / ((1-p) + p/58)` gives `p = 0.9 × 58 / 57 = 0.915789... ≈ 0.916`. Correct.

- **A5: PASS with NOTE** — `28 / 58 = 0.482758... ms`. Rounded to one decimal place this is `0.5 ms`; `22 + 0.482758... = 22.482758... ms`, which rounds to `22.5 ms`. The approximations are acceptable as one-decimal-place rounded values, but a more honest presentation would state `≈ 0.48 ms` or explicitly note that `0.5 ms` is a one-decimal rounding.

- **A6: PASS** — The Chinese translation reproduces the same derivations as the English section; no discrepancies were found.

---

## B: Wording Honesty

- **B1: PASS** — The article clearly labels the 44% breakdown as an "Amdahl-equivalent estimate" and explicitly states it is "not a directly measured profiler breakdown." The follow-up paragraph reinforces that the numbers are for identifying optimization targets, not precision measurement.

- **B2: FAIL** — The pybind11 call-overhead number is presented as a general fact without any source.
  - **Quote:** "A cross-language call has a fixed cost, commonly on the order of roughly 0.5–2 µs depending on signature, conversions, platform, and build."
  - **Why it’s wrong:** No citation, benchmark, or project-specific measurement supports this range. The qualifier "commonly" does not remove the need for a source.
  - **Suggested fix:** Either cite a source (e.g., pybind11 documentation or a measured benchmark) or rephrase as an illustrative assumption: "As a rule-of-thumb illustration, cross-language calls are often said to cost on the order of ..."

- **B3: FAIL** — This claim depends on the incorrect A3 ceiling.
  - **Quote:** "The observed **2.2×** is already close to the approximately **2.3×** ceiling implied by the current architecture."
  - **Why it’s wrong:** Because the true ceiling from the raw data is closer to **2.25×** (or 2.2× rounded to one decimal), the gap is much smaller than the sentence implies. "Close" becomes misleading when the ceiling itself is overstated.
  - **Suggested fix:** Recalculate the ceiling from unrounded `p` and adjust the comparison; e.g., "The observed 2.2× is already within rounding error of the approximately 2.25× ceiling."

- **B4: PASS** — The decomposition section uses estimate language ("~15%", "estimates", "practical decomposition") and avoids strong causation claims.

- **B5: PASS with NOTE** — The article generally scopes claims to "this workload" and "this project." The only mildly over-general sentence is in §5.1: "pybind11 excels at compute-heavy, call-sparse workloads." While broadly true, it is not supported by data in this article. It is acceptable as a mild framing sentence because the surrounding context immediately returns to the specific workload.

- **B6: PASS** — Limitations are stated: synthetic data, single machine, workload-specific, not a trading benchmark, absolute timings will vary.

---

## C: Code Consistency

- **C1: PASS** — The article’s §3 table matches the README table:
  - DTW: 125 µs / 2.9 µs / 43×
  - Single match: 15.3 ms / 0.3 ms / 58×
  - Batch: 50 ms / 23 ms / 2.2×

- **C2: PASS** — Python 3.12.7, MSVC 19.51, pybind11 3.0.4 all match the README/toolchain details.

- **C3: PASS** — Both `verify_etf_core.py` and `verify_batch.py` exist in the repository root.

- **C4: FAIL** — The feature range F16–F21 is inaccurate.
  - **Quote:** "Python-side feature computation | ~6% | F16–F21 market-environment features not ported to C++" (and the equivalent Chinese sentence).
  - **Why it’s wrong:** `src/core/market_features.py` only defines **four** market-environment features: F16 (`compute_market_volatility`), F17 (`compute_size_relative_strength`), F20 (`compute_volume_anomaly`), and F21 (`compute_vol_change`). There are no F18 or F19 functions in the current codebase.
  - **Suggested fix:** Change "F16–F21" to "F16, F17, F20, F21" or "selected F16–F21 market-environment features (F18–F19 are not present in the extracted module)."

- **C5: PASS** — `FEATURE_KEYS` in `etf_core.cpp` contains exactly 15 entries, matching the article’s "15-dimensional features" claim.

- **C6: PASS** — `etf_core.cpp` exposes exactly 7 `m.def()` bindings: `standardize_returns`, `cosine_similarity`, `dtw_distance`, `compute_adx`, `compute_atr`, `pattern_match_single`, `pattern_match_batch`.

---

## Additional Observations

1. **"Collapses by roughly 26-fold"** in §1 is mathematically defensible (`58 / 2.2 ≈ 26.4`), but the phrasing could be read as implying the 58× result is wrong. The article immediately clarifies that this is expected, so it is acceptable.

2. **Visualization section (§6):** The proposed 50/50 split of the optimized bar (`C++ compute 11.5 ms` / `Python overhead 11.5 ms`) is described as a presentation-oriented split distinct from the 56%/44% Amdahl estimate. This distinction is clearly stated and should prevent misreading.

3. **Chinese translation quality:** Accurate and consistent with the English text. The technical terms are well preserved.

4. **README vs. article scope:** The README says the batch speedup is "2.2x" and the article explains why; the two documents are mutually consistent.
