你负责让 etf-pattern-match-pybind11 支持 `pip install`。

## 当前状态

项目用 CMake + pybind11 构建 C++ 加速模块，用户必须手动敲 cmake 命令。目录结构：

```
形态匹配ETF策略-pybind11/
├── CMakeLists.txt              ← CMake 根文件（project etf_pattern_match）
├── src/
│   └── cpp/
│       ├── CMakeLists.txt      ← C++ 子目录（定义 pybind11_add_module）
│       ├── etf_core.cpp        ← 8 个函数的统一加速模块
│       ├── __init__.py         ← Python 包入口（空或简单导入）
│       └── pyi/                ← 类型存根
├── tests/                      ← 54 个 pytest 测试
├── verify_etf_core.py          ← C++ vs Python 一致性验证
├── verify_batch.py             ← 批量验证
└── README.md                   ← 中英双语文档
```

## 任务：实现 pip install

### 1. 创建 pyproject.toml

使用 scikit-build-core 作为构建后端（pybind11 官方推荐方案）：

```toml
[build-system]
requires = ["scikit-build-core>=0.9", "pybind11>=3.0.4", "cmake>=3.20"]
build-backend = "scikit_build_core.build"

[project]
name = "etf-pattern-match-pybind11"
version = "1.0.0"
description = "High-performance ETF pattern matching — pybind11/C++20 acceleration (DTW 37x / pattern match 61x)"
readme = "README.md"
license = { text = "MIT" }
requires-python = ">=3.10"
dependencies = ["numpy>=1.24"]
keywords = ["etf", "pattern-matching", "dtw", "pybind11", "quant"]
classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: C++",
]

[project.urls]
Homepage = "https://github.com/redamancy231-create/etf-pattern-match-pybind11"

[tool.scikit-build]
cmake.minimum-version = "3.20"
wheel.packages = ["src/cpp"]
```

### 2. 修改 CMakeLists.txt（根）

在文件末尾（`add_subdirectory` 之后）添加 install 指令，让 scikit-build-core 能把编译好的 .pyd 打包进 wheel：

```cmake
# Install — scikit-build-core 需要这些指令来打包 wheel
install(TARGETS etf_core DESTINATION src/cpp)
```

### 3. 检查 src/cpp/CMakeLists.txt

确认 pybind11_add_module 的目标名是 `etf_core`（与上面的 install TARGETS 一致）。

### 4. 确保 src/cpp/__init__.py 存在并导入 C++ 模块

```python
from .etf_core import (
    dtw_distance,
    dtw_distance_batch,
    pattern_match_core,
    pattern_match_batch,
    # ... 全部 8 个导出函数
)
```

如果当前 __init__.py 内容不完整，从 etf_core.cpp 的 `m.def(...)` 调用中提取所有函数名。

### 5. 验收

在三个场景下测试（Windows Git Bash，Python 3.12）：

```bash
# 场景 A: 本地 editable 安装
cd E:/workspace/projects/形态匹配ETF策略-pybind11
pip install -e .
python -c "from src.cpp import etf_core; print(dir(etf_core))"

# 场景 B: 本地安装
pip install .
python -c "import etf_core; print(etf_core.dtw_distance)"

# 场景 C: 确保 pytest 仍然通过
python -m pytest tests/ -v
```

### 6. 更新 README 安装说明

在 README.md 的"快速开始"部分，在 cmake 命令之前添加 pip install 方式：

```markdown
### pip install (推荐)
pip install git+https://github.com/redamancy231-create/etf-pattern-match-pybind11.git

### 从源码构建 (cmake)
...
```

## 约束

- 不要修改 etf_core.cpp 的算法逻辑
- 路径使用正斜杠 `/`
- 所有 Python 命令如需输出中文，加 `PYTHONIOENCODING=utf-8`
- 完成后告诉我：三个验收场景是否通过 + 遇到的问题
