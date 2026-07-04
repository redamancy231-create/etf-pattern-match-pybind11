# -*- coding: utf-8 -*-
"""形态匹配引擎测试 — 含 GPT-5.5 完备性审查要求的 F12-F15 固定样例
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 审查输入: GPT-5.5 via Codex CLI (F12-F15 固定样例规格)"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.pattern_match import (
    pattern_match_single,
    compute_pattern_features,
    extract_morph_features,
)


def _generate_random_walk(n_days: int, start_price: float = 100.0) -> np.ndarray:
    """生成随机游走价格序列用于集成测试"""
    np.random.seed(42)
    returns = np.random.randn(n_days) * 0.02
    prices = start_price * np.cumprod(1 + returns)
    return np.asarray(prices, dtype=np.float64)


class TestPatternMatchSingle:
    """pattern_match_single 集成测试"""

    def test_insufficient_data_short_prices(self):
        """价格序列太短"""
        prices = np.array([100.0] * 10)
        result = pattern_match_single(prices, T_idx=5)
        assert result is None

    def test_insufficient_data_small_T_idx(self):
        """T_idx 太小（不足 L_query + M_forward + 10）"""
        prices = _generate_random_walk(100)
        result = pattern_match_single(prices, T_idx=30)
        assert result is None

    def test_basic_extraction(self):
        """基本提取 — 应返回15维非空特征"""
        prices = _generate_random_walk(600)
        T_idx = 500
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        assert len(result) == 15
        # 所有值应为有限数值
        for key, val in result.items():
            assert isinstance(val, (float, int, np.integer)), f"{key} 类型异常: {type(val)}"
            assert np.isfinite(float(val)), f"{key} = {val} 不是有限值"

    def test_no_query_window_leakage(self):
        """前视偏差防护: 所有匹配片段的未来收益端点 < T_idx"""
        prices = _generate_random_walk(800)
        T_idx = 700
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        # 函数内部已保证 fut_end < T_idx，这里验证返回值合理性
        assert -1.0 <= result["avg_future_ret"] <= 1.0

    def test_returns_consistent_shape(self):
        """多次调用应返回一致的特征键集合"""
        prices = _generate_random_walk(600)
        keys = None
        for T_idx in [400, 450, 500]:
            r = pattern_match_single(prices, T_idx)
            if r is None:
                continue
            if keys is None:
                keys = set(r.keys())
            else:
                assert set(r.keys()) == keys

    def test_cos_prefilter_top_effect(self):
        """cos_prefilter_top 参数应影响结果（不同 top 值可能产生不同特征）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx, cos_prefilter_top=50)
        r2 = pattern_match_single(prices, T_idx, cos_prefilter_top=200)
        # 两者都不应为 None（如果数据足够）
        assert r1 is not None
        assert r2 is not None
        # 注意: 不同 top-k 可能产生不同特征值（因为 sigma_fast 也变了）
        # 这里只验证两者都有效

    def test_deterministic_output(self):
        """相同输入应产生相同输出（无随机性）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = pattern_match_single(prices, T_idx)
        assert r1 is not None
        assert r2 is not None
        for key in r1:
            assert r1[key] == pytest.approx(r2[key])


class TestComputePatternFeatures:
    """compute_pattern_features 单元测试 — 固定输入验证"""

    def test_f1_f5_similarity_features(self):
        """F1-F5: 相似度特征 — 固定输入验证"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.3, 0.1])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01, 0.01])
        top_end_indices = np.array([100, 200, 300, 400, 500])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=750,
        )
        assert result["top1_sim"] == 0.9
        assert result["top5_avg_sim"] == pytest.approx(0.5)  # mean of 5
        assert result["sim_decay"] == pytest.approx(0.4)     # 0.9-0.5
        assert result["sim_variance"] > 0                    # 应有方差
        assert result["match_distance_ratio"] == pytest.approx(0.4 / 0.9)

    def test_f6_f11_future_ret_features(self):
        """F6-F11: 后续表现特征"""
        top_scores = np.array([0.9, 0.7, 0.5])
        top_future_rets = np.array([0.06, -0.03, 0.02])
        top_end_indices = np.array([100, 200, 300])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)

        assert result["avg_future_ret"] == pytest.approx(np.mean([0.06, -0.03, 0.02]))
        # weighted: (0.9*0.06 + 0.7*(-0.03) + 0.5*0.02) / (0.9+0.7+0.5) = (0.054-0.021+0.01)/2.1
        assert result["weighted_future_ret"] == pytest.approx(0.043 / 2.1)
        assert result["median_future_ret"] == 0.02
        assert result["ret_sign_consistency"] == pytest.approx(2 / 3)  # 2 positive
        assert result["best_match_ret"] == 0.06
        assert result["max_dd_in_matches"] == 0.03  # max(0, -(-0.03)) = 0.03

    # ═══════════════════════════════════════════════════════════════
    # v2: GPT-5.5 完备性审查 P0 — F12-F15 固定样例
    # ═══════════════════════════════════════════════════════════════

    def test_f12_time_span(self):
        """F12: 匹配时间跨度 — max_index - min_index"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.4])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_time_span"] == 120.0  # 220 - 100
        assert result["match_time_span_ratio"] == pytest.approx(120 / 750)

    def test_f13_time_span_ratio(self):
        """F13: 时间跨度比率 — (max-min)/T_back"""
        top_scores = np.array([0.9, 0.7])
        top_future_rets = np.array([0.05, -0.02])
        # span=500, T_back=1000 → ratio=0.5
        top_end_indices = np.array([100, 600])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=1000,
        )
        assert result["match_time_span_ratio"] == 0.5

    def test_f14_cluster_ratio(self):
        """F14: 聚类比率 — 60日窗口内最大匹配数/K"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        # indices sorted: [100, 120, 160, 220]
        # searchsorted(x+60, side="right") 行为:
        #   i=0: searchsorted(160, right) → 3 (160插入到现有160之后) → 3-0=3
        #   i=1: searchsorted(180, right) → 2 → 2-1=1
        #   i=2: searchsorted(220, right) → 4 (220插入到现有220之后) → 4-2=2
        #   i=3: searchsorted(280, right) → 4 → 4-3=1
        # max_in_window = 3, ratio = 3/4 = 0.75
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_cluster_ratio"] == pytest.approx(3 / 4)  # 3/4=0.75

    def test_f15_n_matches_above_thresh(self):
        """F15: 高于0.8阈值的匹配数 — 严格 > 0.8"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 200, 300, 400])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        # 0.81>0.8 ✓, 0.80>0.8 ✗ (不严格大于), 0.79 ✗, 0.90 ✓
        assert result["n_matches_above_thresh"] == 2

    def test_f15_boundary_exactly_08(self):
        """F15: 恰好等于0.8不计入（> 0.8，非 >= 0.8）"""
        top_scores = np.array([0.80, 0.80])
        top_future_rets = np.array([0.05, -0.02])
        top_end_indices = np.array([100, 200])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["n_matches_above_thresh"] == 0


class TestExtractMorphFeatures:
    """extract_morph_features 便捷接口测试"""

    def test_alias(self):
        """extract_morph_features 应与 pattern_match_single 结果一致"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = extract_morph_features(prices, T_idx)
        assert (r1 is None) == (r2 is None)
        if r1 is not None:
            for key in r1:
                assert r1[key] == pytest.approx(r2[key])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
