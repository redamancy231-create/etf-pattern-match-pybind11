# etf-pattern-match-pybind11 改进方案

> 2026-07-16 · 初稿 DeepSeek-V4-Pro · 审查 GPT-5.6-Sol（via Codex CLI）
> 状态：修订 v1.1（根据 Codex 审查意见调整优先级和范围）

## 概述

当前仓库的核心交付物（C++ 加速模块 + 测试 + notebook + 双语文档）质量很高，但在**可安装性**、**性能可复现性**和**学术可引用性**上有缺口。

## 改进项

### 🔴 P0 — 完整安装链路

**问题**：用户必须手动 cmake 编译。对 Python 用户门槛太高。

**修订**（审查意见：原方案 P0 范围太窄，不能只加一个 `pyproject.toml`）——P0 的完整范围是：构建系统 + wheel + 干净环境验证。

**Step 1：选定构建方案**

在以下两种方案中选一种：

| 方案 | 做法 | 优点 | 缺点 |
|------|------|------|------|
| A | scikit-build-core（`[build-system]` 指向 cmake） | CMake 原生支持，pybind11 官方推荐 | 需要 cmake 在 PATH |
| B | setuptools `build_ext`（手动调用 cmake） | 更灵活，可以 fallback | 维护成本高 |

推荐方案 A（scikit-build-core），ml-quant-trading 用的也是类似模式。

**Step 2：确保 Wheel 包含 C++ 扩展**

```toml
[build-system]
requires = ["scikit-build-core>=0.9", "pybind11>=3.0.4", "cmake>=3.20"]
build-backend = "scikit_build_core.build"

[project]
name = "etf-pattern-match-pybind11"
version = "1.0.0"
requires-python = ">=3.10"
dependencies = ["numpy>=1.24"]
```

CMakeLists.txt 需要添加 `install(TARGETS etf_core DESTINATION .)`。

**Step 3：干净环境验收**

在三个场景下验证：
```bash
# 场景 A: 本地安装
pip install .
python -c "import etf_core; print(etf_core.dtw_distance)"

# 场景 B: wheel 安装
python -m build
pip install dist/*.whl
python -c "import etf_core"

# 场景 C: git 安装
pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git
```

**Step 4：支持平台声明**

```text
第一阶段支持：
  - Windows x64 · Python 3.10–3.12 · MSVC 19.51+
  - Ubuntu/Linux x64 · Python 3.10–3.12 · GCC 11+ / Clang 16+
不支持（首批）：
  - macOS（无硬件测试）
  - Python 3.13+（cvxpy/ecos 可能不兼容）
```

### 🟡 P1 — 性能可复现性

**修订**（审查意见：性能数字来自均值还是最优值？需要可运行脚本而非一次性文档）。

**当前问题**：37×/61×/2.2× 数字已同步到全项目 8 处引用，但没有说明：
- 来自均值还是单次最优？
- 是否包含 Python↔C++ 数据转换开销？
- 多线程还是单线程？
- warm-up 次数、重复次数

**方案**（替代原 P2 Benchmark Board）：

创建 `benchmarks/` 目录：
```text
benchmarks/
├── run_benchmark.py          ← 可运行脚本（--function dtw|pattern|batch --repeat 100）
├── results/
│   └── 2026-07-12-<commit>.json  ← 机器可读结果
└── README.md                 ← 方法说明
```

`docs/benchmark.md` 展示汇总数据（替代 README 中散落的数字）。以后可以通过比较不同 commit 的 JSON 检测性能回归。

**关键规范**：
```text
- warm-up: 5 次 → discard
- 计时轮次: 100 次
- 报告: 中位数 + 95% CI（不是最优值）
- Python baseline: 与 C++ 使用相同算法逻辑
- 记录: Python 版本、C++ 编译器、优化选项、commit SHA
```

### 🟢 P2 — 学术引用支持

**方案**：添加 `CITATION.cff` + README 底部 BibTeX 块（参考 ma-case-study-pipeline）。

### 🟢 P2 — 贡献者基础文档

**修订**（审查意见：比 Community 宣传页优先级高）。

- `CONTRIBUTING.md`：构建说明、测试运行方式、支持平台
- Issue 模板（Bug Report）

### ❌ 移除

- **Makefile**：审查指出 `which python` 在 Windows 上不工作，跨平台维护成本高。README 里的 cmake 命令已经足够清晰。
- **Community 宣传页**：社交草稿已在 GitHub贡献策略 项目中集中管理，不需要在代码仓库重复。

---

## 执行顺序

1. **P0** — 选定构建方案 → 实现 → 干净环境验证 → 更新 README 安装说明
2. **P1** — 创建 benchmarks/ → 重新跑一次 benchmark 记录方法 → 更新 README 数字引用
3. **P2** — CITATION.cff + CONTRIBUTING.md

## 不做

- **多平台 CI**：先定义支持平台，CI 跟随需要。如果只支持 Windows，Windows CI 足够
- **Docker**：不是 Web 服务
- **ruff/formatter**：代码量小，手动风格一致
