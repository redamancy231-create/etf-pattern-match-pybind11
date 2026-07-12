# -*- coding: utf-8 -*-
"""
形态匹配引擎 — 15维特征提取
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 389-627
=============================
从 形态匹配ETF组合策略_V3.3.py 提取，零掘金依赖（仅 numpy）。

模块内容:
  - pattern_match_single: 单ETF单时点形态匹配 + 15维特征提取
  - compute_pattern_features: 辅助函数，从匹配结果提取F1-F15
  - extract_morph_features: 便捷接口，接收标准化收益率一步完成

原始来源:
  V3.3.py 行 389-627 (pattern_match_single, V3.0 余弦预筛选)
  V3.3.py 行 362-382 (standardize_returns, cosine_similarity → 委托给 dtw.py)

算法逻辑零改动 — V3.0-FIX-1/1b/2/3/5 全部保留。
"""

import numpy as np
from typing import Dict, Optional

from .dtw import standardize_returns, cosine_similarity, dtw_distance


# ── 默认参数（与 V3.3.py 第一部分常量一致）──
_DEFAULT_L_QUERY = 20
_DEFAULT_T_BACK = 750
_DEFAULT_MATCH_STEP = 1
_DEFAULT_M_FORWARD = 5
_DEFAULT_K_MATCHES = 10
_DEFAULT_DTW_WINDOW = 5
_DEFAULT_COS_PREFILTER_TOP = 50


def pattern_match_single(
    prices: np.ndarray,
    T_idx: int,
    k: int = _DEFAULT_K_MATCHES,
    L_query: int = _DEFAULT_L_QUERY,
    T_back: int = _DEFAULT_T_BACK,
    match_step: int = _DEFAULT_MATCH_STEP,
    M_forward: int = _DEFAULT_M_FORWARD,
    dtw_window: int = _DEFAULT_DTW_WINDOW,
    cos_prefilter_top: int = _DEFAULT_COS_PREFILTER_TOP,
) -> Optional[Dict[str, float]]:
    """
    对单只 ETF 在时点 T_idx 执行形态匹配，提取 15 维特征。

    V3.0 余弦预筛选：第1遍仅计算余弦相似度(O(L))→取top-N→第2遍仅对top-N计算DTW。

    前视偏差防护（严格因果性约束）：
      - 查询窗口：[T_idx - L_query + 1, T_idx]
      - 历史搜索范围：[max(L_query - 1, T_idx - T_back), T_idx - L_query]
      - 匹配片段后续收益要求 fut_end < T_idx

    Args:
        prices: 完整价格序列, shape (n_days,)
        T_idx: 查询时点索引
        k: Top-K 匹配数（默认 10）
        L_query: 查询窗口长度（默认 20）
        T_back: 历史回溯范围（默认 750）
        match_step: 匹配步长（默认 1）
        M_forward: 预测窗口（默认 5）
        dtw_window: Sakoe-Chiba band 宽度（默认 5）
        cos_prefilter_top: 余弦预筛选保留数（默认 50）

    Returns:
        15维特征字典，数据不足时返回 None。
        键名: top1_sim, top5_avg_sim, sim_decay, sim_variance,
              match_distance_ratio, avg_future_ret, weighted_future_ret,
              median_future_ret, ret_sign_consistency, best_match_ret,
              max_dd_in_matches, match_time_span, match_time_span_ratio,
              match_cluster_ratio, n_matches_above_thresh

    算法逻辑: 与 V3.3.py 第 389-627 行完全一致。
    所有 V3.0-FIX 保留: fast_shape_dists, sigma_fast + DTW归一化修正,
    hist_rets缓存, global_min_cos/max_cos.
    """
    # ── 输入校验 ──
    if M_forward < 1:
        raise ValueError(f"M_forward must be >= 1, got {M_forward}")
    if L_query < 3:
        raise ValueError(f"L_query must be >= 3, got {L_query}")
    if match_step <= 0:
        raise ValueError(f"match_step must be > 0, got {match_step}")
    if T_idx < L_query + M_forward + 10:
        return None

    query_prices = prices[T_idx - L_query + 1: T_idx + 1]
    if len(query_prices) < L_query:
        return None

    query_rets = standardize_returns(query_prices)
    if len(query_rets) < 2:
        return None

    search_end = T_idx - L_query
    if search_end < L_query:
        return None

    search_start = max(L_query - 1, T_idx - T_back)

    # ═══════════════════════════════════════════════════════════════
    # 第1遍：余弦相似度 + 快速形状距离（全量候选）
    # ═══════════════════════════════════════════════════════════════
    cos_candidates: list = []        # (hist_end, hist_start, cos_s, hist_rets)
    fast_shape_dists: list = []      # V3.0-FIX-1: 全量快速距离

    for hist_end in range(search_start, search_end + 1, match_step):
        hist_start = hist_end - L_query + 1
        if hist_start < 0:
            continue

        hist_prices = prices[hist_start: hist_end + 1]
        if len(hist_prices) < L_query:
            continue

        hist_rets = standardize_returns(hist_prices)
        if len(hist_rets) < 2:
            continue

        cos_s = cosine_similarity(hist_rets, query_rets)

        # V3.0-FIX-1: 收集全量 fast_shape_dists（含 cos≤0）
        fast_d = np.sqrt(np.mean((hist_rets - query_rets) ** 2))
        fast_shape_dists.append(fast_d)

        if cos_s > 0:
            # V3.0-FIX-3: 缓存 hist_rets 避免第2遍重复标准化
            cos_candidates.append((hist_end, hist_start, cos_s, hist_rets))

    if len(cos_candidates) < 3:
        return None

    # V3.0-FIX-1b: sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
    # DTW ≈ RMSD / (2*sqrt(L_query-1))，sigma_fast 须同步缩放
    sigma_fast = (
        np.std(fast_shape_dists) / (2.0 * np.sqrt(L_query - 1))
        if len(fast_shape_dists) > 1
        else 1.0
    )
    sigma_fast = max(sigma_fast, 1e-12)

    # V3.0-FIX-5: 全量 cos>0 候选计算余弦归一化边界
    cos_candidates.sort(key=lambda x: x[2], reverse=True)
    all_cos_values = np.array([c[2] for c in cos_candidates])
    global_min_cos = float(np.min(all_cos_values)) if len(all_cos_values) > 0 else 0.0
    global_max_cos = float(np.max(all_cos_values)) if len(all_cos_values) > 0 else 1.0

    n_cos = min(cos_prefilter_top, len(cos_candidates))
    top_cos = cos_candidates[:n_cos]

    # ═══════════════════════════════════════════════════════════════
    # 第2遍：仅对余弦 top-N 计算 DTW
    # ═══════════════════════════════════════════════════════════════
    dtw_dists: list = []
    cos_sims: list = []
    future_rets: list = []
    match_end_indices: list = []

    for hist_end, hist_start, sim_cos, hist_rets in top_cos:
        dtw_d = dtw_distance(hist_rets, query_rets, window=dtw_window)

        dtw_dists.append(dtw_d)
        cos_sims.append(sim_cos)

        fut_end = hist_end + M_forward
        if fut_end < len(prices) and fut_end < T_idx:
            fut_ret = float(prices[fut_end] / prices[hist_end] - 1)
        else:
            fut_ret = np.nan
        future_rets.append(fut_ret)
        match_end_indices.append(hist_end)

    if len(dtw_dists) < 3:
        return None

    dtw_dists_arr = np.array(dtw_dists, dtype=np.float64)
    cos_sims_arr = np.array(cos_sims, dtype=np.float64)
    future_rets_arr = np.array(future_rets, dtype=np.float64)
    match_end_arr = np.array(match_end_indices, dtype=np.int64)

    # V3.0-FIX-2: sigma = sigma_fast（基于全量快速距离）
    sigma = sigma_fast if sigma_fast > 1e-12 else 1.0
    sim_dtw = np.exp(-dtw_dists_arr / sigma)

    if len(sim_dtw) < 3:
        return None

    # ── 综合得分：0.5*DTW + 0.5*cosine（min-max 归一化后）──
    min_dtw_val, max_dtw_val = np.min(sim_dtw), np.max(sim_dtw)
    # V3.0-FIX-5: 余弦归一化使用全量边界
    min_cos, max_cos = global_min_cos, global_max_cos
    range_dtw = max_dtw_val - min_dtw_val if max_dtw_val - min_dtw_val > 1e-12 else 1.0
    range_cos = max_cos - min_cos if max_cos - min_cos > 1e-12 else 1.0
    norm_dtw = (sim_dtw - min_dtw_val) / range_dtw
    norm_cos = (cos_sims_arr - min_cos) / range_cos
    combined_scores = 0.5 * norm_dtw + 0.5 * norm_cos

    sorted_idx = np.argsort(combined_scores)[::-1]
    top_k = min(k, len(sorted_idx))
    top_idx = sorted_idx[:top_k]

    top_scores = combined_scores[top_idx]
    top_future_rets = future_rets_arr[top_idx]
    top_end_indices = match_end_arr[top_idx]

    # 过滤 NaN 未来收益
    nan_mask = ~np.isnan(top_future_rets)
    if np.sum(nan_mask) < 2:
        return None
    top_scores = top_scores[nan_mask]
    top_future_rets = top_future_rets[nan_mask]
    top_end_indices = top_end_indices[nan_mask]
    top_k_actual = len(top_scores)

    if top_k_actual < 2:
        return None

    # ── 提取 15 维特征 ──
    return compute_pattern_features(
        top_scores, top_future_rets, top_end_indices,
        top_k_actual=top_k_actual, T_back=T_back,
    )


def compute_pattern_features(
    top_scores: np.ndarray,
    top_future_rets: np.ndarray,
    top_end_indices: np.ndarray,
    top_k_actual: Optional[int] = None,
    T_back: int = _DEFAULT_T_BACK,
) -> Dict[str, float]:
    """
    从 DTW 精排后的 Top-K 匹配结果中提取 15 维形态特征。

    算法逻辑: 与 V3.3.py 第 579-627 行完全一致。

    Args:
        top_scores: 综合得分, shape (K,)
        top_future_rets: 对应的未来收益, shape (K,)
        top_end_indices: 匹配片段的结束索引, shape (K,)
        top_k_actual: 实际有效匹配数（默认使用 len(top_scores)）
        T_back: 历史回溯范围（用于 F13 归一化）

    Returns:
        15维特征字典
    """
    if len(top_scores) == 0 or len(top_scores) != len(top_future_rets) or len(top_scores) != len(top_end_indices):
        raise ValueError("top_scores, top_future_rets, top_end_indices must be non-empty and equal length")
    if T_back <= 0:
        raise ValueError(f"T_back must be > 0, got {T_back}")
    if top_k_actual is None:
        top_k_actual = len(top_scores)
    if top_k_actual < 1 or top_k_actual > len(top_scores):
        raise ValueError(f"top_k_actual={top_k_actual} must satisfy 1 <= top_k_actual <= {len(top_scores)}")

    # F1-F5: 相似度特征
    top1_sim = float(top_scores[0])
    n_for_avg = min(5, top_k_actual)
    top5_avg_sim = float(np.mean(top_scores[:n_for_avg]))
    sim_decay = top1_sim - top5_avg_sim
    sim_variance = float(np.var(top_scores)) if top_k_actual > 1 else 0.0
    match_distance_ratio = sim_decay / top1_sim if top1_sim > 1e-12 else 0.0

    # F6-F11: 匹配片段后续表现特征
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

    # F12-F15: 匹配质量特征
    match_time_span = (
        float(np.max(top_end_indices) - np.min(top_end_indices))
        if top_k_actual > 1
        else 0.0
    )
    match_time_span_ratio = match_time_span / T_back

    # F14: 聚类比率 — 60日内最大匹配数 / K
    top_end_sorted = np.sort(top_end_indices)
    max_in_window = 0
    for i in range(len(top_end_sorted)):
        j = np.searchsorted(top_end_sorted, top_end_sorted[i] + 60, side="right")
        count = j - i
        if count > max_in_window:
            max_in_window = count
    match_cluster_ratio = max_in_window / top_k_actual if top_k_actual > 0 else 0.0

    # F15: 高于 0.8 阈值的匹配数
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
        "n_matches_above_thresh": n_matches_above_thresh,
    }


def extract_morph_features(
    prices: np.ndarray,
    T_idx: int,
    **kwargs,
) -> Optional[Dict[str, float]]:
    """
    便捷接口：从价格序列一步提取15维形态特征。
    等价于 pattern_match_single(prices, T_idx, **kwargs)。

    提供此接口是为了让调用方无需了解 pattern_match_single 内部细节。
    """
    return pattern_match_single(prices, T_idx, **kwargs)
