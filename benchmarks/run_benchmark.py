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
