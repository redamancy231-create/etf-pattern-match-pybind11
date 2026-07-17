# Why 53× Becomes 2.2×: Amdahl's Law in a pybind11 Workload

> **模型来源 Model provenance**: GPT-5.6-Sol (via Codex CLI), 2026-07-12
> **生成方式 Generation**: single-pass from structured prompt; not independently reviewed
> [中文版](performance-analysis.zh-CN.md)

> **Project scope**: This repository is a Python/C++ hybrid engineering practice project. The measurements below describe computational performance, not trading returns or strategy quality.

## 1. Introduction

Three benchmark results summarize both the promise and the limits of this pybind11 refactor. A dynamic time warping (DTW) distance calculation runs **34×** faster in C++ than in its Python equivalent. A complete single pattern match—15-dimensional feature extraction, DTW refinement, and candidate ranking—reaches **53×**. Yet the batch workload, covering 100 timestamps, improves from 50 ms to 23 ms: only **2.2×** end to end.

At first glance, the sequence looks contradictory. If the most representative single operation is 53 times faster, why does the real batch finish only a little more than twice as fast? Put differently, why does the reported speedup collapse by roughly 26-fold when the measurement moves from a single match to a larger workflow?

The answer is not a correctness bug, a failed compiler optimization, or evidence that the 53× result is false. The measurements describe different boundaries. The micro and meso benchmarks isolate code that C++ can accelerate. The macro benchmark includes Python control flow, NumPy-to-C++ boundary work, repeated binding dispatch, and features that remain in Python. Amdahl's Law predicts exactly this behavior: accelerating one portion of a program cannot eliminate time spent elsewhere. The batch result is therefore the more useful architectural signal.

## 2. Experimental Setup

The benchmark was designed to compare Python and C++ on the same machine, with identical synthetic inputs and unchanged pattern-matching logic. Absolute timings will differ across processors, memory systems, operating-system states, and compiler versions. Relative speedups are more portable because each pair is measured on the same hardware, although they should still be treated as workload-specific rather than universal pybind11 constants.

| Item | Detail |
|------|--------|
| Hardware | Consumer laptop — specific model omitted. Relative speedup ratios are hardware-independent in the limited same-machine Python-vs-C++ sense; absolute timings will vary across hardware. |
| Python | 3.12.7 + NumPy |
| C++ | C++20, MSVC 19.51 (Visual Studio 2026 Community), pybind11 3.0.4 |
| Compiler flags | <code>/O2 /arch:AVX2</code>, Release configuration |
| Test data | 20 ETFs × 1005 trading days, synthetic random-walk price series (<code>seed=42</code>) |
| Measurement | <code>time.perf_counter()</code>, minimum of 3 runs, 100 iterations per run |
| Reproducibility | <code>python verify_etf_core.py</code> + <code>python verify_batch.py</code> |

Synthetic data is appropriate here because the target is execution cost, not market realism. A fixed seed makes the workload repeatable, and the consistency scripts check that the C++ implementation preserves the Python algorithm outputs within the project floating-point tolerances. The benchmark should therefore be read as an engineering comparison of two implementations, not as a backtest and not as evidence about investment performance.

## 3. Three-Tier Benchmark Results

| Function | Python | C++ | Speedup |
|----------|--------|-----|:---:|
| DTW Distance (L=19) | 96 µs | 2.8 µs | **34×** |
| Single Pattern Match | 14.0 ms | 0.26 ms | **53×** |
| Batch Match (×100) | 50 ms¹ | 23 ms | **2.2×¹** |

> ¹ Batch row compares 100 C++ single calls vs 1 C++ batch call — a measure of batch-interface overhead reduction, not Python-vs-C++ speedup. The 50 ms baseline is 100 × C++ `pattern_match_single`, not 100 × Python.

### 3.1 Layer 1 — Micro: one computational kernel

The DTW benchmark compares one C++ function with its Python equivalent over length-19 inputs. This boundary is intentionally narrow: the operation is dominated by nested numeric loops, and little surrounding orchestration is included. Once the arrays have crossed the binding boundary, C++ performs the dynamic-programming recurrence using compiled loops and contiguous numeric storage. There is almost no Python work left in the timed region.

That is why the **34×** result approaches the kind of speedup expected when interpreter-level iteration is replaced with optimized native code. It is a valid measurement, but it answers a narrow question: how much faster is this kernel when called once under these input dimensions? It does not answer how much faster the complete application becomes.

### 3.2 Layer 2 — Meso: one complete pattern match

The single-match benchmark widens the boundary. It includes 15-dimensional feature production, candidate filtering, DTW scoring, and ranking. After the initial call, these stages remain chained inside C++, so intermediate values do not repeatedly return to Python. The native implementation also benefits from keeping hot loops, temporary vectors, and ranking logic in one compiled execution region.

The result is **53×**, even higher than the standalone DTW ratio. This is plausible because the C++ path accelerates more than DTW alone: it removes Python overhead from several coordinated loops and avoids materializing Python objects between internal stages. The lesson is not that pybind11 itself makes a function 53 times faster. The gain comes from moving a sufficiently large, compute-heavy unit of work behind one binding call.

### 3.3 Layer 3 — Macro: 100-timestamp batch

The batch benchmark measures a workflow rather than an isolated kernel. It processes 100 timestamps and therefore exposes costs that are almost invisible in a single native call: Python loop dispatch in the baseline path, NumPy array preparation, argument validation, buffer handling, binding transitions, result construction, and Python-only feature work. The C++ batch API reduces the number of crossings and reuses overlapping candidate-window computations, but it does not erase all work outside the accelerated region.

Consequently, the measured time falls from 50 ms to 23 ms, a useful but modest **2.2×** improvement. The three results are not competing claims. They form a hierarchy: 34× describes a kernel, 53× describes a native computational unit, and 2.2× describes the observed batch architecture. The wider the benchmark boundary becomes, the more non-accelerated work it contains.

## 4. Amdahl's Law Analysis

### 4.1 Step 1: state the model

Amdahl's Law separates a workload into an accelerated fraction and a fraction unaffected by the optimization:

~~~text
S = 1 / ((1 - p) + p/s)

Where:
  S = observed end-to-end speedup (2.2)
  s = speedup of the accelerated portion (53)
  p = fraction of total work that CAN be accelerated
~~~

This is a simplified model. It assumes the accelerated portion scales by a constant factor and that the remaining portion is unchanged. Real pybind11 programs can add or remove allocation, caching, conversion, and scheduling costs, so the result should be interpreted as an architectural estimate rather than a profiler trace.

### 4.2 Step 2: solve for the accelerable fraction

Rearranging the equation gives:

~~~text
Given S = 2.2, s = 53:
p = (S - 1) × s / ((s - 1) × S)
  = (1.2 × 53) / (52 × 2.2)
  ≈ 0.556
~~~

Under this model, only about **56% of the original batch workload** belongs to the portion that can benefit from the 53× native acceleration. The other **44%** is effectively serial with respect to this optimization: it is Python-side orchestration, language-boundary work, or computation not yet moved to C++.

The baseline-normalized interpretation matters. If the original 50 ms is treated as 100%, roughly 28 ms is accelerable and 22 ms is not. Accelerating the 28 ms portion by 53× reduces it to ~0.53 ms (≈0.5 ms rounded), leaving a predicted total near 22.5 ms—very close to the observed 23 ms. This is why a spectacular isolated speedup can coexist with a modest end-to-end result.

### 4.3 Step 3: decompose the 44% overhead

The 44% is an Amdahl-equivalent estimate, not a directly measured profiler breakdown. A practical decomposition for this batch architecture is:

| Overhead Source | Est. % | Mechanism |
|-----------------|:------:|-----------|
| Python for-loop dispatch | ~15% | Interpreter overhead for 100 iterations in the Python-orchestrated path |
| NumPy ↔ C++ data conversion | ~15% | <code>py::array</code> ↔ <code>numpy.ndarray</code> buffer handling and copies where ownership, dtype, or layout requires them |
| pybind11 call overhead | ~8% | Argument parsing, validation, wrapper dispatch, and GIL management at each cross-language call |
| Python-side feature computation | ~6% | F16, F17, F20, F21 market-environment features not ported to C++ |

These estimates sum to 44% of the baseline workload. Their purpose is to identify optimization targets, not to claim sub-millisecond measurement precision. In particular, the NumPy buffer protocol can permit zero-copy access when dtype, contiguity, and lifetime requirements align; the relevant category also includes validation, view creation, forced casts, result allocation, and any unavoidable copying.

### 4.4 Step 4: what would it take to reach 10×?

Suppose the C++ kernel became infinitely fast. Setting <code>s → ∞</code> removes the accelerated term but leaves the serial fraction:

~~~text
S_max = 1 / (1 - p)
      = 1 / (1 - 0.555…)
      ≈ 2.25×
~~~

The observed **2.2×** is already close to the approximately **2.25×** ceiling implied by the current architecture. (Using the rounded p=0.56→0.44 split would give 2.3×, but the exact p≈0.555… yields 2.25×; the difference is small and does not change the conclusion.) Further tuning of DTW or ranking may improve the ~0.48 ms accelerated remainder, but it cannot produce 10× end-to-end performance while 44% of baseline work remains outside that region.

To reach 10×, the serial fraction must be below 10% even with an infinitely fast kernel. With a finite 53× kernel speedup, solving the law for <code>S = 10</code> requires <code>p ≈ 0.916</code>: about 92% of the workload must be accelerable. That means moving more of the workflow—not merely faster arithmetic—behind the C++ boundary: the timestamp loop, data preparation where practical, F16, F17, F20, F21 computation, intermediate aggregation, and final result packing. The optimization problem is therefore one of boundary design.

## 5. Engineering Lessons

### 5.1 pybind11 excels at compute-heavy, call-sparse workloads

A cross-language call has a fixed cost. Community benchmarks and pybind11 documentation suggest roughly 0.5–2 µs per call depending on signature complexity, argument conversions, platform, and build configuration (this is a general order-of-magnitude estimate, not a project-specific measurement). That cost is negligible around a 15 ms Python operation that becomes a substantial native task. It is much more visible around a 2.9 µs DTW call. Calling such a tiny function thousands of times from Python can spend a meaningful share of wall time entering and leaving C++, even when the C++ body is excellent. The antidote is to expose operations at a coarser granularity.

### 5.2 Batch interfaces are the highest-leverage optimization

Changing the interface from 100 individually orchestrated calls to one batch call produced the measured **2.2×** improvement. The batch function can validate shared inputs once, cross the language boundary once, reuse overlapping candidate windows, and construct outputs collectively. Those architectural savings are often more valuable than shaving another percentage point from an already optimized inner loop. A good pybind11 API minimizes crossing frequency, not merely crossing cost.

This also suggests the next iteration: make the batch boundary wider. If Python still computes F16, F17, F20, F21, prepares repeated views, or post-processes every result, those stages should be evaluated as candidates for a single end-to-end native pipeline—provided the resulting API remains testable and maintainable.

### 5.3 Speedup numbers need context

The **53×** figure is an accurate micro/meso benchmark and an attractive README summary. The **2.2×** figure better represents the measured batch workload. Both are true because they answer different questions. Reporting only the larger number would hide the system-level bottleneck; reporting only the smaller number would hide the effectiveness of the extracted native core.

Performance reports should therefore state the benchmark boundary, input size, call count, measurement method, and remaining Python work. A useful report pairs kernel results with end-to-end results and explains the gap. In this project, that gap is not an embarrassment. It is the central engineering finding.

## 6. Visualization Specification

A stacked horizontal bar chart should compare two rows. The top row, **<code>Python batch (50 ms)</code>**, is one solid bar. The bottom row, **<code>C++ batch (23 ms)</code>**, is split into **<code>C++ compute (11.5 ms)</code>** and **<code>Python overhead (11.5 ms)</code>**. Annotate the overhead segment with the four categories from Section 4: loop dispatch, NumPy/C++ transfer, pybind11 calls, and Python-side F16, F17, F20, F21 features. This presentation-oriented 50/50 split describes the observed optimized bar; it should not be mistaken for the baseline-normalized 56%/44% Amdahl estimate.

[Chart to be generated separately with matplotlib — see §4 for data]

*Generated by GPT-5.6-Sol (via Codex CLI) · 2026-07-12*
