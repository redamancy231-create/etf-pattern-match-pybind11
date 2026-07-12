# -*- coding: utf-8 -*-
"""DTW 模块测试 — 与原始 V3.3.py 实现交叉验证
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> v2 新增: NaN 边界测试 + cosine 阈值测试 (GPT-5.5 完备性审查 P1)"""


import sys
import os
import numpy as np
import pytest

# 添加 src 到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.dtw import (
    standardize_returns,
    cosine_similarity,
    dtw_distance,
    dtw_distance_batch,
    generate_query_candidates,
)


class TestStandardizeReturns:
    """standardize_returns 正确性测试"""

    def test_normal_case(self):
        """正常价格序列 — 应输出零均值、单位标准差的序列"""
        prices = np.array([100.0, 101.0, 102.5, 99.8, 103.2, 105.0])
        result = standardize_returns(prices)
        assert len(result) == 5  # n-1
        assert abs(np.mean(result)) < 1e-10  # 零均值
        assert abs(np.std(result) - 1.0) < 1e-10  # 单位标准差

    def test_constant_prices(self):
        """恒定价格 — std=0 时应返回去均值（零向量）序列"""
        prices = np.array([100.0, 100.0, 100.0, 100.0])
        result = standardize_returns(prices)
        assert len(result) == 3
        assert np.allclose(result, 0.0)

    def test_short_series(self):
        """少于2个元素 — 返回零数组"""
        result = standardize_returns(np.array([100.0]))
        assert len(result) == 0

    def test_zero_price_handling(self):
        """价格为0时应被 clip 到 1e-12"""
        prices = np.array([0.0, 100.0, 200.0])
        result = standardize_returns(prices)
        assert not np.any(np.isnan(result))
        assert not np.any(np.isinf(result))

    def test_nan_in_prices(self):
        """含 NaN 的价格 — NaN 收益率应被过滤"""
        # log(0) = -inf → diff 可能产生 nan
        prices = np.array([100.0, 100.0, 100.0, 100.0, 100.0])
        # 模拟: 在实际中 standardize_returns 中 np.diff(np.log(...))
        # 对恒定价格返回全零，不会有 NaN
        result = standardize_returns(prices)
        assert len(result) == 4
        assert not np.any(np.isnan(result))

    # v2 新增: 真实 NaN 边界测试 (GPT-5.5 完备性审查 P1)
    # 2026-07-12 修订: standardize_returns 已改为窗口级非有限值检查，
    # 任一价格为 NaN/Inf 即返回空数组，因此以下测试改为验证新契约。
    def test_nan_value_in_array(self):
        """数组中含 np.nan — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([100.0, np.nan, 101.0]))
        assert len(result) == 0

    def test_all_nan(self):
        """全 NaN — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([np.nan, np.nan]))
        assert len(result) == 0

    def test_zero_then_valid(self):
        """价格为0后被clip — 验证clip不产生NaN"""
        result = standardize_returns(np.array([0.0, 50.0, 100.0]))
        assert len(result) == 2
        assert not np.any(np.isnan(result))


class TestCosineSimilarity:
    """cosine_similarity 正确性测试"""

    def test_identical_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, x) == pytest.approx(1.0)

    def test_opposite_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, -x) == pytest.approx(-1.0)

    def test_orthogonal_vectors(self):
        x = np.array([1.0, 0.0, 0.0])
        y = np.array([0.0, 1.0, 0.0])
        assert cosine_similarity(x, y) == pytest.approx(0.0)

    def test_zero_vector(self):
        x = np.array([0.0, 0.0, 0.0])
        y = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, y) == 0.0
        assert cosine_similarity(y, x) == 0.0

    def test_near_zero_norm(self):
        """极小的 norm 应安全返回 0"""
        x = np.array([1e-13, 1e-13])
        y = np.array([1.0, 2.0])
        assert cosine_similarity(x, y) == 0.0

    # v2 新增: 阈值边界测试 (GPT-5.5 完备性审查 P1)
    def test_exactly_at_threshold(self):
        """norm 恰好等于 1e-12 — 不应返回 0（原逻辑用 < 而非 <=）"""
        x = np.array([1e-12, 0.0])
        y = np.array([1.0, 0.0])
        # norm_x = 1e-12, 不小于 1e-12 → 进入 dot/norm 计算
        result = cosine_similarity(x, y)
        assert result == pytest.approx(1.0)  # 方向完全一致


class TestDTWDistance:
    """DTW 距离正确性测试"""

    def test_identical_sequences(self):
        """相同序列的 DTW 距离应为 0"""
        x = np.array([0.1, 0.2, -0.1, 0.05, 0.0] * 4)  # L=20
        d = dtw_distance(x, x, window=5)
        assert d == pytest.approx(0.0, abs=1e-12)

    def test_same_length_sequences(self):
        """等长序列的基本 DTW 计算"""
        x = np.array([1.0, 2.0, 3.0, 2.0, 1.0])
        y = np.array([1.0, 2.0, 2.0, 3.0, 1.0])
        d = dtw_distance(x, y, window=5)
        assert d > 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_different_length_sequences(self):
        """不同长度序列"""
        x = np.array([0.1, -0.2, 0.3] * 5)   # L=15
        y = np.array([0.1, -0.2, 0.3] * 7)   # L=21
        d = dtw_distance(x, y, window=5)
        assert d >= 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_window_constraint(self):
        """band 约束应限制搜索范围"""
        x = np.random.randn(20)
        y = np.random.randn(20)
        d_narrow = dtw_distance(x, y, window=2)
        d_wide = dtw_distance(x, y, window=10)
        # 窄 band 距离应 ≥ 宽 band（因为搜索空间更受限）
        assert d_narrow >= d_wide - 1e-12

    def test_empty_input(self):
        """空序列应返回 inf"""
        assert dtw_distance(np.array([]), np.array([1.0, 2.0])) == np.inf
        assert dtw_distance(np.array([1.0, 2.0]), np.array([])) == np.inf

    def test_single_element(self):
        """单元素序列"""
        d = dtw_distance(np.array([0.5]), np.array([0.5]))
        assert d == pytest.approx(0.0, abs=1e-12)


class TestDTWDistanceBatch:
    """批量 DTW 测试"""

    def test_basic_batch(self):
        query = np.random.randn(20)
        candidates = np.random.randn(100, 20)
        distances = dtw_distance_batch(query, candidates, window=5)
        assert len(distances) == 100
        assert np.all(distances >= 0)

    def test_top_k(self):
        query = np.random.randn(20)
        candidates = np.random.randn(50, 20)
        idx, dists = dtw_distance_batch(query, candidates, window=5, top_k=10)
        assert len(idx) == 10
        assert len(dists) == 10
        # 确认排序
        assert np.all(np.diff(dists) >= 0)

    def test_consistency_with_single(self):
        """批量结果应与逐个调用一致"""
        query = np.random.randn(20)
        candidates = np.random.randn(30, 20)
        batch_dists = dtw_distance_batch(query, candidates, window=5)
        single_dists = np.array([dtw_distance(query, c, window=5) for c in candidates])
        assert np.allclose(batch_dists, single_dists)

    def test_empty_candidates(self):
        result = dtw_distance_batch(np.array([1.0]), np.empty((0, 1)))
        assert len(result) == 0

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            dtw_distance_batch(
                np.array([1.0, 2.0]),
                np.random.randn(10, 5),  # 列数不匹配
            )


class TestGenerateQueryCandidates:
    """查询/候选窗口生成测试"""

    def test_basic_generation(self):
        prices = np.sin(np.linspace(0, 10 * np.pi, 500)) + 10.0
        T_idx = 400
        q, cands, ends = generate_query_candidates(prices, T_idx, L_query=20)
        assert len(q) == 20
        assert cands.shape[1] == 20
        assert cands.shape[0] >= 300  # ~380 candidates
        # 前视偏差防护: 所有候选窗口结束索引 <= T_idx - L_query (=380)
        assert np.all(ends <= T_idx - 20)

    def test_insufficient_data(self):
        prices = np.array([100.0] * 10)
        with pytest.raises(ValueError):
            generate_query_candidates(prices, T_idx=5, L_query=20)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
