"""Type stubs for etf_core — C++ accelerated ETF pattern matching module."""

import numpy as np
from typing import Dict, Optional

# 模块常量：15 维特征名（顺序与 pattern_match_batch 的 features_X15 列一致）
FEATURE_KEYS: tuple[str, ...]


def standardize_returns(price_series: np.ndarray) -> np.ndarray:
    """
    计算标准化收益率序列: (rets - mean) / std.

    Args:
        price_series: 1-D float64 array, n >= 2.

    Returns:
        1-D float64 array, length n-1.
    """
    ...


def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """
    两向量余弦相似度 ∈ [-1, 1].
    norm < 1e-12 时返回 0.0.
    """
    ...


def dtw_distance(x: np.ndarray, y: np.ndarray, window: int = 5) -> float:
    """
    Sakoe-Chiba band DTW 距离.
    返回归一化距离: sqrt(dtw[n,m]) / (n+m).
    """
    ...


from typing import overload, Tuple

@overload
def dtw_distance_batch(
    query: np.ndarray, candidates: np.ndarray,
    window: int = 5, top_k: int = 0,
) -> np.ndarray:
    """top_k <= 0: 返回全部 distances (N,)."""
    ...

@overload
def dtw_distance_batch(
    query: np.ndarray, candidates: np.ndarray,
    window: int = 5, top_k: int = ...,
) -> Tuple[np.ndarray, np.ndarray]:
    """top_k > 0: 返回 (indices, distances) 各 (top_k,)."""
    ...


def compute_adx(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 14
) -> float:
    """
    ADX (Average Directional Index), Wilder's smoothing.
    数据不足时返回 25.0 (中性值).
    """
    ...


def compute_atr(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 14
) -> np.ndarray:
    """
    ATR (Average True Range). 前 n 天为 NaN.
    """
    ...


def pattern_match_single(
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
    """
    单 ETF 单时点形态匹配 → 15维特征字典.

    V3.0 余弦预筛选: 第1遍全量余弦 → 第2遍 DTW 精排.
    前视偏差防护: fut_end < T_idx 严格约束.

    Returns:
        dict with 15 keys or None.
        F1-F5:  top1_sim, top5_avg_sim, sim_decay, sim_variance, match_distance_ratio
        F6-F11: avg_future_ret, weighted_future_ret, median_future_ret,
                ret_sign_consistency, best_match_ret, max_dd_in_matches
        F12-F15: match_time_span, match_time_span_ratio, match_cluster_ratio,
                 n_matches_above_thresh
    """
    ...

def pattern_match_batch(
    prices: np.ndarray,
    t_indices: np.ndarray,
    k: int = 10,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
    M_forward: int = 5,
    dtw_window: int = 5,
    cos_prefilter_top: int = 50,
) -> tuple[np.ndarray, np.ndarray]:
    """
    批量形态匹配——同 ETF 多 T_idx。

    核心优化：候选窗口标准化收益率预计算，相邻 T_idx 共享缓存。

    Returns:
        (features_X15, valid_mask):
          - features_X15: (n_valid, 15) float64 — 仅有效样本
          - valid_mask: (n_samples,) bool
        feature_keys 已提升为模块常量 FEATURE_KEYS (15 str)。
    """
    ...
