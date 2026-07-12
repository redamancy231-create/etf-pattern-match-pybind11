# -*- coding: utf-8 -*-
"""
DTW 距离计算与序列预处理模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 339-383
===============================
从 形态匹配ETF组合策略_V3.3.py 提取，零外部依赖（仅 numpy）。

模块内容:
  - standardize_returns: 收益率序列标准化（去均值/除标准差）
  - cosine_similarity:   两向量余弦相似度
  - dtw_distance:        带 Sakoe-Chiba band 的 DTW 距离
  - dtw_distance_batch:  批量 DTW（一对多），减少 Python 调用开销

原始来源:
  形态匹配ETF组合策略_V3.3.py (archived in parent project)
  行 339-383 (DTW 模块, V3.3)

算法逻辑零改动 — 仅结构重组 + 类型标注 + 批量接口。
"""

import numpy as np
from typing import Optional, Tuple, Union


def standardize_returns(price_series: np.ndarray) -> np.ndarray:
    """
    计算标准化收益率序列: (rets - mean(rets)) / std(rets)

    Args:
        price_series: 价格序列, shape (n,)

    Returns:
        标准化收益率序列, shape (n-1,). 若任一价格为非有限值则返回空数组。

    算法逻辑: 与 V3.3.py 第 362-373 行完全一致。
    """
    if len(price_series) < 2:
        return np.array([], dtype=np.float64)

    # 窗口级检查：任一价格为非有限值 → 整个窗口无效
    if not np.all(np.isfinite(price_series)):
        return np.array([], dtype=np.float64)

    rets = np.diff(np.log(np.maximum(price_series, 1e-12)))
    std_ = np.std(rets)
    if std_ < 1e-12:
        return rets - np.mean(rets)
    return (rets - np.mean(rets)) / std_


def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """
    计算两向量的余弦相似度 ∈ [-1, 1]

    算法逻辑: 与 V3.3.py 第 376-382 行完全一致。
    """
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x < 1e-12 or norm_y < 1e-12:
        return 0.0
    return float(np.dot(x, y) / (norm_x * norm_y))


def dtw_distance(
    x: np.ndarray,
    y: np.ndarray,
    window: int = 5,
) -> float:
    """
    计算两个序列的 DTW 距离，使用 Sakoe-Chiba band 约束。

    Args:
        x: 查询序列, shape (n,)
        y: 历史序列, shape (m,)
        window: Sakoe-Chiba band 宽度 (默认 5)

    Returns:
        归一化 DTW 距离: sqrt(dtw[n,m]) / (n+m)

    算法逻辑: 与 V3.3.py 第 339-359 行完全一致。
    """
    n, m = len(x), len(y)
    band = max(window, abs(n - m))

    dtw = np.full((n + 1, m + 1), np.inf, dtype=np.float64)
    dtw[0, 0] = 0.0

    for i in range(1, n + 1):
        j_start = max(1, i - band)
        j_end = min(m + 1, i + band + 1)
        for j in range(j_start, j_end):
            cost = (float(x[i - 1]) - float(y[j - 1])) ** 2
            dtw[i, j] = cost + min(dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1])

    path_len = n + m
    return np.sqrt(dtw[n, m]) / path_len if path_len > 0 else np.inf


def dtw_distance_batch(
    query: np.ndarray,
    candidates: np.ndarray,
    window: int = 5,
    top_k: Optional[int] = None,
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """
    批量 DTW：一个 query 对多个 candidates。

    Args:
        query: 查询序列, shape (L,)
        candidates: 候选序列集, shape (N, L)
        window: Sakoe-Chiba band 宽度
        top_k: 若指定，仅返回距离最小的 top_k 个索引和距离

    Returns:
        若 top_k 为 None: distances shape (N,)
        若 top_k 指定: (indices, distances) 各 shape (top_k,)
    """
    n_candidates = len(candidates)
    if n_candidates == 0:
        return np.array([], dtype=np.float64)

    if len(query) != candidates.shape[1]:
        raise ValueError(
            f"query 长度 {len(query)} != candidates 列数 {candidates.shape[1]}"
        )

    distances = np.empty(n_candidates, dtype=np.float64)
    for i in range(n_candidates):
        distances[i] = dtw_distance(query, candidates[i], window=window)

    if top_k is not None and top_k < n_candidates:
        idx = np.argpartition(distances, top_k)[:top_k]
        idx = idx[np.argsort(distances[idx])]
        return idx, distances[idx]

    return distances


def generate_query_candidates(
    prices: np.ndarray,
    T_idx: int,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    从价格序列生成查询窗口和候选窗口集合（前视偏差防护）。

    Args:
        prices: 完整价格序列, shape (n_days,)
        T_idx: 当前时点索引
        L_query: 查询窗口长度（交易日）
        T_back: 历史回溯范围
        match_step: 匹配步长

    Returns:
        (query_prices, candidates_prices, candidate_end_indices)
    """
    if L_query <= 0:
        raise ValueError(f"L_query must be > 0, got {L_query}")
    if T_back <= 0:
        raise ValueError(f"T_back must be > 0, got {T_back}")
    if match_step <= 0:
        raise ValueError(f"match_step must be > 0, got {match_step}")
    if T_idx < 0 or T_idx >= len(prices):
        raise ValueError(f"T_idx={T_idx} must satisfy 0 <= T_idx < {len(prices)}")
    if not np.all(np.isfinite(prices)):
        raise ValueError("prices contains non-finite values")
    if T_idx < L_query:
        raise ValueError(f"T_idx={T_idx} < L_query={L_query}")

    query_prices = prices[T_idx - L_query + 1: T_idx + 1].copy()

    search_end = T_idx - L_query
    search_start = max(L_query - 1, T_idx - T_back)

    candidate_ends = list(range(search_start, search_end + 1, match_step))
    if not candidate_ends:
        raise ValueError(f"无候选窗口: T_idx={T_idx}")

    candidates_array = np.empty((len(candidate_ends), L_query), dtype=np.float64)
    valid_indices = []

    for ci, hist_end in enumerate(candidate_ends):
        hist_start = hist_end - L_query + 1
        if hist_start >= 0:
            candidates_array[ci] = prices[hist_start: hist_end + 1]
            valid_indices.append(hist_end)

    return (
        query_prices,
        candidates_array[:len(valid_indices)],
        np.array(valid_indices, dtype=np.int64),
    )
