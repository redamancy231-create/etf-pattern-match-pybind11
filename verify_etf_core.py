# -*- coding: utf-8 -*-
"""
etf_core C++ 模块验证脚本
==========================
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03

对比 C++ 实现与 Python 参考实现的输出一致性。

用法:
  python verify_etf_core.py          # 完整验证
  python verify_etf_core.py --quick  # 快速冒烟测试
"""

import sys
import os
import time
import argparse
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# ── Python 参考实现 ──
from core.dtw import standardize_returns, cosine_similarity, dtw_distance
from core.technical import compute_adx as py_adx, compute_atr as py_atr
from core.pattern_match import pattern_match_single as py_pattern_match

# ── C++ 加速实现 ──
try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "build", "Release"))
    import etf_core
    CPP_AVAILABLE = True
    print("✅ etf_core C++ 模块加载成功")
except ImportError as e:
    CPP_AVAILABLE = False
    print(f"⚠️  etf_core 未编译: {e}")
    print("   运行: cmake -B build -DPython_EXECUTABLE=... && cmake --build build --config Release")


def generate_test_data(seed: int = 42):
    """生成合成测试数据"""
    np.random.seed(seed)
    n = 600
    prices = 100.0 * np.cumprod(1.0 + np.random.randn(n) * 0.02)
    high = prices + np.abs(np.random.randn(n) * 0.5)
    low = prices - np.abs(np.random.randn(n) * 0.5)
    return prices, high, low


def compare_arrays(py_arr: np.ndarray, cpp_arr: np.ndarray,
                   name: str, tol: float = 1e-10) -> bool:
    """比较两个数组"""
    if py_arr.shape != cpp_arr.shape:
        print(f"  ❌ {name}: shape mismatch {py_arr.shape} vs {cpp_arr.shape}")
        return False
    if np.allclose(py_arr, cpp_arr, atol=tol, rtol=1e-12, equal_nan=True):
        print(f"  ✅ {name}: match (tol={tol})")
        return True
    else:
        max_diff = np.max(np.abs(py_arr - cpp_arr))
        print(f"  ❌ {name}: max diff = {max_diff:.2e}")
        return False


def compare_scalar(py_val: float, cpp_val: float,
                   name: str, tol: float = 1e-10) -> bool:
    """比较两个标量"""
    if np.isnan(py_val) and np.isnan(cpp_val):
        print(f"  ✅ {name}: both NaN")
        return True
    diff = abs(py_val - cpp_val)
    if diff < tol:
        print(f"  ✅ {name}: match (diff={diff:.2e})")
        return True
    else:
        print(f"  ❌ {name}: py={py_val:.10f} cpp={cpp_val:.10f} diff={diff:.2e}")
        return False


def compare_dicts(py_dict: dict, cpp_dict: dict, tol: float = 1e-10) -> bool:
    """比较两个特征字典"""
    if py_dict is None and cpp_dict is None:
        print("  ✅ both None")
        return True
    if py_dict is None or cpp_dict is None:
        print(f"  ❌ one is None: py={py_dict is None} cpp={cpp_dict is None}")
        return False

    all_ok = True
    for key in py_dict:
        if key not in cpp_dict:
            print(f"  ❌ key '{key}' missing in C++ result")
            all_ok = False
            continue
        py_val = py_dict[key]
        cpp_val = cpp_dict[key]
        if isinstance(py_val, (int, np.integer)):
            ok = py_val == cpp_val
        else:
            ok = abs(float(py_val) - float(cpp_val)) < tol
        if not ok:
            print(f"  ❌ {key}: py={py_val} cpp={cpp_val}")
            all_ok = False
    if all_ok:
        print(f"  ✅ all 15 features match (tol={tol})")
    return all_ok


def verify_standardize_returns():
    """验证 standardize_returns"""
    print("\n" + "=" * 60)
    print("📐 standardize_returns")
    print("=" * 60)

    tests = [
        np.array([100.0, 101.0, 102.5, 99.8, 103.2, 105.0]),
        np.array([100.0] * 10),  # constant
        np.array([50.0]),        # single element
        np.array([0.0, 50.0, 100.0]),  # zero price
    ]

    all_ok = True
    for i, prices in enumerate(tests):
        py_r = standardize_returns(prices)
        cpp_r = np.array(etf_core.standardize_returns(prices))
        ok = compare_arrays(py_r, cpp_r, f"test_{i}", tol=1e-10)
        all_ok = all_ok and ok

    # 大规模随机测试
    for seed in range(5):
        prices, _, _ = generate_test_data(seed)
        py_r = standardize_returns(prices)
        cpp_r = np.array(etf_core.standardize_returns(prices))
        ok = compare_arrays(py_r, cpp_r, f"random_{seed}", tol=1e-10)
        all_ok = all_ok and ok

    return all_ok


def verify_cosine_similarity():
    """验证 cosine_similarity"""
    print("\n" + "=" * 60)
    print("📐 cosine_similarity")
    print("=" * 60)

    tests = [
        (np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])),
        (np.array([1.0, 2.0, 3.0]), np.array([-1.0, -2.0, -3.0])),
        (np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0])),
        (np.array([0.0, 0.0, 0.0]), np.array([1.0, 2.0, 3.0])),
    ]

    all_ok = True
    for i, (x, y) in enumerate(tests):
        py_v = cosine_similarity(x, y)
        cpp_v = etf_core.cosine_similarity(x, y)
        ok = compare_scalar(py_v, cpp_v, f"test_{i}")
        all_ok = all_ok and ok
    return all_ok


def verify_dtw_distance():
    """验证 dtw_distance"""
    print("\n" + "=" * 60)
    print("📐 dtw_distance")
    print("=" * 60)

    all_ok = True
    for seed in range(10):
        np.random.seed(seed)
        x = np.random.randn(19)  # L_QUERY-1
        y = np.random.randn(19)
        py_d = dtw_distance(x, y, window=5)
        cpp_d = etf_core.dtw_distance(x, y, 5)
        ok = compare_scalar(py_d, cpp_d, f"random_{seed}", tol=1e-8)
        all_ok = all_ok and ok
    return all_ok


def verify_compute_adx():
    """验证 compute_adx"""
    print("\n" + "=" * 60)
    print("📐 compute_adx")
    print("=" * 60)

    all_ok = True
    for seed in range(5):
        _, high, low = generate_test_data(seed)
        close = (high + low) / 2 + np.random.randn(len(high)) * 0.1
        py_v = py_adx(high, low, close, n=14)
        cpp_v = etf_core.compute_adx(high, low, close, 14)
        ok = compare_scalar(py_v, cpp_v, f"random_{seed}")
        all_ok = all_ok and ok
    return all_ok


def verify_pattern_match_single():
    """验证 pattern_match_single — 核心验证"""
    print("\n" + "=" * 60)
    print("📐 pattern_match_single (核心验证)")
    print("=" * 60)

    all_ok = True
    np.random.seed(42)
    prices = 100.0 * np.cumprod(1.0 + np.random.randn(800) * 0.02)

    for T_idx in [500, 600, 700]:
        print(f"\n  T_idx={T_idx}:")
        py_r = py_pattern_match(prices, T_idx)
        cpp_r = etf_core.pattern_match_single(prices, T_idx)

        if py_r is None and cpp_r is None:
            print("  ✅ both None")
            continue
        if py_r is None or cpp_r is None:
            print(f"  ❌ mismatch: py None={py_r is None} cpp None={cpp_r is None}")
            all_ok = False
            continue

        ok = compare_dicts(py_r, dict(cpp_r), tol=1e-6)
        all_ok = all_ok and ok

    return all_ok


def verify_performance():
    """性能基准"""
    if not CPP_AVAILABLE:
        return

    print("\n" + "=" * 60)
    print("⚡ 性能基准")
    print("=" * 60)

    # DTW
    np.random.seed(0)
    x = np.random.randn(19)
    y = np.random.randn(19)

    n_iter = 1000
    t0 = time.perf_counter()
    for _ in range(n_iter):
        dtw_distance(x, y, window=5)
    py_time = (time.perf_counter() - t0) / n_iter * 1e6

    t0 = time.perf_counter()
    for _ in range(n_iter):
        etf_core.dtw_distance(x, y, 5)
    cpp_time = (time.perf_counter() - t0) / n_iter * 1e6

    print(f"\n  DTW (L=19):")
    print(f"    Python: {py_time:.1f} µs/call")
    print(f"    C++:    {cpp_time:.1f} µs/call")
    print(f"    加速比: {py_time/cpp_time:.1f}x")

    # Pattern match
    prices = 100.0 * np.cumprod(1.0 + np.random.randn(600) * 0.02)
    T_idx = 500

    t0 = time.perf_counter()
    for _ in range(3):
        py_pattern_match(prices, T_idx)
    py_pm = (time.perf_counter() - t0) / 3 * 1000

    t0 = time.perf_counter()
    for _ in range(3):
        etf_core.pattern_match_single(prices, T_idx)
    cpp_pm = (time.perf_counter() - t0) / 3 * 1000

    print(f"\n  pattern_match_single:")
    print(f"    Python: {py_pm:.1f} ms/call")
    print(f"    C++:    {cpp_pm:.1f} ms/call")
    print(f"    加速比: {py_pm/cpp_pm:.1f}x")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()

    if not CPP_AVAILABLE:
        print("\n请先编译 C++ 模块:")
        print("  cmake -B build -DPython_EXECUTABLE=<path-to-python.exe>")
        print("  cmake --build build --config Release")
        return 1

    results = {}

    if args.quick:
        results["standardize_returns"] = verify_standardize_returns()
        results["pattern_match"] = verify_pattern_match_single()
    else:
        results["standardize_returns"] = verify_standardize_returns()
        results["cosine_similarity"] = verify_cosine_similarity()
        results["dtw_distance"] = verify_dtw_distance()
        results["compute_adx"] = verify_compute_adx()
        results["pattern_match"] = verify_pattern_match_single()

    verify_performance()

    print("\n" + "=" * 60)
    passed = sum(results.values())
    total = len(results)
    print(f"  验证结果: {passed}/{total} 通过")
    print("=" * 60)

    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
