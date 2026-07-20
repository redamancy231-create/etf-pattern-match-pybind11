# 关键文件索引 | Key File Index

> 最后更新 Last updated: 2026-07-04

## 代码 | Code
- [dtw.py](../src/core/dtw.py) — DTW 距离 + 序列标准化 | DTW distance + sequence standardization
- [pattern_match.py](../src/core/pattern_match.py) — 形态匹配引擎（15 维特征）| Pattern matching engine (15-dimensional features)
- [technical.py](../src/core/technical.py) — ADX / ATR / 板块轮动 | ADX / ATR / sector rotation
- [market_features.py](../src/core/market_features.py) — F16-F21 市场环境特征 | F16-F21 market environment features
- [risk_controls.py](../src/core/risk_controls.py) — 风控规则（纯计算）| Risk control rules (pure computation)
- [metrics.py](../src/core/metrics.py) — Sortino / Calmar / IC 统计 | Sortino / Calmar / IC statistics
- [etf_core.cpp](../src/cpp/etf_core.cpp) — 统一 C++ 加速模块（7 函数）| Unified C++ acceleration module (7 functions)
- [etf_core.pyi](../src/cpp/pyi/etf_core.pyi) — C++ 类型存根 | C++ type stubs

## 验证 | Verification
- [test_dtw.py](../tests/test_dtw.py) — DTW 模块测试（27 项）| DTW module tests (27 tests)
- [test_technical.py](../tests/test_technical.py) — 技术指标测试（12 项）| Technical indicator tests (12 tests)
- [test_pattern_match.py](../tests/test_pattern_match.py) — 形态匹配测试（15 项）| Pattern matching tests (15 tests)
- [verify_etf_core.py](../verify_etf_core.py) — C++ vs Python 一致性验证 | C++ vs Python consistency verification
- [verify_batch.py](../verify_batch.py) — 批量形态匹配验证 | Batch pattern matching verification

## 构建 | Build
- [CMakeLists.txt](../CMakeLists.txt) — 顶层 CMake 配置 | Top-level CMake configuration
- [src/cpp/CMakeLists.txt](../src/cpp/CMakeLists.txt) — C++ 子目录 CMake | C++ subdirectory CMake
- [ci.yml](../.github/workflows/ci.yml) — GitHub Actions CI（Windows + MSVC）

## 文档 | Documentation
- [README.md](../README.md) — GitHub 首页（简体中文）| GitHub homepage (Simplified Chinese)
- [en/README.md](../en/README.md) — English README
- [zh-Hant/README.md](../zh-Hant/README.md) — 正體中文 README
- [CLAUDE.md](../CLAUDE.md) — 开发笔记与 pybind11 经验 | Development notes and pybind11 lessons
- [project_status.md](../project_status.md) — 项目状态 | Project status
- [docs/file-index.md](file-index.md) — 本文件 | This file
- [docs/performance-analysis.md](performance-analysis.md) — Amdahl 性能分析（英文）| Amdahl performance analysis (English)
- [docs/performance-analysis.zh-CN.md](performance-analysis.zh-CN.md) — Amdahl 性能分析（简体中文）

## 设计文档（中文）| Design Documents (Chinese)
- [初始方案 Initial plan (zh-CN)](reviews/initial-plan.zh-CN.md) — 初始设计提案 | Initial design proposal
- [修订方案 v2 Revision plan v2 (zh-CN)](reviews/revision-plan-v2.zh-CN.md) — 双审查后修订方案 | Revised plan after dual review

## 原始来源 | Original Sources
- V3.3.py — 原始策略（归档基线）| Original strategy (archived baseline)
- V3.6-Decoupled.py — 解耦架构参考 | Decoupled architecture reference
