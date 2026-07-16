# Why 53× Becomes 2.2×: Amdahl’s Law in a pybind11 Workload

> **模型来源 Model provenance**: GPT-5.6-Sol (via Codex CLI), 2026-07-12
> **生成方式 Generation**: single-pass from structured prompt; not independently reviewed

> **Project scope**: This repository is a Python/C++ hybrid engineering practice project. The measurements below describe computational performance, not trading returns or strategy quality.

## 1. Introduction

Three benchmark results summarize both the promise and the limits of this pybind11 refactor. A dynamic time warping (DTW) distance calculation runs **34×** faster in C++ than in its Python equivalent. A complete single pattern match—15-dimensional feature extraction, DTW refinement, and candidate ranking—reaches **53×**. Yet the batch workload, covering 100 timestamps, improves from 50 ms to 23 ms: only **2.2×** end to end.

At first glance, the sequence looks contradictory. If the most representative single operation is 53 times faster, why does the real batch finish only a little more than twice as fast? Put differently, why does the reported speedup collapse by roughly 26-fold when the measurement moves from a single match to a larger workflow?

The answer is not a correctness bug, a failed compiler optimization, or evidence that the 53× result is false. The measurements describe different boundaries. The micro and meso benchmarks isolate code that C++ can accelerate. The macro benchmark includes Python control flow, NumPy-to-C++ boundary work, repeated binding dispatch, and features that remain in Python. Amdahl’s Law predicts exactly this behavior: accelerating one portion of a program cannot eliminate time spent elsewhere. The batch result is therefore the more useful architectural signal.

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

## 4. Amdahl’s Law Analysis

### 4.1 Step 1: state the model

Amdahl’s Law separates a workload into an accelerated fraction and a fraction unaffected by the optimization:

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

<details>
<summary>中文</summary>

# 为什么 53× 最终变成 2.2×：pybind11 工作负载中的 Amdahl 定律

> **项目范围**：本仓库是 Python/C++ 混合编程实践项目。以下测量讨论的是计算性能，不是交易收益或策略质量。

## 1. 引言

三个基准数字同时展示了这次 pybind11 重构的潜力与边界。动态时间规整（DTW）距离的 C++ 实现比 Python 等价实现快 **34×**；一次完整的形态匹配——包括 15 维特征提取、DTW 精排和候选排序——达到 **53×**；但覆盖 100 个时间点的批量工作负载只从 50 ms 降到 23 ms，端到端加速仅为 **2.2×**。

乍看之下，这组结果似乎互相矛盾。如果最具代表性的单次操作已经快了 53 倍，为什么真实批量任务只快了两倍多？换一种说法，当测量范围从单次匹配扩大到完整工作流时，为什么加速比缩小了约 26 倍？

答案不是正确性缺陷、编译器优化失败，也不意味着 53× 是错误数据。不同数字测量的是不同边界。微观和中观基准隔离了 C++ 能够加速的代码；宏观基准还包含 Python 控制流、NumPy 到 C++ 的边界工作、重复绑定分派，以及仍留在 Python 中的特征。Amdahl 定律准确描述了这种现象：加速程序的一部分，无法消除其他部分所花的时间。因此，2.2× 的批量结果反而提供了更有价值的架构信号。

## 2. 实验设置

基准测试在同一台机器上使用相同的合成输入，对比 Python 与 C++ 实现，形态匹配算法逻辑保持不变。处理器、内存系统、操作系统状态和编译器版本都会影响绝对耗时。由于成对结果来自同一硬件，相对加速比更具可比性，但它仍然只适用于当前工作负载，不能被视为普遍适用的 pybind11 常数。

| 项目 | 细节 |
|------|------|
| 硬件 | 消费级笔记本电脑——省略具体型号。在同机 Python 对 C++ 的有限意义上，相对加速比不依赖具体硬件；绝对耗时会随硬件变化。 |
| Python | 3.12.7 + NumPy |
| C++ | C++20、MSVC 19.51（Visual Studio 2026 Community）、pybind11 3.0.4 |
| 编译参数 | <code>/O2 /arch:AVX2</code>，Release 配置 |
| 测试数据 | 20 只 ETF × 1005 个交易日，合成随机游走价格序列（<code>seed=42</code>） |
| 测量方式 | <code>time.perf_counter()</code>，3 轮取最小值，每轮 100 次迭代 |
| 可复现命令 | <code>python verify_etf_core.py</code> + <code>python verify_batch.py</code> |

这里使用合成数据是合理的，因为目标是测量执行成本，而不是模拟真实市场。固定随机种子使工作负载可重复，一致性脚本则检查 C++ 实现是否在项目规定的浮点容差内保持 Python 算法输出。因此，这些数字应被理解为两种实现的工程对比，而不是回测，更不是投资表现证据。

## 3. 三层基准结果

| 函数 | Python | C++ | 加速比 |
|----------|--------|-----|:---:|
| DTW 距离（L=19） | 96 µs | 2.8 µs | **34×** |
| 单次形态匹配 | 14.0 ms | 0.26 ms | **53×** |
| 批量匹配（×100） | 50 ms¹ | 23 ms | **2.2×¹** |

> ¹ 批量行比较的是 100 次 C++ 单次调用 vs 1 次 C++ 批量调用——衡量批量接口开销降低，非 Python vs C++ 加速比。50 ms 基线为 100 × C++ `pattern_match_single`，非 100 × Python。

### 3.1 第一层——微观：单个计算内核

DTW 基准比较长度为 19 的输入上，一个 C++ 函数与其 Python 等价实现。测量边界刻意保持狭窄：主要成本来自嵌套数值循环，外围编排几乎不计入计时区间。数组跨过绑定边界后，C++ 使用编译后的循环和连续数值存储执行动态规划递推，计时范围内几乎不再有 Python 工作。

因此，当解释器级循环被优化后的原生代码替代时，**34×** 是合理结果。它是一项有效测量，但回答的问题很窄：在当前输入维度下，这个内核单次调用能快多少？它不能回答整个应用最终会快多少。

### 3.2 第二层——中观：一次完整形态匹配

单次匹配基准扩大了边界，其中包括 15 维特征生成、候选过滤、DTW 评分和排序。完成初始调用后，各阶段继续在 C++ 内部串联，中间值不会反复返回 Python。原生实现还可以让热点循环、临时向量和排序逻辑保持在同一段编译执行区域中。

结果是 **53×**，甚至高于独立 DTW 的加速比。这是合理的，因为 C++ 路径加速的不只是 DTW：它还消除了多个协同循环中的 Python 开销，并避免在内部阶段之间创建 Python 对象。这里的结论并不是 pybind11 自动让函数快 53 倍，而是：把足够大、计算足够密集的工作单元放在一次绑定调用之后，才能获得这种收益。

### 3.3 第三层——宏观：100 个时间点的批量任务

批量基准测量的是工作流，而不是孤立内核。处理 100 个时间点时，单次原生调用中几乎看不见的成本会显现出来：基线路径中的 Python 循环分派、NumPy 数组准备、参数校验、缓冲区处理、绑定边界切换、结果构造，以及仅在 Python 中执行的特征计算。C++ 批量 API 减少了跨界次数，并复用了高度重叠的候选窗口计算，但它无法清除加速区域之外的全部工作。

因此，耗时从 50 ms 降到 23 ms，得到有用但并不夸张的 **2.2×** 加速。这三个数字不是相互竞争的结论，而是一个层级：34× 描述计算内核，53× 描述原生计算单元，2.2× 描述实际观察到的批量架构。基准边界越宽，其中包含的未加速工作就越多。

## 4. Amdahl 定律分析

### 4.1 第一步：建立模型

Amdahl 定律将工作负载分为可加速部分和不受本次优化影响的部分：

~~~text
S = 1 / ((1 - p) + p/s)

其中：
  S = 观察到的端到端加速比（2.2）
  s = 被加速部分的加速比（58）
  p = 总工作量中可以被加速的比例
~~~

这是一个简化模型。它假设可加速部分按固定倍数缩短，剩余部分保持不变。真实 pybind11 程序还可能增加或减少分配、缓存、转换和调度成本，所以计算结果应被看作架构估计，而不是性能分析器的直接输出。

### 4.2 第二步：求解可加速比例

整理公式可得：

~~~text
已知 S = 2.2，s = 53：
p = (S - 1) × s / ((s - 1) × S)
  = (1.2 × 53) / (52 × 2.2)
  ≈ 0.556
~~~

在该模型下，原始批量工作负载中只有约 **56%** 属于能获得 53× 原生加速的部分；另外 **44%** 相对于本次优化仍是串行的，包括 Python 侧编排、语言边界工作，或尚未迁移到 C++ 的计算。

必须注意，这是相对于基线的解释。若把原始 50 ms 视为 100%，约 28 ms 可加速，22 ms 不可加速。将 28 ms 缩短 53 倍后只剩约 0.53 ms（≈0.5 ms 四舍五入），总耗时预测值约为 22.5 ms，与观察到的 23 ms 非常接近。这正是孤立内核的巨大加速与端到端有限结果能够同时成立的原因。

### 4.3 第三步：分解 44% 的开销

44% 是 Amdahl 等效估计，而不是性能分析器直接测出的明细。对当前批量架构，可以采用如下实用分解：

| 开销来源 | 估算比例 | 机制 |
|-----------------|:------:|-----------|
| Python for 循环分派 | ~15% | Python 编排路径中 100 次迭代的解释器开销 |
| NumPy ↔ C++ 数据转换 | ~15% | <code>py::array</code> ↔ <code>numpy.ndarray</code> 的缓冲区处理，以及所有权、dtype 或布局不满足条件时产生的复制 |
| pybind11 调用开销 | ~8% | 每次跨语言调用的参数解析、校验、包装分派和 GIL 管理 |
| Python 侧特征计算 | ~6% | 尚未迁移到 C++ 的 F16, F17, F20, F21 市场环境特征 |

这些估算合计占基线工作负载的 44%。它们用于识别优化方向，而不是宣称亚毫秒级测量精度。特别需要说明：当 dtype、连续性和生命周期条件满足时，NumPy 缓冲协议可以实现零复制；这里的类别还包括校验、视图创建、强制类型转换、结果分配以及无法避免的复制。

### 4.4 第四步：达到 10× 需要什么？

假设 C++ 内核变得无限快。令 <code>s → ∞</code>，可加速项消失，但串行比例仍然存在：

~~~text
S_max = 1 / (1 - p)
      = 1 / (1 - 0.555…)
      ≈ 2.25×
~~~

观察到的 **2.2×** 已经非常接近当前架构隐含的约 **2.25×** 上限（若用舍入后的 p=0.56→0.44 拆分，会得到 2.3×，但精确 p≈0.555… 给出的是 2.25×；差异很小，不影响结论）。继续调整 DTW 或排序逻辑或许还能缩短剩余约 0.48 ms 的可加速部分，但只要基线中仍有 44% 位于该区域之外，就不可能得到 10× 的端到端性能。

若要达到 10×，即使假设内核无限快，串行比例也必须低于 10%。在内核加速比有限、即 53× 的情况下，将 <code>S = 10</code> 代入公式可得 <code>p ≈ 0.917</code>：约 92% 的工作负载必须能够被加速。这意味着需要把更多工作流——而不仅仅是更快的算术——放到 C++ 边界之后，包括时间点循环、可合理迁移的数据准备、F16, F17, F20, F21 计算、中间聚合和最终结果打包。因此，接下来的优化核心是边界设计。

## 5. 工程启示

### 5.1 pybind11 适合计算密集、调用稀疏的工作负载

一次跨语言调用存在固定成本。社区基准测试和 pybind11 文档表明，每次调用约 0.5–2 µs，具体取决于函数签名复杂度、参数转换、平台和构建配置（这是一般数量级估计，非本项目实测值）。对于一个原本耗时 15 ms、迁移后仍形成较大原生任务的操作，这点成本可以忽略；对于本身只需 2.9 µs 的 DTW 调用，它就明显得多。如果从 Python 调用这种微小函数数千次，即使 C++ 函数体非常优秀，进入和离开 C++ 也会占据可观时间。解决方法是暴露粒度更粗的操作。

### 5.2 批量接口是杠杆最高的优化

将接口从 Python 编排的 100 次独立调用改为 1 次批量调用，产生了测得的 **2.2×** 提升。批量函数只需校验一次共享输入、跨越一次语言边界、复用重叠候选窗口，并集中构造输出。这类架构收益往往比从已经优化的内部循环中再挤出几个百分点更有价值。优秀的 pybind11 API 应减少跨界频率，而不只是降低单次跨界成本。

这也指出了下一步方向：继续扩大批量边界。如果 Python 仍在计算 F16, F17, F20, F21、准备重复视图，或逐项处理结果，就应评估是否能把这些阶段合并进单次端到端原生流水线，同时保证 API 仍然可测试、可维护。

### 5.3 加速比必须附带上下文

**53×** 是准确的微观/中观基准，也是很醒目的 README 摘要；**2.2×** 则更能代表测得的批量工作负载。两者都是真的，因为它们回答不同问题。只报告较大的数字会隐藏系统级瓶颈；只报告较小的数字又会掩盖所提取原生核心的实际效果。

因此，性能报告应明确基准边界、输入规模、调用次数、测量方法和仍留在 Python 中的工作。一份有用的报告会同时给出内核与端到端结果，并解释二者之间的差距。在本项目中，这个差距不是需要回避的问题，而是最重要的工程发现。

## 6. 可视化说明

建议使用水平堆叠条形图比较两行。上方 **<code>Python batch (50 ms)</code>** 使用一条完整实色柱；下方 **<code>C++ batch (23 ms)</code>** 分成 **<code>C++ compute (11.5 ms)</code>** 与 **<code>Python overhead (11.5 ms)</code>**。在开销区段标注第 4 节的四类来源：循环分派、NumPy/C++ 数据传输、pybind11 调用和 Python 侧 F16, F17, F20, F21 特征。这个用于展示的 50/50 切分描述优化后柱形，不应与基线归一化的 56%/44% Amdahl 估计混为一谈。

[图表将另行使用 matplotlib 生成——数据见第 4 节]

</details>

*Generated by GPT-5.6-Sol (via Codex CLI) · 2026-07-12*
