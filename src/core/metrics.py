# -*- coding: utf-8 -*-
"""
绩效指标计算模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 3544-3678
=================
从 形态匹配ETF组合策略_V3.3.py 的 on_backtest_finished 提取。

模块内容:
  - compute_sortino_ratio:  Sortino 比率（下行波动率调整）
  - compute_calmar_ratio:   Calmar 比率（年化收益/最大回撤）
  - compute_max_drawdown:   最大回撤
  - compute_tracking_error: 跟踪误差
  - compute_information_ratio: 信息比率
  - compute_ic_stats:        IC 统计（均值/中位数/IR/区间占比）
  - compute_annual_stats:    年化统计（收益/波动/夏普）

原始来源: V3.3.py 行 3544-3616 (on_backtest_finished 自定义指标段)
"""

import numpy as np
from typing import Dict


def compute_max_drawdown(cumulative_returns: np.ndarray) -> float:
    """
    计算最大回撤。

    Args:
        cumulative_returns: 累计收益序列 (1 + rets 的累积积)

    Returns:
        最大回撤（负值），如 -0.15 表示 15% 回撤。
    """
    running_max = np.maximum.accumulate(cumulative_returns)
    drawdown = (cumulative_returns - running_max) / running_max
    return float(np.min(drawdown))


def compute_annual_stats(daily_returns: np.ndarray, trading_days: int = 252) -> Dict[str, float]:
    """
    从日收益率计算年化统计量。

    Args:
        daily_returns: 日收益率序列
        trading_days: 年交易日数

    Returns:
        {"annual_return": float, "annual_vol": float, "sharpe": float}
    """
    if len(daily_returns) < 2:
        return {"annual_return": 0.0, "annual_vol": 0.0, "sharpe": 0.0}

    mean_ret = float(np.mean(daily_returns))
    std_ret = float(np.std(daily_returns))
    annual_ret = mean_ret * trading_days
    annual_vol = std_ret * np.sqrt(trading_days)
    sharpe = annual_ret / annual_vol if annual_vol > 1e-12 else 0.0

    return {
        "annual_return": annual_ret,
        "annual_vol": annual_vol,
        "sharpe": sharpe,
    }


def compute_sortino_ratio(
    daily_returns: np.ndarray,
    trading_days: int = 252,
) -> float:
    """
    Sortino 比率 = 年化收益 / 下行年化波动率。

    Args:
        daily_returns: 日收益率序列
        trading_days: 年交易日数

    Returns:
        Sortino 比率；无下行波动时返回 inf。
    """
    if len(daily_returns) < 2:
        return 0.0

    annual_ret = float(np.mean(daily_returns)) * trading_days
    downside = daily_returns[daily_returns < 0]
    if len(downside) == 0:
        return float("inf")

    downside_vol = float(np.std(downside)) * np.sqrt(trading_days)
    return annual_ret / downside_vol if downside_vol > 1e-12 else 0.0


def compute_calmar_ratio(
    daily_returns: np.ndarray,
    trading_days: int = 252,
) -> float:
    """
    Calmar 比率 = 年化收益 / |最大回撤|。

    Args:
        daily_returns: 日收益率序列
        trading_days: 年交易日数

    Returns:
        Calmar 比率。
    """
    if len(daily_returns) < 2:
        return 0.0

    annual_ret = float(np.mean(daily_returns)) * trading_days
    cum_ret = np.cumprod(1.0 + daily_returns)
    max_dd = compute_max_drawdown(cum_ret)
    return annual_ret / abs(max_dd) if abs(max_dd) > 1e-12 else 0.0


def compute_tracking_error(
    strategy_returns: np.ndarray,
    benchmark_returns: np.ndarray,
    trading_days: int = 252,
) -> float:
    """
    跟踪误差 = std(超额日收益) * sqrt(交易日)。

    Args:
        strategy_returns: 策略日收益率
        benchmark_returns: 基准日收益率
        trading_days: 年交易日数

    Returns:
        年化跟踪误差。
    """
    min_len = min(len(strategy_returns), len(benchmark_returns))
    if min_len < 2:
        return 0.0

    excess = strategy_returns[-min_len:] - benchmark_returns[-min_len:]
    return float(np.std(excess)) * np.sqrt(trading_days)


def compute_information_ratio(
    strategy_returns: np.ndarray,
    benchmark_returns: np.ndarray,
    trading_days: int = 252,
) -> float:
    """
    信息比率 = 年化超额收益 / 年化跟踪误差。

    Args:
        strategy_returns: 策略日收益率
        benchmark_returns: 基准日收益率
        trading_days: 年交易日数

    Returns:
        信息比率。
    """
    min_len = min(len(strategy_returns), len(benchmark_returns))
    if min_len < 2:
        return 0.0

    strat_ret = float(np.mean(strategy_returns[-min_len:])) * trading_days
    bench_ret = float(np.mean(benchmark_returns[-min_len:])) * trading_days
    excess = strat_ret - bench_ret
    te = compute_tracking_error(strategy_returns, benchmark_returns, trading_days)
    return excess / te if te > 1e-12 else 0.0


def compute_weekly_win_rate(
    daily_returns: np.ndarray,
    dates: np.ndarray,
) -> float:
    """
    按 ISO 日历周对齐计算周度胜率。

    Args:
        daily_returns: 日收益率序列
        dates: 对应的日期序列（datetime64 或兼容类型）

    Returns:
        周度胜率 ∈ [0, 1]；数据不足时返回 0.0。
    """
    try:
        import pandas as pd
    except ImportError:
        # Fallback: 简单每5日分组
        n_weeks = len(daily_returns) // 5
        if n_weeks == 0:
            return 0.0
        weekly_sums = np.array([
            np.sum(daily_returns[i * 5: (i + 1) * 5])
            for i in range(n_weeks)
        ])
        return float(np.mean(weekly_sums > 0))

    dates_pd = pd.to_datetime(dates)
    iso = dates_pd.isocalendar()
    df = pd.DataFrame({
        "iso_year": iso.year.values,
        "iso_week": iso.week.values,
        "ret": daily_returns,
    })
    weekly = df.groupby(["iso_year", "iso_week"])["ret"].sum()
    if len(weekly) == 0:
        return 0.0
    return float(np.mean(weekly.values > 0))


def compute_ic_stats(ic_values: np.ndarray, threshold: float = 0.02) -> Dict[str, float]:
    """
    计算 IC 全历史统计。

    Args:
        ic_values: RankIC 序列
        threshold: IC 阈值（用于空仓/反转判断）

    Returns:
        {
            "mean": float, "median": float, "std": float,
            "ic_gt_positive": float,  # IC > +threshold 占比
            "ic_lt_negative": float,  # IC < -threshold 占比
            "ic_within": float,       # |IC| < threshold 占比
            "ic_positive_ratio": float,  # IC > 0 占比
            "icir": float,            # IC 信息比率
            "n_obs": int,
        }
    """
    if len(ic_values) < 2:
        return {
            "mean": 0.0, "median": 0.0, "std": 0.0,
            "ic_gt_positive": 0.0, "ic_lt_negative": 0.0,
            "ic_within": 0.0, "ic_positive_ratio": 0.0,
            "icir": 0.0, "n_obs": len(ic_values),
        }

    std_ic = float(np.std(ic_values))
    return {
        "mean": float(np.mean(ic_values)),
        "median": float(np.median(ic_values)),
        "std": std_ic,
        "ic_gt_positive": float(np.mean(ic_values > threshold)),
        "ic_lt_negative": float(np.mean(ic_values < -threshold)),
        "ic_within": float(np.mean(np.abs(ic_values) < threshold)),
        "ic_positive_ratio": float(np.mean(ic_values > 0)),
        "icir": float(np.mean(ic_values)) / std_ic if std_ic > 1e-12 else 0.0,
        "n_obs": len(ic_values),
    }
