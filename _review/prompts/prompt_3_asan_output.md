Reading prompt from stdin...
OpenAI Codex v0.144.1
--------
workdir: C:\Users\33455
model: gpt-5.6-sol
provider: packycode
approval: never
sandbox: danger-full-access
reasoning effort: xhigh
reasoning summaries: none
session id: 019f6f8d-bb24-73f3-9a47-11bbdccf0cb9
--------
user
You are adding ASAN/UBSAN configuration for the "etf-pattern-match-pybind11" project at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the existing CI file at .github/workflows/ci.yml and the CMakeLists.txt to understand the current setup.

## Task: Add sanitizer build job to CI

### What to create/modify

1. **New file: `.github/workflows/sanitizer.yml`** — A separate CI workflow (not modifying the main ci.yml) that:
   - Runs on `ubuntu-latest` only (sanitizers are best supported on Linux/GCC)
   - Installs g++, cmake, and Python 3.12
   - Installs numpy, pybind11, pytest
   - Builds with sanitizer flags: `-fsanitize=address,undefined -fno-omit-frame-pointer`
   - Runs Python tests under the sanitized build
   - Uses `ASAN_OPTIONS=detect_leaks=1:halt_on_error=1` env var
   - Trigger: on push to master and pull requests (same as main CI)
   - Name: "Sanitizer (ASAN+UBSAN)"

2. **Optionally modify `CMakeLists.txt`** to accept a `-DUSE_SANITIZERS=ON` flag that adds the sanitizer compiler flags. If modifying CMakeLists.txt is too complex, just set CXXFLAGS in the workflow YAML directly.

### Requirements

- Don't modify the main ci.yml — this is a SEPARATE workflow file
- Don't add sanitizer tests that duplicate the existing Python tests
- The sanitizer job should run the existing Python test suite under the sanitized build
- Provenance comment at top: "GPT-5.6-Sol (via Codex CLI), 2026-07-17"

### What NOT to do

- Don't add to the main ci.yml
- Don't create new test files
- Don't run the CI

### Output

Write the complete new files.

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
2026-07-17T10:09:58.573818Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $files = @('"'.github/workflows/ci.yml','CMakeLists.txt'); foreach ("'$f in $files) { $p = Join-Path (Get-Location) $f; $bytes = [System.IO.File]::ReadAllBytes($p); $bom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF); $utf8 = New-Object System.Text.UTF8Encoding($false,$true); try { [void]$utf8.GetString($bytes); $enc='"'UTF-8-valid' } catch { "'$enc='"'not-valid-UTF-8' }; Write-Output \"--- "'$f | $enc | BOM=$bom ---"; if ($enc -eq '"'UTF-8-valid') { Write-Output ([System.IO.File]::ReadAllText("'$p,[System.Text.Encoding]::UTF8)) } else { Write-Output ([System.IO.File]::ReadAllText($p,[System.Text.Encoding]::Default)) } }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 202ms:
--- .github/workflows/ci.yml | UTF-8-valid | BOM=False ---
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: CI

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build-and-test:
    strategy:
      fail-fast: false
      matrix:
        os:
          - windows-latest
          - ubuntu-latest
          - macos-latest

    runs-on: ${{ matrix.os }}

    env:
      PYTHONIOENCODING: utf-8

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        id: python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Linux build tools
        if: runner.os == 'Linux'
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Install macOS build tools
        if: runner.os == 'macOS'
        run: brew install cmake

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install numpy pybind11 pytest

      - name: Configure CMake
        if: runner.os == 'Windows'
        run: |
          $pythonPath = (Get-Command python).Source
          cmake -B build -DPython_EXECUTABLE="$pythonPath" -DCMAKE_BUILD_TYPE=Release

      - name: Configure CMake (Linux/macOS)
        if: runner.os != 'Windows'
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -B build -DPython_EXECUTABLE="$python_path" -DCMAKE_BUILD_TYPE=Release

      - name: Build
        run: cmake --build build --config Release

      - name: Run tests
        env:
          PYTHONIOENCODING: utf-8
        run: python -m pytest tests/ -v

      - name: Verify C++ vs Python consistency
        env:
          PYTHONIOENCODING: utf-8
        run: python verify_etf_core.py

      - name: Verify batch matching
        env:
          PYTHONIOENCODING: utf-8
        run: python verify_batch.py

--- CMakeLists.txt | UTF-8-valid | BOM=False ---
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


exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Force; Write-Output '"'--- src/cpp/CMakeLists.txt ---'; Get-Content -Raw -Encoding UTF8 'src/cpp/CMakeLists.txt'; Write-Output '--- Python import references ---'; Get-ChildItem -Path tests -Recurse -File | Select-String -Pattern 'etf_core|sys.path|PYTHONPATH' -Encoding UTF8 | Select-Object Path,LineNumber,Line" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 259ms:


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d--h--         2026/7/17     18:01                .git                                                                 
d-----          2026/7/5     12:58                .github                                                              
d-----          2026/7/3     21:42                .pytest_cache                                                        
d-----         2026/7/16     17:17                benchmarks                                                           
d-----         2026/7/12     18:00                build                                                                
d-----         2026/7/12     19:56                docs                                                                 
d-----         2026/7/12     19:41                notebooks                                                            
d-----          2026/7/3     21:29                src                                                                  
d-----         2026/7/17     18:01                tests                                                                
d-----         2026/7/17     17:32                _review                                                              
d-----         2026/7/12     19:33                审查提示词                                                                
-a----          2026/7/4     14:22            397 .gitignore                                                           
-a----         2026/7/16     16:48           1434 CHANGELOG.md                                                         
-a----         2026/7/16     17:29            853 CITATION.cff                                                         
-a----         2026/7/12     19:55          12069 CLAUDE.md                                                            
-a----         2026/7/16     16:48           2653 CMakeLists.txt                                                       
-a----         2026/7/16     17:30           1881 CONTRIBUTING.md                                                      
-a----         2026/7/16     16:18           4484 improvement_plan.md                                                  
-a----          2026/7/4     14:03           1069 LICENSE                                                              
-a----         2026/7/16     17:02           6144 project_status.md                                                    
-a----         2026/7/16     16:32           3641 prompt_p0_build.md                                                   
-a----         2026/7/16     16:52           5077 prompt_p1_benchmark.md                                               
-a----         2026/7/16     16:48            867 pyproject.toml                                                       
-a----         2026/7/16     17:28          14342 README.md                                                            
-a----         2026/7/16     16:48            405 SECURITY.md                                                          
-a----         2026/7/12     19:58          62758 social-preview.png                                                   
-a----          2026/7/4     13:16           8665 verify_batch.py                                                      
-a----          2026/7/4     14:19           9507 verify_etf_core.py                                                   
--- src/cpp/CMakeLists.txt ---
# C++ 加速模块 — 统一 etf_core 模块
# v2 修订：三模块合并为一个，减少 ABI 管理复杂度和重复样板代码
# v3: 固定输出到 build/ (MSVC 加 config 子目录 → build/Release/)

pybind11_add_module(etf_core MODULE etf_core.cpp)
set_target_properties(etf_core PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}"
)
message(STATUS "C++ module: etf_core")

--- Python import references ---

Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 3
Line       : # etf_core 原生 C++ 测试


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 7
Line       :     project(etf_core_native_tests LANGUAGES CXX)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 51
Line       : set(ETF_CORE_SOURCE "${ETF_PROJECT_ROOT}/src/cpp/etf_core.cpp")


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 53
Line       : # 生产 target etf_core 是 MODULE_LIBRARY；CMake 禁止可执行文件直接链接 MODULE_LIBRARY。


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 54
Line       : # 独立配置 tests/ 时，使用同一生产源文件创建可链接的静态 etf_core；若未来从根工程


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 55
Line       : # add_subdirectory(tests)，则保留生产模块并创建仅供原生测试链接的 etf_core_native_link。


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 56
Line       : if(TARGET etf_core)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 57
Line       :     get_target_property(_etf_core_type etf_core TYPE)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 60
Line       : if(TARGET etf_core AND NOT _etf_core_type STREQUAL "MODULE_LIBRARY")


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 61
Line       :     set(ETF_CORE_NATIVE_TARGET etf_core)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 62
Line       : elseif(TARGET etf_core)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 63
Line       :     set(ETF_CORE_NATIVE_TARGET etf_core_native_link)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 64
Line       :     if(NOT TARGET ${ETF_CORE_NATIVE_TARGET})


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 65
Line       :         add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 66
Line       :         target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 67
Line       :         target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 70
Line       :     set(ETF_CORE_NATIVE_TARGET etf_core)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 71
Line       :     add_library(${ETF_CORE_NATIVE_TARGET} STATIC "${ETF_CORE_SOURCE}")


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 72
Line       :     target_link_libraries(${ETF_CORE_NATIVE_TARGET} PUBLIC pybind11::embed)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 73
Line       :     target_compile_features(${ETF_CORE_NATIVE_TARGET} PUBLIC cxx_std_20)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 76
Line       : add_executable(test_native test_etf_core.cpp)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 82
Line       :         ${ETF_CORE_NATIVE_TARGET}


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 88
Line       :     if(ETF_CORE_NATIVE_TARGET STREQUAL "etf_core_native_link"


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 89
Line       :        OR (ETF_CORE_NATIVE_TARGET STREQUAL "etf_core" AND NOT _etf_core_type))


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\CMakeLists.txt
LineNumber : 90
Line       :         target_compile_options(${ETF_CORE_NATIVE_TARGET} PRIVATE /utf-8 /wd4819)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_dtw.py
LineNumber : 13
Line       : sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_etf_core.cpp
LineNumber : 2
Line       :  * test_etf_core.cpp — etf_core 原生 C++ 算法测试


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_etf_core.cpp
LineNumber : 25
Line       : // etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_etf_core.cpp
LineNumber : 54
Line       : // 非有限值策略（由 etf_core.cpp 的当前实现定义）：


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_pattern_match.py
LineNumber : 11
Line       : sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 10
Line       : sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 11
Line       : sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build", "Release"))


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 120
Line       :     import etf_core


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 125
Line       :         etf_core.compute_atr(high, low, close)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 133
Line       :     import etf_core


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\test_technical.py
LineNumber : 139
Line       :     result = etf_core.compute_atr(high, low, close, n)


Path       : E:\workspace\projects\形态匹配ETF策略-pybind11\tests\__pycache__\test_technical.cpython-312-pytest-9.1.1.pyc
LineNumber : 142
Line       : })�py17�py19�py20�py22�py24�py26z%(py28)s�py28�   zassert %(py31)s�py31)�etf_corer   r   �
             uniformr   r   �_format_assertmsgr#   r$   r%   �	Exceptionr�   �lowerr   r    r!   r"   �append�_
             format_boolop)r�   r'   r(   r)   rR   �@py_format2r�   r+   r*   rs   rt   �@py_assert11r�   �@py_ass
             ert16�@py_assert21�@py_assert23�@py_assert25�@py_assert18rv   �@py_format15�@py_format27�@py_format
             29�@py_format30�@py_format32s                           r.   �#test_compute_atr_mismatched_lengthsr�   
             v   s"  � ��




exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Write-Output '"'--- src tree ---'; Get-ChildItem -Path src -Recurse -File | Select-Object FullName; Write-Output '--- Python etf_core import references under src ---'; Get-ChildItem -Path src -Recurse -File -Include *.py | Select-String -Pattern 'etf_core|build' -Encoding UTF8 | Select-Object Path,LineNumber,Line; Write-Output '--- git status ---'; git status --short" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 194ms:
--- src tree ---

 M .github/workflows/ci.yml
 M project_status.md
?? _review/
?? docs/reviews/performance-analysis-review-kimi.md
?? improvement_plan.md
?? notebooks/01_price_series.png
?? notebooks/02_query_window.png
?? notebooks/03_cosine_prefilter.png
?? notebooks/04_dtw_warping.png
?? notebooks/05_feature_evolution.png
?? notebooks/06_trading_signals.png
?? notebooks/07_batch_dtw.png
?? notebooks/08_benchmark.png
?? prompt_p0_build.md
?? prompt_p1_benchmark.md
?? tests/CMakeLists.txt
?? tests/test_etf_core.cpp
FullName                                                                                     
--------                                                                                     
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\dtw.py                                     
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\market_features.py                         
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\metrics.py                                 
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\pattern_match.py                           
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\risk_controls.py                           
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\technical.py                               
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__init__.py                                
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\dtw.cpython-312.pyc            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\dtw.cpython-314.pyc            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\market_features.cpython-312.pyc
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\metrics.cpython-312.pyc        
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\pattern_match.cpython-312.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\pattern_match.cpython-314.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\risk_controls.cpython-312.pyc  
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\technical.cpython-312.pyc      
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\__init__.cpython-312.pyc       
E:\workspace\projects\形态匹配ETF策略-pybind11\src\core\__pycache__\__init__.cpython-314.pyc       
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\CMakeLists.txt                              
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\etf_core.cpp                                
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\__init__.py                                 
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\pyi\etf_core.pyi                            
E:\workspace\projects\形态匹配ETF策略-pybind11\src\strategy\__init__.py                            
--- Python etf_core import references under src ---
                                                                                             
--- git status ---



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; foreach ($f in @('"'src/core/dtw.py','src/core/pattern_match.py','src/core/technical.py','tests/test_dtw.py','tests/test_pattern_match.py','tests/test_technical.py')) { Write-Output \"--- "'$f ---"; Get-Content -Raw -Encoding UTF8 $f }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 160ms:
--- src/core/dtw.py ---
# -*- coding: utf-8 -*-
"""
DTW 距离计算与序列预处理模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 339-383
===============================
从 形态匹配ETF组合策略_V3.3.py 提取，零外部依赖（仅 numpy）。

模块内容:
  - standardize_returns: 收益率序列标准化（去均值/除标准差）
  - cosine_similarity:   两向量余弦相似度
  - dtw_distance:        带 Sakoe-Chiba band 的 DTW 距离
  - dtw_distance_batch:  批量 DTW（一对多），减少 Python 调用开销

原始来源:
  形态匹配ETF组合策略_V3.3.py (archived in parent project)
  行 339-383 (DTW 模块, V3.3)

算法逻辑零改动 — 仅结构重组 + 类型标注 + 批量接口。
"""

import numpy as np
from typing import Optional, Tuple, Union


def standardize_returns(price_series: np.ndarray) -> np.ndarray:
    """
    计算标准化收益率序列: (rets - mean(rets)) / std(rets)

    Args:
        price_series: 价格序列, shape (n,)

    Returns:
        标准化收益率序列, shape (n-1,). 若任一价格为非有限值则返回空数组。

    算法逻辑: 与 V3.3.py 第 362-373 行完全一致。
    """
    if len(price_series) < 2:
        return np.array([], dtype=np.float64)

    # 窗口级检查：任一价格为非有限值 → 整个窗口无效
    if not np.all(np.isfinite(price_series)):
        return np.array([], dtype=np.float64)

    rets = np.diff(np.log(np.maximum(price_series, 1e-12)))
    std_ = np.std(rets)
    if std_ < 1e-12:
        return rets - np.mean(rets)
    return (rets - np.mean(rets)) / std_


def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """
    计算两向量的余弦相似度 ∈ [-1, 1]

    算法逻辑: 与 V3.3.py 第 376-382 行完全一致。
    """
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    if norm_x < 1e-12 or norm_y < 1e-12:
        return 0.0
    return float(np.dot(x, y) / (norm_x * norm_y))


def dtw_distance(
    x: np.ndarray,
    y: np.ndarray,
    window: int = 5,
) -> float:
    """
    计算两个序列的 DTW 距离，使用 Sakoe-Chiba band 约束。

    Args:
        x: 查询序列, shape (n,)
        y: 历史序列, shape (m,)
        window: Sakoe-Chiba band 宽度 (默认 5)

    Returns:
        归一化 DTW 距离: sqrt(dtw[n,m]) / (n+m)

    算法逻辑: 与 V3.3.py 第 339-359 行完全一致。
    """
    n, m = len(x), len(y)
    band = max(window, abs(n - m))

    dtw = np.full((n + 1, m + 1), np.inf, dtype=np.float64)
    dtw[0, 0] = 0.0

    for i in range(1, n + 1):
        j_start = max(1, i - band)
        j_end = min(m + 1, i + band + 1)
        for j in range(j_start, j_end):
            cost = (float(x[i - 1]) - float(y[j - 1])) ** 2
            dtw[i, j] = cost + min(dtw[i - 1, j], dtw[i, j - 1], dtw[i - 1, j - 1])

    path_len = n + m
    return np.sqrt(dtw[n, m]) / path_len if path_len > 0 else np.inf


def dtw_distance_batch(
    query: np.ndarray,
    candidates: np.ndarray,
    window: int = 5,
    top_k: Optional[int] = None,
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """
    批量 DTW：一个 query 对多个 candidates。

    Args:
        query: 查询序列, shape (L,)
        candidates: 候选序列集, shape (N, L)
        window: Sakoe-Chiba band 宽度
        top_k: 若指定，仅返回距离最小的 top_k 个索引和距离

    Returns:
        若 top_k 为 None: distances shape (N,)
        若 top_k 指定: (indices, distances) 各 shape (top_k,)
    """
    n_candidates = len(candidates)
    if n_candidates == 0:
        return np.array([], dtype=np.float64)

    if len(query) != candidates.shape[1]:
        raise ValueError(
            f"query 长度 {len(query)} != candidates 列数 {candidates.shape[1]}"
        )

    distances = np.empty(n_candidates, dtype=np.float64)
    for i in range(n_candidates):
        distances[i] = dtw_distance(query, candidates[i], window=window)

    if top_k is not None and top_k < n_candidates:
        idx = np.argpartition(distances, top_k)[:top_k]
        idx = idx[np.argsort(distances[idx])]
        return idx, distances[idx]

    return distances


def generate_query_candidates(
    prices: np.ndarray,
    T_idx: int,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    从价格序列生成查询窗口和候选窗口集合（前视偏差防护）。

    Args:
        prices: 完整价格序列, shape (n_days,)
        T_idx: 当前时点索引
        L_query: 查询窗口长度（交易日）
        T_back: 历史回溯范围
        match_step: 匹配步长

    Returns:
        (query_prices, candidates_prices, candidate_end_indices)
    """
    if L_query <= 0:
        raise ValueError(f"L_query must be > 0, got {L_query}")
    if T_back <= 0:
        raise ValueError(f"T_back must be > 0, got {T_back}")
    if match_step <= 0:
        raise ValueError(f"match_step must be > 0, got {match_step}")
    if T_idx < 0 or T_idx >= len(prices):
        raise ValueError(f"T_idx={T_idx} must satisfy 0 <= T_idx < {len(prices)}")
    if not np.all(np.isfinite(prices)):
        raise ValueError("prices contains non-finite values")
    if T_idx < L_query:
        raise ValueError(f"T_idx={T_idx} < L_query={L_query}")

    query_prices = prices[T_idx - L_query + 1: T_idx + 1].copy()

    search_end = T_idx - L_query
    search_start = max(L_query - 1, T_idx - T_back)

    candidate_ends = list(range(search_start, search_end + 1, match_step))
    if not candidate_ends:
        raise ValueError(f"无候选窗口: T_idx={T_idx}")

    candidates_array = np.empty((len(candidate_ends), L_query), dtype=np.float64)
    valid_indices = []

    for ci, hist_end in enumerate(candidate_ends):
        hist_start = hist_end - L_query + 1
        if hist_start >= 0:
            candidates_array[ci] = prices[hist_start: hist_end + 1]
            valid_indices.append(hist_end)

    return (
        query_prices,
        candidates_array[:len(valid_indices)],
        np.array(valid_indices, dtype=np.int64),
    )

--- src/core/pattern_match.py ---
# -*- coding: utf-8 -*-
"""
形态匹配引擎 — 15维特征提取
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 389-627
=============================
从 形态匹配ETF组合策略_V3.3.py 提取，零掘金依赖（仅 numpy）。

模块内容:
  - pattern_match_single: 单ETF单时点形态匹配 + 15维特征提取
  - compute_pattern_features: 辅助函数，从匹配结果提取F1-F15
  - extract_morph_features: 便捷接口，接收标准化收益率一步完成

原始来源:
  V3.3.py 行 389-627 (pattern_match_single, V3.0 余弦预筛选)
  V3.3.py 行 362-382 (standardize_returns, cosine_similarity → 委托给 dtw.py)

算法逻辑零改动 — V3.0-FIX-1/1b/2/3/5 全部保留。
"""

import numpy as np
from typing import Dict, Optional

from .dtw import standardize_returns, cosine_similarity, dtw_distance


# ── 默认参数（与 V3.3.py 第一部分常量一致）──
_DEFAULT_L_QUERY = 20
_DEFAULT_T_BACK = 750
_DEFAULT_MATCH_STEP = 1
_DEFAULT_M_FORWARD = 5
_DEFAULT_K_MATCHES = 10
_DEFAULT_DTW_WINDOW = 5
_DEFAULT_COS_PREFILTER_TOP = 50


def pattern_match_single(
    prices: np.ndarray,
    T_idx: int,
    k: int = _DEFAULT_K_MATCHES,
    L_query: int = _DEFAULT_L_QUERY,
    T_back: int = _DEFAULT_T_BACK,
    match_step: int = _DEFAULT_MATCH_STEP,
    M_forward: int = _DEFAULT_M_FORWARD,
    dtw_window: int = _DEFAULT_DTW_WINDOW,
    cos_prefilter_top: int = _DEFAULT_COS_PREFILTER_TOP,
) -> Optional[Dict[str, float]]:
    """
    对单只 ETF 在时点 T_idx 执行形态匹配，提取 15 维特征。

    V3.0 余弦预筛选：第1遍仅计算余弦相似度(O(L))→取top-N→第2遍仅对top-N计算DTW。

    前视偏差防护（严格因果性约束）：
      - 查询窗口：[T_idx - L_query + 1, T_idx]
      - 历史搜索范围：[max(L_query - 1, T_idx - T_back), T_idx - L_query]
      - 匹配片段后续收益要求 fut_end < T_idx

    Args:
        prices: 完整价格序列, shape (n_days,)
        T_idx: 查询时点索引
        k: Top-K 匹配数（默认 10）
        L_query: 查询窗口长度（默认 20）
        T_back: 历史回溯范围（默认 750）
        match_step: 匹配步长（默认 1）
        M_forward: 预测窗口（默认 5）
        dtw_window: Sakoe-Chiba band 宽度（默认 5）
        cos_prefilter_top: 余弦预筛选保留数（默认 50）

    Returns:
        15维特征字典，数据不足时返回 None。
        键名: top1_sim, top5_avg_sim, sim_decay, sim_variance,
              match_distance_ratio, avg_future_ret, weighted_future_ret,
              median_future_ret, ret_sign_consistency, best_match_ret,
              max_dd_in_matches, match_time_span, match_time_span_ratio,
              match_cluster_ratio, n_matches_above_thresh

    算法逻辑: 与 V3.3.py 第 389-627 行完全一致。
    所有 V3.0-FIX 保留: fast_shape_dists, sigma_fast + DTW归一化修正,
    hist_rets缓存, global_min_cos/max_cos.
    """
    # ── 输入校验 ──
    if M_forward < 1:
        raise ValueError(f"M_forward must be >= 1, got {M_forward}")
    if L_query < 3:
        raise ValueError(f"L_query must be >= 3, got {L_query}")
    if match_step <= 0:
        raise ValueError(f"match_step must be > 0, got {match_step}")
    if T_idx < L_query + M_forward + 10:
        return None

    query_prices = prices[T_idx - L_query + 1: T_idx + 1]
    if len(query_prices) < L_query:
        return None

    query_rets = standardize_returns(query_prices)
    if len(query_rets) < 2:
        return None

    search_end = T_idx - L_query
    if search_end < L_query:
        return None

    search_start = max(L_query - 1, T_idx - T_back)

    # ═══════════════════════════════════════════════════════════════
    # 第1遍：余弦相似度 + 快速形状距离（全量候选）
    # ═══════════════════════════════════════════════════════════════
    cos_candidates: list = []        # (hist_end, hist_start, cos_s, hist_rets)
    fast_shape_dists: list = []      # V3.0-FIX-1: 全量快速距离

    for hist_end in range(search_start, search_end + 1, match_step):
        hist_start = hist_end - L_query + 1
        if hist_start < 0:
            continue

        hist_prices = prices[hist_start: hist_end + 1]
        if len(hist_prices) < L_query:
            continue

        hist_rets = standardize_returns(hist_prices)
        if len(hist_rets) < 2:
            continue

        cos_s = cosine_similarity(hist_rets, query_rets)

        # V3.0-FIX-1: 收集全量 fast_shape_dists（含 cos≤0）
        fast_d = np.sqrt(np.mean((hist_rets - query_rets) ** 2))
        fast_shape_dists.append(fast_d)

        if cos_s > 0:
            # V3.0-FIX-3: 缓存 hist_rets 避免第2遍重复标准化
            cos_candidates.append((hist_end, hist_start, cos_s, hist_rets))

    if len(cos_candidates) < 3:
        return None

    # V3.0-FIX-1b: sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
    # DTW ≈ RMSD / (2*sqrt(L_query-1))，sigma_fast 须同步缩放
    sigma_fast = (
        np.std(fast_shape_dists) / (2.0 * np.sqrt(L_query - 1))
        if len(fast_shape_dists) > 1
        else 1.0
    )
    sigma_fast = max(sigma_fast, 1e-12)

    # V3.0-FIX-5: 全量 cos>0 候选计算余弦归一化边界
    cos_candidates.sort(key=lambda x: x[2], reverse=True)
    all_cos_values = np.array([c[2] for c in cos_candidates])
    global_min_cos = float(np.min(all_cos_values)) if len(all_cos_values) > 0 else 0.0
    global_max_cos = float(np.max(all_cos_values)) if len(all_cos_values) > 0 else 1.0

    n_cos = min(cos_prefilter_top, len(cos_candidates))
    top_cos = cos_candidates[:n_cos]

    # ═══════════════════════════════════════════════════════════════
    # 第2遍：仅对余弦 top-N 计算 DTW
    # ═══════════════════════════════════════════════════════════════
    dtw_dists: list = []
    cos_sims: list = []
    future_rets: list = []
    match_end_indices: list = []

    for hist_end, hist_start, sim_cos, hist_rets in top_cos:
        dtw_d = dtw_distance(hist_rets, query_rets, window=dtw_window)

        dtw_dists.append(dtw_d)
        cos_sims.append(sim_cos)

        fut_end = hist_end + M_forward
        if fut_end < len(prices) and fut_end < T_idx:
            fut_ret = float(prices[fut_end] / prices[hist_end] - 1)
        else:
            fut_ret = np.nan
        future_rets.append(fut_ret)
        match_end_indices.append(hist_end)

    if len(dtw_dists) < 3:
        return None

    dtw_dists_arr = np.array(dtw_dists, dtype=np.float64)
    cos_sims_arr = np.array(cos_sims, dtype=np.float64)
    future_rets_arr = np.array(future_rets, dtype=np.float64)
    match_end_arr = np.array(match_end_indices, dtype=np.int64)

    # V3.0-FIX-2: sigma = sigma_fast（基于全量快速距离）
    sigma = sigma_fast if sigma_fast > 1e-12 else 1.0
    sim_dtw = np.exp(-dtw_dists_arr / sigma)

    if len(sim_dtw) < 3:
        return None

    # ── 综合得分：0.5*DTW + 0.5*cosine（min-max 归一化后）──
    min_dtw_val, max_dtw_val = np.min(sim_dtw), np.max(sim_dtw)
    # V3.0-FIX-5: 余弦归一化使用全量边界
    min_cos, max_cos = global_min_cos, global_max_cos
    range_dtw = max_dtw_val - min_dtw_val if max_dtw_val - min_dtw_val > 1e-12 else 1.0
    range_cos = max_cos - min_cos if max_cos - min_cos > 1e-12 else 1.0
    norm_dtw = (sim_dtw - min_dtw_val) / range_dtw
    norm_cos = (cos_sims_arr - min_cos) / range_cos
    combined_scores = 0.5 * norm_dtw + 0.5 * norm_cos

    sorted_idx = np.argsort(combined_scores)[::-1]
    top_k = min(k, len(sorted_idx))
    top_idx = sorted_idx[:top_k]

    top_scores = combined_scores[top_idx]
    top_future_rets = future_rets_arr[top_idx]
    top_end_indices = match_end_arr[top_idx]

    # 过滤 NaN 未来收益
    nan_mask = ~np.isnan(top_future_rets)
    if np.sum(nan_mask) < 2:
        return None
    top_scores = top_scores[nan_mask]
    top_future_rets = top_future_rets[nan_mask]
    top_end_indices = top_end_indices[nan_mask]
    top_k_actual = len(top_scores)

    if top_k_actual < 2:
        return None

    # ── 提取 15 维特征 ──
    return compute_pattern_features(
        top_scores, top_future_rets, top_end_indices,
        top_k_actual=top_k_actual, T_back=T_back,
    )


def compute_pattern_features(
    top_scores: np.ndarray,
    top_future_rets: np.ndarray,
    top_end_indices: np.ndarray,
    top_k_actual: Optional[int] = None,
    T_back: int = _DEFAULT_T_BACK,
) -> Dict[str, float]:
    """
    从 DTW 精排后的 Top-K 匹配结果中提取 15 维形态特征。

    算法逻辑: 与 V3.3.py 第 579-627 行完全一致。

    Args:
        top_scores: 综合得分, shape (K,)
        top_future_rets: 对应的未来收益, shape (K,)
        top_end_indices: 匹配片段的结束索引, shape (K,)
        top_k_actual: 实际有效匹配数（默认使用 len(top_scores)）
        T_back: 历史回溯范围（用于 F13 归一化）

    Returns:
        15维特征字典
    """
    if len(top_scores) == 0 or len(top_scores) != len(top_future_rets) or len(top_scores) != len(top_end_indices):
        raise ValueError("top_scores, top_future_rets, top_end_indices must be non-empty and equal length")
    if T_back <= 0:
        raise ValueError(f"T_back must be > 0, got {T_back}")
    if top_k_actual is None:
        top_k_actual = len(top_scores)
    if top_k_actual < 1 or top_k_actual > len(top_scores):
        raise ValueError(f"top_k_actual={top_k_actual} must satisfy 1 <= top_k_actual <= {len(top_scores)}")

    # F1-F5: 相似度特征
    top1_sim = float(top_scores[0])
    n_for_avg = min(5, top_k_actual)
    top5_avg_sim = float(np.mean(top_scores[:n_for_avg]))
    sim_decay = top1_sim - top5_avg_sim
    sim_variance = float(np.var(top_scores)) if top_k_actual > 1 else 0.0
    match_distance_ratio = sim_decay / top1_sim if top1_sim > 1e-12 else 0.0

    # F6-F11: 匹配片段后续表现特征
    avg_future_ret = float(np.mean(top_future_rets))
    weighted_ret = (
        float(np.average(top_future_rets, weights=top_scores))
        if np.sum(top_scores) > 1e-12
        else avg_future_ret
    )
    median_future_ret = float(np.median(top_future_rets))
    ret_sign_consistency = float(np.sum(top_future_rets > 0) / top_k_actual)
    best_match_ret = float(top_future_rets[0])
    min_ret = float(np.min(top_future_rets))
    max_dd_in_matches = float(max(0.0, -min_ret))

    # F12-F15: 匹配质量特征
    match_time_span = (
        float(np.max(top_end_indices) - np.min(top_end_indices))
        if top_k_actual > 1
        else 0.0
    )
    match_time_span_ratio = match_time_span / T_back

    # F14: 聚类比率 — 60日内最大匹配数 / K
    top_end_sorted = np.sort(top_end_indices)
    max_in_window = 0
    for i in range(len(top_end_sorted)):
        j = np.searchsorted(top_end_sorted, top_end_sorted[i] + 60, side="right")
        count = j - i
        if count > max_in_window:
            max_in_window = count
    match_cluster_ratio = max_in_window / top_k_actual if top_k_actual > 0 else 0.0

    # F15: 高于 0.8 阈值的匹配数
    n_matches_above_thresh = int(np.sum(top_scores > 0.8))

    return {
        "top1_sim": top1_sim,
        "top5_avg_sim": top5_avg_sim,
        "sim_decay": sim_decay,
        "sim_variance": sim_variance,
        "match_distance_ratio": match_distance_ratio,
        "avg_future_ret": avg_future_ret,
        "weighted_future_ret": weighted_ret,
        "median_future_ret": median_future_ret,
        "ret_sign_consistency": ret_sign_consistency,
        "best_match_ret": best_match_ret,
        "max_dd_in_matches": max_dd_in_matches,
        "match_time_span": match_time_span,
        "match_time_span_ratio": match_time_span_ratio,
        "match_cluster_ratio": match_cluster_ratio,
        "n_matches_above_thresh": n_matches_above_thresh,
    }


def extract_morph_features(
    prices: np.ndarray,
    T_idx: int,
    **kwargs,
) -> Optional[Dict[str, float]]:
    """
    便捷接口：从价格序列一步提取15维形态特征。
    等价于 pattern_match_single(prices, T_idx, **kwargs)。

    提供此接口是为了让调用方无需了解 pattern_match_single 内部细节。
    """
    return pattern_match_single(prices, T_idx, **kwargs)

--- src/core/technical.py ---
# -*- coding: utf-8 -*-
"""
技术指标计算模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 757-795, 801-836, 1003-1032
=================
从 形态匹配ETF组合策略_V3.3.py 提取，零掘金依赖。

模块内容:
  - compute_adx:          ADX (Average Directional Index) — Wilder's smoothing
  - compute_sector_rotation: 行业轮动速度 (Spearman rank correlation)

原始来源:
  V3.3.py 行 757-795 (_compute_adx_from_df)
  V3.3.py 行 801-836 (_compute_sector_rotation)
  V3.3.py 行 1003-1032 (_compute_sector_rotation_historical)

算法逻辑零改动。
"""

import numpy as np
from typing import Dict


def compute_adx(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    n: int = 14,
) -> float:
    """
    从 OHLC 数组计算 ADX (Average Directional Index)。

    Args:
        high: 最高价序列, shape (n_days,)
        low:  最低价序列, shape (n_days,)
        close: 收盘价序列, shape (n_days,)
        n: 平滑周期 (默认 14)

    Returns:
        ADX 值 ∈ [0, 100]；数据不足时返回 25.0（中性值）。

    算法逻辑: 与 V3.3.py 第 757-795 行完全一致。
    """
    # 强制转换为 float64，防止整数 dtype 静默截断
    high = np.asarray(high, dtype=np.float64)
    low = np.asarray(low, dtype=np.float64)
    close = np.asarray(close, dtype=np.float64)

    if high.ndim != 1 or low.ndim != 1 or close.ndim != 1:
        raise ValueError("high/low/close must be 1-D arrays")
    if len(high) != len(low) or len(high) != len(close):
        raise ValueError("high/low/close must have same length")
    if n <= 0:
        raise ValueError(f"n must be > 0, got {n}")
    if len(high) < n + 16:
        return 25.0

    # True Range
    tr = np.maximum(
        high[1:] - low[1:],
        np.maximum(np.abs(high[1:] - close[:-1]), np.abs(low[1:] - close[:-1])),
    )

    # Directional Movement
    up = high[1:] - high[:-1]
    down = low[:-1] - low[1:]
    plus_dm = np.where((up > down) & (up > 0), up, 0)
    minus_dm = np.where((down > up) & (down > 0), down, 0)

    # Wilder's smoothing (初始值 = 简单均值，后续指数平滑)
    atr = np.zeros_like(tr)
    atr[:n] = np.mean(tr[:n])
    for i in range(n, len(tr)):
        atr[i] = (atr[i - 1] * (n - 1) + tr[i]) / n

    smoothed_plus = np.zeros_like(tr)
    smoothed_minus = np.zeros_like(tr)
    smoothed_plus[:n] = np.mean(plus_dm[:n])
    smoothed_minus[:n] = np.mean(minus_dm[:n])
    for i in range(n, len(tr)):
        smoothed_plus[i] = (smoothed_plus[i - 1] * (n - 1) + plus_dm[i]) / n
        smoothed_minus[i] = (smoothed_minus[i - 1] * (n - 1) + minus_dm[i]) / n

    plus_di = 100 * smoothed_plus / (atr + 1e-12)
    minus_di = 100 * smoothed_minus / (atr + 1e-12)
    dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di + 1e-12)

    adx = np.zeros_like(dx)
    adx[:n] = np.mean(dx[:n])
    for i in range(n, len(dx)):
        adx[i] = (adx[i - 1] * (n - 1) + dx[i]) / n

    return float(adx[-1])


def compute_sector_rotation(
    prev_returns: Dict[str, float],
    curr_returns: Dict[str, float],
    min_sectors: int = 4,
) -> float:
    """
    计算行业轮动速度。

    基于前后两期行业收益率的排名相关性：
      轮动速度 = 1 - |Spearman ρ|
    ρ 越接近 0 → 轮动越快 → 值越大。

    Args:
        prev_returns: {symbol: prev_period_return} 前一期行业收益
        curr_returns: {symbol: curr_period_return} 当前期行业收益
        min_sectors: 最小行业数要求

    Returns:
        轮动速度 ∈ [0, 1]；数据不足时返回 0.0。

    算法逻辑: 与 V3.3.py 第 801-836, 1003-1032 行完全一致。
    """
    common = sorted(set(prev_returns.keys()) & set(curr_returns.keys()))
    if len(common) < min_sectors:
        return 0.0

    # 按确定顺序提取收益率值
    prev_vals_arr = np.array([prev_returns[k] for k in common], dtype=np.float64)
    curr_vals_arr = np.array([curr_returns[k] for k in common], dtype=np.float64)

    # 使用平均秩（处理并列值），避免 PYTHONHASHSEED 导致的不确定排序
    # 纯 NumPy 实现，等价于 scipy.stats.rankdata(x, method="average")
    def _average_rank(x: np.ndarray) -> np.ndarray:
        sorter = np.argsort(x)
        sorted_vals = x[sorter]
        different = np.concatenate([[True], sorted_vals[1:] != sorted_vals[:-1], [True]])
        diff_idx = np.flatnonzero(different)
        counts = np.diff(diff_idx)
        avg_ranks = diff_idx[:-1] + (counts - 1) / 2.0 + 1.0
        ranks = np.empty(len(x), dtype=np.float64)
        ranks[sorter] = np.repeat(avg_ranks, counts)
        return ranks

    prev_rank_vals = _average_rank(prev_vals_arr)
    curr_rank_vals = _average_rank(curr_vals_arr)

    rho = np.corrcoef(prev_rank_vals, curr_rank_vals)[0, 1]
    if np.isnan(rho):
        rho = 0.0
    return float(1 - abs(rho))


def compute_atr(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    n: int = 14,
) -> np.ndarray:
    """
    计算 ATR (Average True Range)，Wilder's smoothing。

    Args:
        high/low/close: OHLC 序列
        n: 平滑周期

    Returns:
        ATR 序列, shape 与输入相同（前 n 个元素为 NaN，首个有效值位于索引 n）
    """
    high = np.asarray(high, dtype=np.float64)
    low = np.asarray(low, dtype=np.float64)
    close = np.asarray(close, dtype=np.float64)

    if high.ndim != 1 or low.ndim != 1 or close.ndim != 1:
        raise ValueError("high/low/close must be 1-D arrays")
    if len(high) != len(low) or len(high) != len(close):
        raise ValueError("high/low/close must have same length")
    if n <= 0:
        raise ValueError(f"n must be > 0, got {n}")

    length = len(high)
    if length < n + 1:
        # 对齐 C++：数据不足时返回全 NaN（而非崩溃）
        return np.full(length, np.nan, dtype=np.float64)
    tr = np.maximum(
        high[1:] - low[1:],
        np.maximum(
            np.abs(high[1:] - close[:-1]),
            np.abs(low[1:] - close[:-1]),
        ),
    )

    # Wilder's smoothing
    atr = np.full(len(tr) + 1, np.nan, dtype=np.float64)
    atr[n] = np.mean(tr[:n])
    for i in range(n + 1, len(tr) + 1):
        atr[i] = (atr[i - 1] * (n - 1) + tr[i - 1]) / n
    return atr

--- tests/test_dtw.py ---
# -*- coding: utf-8 -*-
"""DTW 模块测试 — 与原始 V3.3.py 实现交叉验证
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> v2 新增: NaN 边界测试 + cosine 阈值测试 (GPT-5.5 完备性审查 P1)"""


import sys
import os
import numpy as np
import pytest

# 添加 src 到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.dtw import (
    standardize_returns,
    cosine_similarity,
    dtw_distance,
    dtw_distance_batch,
    generate_query_candidates,
)


class TestStandardizeReturns:
    """standardize_returns 正确性测试"""

    def test_normal_case(self):
        """正常价格序列 — 应输出零均值、单位标准差的序列"""
        prices = np.array([100.0, 101.0, 102.5, 99.8, 103.2, 105.0])
        result = standardize_returns(prices)
        assert len(result) == 5  # n-1
        assert abs(np.mean(result)) < 1e-10  # 零均值
        assert abs(np.std(result) - 1.0) < 1e-10  # 单位标准差

    def test_constant_prices(self):
        """恒定价格 — std=0 时应返回去均值（零向量）序列"""
        prices = np.array([100.0, 100.0, 100.0, 100.0])
        result = standardize_returns(prices)
        assert len(result) == 3
        assert np.allclose(result, 0.0)

    def test_short_series(self):
        """少于2个元素 — 返回零数组"""
        result = standardize_returns(np.array([100.0]))
        assert len(result) == 0

    def test_zero_price_handling(self):
        """价格为0时应被 clip 到 1e-12"""
        prices = np.array([0.0, 100.0, 200.0])
        result = standardize_returns(prices)
        assert not np.any(np.isnan(result))
        assert not np.any(np.isinf(result))

    def test_nan_in_prices(self):
        """含 NaN 的价格 — NaN 收益率应被过滤"""
        # log(0) = -inf → diff 可能产生 nan
        prices = np.array([100.0, 100.0, 100.0, 100.0, 100.0])
        # 模拟: 在实际中 standardize_returns 中 np.diff(np.log(...))
        # 对恒定价格返回全零，不会有 NaN
        result = standardize_returns(prices)
        assert len(result) == 4
        assert not np.any(np.isnan(result))

    # v2 新增: 真实 NaN 边界测试 (GPT-5.5 完备性审查 P1)
    # 2026-07-12 修订: standardize_returns 已改为窗口级非有限值检查，
    # 任一价格为 NaN/Inf 即返回空数组，因此以下测试改为验证新契约。
    def test_nan_value_in_array(self):
        """数组中含 np.nan — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([100.0, np.nan, 101.0]))
        assert len(result) == 0

    def test_all_nan(self):
        """全 NaN — 窗口级检查应返回空数组"""
        result = standardize_returns(np.array([np.nan, np.nan]))
        assert len(result) == 0

    def test_zero_then_valid(self):
        """价格为0后被clip — 验证clip不产生NaN"""
        result = standardize_returns(np.array([0.0, 50.0, 100.0]))
        assert len(result) == 2
        assert not np.any(np.isnan(result))


class TestCosineSimilarity:
    """cosine_similarity 正确性测试"""

    def test_identical_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, x) == pytest.approx(1.0)

    def test_opposite_vectors(self):
        x = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, -x) == pytest.approx(-1.0)

    def test_orthogonal_vectors(self):
        x = np.array([1.0, 0.0, 0.0])
        y = np.array([0.0, 1.0, 0.0])
        assert cosine_similarity(x, y) == pytest.approx(0.0)

    def test_zero_vector(self):
        x = np.array([0.0, 0.0, 0.0])
        y = np.array([1.0, 2.0, 3.0])
        assert cosine_similarity(x, y) == 0.0
        assert cosine_similarity(y, x) == 0.0

    def test_near_zero_norm(self):
        """极小的 norm 应安全返回 0"""
        x = np.array([1e-13, 1e-13])
        y = np.array([1.0, 2.0])
        assert cosine_similarity(x, y) == 0.0

    # v2 新增: 阈值边界测试 (GPT-5.5 完备性审查 P1)
    def test_exactly_at_threshold(self):
        """norm 恰好等于 1e-12 — 不应返回 0（原逻辑用 < 而非 <=）"""
        x = np.array([1e-12, 0.0])
        y = np.array([1.0, 0.0])
        # norm_x = 1e-12, 不小于 1e-12 → 进入 dot/norm 计算
        result = cosine_similarity(x, y)
        assert result == pytest.approx(1.0)  # 方向完全一致


class TestDTWDistance:
    """DTW 距离正确性测试"""

    def test_identical_sequences(self):
        """相同序列的 DTW 距离应为 0"""
        x = np.array([0.1, 0.2, -0.1, 0.05, 0.0] * 4)  # L=20
        d = dtw_distance(x, x, window=5)
        assert d == pytest.approx(0.0, abs=1e-12)

    def test_same_length_sequences(self):
        """等长序列的基本 DTW 计算"""
        x = np.array([1.0, 2.0, 3.0, 2.0, 1.0])
        y = np.array([1.0, 2.0, 2.0, 3.0, 1.0])
        d = dtw_distance(x, y, window=5)
        assert d > 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_different_length_sequences(self):
        """不同长度序列"""
        x = np.array([0.1, -0.2, 0.3] * 5)   # L=15
        y = np.array([0.1, -0.2, 0.3] * 7)   # L=21
        d = dtw_distance(x, y, window=5)
        assert d >= 0
        assert not np.isnan(d)
        assert not np.isinf(d)

    def test_window_constraint(self):
        """band 约束应限制搜索范围"""
        x = np.random.randn(20)
        y = np.random.randn(20)
        d_narrow = dtw_distance(x, y, window=2)
        d_wide = dtw_distance(x, y, window=10)
        # 窄 band 距离应 ≥ 宽 band（因为搜索空间更受限）
        assert d_narrow >= d_wide - 1e-12

    def test_empty_input(self):
        """空序列应返回 inf"""
        assert dtw_distance(np.array([]), np.array([1.0, 2.0])) == np.inf
        assert dtw_distance(np.array([1.0, 2.0]), np.array([])) == np.inf

    def test_single_element(self):
        """单元素序列"""
        d = dtw_distance(np.array([0.5]), np.array([0.5]))
        assert d == pytest.approx(0.0, abs=1e-12)


class TestDTWDistanceBatch:
    """批量 DTW 测试"""

    def test_basic_batch(self):
        query = np.random.randn(20)
        candidates = np.random.randn(100, 20)
        distances = dtw_distance_batch(query, candidates, window=5)
        assert len(distances) == 100
        assert np.all(distances >= 0)

    def test_top_k(self):
        query = np.random.randn(20)
        candidates = np.random.randn(50, 20)
        idx, dists = dtw_distance_batch(query, candidates, window=5, top_k=10)
        assert len(idx) == 10
        assert len(dists) == 10
        # 确认排序
        assert np.all(np.diff(dists) >= 0)

    def test_consistency_with_single(self):
        """批量结果应与逐个调用一致"""
        query = np.random.randn(20)
        candidates = np.random.randn(30, 20)
        batch_dists = dtw_distance_batch(query, candidates, window=5)
        single_dists = np.array([dtw_distance(query, c, window=5) for c in candidates])
        assert np.allclose(batch_dists, single_dists)

    def test_empty_candidates(self):
        result = dtw_distance_batch(np.array([1.0]), np.empty((0, 1)))
        assert len(result) == 0

    def test_mismatched_lengths(self):
        with pytest.raises(ValueError):
            dtw_distance_batch(
                np.array([1.0, 2.0]),
                np.random.randn(10, 5),  # 列数不匹配
            )


class TestGenerateQueryCandidates:
    """查询/候选窗口生成测试"""

    def test_basic_generation(self):
        prices = np.sin(np.linspace(0, 10 * np.pi, 500)) + 10.0
        T_idx = 400
        q, cands, ends = generate_query_candidates(prices, T_idx, L_query=20)
        assert len(q) == 20
        assert cands.shape[1] == 20
        assert cands.shape[0] >= 300  # ~380 candidates
        # 前视偏差防护: 所有候选窗口结束索引 <= T_idx - L_query (=380)
        assert np.all(ends <= T_idx - 20)

    def test_insufficient_data(self):
        prices = np.array([100.0] * 10)
        with pytest.raises(ValueError):
            generate_query_candidates(prices, T_idx=5, L_query=20)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

--- tests/test_pattern_match.py ---
# -*- coding: utf-8 -*-
"""形态匹配引擎测试 — 含 GPT-5.5 完备性审查要求的 F12-F15 固定样例
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 审查输入: GPT-5.5 via Codex CLI (F12-F15 固定样例规格)"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.pattern_match import (
    pattern_match_single,
    compute_pattern_features,
    extract_morph_features,
)


def _generate_random_walk(n_days: int, start_price: float = 100.0) -> np.ndarray:
    """生成随机游走价格序列用于集成测试"""
    np.random.seed(42)
    returns = np.random.randn(n_days) * 0.02
    prices = start_price * np.cumprod(1 + returns)
    return np.asarray(prices, dtype=np.float64)


class TestPatternMatchSingle:
    """pattern_match_single 集成测试"""

    def test_insufficient_data_short_prices(self):
        """价格序列太短"""
        prices = np.array([100.0] * 10)
        result = pattern_match_single(prices, T_idx=5)
        assert result is None

    def test_insufficient_data_small_T_idx(self):
        """T_idx 太小（不足 L_query + M_forward + 10）"""
        prices = _generate_random_walk(100)
        result = pattern_match_single(prices, T_idx=30)
        assert result is None

    def test_basic_extraction(self):
        """基本提取 — 应返回15维非空特征"""
        prices = _generate_random_walk(600)
        T_idx = 500
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        assert len(result) == 15
        # 所有值应为有限数值
        for key, val in result.items():
            assert isinstance(val, (float, int, np.integer)), f"{key} 类型异常: {type(val)}"
            assert np.isfinite(float(val)), f"{key} = {val} 不是有限值"

    def test_no_query_window_leakage(self):
        """前视偏差防护: 所有匹配片段的未来收益端点 < T_idx"""
        prices = _generate_random_walk(800)
        T_idx = 700
        result = pattern_match_single(prices, T_idx)
        assert result is not None
        # 函数内部已保证 fut_end < T_idx，这里验证返回值合理性
        assert -1.0 <= result["avg_future_ret"] <= 1.0

    def test_returns_consistent_shape(self):
        """多次调用应返回一致的特征键集合"""
        prices = _generate_random_walk(600)
        keys = None
        for T_idx in [400, 450, 500]:
            r = pattern_match_single(prices, T_idx)
            if r is None:
                continue
            if keys is None:
                keys = set(r.keys())
            else:
                assert set(r.keys()) == keys

    def test_cos_prefilter_top_effect(self):
        """cos_prefilter_top 参数应影响结果（不同 top 值可能产生不同特征）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx, cos_prefilter_top=50)
        r2 = pattern_match_single(prices, T_idx, cos_prefilter_top=200)
        # 两者都不应为 None（如果数据足够）
        assert r1 is not None
        assert r2 is not None
        # 注意: 不同 top-k 可能产生不同特征值（因为 sigma_fast 也变了）
        # 这里只验证两者都有效

    def test_deterministic_output(self):
        """相同输入应产生相同输出（无随机性）"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = pattern_match_single(prices, T_idx)
        assert r1 is not None
        assert r2 is not None
        for key in r1:
            assert r1[key] == pytest.approx(r2[key])


class TestComputePatternFeatures:
    """compute_pattern_features 单元测试 — 固定输入验证"""

    def test_f1_f5_similarity_features(self):
        """F1-F5: 相似度特征 — 固定输入验证"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.3, 0.1])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01, 0.01])
        top_end_indices = np.array([100, 200, 300, 400, 500])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=750,
        )
        assert result["top1_sim"] == 0.9
        assert result["top5_avg_sim"] == pytest.approx(0.5)  # mean of 5
        assert result["sim_decay"] == pytest.approx(0.4)     # 0.9-0.5
        assert result["sim_variance"] > 0                    # 应有方差
        assert result["match_distance_ratio"] == pytest.approx(0.4 / 0.9)

    def test_f6_f11_future_ret_features(self):
        """F6-F11: 后续表现特征"""
        top_scores = np.array([0.9, 0.7, 0.5])
        top_future_rets = np.array([0.06, -0.03, 0.02])
        top_end_indices = np.array([100, 200, 300])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)

        assert result["avg_future_ret"] == pytest.approx(np.mean([0.06, -0.03, 0.02]))
        # weighted: (0.9*0.06 + 0.7*(-0.03) + 0.5*0.02) / (0.9+0.7+0.5) = (0.054-0.021+0.01)/2.1
        assert result["weighted_future_ret"] == pytest.approx(0.043 / 2.1)
        assert result["median_future_ret"] == 0.02
        assert result["ret_sign_consistency"] == pytest.approx(2 / 3)  # 2 positive
        assert result["best_match_ret"] == 0.06
        assert result["max_dd_in_matches"] == 0.03  # max(0, -(-0.03)) = 0.03

    # ═══════════════════════════════════════════════════════════════
    # v2: GPT-5.5 完备性审查 P0 — F12-F15 固定样例
    # ═══════════════════════════════════════════════════════════════

    def test_f12_time_span(self):
        """F12: 匹配时间跨度 — max_index - min_index"""
        top_scores = np.array([0.9, 0.7, 0.5, 0.4])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_time_span"] == 120.0  # 220 - 100
        assert result["match_time_span_ratio"] == pytest.approx(120 / 750)

    def test_f13_time_span_ratio(self):
        """F13: 时间跨度比率 — (max-min)/T_back"""
        top_scores = np.array([0.9, 0.7])
        top_future_rets = np.array([0.05, -0.02])
        # span=500, T_back=1000 → ratio=0.5
        top_end_indices = np.array([100, 600])
        result = compute_pattern_features(
            top_scores, top_future_rets, top_end_indices, T_back=1000,
        )
        assert result["match_time_span_ratio"] == 0.5

    def test_f14_cluster_ratio(self):
        """F14: 聚类比率 — 60日窗口内最大匹配数/K"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        # indices sorted: [100, 120, 160, 220]
        # searchsorted(x+60, side="right") 行为:
        #   i=0: searchsorted(160, right) → 3 (160插入到现有160之后) → 3-0=3
        #   i=1: searchsorted(180, right) → 2 → 2-1=1
        #   i=2: searchsorted(220, right) → 4 (220插入到现有220之后) → 4-2=2
        #   i=3: searchsorted(280, right) → 4 → 4-3=1
        # max_in_window = 3, ratio = 3/4 = 0.75
        top_end_indices = np.array([100, 120, 160, 220])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["match_cluster_ratio"] == pytest.approx(3 / 4)  # 3/4=0.75

    def test_f15_n_matches_above_thresh(self):
        """F15: 高于0.8阈值的匹配数 — 严格 > 0.8"""
        top_scores = np.array([0.81, 0.80, 0.79, 0.90])
        top_future_rets = np.array([0.05, -0.02, 0.03, -0.01])
        top_end_indices = np.array([100, 200, 300, 400])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        # 0.81>0.8 ✓, 0.80>0.8 ✗ (不严格大于), 0.79 ✗, 0.90 ✓
        assert result["n_matches_above_thresh"] == 2

    def test_f15_boundary_exactly_08(self):
        """F15: 恰好等于0.8不计入（> 0.8，非 >= 0.8）"""
        top_scores = np.array([0.80, 0.80])
        top_future_rets = np.array([0.05, -0.02])
        top_end_indices = np.array([100, 200])
        result = compute_pattern_features(top_scores, top_future_rets, top_end_indices)
        assert result["n_matches_above_thresh"] == 0


class TestExtractMorphFeatures:
    """extract_morph_features 便捷接口测试"""

    def test_alias(self):
        """extract_morph_features 应与 pattern_match_single 结果一致"""
        prices = _generate_random_walk(600)
        T_idx = 500
        r1 = pattern_match_single(prices, T_idx)
        r2 = extract_morph_features(prices, T_idx)
        assert (r1 is None) == (r2 is None)
        if r1 is not None:
            for key in r1:
                assert r1[key] == pytest.approx(r2[key])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

--- tests/test_technical.py ---
# -*- coding: utf-8 -*-
"""技术指标模块测试
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build", "Release"))

from core.technical import compute_adx, compute_sector_rotation, compute_atr


class TestComputeADX:
    """ADX 计算正确性测试"""

    def test_insufficient_data(self):
        """数据不足时返回中性值 25.0"""
        high = np.random.randn(20) + 100
        low = high - 2
        close = (high + low) / 2
        # n=14, 需要 n+16=30 个元素
        result = compute_adx(high, low, close, n=14)
        assert result == 25.0

    def test_flat_market(self):
        """无趋势市场 — ADX 应接近 0"""
        n_days = 100
        high = np.ones(n_days) * 100 + 0.01 * np.random.randn(n_days)
        low = np.ones(n_days) * 98 + 0.01 * np.random.randn(n_days)
        close = np.ones(n_days) * 99 + 0.01 * np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert result >= 0
        assert result <= 100

    def test_strong_trend(self):
        """强趋势市场 — ADX 应较高"""
        n_days = 200
        trend = np.linspace(100, 200, n_days)
        noise = np.random.randn(n_days) * 0.5
        high = trend + noise + 2
        low = trend + noise - 2
        close = trend + noise
        result = compute_adx(high, low, close, n=14)
        # 强趋势下 ADX 通常 > 20
        assert result > 15

    def test_output_range(self):
        """ADX 值应在 [0, 100] 范围内"""
        n_days = 150
        high = 100 + np.cumsum(np.random.randn(n_days))
        low = high - 5 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days)
        result = compute_adx(high, low, close, n=14)
        assert 0 <= result <= 100


class TestComputeSectorRotation:
    """行业轮动速度测试"""

    def test_no_rotation(self):
        """排名完全不变 — 轮动速度应为 0"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01}
        curr = {"A": 0.08, "B": 0.03, "C": 0.01, "D": -0.02}
        # 排名: A>B>C>D 不变
        result = compute_sector_rotation(prev, curr)
        assert result == pytest.approx(0.0, abs=0.01)

    def test_full_rotation(self):
        """排名完全无关（随机轮动）— 轮动速度应接近 1"""
        # 用6个行业，前后期排名完全正交
        prev = {"A": 0.60, "B": 0.50, "C": 0.40, "D": 0.30, "E": 0.20, "F": 0.10}
        curr = {"A": 0.10, "B": 0.60, "C": 0.05, "D": 0.50, "E": 0.03, "F": 0.40}
        # prev rank: A(0)B(1)C(2)D(3)E(4)F(5)
        # curr rank: B(0)D(1)F(2)A(3)C(4)E(5)
        # 这是大幅重新洗牌，ρ 应 < 0.5
        result = compute_sector_rotation(prev, curr)
        assert result > 0.5  # 高轮动 (1-|ρ| > 0.5)

    def test_partial_rotation(self):
        """部分轮动"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "E": 0.08}
        curr = {"A": 0.01, "B": 0.08, "C": 0.05, "D": -0.03, "E": 0.10}
        result = compute_sector_rotation(prev, curr)
        assert 0.0 < result < 1.0

    def test_insufficient_sectors(self):
        """行业数不足 — 返回 0"""
        prev = {"A": 0.10, "B": 0.05}
        curr = {"A": -0.02, "B": 0.08}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert result == 0.0

    def test_mismatched_symbols(self):
        """部分 symbol 不重叠 — 仅用公共部分"""
        prev = {"A": 0.10, "B": 0.05, "C": 0.02, "D": -0.01, "X": 0.03}
        curr = {"A": -0.02, "B": 0.08, "C": 0.01, "D": 0.03, "Y": -0.05}
        result = compute_sector_rotation(prev, curr, min_sectors=4)
        assert 0.0 <= result <= 1.0  # 仅用 A/B/C/D


class TestComputeATR:
    """ATR 计算测试"""

    def test_basic_atr(self):
        n_days = 50
        high = 100 + np.cumsum(np.random.randn(n_days) * 0.5)
        low = high - 2 - np.abs(np.random.randn(n_days))
        close = (high + low) / 2 + np.random.randn(n_days) * 0.1
        atr = compute_atr(high, low, close, n=14)
        assert len(atr) == n_days
        assert np.all(np.isnan(atr[:14]))  # 前 n 天为 NaN
        assert np.all(atr[14:] > 0)  # ATR 必须为正


def test_compute_atr_mismatched_lengths():
    """high/low/close 长度不一致时应抛异常"""
    import etf_core
    high = np.random.uniform(10, 20, 100)
    low = np.random.uniform(8, 10, 99)  # 比 high 少 1
    close = np.random.uniform(10, 20, 100)
    try:
        etf_core.compute_atr(high, low, close)
        assert False, "长度不一致应抛异常"
    except Exception as e:
        assert "length" in str(e).lower() or "same" in str(e).lower()


def test_compute_atr_short_array():
    """短于 n+1 的数组应返回全 NaN"""
    import etf_core
    n = 14
    short_len = n  # 等于 n，不足 n+1
    high = np.random.uniform(10, 20, short_len)
    low = np.random.uniform(8, 10, short_len)
    close = np.random.uniform(10, 20, short_len)
    result = etf_core.compute_atr(high, low, close, n)
    assert len(result) == short_len
    assert np.all(np.isnan(result)), f"短数组(长度={short_len})应返回全 NaN"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Path src -Recurse -File -Include *.py | Select-String -Pattern '"'import etf_core|from etf_core|importlib|sys.path' -Encoding UTF8 | ForEach-Object { '{0}:{1}: {2}' -f "'$_.Path,$_.LineNumber,$_.Line.Trim() }; Write-Output '"'--- test headers ---'; foreach ("'$f in Get-ChildItem tests -File -Filter '"'*.py') { Write-Output \"--- "'$($f.Name) ---"; Get-Content -Encoding UTF8 $f.FullName -TotalCount 30 }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 185ms:
--- test headers ---
--- test_dtw.py ---
# -*- coding: utf-8 -*-
"""DTW 模块测试 — 与原始 V3.3.py 实现交叉验证
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> v2 新增: NaN 边界测试 + cosine 阈值测试 (GPT-5.5 完备性审查 P1)"""


import sys
import os
import numpy as np
import pytest

# 添加 src 到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.dtw import (
    standardize_returns,
    cosine_similarity,
    dtw_distance,
    dtw_distance_batch,
    generate_query_candidates,
)


class TestStandardizeReturns:
    """standardize_returns 正确性测试"""

    def test_normal_case(self):
        """正常价格序列 — 应输出零均值、单位标准差的序列"""
        prices = np.array([100.0, 101.0, 102.5, 99.8, 103.2, 105.0])
        result = standardize_returns(prices)
--- test_pattern_match.py ---
# -*- coding: utf-8 -*-
"""形态匹配引擎测试 — 含 GPT-5.5 完备性审查要求的 F12-F15 固定样例
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 审查输入: GPT-5.5 via Codex CLI (F12-F15 固定样例规格)"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from core.pattern_match import (
    pattern_match_single,
    compute_pattern_features,
    extract_morph_features,
)


def _generate_random_walk(n_days: int, start_price: float = 100.0) -> np.ndarray:
    """生成随机游走价格序列用于集成测试"""
    np.random.seed(42)
    returns = np.random.randn(n_days) * 0.02
    prices = start_price * np.cumprod(1 + returns)
    return np.asarray(prices, dtype=np.float64)


class TestPatternMatchSingle:
    """pattern_match_single 集成测试"""

--- test_technical.py ---
# -*- coding: utf-8 -*-
"""技术指标模块测试
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03"""

import sys
import os
import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "build", "Release"))

from core.technical import compute_adx, compute_sector_rotation, compute_atr


class TestComputeADX:
    """ADX 计算正确性测试"""

    def test_insufficient_data(self):
        """数据不足时返回中性值 25.0"""
        high = np.random.randn(20) + 100
        low = high - 2
        close = (high + low) / 2
        # n=14, 需要 n+16=30 个元素
        result = compute_adx(high, low, close, n=14)
        assert result == 25.0

    def test_flat_market(self):
        """无趋势市场 — ADX 应接近 0"""
        n_days = 100

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-Content -Encoding UTF8 '"'src/core/technical.py' -TotalCount 80; Write-Output '--- definitions ---'; Select-String -Path 'src/core/technical.py' -Pattern '"'^def compute_|etf_core'"' -Encoding UTF8 | ForEach-Object { '{0}: {1}' -f "'$_.LineNumber,$_.Line.Trim() }; Write-Output '"'--- pyproject ---'; Get-Content -Raw -Encoding UTF8 'pyproject.toml'" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 175ms:
# -*- coding: utf-8 -*-
"""
技术指标计算模块
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03
> 来源: V3.3.py 行 757-795, 801-836, 1003-1032
=================
从 形态匹配ETF组合策略_V3.3.py 提取，零掘金依赖。

模块内容:
  - compute_adx:          ADX (Average Directional Index) — Wilder's smoothing
  - compute_sector_rotation: 行业轮动速度 (Spearman rank correlation)

原始来源:
  V3.3.py 行 757-795 (_compute_adx_from_df)
  V3.3.py 行 801-836 (_compute_sector_rotation)
  V3.3.py 行 1003-1032 (_compute_sector_rotation_historical)

算法逻辑零改动。
"""

import numpy as np
from typing import Dict


def compute_adx(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    n: int = 14,
) -> float:
    """
    从 OHLC 数组计算 ADX (Average Directional Index)。

    Args:
        high: 最高价序列, shape (n_days,)
        low:  最低价序列, shape (n_days,)
        close: 收盘价序列, shape (n_days,)
        n: 平滑周期 (默认 14)

    Returns:
        ADX 值 ∈ [0, 100]；数据不足时返回 25.0（中性值）。

    算法逻辑: 与 V3.3.py 第 757-795 行完全一致。
    """
    # 强制转换为 float64，防止整数 dtype 静默截断
    high = np.asarray(high, dtype=np.float64)
    low = np.asarray(low, dtype=np.float64)
    close = np.asarray(close, dtype=np.float64)

    if high.ndim != 1 or low.ndim != 1 or close.ndim != 1:
        raise ValueError("high/low/close must be 1-D arrays")
    if len(high) != len(low) or len(high) != len(close):
        raise ValueError("high/low/close must have same length")
    if n <= 0:
        raise ValueError(f"n must be > 0, got {n}")
    if len(high) < n + 16:
        return 25.0

    # True Range
    tr = np.maximum(
        high[1:] - low[1:],
        np.maximum(np.abs(high[1:] - close[:-1]), np.abs(low[1:] - close[:-1])),
    )

    # Directional Movement
    up = high[1:] - high[:-1]
    down = low[:-1] - low[1:]
    plus_dm = np.where((up > down) & (up > 0), up, 0)
    minus_dm = np.where((down > up) & (down > 0), down, 0)

    # Wilder's smoothing (初始值 = 简单均值，后续指数平滑)
    atr = np.zeros_like(tr)
    atr[:n] = np.mean(tr[:n])
    for i in range(n, len(tr)):
        atr[i] = (atr[i - 1] * (n - 1) + tr[i]) / n

    smoothed_plus = np.zeros_like(tr)
    smoothed_minus = np.zeros_like(tr)
    smoothed_plus[:n] = np.mean(plus_dm[:n])
    smoothed_minus[:n] = np.mean(minus_dm[:n])
--- definitions ---
25: def compute_adx(
97: def compute_sector_rotation(
149: def compute_atr(
--- pyproject ---
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
cmake.version = ">=3.20"
wheel.packages = ["src/cpp"]


exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$path = Join-Path (Get-Location) '"'.github/workflows/sanitizer.yml'; "'$content = @'"'
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Sanitizer (ASAN+UBSAN)

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  sanitizer:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8
      ASAN_OPTIONS: detect_leaks=1:halt_on_error=1
      UBSAN_OPTIONS: halt_on_error=1:print_stacktrace=1
      SANITIZER_FLAGS: -fsanitize=address,undefined -fno-omit-frame-pointer

    steps:
      - uses: actions/checkout@v4

      - name: Install Linux build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install numpy pybind11 pytest

      - name: Configure sanitized build
        run: |
          python_path=\""'$(python -c '"'import sys; print(sys.executable)')\"
          cmake -S . -B build-sanitizer \\
            -DPython_EXECUTABLE=\""'$python_path" '"\\
            -DCMAKE_BUILD_TYPE=Debug \\
            -DCMAKE_CXX_FLAGS=\""'$SANITIZER_FLAGS" '"\\
            -DCMAKE_MODULE_LINKER_FLAGS=\"-fsanitize=address,undefined\" \\
            -DCMAKE_SHARED_LINKER_FLAGS=\"-fsanitize=address,undefined\"

      - name: Build with ASAN and UBSAN
        run: cmake --build build-sanitizer --config Debug --parallel

      - name: Run existing Python tests under sanitizers
        run: |
          export LD_PRELOAD=\""'$(g++ -print-file-name=libasan.so)"
          export PYTHONPATH="$GITHUB_WORKSPACE/build-sanitizer${PYTHONPATH:+:$PYTHONPATH}"
          python -m pytest tests/ -v
'"'@; [System.IO.File]::WriteAllText("'$path, $content, [System.Text.UTF8Encoding]::new($false))' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 125ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $path = '"'.github/workflows/sanitizer.yml'; "'$bytes = [System.IO.File]::ReadAllBytes((Join-Path (Get-Location) $path)); $bom = ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF); Write-Output "UTF8_BOM=$bom"; Write-Output '"'--- sanitizer.yml ---'; Get-Content -Raw -Encoding UTF8 "'$path; Write-Output '"'--- git diff -- sanitizer.yml CMakeLists.txt ci.yml ---'; git diff -- .github/workflows/sanitizer.yml CMakeLists.txt .github/workflows/ci.yml; Write-Output '--- git status --short ---'; git status --short -- .github/workflows/sanitizer.yml CMakeLists.txt .github/workflows/ci.yml" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 210ms:
UTF8_BOM=False
--- sanitizer.yml ---
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Sanitizer (ASAN+UBSAN)

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  sanitizer:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8
      ASAN_OPTIONS: detect_leaks=1:halt_on_error=1
      UBSAN_OPTIONS: halt_on_error=1:print_stacktrace=1
      SANITIZER_FLAGS: -fsanitize=address,undefined -fno-omit-frame-pointer

    steps:
      - uses: actions/checkout@v4

      - name: Install Linux build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install numpy pybind11 pytest

      - name: Configure sanitized build
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -S . -B build-sanitizer \
            -DPython_EXECUTABLE="$python_path" \
            -DCMAKE_BUILD_TYPE=Debug \
            -DCMAKE_CXX_FLAGS="$SANITIZER_FLAGS" \
            -DCMAKE_MODULE_LINKER_FLAGS="-fsanitize=address,undefined" \
            -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address,undefined"

      - name: Build with ASAN and UBSAN
        run: cmake --build build-sanitizer --config Debug --parallel

      - name: Run existing Python tests under sanitizers
        run: |
          export LD_PRELOAD="$(g++ -print-file-name=libasan.so)"
          export PYTHONPATH="$GITHUB_WORKSPACE/build-sanitizer${PYTHONPATH:+:$PYTHONPATH}"
          python -m pytest tests/ -v
--- git diff -- sanitizer.yml CMakeLists.txt ci.yml ---
diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
index 1618ede..5206782 100644
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ -1,3 +1,4 @@
+# GPT-5.6-Sol (via Codex CLI), 2026-07-17
 name: CI
 
 on:
@@ -8,7 +9,18 @@ on:
 
 jobs:
   build-and-test:
-    runs-on: windows-latest
+    strategy:
+      fail-fast: false
+      matrix:
+        os:
+          - windows-latest
+          - ubuntu-latest
+          - macos-latest
+
+    runs-on: ${{ matrix.os }}
+
+    env:
+      PYTHONIOENCODING: utf-8
 
     steps:
       - uses: actions/checkout@v4
@@ -19,16 +31,33 @@ jobs:
         with:
           python-version: '3.12'
 
+      - name: Install Linux build tools
+        if: runner.os == 'Linux'
+        run: |
+          sudo apt-get update
+          sudo apt-get install -y g++ cmake
+
+      - name: Install macOS build tools
+        if: runner.os == 'macOS'
+        run: brew install cmake
+
       - name: Install Python dependencies
         run: |
           python -m pip install --upgrade pip
           pip install numpy pybind11 pytest
 
       - name: Configure CMake
+        if: runner.os == 'Windows'
         run: |
           $pythonPath = (Get-Command python).Source
           cmake -B build -DPython_EXECUTABLE="$pythonPath" -DCMAKE_BUILD_TYPE=Release
 
+      - name: Configure CMake (Linux/macOS)
+        if: runner.os != 'Windows'
+        run: |
+          python_path="$(python -c 'import sys; print(sys.executable)')"
+          cmake -B build -DPython_EXECUTABLE="$python_path" -DCMAKE_BUILD_TYPE=Release
+
       - name: Build
         run: cmake --build build --config Release
 
--- git status --short ---
 M .github/workflows/ci.yml
?? .github/workflows/sanitizer.yml
warning: in the working copy of '.github/workflows/ci.yml', LF will be replaced by CRLF the next time Git touches it

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command '$path = Join-Path (Get-Location) '"'.github/workflows/sanitizer.yml'; "'$encoding = [System.Text.UTF8Encoding]::new($false); $content = [System.IO.File]::ReadAllText($path, $encoding); $old = @'"'
          cmake -S . -B build-sanitizer \\
            -DPython_EXECUTABLE=\""'$python_path" '"\\
'@; "'$new = @'"'
          cmake -S . -B build-sanitizer \\
            -DCMAKE_CXX_COMPILER=g++ \\
            -DPython_EXECUTABLE=\""'$python_path" '"\\
'@; if (-not "'$content.Contains($old)) { throw '"'Expected configure block not found.' }; "'$content = $content.Replace($old, $new); [System.IO.File]::WriteAllText($path, $content, $encoding)' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 137ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-Content -Raw -Encoding UTF8 '"'.github/workflows/sanitizer.yml'; Write-Output '--- status ---'; git status --short -- '.github/workflows/sanitizer.yml' 'CMakeLists.txt' '.github/workflows/ci.yml'" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 185ms:
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Sanitizer (ASAN+UBSAN)

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  sanitizer:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8
      ASAN_OPTIONS: detect_leaks=1:halt_on_error=1
      UBSAN_OPTIONS: halt_on_error=1:print_stacktrace=1
      SANITIZER_FLAGS: -fsanitize=address,undefined -fno-omit-frame-pointer

    steps:
      - uses: actions/checkout@v4

      - name: Install Linux build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install numpy pybind11 pytest

      - name: Configure sanitized build
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -S . -B build-sanitizer \
            -DCMAKE_CXX_COMPILER=g++ \
            -DPython_EXECUTABLE="$python_path" \
            -DCMAKE_BUILD_TYPE=Debug \
            -DCMAKE_CXX_FLAGS="$SANITIZER_FLAGS" \
            -DCMAKE_MODULE_LINKER_FLAGS="-fsanitize=address,undefined" \
            -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address,undefined"

      - name: Build with ASAN and UBSAN
        run: cmake --build build-sanitizer --config Debug --parallel

      - name: Run existing Python tests under sanitizers
        run: |
          export LD_PRELOAD="$(g++ -print-file-name=libasan.so)"
          export PYTHONPATH="$GITHUB_WORKSPACE/build-sanitizer${PYTHONPATH:+:$PYTHONPATH}"
          python -m pytest tests/ -v
--- status ---
 M .github/workflows/ci.yml
?? .github/workflows/sanitizer.yml

codex
Created **`.github/workflows/sanitizer.yml`**:

```yaml
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Sanitizer (ASAN+UBSAN)

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  sanitizer:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8
      ASAN_OPTIONS: detect_leaks=1:halt_on_error=1
      UBSAN_OPTIONS: halt_on_error=1:print_stacktrace=1
      SANITIZER_FLAGS: -fsanitize=address,undefined -fno-omit-frame-pointer

    steps:
      - uses: actions/checkout@v4

      - name: Install Linux build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install numpy pybind11 pytest

      - name: Configure sanitized build
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -S . -B build-sanitizer \
            -DCMAKE_CXX_COMPILER=g++ \
            -DPython_EXECUTABLE="$python_path" \
            -DCMAKE_BUILD_TYPE=Debug \
            -DCMAKE_CXX_FLAGS="$SANITIZER_FLAGS" \
            -DCMAKE_MODULE_LINKER_FLAGS="-fsanitize=address,undefined" \
            -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address,undefined"

      - name: Build with ASAN and UBSAN
        run: cmake --build build-sanitizer --config Debug --parallel

      - name: Run existing Python tests under sanitizers
        run: |
          export LD_PRELOAD="$(g++ -print-file-name=libasan.so)"
          export PYTHONPATH="$GITHUB_WORKSPACE/build-sanitizer${PYTHONPATH:+:$PYTHONPATH}"
          python -m pytest tests/ -v
```

`CMakeLists.txt` was left unchanged because the sanitizer flags are supplied directly by the workflow. The existing `.github/workflows/ci.yml` was not modified. No tests or CI workflows were run.
tokens used
61,687
Created **`.github/workflows/sanitizer.yml`**:

```yaml
# GPT-5.6-Sol (via Codex CLI), 2026-07-17
name: Sanitizer (ASAN+UBSAN)

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  sanitizer:
    runs-on: ubuntu-latest

    env:
      PYTHONIOENCODING: utf-8
      ASAN_OPTIONS: detect_leaks=1:halt_on_error=1
      UBSAN_OPTIONS: halt_on_error=1:print_stacktrace=1
      SANITIZER_FLAGS: -fsanitize=address,undefined -fno-omit-frame-pointer

    steps:
      - uses: actions/checkout@v4

      - name: Install Linux build tools
        run: |
          sudo apt-get update
          sudo apt-get install -y g++ cmake

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install numpy pybind11 pytest

      - name: Configure sanitized build
        run: |
          python_path="$(python -c 'import sys; print(sys.executable)')"
          cmake -S . -B build-sanitizer \
            -DCMAKE_CXX_COMPILER=g++ \
            -DPython_EXECUTABLE="$python_path" \
            -DCMAKE_BUILD_TYPE=Debug \
            -DCMAKE_CXX_FLAGS="$SANITIZER_FLAGS" \
            -DCMAKE_MODULE_LINKER_FLAGS="-fsanitize=address,undefined" \
            -DCMAKE_SHARED_LINKER_FLAGS="-fsanitize=address,undefined"

      - name: Build with ASAN and UBSAN
        run: cmake --build build-sanitizer --config Debug --parallel

      - name: Run existing Python tests under sanitizers
        run: |
          export LD_PRELOAD="$(g++ -print-file-name=libasan.so)"
          export PYTHONPATH="$GITHUB_WORKSPACE/build-sanitizer${PYTHONPATH:+:$PYTHONPATH}"
          python -m pytest tests/ -v
```

`CMakeLists.txt` was left unchanged because the sanitizer flags are supplied directly by the workflow. The existing `.github/workflows/ci.yml` was not modified. No tests or CI workflows were run.
