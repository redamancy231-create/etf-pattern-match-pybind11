# 性能基准测试

## 快速开始

```bash
python benchmarks/run_benchmark.py
```

也可以只运行一个 benchmark 或调整计时轮次：

```bash
python benchmarks/run_benchmark.py --function dtw
python benchmarks/run_benchmark.py --repeat 50
python benchmarks/run_benchmark.py --output-json benchmarks/results/manual.json
```

脚本只依赖 NumPy、已安装的 `etf_core` 和 Python 标准库，不导入项目内的其它
Python 文件。运行前请确保 `etf_core` 扩展已经安装或已加入 Python 的模块搜索路径。

## 方法

- 每个 Python/C++ 实现分别 warm-up 5 次后计时 100 次；可通过 `--warmup` 和
  `--repeat` 覆盖默认值。
- 每次计时使用 `time.perf_counter()`，单位为微秒；报告中位数、均值、样本标准差，
  以及 percentile 2.5 / 97.5 构成的 95% 经验区间。
- Python baseline 使用相同的算法逻辑和相同的预先生成输入：DTW 使用 NumPy
  数组动态规划，cosine 使用 `np.dot` / `np.linalg.norm`，pattern match 使用
  纯 Python + NumPy 实现，batch baseline 严格循环调用 single。
- 输入数据只生成一次，并在 warm-up 和所有计时轮次中复用；随机种子为 42。
- 输入 NumPy 数组在计时前已构造成连续的 `float64` / `int64` 数组，因此**不包含
  随机数据生成和输入数组转换开销**；计时**包含 Python↔C++ 函数调用边界和返回对象
  构造开销**。
- `pattern_match_batch` 的当前 C++ 绑定接口接收一条 1-D 价格序列和 100 个
  `T_idx`。因此本 benchmark 使用长度 1000 的价格序列和 `T_idx=400..499`；任务
  描述中的 `1000×50` 不能直接作为该接口的输入，其中 50 对应默认的
  `cos_prefilter_top=50`。如果要测 50 条 ETF，应在调用层按列分别运行。

## 结果稳定性

同版本、相同机器上不同次运行的预期波动在 ±5% 以内。如果某次运行偏离超过此
范围，检查后台进程、CPU 频率调节和电源策略。benchmark 记录的是当前机器上的
实际结果，不保证不同 CPU、Python、编译器或 Release/Debug 构建之间的绝对数值相同。

## 历史结果

见 `results/` 目录。文件名格式：`YYYY-MM-DD-<commit_short>.json`。
每个 JSON 文件包含运行环境、warm-up/重复次数、统计方法、输入说明、均值/标准差、
中位数和 95% percentile 区间。
