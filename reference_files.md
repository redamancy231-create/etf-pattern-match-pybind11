# 关键文件索引

> 最后更新: 2026-07-18

## 代码
- [etf_core.cpp](src/cpp/etf_core.cpp) — C++ 统一加速模块（8 函数）
- [dtw.py](src/core/dtw.py) — DTW 距离 + 序列标准化
- [pattern_match.py](src/core/pattern_match.py) — 形态匹配引擎（15 维特征）
- [technical.py](src/core/technical.py) — ADX / ATR / 板块轮动
- [market_features.py](src/core/market_features.py) — F16-F21 市场环境特征
- [risk_controls.py](src/core/risk_controls.py) — 风控规则（纯计算）
- [metrics.py](src/core/metrics.py) — Sortino / Calmar / IC 统计
- [etf_core.pyi](src/cpp/pyi/etf_core.pyi) — C++ 类型存根

## 测试
- [test_dtw.py](tests/test_dtw.py) — DTW 模块测试（27 项）
- [test_technical.py](tests/test_technical.py) — 技术指标测试（12 项）
- [test_pattern_match.py](tests/test_pattern_match.py) — 形态匹配测试（15 项）
- [test_etf_core.cpp](tests/test_etf_core.cpp) — C++ 原生测试（58 cases）
- [verify_etf_core.py](verify_etf_core.py) — C++ vs Python 一致性验证
- [verify_batch.py](verify_batch.py) — 批量形态匹配验证

## 配置
- [pyproject.toml](pyproject.toml) — Python 构建配置（scikit-build-core）
- [CMakeLists.txt](CMakeLists.txt) — 顶层 CMake 配置
- [ci.yml](.github/workflows/ci.yml) — GitHub Actions CI（三平台）
- [sanitizer.yml](.github/workflows/sanitizer.yml) — ASAN+UBSAN CI
- [benchmark.yml](.github/workflows/benchmark.yml) — 性能回归 CI

## 文档
- [README.md](README.md) — 项目首页（简体中文）
- [en/README.md](en/README.md) — English README
- [zh-Hant/README.md](zh-Hant/README.md) — 正體中文 README
- [CLAUDE.md](CLAUDE.md) — 开发笔记与 pybind11 经验
- [project_status.md](project_status.md) — 项目状态追踪
- [improvement_plan.md](improvement_plan.md) — 改进方案（已完成 ✅）
- [docs/file-index.md](docs/file-index.md) — 关键文件索引
- [docs/performance-analysis.md](docs/performance-analysis.md) — Amdahl 性能分析（英文）
- [docs/performance-analysis.zh-CN.md](docs/performance-analysis.zh-CN.md) — Amdahl 性能分析（简体中文）
- [docs/reviews/initial-plan.zh-CN.md](docs/reviews/initial-plan.zh-CN.md) — 初始设计方案
- [docs/reviews/revision-plan-v2.zh-CN.md](docs/reviews/revision-plan-v2.zh-CN.md) — 修订方案 v2

## 工具
- [run_benchmark.py](benchmarks/run_benchmark.py) — 可复现性能基准测试
- [quickstart.py](examples/quickstart.py) — 快速示例
