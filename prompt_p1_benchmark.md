你负责为 etf-pattern-match-pybind11 创建可复现的性能基准测试。

## 当前状态

项目有 37× DTW / 61× pattern match / 2.2× batch 的性能数字，但没有：
- 说明数字来自均值还是最优值
- 可运行脚本让别人在自己机器上复现
- 方法文档（warm-up、重复次数、统计方式）
- 机器可读的历史结果（JSON）

已有的相关文件：
- `verify_etf_core.py` — C++ vs Python 一致性验证（含一些性能计时）
- `verify_batch.py` — 批量验证（含 batch 性能对比）
- `README.md` — 含加速结果表
- `src/cpp/etf_core.cpp` — 8 个 C++ 函数

## 任务

### 1. 创建 benchmarks/ 目录结构

```
benchmarks/
├── run_benchmark.py          ← 可运行脚本
├── results/
│   └── .gitkeep              ← 占位文件
└── README.md                 ← 方法说明
```

### 2. 创建 benchmarks/run_benchmark.py

一个独立的 Python 脚本，不依赖项目其他文件（除了已安装的 etf_core 和 numpy）。

```python
"""可复现的性能基准测试

用法:
    python benchmarks/run_benchmark.py                    # 全部基准
    python benchmarks/run_benchmark.py --function dtw     # 仅 DTW
    python benchmarks/run_benchmark.py --repeat 50        # 自定义重复次数
"""
```

**设计约束**：

- **warm-up**: 每个函数先跑 5 次（结果丢弃），排除首次调用的 JIT/缓存开销
- **计时轮次**: 默认 100 次
- **统计输出**: 中位数 + 95% 置信区间（percentile 2.5 / 97.5），同时报告均值和标准差
- **Python baseline**: 为每个 benchmark 实现对应的纯 Python 版本（NumPy），和 C++ 用完全相同的算法逻辑和输入数据
- **计时方式**: 使用 `time.perf_counter()` 或 `timeit`。明确是否包含 Python↔C++ 数据转换开销

**要 benchmark 的函数**：

| 函数 | 输入 | Python baseline |
|------|------|----------------|
| `dtw_distance` | 两个长度 19 的随机序列，window=5 | 纯 NumPy 实现的 DTW |
| `cosine_similarity` | 两个长度 19 的随机序列 | NumPy `np.dot` / `np.linalg.norm` |
| `pattern_match_single` | 随机价格序列 (长度 1000)，T_idx=500 | 纯 Python 的形态匹配逻辑 |
| `pattern_match_batch` | 随机价格序列 (1000×50)，100 个时间点 | 循环调用 single 做 baseline |

**输出格式**（stdout，Markdown 表格 + JSON）：

```markdown
## Benchmark Results

Environment: Windows 11, Python 3.12.7, PyTorch 2.13.0+cpu, MSVC 19.51 /O2
Commit: abc1234
Date: 2026-07-16

| Function | Python Median (µs) | C++ Median (µs) | Speedup | 95% CI |
|----------|-------------------|-----------------|---------|--------|
| dtw_distance | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
```

同时将结果写入 `benchmarks/results/<date>-<commit>.json`：

```json
{
  "environment": {
    "os": "Windows 11",
    "python": "3.12.7",
    "compiler": "MSVC 19.51",
    "optimization": "/O2",
    "cpu": "...",
    "commit": "abc1234",
    "date": "2026-07-16"
  },
  "methodology": {
    "warmup_runs": 5,
    "timed_runs": 100,
    "statistic": "median",
    "ci_level": 95,
    "ci_method": "percentile"
  },
  "results": [
    {
      "function": "dtw_distance",
      "python_median_us": ...,
      "cpp_median_us": ...,
      "speedup_median": ...,
      "python_mean_us": ...,
      "cpp_mean_us": ...,
      "python_ci_95": [..., ...],
      "cpp_ci_95": [..., ...]
    }
  ]
}
```

### 3. 创建 benchmarks/README.md

```markdown
# 性能基准测试

## 快速开始
python benchmarks/run_benchmark.py

## 方法
- 每个函数 warm-up 5 次后计时 100 次
- 报告中位数和 95% 分位数置信区间
- Python baseline 使用相同算法逻辑和 NumPy 实现
- 计时使用 time.perf_counter()，排除数据转换开销

## 结果稳定性
同版本不同次运行的预期波动在 ±5% 以内。
如果某次运行偏离超过此范围，检查后台进程或 CPU 频率调节。

## 历史结果
见 results/ 目录。文件名格式: YYYY-MM-DD-<commit_short>.json
```

### 4. 验收

```bash
cd E:/workspace/projects/形态匹配ETF策略-pybind11
python benchmarks/run_benchmark.py
```

- 脚本运行无报错
- 输出中包含中位数和 CI
- `benchmarks/results/` 中生成了 JSON 文件
- 报告的中位数 speedup 与 README 中声明的 37×/61× 在 ±10% 以内。如果不一致，不要修改代码——诚实记录差异，可能是不同基准测试方法导致的

### 5. 可选项：如果时间允许

- 在 `docs/benchmark.md` 创建一个汇总页面，展示最新 benchmark 结果（替代 README 中散落的数字引用）
- 添加 `--output-json` 参数指定 JSON 输出路径

## 约束

- 不要修改 src/cpp/etf_core.cpp 的算法逻辑
- 不要修改 CMakeLists.txt
- 路径使用正斜杠
- Python 命令如需输出中文，加 `PYTHONIOENCODING=utf-8`
- benchmark 脚本应能脱离项目其他文件独立运行（只依赖 numpy 和已安装的 etf_core）
- 完成后告诉我：脚本运行结果 + 与 README 数字是否一致
