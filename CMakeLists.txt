cmake_minimum_required(VERSION 3.20)

# ──────────────────────────────────────────────
# 形态匹配ETF策略 — C++ 加速模块
# > 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
# > 复用 pybind11-demo 已验证的 MSVC 配置
# > v2: 三模块合并为单 etf_core, /utf-8 优先
# ──────────────────────────────────────────────

project(etf_pattern_match LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Python
set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
endif()
if(NOT Python_EXECUTABLE)
    message(WARNING
        "Python_EXECUTABLE not set. "
        "Use -DPython_EXECUTABLE=/path/to/python.exe to specify which Python to use.\n"
        "  Example: cmake -B build -DPython_EXECUTABLE=<path-to-python.exe>")
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module)

# pybind11 — auto-detect
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir OUTPUT_STRIP_TRAILING_WHITESPACE ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found!\n"
        "  Install: pip install pybind11\n"
        "  Verify:  python -c \"import pybind11; print(pybind11.__version__)\"\n"
        "  Or set:  -Dpybind11_DIR=/path/to/share/cmake/pybind11\n"
        "  Or set:  -DPython_EXECUTABLE=/path/to/python.exe (auto-detect uses this Python)")
endif()
find_package(pybind11 REQUIRED CONFIG)

# MSVC — v2: 优先 /utf-8，/wd4819 为后备
if(MSVC)
    add_compile_options("$<$<CONFIG:Release>:/O2>")
    add_compile_options(/utf-8 /wd4819)
endif()

# 子目录 — C++ 模块
add_subdirectory(src/cpp)

# Install — scikit-build-core 需要这些指令来打包 wheel
install(TARGETS etf_core DESTINATION src/cpp)
# Also expose the extension at the top level for ``import etf_core`` after pip install.
install(TARGETS etf_core DESTINATION .)
# Match scikit-build-core's wheel package destination (``cpp``) as well.
install(TARGETS etf_core DESTINATION cpp)
