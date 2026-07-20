# Comprehensive Analysis of Modification Directions for the etf-pattern-match-pybind11 Fork

> Generated: 2026-07-20 · Revised: 2026-07-21
> Model provenance: DeepSeek-V4-Pro (via Claude Code CLI) · Review: GPT-5.6-Sol (via Codex CLI)
> Based on: Full source code from the project README/CLAUDE.md/src + project_status.md
> Review report: `_review/conclusions/GPT-5.6-Sol_fork-directions-review_2026-07-21.md`

## Project Status at a Glance

- **Core**: Extracted pure computational modules from the 3,836-line ETF pattern matching strategy V3.3 and accelerated them with pybind11 + C++20
- **Acceleration**: Single DTW call 34× (96µs→2.8µs) / single pattern matching call 53× (14.0ms→0.26ms) / batch API overhead reduced by 2.2× (100 individual C++ calls → 1 C++ batch call); end-to-end Python batch vs C++ batch performance is approximately 93× (see benchmark JSON)
- **Algorithm**: Cosine pre-filtering → DTW reranking → combined score (0.5×norm_dtw + 0.5×norm_cos) → 15-dimensional features
- **Modules**: 6 pure-computation Python modules + 1 unified C++ acceleration module (8 functions, ~1,100 lines)
- **Tests**: 54 unit tests + 2 verification scripts + interactive Notebook
- **Toolchain**: MSVC 19.51 + pybind11 3.0.4 + C++20 + CMake 3.20+
- **License**: MIT (covers only the code published in this repository; licenses for external SDKs, data sources, and third-party models must be reviewed separately)
- **Explicitly excluded**: Live trading code, GmQuant SDK bindings, and backtesting results/performance claims (this repository does not provide such conclusions; forks may add related functionality but must independently disclose data sources, sample periods, transaction cost assumptions, and validation methods)

---

## Prerequisites / Assumed Knowledge

This document assumes that fork contributors:
- Are familiar with Python/NumPy and basic C++
- Understand basic pybind11 concepts (GIL management, `py::array_t`, `py::object`)
- Can read CMake build configurations
- Have a basic understanding of look-ahead bias, time-series cross-validation (purged k-fold), and transaction costs in quantitative finance

For directions marked as "requires external materials" or "requires platform access," the document explicitly lists the blockers. **Before starting work, review the prerequisites for each direction—even directions marked as having "low" or "medium" effort may have unresolved prerequisites.**

---

## 1. Algorithm Core Directions

### 1.1 Replacing DTW with Variants

The current implementation uses standard DTW + a Sakoe-Chiba band (window=5). `dtw_distance_span()` is a pure function with a clean interface, making replacement of the distance metric the lowest-barrier fork direction.

| Variant | Applicable Scenario | Implementation Complexity | Key Risks |
|------|---------|-----------|---------|
| **Derivative DTW (DDTW)** | Match pattern "shape" rather than absolute level by first differencing the series and then applying DTW | Low (preprocessing only) | Differencing amplifies noise; numerical stability must be verified on short series (L≈19) |
| **Weighted DTW** | Weight recent data points more heavily to reflect the market intuition that "recent observations matter more" | Low (add a weighting factor to the DP recurrence) | The weight decay rate is an additional hyperparameter; weights may be discontinuous at window boundaries |
| **Soft-DTW** | Numerically differentiable (mathematically); however, **the current pybind11 functions return NumPy/float values and do not carry an automatic differentiation graph**—training use requires an additional PyTorch custom autograd implementation, JAX custom VJP, or an existing differentiable DTW library | Medium (replace the DP recurrence with softmin + integrate with a differentiation framework) | Differentiability ≠ training-ready; numerical gradient validation is required; sensitive to the γ parameter |
| **ShapeDTW** | Extract local shape descriptors first (subsequence→descriptor), then apply DTW | Medium (requires a new descriptor extraction module) | There is no universal standard for descriptor selection; subsequences are extremely short when L_query=20 |
| **FastDTW** | Approximate linear time O(L); **suitable when L_query itself is long (hundreds of points or more)**; if only T_back is increased, creating more candidates, prioritize candidate indexing and pruning rather than replacing the DTW algorithm | Medium (three-level recursion: coarsening → projection → refinement) | Approximation error vs Top-K stability requires a separate benchmark; FastDTW offers limited benefits with the current L_query=20 |

**Entry point**: C++ `src/cpp/etf_core.cpp` `dtw_distance_span()` (lines ~150-180); Python reference implementation: `src/core/dtw.py`. After modifying the algorithm, update the Python reference implementation and pass the `verify_etf_core.py` consistency verification.

**Acceptance criteria**: (a) All checks in `verify_etf_core.py` PASS; (b) add independent unit tests for the new DTW variant; (c) benchmark the variant against standard DTW for speed and Top-K recall.

### 1.2 Redesigning the Combined Score Formula

Current formula: `combined_score = 0.5 × norm_dtw + 0.5 × norm_cos`, combining equal-weight min-max normalization results.

Possible replacements:
- **Adaptive weights**: Dynamically adjust DTW/Cos weights based on the distribution of cosine candidates, such as the Gini coefficient
- **Rank aggregation**: Replace the weighted average with Spearman footrule distance or Borda count
- **Pareto frontier**: Do not combine the scores; retain the DTW and Cos dimensions and select non-dominated solutions in two-dimensional space
- **Probability calibration**: Calibrate similarity scores using **historical subsequent return statistics** from historical matches (note: this is a statistical feature, not a predicted probability—see the terminology notes in §Key Constraints and Considerations)

**Entry point**: C++ `src/cpp/etf_core.cpp:551–707` (`pattern_match_core()`, where the `Scored` struct and combined score are located at lines 680–690); Python reference implementation: `src/core/pattern_match.py:192–200`.

### 1.3 Multivariate Pattern Matching

The current implementation performs matching only on a standardized one-dimensional return series. It can be extended to multiple dimensions:
- Match simultaneously on: price trend + volume pattern + volatility pattern + ADX direction
- Extend DTW from one to multiple dimensions: `cost = Σⱼ wⱼ × (x[i][j] - y[i][j])²`
- Distance aggregation strategies: weighted sum / Pareto frontier / normalize each dimension with Mahalanobis distance before applying DTW

**Entry point**: `dtw_distance_span()` currently accepts only `const double*`. Multidimensional support requires changes to both the function signature and the DP recurrence. A new C++ multidimensional array input interface and Python-side data assembly logic are also required.

### 1.4 Accelerating Candidate Retrieval

The current cosine pre-filtering performs a full scan (`for hist_end in range(search_start, search_end+1, match_step)`). Alternatives include:
- **k-NN indexes**: Build an index over historical-window return vectors using FLANN / HNSW / FAISS—with provable recall guarantees
- **Approximate indexes (LSH)**: Explicitly disclose the recall-speed trade-off and include Top-K recall tests
- **Blockwise dot-product upper-bound pruning**: Precompute norms and use partial accumulated dot-product upper bounds for safe pruning—**this differs from simply "stopping once a satisfactory result is found"** (the latter changes the Top-K results and is approximate search rather than safe pruning)

Each retrieval method should be tested for: Top-K recall, changes in the combined score, stability of the 15-dimensional features, and end-to-end speed.

**Entry point**: The for loop under "Pass 1: cosine similarity" in `pattern_match_core()`

---

## 2. Acceleration Platform Directions

### 2.1 GPU Acceleration (CUDA/ROCm)

Batch DTW computation is naturally suited to GPUs: `dtw_distance_batch` applies a one-to-many loop between one query and N candidates, which can be mapped to a CUDA kernel.

- **CUDA C++**: Replace the CPU loop in `pattern_match_core` with a custom kernel
- **cuBLAS**: Convert cosine similarity computation into matrix multiplication (candidates × query = batched dot product)
- **Performance expectations**: The end-to-end speedup in batch scenarios **remains to be validated**—under clearly defined n_samples, candidate counts, and sequence lengths, separately measure host→device transfer, cosine, DTW, sorting, and feature aggregation time, using the current Python version as the numerical and result baseline
- **Challenges**: Control flow in `pattern_match_core` (`if cos_s > 0`, `if fut_end < T_idx`) requires warp-level branch handling on GPUs; host-device data transfers and the Python API boundary may become the dominant overhead

**Entry point**: The loops in `dtw_distance_batch()` and `pattern_match_core()`.

**Acceptance criteria**: (a) Numerically consistent with the current Python/C++ reference implementations (floating-point tolerance of 1e-6); (b) stage-by-stage benchmark report; (c) CPU fallback path; (d) Top-K and 15-dimensional feature consistency tests.

### 2.2 SIMD Vectorization

The current C++ code does not use explicit SIMD. SIMD-friendly hotspots include:
- Dot-product loop in `cosine_similarity_vec()` → `_mm512_fmadd_pd`
- Inner loop in `dtw_distance_span()` → vectorizable, but constrained by DP data dependencies
- `std::accumulate` in `standardize_returns_cpp()` → SIMD reduce
- The data structure must be changed to **SoA** (Structure of Arrays) to achieve contiguous memory access

**Critical—CPU capability dispatch**: Compiling directly with `/arch:AVX512` prevents execution on CPUs without AVX512. The implementation should include:
- Runtime CPUID detection
- AVX512 / AVX2 / scalar multilevel fallback
- Separate benchmarks for different CPUs
- SIMD vs scalar result error tests (FMA and reduction order may introduce floating-point differences, which must be verified against 1e-8/1e-6 tolerances)

**Compiler options**: MSVC `/arch:AVX512` (AVX512 path only) / GCC `-mavx512f` / handwritten intrinsics with runtime dispatch.

### 2.3 Multithreaded Batch Processing

The current `pattern_match_batch` loop over multiple T_idx values is serial (the GIL is released, but no multithreading is used).

**Recommended safe pattern** (to avoid data races and incorrect result ordering):
1. Worker threads write only C++ data and do not create Python objects
2. Preallocate a fixed location for each sample, such as `features[n_samples][15]`
3. Each thread writes only to its own sample slot
4. Keep `valid_mask` and the feature matrix aligned with the input `t_indices` order
5. After the main thread reacquires the GIL, create all NumPy return objects **in one place**
6. Add tests for concurrent correctness, stable output ordering, and exception safety

**Not recommended**: Using `gil_scoped_acquire` in worker threads and directly creating Python objects—this introduces object lifetime, thread safety, exception propagation, and Python allocator contention issues.

**Entry point**: The `for (py::ssize_t s = 0; s < n_samples; ++s)` loop in `pattern_match_batch()`.

### 2.4 pandas → Arrow Zero-Copy Integration

The current `py::array_t<double>` interface can avoid additional copies for **float64, C-contiguous** NumPy arrays. Copies may still occur in the following cases:
- `forcecast` conversion when the dtype does not match
- Non-contiguous arrays (Fortran-contiguous arrays or sliced/strided views)
- Implicit pandas DataFrame → NumPy conversion, depending on the underlying data layout and dtype

Arrow integration requires a new adapter layer; it is not merely a replacement for the call entry point. Recommendation: First benchmark the proportion of total runtime currently spent moving data, then decide whether introducing an Arrow dependency is worthwhile.

---

## 3. Strategy System Directions

### 3.1 Reintegrating with a Backtesting Framework

**Prerequisite**: The current project is a "pure computational module without platform bindings." **The following blockers must be resolved before starting work**:
- The complete original V3.3.py file **is not included in this repository**
- The original training data, model files, and label definitions **are not included in this repository**
- The original backtesting configuration (date range, transaction costs, slippage, and trading suspension rules) **is not included in this repository**

Once the prerequisites are satisfied, a fork can integrate with:

| Framework | Approach | Difficulty | Key Challenges |
|------|------|---------|---------|
| **backtrader** | Wrap `pattern_match_single` as a `bt.Indicator` subclass | **Medium¹** | Mapping T_idx to framework bar indexes, warm-up phase, weekly rebalancing vs daily bars, strict causality verification |
| **vnpy** | Implement `CtaTemplate` and call the C++ module from `on_bar()` | Medium | Requires platform API documentation and a test environment |
| **zipline-reloaded** | Implement a `CustomFactor` in pipeline API style | Medium | Adapting pipeline semantics to the 15-dimensional features |
| **bt** (Python) | Implement an `Algo` subclass that calls `pattern_match_batch` at fixed intervals | **Medium¹** | Same challenges as backtrader |
| **GmQuant platform** | Reverse-engineer and restore the platform binding layer to recover the complete executable V3.3 strategy | **High** (requires external materials) | Original file is not in the repository; requires the GmQuant SDK and a platform account |

> ¹ The original draft classified this as "low," but the review noted that GIL handling, C++ object lifetimes, multi-ETF data organization, and look-ahead-free testing are required, making the actual difficulty medium.

Core value: Transform the "C++-accelerated computational core" from a standalone demo into a strategy that can be backtested and evaluated. **The output should be described as "capable of integration with a backtesting framework," not "production-ready."** Full production readiness requires an execution layer, transaction cost modeling, and out-of-sample validation.

### 3.2 Multi-ETF Cross-Sectional Rotation

The original V3.3 is a "long-only rotation strategy" that selects the best ETF from an ETF universe based on pattern signals. The current project only provides feature extraction for a single ETF. A fork should proceed in two phases:

**Phase 1 (parallelizable)**: Independently generate the 15-dimensional features for each ETF. The current `pattern_match_batch()` accepts only a one-dimensional `prices` series for one ETF and a set of `t_indices`—a multi-ETF batch input interface is required because different ETFs may have different series lengths and missing-value policies.

**Phase 2 (not trivially parallelizable)**: After collecting features for all ETFs, perform cross-sectional rank/z-score normalization, ranking, and position decisions. This phase depends on results from all ETFs and does not consist of independent per-ETF tasks.

- **Cross-sectional comparability**: Apply rank / z-score normalization to the 15-dimensional features across ETFs
- **Ranking layer**: Use LambdaRank / XGBoost ranker to learn a mapping from F1-F15 to position weights
- **Rotation frequency**: Weekly rebalancing, consistent with the original strategy
- **Transaction cost modeling**: Market impact + commissions + stamp duty

### 3.3 Risk Control Execution Layer

Risk control code in the current project is distributed across multiple modules—it is **not a single risk control system**:

| Functionality | Actual Location | Current Status |
|------|---------|---------|
| Rolling volatility risk control (quantile-based position reduction) | `src/core/risk_controls.py` | ✅ Implemented |
| MA trend filter | `src/core/risk_controls.py` | ✅ Implemented |
| Position cap constraint | `src/core/risk_controls.py` | ✅ Implemented |
| ATR | `src/core/technical.py` / C++ module | ✅ Implemented |
| Maximum drawdown | `src/core/metrics.py` | ✅ Implemented |
| VaR | — | ❌ Not implemented |
| Stop-loss / take-profit triggers | — | ❌ Not implemented |
| Position rebalancing scheduler | — | ❌ Not implemented |
| Maximum drawdown circuit breaker (account + ETF layers) | — | ❌ Not implemented |

An **execution layer** that a fork could add, distinct from the existing **calculation layer**:
- Stop-loss / take-profit triggers: trailing stop / time stop / volatility stop
- Position rebalancing scheduler: deviation from target weight exceeds a threshold → trigger rebalancing
- Blacklist: If pattern matching fails N consecutive times → suspend trading in that ETF
- Maximum drawdown circuit breaker: Separate account-level and ETF-level limits

### 3.4 Signal Server (Microservices)

A two-layer architecture is recommended—the current `etf_core` outputs 15-dimensional features, not trading signals:

**Computation service** (directly corresponding to the current module):
- Receive price data through HTTP/gRPC → return 15-dimensional features + version information
- Use Redis to cache precomputed windows and intermediate results
- Define the API schema, parameter versions, data timestamps, and cache invalidation policy

**Strategy service** (requires additional implementation):
- Receive features for multiple ETFs → execute ranking, risk control, and rebalancing rules → output signals and explanations
- Signal thresholds, position rules, rebalancing frequency, transaction costs, and execution state

**Technology choices**: FastAPI + uvicorn is sufficient for rapid prototyping; any language can call the service through HTTP/gRPC (Python/C++/Go/Rust).

---

## 4. Language Ecosystem Expansion Directions

### 4.1 Rewrite in Rust + PyO3

Preserve the same Python API while implementing the computational core in Rust:
- Zero-copy interoperability using the `numpy` crate, comparable to `py::array_t`
- Use the ownership system to avoid C++ memory management pitfalls
- Use the `rayon` crate instead of OpenMP for parallelism
- Compare the DX (Developer Experience) of pybind11 vs PyO3

### 4.2 Pure-Python Acceleration with Numba/Cython

Provide alternatives for users who do not want to install a C++ compiler:
- **Numba CPU JIT**: Decorate core loops with `@jit(nopython=True)` to accelerate CPU-side computation
- **Numba CUDA**: Requires explicit use of `@cuda.jit` and the CUDA Array API, with redesigned kernels, thread layouts, and memory access—**`@jit` does not automatically provide GPU acceleration**
- **Cython**: Declare C types in `.pyx`; the build process is simpler because it does not require CMake, while performance can approach C++
- Performance comparisons against the C++ version must be benchmarked separately using identical hardware and inputs

### 4.3 Bindings for Other Languages

**Prerequisite—the current C++ core is not a pure C++ library independent of Python.** It directly and extensively depends on pybind11 types such as `py::array_t`, `py::object`, `py::dict`, `py::tuple`, and `py::gil_scoped_release`. Therefore, adding support for another language is not a matter of "just adding a new binding layer."

**Phase 1: Core abstraction** (prerequisite):
- Extract a C++ algorithm library that does not depend on pybind11
- Use `std::span`, raw pointer + length pairs, or a standalone C ABI
- Define error codes, memory ownership, and thread safety rules
- Retain the existing pybind11 layer as the Python adapter

**Phase 2: Language bindings** (after completing Phase 1):
- **R bindings** (Rcpp): R has a large quantitative finance user base, and `Rcpp::NumericVector` conceptually maps to the C ABI
- **Node.js** (node-addon-api): Web-based quantitative platforms commonly use Node backends
- **WASM** (Emscripten): Run in the browser with a Streamlit/Observable frontend
- **Go** (cgo): High-performance microservice scenarios

> Note: The R/Node/WASM/Go paths have independent and substantially different levels of effort and risk. They should not be combined into a single "medium" project estimate.

---

## 5. Feature Engineering Directions

### 5.1 Integrating the Complete F16-F21 Feature Set

**Actual current implementation status** (not the "six market environment features" claimed in the documentation):

| Feature | Function | Location | Status |
|------|------|------|------|
| F16 | Market volatility over the last 20 days | `src/core/market_features.py` `compute_market_volatility()` | ✅ Implemented |
| F17 | Large-cap vs small-cap relative strength | `src/core/market_features.py` `compute_size_relative_strength()` | ✅ Implemented |
| F18 | — | — | ❌ Not implemented |
| F19 | — | — | ❌ Not implemented |
| F20 | Volume anomaly | `src/core/market_features.py` `compute_volume_anomaly()` | ✅ Implemented |
| F21 | Volatility change | `src/core/market_features.py` `compute_vol_change()` | ✅ Implemented |

The sector rotation logic is located in `src/core/technical.py` (`compute_sector_rotation()`), independently of `market_features.py`. "Market breadth" and "capital flow" have no corresponding implementations in the current code.

Therefore, expanding from 15 to 21 dimensions is not a simple concatenation. At minimum, it requires:
1. Defining or restoring F18/F19, including their indicator meanings and data sources
2. Aligning feature IDs across modules
3. Designing external data inputs because some features depend on non-price data
4. Implementing both Python and C++ versions
5. Updating the 21-dimensional output contract and `FEATURE_KEYS`

**Prerequisite**: Determine the definitions, data sources, frequencies, and time-alignment rules for F18/F19.

### 5.2 Adding New Feature Categories

| Category | Example Features | Data Dependencies |
|------|---------|---------|
| Volatility surface | ATM IV, skew, term-structure slope | Options data (requires a data source + license) |
| Macro factors | Yield curve, credit spreads, VIX, U.S. Dollar Index | Multiple macro data sources with different frequencies/time zones/trading calendars |
| Capital flow | ETF net inflows/outflows, large-order capital flow | Capital flow data (commercial data source with licensing restrictions) |
| Correlation | Rolling correlation with a benchmark ETF, such as SPY/510050 | Benchmark ETF price data |
| Liquidity | Amihud illiquidity measure, bid-ask spread | Intraday data with a much higher frequency than daily data |

**Data contract requirements** (must be explicitly defined for every data-related direction):

| Field | Description |
|------|------|
| Data source | Specific service or file format |
| Frequency | Daily/minute/real-time |
| Time zone | UTC/Beijing time/etc. |
| Availability time | After market close/intraday/T+1, to prevent look-ahead bias |
| Missing-data policy | Drop/forward-fill/interpolate |
| License | Whether commercial use and redistribution are permitted |
| Look-ahead prevention | Actual data availability time vs signal generation time |

### 5.3 Feature Interactions and Automatic Selection

- **Interaction terms**: F1×F6 (joint signal of high similarity + high historical subsequent returns), F3×F12 (similarity decay × time span)
- **Boruta / SHAP**: Feature importance analysis and dimensionality reduction
- **RFE** (recursive feature elimination): Identify the smallest effective feature subset
- **Genetic programming**: Automatically generate nonlinear feature combinations

---

## 6. ML Enhancement Directions

### 6.1 Restoring the Original ML Stacking

**Prerequisites (blockers)**:
- The original V3.3 RF/SVM training code, model parameters, and training data **are not included in this repository**
- The original label definitions, feature engineering steps, and cross-validation scheme must be restored from the archived baseline
- The specific implementation of time-series cross-validation (purged k-fold) must be designed separately

The original V3.3 used RF/SVM Stacking → 15-dimensional features → combined signal. Once the prerequisites are satisfied, a fork can:
- Restore two-layer RF+SVM Stacking
- Upgrade to XGBoost + LightGBM + CatBoost Stacking with three-model voting
- Add a deep-learning layer using LSTM/Transformer instead of DTW for sequence matching
- **Critical**: Use time-series cross-validation (purged k-fold) to prevent look-ahead bias
- **Acceptance**: Risk-adjusted return on an out-of-sample test set + comparison with the original V3.3, if original results are available

> Marked as "requires external materials"—the fact that it does not depend entirely on external materials does not mean the prerequisites can be ignored. The actual threshold for starting this direction is much higher than the "high effort" label suggests.

### 6.2 Parameter Adaptation / Online Learning

All current parameters (L_query=20, T_back=750, M_forward=5, k=10, cos_prefilter_top=50) are hardcoded.
- **Walk-forward optimization**: Use Optuna/Hyperopt to perform hyperparameter search over rolling windows
- **Online adaptation**: Use EWMA to update `cos_prefilter_top` (high market volatility → fewer candidates, low volatility → more candidates)
- **Regime switching**: Detect volatility regimes → switch parameter sets (high-volatility parameter set vs low-volatility parameter set)

### 6.3 Reinforcement Learning for Position Management

Use pattern matching as the state encoder and reinforcement learning for position decisions:
- **State**: 15-dimensional features + current position + account state
- **Action**: Rebalancing direction (increase/reduce/liquidate ETF position)
- **Reward**: Risk-adjusted return + transaction cost penalty
- Pattern matching provides feature extraction, while RL provides the decision rules—the interface between the two systems is the 15-dimensional feature vector

---

## 7. Asset Class Expansion

### 7.1 Cryptocurrencies

Cryptocurrency markets have a fundamentally different microstructure from ETFs:
- 24/7 trading with no daily price limits → adjust M_forward and T_back parameters for higher-frequency data
- Perpetual contracts → funding rate can be used as an additional feature (subject to data source licensing)
- Missing-data handling: Exchange outages / discontinuous data sources

### 7.2 Individual A-Shares

Expanding from ETFs to individual stocks requires additional handling:
- Missing data caused by trading suspensions/daily price limits/ST status → improve the robustness of `standardize_returns_cpp`
- Dividends and corporate actions → forward-adjusted price handling
- Industry neutralization → apparent pattern similarity between individual stocks may only reflect industry β, requiring cross-sectional demeaning

### 7.3 Cross-Asset Classes

- **Commodity futures**: Term-structure features + contango/backwardation
- **Foreign exchange**: Interest-rate differentials + central bank policy calendars
- **Convertible bonds**: Conversion premium + straight-bond value

> All of the above directions involve external data sources—refer to the data contract requirements in §5.2.

---

## 8. Infrastructure Directions

### 8.1 Prebuilt Wheel Distribution

**Prerequisites that must be resolved before starting**:
1. **Python version conflict**: `pyproject.toml` declares `requires-python = ">=3.10"`, but the top-level `CMakeLists.txt` uses `find_package(Python 3.12 REQUIRED ...)`—Python 3.10/3.11 cannot build through CMake. These must be aligned: either restrict the project to Python 3.12+, or modify CMake to support the declared version matrix.
2. **Package layout**: `wheel.packages = ["src/cpp"]` does not explicitly include `src/core` (the Python reference implementation); the packaging scope must be defined.
3. **Verification**: Verify `pip install dist/*.whl && python -c "import etf_core"` in a clean virtualenv.

After resolving the prerequisites, a fork can add:
- **cibuildwheel**: Build wheels for Windows/Linux/macOS × x86_64/ARM64 (note: the current CI covers three platforms but tests only Python 3.12, which does not mean the complete matrix has been validated)
- **PyPI release**: Install with a single `pip install etf-core` command
- **conda-forge**: Distribution through the conda ecosystem

**Acceptance criteria**: Successful build + successful installation + successful `import etf_core` + importable `import core` + usable type stubs + at least one passing smoke test.

### 8.2 Real-Time Data Pipeline

Transform the system from "offline batch feature computation" to "automatic daily signal generation":
- WebSocket real-time data (AKShare/Tushare/Binance)—subject to each data source's licensing and redistribution restrictions
- Redis caching for precomputed windows to avoid repeated normalization
- Cron/Airflow scheduled jobs: Automatically generate signals after each market close
- Message delivery: Slack/DingTalk/WeCom

**Data contract**: Refer to the data contract requirements in §5.2—frequency, time zone, availability time, missing-data policy, and look-ahead prevention.

### 8.3 Performance Regression Monitoring

Extend the existing `benchmarks/` framework:
- Automatically compare benchmark JSON files across commits in CI
- One-sided slowdown threshold → automatic alert
- Multi-hardware baselines with reference values for different CPU generations

---

## 9. Academic/Educational Directions

### 9.1 Interactive Visualization Platform

**Prerequisite**: The current `pattern_match_single()` primarily returns a dictionary of 15-dimensional aggregated features—it does not have a stable public interface for returning candidate-window indexes, each candidate's cosine/DTW/combined score/historical subsequent return, or the DTW alignment path. Visualizing the Top-5 matches and DTW paths requires a new optional debug/trace API.

Expand the Jupyter Notebook into a complete experience:
- **Streamlit/Gradio Web App**: Select an ETF → adjust parameters → view historical Top-5 matches → view subsequent performance
- **Plotly visualizations**: Overlay the query window and matched windows + DTW alignment path heatmap
- **Parameter sandbox**: Adjust L_query/T_back/k and other parameters in real time and observe changes in the results

**Prerequisite API requirements** (recommended before visualization work begins):
```python
pattern_match_single(..., return_details=True)
# Returns: query_range, candidate_ranges, cosine_scores,
#        dtw_distances, combined_scores, future_returns, dtw_paths
```
Update `src/cpp/pyi/etf_core.pyi`, the Python reference implementation, the C++ implementation, and tests together.

### 9.2 Systematic Benchmarking of DTW Variants

A purely academic fork:
- Run standard DTW / Soft-DTW / DDTW / Weighted DTW / ShapeDTW / FastDTW on a unified dataset
- Comparison dimensions: **historical matched-window subsequent return statistics** + computation speed + parameter sensitivity
- The existing `benchmarks/run_benchmark.py` + JSON result format naturally supports multi-algorithm comparisons
- Deliverable: A methodological comparison article or technical report

### 9.3 Algorithm Visualization Tutorial

Create an independent visualization for each of the 15 features (F1-F15):
- Compare high-similarity→high-return cases with high-similarity→low-return cases for instructional purposes
- Animated DTW alignment paths
- Analysis of representative "pattern matching failure" cases

---

## 10. Methodological Improvement Directions

### 10.1 Reproducing the Original V3.3 Performance

**⚠️ Blocked by external materials—the following must be obtained before work can begin**:
- [ ] Complete original V3.3.py file, including GmQuant platform bindings and strategy logic
- [ ] Original training data, or an equivalent dataset + data version
- [ ] RF/SVM model hyperparameters and serialized files, if any
- [ ] Original backtesting configuration, including date range, transaction costs, slippage, and trading suspension rules
- [ ] Original backtesting result calculation methodology for comparative validation
- [ ] GmQuant SDK and platform account

The current project explicitly states that it "cannot rerun the original backtesting and does not include the complete platform-bound strategy." This direction cannot begin independently until the above materials are obtained. Once they are available, this becomes a typical academic reproduction study with methodological value for understanding the strategy's actual effectiveness.

### 10.2 Generalizing the Review Methodology

The project's core methodological value lies in its **review process** (multiple rounds of cross-backend review + zero regressions). A fork could apply this SOP to:
- C++ acceleration of other quantitative strategies → general framework: extract pure computation → accelerate with pybind11 → verify cross-backend consistency
- Comparative reviews of different acceleration approaches (C++ vs Rust vs Numba vs pure NumPy)
- Establish an "AI-assisted quantitative strategy code review checklist"

### 10.3 Quantifying Differences from the Original Strategy

Quantitatively analyze differences before and after extraction:
- Distribution of floating-point-level differences between C++ and Python outputs under identical inputs
- Cumulative effects of these differences at the strategy level—do they affect final position decisions?
- A case study on "fidelity in AI-assisted code migration"

---

## 11. Correctness and Cross-Backend Contract Validation

> This direction was proposed during the GPT-5.6-Sol review—the project's distinctive strengths are not limited to C++ acceleration; they also include the Python reference implementation + strict consistency verification + 54 tests + a multi-backend review process. The current direction list emphasizes performance and functionality while overlooking correctness validation as an independent direction.

Generalize the project's validation system into a reusable fork direction:
- **Property-based testing**: Use Hypothesis to generate random inputs, including NaN/Inf/zero-length/constant series/non-contiguous arrays/dtype variations, and verify numerical, exception, and return-structure consistency across Python/C++/alternative backends
- **Fuzz testing**: Random inputs + fixed seeds for differential testing across backends
- **Boundary-input catalog**: Zero-length series, single-element series, constant series, all-NaN inputs, extremely large/small values, and non-contiguous layouts
- **Cross-backend consistency matrix**: Python vs C++ vs Rust vs Numba vs Cython—with unified numerical tolerances (distance 1e-8, score 1e-6), exception semantics, and return-structure contracts
- **Automated regression testing**: Automatically trigger complete consistency verification after every algorithm change

**Related files**: `src/core/dtw.py`, `src/core/pattern_match.py`, `src/cpp/etf_core.cpp`, `src/cpp/pyi/etf_core.pyi`, `verify_etf_core.py`, `verify_batch.py`, `tests/`

---

## Fork Directions Ranked by Implementation Threshold and External Dependencies

> Ranking logic: First group by "ready to start," then sort within each group by effort. "Ready to start" = all entry files and data are available in this repository + no external platform/account is required.

### Ready to Start

| Direction | Effort | Technical Risk | Acceptance Clarity | Standalone Value | Entry Files |
|------|--------|---------|-----------|---------|---------|
| Replace DTW with variants (DDTW/Weighted DTW) | Low | Medium | High | Medium | `src/cpp/etf_core.cpp` `dtw_distance_span()` |
| Candidate retrieval acceleration (pruning/indexing) | Low-Medium | Medium | Medium | Medium | Cosine loop in `pattern_match_core()` |
| Combined score formula redesign | Low-Medium | Medium | Medium | Medium | `etf_core.cpp:680–690` |
| Multithreaded batch parallelization | Medium | High (data races) | High | Medium | Loop in `pattern_match_batch()` |
| Correctness and cross-backend contract validation | Medium | Medium | High | High | `verify_etf_core.py` + `tests/` |

### Requires External Materials or Platforms

| Direction | Effort | External Dependencies | Technical Risk | Standalone Value | Blockers |
|------|--------|---------|---------|---------|--------|
| Streamlit visualization Web App | **Medium¹** | None | Medium | High | Must first implement the debug/trace API (§9.1) |
| Prebuilt Wheel + PyPI release | **Medium¹** | None | Medium | High | Python version conflict + package layout (§8.1) |
| Reintegrate with a backtesting framework | Medium | Backtesting framework | Medium | High | Original data/configuration not in the repository |
| Expand to cryptocurrencies/individual A-shares | Medium | New market data sources + licenses | Medium | Medium | Data contract not yet defined |
| Risk control execution layer (stop-loss/circuit breaker/scheduling) | Medium | None | Medium | Medium | Interface with the calculation layer must be defined first |
| Signal server (computation service layer) | Medium | None | Medium | Medium | API schema must be defined |
| Complete F16-F21 integration | Medium-High | F18/F19 definitions + data sources | Medium | Medium | Missing feature definitions and data |
| Multi-ETF cross-sectional rotation | High | Backtesting framework + transaction cost model | High | High | Requires a multi-ETF batch interface + cross-sectional ranking layer |
| Multilanguage bindings (R/Node/WASM/Go) | **High¹** | None | High | Medium | Must first extract a pybind11-independent C ABI core (§4.3) |
| GPU acceleration (CUDA) | High | CUDA toolchain + hardware | High | High | None; however, 10-20× is an unvalidated assumption |
| Restore ML Stacking | High | Original code/data/models | High | High | Original files are not in the repository |
| SIMD vectorization + SoA | High | None | High | Medium | CPU dispatch + numerical consistency must be designed |
| Reproduce the complete original V3.3 strategy | High | Original files + GmQuant SDK + data | Very High | High | **Blocked by external materials—cannot start independently** |
| Reinforcement learning for position management | High | RL framework + backtesting environment | High | Medium | Requires a working backtesting framework |
| Real-time data pipeline | Medium-High | Data sources + messaging services | Medium | Medium | Data source licensing + availability times must be confirmed |

> ¹ Raised from "low" or "medium-low" after review (Streamlit requires a prerequisite debug API, Wheel distribution has conflicting build configurations, and multilanguage bindings require architectural refactoring).

### Purely Academic/Educational Directions (Standalone Value Is Primarily Academic)

| Direction | Effort | External Dependencies | Deliverable Type |
|------|--------|---------|---------|
| Numba/Cython acceleration comparison | Medium | None | Technical report/blog |
| Systematic benchmarking of DTW variants | Medium | None | Methodological comparison article |
| Rust + PyO3 rewrite comparison | High | None | Engineering comparison report |
| Algorithm visualization tutorial | Medium | Requires debug API | Educational materials |
| Generalize the review methodology | Low (primarily documentation) | None | SOP framework |
| Quantify differences from the original strategy | Medium | Archived original V3.3 | Fidelity study |

---

## Key Constraints and Considerations

### License and External Dependency Boundaries

1. The **MIT License** covers only the code published in this repository. The following are not covered by the MIT License and require separate license review:
   - GmQuant SDK and platform terms of service
   - External data sources such as AKShare / Tushare / Binance, including commercial-use restrictions
   - Redistribution rights for historical market data
   - Files from the original strategy that are not included in this repository
   - Third-party models, such as model files trained with XGBoost/LightGBM, and dependency libraries

2. **No GmQuant SDK**: The original platform bindings are not included in the repository. Any fork that "restores the complete strategy" must independently handle platform adaptation and licensing.

3. **Single-platform benchmarks**: The current benchmark figures (34×/53×/2.2×/93×) come from Windows + MSVC. They must be recalibrated for other platforms and compilers.

### Terminology Conventions

To avoid over-inference from "historical statistical features" to "strategy predictive capability," this document distinguishes the following terms:

| Term | Meaning | Does Not Equal |
|------|------|--------|
| **Subsequent returns of historical matched segments** | Return statistics over the M_forward time points following each historical matched window, which is the essence of the current F6-F11 | Future returns / strategy returns |
| **Historical statistical features** | Descriptive metrics calculated from historical data | Predictive signals |
| **Model predictions** | ML model outputs validated through time-series cross-validation (purged k-fold) and out-of-sample testing | Uncalibrated statistical values |
| **Backtesting realized returns** | Backtesting results under explicitly defined transaction costs, slippage, and execution rules | Live trading returns |
| **Net post-trade returns** | Realized returns after deducting all costs | Simulated backtesting returns |

Expressions such as "production-ready," "strategy improvement," and "validation of original performance" in this document refer only to **possibilities after completing the execution layer, transaction cost modeling, and out-of-sample validation**. They are not performance claims about the code in the current repository.

### Floating-Point and Contract Considerations

4. **15-dimensional feature order**: `etf_core.FEATURE_KEYS` is fixed as a module constant. Any feature modification must update this constant and all references to it.

5. **GIL release boundaries**: When adding new functions, place `py::gil_scoped_release/acquire` correctly. **Worker threads should not directly create Python objects**—see §2.3 and CLAUDE.md.

6. **Floating-point tolerances**: The C++ vs Python consistency verification tolerances are distance 1e-8 and score 1e-6. Revalidate them after changing an algorithm. **Optimizations such as SIMD/GPU that change calculation order may violate these tolerances**—performance acceptance and numerical acceptance must be evaluated separately.

---

## Related Files

### Source Code
- `src/cpp/etf_core.cpp` — All C++ acceleration logic (~1,100 lines with detailed comments)
- `src/cpp/pyi/etf_core.pyi` — C++ type stubs (API contract)
- `src/core/dtw.py` — DTW distance + sequence standardization (Python reference)
- `src/core/pattern_match.py` — Pattern matching engine with 15-dimensional features (Python reference)
- `src/core/technical.py` — ADX / ATR / sector rotation
- `src/core/market_features.py` — F16/F17/F20/F21 market environment features
- `src/core/risk_controls.py` — Rolling volatility quantiles / MA trend / position caps
- `src/core/metrics.py` — Sortino / Calmar / maximum drawdown / IC statistics

### Build and CI
- `pyproject.toml` — Python build configuration (scikit-build-core)
- `CMakeLists.txt` — Project build configuration (top level)
- `src/cpp/CMakeLists.txt` — C++ module build configuration
- `.github/workflows/ci.yml` — Three-platform CI (Windows/Linux/macOS, Python 3.12)
- `.github/workflows/benchmark.yml` — Performance regression CI
- `.github/workflows/sanitizer.yml` — ASAN+UBSAN CI

### Tests and Verification
- `tests/test_dtw.py` — DTW module tests (27 items)
- `tests/test_pattern_match.py` — Pattern matching tests (15 items)
- `tests/test_technical.py` — Technical indicator tests (12 items)
- `tests/test_etf_core.cpp` — Native C++ tests (58 cases)
- `verify_etf_core.py` — C++ vs Python consistency verification
- `verify_batch.py` — Batch pattern matching verification

### Documentation
- `CLAUDE.md` — Practical pybind11 experience, GIL management, and ABI troubleshooting
- `project_status.md` — Review-chain lineage and session history
- `benchmarks/run_benchmark.py` — Reproducible benchmarking
- `benchmarks/results/` — Historical benchmark JSON files
