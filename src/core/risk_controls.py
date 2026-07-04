# -*- coding: utf-8 -*-
"""
风控规则模块 — 纯计算部分
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 1940-2104
===========================
从 形态匹配ETF组合策略_V3.3.py 的 apply_risk_controls 提取。

模块内容:
  - compute_rolling_vol_percentile: 滚动波动率分位数
  - compute_ma_trend_signal:        MA60 趋势过滤信号
  - apply_position_cap:            仓位上限约束

原始来源: V3.3.py 行 1940-2104 (apply_risk_controls)

这些是纯计算函数，接受数值输入返回数值输出。
策略层的 context/掘金 SDK 依赖不在此模块中。
"""

import numpy as np
from typing import Dict, Optional, Tuple


def compute_rolling_vol_percentile(
    close_prices: np.ndarray,
    window: int = 20,
    lookback: int = 252,
    percentile: float = 90.0,
    absolute_cap: Optional[float] = None,
) -> Dict[str, float]:
    """
    计算滚动波动率分位数——用于波动率减仓规则。

    Args:
        close_prices: 收盘价序列
        window: 滚动波动率窗口（交易日）
        lookback: 分位数计算回溯窗口
        percentile: 分位数阈值
        absolute_cap: 绝对上限（如 0.022），若提供则取 min(分位数, cap)

    Returns:
        {
            "current_vol": 当前波动率,
            "percentile_N": 分位数值,
            "threshold": 实际使用的阈值,
            "triggered": 是否触发,
        }
    """
    if len(close_prices) < lookback + window:
        return {
            "current_vol": 0.0, "percentile_N": 0.0,
            "threshold": 0.0, "triggered": False,
        }

    rets = np.diff(np.log(np.maximum(close_prices, 1e-12)))
    rets = rets[~np.isnan(rets)]

    if len(rets) < lookback + window:
        return {
            "current_vol": 0.0, "percentile_N": 0.0,
            "threshold": 0.0, "triggered": False,
        }

    # 滚动标准差
    rolling_std = np.array([
        np.std(rets[i: i + window])
        for i in range(len(rets) - window + 1)
    ])

    available = min(len(rolling_std), lookback)
    current_vol = float(rolling_std[-1])
    pct_val = float(np.percentile(rolling_std[-available:], percentile))
    threshold = min(pct_val, absolute_cap) if absolute_cap is not None else pct_val
    triggered = current_vol > threshold

    return {
        "current_vol": current_vol,
        "percentile_N": pct_val,
        "threshold": threshold,
        "triggered": triggered,
    }


def compute_ma_trend_signal(
    close_prices: np.ndarray,
    ma_period: int = 60,
    downside_confirm_days: int = 5,
    upside_confirm_days: int = 3,
) -> Tuple[bool, float, float]:
    """
    MA趋势过滤信号。

    Args:
        close_prices: 收盘价序列（至少 ma_period + max(confirm_days) 个元素）
        ma_period: 均线周期
        downside_confirm_days: 连续N日在MA下方确认下行
        upside_confirm_days: 连续N日在MA上方确认恢复

    Returns:
        (trend_down: bool, current_price: float, ma_value: float)
    """
    min_len = ma_period + max(downside_confirm_days, upside_confirm_days)
    if len(close_prices) < min_len:
        return False, float(close_prices[-1]), float(np.mean(close_prices))

    ma_value = float(np.mean(close_prices[-ma_period:]))
    current_price = float(close_prices[-1])

    # 下行确认
    below = close_prices[-downside_confirm_days:] < ma_value
    if np.all(below):
        return True, current_price, ma_value

    # 上行恢复
    above = close_prices[-upside_confirm_days:] > ma_value
    if np.all(above):
        return False, current_price, ma_value

    return False, current_price, ma_value


def apply_position_cap(
    weights: Dict[str, float],
    max_position: float,
) -> Dict[str, float]:
    """
    按仓位上限等比缩放权重。

    Args:
        weights: {symbol: weight}
        max_position: 总仓位上限 ∈ [0, 1]

    Returns:
        缩放后的权重字典。
    """
    if not weights:
        return {}

    total = sum(weights.values())
    if total <= max_position:
        return weights

    scale = max_position / total
    return {s: w * scale for s, w in weights.items()}


def apply_min_holdings(
    weights: Dict[str, float],
    predictions: Dict[str, float],
    min_count: int = 2,
    negligible: float = 0.005,
) -> Dict[str, float]:
    """
    保障最低持仓数量——按预测概率保留 top-N。

    Args:
        weights: {symbol: weight}
        predictions: {symbol: P_final}
        min_count: 最低持仓数
        negligible: 可忽略权重阈值

    Returns:
        调整后的权重字典。
    """
    if not weights:
        return weights

    active = {s: w for s, w in weights.items() if w > negligible}
    if len(active) >= min_count:
        return weights

    # 按概率排序保留 top-N
    sorted_by_prob = sorted(
        weights.items(),
        key=lambda x: predictions.get(x[0], 0.0),
        reverse=True,
    )
    keep_count = min(min_count, len(sorted_by_prob))
    return dict(sorted_by_prob[:keep_count])
