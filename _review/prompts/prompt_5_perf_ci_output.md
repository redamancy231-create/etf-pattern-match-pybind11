Reading prompt from stdin...
OpenAI Codex v0.144.1
--------
workdir: C:\Users\33455
model: gpt-5.6-sol
provider: packycode
approval: never
sandbox: danger-full-access
reasoning effort: xhigh
reasoning summaries: none
session id: 019f6ff2-c2f2-7e52-8acc-4b78240e06a8
--------
user
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

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
2026-07-17T12:00:19.874960Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- benchmarks/run_benchmark.py ---'; Get-Content -LiteralPath 'benchmarks/run_benchmark.py' -Raw -Encoding UTF8; Write-Host '--- .github/workflows/ci.yml ---'; Get-Content -LiteralPath '.github/workflows/ci.yml' -Raw -Encoding UTF8; Write-Host '--- benchmark results files ---'; Get-ChildItem -LiteralPath 'benchmarks/results' -File | Select-Object Name,Length,LastWriteTime; foreach ("'$f in Get-ChildItem -LiteralPath '"'benchmarks/results' -File) { Write-Host (\"--- \" + "'$f.FullName + " ---"); Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8 }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 214ms:
--- benchmarks/run_benchmark.py ---
"""可复现的性能基准测试

用法:
    python benchmarks/run_benchmark.py                    # 全部基准
    python benchmarks/run_benchmark.py --function dtw     # 仅 DTW
    python benchmarks/run_benchmark.py --repeat 50        # 自定义重复次数

脚本只依赖 NumPy、已安装的 etf_core，以及 Python 标准库；不导入项目内的
src/core 模块，因此可以复制到另一个目录运行。输入数组在计时前预先构造为
连续的 float64/int64 NumPy 数组，计时包含函数调用边界和返回对象构造，但不
包含随机数据生成或输入数组转换。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

# Windows ??????????? ? / ??????????????
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np

try:
    import etf_core
except ImportError as exc:  # pragma: no cover - exercised when the extension is absent
    raise SystemExit(
        "无法导入 etf_core。请先安装/编译 pybind11 扩展，然后重新运行此脚本。"
    ) from exc


DEFAULT_WARMUP_RUNS = 5
DEFAULT_TIMED_RUNS = 100
RANDOM_SEED = 42
FEATURE_KEYS = tuple(str(key) for key in etf_core.FEATURE_KEYS)


# ---------------------------------------------------------------------------
# Pure NumPy/Python baseline implementations
# ---------------------------------------------------------------------------


def py_standardize_returns(price_series: np.ndarray) -> np.ndarray:
    """与 etf_core 使用相同逻辑的标准化收益率实现。"""
    if len(price_series) < 2:
        return np.array([], dtype=np.float64)
    if not np.all(np.isfinite(price_series)):
        return np.array([], dtype=np.float64)

    rets = np.diff(np.log(np.maximum(price_series, 1e-12)))
    std_ = np.std(rets)
    if std_ < 1e-12:
        return rets - np.mean(rets)
    return (rets - np.mean(rets)) / std_


def py_cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """NumPy baseline for cosine_similarity."""
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x < 1e-12 or norm_y < 1e-12:
        return 0.0
    return float(np.dot(x, y) / (norm_x * norm_y))


def py_dtw_distance(x: np.ndarray, y: np.ndarray, window: int = 5) -> float:
    """与 C++ dtw_distance 相同的 Sakoe-Chiba band DTW。"""
    n, m = len(x), len(y)
    band = max(window, abs(n - m))

    dtw = np.full((n + 1, m + 1), np.inf, dtype=np.float64)
    dtw[0, 0] = 0.0

    for i in range(1, n + 1):
        j_start = max(1, i - band)
        j_end = min(m + 1, i + band + 1)
        for j in range(j_start, j_end):
            cost = (float(x[i - 1]) - float(y[j - 1])) ** 2
            dtw[i, j] = cost + min(
                dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1]
            )

    path_len = n + m
    return np.sqrt(dtw[n, m]) / path_len if path_len > 0 else np.inf


def py_pattern_match_single(
    prices: np.ndarray,
    T_idx: int,
    k: int = 10,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
    M_forward: int = 5,
    dtw_window: int = 5,
    cos_prefilter_top: int = 50,
) -> Optional[Dict[str, float]]:
    """纯 Python/NumPy 形态匹配 baseline。

    逻辑与项目中的 Python 参考实现以及 C++ 共享核心一致：全量余弦预筛选，
    对 top-N 候选做 DTW，再进行 15 维特征提取。这里重复实现逻辑是为了让
    benchmark 脱离项目其它文件也能运行。
    """
    if M_forward < 1:
        raise ValueError(f"M_forward must be >= 1, got {M_forward}")
    if L_query < 3:
        raise ValueError(f"L_query must be >= 3, got {L_query}")
    if match_step <= 0:
        raise ValueError(f"match_step must be > 0, got {match_step}")
    if T_idx < L_query + M_forward + 10:
        return None

    query_prices = prices[T_idx - L_query + 1 : T_idx + 1]
    if len(query_prices) < L_query:
        return None

    query_rets = py_standardize_returns(query_prices)
    if len(query_rets) < 2:
        return None

    search_end = T_idx - L_query
    if search_end < L_query:
        return None
    search_start = max(L_query - 1, T_idx - T_back)

    cos_candidates: List[Tuple[int, int, float, np.ndarray]] = []
    fast_shape_dists: List[float] = []

    for hist_end in range(search_start, search_end + 1, match_step):
        hist_start = hist_end - L_query + 1
        if hist_start < 0:
            continue

        hist_prices = prices[hist_start : hist_end + 1]
        if len(hist_prices) < L_query:
            continue

        hist_rets = py_standardize_returns(hist_prices)
        if len(hist_rets) < 2:
            continue

        cos_s = py_cosine_similarity(hist_rets, query_rets)
        fast_d = np.sqrt(np.mean((hist_rets - query_rets) ** 2))
        fast_shape_dists.append(float(fast_d))

        if cos_s > 0:
            # 保留标准化收益率，避免第二遍重复计算。
            cos_candidates.append((hist_end, hist_start, cos_s, hist_rets))

    if len(cos_candidates) < 3:
        return None

    sigma_fast = (
        np.std(fast_shape_dists) / (2.0 * np.sqrt(L_query - 1))
        if len(fast_shape_dists) > 1
        else 1.0
    )
    sigma_fast = max(float(sigma_fast), 1e-12)

    cos_candidates.sort(key=lambda item: item[2], reverse=True)
    all_cos_values = np.array([candidate[2] for candidate in cos_candidates])
    global_min_cos = float(np.min(all_cos_values)) if len(all_cos_values) > 0 else 0.0
    global_max_cos = float(np.max(all_cos_values)) if len(all_cos_values) > 0 else 1.0

    n_cos = min(cos_prefilter_top, len(cos_candidates))
    top_cos = cos_candidates[:n_cos]

    dtw_dists: List[float] = []
    cos_sims: List[float] = []
    future_rets: List[float] = []
    match_end_indices: List[int] = []

    for hist_end, hist_start, sim_cos, hist_rets in top_cos:
        del hist_start  # 只用于保持与原始算法相同的候选记录结构。
        dtw_d = py_dtw_distance(hist_rets, query_rets, window=dtw_window)
        dtw_dists.append(dtw_d)
        cos_sims.append(sim_cos)

        fut_end = hist_end + M_forward
        if fut_end < len(prices) and fut_end < T_idx:
            fut_ret = float(prices[fut_end] / prices[hist_end] - 1)
        else:
            fut_ret = float("nan")
        future_rets.append(fut_ret)
        match_end_indices.append(hist_end)

    if len(dtw_dists) < 3:
        return None

    dtw_dists_arr = np.array(dtw_dists, dtype=np.float64)
    cos_sims_arr = np.array(cos_sims, dtype=np.float64)
    future_rets_arr = np.array(future_rets, dtype=np.float64)
    match_end_arr = np.array(match_end_indices, dtype=np.int64)

    sigma = sigma_fast if sigma_fast > 1e-12 else 1.0
    sim_dtw = np.exp(-dtw_dists_arr / sigma)

    if len(sim_dtw) < 3:
        return None

    min_dtw_val, max_dtw_val = np.min(sim_dtw), np.max(sim_dtw)
    range_dtw = max_dtw_val - min_dtw_val
    range_cos = global_max_cos - global_min_cos
    range_dtw = range_dtw if range_dtw > 1e-12 else 1.0
    range_cos = range_cos if range_cos > 1e-12 else 1.0

    norm_dtw = (sim_dtw - min_dtw_val) / range_dtw
    norm_cos = (cos_sims_arr - global_min_cos) / range_cos
    combined_scores = 0.5 * norm_dtw + 0.5 * norm_cos

    sorted_idx = np.argsort(combined_scores)[::-1]
    top_k = min(k, len(sorted_idx))
    top_idx = sorted_idx[:top_k]

    top_scores = combined_scores[top_idx]
    top_future_rets = future_rets_arr[top_idx]
    top_end_indices = match_end_arr[top_idx]

    nan_mask = ~np.isnan(top_future_rets)
    if np.sum(nan_mask) < 2:
        return None
    top_scores = top_scores[nan_mask]
    top_future_rets = top_future_rets[nan_mask]
    top_end_indices = top_end_indices[nan_mask]
    top_k_actual = len(top_scores)
    if top_k_actual < 2:
        return None

    top1_sim = float(top_scores[0])
    n_for_avg = min(5, top_k_actual)
    top5_avg_sim = float(np.mean(top_scores[:n_for_avg]))
    sim_decay = top1_sim - top5_avg_sim
    sim_variance = float(np.var(top_scores)) if top_k_actual > 1 else 0.0
    match_distance_ratio = sim_decay / top1_sim if top1_sim > 1e-12 else 0.0

    avg_future_ret = float(np.mean(top_future_rets))
    weighted_ret = (
        float(np.average(top_future_rets, weights=top_scores))
        if np.sum(top_scores) > 1e-12
        else avg_future_ret
    )
    median_future_ret = float(np.median(top_future_rets))
    ret_sign_consistency = float(np.sum(top_future_rets > 0) / top_k_actual)
    best_match_ret = float(top_future_rets[0])
    min_ret = float(np.min(top_future_rets))
    max_dd_in_matches = float(max(0.0, -min_ret))

    match_time_span = (
        float(np.max(top_end_indices) - np.min(top_end_indices))
        if top_k_actual > 1
        else 0.0
    )
    match_time_span_ratio = match_time_span / T_back

    top_end_sorted = np.sort(top_end_indices)
    max_in_window = 0
    for i in range(len(top_end_sorted)):
        j = np.searchsorted(top_end_sorted, top_end_sorted[i] + 60, side="right")
        max_in_window = max(max_in_window, int(j - i))
    match_cluster_ratio = max_in_window / top_k_actual if top_k_actual > 0 else 0.0
    n_matches_above_thresh = int(np.sum(top_scores > 0.8))

    return {
        "top1_sim": top1_sim,
        "top5_avg_sim": top5_avg_sim,
        "sim_decay": sim_decay,
        "sim_variance": sim_variance,
        "match_distance_ratio": match_distance_ratio,
        "avg_future_ret": avg_future_ret,
        "weighted_future_ret": weighted_ret,
        "median_future_ret": median_future_ret,
        "ret_sign_consistency": ret_sign_consistency,
        "best_match_ret": best_match_ret,
        "max_dd_in_matches": max_dd_in_matches,
        "match_time_span": match_time_span,
        "match_time_span_ratio": match_time_span_ratio,
        "match_cluster_ratio": match_cluster_ratio,
        "n_matches_above_thresh": float(n_matches_above_thresh),
    }


def py_pattern_match_batch(
    prices: np.ndarray,
    t_indices: np.ndarray,
    **kwargs: Any,
) -> List[Optional[Dict[str, float]]]:
    """batch baseline：严格按要求循环调用 pure-Python single。"""
    return [
        py_pattern_match_single(prices, int(t_idx), **kwargs) for t_idx in t_indices
    ]


# ---------------------------------------------------------------------------
# Benchmark fixtures and measurement
# ---------------------------------------------------------------------------


def make_fixtures() -> Dict[str, Any]:
    """创建一次、之后在所有 warm-up/timed runs 中复用的确定性输入。"""
    rng = np.random.default_rng(RANDOM_SEED)

    dtw_x = np.ascontiguousarray(rng.normal(size=19), dtype=np.float64)
    dtw_y = np.ascontiguousarray(rng.normal(size=19), dtype=np.float64)

    cosine_x = np.ascontiguousarray(rng.normal(size=19), dtype=np.float64)
    cosine_y = np.ascontiguousarray(rng.normal(size=19), dtype=np.float64)

    pattern_prices = np.ascontiguousarray(
        100.0 * np.exp(np.cumsum(rng.normal(0.0005, 0.01, size=1000))),
        dtype=np.float64,
    )

    # etf_core.pattern_match_batch 的 C++ API 接收一条 1-D 价格序列和一组
    # T_idx；这里使用 1000 点、100 个连续时间点，和 single 使用同一算法参数。
    # task 中的“1000×50”无法直接作为该 1-D API 的输入；50 在默认参数中
    # 对应 cos_prefilter_top=50。若要测 50 条 ETF，应在调用层按列分别运行。
    batch_t_indices = np.arange(400, 500, dtype=np.int64)

    return {
        "dtw_x": dtw_x,
        "dtw_y": dtw_y,
        "cosine_x": cosine_x,
        "cosine_y": cosine_y,
        "pattern_prices": pattern_prices,
        "pattern_t_idx": 500,
        "batch_prices": pattern_prices,
        "batch_t_indices": batch_t_indices,
    }


def _measure(fn: Callable[[], Any], warmup_runs: int, timed_runs: int) -> Dict[str, Any]:
    """warm-up 后使用 perf_counter 逐次采样，单位为微秒。"""
    for _ in range(warmup_runs):
        fn()

    samples_us: List[float] = []
    for _ in range(timed_runs):
        start = time.perf_counter()
        fn()
        samples_us.append((time.perf_counter() - start) * 1_000_000.0)

    values = np.asarray(samples_us, dtype=np.float64)
    return {
        "samples_us": samples_us,
        "median_us": float(np.median(values)),
        "mean_us": float(np.mean(values)),
        "std_us": float(np.std(values, ddof=1)) if len(values) > 1 else 0.0,
        "ci_95": [
            float(np.percentile(values, 2.5)),
            float(np.percentile(values, 97.5)),
        ],
    }


def _assert_close_scalar(name: str, py_value: float, cpp_value: float) -> None:
    if not np.isclose(py_value, cpp_value, rtol=1e-8, atol=1e-10, equal_nan=True):
        raise RuntimeError(
            f"{name} baseline mismatch: Python={py_value!r}, C++={cpp_value!r}"
        )


def _validate_single_pattern(fixtures: Dict[str, Any]) -> None:
    prices = fixtures["pattern_prices"]
    t_idx = fixtures["pattern_t_idx"]
    py_result = py_pattern_match_single(prices, t_idx)
    cpp_result = etf_core.pattern_match_single(prices, t_idx)
    if (py_result is None) != (cpp_result is None):
        raise RuntimeError("pattern_match_single baseline/C++ validity mismatch")
    if py_result is None or cpp_result is None:
        raise RuntimeError("pattern_match_single fixture unexpectedly has no result")
    for key in FEATURE_KEYS:
        _assert_close_scalar(key, float(py_result[key]), float(cpp_result[key]))


def _validate_batch_pattern(fixtures: Dict[str, Any]) -> None:
    prices = fixtures["batch_prices"]
    t_indices = fixtures["batch_t_indices"]
    py_results = py_pattern_match_batch(prices, t_indices)
    cpp_features, cpp_mask = etf_core.pattern_match_batch(prices, t_indices)
    cpp_features = np.asarray(cpp_features)
    cpp_mask = np.asarray(cpp_mask, dtype=bool)

    if cpp_features.shape[0] != int(cpp_mask.sum()) or cpp_features.shape[1] != 15:
        raise RuntimeError(
            "pattern_match_batch returned an unexpected shape: "
            f"features={cpp_features.shape}, mask={cpp_mask.shape}"
        )

    row = 0
    for index, valid in enumerate(cpp_mask):
        if not valid:
            if py_results[index] is not None:
                raise RuntimeError("pattern_match_batch validity mismatch")
            continue
        if py_results[index] is None:
            raise RuntimeError("pattern_match_batch validity mismatch")
        for column, key in enumerate(FEATURE_KEYS):
            _assert_close_scalar(key, float(py_results[index][key]), float(cpp_features[row, column]))
        row += 1


def benchmark_dtw(fixtures: Dict[str, Any]) -> Tuple[Callable[[], Any], Callable[[], Any]]:
    x, y = fixtures["dtw_x"], fixtures["dtw_y"]
    return (
        lambda: py_dtw_distance(x, y, window=5),
        lambda: etf_core.dtw_distance(x, y, 5),
    )


def benchmark_cosine(fixtures: Dict[str, Any]) -> Tuple[Callable[[], Any], Callable[[], Any]]:
    x, y = fixtures["cosine_x"], fixtures["cosine_y"]
    return (
        lambda: py_cosine_similarity(x, y),
        lambda: etf_core.cosine_similarity(x, y),
    )


def benchmark_pattern_single(
    fixtures: Dict[str, Any],
) -> Tuple[Callable[[], Any], Callable[[], Any]]:
    prices, t_idx = fixtures["pattern_prices"], fixtures["pattern_t_idx"]
    return (
        lambda: py_pattern_match_single(prices, t_idx),
        lambda: etf_core.pattern_match_single(prices, t_idx),
    )


def benchmark_pattern_batch(
    fixtures: Dict[str, Any],
) -> Tuple[Callable[[], Any], Callable[[], Any]]:
    prices, t_indices = fixtures["batch_prices"], fixtures["batch_t_indices"]
    return (
        lambda: py_pattern_match_batch(prices, t_indices),
        lambda: etf_core.pattern_match_batch(prices, t_indices),
    )


BENCHMARKS: Dict[str, Callable[[Dict[str, Any]], Tuple[Callable[[], Any], Callable[[], Any]]]] = {
    "dtw_distance": benchmark_dtw,
    "cosine_similarity": benchmark_cosine,
    "pattern_match_single": benchmark_pattern_single,
    "pattern_match_batch": benchmark_pattern_batch,
}
ALIASES = {
    "dtw": "dtw_distance",
    "cosine": "cosine_similarity",
    "pattern": "pattern_match_single",
    "single": "pattern_match_single",
    "batch": "pattern_match_batch",
}


def get_git_commit(repo_root: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=2,
        )
    except (OSError, subprocess.SubprocessError):
        return "unknown"
    commit = completed.stdout.strip()
    return commit or "unknown"


def detect_os() -> str:
    system = platform.system()
    if system == "Windows":
        # Windows 11 still reports 10.0 through platform.release(); use the
        # build number when available and otherwise retain a conservative name.
        version_parts = platform.version().split(".")
        try:
            build = int(version_parts[-1])
        except (ValueError, IndexError):
            build = 0
        return "Windows 11" if build >= 22000 else "Windows"
    return f"{system} {platform.release()}".strip()


def collect_environment(commit: str, date: str) -> Dict[str, str]:
    system = platform.system()
    default_compiler = "MSVC (version unknown)" if system == "Windows" else "unknown"
    default_optimization = "/O2 (Release build assumed)" if system == "Windows" else "unknown"
    cpu = (
        os.environ.get("PROCESSOR_IDENTIFIER")
        or platform.processor()
        or platform.machine()
        or "unknown"
    )
    return {
        "os": detect_os(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "compiler": os.environ.get("ETF_BENCHMARK_COMPILER", default_compiler),
        "optimization": os.environ.get(
            "ETF_BENCHMARK_OPTIMIZATION", default_optimization
        ),
        "cpu": cpu,
        "machine": platform.machine(),
        "commit": commit,
        "date": date,
    }


def format_us(value: float) -> str:
    if value >= 1000:
        return f"{value:,.1f}"
    return f"{value:.2f}"


def format_ci(ci: Sequence[float]) -> str:
    return f"[{format_us(ci[0])}, {format_us(ci[1])}]"


def build_payload(
    environment: Dict[str, str],
    warmup_runs: int,
    timed_runs: int,
    result_rows: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return {
        "environment": environment,
        "methodology": {
            "warmup_runs": warmup_runs,
            "timed_runs": timed_runs,
            "statistic": "median",
            "ci_level": 95,
            "ci_method": "percentile",
            "percentiles": [2.5, 97.5],
            "timer": "time.perf_counter",
            "timing_unit": "microseconds",
            "input_conversion_included": False,
            "call_boundary_included": True,
        },
        "inputs": {
            "random_seed": RANDOM_SEED,
            "dtw_length": 19,
            "dtw_window": 5,
            "pattern_prices_length": 1000,
            "pattern_single_T_idx": 500,
            "batch_timestamps": 100,
            "batch_T_idx_range": [400, 499],
            "batch_api_note": "etf_core.pattern_match_batch accepts one 1-D price series; 50 is cos_prefilter_top.",
        },
        "results": result_rows,
    }


def run(args: argparse.Namespace) -> Path:
    if args.repeat < 1:
        raise SystemExit("--repeat 必须是正整数")
    if args.warmup < 0:
        raise SystemExit("--warmup 不能为负数")

    selected_name = args.function
    if selected_name == "all":
        selected = list(BENCHMARKS)
    else:
        selected_name = ALIASES.get(selected_name, selected_name)
        if selected_name not in BENCHMARKS:
            choices = ", ".join(["all", *ALIASES.keys(), *BENCHMARKS.keys()])
            raise SystemExit(f"未知函数 {args.function!r}；可选值: {choices}")
        selected = [selected_name]

    fixtures = make_fixtures()
    # 一致性检查不计入 benchmark，但能避免输出没有意义的速度数字。
    if "pattern_match_single" in selected:
        _validate_single_pattern(fixtures)
    if "pattern_match_batch" in selected:
        _validate_batch_pattern(fixtures)

    result_rows: List[Dict[str, Any]] = []
    for name in selected:
        python_fn, cpp_fn = BENCHMARKS[name](fixtures)
        python_stats = _measure(python_fn, args.warmup, args.repeat)
        cpp_stats = _measure(cpp_fn, args.warmup, args.repeat)
        cpp_median = cpp_stats["median_us"]
        speedup = (
            python_stats["median_us"] / cpp_median
            if cpp_median > 0
            else math.inf
        )
        result_rows.append(
            {
                "function": name,
                "python_median_us": python_stats["median_us"],
                "cpp_median_us": cpp_stats["median_us"],
                "speedup_median": float(speedup),
                "python_mean_us": python_stats["mean_us"],
                "cpp_mean_us": cpp_stats["mean_us"],
                "python_std_us": python_stats["std_us"],
                "cpp_std_us": cpp_stats["std_us"],
                "python_ci_95": python_stats["ci_95"],
                "cpp_ci_95": cpp_stats["ci_95"],
            }
        )

    date = dt.date.today().isoformat()
    repo_root = Path(__file__).resolve().parent.parent
    commit = get_git_commit(repo_root)
    environment = collect_environment(commit, date)
    payload = build_payload(environment, args.warmup, args.repeat, result_rows)

    if args.output_json:
        output_path = Path(args.output_json)
        if not output_path.is_absolute():
            output_path = Path.cwd() / output_path
    else:
        output_path = Path(__file__).resolve().parent / "results" / f"{date}-{commit}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print("## Benchmark Results")
    print()
    print(
        "Environment: "
        f"{environment['os']}, Python {environment['python']}, "
        f"NumPy {environment['numpy']}, {environment['compiler']} "
        f"{environment['optimization']}"
    )
    print(f"Commit: {commit}")
    print(f"Date: {date}")
    print()
    print("| Function | Python Median (µs) | C++ Median (µs) | Speedup | 95% CI |")
    print("|----------|-------------------|-----------------|---------|--------|")
    for row in result_rows:
        print(
            f"| {row['function']} | {format_us(row['python_median_us'])} | "
            f"{format_us(row['cpp_median_us'])} | {row['speedup_median']:.2f}x | "
            f"Python {format_ci(row['python_ci_95'])} / C++ {format_ci(row['cpp_ci_95'])} |"
        )

    print()
    print("### Detailed statistics")
    print()
    print("| Function | Python Mean ± Std (µs) | C++ Mean ± Std (µs) |")
    print("|----------|------------------------|---------------------|")
    for row in result_rows:
        print(
            f"| {row['function']} | "
            f"{format_us(row['python_mean_us'])} ± {format_us(row['python_std_us'])} | "
            f"{format_us(row['cpp_mean_us'])} ± {format_us(row['cpp_std_us'])} |"
        )

    print()
    print(f"JSON: {output_path.as_posix()}")
    print()
    print("## JSON")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return output_path


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="可复现的 etf_core 性能基准测试")
    parser.add_argument(
        "--function",
        default="all",
        help=(
            "要运行的函数：all、dtw、cosine、pattern_match_single 或 "
            "pattern_match_batch（默认：all）"
        ),
    )
    parser.add_argument(
        "--repeat",
        type=int,
        default=DEFAULT_TIMED_RUNS,
        help=f"计时轮次（默认：{DEFAULT_TIMED_RUNS}）",
    )
    parser.add_argument(
        "--warmup",
        type=int,
        default=DEFAULT_WARMUP_RUNS,
        help=f"每个实现的 warm-up 次数（默认：{DEFAULT_WARMUP_RUNS}）",
    )
    parser.add_argument(
        "--output-json",
        default=None,
        help="指定 JSON 输出路径；默认写入 benchmarks/results/YYYY-MM-DD-<commit>.json",
    )
    return parser.parse_args(argv)


if __name__ == "__main__":
    run(parse_args())

--- .github/workflows/ci.yml ---
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: CI

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build-and-test:
    strategy:
      fail-fast: false
      matrix:
        os:
          - windows-latest
          - ubuntu-latest
          - macos-latest

    runs-on: ${{ matrix.os }}

    env:
      PYTHONIOENCODING: utf-8

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        id: python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Linux build tools
        if: runner.os == 'Linux'
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Install macOS build tools
        if: runner.os == 'macOS'
        run: brew install cmake

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy pybind11 pytest

      - name: Configure CMake
        if: runner.os == 'Windows'
        run: |
          $pythonPath = (Get-Command python).Source
          cmake -B build -DPython_EXECUTABLE="$pythonPath" -DCMAKE_BUILD_TYPE=Release

      - name: Configure CMake (Linux/macOS)
        if: runner.os != 'Windows'
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -B build -DPython_EXECUTABLE="$python_path" -DCMAKE_BUILD_TYPE=Release

      - name: Build
        run: cmake --build build --config Release

      - name: Set PYTHONPATH (Linux/macOS)
        if: runner.os != 'Windows'
        run: echo "PYTHONPATH=build:${{ github.workspace }}/build" >> $GITHUB_ENV

      - name: Run tests
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python -m pytest tests/ -v

      - name: Verify C++ vs Python consistency
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python verify_etf_core.py

      - name: Verify batch matching
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python verify_batch.py

--- benchmark results files ---

--- E:\workspace\projects\形态匹配ETF策略-pybind11\benchmarks\results\.gitkeep ---
--- E:\workspace\projects\形态匹配ETF策略-pybind11\benchmarks\results\2026-07-16-ca13e26.json ---
Name                    Length LastWriteTime     
----                    ------ -------------     
.gitkeep                     0 2026/7/16 17:15:46
2026-07-16-ca13e26.json   3231 2026/7/16 17:20:33
{
  "environment": {
    "os": "Windows 11",
    "python": "3.12.7",
    "numpy": "2.4.4",
    "compiler": "MSVC (version unknown)",
    "optimization": "/O2 (Release build assumed)",
    "cpu": "Intel64 Family 6 Model 183 Stepping 1, GenuineIntel",
    "machine": "AMD64",
    "commit": "ca13e26",
    "date": "2026-07-16"
  },
  "methodology": {
    "warmup_runs": 5,
    "timed_runs": 100,
    "statistic": "median",
    "ci_level": 95,
    "ci_method": "percentile",
    "percentiles": [
      2.5,
      97.5
    ],
    "timer": "time.perf_counter",
    "timing_unit": "microseconds",
    "input_conversion_included": false,
    "call_boundary_included": true
  },
  "inputs": {
    "random_seed": 42,
    "dtw_length": 19,
    "dtw_window": 5,
    "pattern_prices_length": 1000,
    "pattern_single_T_idx": 500,
    "batch_timestamps": 100,
    "batch_T_idx_range": [
      400,
      499
    ],
    "batch_api_note": "etf_core.pattern_match_batch accepts one 1-D price series; 50 is cos_prefilter_top."
  },
  "results": [
    {
      "function": "dtw_distance",
      "python_median_us": 95.74999967298936,
      "cpp_median_us": 2.7999994927085936,
      "speedup_median": 34.19643465019528,
      "python_mean_us": 96.59500008638133,
      "cpp_mean_us": 3.049999868380837,
      "python_std_us": 8.557297954098495,
      "cpp_std_us": 0.7012974836480707,
      "python_ci_95": [
        90.34750037244521,
        116.62500014608646
      ],
      "cpp_ci_95": [
        2.70000055024866,
        4.804999252883134
      ]
    },
    {
      "function": "cosine_similarity",
      "python_median_us": 2.4000000848900527,
      "cpp_median_us": 0.6999998731771484,
      "speedup_median": 3.4285721710162176,
      "python_mean_us": 2.4340000527445227,
      "cpp_mean_us": 0.6659998507529963,
      "python_std_us": 0.7367988942491172,
      "cpp_std_us": 0.05359790870846016,
      "python_ci_95": [
        2.2999993234407157,
        2.5000008463393897
      ],
      "cpp_ci_95": [
        0.5999991117278114,
        0.7525001819885793
      ]
    },
    {
      "function": "pattern_match_single",
      "python_median_us": 13976.25000026892,
      "cpp_median_us": 264.5999993546866,
      "speedup_median": 52.820294914416344,
      "python_mean_us": 14420.22100007307,
      "cpp_mean_us": 278.9390000725689,
      "python_std_us": 1355.4721225888447,
      "cpp_std_us": 68.19982060321671,
      "python_ci_95": [
        13136.750000285247,
        18516.582499751166
      ],
      "cpp_ci_95": [
        219.44750114926137,
        508.9349999707337
      ]
    },
    {
      "function": "pattern_match_batch",
      "python_median_us": 1412466.5999997887,
      "cpp_median_us": 15137.45000011113,
      "speedup_median": 93.3094147289946,
      "python_mean_us": 1670540.4559999811,
      "cpp_mean_us": 15571.430999934817,
      "python_std_us": 644960.5075778764,
      "cpp_std_us": 1269.609817495821,
      "python_ci_95": [
        1336154.7225001685,
        3356455.5575001123
      ],
      "cpp_ci_95": [
        14216.449998684766,
        19329.202499511666
      ]
    }
  ]
}




exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- benchmark CLI/save excerpts ---'; Select-String -LiteralPath 'benchmarks/run_benchmark.py' -Pattern 'ArgumentParser|add_argument|output|results|json|speedup_median|cpp_median_us|def main|write_text|dump' -Context 3,5 -Encoding UTF8; Write-Host '--- full ci.yml ---'; Get-Content -LiteralPath '.github/workflows/ci.yml' -Raw -Encoding UTF8" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 207ms:
--- benchmark CLI/save excerpts ---

  benchmarks\run_benchmark.py:15:
  benchmarks\run_benchmark.py:16:import argparse
  benchmarks\run_benchmark.py:17:import datetime as dt
> benchmarks\run_benchmark.py:18:import json
  benchmarks\run_benchmark.py:19:import math
  benchmarks\run_benchmark.py:20:import os
  benchmarks\run_benchmark.py:21:import platform
  benchmarks\run_benchmark.py:22:import subprocess
  benchmarks\run_benchmark.py:23:import sys
  benchmarks\run_benchmark.py:385:def _validate_batch_pattern(fixtures: Dict[str, Any]) -> None:
  benchmarks\run_benchmark.py:386:    prices = fixtures["batch_prices"]
  benchmarks\run_benchmark.py:387:    t_indices = fixtures["batch_t_indices"]
> benchmarks\run_benchmark.py:388:    py_results = py_pattern_match_batch(prices, t_indices)
  benchmarks\run_benchmark.py:389:    cpp_features, cpp_mask = etf_core.pattern_match_batch(prices, t_indices)
  benchmarks\run_benchmark.py:390:    cpp_features = np.asarray(cpp_features)
  benchmarks\run_benchmark.py:391:    cpp_mask = np.asarray(cpp_mask, dtype=bool)
  benchmarks\run_benchmark.py:392:
  benchmarks\run_benchmark.py:393:    if cpp_features.shape[0] != int(cpp_mask.sum()) or cpp_features.shape[1] != 15:
  benchmarks\run_benchmark.py:399:    row = 0
  benchmarks\run_benchmark.py:400:    for index, valid in enumerate(cpp_mask):
  benchmarks\run_benchmark.py:401:        if not valid:
> benchmarks\run_benchmark.py:402:            if py_results[index] is not None:
  benchmarks\run_benchmark.py:403:                raise RuntimeError("pattern_match_batch validity mismatch")
  benchmarks\run_benchmark.py:404:            continue
> benchmarks\run_benchmark.py:405:        if py_results[index] is None:
  benchmarks\run_benchmark.py:406:            raise RuntimeError("pattern_match_batch validity mismatch")
  benchmarks\run_benchmark.py:407:        for column, key in enumerate(FEATURE_KEYS):
> benchmarks\run_benchmark.py:408:            _assert_close_scalar(key, float(py_results[index][key]), float(cpp_featur
es[row, column]))
  benchmarks\run_benchmark.py:409:        row += 1
  benchmarks\run_benchmark.py:410:
  benchmarks\run_benchmark.py:411:
  benchmarks\run_benchmark.py:412:def benchmark_dtw(fixtures: Dict[str, Any]) -> Tuple[Callable[[], Any], Callable[[], 
Any]]:
  benchmarks\run_benchmark.py:413:    x, y = fixtures["dtw_x"], fixtures["dtw_y"]
  benchmarks\run_benchmark.py:466:            ["git", "rev-parse", "--short", "HEAD"],
  benchmarks\run_benchmark.py:467:            cwd=repo_root,
  benchmarks\run_benchmark.py:468:            check=True,
> benchmarks\run_benchmark.py:469:            capture_output=True,
  benchmarks\run_benchmark.py:470:            text=True,
  benchmarks\run_benchmark.py:471:            encoding="utf-8",
  benchmarks\run_benchmark.py:472:            timeout=2,
  benchmarks\run_benchmark.py:473:        )
  benchmarks\run_benchmark.py:474:    except (OSError, subprocess.SubprocessError):
  benchmarks\run_benchmark.py:556:            "batch_T_idx_range": [400, 499],
  benchmarks\run_benchmark.py:557:            "batch_api_note": "etf_core.pattern_match_batch accepts one 1-D price ser
ies; 50 is cos_prefilter_top.",
  benchmarks\run_benchmark.py:558:        },
> benchmarks\run_benchmark.py:559:        "results": result_rows,
  benchmarks\run_benchmark.py:560:    }
  benchmarks\run_benchmark.py:561:
  benchmarks\run_benchmark.py:562:
  benchmarks\run_benchmark.py:563:def run(args: argparse.Namespace) -> Path:
  benchmarks\run_benchmark.py:564:    if args.repeat < 1:
  benchmarks\run_benchmark.py:598:            {
  benchmarks\run_benchmark.py:599:                "function": name,
  benchmarks\run_benchmark.py:600:                "python_median_us": python_stats["median_us"],
> benchmarks\run_benchmark.py:601:                "cpp_median_us": cpp_stats["median_us"],
> benchmarks\run_benchmark.py:602:                "speedup_median": float(speedup),
  benchmarks\run_benchmark.py:603:                "python_mean_us": python_stats["mean_us"],
  benchmarks\run_benchmark.py:604:                "cpp_mean_us": cpp_stats["mean_us"],
  benchmarks\run_benchmark.py:605:                "python_std_us": python_stats["std_us"],
  benchmarks\run_benchmark.py:606:                "cpp_std_us": cpp_stats["std_us"],
  benchmarks\run_benchmark.py:607:                "python_ci_95": python_stats["ci_95"],
  benchmarks\run_benchmark.py:615:    environment = collect_environment(commit, date)
  benchmarks\run_benchmark.py:616:    payload = build_payload(environment, args.warmup, args.repeat, result_rows)
  benchmarks\run_benchmark.py:617:
> benchmarks\run_benchmark.py:618:    if args.output_json:
> benchmarks\run_benchmark.py:619:        output_path = Path(args.output_json)
> benchmarks\run_benchmark.py:620:        if not output_path.is_absolute():
> benchmarks\run_benchmark.py:621:            output_path = Path.cwd() / output_path
  benchmarks\run_benchmark.py:622:    else:
> benchmarks\run_benchmark.py:623:        output_path = Path(__file__).resolve().parent / "results" / f"{date}-{commit}
.json"
> benchmarks\run_benchmark.py:624:    output_path.parent.mkdir(parents=True, exist_ok=True)
> benchmarks\run_benchmark.py:625:    output_path.write_text(
> benchmarks\run_benchmark.py:626:        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
  benchmarks\run_benchmark.py:627:    )
  benchmarks\run_benchmark.py:628:
> benchmarks\run_benchmark.py:629:    print("## Benchmark Results")
  benchmarks\run_benchmark.py:630:    print()
  benchmarks\run_benchmark.py:631:    print(
  benchmarks\run_benchmark.py:632:        "Environment: "
  benchmarks\run_benchmark.py:633:        f"{environment['os']}, Python {environment['python']}, "
  benchmarks\run_benchmark.py:634:        f"NumPy {environment['numpy']}, {environment['compiler']} "
  benchmarks\run_benchmark.py:642:    for row in result_rows:
  benchmarks\run_benchmark.py:643:        print(
  benchmarks\run_benchmark.py:644:            f"| {row['function']} | {format_us(row['python_median_us'])} | "
> benchmarks\run_benchmark.py:645:            f"{format_us(row['cpp_median_us'])} | {row['speedup_median']:.2f}x | "
  benchmarks\run_benchmark.py:646:            f"Python {format_ci(row['python_ci_95'])} / C++ {format_ci(row['cpp_ci_95
'])} |"
  benchmarks\run_benchmark.py:647:        )
  benchmarks\run_benchmark.py:648:
  benchmarks\run_benchmark.py:649:    print()
  benchmarks\run_benchmark.py:650:    print("### Detailed statistics")
  benchmarks\run_benchmark.py:659:        )
  benchmarks\run_benchmark.py:660:
  benchmarks\run_benchmark.py:661:    print()
> benchmarks\run_benchmark.py:662:    print(f"JSON: {output_path.as_posix()}")
  benchmarks\run_benchmark.py:663:    print()
> benchmarks\run_benchmark.py:664:    print("## JSON")
> benchmarks\run_benchmark.py:665:    print(json.dumps(payload, ensure_ascii=False, indent=2))
> benchmarks\run_benchmark.py:666:    return output_path
  benchmarks\run_benchmark.py:667:
  benchmarks\run_benchmark.py:668:
  benchmarks\run_benchmark.py:669:def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
> benchmarks\run_benchmark.py:670:    parser = argparse.ArgumentParser(description="可复现的 etf_core 性能基准测试")
> benchmarks\run_benchmark.py:671:    parser.add_argument(
  benchmarks\run_benchmark.py:672:        "--function",
  benchmarks\run_benchmark.py:673:        default="all",
  benchmarks\run_benchmark.py:674:        help=(
  benchmarks\run_benchmark.py:675:            "要运行的函数：all、dtw、cosine、pattern_match_single 或 "
  benchmarks\run_benchmark.py:676:            "pattern_match_batch（默认：all）"
  benchmarks\run_benchmark.py:677:        ),
  benchmarks\run_benchmark.py:678:    )
> benchmarks\run_benchmark.py:679:    parser.add_argument(
  benchmarks\run_benchmark.py:680:        "--repeat",
  benchmarks\run_benchmark.py:681:        type=int,
  benchmarks\run_benchmark.py:682:        default=DEFAULT_TIMED_RUNS,
  benchmarks\run_benchmark.py:683:        help=f"计时轮次（默认：{DEFAULT_TIMED_RUNS}）",
  benchmarks\run_benchmark.py:684:    )
> benchmarks\run_benchmark.py:685:    parser.add_argument(
  benchmarks\run_benchmark.py:686:        "--warmup",
  benchmarks\run_benchmark.py:687:        type=int,
  benchmarks\run_benchmark.py:688:        default=DEFAULT_WARMUP_RUNS,
  benchmarks\run_benchmark.py:689:        help=f"每个实现的 warm-up 次数（默认：{DEFAULT_WARMUP_RUNS}）",
  benchmarks\run_benchmark.py:690:    )
> benchmarks\run_benchmark.py:691:    parser.add_argument(
> benchmarks\run_benchmark.py:692:        "--output-json",
  benchmarks\run_benchmark.py:693:        default=None,
> benchmarks\run_benchmark.py:694:        help="指定 JSON 输出路径；默认写入 benchmarks/results/YYYY-MM-DD-<commit>.json",
  benchmarks\run_benchmark.py:695:    )
  benchmarks\run_benchmark.py:696:    return parser.parse_args(argv)
  benchmarks\run_benchmark.py:697:
  benchmarks\run_benchmark.py:698:
  benchmarks\run_benchmark.py:699:if __name__ == "__main__":
--- full ci.yml ---
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: CI

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build-and-test:
    strategy:
      fail-fast: false
      matrix:
        os:
          - windows-latest
          - ubuntu-latest
          - macos-latest

    runs-on: ${{ matrix.os }}

    env:
      PYTHONIOENCODING: utf-8

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        id: python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Linux build tools
        if: runner.os == 'Linux'
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Install macOS build tools
        if: runner.os == 'macOS'
        run: brew install cmake

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy pybind11 pytest

      - name: Configure CMake
        if: runner.os == 'Windows'
        run: |
          $pythonPath = (Get-Command python).Source
          cmake -B build -DPython_EXECUTABLE="$pythonPath" -DCMAKE_BUILD_TYPE=Release

      - name: Configure CMake (Linux/macOS)
        if: runner.os != 'Windows'
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -B build -DPython_EXECUTABLE="$python_path" -DCMAKE_BUILD_TYPE=Release

      - name: Build
        run: cmake --build build --config Release

      - name: Set PYTHONPATH (Linux/macOS)
        if: runner.os != 'Windows'
        run: echo "PYTHONPATH=build:${{ github.workspace }}/build" >> $GITHUB_ENV

      - name: Run tests
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python -m pytest tests/ -v

      - name: Verify C++ vs Python consistency
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python verify_etf_core.py

      - name: Verify batch matching
        env:
          PYTHONIOENCODING: utf-8
          PYTHONPATH: ${{ env.PYTHONPATH }}
        run: python verify_batch.py




exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -LiteralPath '"'benchmarks/run_benchmark.py' -Encoding UTF8; for ("'$i = 550; $i -le 705; $i++) { if ($i -le $lines.Count) { '"'{0,4}: {1}' -f "'$i, $lines[$i-1] } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 163ms:
 550:             "random_seed": RANDOM_SEED,
 551:             "dtw_length": 19,
 552:             "dtw_window": 5,
 553:             "pattern_prices_length": 1000,
 554:             "pattern_single_T_idx": 500,
 555:             "batch_timestamps": 100,
 556:             "batch_T_idx_range": [400, 499],
 557:             "batch_api_note": "etf_core.pattern_match_batch accepts one 1-D price series; 50 is cos_prefilter_top.",
 558:         },
 559:         "results": result_rows,
 560:     }
 561: 
 562: 
 563: def run(args: argparse.Namespace) -> Path:
 564:     if args.repeat < 1:
 565:         raise SystemExit("--repeat 必须是正整数")
 566:     if args.warmup < 0:
 567:         raise SystemExit("--warmup 不能为负数")
 568: 
 569:     selected_name = args.function
 570:     if selected_name == "all":
 571:         selected = list(BENCHMARKS)
 572:     else:
 573:         selected_name = ALIASES.get(selected_name, selected_name)
 574:         if selected_name not in BENCHMARKS:
 575:             choices = ", ".join(["all", *ALIASES.keys(), *BENCHMARKS.keys()])
 576:             raise SystemExit(f"未知函数 {args.function!r}；可选值: {choices}")
 577:         selected = [selected_name]
 578: 
 579:     fixtures = make_fixtures()
 580:     # 一致性检查不计入 benchmark，但能避免输出没有意义的速度数字。
 581:     if "pattern_match_single" in selected:
 582:         _validate_single_pattern(fixtures)
 583:     if "pattern_match_batch" in selected:
 584:         _validate_batch_pattern(fixtures)
 585: 
 586:     result_rows: List[Dict[str, Any]] = []
 587:     for name in selected:
 588:         python_fn, cpp_fn = BENCHMARKS[name](fixtures)
 589:         python_stats = _measure(python_fn, args.warmup, args.repeat)
 590:         cpp_stats = _measure(cpp_fn, args.warmup, args.repeat)
 591:         cpp_median = cpp_stats["median_us"]
 592:         speedup = (
 593:             python_stats["median_us"] / cpp_median
 594:             if cpp_median > 0
 595:             else math.inf
 596:         )
 597:         result_rows.append(
 598:             {
 599:                 "function": name,
 600:                 "python_median_us": python_stats["median_us"],
 601:                 "cpp_median_us": cpp_stats["median_us"],
 602:                 "speedup_median": float(speedup),
 603:                 "python_mean_us": python_stats["mean_us"],
 604:                 "cpp_mean_us": cpp_stats["mean_us"],
 605:                 "python_std_us": python_stats["std_us"],
 606:                 "cpp_std_us": cpp_stats["std_us"],
 607:                 "python_ci_95": python_stats["ci_95"],
 608:                 "cpp_ci_95": cpp_stats["ci_95"],
 609:             }
 610:         )
 611: 
 612:     date = dt.date.today().isoformat()
 613:     repo_root = Path(__file__).resolve().parent.parent
 614:     commit = get_git_commit(repo_root)
 615:     environment = collect_environment(commit, date)
 616:     payload = build_payload(environment, args.warmup, args.repeat, result_rows)
 617: 
 618:     if args.output_json:
 619:         output_path = Path(args.output_json)
 620:         if not output_path.is_absolute():
 621:             output_path = Path.cwd() / output_path
 622:     else:
 623:         output_path = Path(__file__).resolve().parent / "results" / f"{date}-{commit}.json"
 624:     output_path.parent.mkdir(parents=True, exist_ok=True)
 625:     output_path.write_text(
 626:         json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
 627:     )
 628: 
 629:     print("## Benchmark Results")
 630:     print()
 631:     print(
 632:         "Environment: "
 633:         f"{environment['os']}, Python {environment['python']}, "
 634:         f"NumPy {environment['numpy']}, {environment['compiler']} "
 635:         f"{environment['optimization']}"
 636:     )
 637:     print(f"Commit: {commit}")
 638:     print(f"Date: {date}")
 639:     print()
 640:     print("| Function | Python Median (µs) | C++ Median (µs) | Speedup | 95% CI |")
 641:     print("|----------|-------------------|-----------------|---------|--------|")
 642:     for row in result_rows:
 643:         print(
 644:             f"| {row['function']} | {format_us(row['python_median_us'])} | "
 645:             f"{format_us(row['cpp_median_us'])} | {row['speedup_median']:.2f}x | "
 646:             f"Python {format_ci(row['python_ci_95'])} / C++ {format_ci(row['cpp_ci_95'])} |"
 647:         )
 648: 
 649:     print()
 650:     print("### Detailed statistics")
 651:     print()
 652:     print("| Function | Python Mean ± Std (µs) | C++ Mean ± Std (µs) |")
 653:     print("|----------|------------------------|---------------------|")
 654:     for row in result_rows:
 655:         print(
 656:             f"| {row['function']} | "
 657:             f"{format_us(row['python_mean_us'])} ± {format_us(row['python_std_us'])} | "
 658:             f"{format_us(row['cpp_mean_us'])} ± {format_us(row['cpp_std_us'])} |"
 659:         )
 660: 
 661:     print()
 662:     print(f"JSON: {output_path.as_posix()}")
 663:     print()
 664:     print("## JSON")
 665:     print(json.dumps(payload, ensure_ascii=False, indent=2))
 666:     return output_path
 667: 
 668: 
 669: def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
 670:     parser = argparse.ArgumentParser(description="可复现的 etf_core 性能基准测试")
 671:     parser.add_argument(
 672:         "--function",
 673:         default="all",
 674:         help=(
 675:             "要运行的函数：all、dtw、cosine、pattern_match_single 或 "
 676:             "pattern_match_batch（默认：all）"
 677:         ),
 678:     )
 679:     parser.add_argument(
 680:         "--repeat",
 681:         type=int,
 682:         default=DEFAULT_TIMED_RUNS,
 683:         help=f"计时轮次（默认：{DEFAULT_TIMED_RUNS}）",
 684:     )
 685:     parser.add_argument(
 686:         "--warmup",
 687:         type=int,
 688:         default=DEFAULT_WARMUP_RUNS,
 689:         help=f"每个实现的 warm-up 次数（默认：{DEFAULT_WARMUP_RUNS}）",
 690:     )
 691:     parser.add_argument(
 692:         "--output-json",
 693:         default=None,
 694:         help="指定 JSON 输出路径；默认写入 benchmarks/results/YYYY-MM-DD-<commit>.json",
 695:     )
 696:     return parser.parse_args(argv)
 697: 
 698: 
 699: if __name__ == "__main__":
 700:     run(parse_args())

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- AGENTS.md files ---'; Get-ChildItem -LiteralPath . -Filter AGENTS.md -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object { "'$_.FullName }; Write-Host '"'--- existing benchmark workflow ---'; if (Test-Path -LiteralPath '.github/workflows/benchmark.yml') { Get-Content -LiteralPath '.github/workflows/benchmark.yml' -Raw -Encoding UTF8 } else { Write-Host '(not present)' }; Write-Host '--- git status ---'; git status --short" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 206ms:
--- AGENTS.md files ---
--- existing benchmark workflow ---
(not present)
--- git status ---
 M project_status.md
?? _review/prompts/prompt_5_perf_ci.md
?? _review/prompts/prompt_5_perf_ci_output.md
?? docs/reviews/performance-analysis-review-kimi.md
?? improvement_plan.md
?? notebooks/01_price_series.png
?? notebooks/02_query_window.png
?? notebooks/03_cosine_prefilter.png
?? notebooks/04_dtw_warping.png
?? notebooks/05_feature_evolution.png
?? notebooks/06_trading_signals.png
?? notebooks/07_batch_dtw.png
?? notebooks/08_benchmark.png
?? prompt_p0_build.md
?? prompt_p1_benchmark.md

2026-07-17T12:03:10.389581Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$content = @'"'
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Performance Benchmark

on:
  push:
    branches: [master]

permissions:
  contents: write

concurrency:
  group: performance-benchmark-"'${{ github.ref }}
  cancel-in-progress: true

jobs:
  benchmark:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '"'3.12'

      - name: Install build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy pybind11

      - name: Configure CMake
        run: |
          python_path=\""'$(python -c '"'import sys; print(sys.executable)')\"
          cmake -B build -DPython_EXECUTABLE=\""'$python_path" -DCMAKE_BUILD_TYPE=Release

      - name: Build
        run: cmake --build build --config Release

      - name: Set PYTHONPATH
        run: echo "PYTHONPATH=build:${{ github.workspace }}/build" >> "$GITHUB_ENV"

      - name: Locate baseline
        id: baseline
        shell: bash
        run: |
          set -euo pipefail

          baseline="$(
            git log --format= --name-only --diff-filter=AM -- '"'benchmarks/results/*.json' \\
              | awk 'NF { print; exit }'
          )\"

          if [[ -z \""'$baseline" || ! -f "$baseline" ]]; then
            baseline="$(find benchmarks/results -maxdepth 1 -type f -name '"'*.json' | sort | tail -n 1)\"
          fi

          if [[ -z \""'$baseline" || ! -f "$baseline" ]]; then
            echo "::error::No baseline JSON file found in benchmarks/results/."
            exit 1
          fi

          snapshot="$RUNNER_TEMP/benchmark-baseline.json"
          cp "$baseline" "$snapshot"
          echo "source=$baseline" >> "$GITHUB_OUTPUT"
          echo "snapshot=$snapshot" >> "$GITHUB_OUTPUT"
          echo "Using baseline: $baseline"

      - name: Run benchmark
        id: current
        shell: bash
        run: |
          set -euo pipefail
          result="benchmarks/results/$(date -u +%F)-${GITHUB_SHA::7}.json"
          echo "path=$result" >> "$GITHUB_OUTPUT"
          python benchmarks/run_benchmark.py --repeat 50 --output-json "$result"

      - name: Compare with baseline
        id: compare
        shell: bash
        env:
          BASELINE_JSON: ${{ steps.baseline.outputs.snapshot }}
          BASELINE_SOURCE: ${{ steps.baseline.outputs.source }}
          CURRENT_JSON: ${{ steps.current.outputs.path }}
        run: |
          python - <<'"'PY'
          import json
          import os
          import sys
          from pathlib import Path

          WARN_RATIO = 1.15
          FAIL_RATIO = 1.25

          def load_medians(path: str) -> dict[str, float]:
              payload = json.loads(Path(path).read_text(encoding=\"utf-8\"))
              return {
                  row[\"function\"]: float(row[\"cpp_median_us\"])
                  for row in payload[\"results\"]
              }

          baseline = load_medians(os.environ[\"BASELINE_JSON\"])
          current = load_medians(os.environ[\"CURRENT_JSON\"])

          missing = sorted(set(baseline) - set(current))
          unexpected = sorted(set(current) - set(baseline))
          if missing or unexpected:
              details = []
              if missing:
                  details.append(f\"missing current results: {', '.join(missing)}\")
              if unexpected:
                  details.append(f\"unexpected current results: {', '.join(unexpected)}\")
              print(f\"::error::Benchmark result mismatch ({'; '.join(details)}).\")
              with open(os.environ[\"GITHUB_OUTPUT\"], \"a\", encoding=\"utf-8\") as output:
                  output.write(\"update_baseline=false\\n\")
              raise SystemExit(1)

          warnings = []
          failures = []
          table = [
              f\"{'Function':<24} {'Baseline':>12} {'Current':>12} {'Change':>18}\",
              f\"{'-' * 24} {'-' * 12} {'-' * 12} {'-' * 18}\",
          ]

          for function, baseline_median in baseline.items():
              current_median = current[function]
              if baseline_median <= 0:
                  print(f\"::error::Invalid non-positive baseline median for {function}.\")
                  with open(os.environ[\"GITHUB_OUTPUT\"], \"a\", encoding=\"utf-8\") as output:
                      output.write(\"update_baseline=false\\n\")
                  raise SystemExit(1)

              change_percent = (current_median / baseline_median - 1.0) * 100.0
              if current_median > baseline_median * FAIL_RATIO:
                  status = \"FAIL\"
                  failures.append((function, change_percent))
              elif current_median > baseline_median * WARN_RATIO:
                  status = \"WARN\"
                  warnings.append((function, change_percent))
              else:
                  status = \"OK\"

              change = f\"{change_percent:+.1f}% {status}\"
              table.append(
                  f\"{function:<24} \"
                  f\"{baseline_median:>8.1f} us \"
                  f\"{current_median:>8.1f} us \"
                  f\"{change:>18}\"
              )

          print(f\"Baseline file: {os.environ['BASELINE_SOURCE']}\")
          print()
          print(\"\\n\".join(table))

          with open(os.environ[\"GITHUB_STEP_SUMMARY\"], \"a\", encoding=\"utf-8\") as summary:
              summary.write(\"## Performance regression check\\n\\n\")
              summary.write(f\"Baseline: "'`{os.environ['"'BASELINE_SOURCE']}"'`'"\\n\\n\")
              summary.write(\""'```text'"\\n\")
              summary.write(\"\\n\".join(table))
              summary.write(\"\\n"'```'"\\n\")

          for function, change_percent in warnings:
              print(
                  f\"::warning title=Performance regression::{function} slowed by \"
                  f\"{change_percent:.1f}% (warning threshold: 15%).\"
              )
          for function, change_percent in failures:
              print(
                  f\"::error title=Performance regression::{function} slowed by \"
                  f\"{change_percent:.1f}% (failure threshold: 25%).\"
              )

          update_baseline = not warnings and not failures
          with open(os.environ[\"GITHUB_OUTPUT\"], \"a\", encoding=\"utf-8\") as output:
              output.write(f\"update_baseline={'true' if update_baseline else 'false'}\\n\")

          if failures:
              sys.exit(1)
          PY

      - name: Update baseline
        if: success() && steps.compare.outputs.update_baseline == 'true'
        env:
          CURRENT_JSON: "'${{ steps.current.outputs.path }}
        run: |
          set -euo pipefail
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add -- "$CURRENT_JSON"

          if git diff --cached --quiet; then
            echo "Baseline is unchanged; nothing to commit."
            exit 0
          fi

          git commit -m "chore(benchmark): update performance baseline [skip ci]"
          git push origin HEAD:master
'"'@
"'$content = $content -replace "`r`n", "`n"
$path = Join-Path (Get-Location) '"'.github/workflows/benchmark.yml'
[System.IO.File]::WriteAllText("'$path, $content + "`n", [System.Text.UTF8Encoding]::new($false))' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 297ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Host '"'--- benchmark.yml ---'; Get-Content -LiteralPath '.github/workflows/benchmark.yml' -Raw -Encoding UTF8; Write-Host '--- git diff --check ---'; git diff --check -- .github/workflows/benchmark.yml; Write-Host '--- git status --short ---'; git status --short -- .github/workflows/benchmark.yml" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 218ms:
--- benchmark.yml ---
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Performance Benchmark

on:
  push:
    branches: [master]

permissions:
  contents: write

concurrency:
  group: performance-benchmark-${{ github.ref }}
  cancel-in-progress: true

jobs:
  benchmark:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy pybind11

      - name: Configure CMake
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -B build -DPython_EXECUTABLE="$python_path" -DCMAKE_BUILD_TYPE=Release

      - name: Build
        run: cmake --build build --config Release

      - name: Set PYTHONPATH
        run: echo "PYTHONPATH=build:${{ github.workspace }}/build" >> "$GITHUB_ENV"

      - name: Locate baseline
        id: baseline
        shell: bash
        run: |
          set -euo pipefail

          baseline="$(
            git log --format= --name-only --diff-filter=AM -- 'benchmarks/results/*.json' \
              | awk 'NF { print; exit }'
          )"

          if [[ -z "$baseline" || ! -f "$baseline" ]]; then
            baseline="$(find benchmarks/results -maxdepth 1 -type f -name '*.json' | sort | tail -n 1)"
          fi

          if [[ -z "$baseline" || ! -f "$baseline" ]]; then
            echo "::error::No baseline JSON file found in benchmarks/results/."
            exit 1
          fi

          snapshot="$RUNNER_TEMP/benchmark-baseline.json"
          cp "$baseline" "$snapshot"
          echo "source=$baseline" >> "$GITHUB_OUTPUT"
          echo "snapshot=$snapshot" >> "$GITHUB_OUTPUT"
          echo "Using baseline: $baseline"

      - name: Run benchmark
        id: current
        shell: bash
        run: |
          set -euo pipefail
          result="benchmarks/results/$(date -u +%F)-${GITHUB_SHA::7}.json"
          echo "path=$result" >> "$GITHUB_OUTPUT"
          python benchmarks/run_benchmark.py --repeat 50 --output-json "$result"

      - name: Compare with baseline
        id: compare
        shell: bash
        env:
          BASELINE_JSON: ${{ steps.baseline.outputs.snapshot }}
          BASELINE_SOURCE: ${{ steps.baseline.outputs.source }}
          CURRENT_JSON: ${{ steps.current.outputs.path }}
        run: |
          python - <<'PY'
          import json
          import os
          import sys
          from pathlib import Path

          WARN_RATIO = 1.15
          FAIL_RATIO = 1.25

          def load_medians(path: str) -> dict[str, float]:
              payload = json.loads(Path(path).read_text(encoding="utf-8"))
              return {
                  row["function"]: float(row["cpp_median_us"])
                  for row in payload["results"]
              }

          baseline = load_medians(os.environ["BASELINE_JSON"])
          current = load_medians(os.environ["CURRENT_JSON"])

          missing = sorted(set(baseline) - set(current))
          unexpected = sorted(set(current) - set(baseline))
          if missing or unexpected:
              details = []
              if missing:
                  details.append(f"missing current results: {', '.join(missing)}")
              if unexpected:
                  details.append(f"unexpected current results: {', '.join(unexpected)}")
              print(f"::error::Benchmark result mismatch ({'; '.join(details)}).")
              with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
                  output.write("update_baseline=false\n")
              raise SystemExit(1)

          warnings = []
          failures = []
          table = [
              f"{'Function':<24} {'Baseline':>12} {'Current':>12} {'Change':>18}",
              f"{'-' * 24} {'-' * 12} {'-' * 12} {'-' * 18}",
          ]

          for function, baseline_median in baseline.items():
              current_median = current[function]
              if baseline_median <= 0:
                  print(f"::error::Invalid non-positive baseline median for {function}.")
                  with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
                      output.write("update_baseline=false\n")
                  raise SystemExit(1)

              change_percent = (current_median / baseline_median - 1.0) * 100.0
              if current_median > baseline_median * FAIL_RATIO:
                  status = "FAIL"
                  failures.append((function, change_percent))
              elif current_median > baseline_median * WARN_RATIO:
                  status = "WARN"
                  warnings.append((function, change_percent))
              else:
                  status = "OK"

              change = f"{change_percent:+.1f}% {status}"
              table.append(
                  f"{function:<24} "
                  f"{baseline_median:>8.1f} us "
                  f"{current_median:>8.1f} us "
                  f"{change:>18}"
              )

          print(f"Baseline file: {os.environ['BASELINE_SOURCE']}")
          print()
          print("\n".join(table))

          with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as summary:
              summary.write("## Performance regression check\n\n")
              summary.write(f"Baseline: `{os.environ['BASELINE_SOURCE']}`\n\n")
              summary.write("```text\n")
              summary.write("\n".join(table))
              summary.write("\n```\n")

          for function, change_percent in warnings:
              print(
                  f"::warning title=Performance regression::{function} slowed by "
                  f"{change_percent:.1f}% (warning threshold: 15%)."
              )
          for function, change_percent in failures:
              print(
                  f"::error title=Performance regression::{function} slowed by "
                  f"{change_percent:.1f}% (failure threshold: 25%)."
              )

          update_baseline = not warnings and not failures
          with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
              output.write(f"update_baseline={'true' if update_baseline else 'false'}\n")

          if failures:
              sys.exit(1)
          PY

      - name: Update baseline
        if: success() && steps.compare.outputs.update_baseline == 'true'
        env:
          CURRENT_JSON: ${{ steps.current.outputs.path }}
        run: |
          set -euo pipefail
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add -- "$CURRENT_JSON"

          if git diff --cached --quiet; then
            echo "Baseline is unchanged; nothing to commit."
            exit 0
          fi

          git commit -m "chore(benchmark): update performance baseline [skip ci]"
          git push origin HEAD:master

--- git diff --check ---
--- git status --short ---
?? .github/workflows/benchmark.yml

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'
from pathlib import Path
try:
    import yaml
except ImportError:
    print('PyYAML not installed; skipped YAML parse')
else:
    path = Path('.github/workflows/benchmark.yml')
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    print(f\"Parsed workflow: {data.get('name')}\")
    print(f\"Jobs: {', '.join(data.get('jobs', {}))}\")
'@ | python -" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 194ms:
Parsed workflow: Performance Benchmark
Jobs: benchmark

codex
Created the complete workflow:

`E:/workspace/projects/形态匹配ETF策略-pybind11/.github/workflows/benchmark.yml`

It includes:

- Push-to-`master` trigger only
- `ubuntu-latest` with Python 3.12
- Release-mode C++ build
- Existing benchmark script with `--repeat 50`
- Repository baseline snapshot and same-job comparison
- One-sided thresholds: `WARN` above 15%, `FAIL` above 25%
- CI log and job-summary performance tables
- Baseline commit/push only when every result is `OK`
- `contents: write` permission
- Provenance comment
- Concurrency protection and `[skip ci]` on baseline commits

The workflow passed YAML parsing and `git diff --check`. Per your instruction, the CI/benchmark was not run.
tokens used
70,211
Created the complete workflow:

`E:/workspace/projects/形态匹配ETF策略-pybind11/.github/workflows/benchmark.yml`

It includes:

- Push-to-`master` trigger only
- `ubuntu-latest` with Python 3.12
- Release-mode C++ build
- Existing benchmark script with `--repeat 50`
- Repository baseline snapshot and same-job comparison
- One-sided thresholds: `WARN` above 15%, `FAIL` above 25%
- CI log and job-summary performance tables
- Baseline commit/push only when every result is `OK`
- `contents: write` permission
- Provenance comment
- Concurrency protection and `[skip ci]` on baseline commits

The workflow passed YAML parsing and `git diff --check`. Per your instruction, the CI/benchmark was not run.
