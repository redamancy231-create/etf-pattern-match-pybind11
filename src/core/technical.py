# -*- coding: utf-8 -*-
"""
技术指标计算模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 757-795, 801-836, 1003-1032
=================
从 形态匹配ETF组合策略_V3.3.py 提取，零掘金依赖。

模块内容:
  - compute_adx:          ADX (Average Directional Index) — Wilder's smoothing
  - compute_sector_rotation: 行业轮动速度 (Spearman rank correlation)

原始来源:
  V3.3.py 行 757-795 (_compute_adx_from_df)
  V3.3.py 行 801-836 (_compute_sector_rotation)
  V3.3.py 行 1003-1032 (_compute_sector_rotation_historical)

算法逻辑零改动。
"""

import numpy as np
from typing import Dict


def compute_adx(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    n: int = 14,
) -> float:
    """
    从 OHLC 数组计算 ADX (Average Directional Index)。

    Args:
        high: 最高价序列, shape (n_days,)
        low:  最低价序列, shape (n_days,)
        close: 收盘价序列, shape (n_days,)
        n: 平滑周期 (默认 14)

    Returns:
        ADX 值 ∈ [0, 100]；数据不足时返回 25.0（中性值）。

    算法逻辑: 与 V3.3.py 第 757-795 行完全一致。
    """
    if len(high) < n + 16 or len(low) < n + 16 or len(close) < n + 16:
        return 25.0

    # True Range
    tr = np.maximum(
        high[1:] - low[1:],
        np.maximum(np.abs(high[1:] - close[:-1]), np.abs(low[1:] - close[:-1])),
    )

    # Directional Movement
    up = high[1:] - high[:-1]
    down = low[:-1] - low[1:]
    plus_dm = np.where((up > down) & (up > 0), up, 0)
    minus_dm = np.where((down > up) & (down > 0), down, 0)

    # Wilder's smoothing (初始值 = 简单均值，后续指数平滑)
    atr = np.zeros_like(tr)
    atr[:n] = np.mean(tr[:n])
    for i in range(n, len(tr)):
        atr[i] = (atr[i - 1] * (n - 1) + tr[i]) / n

    smoothed_plus = np.zeros_like(tr)
    smoothed_minus = np.zeros_like(tr)
    smoothed_plus[:n] = np.mean(plus_dm[:n])
    smoothed_minus[:n] = np.mean(minus_dm[:n])
    for i in range(n, len(tr)):
        smoothed_plus[i] = (smoothed_plus[i - 1] * (n - 1) + plus_dm[i]) / n
        smoothed_minus[i] = (smoothed_minus[i - 1] * (n - 1) + minus_dm[i]) / n

    plus_di = 100 * smoothed_plus / (atr + 1e-12)
    minus_di = 100 * smoothed_minus / (atr + 1e-12)
    dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di + 1e-12)

    adx = np.zeros_like(dx)
    adx[:n] = np.mean(dx[:n])
    for i in range(n, len(dx)):
        adx[i] = (adx[i - 1] * (n - 1) + dx[i]) / n

    return float(adx[-1])


def compute_sector_rotation(
    prev_returns: Dict[str, float],
    curr_returns: Dict[str, float],
    min_sectors: int = 4,
) -> float:
    """
    计算行业轮动速度。

    基于前后两期行业收益率的排名相关性：
      轮动速度 = 1 - |Spearman ρ|
    ρ 越接近 0 → 轮动越快 → 值越大。

    Args:
        prev_returns: {symbol: prev_period_return} 前一期行业收益
        curr_returns: {symbol: curr_period_return} 当前期行业收益
        min_sectors: 最小行业数要求

    Returns:
        轮动速度 ∈ [0, 1]；数据不足时返回 0.0。

    算法逻辑: 与 V3.3.py 第 801-836, 1003-1032 行完全一致。
    """
    common = set(prev_returns.keys()) & set(curr_returns.keys())
    if len(common) < min_sectors:
        return 0.0

    prev_vals = {k: prev_returns[k] for k in common}
    curr_vals = {k: curr_returns[k] for k in common}

    prev_order = sorted(prev_vals, key=prev_vals.get)
    curr_order = sorted(curr_vals, key=curr_vals.get)

    prev_rank_map = {s: i for i, s in enumerate(prev_order)}
    curr_rank_map = {s: i for i, s in enumerate(curr_order)}

    common_set = set(prev_rank_map.keys()) & set(curr_rank_map.keys())
    if len(common_set) < min_sectors:
        return 0.0

    prev_rank_vals = [prev_rank_map[s] for s in common_set]
    curr_rank_vals = [curr_rank_map[s] for s in common_set]

    rho = np.corrcoef(prev_rank_vals, curr_rank_vals)[0, 1]
    if np.isnan(rho):
        rho = 0.0
    return float(1 - abs(rho))


def compute_atr(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    n: int = 14,
) -> np.ndarray:
    """
    计算 ATR (Average True Range)，Wilder's smoothing。

    Args:
        high/low/close: OHLC 序列
        n: 平滑周期

    Returns:
        ATR 序列, shape 与输入相同（前 n-1 天为 NaN）
    """
    # True Range
    tr = np.maximum(
        high[1:] - low[1:],
        np.maximum(
            np.abs(high[1:] - close[:-1]),
            np.abs(low[1:] - close[:-1]),
        ),
    )

    # Wilder's smoothing
    atr = np.full(len(tr) + 1, np.nan, dtype=np.float64)
    atr[n] = np.mean(tr[:n])
    for i in range(n + 1, len(tr) + 1):
        atr[i] = (atr[i - 1] * (n - 1) + tr[i - 1]) / n
    return atr
