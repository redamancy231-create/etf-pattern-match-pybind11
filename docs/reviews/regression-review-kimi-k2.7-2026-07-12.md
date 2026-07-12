# Kimi-K2.7-Code 重构回归审查报告

> **审查日期**: 2026-07-12
> **审查后端**: Kimi-K2.7-Code (via Kimi Code CLI)
> **审查类型**: 魔鬼代言人式回归审查
> **背景**: GPT-5.6-Sol 发现 32 条问题并已修复，本审查独立验证修复未引入新 bug。

---

## 发现的总数

- **回归 bug（修复引入的新问题）**: 0 条
- **残留问题（修复不完整 / 测试未同步）**: 1 条（已就地修复）
- **正面确认（验证无问题的改动）**: 7 条

---

## 回归 bug

未发现由本次修复引入的新 bug。

所有 7 项高风险改动均通过静态审查与实证测试，未触发崩溃、结果不一致或契约破坏。

---

## 残留问题

**#U1 `tests/test_dtw.py:64-75` standardize_returns NaN 测试未随契约更新**

- **引入者**: `standardize_returns` NaN 处理修复（逐元素过滤 → 窗口级 `isfinite` 检查）。
- **触发条件**: 运行 `python -m pytest tests/test_dtw.py -v`。
- **后果**: `test_nan_value_in_array` 与 `test_all_nan` 两个用例断言仍期望旧行为（NaN 被 `np.maximum` 替换后继续计算），但当前实现已在函数入口按窗口拒绝任何含 NaN/Inf 的输入，导致这两个用例失败。
- **修复建议**: 将这两个用例更新为验证新契约——含 NaN/Inf 的输入返回空数组。
- **处理状态**: 已在本审查中就地修复，当前测试套件 54/54 通过。

---

## 正面确认

以下 7 项高风险改动均通过针对性实证验证，未发现回归。

### #V1 DTW 滚动双行数组 (`dtw_distance_span`)

- **验证方法**:
  - 随机生成 20+ 组不同长度、不同 window 的序列，对比 C++ `etf_core.dtw_distance` 与 Python `core.dtw.dtw_distance`。
  - 极端输入：空序列、单元素、长度差大、`window=0`。
- **结果**: 所有情况差异均 ≤ 1e-8，空序列/零长度均返回 `inf`。
- **结论**: 滚动双行实现与 Python 全矩阵实现数值等价，`prev[0]=INF` 重置正确。

### #V2 `pattern_match_core` 共享核心提取

- **验证方法**:
  - 相同 `T_idx` 分别调用 `etf_core.pattern_match_single` 与 `etf_core.pattern_match_batch`（单元素 `t_indices`），逐项对比 15 维特征。
  - 在历史价格中注入 NaN，验证双路径均优雅跳过并保持一致。
- **结果**: 15 维特征逐项一致（容差 1e-6），NaN 场景下单/batch 行为一致。
- **结论**: 共享核心两条路径（无缓存 vs 预计算缓存）结果一致，NaN 过滤与特征提取逻辑收敛。

### #V3 `standardize_returns` NaN/Inf 处理

- **验证方法**:
  - 对含 `np.inf`、`-np.inf`、`np.nan`、全 NaN 的输入分别调用 Python 与 C++ 版本。
  - 验证下游 `pattern_match_single`/`pattern_match_batch` 对空返回的处理。
- **结果**: 双端均返回空数组；下游调用者均按 `len(result) < 2` 正确跳过或返回 None。
- **结论**: 新契约被正确实现，调用链已适配。唯一残留是测试未同步（已修复）。

### #V4 ADX Wilder's smoothing 初始化

- **验证方法**:
  - 对 `n ∈ {7, 14, 21}`，分别取长度 `n+14`、`n+15`、`n+16`，对比 Python 与 C++ `compute_adx`。
  - 验证长度不足时返回 25.0，长度足够时返回真实计算值。
- **结果**: Python 与 C++ 输出完全一致（差异 ≤ 1e-10），长度边界正确。
- **结论**: C++ 填满前 n 个位置的行为已与 Python 对齐。

### #V5 `pattern_match_batch` 按需预计算

- **验证方法**:
  - 正常批量调用 vs 100 次独立 `pattern_match_single` 对比。
  - 全无效 `T_idx`、`t_indices` 为空、相邻 `T_idx` 搜索范围高度重叠、价格含 NaN。
- **结果**: `features` 形状 `(0, 15)` / `(n_valid, 15)` 正确，`valid_mask` 形状 `(n_samples,)` 正确；与 single 结果一致；无崩溃。
- **结论**: 按需预计算并集实现正确，边界退化场景稳定。

### #V6 技术指标 dtype 强制转换

- **验证方法**:
  - 向 `compute_adx`、`compute_atr` 传入 `np.int64` 类型的 OHLC 数组。
  - 验证 Python 不再返回 0.0，C++ 与 Python 结果一致。
- **结果**: Python 输出非零真实 ADX 值，C++ 与 Python ATR 序列一致。
- **结论**: dtype 强制转换有效阻止了整数输入的静默截断。

### #V7 `sector_rotation` 确定性排序

- **验证方法**:
  - 使用含并列收益率的字典，重复调用 10 次，观察结果是否稳定。
- **结果**: 10 次结果完全一致。
- **结论**: `rankdata(method="average")` 消除了 PYTHONHASHSEED 依赖性。

---

## 实证测试汇总

| 测试集 | 用例数 | 结果 |
|--------|--------|------|
| `python -m pytest tests/` | 54 | 通过（含已修复的 NaN 测试） |
| `python verify_etf_core.py` | 5 大项 | 通过 |
| `python verify_batch.py` | 7 大项 | 通过 |
| 自定义回归测试（滚动 DTW、Inf 拒绝、ADX 短序列、整数 OHLC 等） | 21+ | 通过 |

---

## 结论

本轮魔鬼代言人式回归审查未发现 GPT-5.6-Sol 修复引入的新 bug。仅发现 1 处测试用例未随 `standardize_returns` 契约更新而同步修改，已就地修复。当前代码库测试套件全绿，7 项高风险改动均表现稳定。
