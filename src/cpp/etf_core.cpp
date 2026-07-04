/**
 * etf_core.cpp — 形态匹配ETF策略 C++ 加速模块 (pybind11)
 * =============================================================
 *
 * > 模型 provenance:
 * >   DeepSeek-V4-Pro (via Claude Code CLI), 2026-07-03:
 * >     standardize_returns, cosine_similarity, dtw_distance,
 * >     compute_adx, compute_atr, pattern_match_single, 模块骨架, PYBIND11_MODULE
 * >   Kimi-K2.7-Code (via Kimi Code CLI), 2026-07-03:
 * >     pattern_match_batch, cosine_similarity_vec, dtw_distance_vec,
 * >     compute_pattern_features_cpp, 预计算缓存架构, v3 修订
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
        return std::vector<double>(std::max(py::ssize_t(0), n - 1), 0.0);
    }

    // 计算对数收益率
    std::vector<double> rets;
    rets.reserve(n - 1);
    for (py::ssize_t i = 1; i < n; ++i) {
        double p_prev = std::max(prices[i - 1], 1e-12);
        double p_curr = std::max(prices[i], 1e-12);
        double r = std::log(p_curr / p_prev);
        if (!std::isnan(r)) {
            rets.push_back(r);
        }
    }

    if (rets.empty()) {
        return std::vector<double>(std::max(py::ssize_t(0), n - 1), 0.0);
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

    auto result_vec = standardize_returns_cpp(buf.data(0), n);
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

    double dot = 0.0, norm_x2 = 0.0, norm_y2 = 0.0;
    for (py::ssize_t i = 0; i < n; ++i) {
        dot += x(i) * y(i);
        norm_x2 += x(i) * x(i);
        norm_y2 += y(i) * y(i);
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

double dtw_distance(ArrD x_arr, ArrD y_arr, int window = 5) {
    auto x = x_arr.unchecked<1>();
    auto y = y_arr.unchecked<1>();
    py::ssize_t n = x.shape(0);
    py::ssize_t m = y.shape(0);

    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    int band = std::max(window, static_cast<int>(std::abs(n - m)));

    // DTW 矩阵和计算在 GIL 释放区执行
    double result;
    {
        py::gil_scoped_release release;

        std::vector<double> dtw_data((n + 1) * (m + 1), std::numeric_limits<double>::infinity());
        auto dtw = [&](py::ssize_t i, py::ssize_t j) -> double& {
            return dtw_data[i * (m + 1) + j];
        };

        dtw(0, 0) = 0.0;

        for (py::ssize_t i = 1; i <= n; ++i) {
            py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
            py::ssize_t j_end = std::min(m + 1, i + band + 1);
            for (py::ssize_t j = j_start; j < j_end; ++j) {
                double cost = (x(i - 1) - y(j - 1));
                cost *= cost;
                double prev = std::min({dtw(i - 1, j), dtw(i, j - 1), dtw(i - 1, j - 1)});
                dtw(i, j) = cost + prev;
            }
        }

        double path_len = static_cast<double>(n + m);
        result = (path_len > 0) ? std::sqrt(dtw(n, m)) / path_len
                                : std::numeric_limits<double>::infinity();
    } // GIL 在此重获

    return result;
}

// ═══════════════════════════════════════════════════════════════
// 第四部分: ADX 计算 (V3.3.py 行 757-795)
// ═══════════════════════════════════════════════════════════════

double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n = 14) {
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
            smoothed[n - 1] = init_sum / n;
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

    ArrD result(len);
    auto res = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < n; ++i) res(i) = std::numeric_limits<double>::quiet_NaN();

    py::ssize_t tr_len = len - 1;
    std::vector<double> tr(tr_len);

    for (py::ssize_t i = 0; i < tr_len; ++i) {
        double hl = high(i + 1) - low(i + 1);
        double hc = std::abs(high(i + 1) - close(i));
        double lc = std::abs(low(i + 1) - close(i));
        tr[i] = std::max({hl, hc, lc});
    }

    double init_sum = 0.0;
    for (int i = 0; i < n; ++i) init_sum += tr[i];
    res(n) = init_sum / n;

    for (py::ssize_t i = n + 1; i < len; ++i) {
        res(i) = (res(i - 1) * (n - 1) + tr[i - 1]) / n;
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

// 向量版 DTW 距离（用于批量内部精排）
double dtw_distance_vec(const std::vector<double>& x, const std::vector<double>& y, int window = 5) {
    py::ssize_t n = static_cast<py::ssize_t>(x.size());
    py::ssize_t m = static_cast<py::ssize_t>(y.size());

    if (n == 0 || m == 0) return std::numeric_limits<double>::infinity();

    int band = std::max(window, static_cast<int>(std::abs(n - m)));

    std::vector<double> dtw_data((n + 1) * (m + 1), std::numeric_limits<double>::infinity());
    auto dtw = [&](py::ssize_t i, py::ssize_t j) -> double& {
        return dtw_data[i * (m + 1) + j];
    };

    dtw(0, 0) = 0.0;

    for (py::ssize_t i = 1; i <= n; ++i) {
        py::ssize_t j_start = std::max(py::ssize_t(1), i - band);
        py::ssize_t j_end = std::min(m + 1, i + band + 1);
        for (py::ssize_t j = j_start; j < j_end; ++j) {
            double cost = x[i - 1] - y[j - 1];
            cost *= cost;
            double prev = std::min({dtw(i - 1, j), dtw(i, j - 1), dtw(i - 1, j - 1)});
            dtw(i, j) = cost + prev;
        }
    }

    double path_len = static_cast<double>(n + m);
    return (path_len > 0) ? std::sqrt(dtw(n, m)) / path_len
                          : std::numeric_limits<double>::infinity();
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

} // namespace
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
    if (T_idx < L_query + M_forward + 10) return py::none();
    if (T_idx - L_query + 1 < 0) return py::none();

    // 查询窗口
    auto query_prices_vec = extract_window(prices, T_idx - L_query + 1, T_idx);
    if (static_cast<py::ssize_t>(query_prices_vec.size()) < L_query) return py::none();

    auto query_rets = standardize_returns_cpp(query_prices_vec.data(), L_query);
    if (query_rets.size() < 2) return py::none();

    py::ssize_t search_end = T_idx - L_query;
    if (search_end < L_query) return py::none();
    py::ssize_t search_start = std::max(py::ssize_t(L_query - 1),
                                        py::ssize_t(T_idx - T_back));

    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }

    std::optional<PatternResult> result_opt;

    // ── GIL 释放区：查询窗口标准化、余弦预筛选、DTW 精排、特征提取 ──
    {
        py::gil_scoped_release release;

        result_opt = [&]() -> std::optional<PatternResult> {
            // ═══════════════════════════════════════════════════════
            // 第1遍：余弦相似度 + 快速形状距离（全量候选）
            // ═══════════════════════════════════════════════════════
            std::vector<MatchCandidate> cos_candidates;
            std::vector<double> fast_shape_dists;
            py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());

            for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
                py::ssize_t hist_start = hist_end - L_query + 1;
                if (hist_start < 0) continue;

                auto hist_prices_vec = extract_window(prices, hist_start, hist_end);
                if (static_cast<py::ssize_t>(hist_prices_vec.size()) < L_query) continue;

                auto hist_rets = standardize_returns_cpp(hist_prices_vec.data(), L_query);
                if (hist_rets.size() < 2) continue;

                // 余弦相似度 (用 hist_rets 和 query_rets)
                double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
                py::ssize_t rlen = static_cast<py::ssize_t>(hist_rets.size());
                py::ssize_t qlen = n_query;
                py::ssize_t min_len = std::min(rlen, qlen);
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
                    cos_candidates.push_back({hist_end, hist_start, cos_s, std::move(hist_rets)});
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
                      [](const MatchCandidate& a, const MatchCandidate& b) {
                          return a.cos_s > b.cos_s;
                      });

            double global_min_cos = cos_candidates.back().cos_s;
            double global_max_cos = cos_candidates.front().cos_s;

            int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
            cos_candidates.resize(n_cos);

            // ═══════════════════════════════════════════════════════
            // 第2遍：DTW 精排 (仅 top-N)
            // ═══════════════════════════════════════════════════════
            std::vector<double> dtw_dists, cos_sims, future_rets;
            std::vector<py::ssize_t> match_ends;
            dtw_dists.reserve(n_cos);
            cos_sims.reserve(n_cos);
            future_rets.reserve(n_cos);
            match_ends.reserve(n_cos);

            for (const auto& cand : cos_candidates) {
                // DTW
                py::ssize_t hn = static_cast<py::ssize_t>(cand.hist_rets.size());
                int band = std::max(dtw_window, static_cast<int>(std::abs(hn - n_query)));

                // 局部 DTW 矩阵
                std::vector<double> dtw_data((hn + 1) * (n_query + 1),
                                             std::numeric_limits<double>::infinity());
                auto dtw_at = [&](py::ssize_t i, py::ssize_t j) -> double& {
                    return dtw_data[i * (n_query + 1) + j];
                };
                dtw_at(0, 0) = 0.0;

                for (py::ssize_t i = 1; i <= hn; ++i) {
                    py::ssize_t js = std::max(py::ssize_t(1), i - band);
                    py::ssize_t je = std::min(n_query + 1, i + band + 1);
                    for (py::ssize_t j = js; j < je; ++j) {
                        double cost = cand.hist_rets[i - 1] - query_rets[j - 1];
                        cost *= cost;
                        double prev = std::min({dtw_at(i - 1, j), dtw_at(i, j - 1), dtw_at(i - 1, j - 1)});
                        dtw_at(i, j) = cost + prev;
                    }
                }

                double path_len = static_cast<double>(hn + n_query);
                double dtw_d = (path_len > 0) ? std::sqrt(dtw_at(hn, n_query)) / path_len
                                              : std::numeric_limits<double>::infinity();

                dtw_dists.push_back(dtw_d);
                cos_sims.push_back(cand.cos_s);

                // 未来收益
                py::ssize_t fut_end = cand.hist_end + M_forward;
                if (fut_end < n_prices && fut_end < T_idx) {
                    future_rets.push_back(prices[fut_end] / prices[cand.hist_end] - 1.0);
                } else {
                    future_rets.push_back(std::numeric_limits<double>::quiet_NaN());
                }
                match_ends.push_back(cand.hist_end);
            }

            if (dtw_dists.size() < 3) return std::nullopt;

            // sigma (V3.0-FIX-2: 使用 sigma_fast)
            double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;

            // sim_dtw = exp(-dtw/sigma)
            std::vector<double> sim_dtw(dtw_dists.size());
            double min_dtw = std::numeric_limits<double>::max();
            double max_dtw = std::numeric_limits<double>::lowest();
            for (size_t i = 0; i < dtw_dists.size(); ++i) {
                sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
                min_dtw = std::min(min_dtw, sim_dtw[i]);
                max_dtw = std::max(max_dtw, sim_dtw[i]);
            }

            // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
            double range_dtw = (max_dtw - min_dtw > 1e-12) ? (max_dtw - min_dtw) : 1.0;
            double range_cos = (global_max_cos - global_min_cos > 1e-12)
                               ? (global_max_cos - global_min_cos) : 1.0;

            struct Scored {
                double score, fut_ret;
                py::ssize_t end_idx;
            };
            std::vector<Scored> scored;
            scored.reserve(sim_dtw.size());
            for (size_t i = 0; i < sim_dtw.size(); ++i) {
                double nd = (sim_dtw[i] - min_dtw) / range_dtw;
                double nc = (cos_sims[i] - global_min_cos) / range_cos;
                scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
            }

            std::sort(scored.begin(), scored.end(),
                      [](const Scored& a, const Scored& b) { return a.score > b.score; });

            int top_k = std::min(k, static_cast<int>(scored.size()));

            // 过滤 NaN 未来收益（V3.3 原逻辑: 过滤后至少2个有效）
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

            // ── 提取 15 维特征 ──
            return compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);
        }();
    } // GIL 在此重获

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

    if (match_step <= 0) {
        throw std::invalid_argument("match_step must be > 0");
    }

    std::vector<double> features_flat;
    features_flat.reserve(n_samples * 15);
    std::vector<bool> valid_mask(n_samples, false);

    {
        // ── GIL 释放区：纯 C++ 批量计算 ──
        py::gil_scoped_release release;

        // ── 预计算所有合法窗口的标准化收益率 ──
        // 窗口结束索引 end ∈ [L_query - 1, n_prices - 1]
        std::vector<std::vector<double>> precomputed_rets(n_prices);
        for (py::ssize_t end = L_query - 1; end < n_prices; ++end) {
            py::ssize_t start = end - L_query + 1;
            if (start >= 0) {
                auto window_prices = extract_window(prices, start, end);
                precomputed_rets[end] = standardize_returns_cpp(window_prices.data(), L_query);
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

            py::ssize_t n_query = static_cast<py::ssize_t>(query_rets.size());

            // 第1遍：余弦相似度 + 快速形状距离（全量候选）
            std::vector<MatchCandidate> cos_candidates;
            std::vector<double> fast_shape_dists;

            for (py::ssize_t hist_end = search_start; hist_end <= search_end; hist_end += match_step) {
                py::ssize_t hist_start = hist_end - L_query + 1;
                if (hist_start < 0) continue;

                const auto& hist_rets = precomputed_rets[hist_end];
                if (hist_rets.size() < 2) continue;

                double dot = 0.0, nx2 = 0.0, ny2 = 0.0;
                py::ssize_t rlen = static_cast<py::ssize_t>(hist_rets.size());
                py::ssize_t min_len = std::min(rlen, n_query);
                for (py::ssize_t i = 0; i < min_len; ++i) {
                    dot += hist_rets[i] * query_rets[i];
                    nx2 += hist_rets[i] * hist_rets[i];
                    ny2 += query_rets[i] * query_rets[i];
                }
                double nx = std::sqrt(nx2), ny = std::sqrt(ny2);
                double cos_s = (nx > 1e-12 && ny > 1e-12) ? dot / (nx * ny) : 0.0;

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

            if (cos_candidates.size() < 3) continue;

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
                      [](const MatchCandidate& a, const MatchCandidate& b) {
                          return a.cos_s > b.cos_s;
                      });

            double global_min_cos = cos_candidates.back().cos_s;
            double global_max_cos = cos_candidates.front().cos_s;

            int n_cos = std::min(cos_prefilter_top, static_cast<int>(cos_candidates.size()));
            cos_candidates.resize(n_cos);

            // 第2遍：DTW 精排 (仅 top-N)
            std::vector<double> dtw_dists, cos_sims, future_rets;
            std::vector<py::ssize_t> match_ends;
            dtw_dists.reserve(n_cos);
            cos_sims.reserve(n_cos);
            future_rets.reserve(n_cos);
            match_ends.reserve(n_cos);

            for (const auto& cand : cos_candidates) {
                double dtw_d = dtw_distance_vec(cand.hist_rets, query_rets, dtw_window);

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

            if (dtw_dists.size() < 3) continue;

            // sigma (V3.0-FIX-2: 使用 sigma_fast)
            double sigma = (sigma_fast > 1e-12) ? sigma_fast : 1.0;

            // sim_dtw = exp(-dtw/sigma)
            std::vector<double> sim_dtw(dtw_dists.size());
            double min_dtw = std::numeric_limits<double>::max();
            double max_dtw = std::numeric_limits<double>::lowest();
            for (size_t i = 0; i < dtw_dists.size(); ++i) {
                sim_dtw[i] = std::exp(-dtw_dists[i] / sigma);
                min_dtw = std::min(min_dtw, sim_dtw[i]);
                max_dtw = std::max(max_dtw, sim_dtw[i]);
            }

            // 综合得分: 0.5*norm_dtw + 0.5*norm_cos
            double range_dtw = (max_dtw - min_dtw > 1e-12) ? (max_dtw - min_dtw) : 1.0;
            double range_cos = (global_max_cos - global_min_cos > 1e-12)
                               ? (global_max_cos - global_min_cos) : 1.0;

            struct Scored {
                double score, fut_ret;
                py::ssize_t end_idx;
            };
            std::vector<Scored> scored;
            scored.reserve(sim_dtw.size());
            for (size_t i = 0; i < sim_dtw.size(); ++i) {
                double nd = (sim_dtw[i] - min_dtw) / range_dtw;
                double nc = (cos_sims[i] - global_min_cos) / range_cos;
                scored.push_back({0.5 * nd + 0.5 * nc, future_rets[i], match_ends[i]});
            }

            std::sort(scored.begin(), scored.end(),
                      [](const Scored& a, const Scored& b) { return a.score > b.score; });

            int top_k = std::min(k, static_cast<int>(scored.size()));

            // 过滤 NaN 未来收益（过滤后至少2个有效）
            std::vector<double> valid_scores, valid_frets;
            std::vector<py::ssize_t> valid_ends;
            for (int i = 0; i < top_k; ++i) {
                if (!std::isnan(scored[i].fut_ret)) {
                    valid_scores.push_back(scored[i].score);
                    valid_frets.push_back(scored[i].fut_ret);
                    valid_ends.push_back(scored[i].end_idx);
                }
            }
            if (valid_scores.size() < 2) continue;

            // 提取 15 维特征
            auto r = compute_pattern_features_cpp(valid_scores, valid_frets, valid_ends, T_back);

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
              "       compute_adx, compute_atr, pattern_match_single, pattern_match_batch\n"
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
