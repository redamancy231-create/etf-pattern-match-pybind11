# C++ 加速模块 — 统一 etf_core 模块
# v2 修订：三模块合并为一个，减少 ABI 管理复杂度和重复样板代码
# v3: 固定输出到 build/ (MSVC 加 config 子目录 → build/Release/)

pybind11_add_module(etf_core MODULE etf_core.cpp)
set_target_properties(etf_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)
message(STATUS "C++ module: etf_core")
