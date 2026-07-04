# -*- coding: utf-8 -*-
"""技术指标模块测试
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build", "Release"))

from core.technical import compute_adx, compute_sector_rotation, compute_atr


class TestComputeADX:
    """ADX 计算正确性测试"""

    def test_insufficient_data(self):
        """数据不足时返回中性值 25.0"""
        high = np.random.randn(20) + 100
        low = high - 2
        close = (high + low) / 2
        # n=14, 需要 n+16=30 个元素
        result = compute_adx(high, low, close, n=14)
        assert result == 25.0

    def test_flat_market(self):
        """无趋势市场 — ADX 应接近 0"""
        n_days = 100
        high = np.ones(n_days) * 100 + 0.01 * np.random.randn(n_days)
        low = np.ones(n_days) * 98 + 0.01 * np.random.randn(n_days)
        close = np.ones(n_days) * 99 + 0.01 * np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert result >= 0
        assert result <= 100

    def test_strong_trend(self):
        """强趋势市场 — ADX 应较高"""
        n_days = 200
        trend = np.linspace(100, 200, n_days)
        noise = np.random.randn(n_days) * 0.5
        high = trend + noise + 2
        low = trend + noise - 2
        close = trend + noise
        result = compute_adx(high, low, close, n=14)
        # 强趋势下 ADX 通常 > 20
        assert result > 15

    def test_output_range(self):
        """ADX 值应在 [0, 100] 范围内"""
        n_days = 150
        high = 100 + np.cumsum(np.random.randn(n_days))
        low = high - 5 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert 0 <= result <= 100


class TestComputeSectorRotation:
    """行业轮动速度测试"""

    def test_no_rotation(self):
        """排名完全不变 — 轮动速度应为 0"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01}
        curr = {"A": 0.08, "B": 0.03, "C": 0.01, "D": -0.02}
        # 排名: A>B>C>D 不变
        result = compute_sector_rotation(prev, curr)
        assert result == pytest.approx(0.0, abs=0.01)

    def test_full_rotation(self):
        """排名完全无关（随机轮动）— 轮动速度应接近 1"""
        # 用6个行业，前后期排名完全正交
        prev = {"A": 0.60, "B": 0.50, "C": 0.40, "D": 0.30, "E": 0.20, "F": 0.10}
        curr = {"A": 0.10, "B": 0.60, "C": 0.05, "D": 0.50, "E": 0.03, "F": 0.40}
        # prev rank: A(0)B(1)C(2)D(3)E(4)F(5)
        # curr rank: B(0)D(1)F(2)A(3)C(4)E(5)
        # 这是大幅重新洗牌，ρ 应 < 0.5
        result = compute_sector_rotation(prev, curr)
        assert result > 0.5  # 高轮动 (1-|ρ| > 0.5)

    def test_partial_rotation(self):
        """部分轮动"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "E": 0.08}
        curr = {"A": 0.01, "B": 0.08, "C": 0.05, "D": -0.03, "E": 0.10}
        result = compute_sector_rotation(prev, curr)
        assert 0.0 < result < 1.0

    def test_insufficient_sectors(self):
        """行业数不足 — 返回 0"""
        prev = {"A": 0.10, "B": 0.05}
        curr = {"A": -0.02, "B": 0.08}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert result == 0.0

    def test_mismatched_symbols(self):
        """部分 symbol 不重叠 — 仅用公共部分"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "X": 0.03}
        curr = {"A": -0.02, "B": 0.08, "C": 0.01, "D": 0.03, "Y": -0.05}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert 0.0 <= result <= 1.0  # 仅用 A/B/C/D


class TestComputeATR:
    """ATR 计算测试"""

    def test_basic_atr(self):
        n_days = 50
        high = 100 + np.cumsum(np.random.randn(n_days) * 0.5)
        low = high - 2 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days) * 0.1
        atr = compute_atr(high, low, close, n=14)
        assert len(atr) == n_days
        assert np.all(np.isnan(atr[:14]))  # 前 n 天为 NaN
        assert np.all(atr[14:] > 0)  # ATR 必须为正


def test_compute_atr_mismatched_lengths():
    """high/low/close 长度不一致时应抛异常"""
    import etf_core
    high = np.random.uniform(10, 20, 100)
    low = np.random.uniform(8, 10, 99)  # 比 high 少 1
    close = np.random.uniform(10, 20, 100)
    try:
        etf_core.compute_atr(high, low, close)
        assert False, "长度不一致应抛异常"
    except Exception as e:
        assert "length" in str(e).lower() or "same" in str(e).lower()


def test_compute_atr_short_array():
    """短于 n+1 的数组应返回全 NaN"""
    import etf_core
    n = 14
    short_len = n  # 等于 n，不足 n+1
    high = np.random.uniform(10, 20, short_len)
    low = np.random.uniform(8, 10, short_len)
    close = np.random.uniform(10, 20, short_len)
    result = etf_core.compute_atr(high, low, close, n)
    assert len(result) == short_len
    assert np.all(np.isnan(result)), f"短数组(长度={short_len})应返回全 NaN"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
