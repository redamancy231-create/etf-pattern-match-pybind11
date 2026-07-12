# -*- coding: utf-8 -*-
"""
市场环境特征模块 — F16-F21
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 882-1001
===========================
从 形态匹配ETF组合策略_V3.3.py 提取，纯计算版本（无掘金依赖）。

模块内容:
  - compute_market_volatility:  F16, 近20日波动率
  - compute_size_relative_strength: F17, 大小盘相对强度
  - compute_volume_anomaly:     F20, 成交量异常
  - compute_vol_change:         F21, 波动率变化

原始来源:
  V3.3.py 行 882-1001 (compute_market_features, _compute_market_features_historical)
"""

import numpy as np


def compute_market_volatility(close_prices: np.ndarray, window: int = 20) -> float:
    """
    F16: 近 window 日对数收益率的标准差。

    Args:
        close_prices: 收盘价序列, shape (n_days,), 至少 window+1 个元素
        window: 滚动窗口（默认20日）

    Returns:
        日度波动率；数据不足时返回 0.0。

    算法逻辑: 与 V3.3.py 第 886-892 行一致.
    """
    close_prices = np.asarray(close_prices, dtype=np.float64)
    if window <= 0:
        raise ValueError(f"window must be > 0, got {window}")
    if len(close_prices) < window + 1:
        return 0.0
    prices_slice = close_prices[-(window + 1):]
    if not np.all(np.isfinite(prices_slice)):
        return 0.0
    rets = np.diff(np.log(np.maximum(prices_slice, 1e-12)))
    rets = rets[~np.isnan(rets)]
    if len(rets) < 2:
        return 0.0
    return float(np.std(rets))


def compute_size_relative_strength(
    hs300_close: np.ndarray,
    zz500_close: np.ndarray,
    window: int = 20,
) -> float:
    """
    F17: 大小盘相对强度 = zz500_ret / abs(hs300_ret) - 1

    Args:
        hs300_close: 沪深300收盘价, shape (n,)
        zz500_close: 中证500收盘价, shape (n,)
        window: 收益计算窗口

    Returns:
        相对强度；数据不足或含非有限值时返回 0.0。

    算法逻辑: 与 V3.3.py 第 894-902 行一致.
    """
    hs300_close = np.asarray(hs300_close, dtype=np.float64)
    zz500_close = np.asarray(zz500_close, dtype=np.float64)
    if window <= 0:
        raise ValueError(f"window must be > 0, got {window}")
    if len(hs300_close) < window + 1 or len(zz500_close) < window + 1:
        return 0.0
    if not (np.isfinite(hs300_close[-(window + 1)]) and np.isfinite(hs300_close[-1])
            and np.isfinite(zz500_close[-(window + 1)]) and np.isfinite(zz500_close[-1])):
        return 0.0

    hs300_ret = float(hs300_close[-1] / hs300_close[-(window + 1)] - 1)
    zz500_ret = float(zz500_close[-1] / zz500_close[-(window + 1)] - 1)
    denom = abs(hs300_ret) + 1e-12
    return float(zz500_ret / denom - 1) if denom > 1e-12 else 0.0


def compute_volume_anomaly(
    amounts: np.ndarray,
    short_window: int = 5,
    long_window: int = 20,
) -> float:
    """
    F20: 成交量异常 = mean(近short日) / mean(近long日) - 1

    Args:
        amounts: 成交额序列, shape (n,)
        short_window: 短期窗口（默认5日）
        long_window: 长期窗口（默认20日）

    Returns:
        异常比率；数据不足或含非有限值时返回 0.0。

    算法逻辑: 与 V3.3.py 第 915-918 行一致.
    """
    amounts = np.asarray(amounts, dtype=np.float64)
    if short_window <= 0 or long_window <= 0:
        raise ValueError(f"windows must be > 0, got short={short_window}, long={long_window}")
    if short_window > long_window:
        raise ValueError(f"short_window ({short_window}) must be <= long_window ({long_window})")
    if len(amounts) < long_window:
        return 0.0
    short_slice = amounts[-short_window:]
    long_slice = amounts[-long_window:]
    if not (np.all(np.isfinite(short_slice)) and np.all(np.isfinite(long_slice))):
        return 0.0
    short_avg = float(np.mean(amounts[-short_window:]))
    long_avg = float(np.mean(amounts[-long_window:]))
    denom = long_avg + 1e-12
    return float(short_avg / denom - 1) if denom > 1e-12 else 0.0


def compute_vol_change(
    close_prices: np.ndarray,
    short_window: int = 5,
    long_window: int = 20,
) -> float:
    """
    F21: 波动率变化 = std(近short日收益) / std(近long日收益) - 1

    Args:
        close_prices: 收盘价序列, shape (n,)
        short_window: 短期窗口（默认5日）
        long_window: 长期窗口（默认20日）

    Returns:
        波动率变化比率；数据不足或含非有限值时返回 0.0。

    算法逻辑: 与 V3.3.py 第 922-928 行一致.
    """
    close_prices = np.asarray(close_prices, dtype=np.float64)
    if short_window <= 0 or long_window <= 0:
        raise ValueError(f"windows must be > 0, got short={short_window}, long={long_window}")
    if short_window > long_window:
        raise ValueError(f"short_window ({short_window}) must be <= long_window ({long_window})")
    if len(close_prices) < long_window + 1:
        return 0.0
    if not np.all(np.isfinite(close_prices[-(long_window + 1):])):
        return 0.0

    rets = np.diff(np.log(np.maximum(close_prices, 1e-12)))
    rets = rets[~np.isnan(rets)]
    if len(rets) < long_window:
        return 0.0

    vol_short = float(np.std(rets[-short_window:]))
    vol_long = float(np.std(rets[-long_window:]))
    denom = vol_long + 1e-12
    return float(vol_short / denom - 1) if denom > 1e-12 else 0.0
