cmake_minimum_required(VERSION 3.20)

# etf_core 原生 C++ 测试
# 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    project(etf_core_native_tests LANGUAGES CXX)
endif()

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 测试直接调用含 py::array_t 参数的 C++ 入口，因此需要嵌入式 Python 运行时。
set(Python_EXECUTABLE "" CACHE FILEPATH "Path to python.exe")
if(Python_EXECUTABLE)
    get_filename_component(Python_ROOT_DIR "${Python_EXECUTABLE}" DIRECTORY)
endif()
find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Embed)

# pybind11 — 与项目根 CMakeLists.txt 使用相同的自动探测策略。
set(pybind11_DIR "" CACHE PATH "pybind11 cmake config dir")
if(NOT pybind11_DIR)
    execute_process(
        COMMAND "${Python_EXECUTABLE}" -c "import pybind11; print(pybind11.get_cmake_dir())"
        OUTPUT_VARIABLE _pybind11_cmake_dir
        OUTPUT_STRIP_TRAILING_WHITESPACE
        ERROR_QUIET
    )
    if(_pybind11_cmake_dir)
        set(pybind11_DIR "${_pybind11_cmake_dir}")
    endif()
endif()
if(NOT pybind11_DIR)
    message(FATAL_ERROR
        "pybind11 not found. Install it for the selected Python or set pybind11_DIR.")
endif()
find_package(pybind11 REQUIRED CONFIG)

include(FetchContent)
set(DOCTEST_WITH_TESTS OFF CACHE BOOL "" FORCE)
FetchContent_Declare(
    doctest
    GIT_REPOSITORY https://github.com/doctest/doctest.git
    GIT_TAG v2.4.11
    GIT_SHALLOW TRUE
)
FetchContent_MakeAvailable(doctest)

get_filename_component(ETF_PROJECT_ROOT "${CMAKE_CURRENT_LIST_DIR}/.." ABSOLUTE)
set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")

# 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。
# 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程
# add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。
if(TARGET etf_core)
    get_target_property(_etf_core_type etf_core TYPE)
endif()

if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")
    set(ETF_CORE_NATIVE_TARGET etf_core)
elseif(TARGET etf_core)
    set(ETF_CORE_NATIVE_TARGET etf_core_native_link)
    if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})
        add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
        target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
        target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
    endif()
else()
    set(ETF_CORE_NATIVE_TARGET etf_core)
    add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")
    target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)
    target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)
endif()

add_executable(test_native test_etf_core.cpp)
target_compile_features(test_native PRIVATE cxx_std_20)
target_link_libraries(
    test_native
    PRIVATE
        doctest::doctest
        ${ETF_CORE_NATIVE_TARGET}
        pybind11::embed
)

if(MSVC)
    target_compile_options(test_native PRIVATE /utf-8 /wd4819)
    if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"
       OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))
        target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)
    endif()
endif()

enable_testing()
add_test(NAME test_native COMMAND test_native)