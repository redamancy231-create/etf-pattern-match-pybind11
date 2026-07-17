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
session id: 019f6f94-2910-7923-913d-07ae9bffb8db
--------
user
You are adding a minimal usage example for the "etf-pattern-match-pybind11" project at: E:/workspace/projects/形态匹配ETF策略-pybind11

Read the existing code to understand the API (especially the C++ bindings in src/cpp/etf_core.cpp PYBIND11_MODULE section and the .pyi stub), then create a quickstart example.

## Task: Create `examples/quickstart.py`

A 15-25 line Python script that demonstrates the core workflow for a user who just ran `pip install`:

### What the script should do

1. Import `etf_core`
2. Generate a small random price series (e.g., `np.random.randn(100).cumsum() + 100`)
3. Call `dtw_distance` with two sub-series
4. Call `cosine_similarity` with two feature vectors
5. Call `pattern_match_single` with a price series and a T_idx
6. Call `pattern_match_batch` with a price series and multiple T_idx values
7. Print results with labels (e.g., "DTW distance: 12.34")
8. Include a comment at top: "# Quickstart example for etf_core — pip install etf-pattern-match-pybind11 && python examples/quickstart.py"

### Requirements

- No external data files needed — generate random data inline
- Use `numpy` for data generation
- Include the provenance comment: "# Provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17"
- Create `examples/` directory if it doesn't exist
- PEP 8, UTF-8 encoding

### What NOT to do

- Don't create a notebook
- Don't import from src/ (only from installed etf_core package)
- Don't run the script
- Don't require external data files

### Output

Write the complete new file.

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
2026-07-17T10:17:09.428360Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
2026-07-17T10:17:19.785142Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Force' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 208ms:


    目录: E:\workspace\projects\形态匹配ETF策略-pybind11


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d--h--         2026/7/17     18:13                .git                                                                 
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



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Path .. -Filter AGENTS.md -Recurse -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName; Get-ChildItem -Path . -Recurse -File | Where-Object { $_.Name -eq '"'etf_core.cpp' -or "'$_.Extension -eq '"'.pyi' } | Select-Object FullName,Length" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 385ms:

FullName                                                          Length
--------                                                          ------
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\etf_core.cpp      44567
E:\workspace\projects\形态匹配ETF策略-pybind11\src\cpp\pyi\etf_core.pyi   3408



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $stub = Get-Content -Raw -Encoding UTF8 '"'src\\cpp\\pyi\\etf_core.pyi'; "'$cpp = Get-Content -Raw -Encoding UTF8 '"'src\\cpp\\etf_core.cpp'; '--- etf_core.pyi ---'; "'$stub; '"'--- PYBIND11_MODULE section ---'; "'$start = $cpp.IndexOf('"'PYBIND11_MODULE'); if ("'$start -ge 0) { $cpp.Substring($start) }' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 146ms:
--- etf_core.pyi ---
"""Type stubs for etf_core — C++ accelerated ETF pattern matching module."""

import numpy as np
from typing import Dict, Optional

# 模块常量：15 维特征名（顺序与 pattern_match_batch 的 features_X15 列一致）
FEATURE_KEYS: tuple[str, ...]


def standardize_returns(price_series: np.ndarray) -> np.ndarray:
    """
    计算标准化收益率序列: (rets - mean) / std.

    Args:
        price_series: 1-D float64 array, n >= 2.

    Returns:
        1-D float64 array, length n-1.
    """
    ...


def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    """
    两向量余弦相似度 ∈ [-1, 1].
    norm < 1e-12 时返回 0.0.
    """
    ...


def dtw_distance(x: np.ndarray, y: np.ndarray, window: int = 5) -> float:
    """
    Sakoe-Chiba band DTW 距离.
    返回归一化距离: sqrt(dtw[n,m]) / (n+m).
    """
    ...


from typing import overload, Tuple

@overload
def dtw_distance_batch(
    query: np.ndarray, candidates: np.ndarray,
    window: int = 5, top_k: int = 0,
) -> np.ndarray:
    """top_k <= 0: 返回全部 distances (N,)."""
    ...

@overload
def dtw_distance_batch(
    query: np.ndarray, candidates: np.ndarray,
    window: int = 5, top_k: int = ...,
) -> Tuple[np.ndarray, np.ndarray]:
    """top_k > 0: 返回 (indices, distances) 各 (top_k,)."""
    ...


def compute_adx(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 14
) -> float:
    """
    ADX (Average Directional Index), Wilder's smoothing.
    数据不足时返回 25.0 (中性值).
    """
    ...


def compute_atr(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, n: int = 14
) -> np.ndarray:
    """
    ATR (Average True Range). 前 n 天为 NaN.
    """
    ...


def pattern_match_single(
    prices: np.ndarray,
    T_idx: int,
    k: int = 10,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
    M_forward: int = 5,
    dtw_window: int = 5,
    cos_prefilter_top: int = 50,
) -> Optional[Dict[str, float]]:
    """
    单 ETF 单时点形态匹配 → 15维特征字典.

    V3.0 余弦预筛选: 第1遍全量余弦 → 第2遍 DTW 精排.
    前视偏差防护: fut_end < T_idx 严格约束.

    Returns:
        dict with 15 keys or None.
        F1-F5:  top1_sim, top5_avg_sim, sim_decay, sim_variance, match_distance_ratio
        F6-F11: avg_future_ret, weighted_future_ret, median_future_ret,
                ret_sign_consistency, best_match_ret, max_dd_in_matches
        F12-F15: match_time_span, match_time_span_ratio, match_cluster_ratio,
                 n_matches_above_thresh
    """
    ...

def pattern_match_batch(
    prices: np.ndarray,
    t_indices: np.ndarray,
    k: int = 10,
    L_query: int = 20,
    T_back: int = 750,
    match_step: int = 1,
    M_forward: int = 5,
    dtw_window: int = 5,
    cos_prefilter_top: int = 50,
) -> tuple[np.ndarray, np.ndarray]:
    """
    批量形态匹配——同 ETF 多 T_idx。

    核心优化：候选窗口标准化收益率预计算，相邻 T_idx 共享缓存。

    Returns:
        (features_X15, valid_mask):
          - features_X15: (n_valid, 15) float64 — 仅有效样本
          - valid_mask: (n_samples,) bool
        feature_keys 已提升为模块常量 FEATURE_KEYS (15 str)。
    """
    ...

--- PYBIND11_MODULE section ---
PYBIND11_MODULE
 * >   Kimi-K2.7-Code (via Kimi Code CLI), 2026-07-03:
 * >     pattern_match_batch, cosine_similarity_vec, dtw_distance_vec,
 * >     compute_pattern_features_cpp, 预计算缓存架构, v3 修订
 * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-12:
 * >     dtw_distance_batch, 模块绑定
 *
 * 来源: 形态匹配ETF组合策略_V3.3.py
 *   - dtw_distance:         行 339-359
 *   - standardize_returns:  行 362-373
 *   - cosine_similarity:    行 376-382
 *   - _compute_adx_from_df: 行 757-795
 *   - pattern_match_single: 行 389-627 (含 V3.0 余弦预筛选)
 *   - pattern_match_batch:  新增 — 同 ETF 多 T_idx 批量形态匹配
 *
 * 工具链: MSVC 19.51 + pybind11 3.0.4 + C++20
 * 编译:   cmake -B build -DPython_EXECUTABLE=... && cmake --build build --config Release
 *
 * 审查: Kimi-K2.7-Code (魔鬼代言人) + GPT-5.5 via Codex CLI (完备性)
 *
 * v2 修订 (基于双审):
 *   - 三模块合并为一个 etf_core
 *   - GIL释放边界明确标注
 *   - py::ssize_t 索引 (MSVC兼容)
 *   - forcecast 策略处理 dtype
 *   - 浮点容差分两层 (距离 <1e-8, 得分 <1e-6)
 *   - 返回结构契约: dict key 稳定, None 语义一致
 *
 * v3 修订:
 *   - 新增 pattern_match_batch，消除同 ETF 多 T_idx 场景下的 Python 往返和重复标准化
 */

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <limits>
#include <numeric>
#include <optional>
#include <stdexcept>

namespace py = pybind11;

// ── 类型别名 (v2: forcecast 策略) ──
using ArrD  = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// ═══════════════════════════════════════════════════════════════
// 第一部分: 序列标准化 (V3.3.py 行 362-373)
// ═══════════════════════════════════════════════════════════════

std::vector<double> standardize_returns_cpp(const double* prices, py::ssize_t n) {
    if (n < 2) {
        return {};  // 返回空向量表示无效窗口
    }

    // 窗口级检查：任一价格为非有限值 → 整个窗口无效
    for (py::ssize_t i = 0; i < n; ++i) {
        if (!std::isfinite(prices[i])) {
            return {};
        }
    }

    // 计算对数收益率（所有价格已通过有限性检查，长度固定为 n-1）
    std::vector<double> rets;
    rets.reserve(n - 1);
    for (py::ssize_t i = 1; i < n; ++i) {
        double p_prev = std::max(prices[i - 1], 1e-12);
        double p_curr = std::max(prices[i], 1e-12);
        rets.push_back(std::log(p_curr / p_prev));
    }

    if (rets.empty()) {
        return {};
    }

    // 去均值
    double mean = std::accumulate(rets.begin(), rets.end(), 0.0) / rets.size();
    for (auto& r : rets) r -= mean;

    // 标准差
    double sq_sum = 0.0;
    for (auto r : rets) sq_sum += r * r;
    double std_val = std::sqrt(sq_sum / rets.size());

    if (std_val < 1e-12) {
        return rets;  // 已去均值，不再除以 std
    }

    for (auto& r : rets) r /= std_val;
    return rets;
}

// Python 绑定包装
ArrD standardize_returns(ArrD price_series) {
    auto buf = price_series.unchecked<1>();
    py::ssize_t n = buf.shape(0);
    const double* ptr = buf.data(0);

    std::vector<double> result_vec;
    {
        py::gil_scoped_release release;
        result_vec = standardize_returns_cpp(ptr, n);
    }

    py::ssize_t m = static_cast<py::ssize_t>(result_vec.size());
    ArrD result(m);
    auto res_buf = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < m; ++i) {
        res_buf(i) = result_vec[i];
    }
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第二部分: 余弦相似度 (V3.3.py 行 376-382)
// ═══════════════════════════════════════════════════════════════

double cosine_similarity(ArrD x_arr, ArrD y_arr) {
    auto x = x_arr.unchecked<1>();
    auto y = y_arr.unchecked<1>();
    py::ssize_t n = x.shape(0);

    if (n != y.shape(0)) {
        throw std::invalid_argument("x and y must have same length");
    }

    const double* xp = x.data(0);
    const double* yp = y.data(0);

    double dot, norm_x2, norm_y2;
    {
        py::gil_scoped_release release;
        dot = 0.0; norm_x2 = 0.0; norm_y2 = 0.0;
        for (py::ssize_t i = 0; i < n; ++i) {
            dot += xp[i] * yp[i];
            norm_x2 += xp[i] * xp[i];
            norm_y2 += yp[i] * yp[i];
        }
    }

    double norm_x = std::sqrt(norm_x2);
    double norm_y = std::sqrt(norm_y2);
    if (norm_x < 1e-12 || norm_y < 1e-12) {
        return 0.0;
    }
    return dot / (norm_x * norm_y);
}

// ═══════════════════════════════════════════════════════════════
// 第三部分: DTW 距离 (V3.3.py 行 339-359)
// ═══════════════════════════════════════════════════════════════

// Span版 DTW 距离（零拷贝 + 滚动双行数组，O(m) 内存）
// 供 public API 和内部批量函数共用
double dtw_distance_span(const double* x, py::ssize_t n,
                          const double* y, py::ssize_t m,
                          int window = 5) {
    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    int band = std::max(window, static_cast<int>(std::abs(n - m)));
    const double INF = std::numeric_limits<double>::infinity();

    std::vector<double> prev(m + 1, INF);
    std::vector<double> curr(m + 1, INF);
    prev[0] = 0.0;

    for (py::ssize_t i = 1; i <= n; ++i) {
        py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
        py::ssize_t j_end = std::min(m, i + band);

        for (py::ssize_t j = j_start; j <= j_end; ++j) {
            double cost = x[i - 1] - y[j - 1];
            cost *= cost;

            double pj = (std::abs((i - 1) - j) <= band) ? prev[j] : INF;
            double cj = (j > j_start) ? curr[j - 1] : INF;
            double pj1 = prev[j - 1];

            curr[j] = cost + std::min({pj, cj, pj1});
        }

        std::swap(prev, curr);
        // dtw[i][0] = INF for all i > 0（prev[0] 经 swap 可能残留 0.0）
        prev[0] = INF;
    }

    double path_len = static_cast<double>(n + m);
    return (path_len > 0) ? std::sqrt(prev[m]) / path_len : INF;
}

double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
    auto x = x_arr.unchecked<1>();
    auto y = y_arr.unchecked<1>();
    py::ssize_t n = x.shape(0);
    py::ssize_t m = y.shape(0);

    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    double result;
    {
        py::gil_scoped_release release;
        result = dtw_distance_span(x.data(0), n, y.data(0), m, window);
    }

    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第四部分: ADX 计算 (V3.3.py 行 757-795)
// ═══════════════════════════════════════════════════════════════

double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
    if (n <= 0) {
        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
    }
    auto high = high_arr.unchecked<1>();
    auto low  = low_arr.unchecked<1>();
    auto close = close_arr.unchecked<1>();
    py::ssize_t len = high.shape(0);

    if (len < n + 16) return 25.0;
    if (low.shape(0) != len || close.shape(0) != len) {
        throw std::invalid_argument("high/low/close must have same length");
    }

    double result;
    {
        py::gil_scoped_release release;

        py::ssize_t tr_len = len - 1;
        std::vector<double> tr(tr_len), plus_dm(tr_len), minus_dm(tr_len);

        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double hl = high(i + 1) - low(i + 1);
            double hc = std::abs(high(i + 1) - close(i));
            double lc = std::abs(low(i + 1) - close(i));
            tr[i] = std::max({hl, hc, lc});

            double up = high(i + 1) - high(i);
            double down = low(i) - low(i + 1);
            plus_dm[i]  = (up > down && up > 0) ? up : 0.0;
            minus_dm[i] = (down > up && down > 0) ? down : 0.0;
        }

        // Wilder's smoothing
        auto wilder_smooth = [&](const std::vector<double>& raw) {
            std::vector<double> smoothed(tr_len, 0.0);
            double init_sum = 0.0;
            for (int i = 0; i < n; ++i) init_sum += raw[i];
            // Fill first n positions with initial mean (match Python behaviour)
            double init_mean = init_sum / n;
            for (int i = 0; i < n; ++i) smoothed[i] = init_mean;
            for (py::ssize_t i = n; i < tr_len; ++i) {
                smoothed[i] = (smoothed[i - 1] * (n - 1) + raw[i]) / n;
            }
            return smoothed;
        };

        auto atr_s = wilder_smooth(tr);
        auto plus_s = wilder_smooth(plus_dm);
        auto minus_s = wilder_smooth(minus_dm);

        std::vector<double> dx(tr_len);
        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double pdi = 100.0 * plus_s[i] / (atr_s[i] + 1e-12);
            double mdi = 100.0 * minus_s[i] / (atr_s[i] + 1e-12);
            dx[i] = 100.0 * std::abs(pdi - mdi) / (pdi + mdi + 1e-12);
        }

        auto adx_s = wilder_smooth(dx);
        result = adx_s.back();
    }

    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第五部分: ATR 计算
// ═══════════════════════════════════════════════════════════════

ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
    if (n <= 0) {
        throw std::invalid_argument("n must be > 0, got " + std::to_string(n));
    }
    auto high = high_arr.unchecked<1>();
    auto low  = low_arr.unchecked<1>();
    auto close = close_arr.unchecked<1>();
    py::ssize_t len = high.shape(0);

    // v3: 输入校验 (GPT-5.5 最终审查 P0)
    if (low.shape(0) != len || close.shape(0) != len) {
        throw std::invalid_argument("high/low/close must have same length");
    }
    if (len < n + 1) {
        ArrD result(len);
        auto res = result.mutable_unchecked<1>();
        for (py::ssize_t i = 0; i < len; ++i)
            res(i) = std::numeric_limits<double>::quiet_NaN();
        return result;
    }

    const double* hp = high.data(0);
    const double* lp = low.data(0);
    const double* cp = close.data(0);

    ArrD result(len);
    auto res = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();

    {
        py::gil_scoped_release release;

        py::ssize_t tr_len = len - 1;
        std::vector<double> tr(tr_len);

        for (py::ssize_t i = 0; i < tr_len; ++i) {
            double hl = hp[i + 1] - lp[i + 1];
            double hc = std::abs(hp[i + 1] - cp[i]);
            double lc = std::abs(lp[i + 1] - cp[i]);
            tr[i] = std::max({hl, hc, lc});
        }

        double init_sum = 0.0;
        for (int i = 0; i < n; ++i) init_sum += tr[i];
        res(n) = init_sum / n;

        for (py::ssize_t i = n + 1; i < len; ++i) {
            res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
        }
    }
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第六部分: 形态匹配引擎 (V3.3.py 行 389-627)
// ═══════════════════════════════════════════════════════════════

namespace {

struct MatchCandidate {
    py::ssize_t hist_end;
    py::ssize_t hist_start;
    double cos_s;
    std::vector<double> hist_rets;
};

struct PatternResult {
    double top1_sim, top5_avg_sim, sim_decay, sim_variance;
    double match_distance_ratio, avg_future_ret, weighted_future_ret;
    double median_future_ret, ret_sign_consistency, best_match_ret;
    double max_dd_in_matches, match_time_span, match_time_span_ratio;
    double match_cluster_ratio;
    int n_matches_above_thresh;
};

// 从价格数组提取窗口
std::vector<double> extract_window(const double* prices, py::ssize_t start, py::ssize_t end) {
    std::vector<double> result;
    result.reserve(end - start + 1);
    for (py::ssize_t i = start; i <= end; ++i) {
        result.push_back(prices[i]);
    }
    return result;
}

// 向量版余弦相似度（用于批量内部计算）
double cosine_similarity_vec(const std::vector<double>& x, const std::vector<double>& y) {
    py::ssize_t n = static_cast<py::ssize_t>(x.size());
    if (n != static_cast<py::ssize_t>(y.size())) {
        return 0.0;
    }
    if (n == 0) return 0.0;

    double dot = 0.0, norm_x2 = 0.0, norm_y2 = 0.0;
    for (py::ssize_t i = 0; i < n; ++i) {
        dot += x[i] * y[i];
        norm_x2 += x[i] * x[i];
        norm_y2 += y[i] * y[i];
    }
    double norm_x = std::sqrt(norm_x2);
    double norm_y = std::sqrt(norm_y2);
    if (norm_x < 1e-12 || norm_y < 1e-12) {
        return 0.0;
    }
    return dot / (norm_x * norm_y);
}

// 向量版 DTW（兼容旧调用，委托给 span 版）
inline double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
    return dtw_distance_span(x.data(), static_cast<py::ssize_t>(x.size()),
                              y.data(), static_cast<py::ssize_t>(y.size()), window);
}

// 批量 DTW: 一个 query 对 N 个 candidates（一对一远端循环，GIL 释放）
py::object dtw_distance_batch(
    ArrD query_arr,
    ArrD candidates_arr,
    int window = 5,
    int top_k = 0
) {
    auto q = query_arr.unchecked<1>();
    auto c = candidates_arr.unchecked<2>();
    py::ssize_t L = q.shape(0);
    py::ssize_t N = c.shape(0);

    if (N == 0) {
        if (top_k > 0) {
            ArrI64 empty_idx(0);
            ArrD empty_dist(0);
            return py::make_tuple(empty_idx, empty_dist);
        }
        ArrD empty_result(0);
        return empty_result;
    }

    if (c.shape(1) != L) {
        throw std::invalid_argument(
            "candidates.shape[1] must equal query length, got " +
            std::to_string(c.shape(1)) + " vs " + std::to_string(L));
    }

    std::vector<double> distances(N);

    {
        py::gil_scoped_release release;
        const double* q_ptr = q.data(0);
        for (py::ssize_t i = 0; i < N; ++i) {
            distances[i] = dtw_distance_span(q_ptr, L, c.data(i, 0), L, window);
        }
    }

    if (top_k <= 0 || top_k >= static_cast<int>(N)) {
        ArrD result(N);
        auto res_buf = result.mutable_unchecked<1>();
        for (py::ssize_t i = 0; i < N; ++i) res_buf(i) = distances[i];
        return result;
    }

    // Top-K via partial_sort
    std::vector<std::pair<double, py::ssize_t>> indexed;
    indexed.reserve(N);
    for (py::ssize_t i = 0; i < N; ++i) {
        indexed.emplace_back(distances[i], i);
    }
    std::partial_sort(
        indexed.begin(),
        indexed.begin() + top_k,
        indexed.end());

    ArrI64 top_indices(top_k);
    ArrD top_dists(top_k);
    auto idx_buf = top_indices.mutable_unchecked<1>();
    auto dist_buf = top_dists.mutable_unchecked<1>();
    for (int i = 0; i < top_k; ++i) {
        idx_buf(i) = static_cast<int64_t>(indexed[i].second);
        dist_buf(i) = indexed[i].first;
    }

    return py::make_tuple(top_indices, top_dists);
}

// 从 Top-K 有效匹配中提取 15 维特征
PatternResult compute_pattern_features_cpp(
    const std::vector<double>& valid_scores,
    const std::vector<double>& valid_frets,
    const std::vector<py::ssize_t>& valid_ends,
    int T_back
) {
    PatternResult r{};
    int top_k_actual = static_cast<int>(valid_scores.size());

    // F1-F5: 相似度特征
    r.top1_sim = valid_scores[0];
    int n_avg = std::min(5, top_k_actual);
    double sum_avg = 0.0;
    for (int i = 0; i < n_avg; ++i) sum_avg += valid_scores[i];
    r.top5_avg_sim = sum_avg / n_avg;
    r.sim_decay = r.top1_sim - r.top5_avg_sim;

    double var = 0.0, mean_s = 0.0;
    for (auto s : valid_scores) mean_s += s;
    mean_s /= top_k_actual;
    for (auto s : valid_scores) var += (s - mean_s) * (s - mean_s);
    r.sim_variance = (top_k_actual > 1) ? var / top_k_actual : 0.0;
    r.match_distance_ratio = (r.top1_sim > 1e-12) ? r.sim_decay / r.top1_sim : 0.0;

    // F6-F11: 后续表现
    double sum_fr = 0.0;
    for (auto fr : valid_frets) sum_fr += fr;
    r.avg_future_ret = sum_fr / top_k_actual;

    double sum_ws = 0.0, sum_w = 0.0;
    for (int i = 0; i < top_k_actual; ++i) {
        sum_ws += valid_scores[i] * valid_frets[i];
        sum_w += valid_scores[i];
    }
    r.weighted_future_ret = (sum_w > 1e-12) ? sum_ws / sum_w : r.avg_future_ret;

    std::vector<double> sorted_fr = valid_frets;
    std::sort(sorted_fr.begin(), sorted_fr.end());
    r.median_future_ret = (top_k_actual % 2 == 1)
        ? sorted_fr[top_k_actual / 2]
        : (sorted_fr[top_k_actual / 2 - 1] + sorted_fr[top_k_actual / 2]) / 2.0;

    int pos_count = 0;
    for (auto fr : valid_frets) if (fr > 0) ++pos_count;
    r.ret_sign_consistency = static_cast<double>(pos_count) / top_k_actual;
    r.best_match_ret = valid_frets[0];

    double min_fr = *std::min_element(valid_frets.begin(), valid_frets.end());
    r.max_dd_in_matches = std::max(0.0, -min_fr);

    // F12-F15: 匹配质量
    auto [min_e, max_e] = std::minmax_element(valid_ends.begin(), valid_ends.end());
    r.match_time_span = static_cast<double>(*max_e - *min_e);
    r.match_time_span_ratio = r.match_time_span / T_back;

    std::vector<py::ssize_t> sorted_ends = valid_ends;
    std::sort(sorted_ends.begin(), sorted_ends.end());
    int max_in_window = 0;
    for (int i = 0; i < top_k_actual; ++i) {
        double target = static_cast<double>(sorted_ends[i]) + 60.0;
        auto it = std::upper_bound(sorted_ends.begin(), sorted_ends.end(),
                                   static_cast<py::ssize_t>(target));
        int count = static_cast<int>(it - sorted_ends.begin()) - i;
        max_in_window = std::max(max_in_window, count);
    }
    r.match_cluster_ratio = static_cast<double>(max_in_window) / top_k_actual;

    int above = 0;
    for (auto s : valid_scores) if (s > 0.8) ++above;
    r.n_matches_above_thresh = above;

    return r;
}

// ═══════════════════════════════════════════════════════════════
// 共享核心：余弦预筛选 → DTW 精排 → 特征提取
// single 和 batch 共用此函数，消除 ~400 行重复逻辑
// ═══════════════════════════════════════════════════════════════
std::optional<PatternResult> pattern_match_core(
    const double* prices, py::ssize_t n_prices,
    int T_idx, int k, int L_query, int T_back,
    int match_step, int M_forward, int dtw_window,
    int cos_prefilter_top,
    const std::vector<double>& query_rets,
    py::ssize_t search_start, py::ssize_t search_end,
    const std::vector<std::vector<double>>* precomputed_rets
) {
    py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());

    // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
    std::vector<MatchCandidate> cos_candidates;
    std::vector<double> fast_shape_dists;

    for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
        py::ssize_t hist_start = hist_end - L_query + 1;
        if (hist_start < 0) continue;

        // 获取标准化收益率：缓存优先，否则现场计算
        const std::vector<double>* hist_rets_ptr = nullptr;
        std::vector<double> hist_rets_scratch;

        if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size())) {
            hist_rets_ptr = &(*precomputed_rets)[hist_end];
        } else {
            auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
            if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
                hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query);
                hist_rets_ptr = &hist_rets_scratch;
            }
        }

        if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;

        const auto& hist_rets = *hist_rets_ptr;

        // 余弦相似度
        double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
        py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
        for (py::ssize_t i = 0; i < min_len; ++i) {
            dot += hist_rets[i] * query_rets[i];
            nx2 += hist_rets[i] * hist_rets[i];
            ny2 += query_rets[i] * query_rets[i];
        }
        double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
        double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;

        // 快速形状距离
        double fast_d2 = 0.0;
        for (py::ssize_t i = 0; i < min_len; ++i) {
            double diff = hist_rets[i] - query_rets[i];
            fast_d2 += diff * diff;
        }
        fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));

        if (cos_s > 0) {
            cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
        }
    }

    if (cos_candidates.size() < 3) return std::nullopt;

    // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
    double sigma_fast = 1.0;
    if (fast_shape_dists.size() > 1) {
        double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0.0)
                        / fast_shape_dists.size();
        double var_fd = 0.0;
        for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
        var_fd /= fast_shape_dists.size();
        sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)));
    }
    sigma_fast = std::max(sigma_fast, 1e-12);

    // 余弦排序 + 全量边界
    std::sort(cos_candidates.begin(), cos_candidates.end(),
              [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_s; });

    double global_min_cos = cos_candidates.back().cos_s;
    double global_max_cos = cos_candidates.front().cos_s;

    int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
    cos_candidates.resize(n_cos);

    // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
    std::vector<double> dtw_dists, cos_sims, future_rets;
    std::vector<py::ssize_t> match_ends;
    dtw_dists.reserve(n_cos);
    cos_sims.reserve(n_cos);
    future_rets.reserve(n_cos);
    match_ends.reserve(n_cos);

    for (const auto& cand : cos_candidates) {
        py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
        double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
                                          query_rets.data(), n_query, dtw_window);

        dtw_dists.push_back(dtw_d);
        cos_sims.push_back(cand.cos_s);

        py::ssize_t fut_end = cand.hist_end + M_forward;
        if (fut_end < n_prices && fut_end < T_idx) {
            future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
        } else {
            future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
        }
        match_ends.push_back(cand.hist_end);
    }

    if (dtw_dists.size() < 3) return std::nullopt;

    // sim_dtw = exp(-dtw/sigma)
    double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;

    std::vector<double> sim_dtw(dtw_dists.size());
    double min_dtw_v = std::numeric_limits<double>::max();
    double max_dtw_v = std::numeric_limits<double>::lowest();
    for (size_t i = 0; i < dtw_dists.size(); ++i) {
        sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
        min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
        max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
    }

    // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
    double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
    double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
                           ? (global_max_cos - global_min_cos) : 1.0;

    struct Scored { double score, fut_ret; py::ssize_t end_idx; };
    std::vector<Scored> scored;
    scored.reserve(sim_dtw.size());
    for (size_t i = 0; i < sim_dtw.size(); ++i) {
        double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
        double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
        scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
    }

    std::sort(scored.begin(), scored.end(),
              [](const Scored& a, const Scored& b) { return a.score > b.score; });

    int top_k = std::min(k, static_cast<int>(scored.size()));

    // 过滤 NaN 未来收益
    std::vector<double> valid_scores, valid_frets;
    std::vector<py::ssize_t> valid_ends;
    for (int i = 0; i < top_k; ++i) {
        if (!std::isnan(scored[i].fut_ret)) {
            valid_scores.push_back(scored[i].score);
            valid_frets.push_back(scored[i].fut_ret);
            valid_ends.push_back(scored[i].end_idx);
        }
    }
    if (valid_scores.size() < 2) return std::nullopt;

    return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
}

} // namespace

// ═══════════════════════════════════════════════════════════════
// 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
// ═══════════════════════════════════════════════════════════════
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k = 10,
    int L_query = 20,
    int T_back = 750,
    int match_step = 1,
    int M_forward = 5,
    int dtw_window = 5,
    int cos_prefilter_top = 50
) {
    auto prices_buf = prices_arr.unchecked<1>();
    py::ssize_t n_prices = prices_buf.shape(0);
    const double* prices = prices_buf.data(0);

    // ── 输入校验 ──
    if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
        throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::to_string(T_idx));
    }
    if (L_query < 3) {
        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
    }
    if (T_back <= 0) {
        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
    }
    if (k <= 0) {
        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
    }
    if (M_forward < 1) {
        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
    }
    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }
    if (dtw_window < 0) {
        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
    }
    if (cos_prefilter_top <= 0) {
        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
    }
    if (T_idx < L_query + M_forward + 10) return py::none();
    if (T_idx - L_query + 1 < 0) return py::none();

    // 查询窗口标准化
    auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
    if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();

    std::vector<double> query_rets;
    {
        py::gil_scoped_release release;
        query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
    }
    if (query_rets.size() < 2) return py::none();

    py::ssize_t search_end = T_idx - L_query;
    if (search_end < L_query) return py::none();
    py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
                                        py::ssize_t(T_idx - T_back));

    // ── 委托共享核心（无预计算缓存，现场标准化）──
    std::optional<PatternResult> result_opt;
    {
        py::gil_scoped_release release;
        result_opt = pattern_match_core(
            prices, n_prices, T_idx, k, L_query, T_back,
            match_step, M_forward, dtw_window, cos_prefilter_top,
            query_rets, search_start, search_end,
            nullptr  // 无预计算缓存
        );
    }

    if (!result_opt.has_value()) return py::none();

    // ── 构造返回值 ──
    py::dict result;
    result["top1_sim"] = result_opt->top1_sim;
    result["top5_avg_sim"] = result_opt->top5_avg_sim;
    result["sim_decay"] = result_opt->sim_decay;
    result["sim_variance"] = result_opt->sim_variance;
    result["match_distance_ratio"] = result_opt->match_distance_ratio;
    result["avg_future_ret"] = result_opt->avg_future_ret;
    result["weighted_future_ret"] = result_opt->weighted_future_ret;
    result["median_future_ret"] = result_opt->median_future_ret;
    result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
    result["best_match_ret"] = result_opt->best_match_ret;
    result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
    result["match_time_span"] = result_opt->match_time_span;
    result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
    result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
    result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第七部分: 批量形态匹配 (v3 新增)
// ═══════════════════════════════════════════════════════════════

py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k = 10,
    int L_query = 20,
    int T_back = 750,
    int match_step = 1,
    int M_forward = 5,
    int dtw_window = 5,
    int cos_prefilter_top = 50
) {
    auto prices_buf = prices_arr.unchecked<1>();
    py::ssize_t n_prices = prices_buf.shape(0);
    const double* prices = prices_buf.data(0);

    auto t_buf = t_indices_arr.unchecked<1>();
    py::ssize_t n_samples = t_buf.shape(0);
    const int64_t* t_ptr = t_buf.data(0);

    // ── 输入校验 ──
    if (L_query < 3) {
        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
    }
    if (T_back <= 0) {
        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
    }
    if (k <= 0) {
        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
    }
    if (M_forward < 1) {
        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forward));
    }
    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }
    if (dtw_window < 0) {
        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_window));
    }
    if (cos_prefilter_top <= 0) {
        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(cos_prefilter_top));
    }
    if (n_samples == 0) {
        ArrD empty_features(std::vector<py::ssize_t>{0, 15});
        py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
        return py::make_tuple(empty_features, empty_mask);
    }

    for (py::ssize_t i = 1; i < n_samples; ++i) {
        if (t_ptr[i] <= t_ptr[i - 1]) {
            throw std::invalid_argument("t_indices must be strictly increasing");
        }
    }
    if (t_ptr[n_samples - 1] >= n_prices) {
        throw std::invalid_argument("max(t_indices) must be < len(prices)");
    }

    std::vector<double> features_flat;
    features_flat.reserve(n_samples * 15);
    std::vector<bool> valid_mask(n_samples, false);

    {
        // ── GIL 释放区：纯 C++ 批量计算 ──
        py::gil_scoped_release release;

        // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
        py::ssize_t precompute_start = n_prices;
        py::ssize_t precompute_end = 0;
        for (py::ssize_t s = 0; s < n_samples; ++s) {
            int T_idx = static_cast<int>(t_ptr[s]);
            if (T_idx < L_query + M_forward + 10) continue;
            py::ssize_t s_end = T_idx - L_query;
            if (s_end < L_query) continue;
            py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
                                           py::ssize_t(T_idx - T_back));
            if (s_start < s_end) {
                precompute_start = std::min(precompute_start, s_start);
                precompute_end = std::max(precompute_end, s_end);
            }
        }

        // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
        std::vector<std::vector<double>> precomputed_rets(n_prices);
        if (precompute_start <= precompute_end) {
            for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
                py::ssize_t start = end - L_query + 1;
                if (start >= 0) {
                    auto window_prices = extract_window(prices, start, end);
                    precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
                }
            }
        }

        // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
        for (py::ssize_t s = 0; s < n_samples; ++s) {
            int T_idx = static_cast<int>(t_ptr[s]);

            if (T_idx < L_query + M_forward + 10) continue;
            if (T_idx - L_query + 1 < 0) continue;

            auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
            if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) continue;

            auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
            if (query_rets.size() < 2) continue;

            py::ssize_t search_end = T_idx - L_query;
            if (search_end < L_query) continue;
            py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
                                                py::ssize_t(T_idx - T_back));

            // ── 委托共享核心（使用预计算缓存）──
            auto result_opt = pattern_match_core(
                prices, n_prices, T_idx, k, L_query, T_back,
                match_step, M_forward, dtw_window, cos_prefilter_top,
                query_rets, search_start, search_end,
                &precomputed_rets
            );

            if (!result_opt.has_value()) continue;

            auto& r = *result_opt;
            features_flat.push_back(r.top1_sim);
            features_flat.push_back(r.top5_avg_sim);
            features_flat.push_back(r.sim_decay);
            features_flat.push_back(r.sim_variance);
            features_flat.push_back(r.match_distance_ratio);
            features_flat.push_back(r.avg_future_ret);
            features_flat.push_back(r.weighted_future_ret);
            features_flat.push_back(r.median_future_ret);
            features_flat.push_back(r.ret_sign_consistency);
            features_flat.push_back(r.best_match_ret);
            features_flat.push_back(r.max_dd_in_matches);
            features_flat.push_back(r.match_time_span);
            features_flat.push_back(r.match_time_span_ratio);
            features_flat.push_back(r.match_cluster_ratio);
            features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));

            valid_mask[s] = true;
        }
    } // GIL 在此重新获取

    // ── 构造返回数组 ──
    py::ssize_t n_valid = static_cast<py::ssize_t>(features_flat.size()) / 15;
    ArrD features_X15(std::vector<py::ssize_t>{n_valid, 15});
    auto fx_buf = features_X15.mutable_unchecked<2>();
    for (py::ssize_t i = 0; i < n_valid; ++i) {
        for (py::ssize_t j = 0; j < 15; ++j) {
            fx_buf(i, j) = features_flat[i * 15 + j];
        }
    }

    py::array_t<bool> valid_mask_arr(std::vector<py::ssize_t>{n_samples});
    auto vm_buf = valid_mask_arr.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < n_samples; ++i) {
        vm_buf(i) = valid_mask[i];
    }

    return py::make_tuple(features_X15, valid_mask_arr);
}

// ═══════════════════════════════════════════════════════════════
// 模块定义
// ═══════════════════════════════════════════════════════════════

PYBIND11_MODULE(etf_core, m) {
    m.doc() = "ETF pattern matching core — C++ accelerated (pybind11)\n\n"
              "来源: 形态匹配ETF组合策略_V3.3.py\n"
              "模块: dtw_distance, standardize_returns, cosine_similarity,\n"
              "       compute_adx, compute_atr, dtw_distance_batch,\n"
              "       pattern_match_single, pattern_match_batch\n"
              "v2: 三模块合并为单一 etf_core, /utf-8, py::ssize_t, forcecast\n"
              "v3: 新增 pattern_match_batch，支持同 ETF 多 T_idx 批量形态匹配";

    // ── 序列预处理 ──
    m.def("standardize_returns", &standardize_returns,
          py::arg("price_series"),
          "计算标准化收益率序列: (rets - mean) / std.\n\n"
          "Args: price_series (1-D float64 array, n>=2)\n"
          "Returns: 1-D float64 array (length n-1)");

    m.def("cosine_similarity", &cosine_similarity,
          py::arg("x"), py::arg("y"),
          "两向量余弦相似度 ∈ [-1, 1].\n"
          "norm < 1e-12 时返回 0.0.");

    // ── DTW ──
    m.def("dtw_distance", &dtw_distance,
          py::arg("x"), py::arg("y"), py::arg("window") = 5,
          "Sakoe-Chiba band DTW 距离.\n"
          "返回归一化距离: sqrt(dtw[n,m]) / (n+m).\n"
          "空序列返回 inf.");

    m.def("dtw_distance_batch", &dtw_distance_batch,
          py::arg("query"), py::arg("candidates"),
          py::arg("window") = 5, py::arg("top_k") = 0,
          "批量 DTW: 一个 query 对 N 个 candidates.\n\n"
          "Args:\n"
          "  query: 1-D float64 array (L,)\n"
          "  candidates: 2-D float64 array (N, L)\n"
          "  window: Sakoe-Chiba band 宽度\n"
          "  top_k: 若 >0 且 <N，返回 (top_indices, top_distances);\n"
          "         否则返回全部 distances (N,)\n\n"
          "Returns: distances (N,) 或 (indices, distances) 各 (top_k,)");

    // ── 技术指标 ──
    m.def("compute_adx", &compute_adx,
          py::arg("high"), py::arg("low"), py::arg("close"),
          py::arg("n") = 14,
          "ADX (Average Directional Index), Wilder's smoothing.\n"
          "数据不足时返回 25.0 (中性值).");

    m.def("compute_atr", &compute_atr,
          py::arg("high"), py::arg("low"), py::arg("close"),
          py::arg("n") = 14,
          "ATR (Average True Range).\n"
          "前 n 天为 NaN.");

    // 模块常量：15 维特征名（顺序与 pattern_match_batch 的 features_X15 列一致）
    m.attr("FEATURE_KEYS") = py::make_tuple(
        "top1_sim",
        "top5_avg_sim",
        "sim_decay",
        "sim_variance",
        "match_distance_ratio",
        "avg_future_ret",
        "weighted_future_ret",
        "median_future_ret",
        "ret_sign_consistency",
        "best_match_ret",
        "max_dd_in_matches",
        "match_time_span",
        "match_time_span_ratio",
        "match_cluster_ratio",
        "n_matches_above_thresh"
    );

    // ── 形态匹配 ──
    m.def("pattern_match_single", &pattern_match_single,
          py::arg("prices"),
          py::arg("T_idx"),
          py::arg("k") = 10,
          py::arg("L_query") = 20,
          py::arg("T_back") = 750,
          py::arg("match_step") = 1,
          py::arg("M_forward") = 5,
          py::arg("dtw_window") = 5,
          py::arg("cos_prefilter_top") = 50,
          "单 ETF 单时点形态匹配 → 15维特征字典.\n\n"
          "V3.0 余弦预筛选: 第1遍全量余弦 → 第2遍 DTW 精排.\n"
          "前视偏差防护: fut_end < T_idx 严格约束.\n"
          "数据不足返回 None.\n\n"
          "Returns: dict with 15 keys or None.\n"
          "  F1-F5:  top1_sim, top5_avg_sim, sim_decay, sim_variance, match_distance_ratio\n"
          "  F6-F11: avg_future_ret, weighted_future_ret, median_future_ret,\n"
          "          ret_sign_consistency, best_match_ret, max_dd_in_matches\n"
          "  F12-F15: match_time_span, match_time_span_ratio, match_cluster_ratio,\n"
          "           n_matches_above_thresh");

    m.def("pattern_match_batch", &pattern_match_batch,
          py::arg("prices"), py::arg("t_indices"),
          py::arg("k") = 10, py::arg("L_query") = 20,
          py::arg("T_back") = 750, py::arg("match_step") = 1,
          py::arg("M_forward") = 5, py::arg("dtw_window") = 5,
          py::arg("cos_prefilter_top") = 50,
          "批量形态匹配——同ETF多T_idx.\n\n"
          "核心优化: 候选窗口标准化收益率在相邻 T_idx 之间高度重叠，\n"
          "C++ 内部一次性预计算并复用，避免 Python 往返和重复标准化.\n\n"
          "Returns: (features_X15, valid_mask).\n"
          "features_X15: (n_valid, 15) float64 — 仅有效样本.\n"
          "valid_mask: (n_samples,) bool.\n"
          "feature_keys 已提升为模块常量 etf_core.FEATURE_KEYS (15 str).");
}


exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Select-String -Path '"'src\\cpp\\etf_core.cpp' -Pattern '"'^py::object pattern_match_single|''^py::tuple pattern_match_batch|pattern_match_single'"\\(|pattern_match_batch\\(' -Encoding UTF8 -Context 0,140" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 194ms:

> src\cpp\etf_core.cpp:714:py::object pattern_match_single(
  src\cpp\etf_core.cpp:715:    ArrD prices_arr,
  src\cpp\etf_core.cpp:716:    int T_idx,
  src\cpp\etf_core.cpp:717:    int k = 10,
  src\cpp\etf_core.cpp:718:    int L_query = 20,
  src\cpp\etf_core.cpp:719:    int T_back = 750,
  src\cpp\etf_core.cpp:720:    int match_step = 1,
  src\cpp\etf_core.cpp:721:    int M_forward = 5,
  src\cpp\etf_core.cpp:722:    int dtw_window = 5,
  src\cpp\etf_core.cpp:723:    int cos_prefilter_top = 50
  src\cpp\etf_core.cpp:724:) {
  src\cpp\etf_core.cpp:725:    auto prices_buf = prices_arr.unchecked<1>();
  src\cpp\etf_core.cpp:726:    py::ssize_t n_prices = prices_buf.shape(0);
  src\cpp\etf_core.cpp:727:    const double* prices = prices_buf.data(0);
  src\cpp\etf_core.cpp:728:
  src\cpp\etf_core.cpp:729:    // ── 输入校验 ──
  src\cpp\etf_core.cpp:730:    if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
  src\cpp\etf_core.cpp:731:        throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::t
o_string(T_idx));
  src\cpp\etf_core.cpp:732:    }
  src\cpp\etf_core.cpp:733:    if (L_query < 3) {
  src\cpp\etf_core.cpp:734:        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
  src\cpp\etf_core.cpp:735:    }
  src\cpp\etf_core.cpp:736:    if (T_back <= 0) {
  src\cpp\etf_core.cpp:737:        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
  src\cpp\etf_core.cpp:738:    }
  src\cpp\etf_core.cpp:739:    if (k <= 0) {
  src\cpp\etf_core.cpp:740:        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
  src\cpp\etf_core.cpp:741:    }
  src\cpp\etf_core.cpp:742:    if (M_forward < 1) {
  src\cpp\etf_core.cpp:743:        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forwar
d));
  src\cpp\etf_core.cpp:744:    }
  src\cpp\etf_core.cpp:745:    if (match_step <= 0) {
  src\cpp\etf_core.cpp:746:        throw std::invalid_argument("match_step must be > 0");
  src\cpp\etf_core.cpp:747:    }
  src\cpp\etf_core.cpp:748:    if (dtw_window < 0) {
  src\cpp\etf_core.cpp:749:        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_win
dow));
  src\cpp\etf_core.cpp:750:    }
  src\cpp\etf_core.cpp:751:    if (cos_prefilter_top <= 0) {
  src\cpp\etf_core.cpp:752:        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(c
os_prefilter_top));
  src\cpp\etf_core.cpp:753:    }
  src\cpp\etf_core.cpp:754:    if (T_idx < L_query + M_forward + 10) return py::none();
  src\cpp\etf_core.cpp:755:    if (T_idx - L_query + 1 < 0) return py::none();
  src\cpp\etf_core.cpp:756:
  src\cpp\etf_core.cpp:757:    // 查询窗口标准化
  src\cpp\etf_core.cpp:758:    auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
  src\cpp\etf_core.cpp:759:    if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
  src\cpp\etf_core.cpp:760:
  src\cpp\etf_core.cpp:761:    std::vector<double> query_rets;
  src\cpp\etf_core.cpp:762:    {
  src\cpp\etf_core.cpp:763:        py::gil_scoped_release release;
  src\cpp\etf_core.cpp:764:        query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
  src\cpp\etf_core.cpp:765:    }
  src\cpp\etf_core.cpp:766:    if (query_rets.size() < 2) return py::none();
  src\cpp\etf_core.cpp:767:
  src\cpp\etf_core.cpp:768:    py::ssize_t search_end = T_idx - L_query;
  src\cpp\etf_core.cpp:769:    if (search_end < L_query) return py::none();
  src\cpp\etf_core.cpp:770:    py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
  src\cpp\etf_core.cpp:771:                                        py::ssize_t(T_idx - T_back));
  src\cpp\etf_core.cpp:772:
  src\cpp\etf_core.cpp:773:    // ── 委托共享核心（无预计算缓存，现场标准化）──
  src\cpp\etf_core.cpp:774:    std::optional<PatternResult> result_opt;
  src\cpp\etf_core.cpp:775:    {
  src\cpp\etf_core.cpp:776:        py::gil_scoped_release release;
  src\cpp\etf_core.cpp:777:        result_opt = pattern_match_core(
  src\cpp\etf_core.cpp:778:            prices, n_prices, T_idx, k, L_query, T_back,
  src\cpp\etf_core.cpp:779:            match_step, M_forward, dtw_window, cos_prefilter_top,
  src\cpp\etf_core.cpp:780:            query_rets, search_start, search_end,
  src\cpp\etf_core.cpp:781:            nullptr  // 无预计算缓存
  src\cpp\etf_core.cpp:782:        );
  src\cpp\etf_core.cpp:783:    }
  src\cpp\etf_core.cpp:784:
  src\cpp\etf_core.cpp:785:    if (!result_opt.has_value()) return py::none();
  src\cpp\etf_core.cpp:786:
  src\cpp\etf_core.cpp:787:    // ── 构造返回值 ──
  src\cpp\etf_core.cpp:788:    py::dict result;
  src\cpp\etf_core.cpp:789:    result["top1_sim"] = result_opt->top1_sim;
  src\cpp\etf_core.cpp:790:    result["top5_avg_sim"] = result_opt->top5_avg_sim;
  src\cpp\etf_core.cpp:791:    result["sim_decay"] = result_opt->sim_decay;
  src\cpp\etf_core.cpp:792:    result["sim_variance"] = result_opt->sim_variance;
  src\cpp\etf_core.cpp:793:    result["match_distance_ratio"] = result_opt->match_distance_ratio;
  src\cpp\etf_core.cpp:794:    result["avg_future_ret"] = result_opt->avg_future_ret;
  src\cpp\etf_core.cpp:795:    result["weighted_future_ret"] = result_opt->weighted_future_ret;
  src\cpp\etf_core.cpp:796:    result["median_future_ret"] = result_opt->median_future_ret;
  src\cpp\etf_core.cpp:797:    result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
  src\cpp\etf_core.cpp:798:    result["best_match_ret"] = result_opt->best_match_ret;
  src\cpp\etf_core.cpp:799:    result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
  src\cpp\etf_core.cpp:800:    result["match_time_span"] = result_opt->match_time_span;
  src\cpp\etf_core.cpp:801:    result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
  src\cpp\etf_core.cpp:802:    result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
  src\cpp\etf_core.cpp:803:    result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
  src\cpp\etf_core.cpp:804:    return result;
  src\cpp\etf_core.cpp:805:}
  src\cpp\etf_core.cpp:806:
  src\cpp\etf_core.cpp:807:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:808:// 第七部分: 批量形态匹配 (v3 新增)
  src\cpp\etf_core.cpp:809:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:810:
> src\cpp\etf_core.cpp:811:py::tuple pattern_match_batch(
  src\cpp\etf_core.cpp:812:    ArrD prices_arr,
  src\cpp\etf_core.cpp:813:    ArrI64 t_indices_arr,
  src\cpp\etf_core.cpp:814:    int k = 10,
  src\cpp\etf_core.cpp:815:    int L_query = 20,
  src\cpp\etf_core.cpp:816:    int T_back = 750,
  src\cpp\etf_core.cpp:817:    int match_step = 1,
  src\cpp\etf_core.cpp:818:    int M_forward = 5,
  src\cpp\etf_core.cpp:819:    int dtw_window = 5,
  src\cpp\etf_core.cpp:820:    int cos_prefilter_top = 50
  src\cpp\etf_core.cpp:821:) {
  src\cpp\etf_core.cpp:822:    auto prices_buf = prices_arr.unchecked<1>();
  src\cpp\etf_core.cpp:823:    py::ssize_t n_prices = prices_buf.shape(0);
  src\cpp\etf_core.cpp:824:    const double* prices = prices_buf.data(0);
  src\cpp\etf_core.cpp:825:
  src\cpp\etf_core.cpp:826:    auto t_buf = t_indices_arr.unchecked<1>();
  src\cpp\etf_core.cpp:827:    py::ssize_t n_samples = t_buf.shape(0);
  src\cpp\etf_core.cpp:828:    const int64_t* t_ptr = t_buf.data(0);
  src\cpp\etf_core.cpp:829:
  src\cpp\etf_core.cpp:830:    // ── 输入校验 ──
  src\cpp\etf_core.cpp:831:    if (L_query < 3) {
  src\cpp\etf_core.cpp:832:        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
  src\cpp\etf_core.cpp:833:    }
  src\cpp\etf_core.cpp:834:    if (T_back <= 0) {
  src\cpp\etf_core.cpp:835:        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
  src\cpp\etf_core.cpp:836:    }
  src\cpp\etf_core.cpp:837:    if (k <= 0) {
  src\cpp\etf_core.cpp:838:        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
  src\cpp\etf_core.cpp:839:    }
  src\cpp\etf_core.cpp:840:    if (M_forward < 1) {
  src\cpp\etf_core.cpp:841:        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forwar
d));
  src\cpp\etf_core.cpp:842:    }
  src\cpp\etf_core.cpp:843:    if (match_step <= 0) {
  src\cpp\etf_core.cpp:844:        throw std::invalid_argument("match_step must be > 0");
  src\cpp\etf_core.cpp:845:    }
  src\cpp\etf_core.cpp:846:    if (dtw_window < 0) {
  src\cpp\etf_core.cpp:847:        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_win
dow));
  src\cpp\etf_core.cpp:848:    }
  src\cpp\etf_core.cpp:849:    if (cos_prefilter_top <= 0) {
  src\cpp\etf_core.cpp:850:        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(c
os_prefilter_top));
  src\cpp\etf_core.cpp:851:    }
  src\cpp\etf_core.cpp:852:    if (n_samples == 0) {
  src\cpp\etf_core.cpp:853:        ArrD empty_features(std::vector<py::ssize_t>{0, 15});
  src\cpp\etf_core.cpp:854:        py::array_t<bool> empty_mask(std::vector<py::ssize_t>{0});
  src\cpp\etf_core.cpp:855:        return py::make_tuple(empty_features, empty_mask);
  src\cpp\etf_core.cpp:856:    }
  src\cpp\etf_core.cpp:857:
  src\cpp\etf_core.cpp:858:    for (py::ssize_t i = 1; i < n_samples; ++i) {
  src\cpp\etf_core.cpp:859:        if (t_ptr[i] <= t_ptr[i - 1]) {
  src\cpp\etf_core.cpp:860:            throw std::invalid_argument("t_indices must be strictly increasing");
  src\cpp\etf_core.cpp:861:        }
  src\cpp\etf_core.cpp:862:    }
  src\cpp\etf_core.cpp:863:    if (t_ptr[n_samples - 1] >= n_prices) {
  src\cpp\etf_core.cpp:864:        throw std::invalid_argument("max(t_indices) must be < len(prices)");
  src\cpp\etf_core.cpp:865:    }
  src\cpp\etf_core.cpp:866:
  src\cpp\etf_core.cpp:867:    std::vector<double> features_flat;
  src\cpp\etf_core.cpp:868:    features_flat.reserve(n_samples * 15);
  src\cpp\etf_core.cpp:869:    std::vector<bool> valid_mask(n_samples, false);
  src\cpp\etf_core.cpp:870:
  src\cpp\etf_core.cpp:871:    {
  src\cpp\etf_core.cpp:872:        // ── GIL 释放区：纯 C++ 批量计算 ──
  src\cpp\etf_core.cpp:873:        py::gil_scoped_release release;
  src\cpp\etf_core.cpp:874:
  src\cpp\etf_core.cpp:875:        // ── 第一遍：计算所有 T_idx 搜索范围的并集（避免预计算无用窗口）──
  src\cpp\etf_core.cpp:876:        py::ssize_t precompute_start = n_prices;
  src\cpp\etf_core.cpp:877:        py::ssize_t precompute_end = 0;
  src\cpp\etf_core.cpp:878:        for (py::ssize_t s = 0; s < n_samples; ++s) {
  src\cpp\etf_core.cpp:879:            int T_idx = static_cast<int>(t_ptr[s]);
  src\cpp\etf_core.cpp:880:            if (T_idx < L_query + M_forward + 10) continue;
  src\cpp\etf_core.cpp:881:            py::ssize_t s_end = T_idx - L_query;
  src\cpp\etf_core.cpp:882:            if (s_end < L_query) continue;
  src\cpp\etf_core.cpp:883:            py::ssize_t s_start = std::max(py::ssize_t(L_query - 1),
  src\cpp\etf_core.cpp:884:                                           py::ssize_t(T_idx - T_back));
  src\cpp\etf_core.cpp:885:            if (s_start < s_end) {
  src\cpp\etf_core.cpp:886:                precompute_start = std::min(precompute_start, s_start);
  src\cpp\etf_core.cpp:887:                precompute_end = std::max(precompute_end, s_end);
  src\cpp\etf_core.cpp:888:            }
  src\cpp\etf_core.cpp:889:        }
  src\cpp\etf_core.cpp:890:
  src\cpp\etf_core.cpp:891:        // ── 仅预计算搜索范围并集内的窗口标准化收益率 ──
  src\cpp\etf_core.cpp:892:        std::vector<std::vector<double>> precomputed_rets(n_prices);
  src\cpp\etf_core.cpp:893:        if (precompute_start <= precompute_end) {
  src\cpp\etf_core.cpp:894:            for (py::ssize_t end = precompute_start; end <= precompute_end; ++end) {
  src\cpp\etf_core.cpp:895:                py::ssize_t start = end - L_query + 1;
  src\cpp\etf_core.cpp:896:                if (start >= 0) {
  src\cpp\etf_core.cpp:897:                    auto window_prices = extract_window(prices, start, end);
  src\cpp\etf_core.cpp:898:                    precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_
query);
  src\cpp\etf_core.cpp:899:                }
  src\cpp\etf_core.cpp:900:            }
  src\cpp\etf_core.cpp:901:        }
  src\cpp\etf_core.cpp:902:
  src\cpp\etf_core.cpp:903:        // ── 对每个 T_idx 执行形态匹配（复用预计算缓存）──
  src\cpp\etf_core.cpp:904:        for (py::ssize_t s = 0; s < n_samples; ++s) {
  src\cpp\etf_core.cpp:905:            int T_idx = static_cast<int>(t_ptr[s]);
  src\cpp\etf_core.cpp:906:
  src\cpp\etf_core.cpp:907:            if (T_idx < L_query + M_forward + 10) continue;
  src\cpp\etf_core.cpp:908:            if (T_idx - L_query + 1 < 0) continue;
  src\cpp\etf_core.cpp:909:
  src\cpp\etf_core.cpp:910:            auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
  src\cpp\etf_core.cpp:911:            if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) continue;
  src\cpp\etf_core.cpp:912:
  src\cpp\etf_core.cpp:913:            auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
  src\cpp\etf_core.cpp:914:            if (query_rets.size() < 2) continue;
  src\cpp\etf_core.cpp:915:
  src\cpp\etf_core.cpp:916:            py::ssize_t search_end = T_idx - L_query;
  src\cpp\etf_core.cpp:917:            if (search_end < L_query) continue;
  src\cpp\etf_core.cpp:918:            py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
  src\cpp\etf_core.cpp:919:                                                py::ssize_t(T_idx - T_back));
  src\cpp\etf_core.cpp:920:
  src\cpp\etf_core.cpp:921:            // ── 委托共享核心（使用预计算缓存）──
  src\cpp\etf_core.cpp:922:            auto result_opt = pattern_match_core(
  src\cpp\etf_core.cpp:923:                prices, n_prices, T_idx, k, L_query, T_back,
  src\cpp\etf_core.cpp:924:                match_step, M_forward, dtw_window, cos_prefilter_top,
  src\cpp\etf_core.cpp:925:                query_rets, search_start, search_end,
  src\cpp\etf_core.cpp:926:                &precomputed_rets
  src\cpp\etf_core.cpp:927:            );
  src\cpp\etf_core.cpp:928:
  src\cpp\etf_core.cpp:929:            if (!result_opt.has_value()) continue;
  src\cpp\etf_core.cpp:930:
  src\cpp\etf_core.cpp:931:            auto& r = *result_opt;
  src\cpp\etf_core.cpp:932:            features_flat.push_back(r.top1_sim);
  src\cpp\etf_core.cpp:933:            features_flat.push_back(r.top5_avg_sim);
  src\cpp\etf_core.cpp:934:            features_flat.push_back(r.sim_decay);
  src\cpp\etf_core.cpp:935:            features_flat.push_back(r.sim_variance);
  src\cpp\etf_core.cpp:936:            features_flat.push_back(r.match_distance_ratio);
  src\cpp\etf_core.cpp:937:            features_flat.push_back(r.avg_future_ret);
  src\cpp\etf_core.cpp:938:            features_flat.push_back(r.weighted_future_ret);
  src\cpp\etf_core.cpp:939:            features_flat.push_back(r.median_future_ret);
  src\cpp\etf_core.cpp:940:            features_flat.push_back(r.ret_sign_consistency);
  src\cpp\etf_core.cpp:941:            features_flat.push_back(r.best_match_ret);
  src\cpp\etf_core.cpp:942:            features_flat.push_back(r.max_dd_in_matches);
  src\cpp\etf_core.cpp:943:            features_flat.push_back(r.match_time_span);
  src\cpp\etf_core.cpp:944:            features_flat.push_back(r.match_time_span_ratio);
  src\cpp\etf_core.cpp:945:            features_flat.push_back(r.match_cluster_ratio);
  src\cpp\etf_core.cpp:946:            features_flat.push_back(static_cast<double>(r.n_matches_above_thresh));
  src\cpp\etf_core.cpp:947:
  src\cpp\etf_core.cpp:948:            valid_mask[s] = true;
  src\cpp\etf_core.cpp:949:        }
  src\cpp\etf_core.cpp:950:    } // GIL 在此重新获取
  src\cpp\etf_core.cpp:951:



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Select-String -Path '"'README.md','tests\\*.py','verify_*.py' -Pattern 'pattern_match_single\\(|pattern_match_batch\\(' -Encoding UTF8 -Context 2,8" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 202ms:

  tests\test_pattern_match.py:32:        """价格序列太短"""
  tests\test_pattern_match.py:33:        prices = np.array([100.0] * 10)
> tests\test_pattern_match.py:34:        result = pattern_match_single(prices, T_idx=5)
  tests\test_pattern_match.py:35:        assert result is None
  tests\test_pattern_match.py:36:
  tests\test_pattern_match.py:37:    def test_insufficient_data_small_T_idx(self):
  tests\test_pattern_match.py:38:        """T_idx 太小（不足 L_query + M_forward + 10）"""
  tests\test_pattern_match.py:39:        prices = _generate_random_walk(100)
> tests\test_pattern_match.py:40:        result = pattern_match_single(prices, T_idx=30)
  tests\test_pattern_match.py:41:        assert result is None
  tests\test_pattern_match.py:42:
  tests\test_pattern_match.py:43:    def test_basic_extraction(self):
  tests\test_pattern_match.py:44:        """基本提取 — 应返回15维非空特征"""
  tests\test_pattern_match.py:45:        prices = _generate_random_walk(600)
  tests\test_pattern_match.py:46:        T_idx = 500
> tests\test_pattern_match.py:47:        result = pattern_match_single(prices, T_idx)
  tests\test_pattern_match.py:48:        assert result is not None
  tests\test_pattern_match.py:49:        assert len(result) == 15
  tests\test_pattern_match.py:50:        # 所有值应为有限数值
  tests\test_pattern_match.py:51:        for key, val in result.items():
  tests\test_pattern_match.py:52:            assert isinstance(val, (float, int, np.integer)), f"{key} 类型异常: {type(val)
}"
  tests\test_pattern_match.py:53:            assert np.isfinite(float(val)), f"{key} = {val} 不是有限值"
  tests\test_pattern_match.py:54:
  tests\test_pattern_match.py:55:    def test_no_query_window_leakage(self):
  tests\test_pattern_match.py:57:        prices = _generate_random_walk(800)
  tests\test_pattern_match.py:58:        T_idx = 700
> tests\test_pattern_match.py:59:        result = pattern_match_single(prices, T_idx)
  tests\test_pattern_match.py:60:        assert result is not None
  tests\test_pattern_match.py:61:        # 函数内部已保证 fut_end < T_idx，这里验证返回值合理性
  tests\test_pattern_match.py:62:        assert -1.0 <= result["avg_future_ret"] <= 1.0
  tests\test_pattern_match.py:63:
  tests\test_pattern_match.py:64:    def test_returns_consistent_shape(self):
  tests\test_pattern_match.py:65:        """多次调用应返回一致的特征键集合"""
  tests\test_pattern_match.py:66:        prices = _generate_random_walk(600)
  tests\test_pattern_match.py:67:        keys = None
  tests\test_pattern_match.py:68:        for T_idx in [400, 450, 500]:
> tests\test_pattern_match.py:69:            r = pattern_match_single(prices, T_idx)
  tests\test_pattern_match.py:70:            if r is None:
  tests\test_pattern_match.py:71:                continue
  tests\test_pattern_match.py:72:            if keys is None:
  tests\test_pattern_match.py:73:                keys = set(r.keys())
  tests\test_pattern_match.py:74:            else:
  tests\test_pattern_match.py:75:                assert set(r.keys()) == keys
  tests\test_pattern_match.py:76:
  tests\test_pattern_match.py:77:    def test_cos_prefilter_top_effect(self):
  tests\test_pattern_match.py:79:        prices = _generate_random_walk(600)
  tests\test_pattern_match.py:80:        T_idx = 500
> tests\test_pattern_match.py:81:        r1 = pattern_match_single(prices, T_idx, cos_prefilter_top=50)
> tests\test_pattern_match.py:82:        r2 = pattern_match_single(prices, T_idx, cos_prefilter_top=200)
  tests\test_pattern_match.py:83:        # 两者都不应为 None（如果数据足够）
  tests\test_pattern_match.py:84:        assert r1 is not None
  tests\test_pattern_match.py:85:        assert r2 is not None
  tests\test_pattern_match.py:86:        # 注意: 不同 top-k 可能产生不同特征值（因为 sigma_fast 也变了）
  tests\test_pattern_match.py:87:        # 这里只验证两者都有效
  tests\test_pattern_match.py:88:
  tests\test_pattern_match.py:89:    def test_deterministic_output(self):
  tests\test_pattern_match.py:90:        """相同输入应产生相同输出（无随机性）"""
  tests\test_pattern_match.py:91:        prices = _generate_random_walk(600)
  tests\test_pattern_match.py:92:        T_idx = 500
> tests\test_pattern_match.py:93:        r1 = pattern_match_single(prices, T_idx)
> tests\test_pattern_match.py:94:        r2 = pattern_match_single(prices, T_idx)
  tests\test_pattern_match.py:95:        assert r1 is not None
  tests\test_pattern_match.py:96:        assert r2 is not None
  tests\test_pattern_match.py:97:        for key in r1:
  tests\test_pattern_match.py:98:            assert r1[key] == pytest.approx(r2[key])
  tests\test_pattern_match.py:99:
  tests\test_pattern_match.py:100:
  tests\test_pattern_match.py:101:class TestComputePatternFeatures:
  tests\test_pattern_match.py:102:    """compute_pattern_features 单元测试 — 固定输入验证"""
  tests\test_pattern_match.py:195:        prices = _generate_random_walk(600)
  tests\test_pattern_match.py:196:        T_idx = 500
> tests\test_pattern_match.py:197:        r1 = pattern_match_single(prices, T_idx)
  tests\test_pattern_match.py:198:        r2 = extract_morph_features(prices, T_idx)
  tests\test_pattern_match.py:199:        assert (r1 is None) == (r2 is None)
  tests\test_pattern_match.py:200:        if r1 is not None:
  tests\test_pattern_match.py:201:            for key in r1:
  tests\test_pattern_match.py:202:                assert r1[key] == pytest.approx(r2[key])
  tests\test_pattern_match.py:203:
  tests\test_pattern_match.py:204:
  tests\test_pattern_match.py:205:if __name__ == "__main__":
  verify_batch.py:68:all_pass = True
  verify_batch.py:69:for T_idx in sample_Ts:
> verify_batch.py:70:    single_res = etf_core.pattern_match_single(
  verify_batch.py:71:        prices,
  verify_batch.py:72:        int(T_idx),
  verify_batch.py:73:        k,
  verify_batch.py:74:        L_query,
  verify_batch.py:75:        T_back,
  verify_batch.py:76:        match_step,
  verify_batch.py:77:        M_forward,
  verify_batch.py:78:        dtw_window,
  verify_batch.py:79:        cos_prefilter_top,
  verify_batch.py:80:    )
> verify_batch.py:81:    features, mask = etf_core.pattern_match_batch(
  verify_batch.py:82:        prices,
  verify_batch.py:83:        np.array([int(T_idx)], dtype=np.int64),
  verify_batch.py:84:        k,
  verify_batch.py:85:        L_query,
  verify_batch.py:86:        T_back,
  verify_batch.py:87:        match_step,
  verify_batch.py:88:        M_forward,
  verify_batch.py:89:        dtw_window,
  verify_batch.py:102:print("\n=== 测试 2：边界条件 ===")
  verify_batch.py:103:boundary_Ts = np.array([0, 5, min_T - 1, min_T], dtype=np.int64)
> verify_batch.py:104:features, mask = etf_core.pattern_match_batch(
  verify_batch.py:105:    prices,
  verify_batch.py:106:    boundary_Ts,
  verify_batch.py:107:    k,
  verify_batch.py:108:    L_query,
  verify_batch.py:109:    T_back,
  verify_batch.py:110:    match_step,
  verify_batch.py:111:    M_forward,
  verify_batch.py:112:    dtw_window,
  verify_batch.py:122:# 用一个明显有效的 T_idx 验证 mask 为 True
  verify_batch.py:123:valid_T = 2 * L_query + M_forward + 10
> verify_batch.py:124:_, single_mask = etf_core.pattern_match_batch(
  verify_batch.py:125:    prices,
  verify_batch.py:126:    np.array([valid_T], dtype=np.int64),
  verify_batch.py:127:    k,
  verify_batch.py:128:    L_query,
  verify_batch.py:129:    T_back,
  verify_batch.py:130:    match_step,
  verify_batch.py:131:    M_forward,
  verify_batch.py:132:    dtw_window,
  verify_batch.py:149:
  verify_batch.py:150:# 预热
> verify_batch.py:151:_ = etf_core.pattern_match_single(
  verify_batch.py:152:    prices, int(test_Ts[0]), k, L_query, T_back,
  verify_batch.py:153:    match_step, M_forward, dtw_window, cos_prefilter_top,
  verify_batch.py:154:)
> verify_batch.py:155:_ = etf_core.pattern_match_batch(
  verify_batch.py:156:    prices, test_Ts[:5], k, L_query, T_back,
  verify_batch.py:157:    match_step, M_forward, dtw_window, cos_prefilter_top,
  verify_batch.py:158:)
  verify_batch.py:159:
  verify_batch.py:160:# 100 次 single
  verify_batch.py:161:single_times = []
  verify_batch.py:162:for _ in range(3):
  verify_batch.py:163:    t0 = time.perf_counter()
  verify_batch.py:164:    for T_idx in test_Ts:
> verify_batch.py:165:        etf_core.pattern_match_single(
  verify_batch.py:166:            prices,
  verify_batch.py:167:            int(T_idx),
  verify_batch.py:168:            k,
  verify_batch.py:169:            L_query,
  verify_batch.py:170:            perf_T_back,
  verify_batch.py:171:            perf_match_step,
  verify_batch.py:172:            M_forward,
  verify_batch.py:173:            dtw_window,
  verify_batch.py:181:for _ in range(3):
  verify_batch.py:182:    t0 = time.perf_counter()
> verify_batch.py:183:    features, mask = etf_core.pattern_match_batch(
  verify_batch.py:184:        prices,
  verify_batch.py:185:        test_Ts,
  verify_batch.py:186:        k,
  verify_batch.py:187:        L_query,
  verify_batch.py:188:        perf_T_back,
  verify_batch.py:189:        perf_match_step,
  verify_batch.py:190:        M_forward,
  verify_batch.py:191:        dtw_window,
  verify_batch.py:206:print("\n=== 测试 4：空 t_indices ===")
  verify_batch.py:207:empty_Ts = np.array([], dtype=np.int64)
> verify_batch.py:208:features, mask = etf_core.pattern_match_batch(
  verify_batch.py:209:    prices, empty_Ts, k, L_query, T_back, match_step, M_forward, dtw_window, cos_prefilter_top)
  verify_batch.py:210:print(f"features shape: {features.shape}")
  verify_batch.py:211:print(f"mask shape: {mask.shape}")
  verify_batch.py:212:assert features.shape == (0, 15), f"空输入应返回 (0,15) 的 features, 实际: {features.shape}"
  verify_batch.py:213:assert mask.shape == (0,), f"空输入应返回 (0,) 的 mask, 实际: {mask.shape}"
  verify_batch.py:214:print("空 t_indices 测试通过")
  verify_batch.py:215:
  verify_batch.py:216:print("\n=== 测试 5：全部无效 T_idx ===")
  verify_batch.py:217:all_invalid = np.array([0, 1, 2, 5, min_T - 1], dtype=np.int64)
> verify_batch.py:218:features, mask = etf_core.pattern_match_batch(
  verify_batch.py:219:    prices, all_invalid, k, L_query, T_back, match_step, M_forward, dtw_window, cos_prefilter_top
)
  verify_batch.py:220:print(f"features shape: {features.shape}, mask: {mask}")
  verify_batch.py:221:assert features.shape[0] == 0, f"全部无效时应返回 0 有效样本"
  verify_batch.py:222:assert not mask.any(), f"全部无效时 mask 应全为 False"
  verify_batch.py:223:print("全部无效 T_idx 测试通过")
  verify_batch.py:224:
  verify_batch.py:225:print("\n=== 测试 6：单有效 T_idx ===")
  verify_batch.py:226:valid_T = int(2 * L_query + M_forward + 100)
  verify_batch.py:227:single_T = np.array([valid_T], dtype=np.int64)
> verify_batch.py:228:features, mask = etf_core.pattern_match_batch(
  verify_batch.py:229:    prices, single_T, k, L_query, T_back, match_step, M_forward, dtw_window, cos_prefilter_top)
  verify_batch.py:230:print(f"features shape: {features.shape}, mask: {mask}")
  verify_batch.py:231:assert mask[0], f"T_idx={valid_T} 应为有效"
  verify_batch.py:232:assert features.shape[0] == 1, "应恰好返回 1 个有效样本"
  verify_batch.py:233:assert features.shape[1] == 15, "应有 15 维特征"
  verify_batch.py:234:# 与 single 结果一致
> verify_batch.py:235:single_res = etf_core.pattern_match_single(
  verify_batch.py:236:    prices, valid_T, k, L_query, T_back, match_step, M_forward, dtw_window, cos_prefilter_top)
  verify_batch.py:237:assert single_res is not None, "single 也不应为 None"
  verify_batch.py:238:for i, key in enumerate(etf_core.FEATURE_KEYS):
  verify_batch.py:239:    diff = abs(float(single_res[key]) - float(features[0, i]))
  verify_batch.py:240:    assert diff < 1e-6, f"单样本 batch vs single 不一致: {key}, diff={diff:.2e}"
  verify_batch.py:241:print("单有效 T_idx 测试通过")
  verify_batch.py:242:
  verify_batch.py:243:print("\n=== 测试 7：match_step <= 0 应抛异常 ===")
  verify_batch.py:244:try:
> verify_batch.py:245:    etf_core.pattern_match_single(
  verify_batch.py:246:        prices, int(valid_T), k, L_query, T_back, 0, M_forward, dtw_window, cos_prefilter_top)
  verify_batch.py:247:    assert False, "match_step=0 应抛出异常"
  verify_batch.py:248:except Exception as e:
> verify_batch.py:249:    print(f"pattern_match_single(match_step=0): {type(e).__name__}: {e}")
  verify_batch.py:250:    assert "match_step" in str(e).lower()
  verify_batch.py:251:
  verify_batch.py:252:try:
> verify_batch.py:253:    etf_core.pattern_match_batch(
  verify_batch.py:254:        prices, np.array([valid_T], dtype=np.int64),
  verify_batch.py:255:        k, L_query, T_back, 0, M_forward, dtw_window, cos_prefilter_top)
  verify_batch.py:256:    assert False, "match_step=0 应抛出异常"
  verify_batch.py:257:except Exception as e:
> verify_batch.py:258:    print(f"pattern_match_batch(match_step=0): {type(e).__name__}: {e}")
  verify_batch.py:259:    assert "match_step" in str(e).lower()
  verify_batch.py:260:
  verify_batch.py:261:print("match_step 守卫测试通过")
  verify_batch.py:262:
  verify_batch.py:263:print("\n全部测试通过")
  verify_etf_core.py:194:
  verify_etf_core.py:195:
> verify_etf_core.py:196:def verify_pattern_match_single():
  verify_etf_core.py:197:    """验证 pattern_match_single — 核心验证"""
  verify_etf_core.py:198:    print("\n" + "=" * 60)
  verify_etf_core.py:199:    print("📐 pattern_match_single (核心验证)")
  verify_etf_core.py:200:    print("=" * 60)
  verify_etf_core.py:201:
  verify_etf_core.py:202:    all_ok = True
  verify_etf_core.py:203:    np.random.seed(42)
  verify_etf_core.py:204:    prices = 100.0 * np.cumprod(1.0 + np.random.randn(800) * 0.02)
  verify_etf_core.py:207:        print(f"\n  T_idx={T_idx}:")
  verify_etf_core.py:208:        py_r = py_pattern_match(prices, T_idx)
> verify_etf_core.py:209:        cpp_r = etf_core.pattern_match_single(prices, T_idx)
  verify_etf_core.py:210:
  verify_etf_core.py:211:        if py_r is None and cpp_r is None:
  verify_etf_core.py:212:            print("  ✅ both None")
  verify_etf_core.py:213:            continue
  verify_etf_core.py:214:        if py_r is None or cpp_r is None:
  verify_etf_core.py:215:            print(f"  ❌ mismatch: py None={py_r is None} cpp None={cpp_r is None}")
  verify_etf_core.py:216:            all_ok = False
  verify_etf_core.py:217:            continue
  verify_etf_core.py:264:    t0 = time.perf_counter()
  verify_etf_core.py:265:    for _ in range(3):
> verify_etf_core.py:266:        etf_core.pattern_match_single(prices, T_idx)
  verify_etf_core.py:267:    cpp_pm = (time.perf_counter() - t0) / 3 * 1000
  verify_etf_core.py:268:
  verify_etf_core.py:269:    print(f"\n  pattern_match_single:")
  verify_etf_core.py:270:    print(f"    Python: {py_pm:.1f} ms/call")
  verify_etf_core.py:271:    print(f"    C++:    {cpp_pm:.1f} ms/call")
  verify_etf_core.py:272:    print(f"    加速比: {py_pm/cpp_pm:.1f}x")
  verify_etf_core.py:273:
  verify_etf_core.py:274:
  verify_etf_core.py:288:    if args.quick:
  verify_etf_core.py:289:        results["standardize_returns"] = verify_standardize_returns()
> verify_etf_core.py:290:        results["pattern_match"] = verify_pattern_match_single()
  verify_etf_core.py:291:    else:
  verify_etf_core.py:292:        results["standardize_returns"] = verify_standardize_returns()
  verify_etf_core.py:293:        results["cosine_similarity"] = verify_cosine_similarity()
  verify_etf_core.py:294:        results["dtw_distance"] = verify_dtw_distance()
  verify_etf_core.py:295:        results["compute_adx"] = verify_compute_adx()
> verify_etf_core.py:296:        results["pattern_match"] = verify_pattern_match_single()
  verify_etf_core.py:297:
  verify_etf_core.py:298:    verify_performance()
  verify_etf_core.py:299:
  verify_etf_core.py:300:    print("\n" + "=" * 60)
  verify_etf_core.py:301:    passed = sum(results.values())
  verify_etf_core.py:302:    total = len(results)
  verify_etf_core.py:303:    print(f"  验证结果: {passed}/{total} 通过")
  verify_etf_core.py:304:    print("=" * 60)



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Select-String -Path '"'src\\cpp\\etf_core.cpp' -Pattern '"'^std::optional<PatternResult> pattern_match_core'"' -Encoding UTF8 -Context 0,260" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 193ms:

> src\cpp\etf_core.cpp:551:std::optional<PatternResult> pattern_match_core(
  src\cpp\etf_core.cpp:552:    const double* prices, py::ssize_t n_prices,
  src\cpp\etf_core.cpp:553:    int T_idx, int k, int L_query, int T_back,
  src\cpp\etf_core.cpp:554:    int match_step, int M_forward, int dtw_window,
  src\cpp\etf_core.cpp:555:    int cos_prefilter_top,
  src\cpp\etf_core.cpp:556:    const std::vector<double>& query_rets,
  src\cpp\etf_core.cpp:557:    py::ssize_t search_start, py::ssize_t search_end,
  src\cpp\etf_core.cpp:558:    const std::vector<std::vector<double>>* precomputed_rets
  src\cpp\etf_core.cpp:559:) {
  src\cpp\etf_core.cpp:560:    py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());
  src\cpp\etf_core.cpp:561:
  src\cpp\etf_core.cpp:562:    // ═══ 第1遍：余弦相似度 + 快速形状距离（全量候选）═══
  src\cpp\etf_core.cpp:563:    std::vector<MatchCandidate> cos_candidates;
  src\cpp\etf_core.cpp:564:    std::vector<double> fast_shape_dists;
  src\cpp\etf_core.cpp:565:
  src\cpp\etf_core.cpp:566:    for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step
) {
  src\cpp\etf_core.cpp:567:        py::ssize_t hist_start = hist_end - L_query + 1;
  src\cpp\etf_core.cpp:568:        if (hist_start < 0) continue;
  src\cpp\etf_core.cpp:569:
  src\cpp\etf_core.cpp:570:        // 获取标准化收益率：缓存优先，否则现场计算
  src\cpp\etf_core.cpp:571:        const std::vector<double>* hist_rets_ptr = nullptr;
  src\cpp\etf_core.cpp:572:        std::vector<double> hist_rets_scratch;
  src\cpp\etf_core.cpp:573:
  src\cpp\etf_core.cpp:574:        if (precomputed_rets && hist_end < static_cast<py::ssize_t>(precomputed_rets->size()
)) {
  src\cpp\etf_core.cpp:575:            hist_rets_ptr = &(*precomputed_rets)[hist_end];
  src\cpp\etf_core.cpp:576:        } else {
  src\cpp\etf_core.cpp:577:            auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
  src\cpp\etf_core.cpp:578:            if (static_cast<py::ssize_t>(hist_prices_vec.size()) >= L_query) {
  src\cpp\etf_core.cpp:579:                hist_rets_scratch = standardize_returns_cpp(hist_prices_vec.data(), L_query)
;
  src\cpp\etf_core.cpp:580:                hist_rets_ptr = &hist_rets_scratch;
  src\cpp\etf_core.cpp:581:            }
  src\cpp\etf_core.cpp:582:        }
  src\cpp\etf_core.cpp:583:
  src\cpp\etf_core.cpp:584:        if (!hist_rets_ptr || hist_rets_ptr->size() < 2) continue;
  src\cpp\etf_core.cpp:585:
  src\cpp\etf_core.cpp:586:        const auto& hist_rets = *hist_rets_ptr;
  src\cpp\etf_core.cpp:587:
  src\cpp\etf_core.cpp:588:        // 余弦相似度
  src\cpp\etf_core.cpp:589:        double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
  src\cpp\etf_core.cpp:590:        py::ssize_t min_len = std::min(static_cast<py::ssize_t>(hist_rets.size()), n_query);
  src\cpp\etf_core.cpp:591:        for (py::ssize_t i = 0; i < min_len; ++i) {
  src\cpp\etf_core.cpp:592:            dot += hist_rets[i] * query_rets[i];
  src\cpp\etf_core.cpp:593:            nx2 += hist_rets[i] * hist_rets[i];
  src\cpp\etf_core.cpp:594:            ny2 += query_rets[i] * query_rets[i];
  src\cpp\etf_core.cpp:595:        }
  src\cpp\etf_core.cpp:596:        double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
  src\cpp\etf_core.cpp:597:        double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;
  src\cpp\etf_core.cpp:598:
  src\cpp\etf_core.cpp:599:        // 快速形状距离
  src\cpp\etf_core.cpp:600:        double fast_d2 = 0.0;
  src\cpp\etf_core.cpp:601:        for (py::ssize_t i = 0; i < min_len; ++i) {
  src\cpp\etf_core.cpp:602:            double diff = hist_rets[i] - query_rets[i];
  src\cpp\etf_core.cpp:603:            fast_d2 += diff * diff;
  src\cpp\etf_core.cpp:604:        }
  src\cpp\etf_core.cpp:605:        fast_shape_dists.push_back(std::sqrt(fast_d2 / min_len));
  src\cpp\etf_core.cpp:606:
  src\cpp\etf_core.cpp:607:        if (cos_s > 0) {
  src\cpp\etf_core.cpp:608:            cos_candidates.push_back({hist_end, hist_start, cos_s, hist_rets});
  src\cpp\etf_core.cpp:609:        }
  src\cpp\etf_core.cpp:610:    }
  src\cpp\etf_core.cpp:611:
  src\cpp\etf_core.cpp:612:    if (cos_candidates.size() < 3) return std::nullopt;
  src\cpp\etf_core.cpp:613:
  src\cpp\etf_core.cpp:614:    // sigma_fast = std(RMSD) / (2*sqrt(L_query-1))
  src\cpp\etf_core.cpp:615:    double sigma_fast = 1.0;
  src\cpp\etf_core.cpp:616:    if (fast_shape_dists.size() > 1) {
  src\cpp\etf_core.cpp:617:        double mean_fd = std::accumulate(fast_shape_dists.begin(), fast_shape_dists.end(), 0
.0)
  src\cpp\etf_core.cpp:618:                        / fast_shape_dists.size();
  src\cpp\etf_core.cpp:619:        double var_fd = 0.0;
  src\cpp\etf_core.cpp:620:        for (auto d : fast_shape_dists) var_fd += (d - mean_fd) * (d - mean_fd);
  src\cpp\etf_core.cpp:621:        var_fd /= fast_shape_dists.size();
  src\cpp\etf_core.cpp:622:        sigma_fast = std::sqrt(var_fd) / (2.0 * std::sqrt(static_cast<double>(L_query - 1)))
;
  src\cpp\etf_core.cpp:623:    }
  src\cpp\etf_core.cpp:624:    sigma_fast = std::max(sigma_fast, 1e-12);
  src\cpp\etf_core.cpp:625:
  src\cpp\etf_core.cpp:626:    // 余弦排序 + 全量边界
  src\cpp\etf_core.cpp:627:    std::sort(cos_candidates.begin(), cos_candidates.end(),
  src\cpp\etf_core.cpp:628:              [](const MatchCandidate& a, const MatchCandidate& b) { return a.cos_s > b.cos_
s; });
  src\cpp\etf_core.cpp:629:
  src\cpp\etf_core.cpp:630:    double global_min_cos = cos_candidates.back().cos_s;
  src\cpp\etf_core.cpp:631:    double global_max_cos = cos_candidates.front().cos_s;
  src\cpp\etf_core.cpp:632:
  src\cpp\etf_core.cpp:633:    int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
  src\cpp\etf_core.cpp:634:    cos_candidates.resize(n_cos);
  src\cpp\etf_core.cpp:635:
  src\cpp\etf_core.cpp:636:    // ═══ 第2遍：DTW 精排 (仅 top-N) ═══
  src\cpp\etf_core.cpp:637:    std::vector<double> dtw_dists, cos_sims, future_rets;
  src\cpp\etf_core.cpp:638:    std::vector<py::ssize_t> match_ends;
  src\cpp\etf_core.cpp:639:    dtw_dists.reserve(n_cos);
  src\cpp\etf_core.cpp:640:    cos_sims.reserve(n_cos);
  src\cpp\etf_core.cpp:641:    future_rets.reserve(n_cos);
  src\cpp\etf_core.cpp:642:    match_ends.reserve(n_cos);
  src\cpp\etf_core.cpp:643:
  src\cpp\etf_core.cpp:644:    for (const auto& cand : cos_candidates) {
  src\cpp\etf_core.cpp:645:        py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
  src\cpp\etf_core.cpp:646:        double dtw_d = dtw_distance_span(cand.hist_rets.data(), hn,
  src\cpp\etf_core.cpp:647:                                          query_rets.data(), n_query, dtw_window);
  src\cpp\etf_core.cpp:648:
  src\cpp\etf_core.cpp:649:        dtw_dists.push_back(dtw_d);
  src\cpp\etf_core.cpp:650:        cos_sims.push_back(cand.cos_s);
  src\cpp\etf_core.cpp:651:
  src\cpp\etf_core.cpp:652:        py::ssize_t fut_end = cand.hist_end + M_forward;
  src\cpp\etf_core.cpp:653:        if (fut_end < n_prices && fut_end < T_idx) {
  src\cpp\etf_core.cpp:654:            future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
  src\cpp\etf_core.cpp:655:        } else {
  src\cpp\etf_core.cpp:656:            future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
  src\cpp\etf_core.cpp:657:        }
  src\cpp\etf_core.cpp:658:        match_ends.push_back(cand.hist_end);
  src\cpp\etf_core.cpp:659:    }
  src\cpp\etf_core.cpp:660:
  src\cpp\etf_core.cpp:661:    if (dtw_dists.size() < 3) return std::nullopt;
  src\cpp\etf_core.cpp:662:
  src\cpp\etf_core.cpp:663:    // sim_dtw = exp(-dtw/sigma)
  src\cpp\etf_core.cpp:664:    double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;
  src\cpp\etf_core.cpp:665:
  src\cpp\etf_core.cpp:666:    std::vector<double> sim_dtw(dtw_dists.size());
  src\cpp\etf_core.cpp:667:    double min_dtw_v = std::numeric_limits<double>::max();
  src\cpp\etf_core.cpp:668:    double max_dtw_v = std::numeric_limits<double>::lowest();
  src\cpp\etf_core.cpp:669:    for (size_t i = 0; i < dtw_dists.size(); ++i) {
  src\cpp\etf_core.cpp:670:        sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
  src\cpp\etf_core.cpp:671:        min_dtw_v = std::min(min_dtw_v, sim_dtw[i]);
  src\cpp\etf_core.cpp:672:        max_dtw_v = std::max(max_dtw_v, sim_dtw[i]);
  src\cpp\etf_core.cpp:673:    }
  src\cpp\etf_core.cpp:674:
  src\cpp\etf_core.cpp:675:    // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
  src\cpp\etf_core.cpp:676:    double range_dtw = (max_dtw_v - min_dtw_v > 1e-12) ? (max_dtw_v - min_dtw_v) : 1.0;
  src\cpp\etf_core.cpp:677:    double range_cos_val = (global_max_cos - global_min_cos > 1e-12)
  src\cpp\etf_core.cpp:678:                           ? (global_max_cos - global_min_cos) : 1.0;
  src\cpp\etf_core.cpp:679:
  src\cpp\etf_core.cpp:680:    struct Scored { double score, fut_ret; py::ssize_t end_idx; };
  src\cpp\etf_core.cpp:681:    std::vector<Scored> scored;
  src\cpp\etf_core.cpp:682:    scored.reserve(sim_dtw.size());
  src\cpp\etf_core.cpp:683:    for (size_t i = 0; i < sim_dtw.size(); ++i) {
  src\cpp\etf_core.cpp:684:        double nd = (sim_dtw[i] - min_dtw_v) / range_dtw;
  src\cpp\etf_core.cpp:685:        double nc = (cos_sims[i] - global_min_cos) / range_cos_val;
  src\cpp\etf_core.cpp:686:        scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
  src\cpp\etf_core.cpp:687:    }
  src\cpp\etf_core.cpp:688:
  src\cpp\etf_core.cpp:689:    std::sort(scored.begin(), scored.end(),
  src\cpp\etf_core.cpp:690:              [](const Scored& a, const Scored& b) { return a.score > b.score; });
  src\cpp\etf_core.cpp:691:
  src\cpp\etf_core.cpp:692:    int top_k = std::min(k, static_cast<int>(scored.size()));
  src\cpp\etf_core.cpp:693:
  src\cpp\etf_core.cpp:694:    // 过滤 NaN 未来收益
  src\cpp\etf_core.cpp:695:    std::vector<double> valid_scores, valid_frets;
  src\cpp\etf_core.cpp:696:    std::vector<py::ssize_t> valid_ends;
  src\cpp\etf_core.cpp:697:    for (int i = 0; i < top_k; ++i) {
  src\cpp\etf_core.cpp:698:        if (!std::isnan(scored[i].fut_ret)) {
  src\cpp\etf_core.cpp:699:            valid_scores.push_back(scored[i].score);
  src\cpp\etf_core.cpp:700:            valid_frets.push_back(scored[i].fut_ret);
  src\cpp\etf_core.cpp:701:            valid_ends.push_back(scored[i].end_idx);
  src\cpp\etf_core.cpp:702:        }
  src\cpp\etf_core.cpp:703:    }
  src\cpp\etf_core.cpp:704:    if (valid_scores.size() < 2) return std::nullopt;
  src\cpp\etf_core.cpp:705:
  src\cpp\etf_core.cpp:706:    return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
  src\cpp\etf_core.cpp:707:}
  src\cpp\etf_core.cpp:708:
  src\cpp\etf_core.cpp:709:} // namespace
  src\cpp\etf_core.cpp:710:
  src\cpp\etf_core.cpp:711:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:712:// 第六部分-A: 单点形态匹配（薄包装 → pattern_match_core）
  src\cpp\etf_core.cpp:713:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:714:py::object pattern_match_single(
  src\cpp\etf_core.cpp:715:    ArrD prices_arr,
  src\cpp\etf_core.cpp:716:    int T_idx,
  src\cpp\etf_core.cpp:717:    int k = 10,
  src\cpp\etf_core.cpp:718:    int L_query = 20,
  src\cpp\etf_core.cpp:719:    int T_back = 750,
  src\cpp\etf_core.cpp:720:    int match_step = 1,
  src\cpp\etf_core.cpp:721:    int M_forward = 5,
  src\cpp\etf_core.cpp:722:    int dtw_window = 5,
  src\cpp\etf_core.cpp:723:    int cos_prefilter_top = 50
  src\cpp\etf_core.cpp:724:) {
  src\cpp\etf_core.cpp:725:    auto prices_buf = prices_arr.unchecked<1>();
  src\cpp\etf_core.cpp:726:    py::ssize_t n_prices = prices_buf.shape(0);
  src\cpp\etf_core.cpp:727:    const double* prices = prices_buf.data(0);
  src\cpp\etf_core.cpp:728:
  src\cpp\etf_core.cpp:729:    // ── 输入校验 ──
  src\cpp\etf_core.cpp:730:    if (T_idx < 0 || static_cast<py::ssize_t>(T_idx) >= n_prices) {
  src\cpp\etf_core.cpp:731:        throw std::out_of_range("T_idx must satisfy 0 <= T_idx < len(prices), got " + std::t
o_string(T_idx));
  src\cpp\etf_core.cpp:732:    }
  src\cpp\etf_core.cpp:733:    if (L_query < 3) {
  src\cpp\etf_core.cpp:734:        throw std::invalid_argument("L_query must be >= 3, got " + std::to_string(L_query));
  src\cpp\etf_core.cpp:735:    }
  src\cpp\etf_core.cpp:736:    if (T_back <= 0) {
  src\cpp\etf_core.cpp:737:        throw std::invalid_argument("T_back must be > 0, got " + std::to_string(T_back));
  src\cpp\etf_core.cpp:738:    }
  src\cpp\etf_core.cpp:739:    if (k <= 0) {
  src\cpp\etf_core.cpp:740:        throw std::invalid_argument("k must be > 0, got " + std::to_string(k));
  src\cpp\etf_core.cpp:741:    }
  src\cpp\etf_core.cpp:742:    if (M_forward < 1) {
  src\cpp\etf_core.cpp:743:        throw std::invalid_argument("M_forward must be >= 1, got " + std::to_string(M_forwar
d));
  src\cpp\etf_core.cpp:744:    }
  src\cpp\etf_core.cpp:745:    if (match_step <= 0) {
  src\cpp\etf_core.cpp:746:        throw std::invalid_argument("match_step must be > 0");
  src\cpp\etf_core.cpp:747:    }
  src\cpp\etf_core.cpp:748:    if (dtw_window < 0) {
  src\cpp\etf_core.cpp:749:        throw std::invalid_argument("dtw_window must be >= 0, got " + std::to_string(dtw_win
dow));
  src\cpp\etf_core.cpp:750:    }
  src\cpp\etf_core.cpp:751:    if (cos_prefilter_top <= 0) {
  src\cpp\etf_core.cpp:752:        throw std::invalid_argument("cos_prefilter_top must be > 0, got " + std::to_string(c
os_prefilter_top));
  src\cpp\etf_core.cpp:753:    }
  src\cpp\etf_core.cpp:754:    if (T_idx < L_query + M_forward + 10) return py::none();
  src\cpp\etf_core.cpp:755:    if (T_idx - L_query + 1 < 0) return py::none();
  src\cpp\etf_core.cpp:756:
  src\cpp\etf_core.cpp:757:    // 查询窗口标准化
  src\cpp\etf_core.cpp:758:    auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
  src\cpp\etf_core.cpp:759:    if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();
  src\cpp\etf_core.cpp:760:
  src\cpp\etf_core.cpp:761:    std::vector<double> query_rets;
  src\cpp\etf_core.cpp:762:    {
  src\cpp\etf_core.cpp:763:        py::gil_scoped_release release;
  src\cpp\etf_core.cpp:764:        query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
  src\cpp\etf_core.cpp:765:    }
  src\cpp\etf_core.cpp:766:    if (query_rets.size() < 2) return py::none();
  src\cpp\etf_core.cpp:767:
  src\cpp\etf_core.cpp:768:    py::ssize_t search_end = T_idx - L_query;
  src\cpp\etf_core.cpp:769:    if (search_end < L_query) return py::none();
  src\cpp\etf_core.cpp:770:    py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
  src\cpp\etf_core.cpp:771:                                        py::ssize_t(T_idx - T_back));
  src\cpp\etf_core.cpp:772:
  src\cpp\etf_core.cpp:773:    // ── 委托共享核心（无预计算缓存，现场标准化）──
  src\cpp\etf_core.cpp:774:    std::optional<PatternResult> result_opt;
  src\cpp\etf_core.cpp:775:    {
  src\cpp\etf_core.cpp:776:        py::gil_scoped_release release;
  src\cpp\etf_core.cpp:777:        result_opt = pattern_match_core(
  src\cpp\etf_core.cpp:778:            prices, n_prices, T_idx, k, L_query, T_back,
  src\cpp\etf_core.cpp:779:            match_step, M_forward, dtw_window, cos_prefilter_top,
  src\cpp\etf_core.cpp:780:            query_rets, search_start, search_end,
  src\cpp\etf_core.cpp:781:            nullptr  // 无预计算缓存
  src\cpp\etf_core.cpp:782:        );
  src\cpp\etf_core.cpp:783:    }
  src\cpp\etf_core.cpp:784:
  src\cpp\etf_core.cpp:785:    if (!result_opt.has_value()) return py::none();
  src\cpp\etf_core.cpp:786:
  src\cpp\etf_core.cpp:787:    // ── 构造返回值 ──
  src\cpp\etf_core.cpp:788:    py::dict result;
  src\cpp\etf_core.cpp:789:    result["top1_sim"] = result_opt->top1_sim;
  src\cpp\etf_core.cpp:790:    result["top5_avg_sim"] = result_opt->top5_avg_sim;
  src\cpp\etf_core.cpp:791:    result["sim_decay"] = result_opt->sim_decay;
  src\cpp\etf_core.cpp:792:    result["sim_variance"] = result_opt->sim_variance;
  src\cpp\etf_core.cpp:793:    result["match_distance_ratio"] = result_opt->match_distance_ratio;
  src\cpp\etf_core.cpp:794:    result["avg_future_ret"] = result_opt->avg_future_ret;
  src\cpp\etf_core.cpp:795:    result["weighted_future_ret"] = result_opt->weighted_future_ret;
  src\cpp\etf_core.cpp:796:    result["median_future_ret"] = result_opt->median_future_ret;
  src\cpp\etf_core.cpp:797:    result["ret_sign_consistency"] = result_opt->ret_sign_consistency;
  src\cpp\etf_core.cpp:798:    result["best_match_ret"] = result_opt->best_match_ret;
  src\cpp\etf_core.cpp:799:    result["max_dd_in_matches"] = result_opt->max_dd_in_matches;
  src\cpp\etf_core.cpp:800:    result["match_time_span"] = result_opt->match_time_span;
  src\cpp\etf_core.cpp:801:    result["match_time_span_ratio"] = result_opt->match_time_span_ratio;
  src\cpp\etf_core.cpp:802:    result["match_cluster_ratio"] = result_opt->match_cluster_ratio;
  src\cpp\etf_core.cpp:803:    result["n_matches_above_thresh"] = result_opt->n_matches_above_thresh;
  src\cpp\etf_core.cpp:804:    return result;
  src\cpp\etf_core.cpp:805:}
  src\cpp\etf_core.cpp:806:
  src\cpp\etf_core.cpp:807:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:808:// 第七部分: 批量形态匹配 (v3 新增)
  src\cpp\etf_core.cpp:809:// ═══════════════════════════════════════════════════════════════
  src\cpp\etf_core.cpp:810:
  src\cpp\etf_core.cpp:811:py::tuple pattern_match_batch(



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; New-Item -ItemType Directory -Path '"'examples' -Force | Out-Null; "'$lines = @('"'# Quickstart example for etf_core — pip install etf-pattern-match-pybind11 && python examples/quickstart.py', '# Provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17', '', 'import etf_core', 'import numpy as np', '', 'rng = np.random.default_rng(42)', 'prices = rng.standard_normal(100).cumsum() + 100.0', '', 'dtw = etf_core.dtw_distance(prices[10:20], prices[20:30])', 'feature_a = np.array([0.5, -0.2, 1.0])', 'feature_b = np.array([0.4, -0.1, 0.8])', 'cosine = etf_core.cosine_similarity(feature_a, feature_b)', '', 'params = {\"k\": 5, \"L_query\": 10, \"T_back\": 60, \"M_forward\": 3}', 'single = etf_core.pattern_match_single(prices, T_idx=80, **params)', 't_indices = np.array([70, 80, 90], dtype=np.int64)', 'batch, valid = etf_core.pattern_match_batch(prices, t_indices, **params)', '', 'print(f\"DTW distance: {dtw:.4f}\")', 'print(f\"Cosine similarity: {cosine:.4f}\")', 'print(\"Single-match features:\", single)', 'print(\"Batch feature matrix:\", batch)', 'print(\"Batch valid mask:\", valid)'); "'$content = [string]::Join("`n", $lines) + "`n"; $path = [System.IO.Path]::GetFullPath('"'examples\\quickstart.py'); [System.IO.File]::WriteAllText("'$path, $content, [System.Text.UTF8Encoding]::new($false))' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 142ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $path = '"'examples\\quickstart.py'; "'$content = Get-Content -Raw -Encoding UTF8 $path; $bytes = [System.IO.File]::ReadAllBytes((Resolve-Path $path)); "Lines: $((Get-Content -Encoding UTF8 $path).Count)"; "UTF-8 BOM: $($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF)"; '"'--- file ---'; "'$content; '"'--- git diff --stat ---'; git diff --stat -- examples/quickstart.py; '--- git diff ---'; git diff -- examples/quickstart.py" in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 191ms:
Lines: 24
UTF-8 BOM: False
--- file ---
# Quickstart example for etf_core — pip install etf-pattern-match-pybind11 && python examples/quickstart.py
# Provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17

import etf_core
import numpy as np

rng = np.random.default_rng(42)
prices = rng.standard_normal(100).cumsum() + 100.0

dtw = etf_core.dtw_distance(prices[10:20], prices[20:30])
feature_a = np.array([0.5, -0.2, 1.0])
feature_b = np.array([0.4, -0.1, 0.8])
cosine = etf_core.cosine_similarity(feature_a, feature_b)

params = {"k": 5, "L_query": 10, "T_back": 60, "M_forward": 3}
single = etf_core.pattern_match_single(prices, T_idx=80, **params)
t_indices = np.array([70, 80, 90], dtype=np.int64)
batch, valid = etf_core.pattern_match_batch(prices, t_indices, **params)

print(f"DTW distance: {dtw:.4f}")
print(f"Cosine similarity: {cosine:.4f}")
print("Single-match features:", single)
print("Batch feature matrix:", batch)
print("Batch valid mask:", valid)

--- git diff --stat ---
--- git diff ---

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'git status --short -- examples/quickstart.py' in E:\workspace\projects\形态匹配ETF策略-pybind11
 succeeded in 121ms:
?? examples/quickstart.py

codex
Created [`examples/quickstart.py`](E:/workspace/projects/形态匹配ETF策略-pybind11/examples/quickstart.py).

- 24 lines, PEP 8 style
- UTF-8 without BOM
- Demonstrates DTW, cosine similarity, single matching, and batch matching
- Uses generated NumPy data only
- Script was **not executed**, as requested
tokens used
75,961
Created [`examples/quickstart.py`](E:/workspace/projects/形态匹配ETF策略-pybind11/examples/quickstart.py).

- 24 lines, PEP 8 style
- UTF-8 without BOM
- Demonstrates DTW, cosine similarity, single matching, and batch matching
- Uses generated NumPy data only
- Script was **not executed**, as requested
