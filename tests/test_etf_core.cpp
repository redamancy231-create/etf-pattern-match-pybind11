/**
 * test_etf_core.cpp — etf_core 原生 C++ 算法测试
 *
 * 模型 provenance: GPT-5.6-Sol (via Codex CLI), 2026-07-17
 */

#define DOCTEST_CONFIG_IMPLEMENT
#include <doctest/doctest.h>

#include <pybind11/embed.h>
#include <pybind11/numpy.h>

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <stdexcept>
#include <vector>

namespace py = pybind11;

using ArrD = py::array_t<double, py::array::c_style | py::array::forcecast>;
using ArrI64 = py::array_t<int64_t, py::array::c_style | py::array::forcecast>;

// etf_core.cpp 当前没有公共 C++ 头文件，因此在此声明原生入口。
// 测试直接调用这些符号，不导入 Python 扩展模块，也不测试绑定分发层。
ArrD standardize_returns(ArrD price_series);
double cosine_similarity(ArrD x_arr, ArrD y_arr);
double dtw_distance(ArrD x_arr, ArrD y_arr, int window);
py::object dtw_distance_batch(ArrD query_arr, ArrD candidates_arr, int window, int top_k);
double compute_adx(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
ArrD compute_atr(ArrD high_arr, ArrD low_arr, ArrD close_arr, int n);
py::object pattern_match_single(
    ArrD prices_arr,
    int T_idx,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);
py::tuple pattern_match_batch(
    ArrD prices_arr,
    ArrI64 t_indices_arr,
    int k,
    int L_query,
    int T_back,
    int match_step,
    int M_forward,
    int dtw_window,
    int cos_prefilter_top);

// 非有限值策略（由 etf_core.cpp 的当前实现定义）：
// 1. standardize_returns 对价格窗口执行有限性检查；任一 NaN/Inf 都拒绝整个窗口并返回空数组。
// 2. cosine_similarity 与 DTW 不预先拒绝 NaN/Inf，而是按 IEEE-754 传播；Inf/Inf 等不定式产生 NaN。
// 3. compute_adx 与 compute_atr 不预先拒绝 NaN/Inf；ADX 中 Inf/Inf 可变为 NaN，ATR 保留 NaN/Inf。
// 4. pattern_match_single/batch 通过标准化步骤拒绝含 NaN/Inf 的查询窗口；single 返回 None，batch 标记无效。

namespace {

constexpr int kPatternTIdx = 30;
constexpr int kPatternK = 50;
constexpr int kPatternQueryLength = 3;
constexpr int kPatternLookback = 100;
constexpr int kPatternStep = 1;
constexpr int kPatternForward = 1;
constexpr int kPatternDtwWindow = 1;
constexpr int kPatternPrefilterTop = 50;

constexpr std::array<const char*, 15> kFeatureKeys = {
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
    "n_matches_above_thresh",
};

constexpr std::array<double, 15> kPeriodicExpectedFeatures = {
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    24.0,
    0.24,
    1.0,
    0.0,
};

ArrD make_array(const std::vector<double>& values) {
    ArrD result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_array(std::initializer_list<double> values) {
    return make_array(std::vector<double>(values));
}

ArrI64 make_index_array(const std::vector<int64_t>& values) {
    ArrI64 result(static_cast<py::ssize_t>(values.size()));
    auto out = result.mutable_unchecked<1>();
    for (py::ssize_t i = 0; i < out.shape(0); ++i) {
        out(i) = values[static_cast<std::size_t>(i)];
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    const std::vector<double>& values) {
    if (values.size() != static_cast<std::size_t>(rows * cols)) {
        throw std::invalid_argument("matrix data size does not match shape");
    }

    ArrD result(std::vector<py::ssize_t>{rows, cols});
    auto out = result.mutable_unchecked<2>();
    for (py::ssize_t row = 0; row < rows; ++row) {
        for (py::ssize_t col = 0; col < cols; ++col) {
            out(row, col) = values[static_cast<std::size_t>(row * cols + col)];
        }
    }
    return result;
}

ArrD make_matrix(
    py::ssize_t rows,
    py::ssize_t cols,
    std::initializer_list<double> values) {
    return make_matrix(rows, cols, std::vector<double>(values));
}

std::vector<double> make_periodic_prices(double scale) {
    std::vector<double> prices(41);
    prices[0] = scale;
    for (std::size_t i = 1; i < prices.size(); ++i) {
        const double factor = ((i - 1) % 2 == 0) ? 2.0 : 4.0;
        prices[i] = prices[i - 1] * factor;
    }
    return prices;
}

struct OhlcVectors {
    std::vector<double> high;
    std::vector<double> low;
    std::vector<double> close;
};

OhlcVectors make_trending_ohlc(double scale) {
    OhlcVectors data;
    data.high.resize(18);
    data.low.resize(18);
    data.close.resize(18);

    for (std::size_t i = 0; i < data.close.size(); ++i) {
        data.close[i] = (static_cast<double>(i) + 2.0) * scale;
        data.high[i] = data.close[i] + 0.5 * scale;
        data.low[i] = data.close[i] - 0.5 * scale;
    }
    return data;
}

OhlcVectors make_known_atr_input(double scale = 1.0) {
    return {
        {10.0 * scale, 12.0 * scale, 13.0 * scale, 15.0 * scale},
        {8.0 * scale, 9.0 * scale, 11.0 * scale, 12.0 * scale},
        {9.0 * scale, 11.0 * scale, 12.0 * scale, 14.0 * scale},
    };
}

py::object run_pattern_single(const std::vector<double>& prices, int t_idx = kPatternTIdx) {
    return pattern_match_single(
        make_array(prices),
        t_idx,
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

py::tuple run_pattern_batch(
    const std::vector<double>& prices,
    const std::vector<int64_t>& t_indices) {
    return pattern_match_batch(
        make_array(prices),
        make_index_array(t_indices),
        kPatternK,
        kPatternQueryLength,
        kPatternLookback,
        kPatternStep,
        kPatternForward,
        kPatternDtwWindow,
        kPatternPrefilterTop);
}

std::array<double, 15> values_from_dict(const py::dict& result) {
    std::array<double, 15> values{};
    for (std::size_t i = 0; i < kFeatureKeys.size(); ++i) {
        values[i] = py::cast<double>(result[py::str(kFeatureKeys[i])]);
    }
    return values;
}

std::array<double, 15> values_from_batch_row(const ArrD& features, py::ssize_t row) {
    const auto data = features.unchecked<2>();
    std::array<double, 15> values{};
    for (py::ssize_t col = 0; col < 15; ++col) {
        values[static_cast<std::size_t>(col)] = data(row, col);
    }
    return values;
}

void check_periodic_expected_features(const std::array<double, 15>& actual) {
    for (std::size_t i = 0; i < actual.size(); ++i) {
        CAPTURE(i);
        CHECK(actual[i] == doctest::Approx(kPeriodicExpectedFeatures[i]).epsilon(1e-12));
    }
}

} // namespace

int main(int argc, char** argv) {
    py::scoped_interpreter interpreter{};
    doctest::Context context(argc, argv);
    return context.run();
}

TEST_CASE("standardize_returns covers edge cases and a hand-computed result") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = standardize_returns(make_array({}));
        CHECK(result.ndim() == 1);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("single price returns an empty array") {
        const ArrD result = standardize_returns(make_array({42.0}));
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("NaN and Inf reject the whole price window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(standardize_returns(make_array({1.0, nan, 2.0})).shape(0) == 0);
        CHECK(standardize_returns(make_array({1.0, inf, 2.0})).shape(0) == 0);
    }

    SUBCASE("very small prices are floored and become zero returns") {
        const double tiny = std::ldexp(1.0, -900);
        const ArrD result = standardize_returns(make_array({tiny, 2.0 * tiny, 8.0 * tiny}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.0));
    }

    SUBCASE("very large finite prices remain numerically stable") {
        const double huge = std::ldexp(1.0, 900);
        const ArrD result = standardize_returns(make_array({huge, 2.0 * huge, 8.0 * huge}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known answer for prices 1, 2, 8 is -1, 1") {
        const ArrD result = standardize_returns(make_array({1.0, 2.0, 8.0}));
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(-1.0).epsilon(1e-12));
        CHECK(out(1) == doctest::Approx(1.0).epsilon(1e-12));
    }
}

TEST_CASE("cosine_similarity covers edge cases and a hand-computed result") {
    SUBCASE("empty vectors return the neutral similarity zero") {
        CHECK(cosine_similarity(make_array({}), make_array({})) == doctest::Approx(0.0));
    }

    SUBCASE("single positive elements have similarity one") {
        CHECK(cosine_similarity(make_array({2.0}), make_array({3.0})) == doctest::Approx(1.0));
    }

    SUBCASE("NaN and Inf propagate to NaN") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(cosine_similarity(make_array({nan}), make_array({1.0}))));
        CHECK(std::isnan(cosine_similarity(make_array({inf}), make_array({1.0}))));
    }

    SUBCASE("very small norm returns zero and huge squaring overflow returns NaN") {
        CHECK(cosine_similarity(make_array({1e-300}), make_array({1.0})) == doctest::Approx(0.0));
        CHECK(std::isnan(cosine_similarity(make_array({1e308}), make_array({1e308}))));
    }

    SUBCASE("known answer is four fifths") {
        CHECK(cosine_similarity(make_array({1.0, 2.0}), make_array({2.0, 1.0}))
              == doctest::Approx(0.8).epsilon(1e-12));
    }

    SUBCASE("mismatched lengths are rejected") {
        CHECK_THROWS_AS(
            cosine_similarity(make_array({1.0}), make_array({1.0, 2.0})),
            std::invalid_argument);
    }
}

TEST_CASE("dtw_distance covers ties, window boundaries, and numeric policies") {
    SUBCASE("an empty sequence returns infinity") {
        CHECK(std::isinf(dtw_distance(make_array({}), make_array({1.0}), 1)));
        CHECK(std::isinf(dtw_distance(make_array({1.0}), make_array({}), 1)));
    }

    SUBCASE("single elements use sqrt squared cost divided by total length") {
        CHECK(dtw_distance(make_array({2.0}), make_array({5.0}), 0)
              == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN propagates and finite versus Inf returns Inf") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        CHECK(std::isnan(dtw_distance(make_array({nan}), make_array({0.0}), 0)));
        CHECK(std::isinf(dtw_distance(make_array({inf}), make_array({0.0}), 0)));
    }

    SUBCASE("very large and very small finite costs remain representable") {
        CHECK(dtw_distance(make_array({1e150}), make_array({-1e150}), 0)
              == doctest::Approx(1e150).epsilon(1e-12));
        CHECK(dtw_distance(make_array({1e-150}), make_array({-1e-150}), 0) / 1e-150
              == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known diagonal answer is one quarter") {
        CHECK(dtw_distance(make_array({0.0, 1.0}), make_array({0.0, 2.0}), 0)
              == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("equal predecessor ties stay deterministic in distance") {
        CHECK(dtw_distance(make_array({0.0, 0.0}), make_array({0.0, 0.0, 0.0}), 0)
              == doctest::Approx(0.0));
    }

    SUBCASE("window zero enforces the diagonal and window one permits warping") {
        const ArrD x = make_array({0.0, 1.0, 1.0});
        const ArrD y = make_array({0.0, 0.0, 1.0});
        CHECK(dtw_distance(x, y, 0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(dtw_distance(x, y, 1) == doctest::Approx(0.0));
    }
}

TEST_CASE("dtw_distance_batch matches scalar DTW and honors Top-K ties") {
    SUBCASE("empty candidates return empty arrays in both modes") {
        const py::object all_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 0);
        const ArrD all_distances = py::reinterpret_borrow<ArrD>(all_result);
        CHECK(all_distances.shape(0) == 0);

        const py::object top_result = dtw_distance_batch(
            make_array({}), make_matrix(0, 0, {}), 0, 1);
        REQUIRE(py::isinstance<py::tuple>(top_result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(top_result);
        const ArrI64 indices = top[0].cast<ArrI64>();
        const ArrD distances = top[1].cast<ArrD>();
        CHECK(indices.shape(0) == 0);
        CHECK(distances.shape(0) == 0);
    }

    SUBCASE("one query value and one candidate produce the scalar answer") {
        const py::object result = dtw_distance_batch(
            make_array({2.0}), make_matrix(1, 1, {5.0}), 0, 0);
        const ArrD distances = py::reinterpret_borrow<ArrD>(result);
        const auto out = distances.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(out(0) == doctest::Approx(1.5).epsilon(1e-12));
    }

    SUBCASE("NaN and Inf propagate per candidate row") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();
        const py::object result = dtw_distance_batch(
            make_array({0.0}), make_matrix(2, 1, {nan, inf}), 0, 0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(std::isnan(out(0)));
        CHECK(std::isinf(out(1)));
    }

    SUBCASE("very large and very small candidates match scalar policy") {
        const py::object large_result = dtw_distance_batch(
            make_array({1e150}), make_matrix(1, 1, {-1e150}), 0, 0);
        const auto large = py::reinterpret_borrow<ArrD>(large_result).unchecked<1>();
        CHECK(large(0) == doctest::Approx(1e150).epsilon(1e-12));

        const py::object small_result = dtw_distance_batch(
            make_array({1e-150}), make_matrix(1, 1, {-1e-150}), 0, 0);
        const auto small = py::reinterpret_borrow<ArrD>(small_result).unchecked<1>();
        CHECK(small(0) / 1e-150 == doctest::Approx(1.0).epsilon(1e-12));
    }

    SUBCASE("known candidate distances are zero and one quarter") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(2, 2, {0.0, 1.0, 0.0, 2.0}),
            0,
            0);
        const auto out = py::reinterpret_borrow<ArrD>(result).unchecked<1>();
        REQUIRE(out.shape(0) == 2);
        CHECK(out(0) == doctest::Approx(0.0));
        CHECK(out(1) == doctest::Approx(0.25).epsilon(1e-12));
    }

    SUBCASE("Top-K breaks equal-distance ties by candidate index") {
        const py::object result = dtw_distance_batch(
            make_array({0.0, 1.0}),
            make_matrix(3, 2, {0.0, 1.0, 0.0, 1.0, 1.0, 1.0}),
            0,
            2);
        REQUIRE(py::isinstance<py::tuple>(result));
        const py::tuple top = py::reinterpret_borrow<py::tuple>(result);
        const auto indices = top[0].cast<ArrI64>().unchecked<1>();
        const auto distances = top[1].cast<ArrD>().unchecked<1>();
        REQUIRE(indices.shape(0) == 2);
        CHECK(indices(0) == 0);
        CHECK(indices(1) == 1);
        CHECK(distances(0) == doctest::Approx(0.0));
        CHECK(distances(1) == doctest::Approx(0.0));
    }

    SUBCASE("batch mode observes the same boundary window behavior") {
        const ArrD query = make_array({0.0, 1.0, 1.0});
        const ArrD candidates = make_matrix(1, 3, {0.0, 0.0, 1.0});
        const py::object diagonal_result = dtw_distance_batch(query, candidates, 0, 0);
        const py::object warped_result = dtw_distance_batch(query, candidates, 1, 0);
        const auto diagonal = py::reinterpret_borrow<ArrD>(diagonal_result).unchecked<1>();
        const auto warped = py::reinterpret_borrow<ArrD>(warped_result).unchecked<1>();
        CHECK(diagonal(0) == doctest::Approx(1.0 / 6.0).epsilon(1e-12));
        CHECK(warped(0) == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_adx covers neutral, propagation, extremes, and known answers") {
    SUBCASE("empty input returns the neutral ADX value") {
        CHECK(compute_adx(make_array({}), make_array({}), make_array({}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("a single OHLC point also returns the neutral ADX value") {
        CHECK(compute_adx(make_array({10.0}), make_array({9.0}), make_array({9.5}), 14)
              == doctest::Approx(25.0));
    }

    SUBCASE("NaN and Inf propagate to NaN for a full calculation window") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_trending_ohlc(1.0);
        nan_data.high[1] = nan;
        CHECK(std::isnan(compute_adx(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)));

        OhlcVectors inf_data = make_trending_ohlc(1.0);
        inf_data.high[1] = inf;
        CHECK(std::isnan(compute_adx(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)));
    }

    SUBCASE("very large trend approaches one hundred without overflow") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, 900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result == doctest::Approx(100.0).epsilon(1e-12));
    }

    SUBCASE("very small trend is dominated by the fixed epsilon but remains finite") {
        const OhlcVectors data = make_trending_ohlc(std::ldexp(1.0, -900));
        const double result = compute_adx(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        CHECK(std::isfinite(result));
        CHECK(result >= 0.0);
        CHECK(result < 1e-200);
    }

    SUBCASE("flat prices have known ADX zero") {
        const std::vector<double> flat(18, 10.0);
        CHECK(compute_adx(make_array(flat), make_array(flat), make_array(flat), 2)
              == doctest::Approx(0.0));
    }
}

TEST_CASE("compute_atr covers short inputs, propagation, scaling, and a known series") {
    SUBCASE("empty input returns an empty array") {
        const ArrD result = compute_atr(make_array({}), make_array({}), make_array({}), 14);
        CHECK(result.shape(0) == 0);
    }

    SUBCASE("a single point returns one NaN because the warmup is incomplete") {
        const ArrD result = compute_atr(
            make_array({10.0}), make_array({9.0}), make_array({9.5}), 14);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 1);
        CHECK(std::isnan(out(0)));
    }

    SUBCASE("NaN propagates and Inf is preserved by Wilder smoothing") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        OhlcVectors nan_data = make_known_atr_input();
        nan_data.high[2] = nan;
        const auto nan_out = compute_atr(
            make_array(nan_data.high), make_array(nan_data.low), make_array(nan_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isnan(nan_out(2)));
        CHECK(std::isnan(nan_out(3)));

        OhlcVectors inf_data = make_known_atr_input();
        inf_data.high[2] = inf;
        const auto inf_out = compute_atr(
            make_array(inf_data.high), make_array(inf_data.low), make_array(inf_data.close), 2)
                                 .unchecked<1>();
        CHECK(std::isinf(inf_out(2)));
        CHECK(std::isinf(inf_out(3)));
    }

    SUBCASE("very large and very small finite inputs scale linearly") {
        for (const double scale : {std::ldexp(1.0, 900), std::ldexp(1.0, -900)}) {
            CAPTURE(scale);
            const OhlcVectors data = make_known_atr_input(scale);
            const auto out = compute_atr(
                make_array(data.high), make_array(data.low), make_array(data.close), 2)
                                 .unchecked<1>();
            CHECK(out(2) / scale == doctest::Approx(2.5).epsilon(1e-12));
            CHECK(out(3) / scale == doctest::Approx(2.75).epsilon(1e-12));
        }
    }

    SUBCASE("known ATR is NaN, NaN, 2.5, 2.75") {
        const OhlcVectors data = make_known_atr_input();
        const ArrD result = compute_atr(
            make_array(data.high), make_array(data.low), make_array(data.close), 2);
        const auto out = result.unchecked<1>();
        REQUIRE(out.shape(0) == 4);
        CHECK(std::isnan(out(0)));
        CHECK(std::isnan(out(1)));
        CHECK(out(2) == doctest::Approx(2.5).epsilon(1e-12));
        CHECK(out(3) == doctest::Approx(2.75).epsilon(1e-12));
    }
}

TEST_CASE("pattern_match_single covers invalid indices and deterministic features") {
    SUBCASE("empty prices reject T_idx as out of range without a native crash") {
        CHECK_THROWS_AS(run_pattern_single({}, 0), std::out_of_range);
    }

    SUBCASE("one price is valid input but has insufficient history and returns None") {
        const py::object result = run_pattern_single({1.0}, 0);
        CHECK(result.is_none());
    }

    SUBCASE("negative and one-past-end T_idx are rejected") {
        const std::vector<double> prices = {1.0, 2.0, 4.0};
        CHECK_THROWS_AS(run_pattern_single(prices, -1), std::out_of_range);
        CHECK_THROWS_AS(run_pattern_single(prices, 3), std::out_of_range);
    }

    SUBCASE("NaN and Inf in the query window are rejected as None") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        std::vector<double> nan_prices = make_periodic_prices(1.0);
        nan_prices[kPatternTIdx] = nan;
        CHECK(run_pattern_single(nan_prices).is_none());

        std::vector<double> inf_prices = make_periodic_prices(1.0);
        inf_prices[kPatternTIdx] = inf;
        CHECK(run_pattern_single(inf_prices).is_none());
    }

    SUBCASE("very large powers of two preserve the deterministic known features") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, 900)));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }

    SUBCASE("very small prices are floored, lose shape, and return None") {
        const py::object result = run_pattern_single(
            make_periodic_prices(std::ldexp(1.0, -900)));
        CHECK(result.is_none());
    }

    SUBCASE("periodic prices have a hand-derived 15-feature answer") {
        const py::object result = run_pattern_single(make_periodic_prices(1.0));
        REQUIRE_FALSE(result.is_none());
        REQUIRE(py::isinstance<py::dict>(result));
        check_periodic_expected_features(
            values_from_dict(py::reinterpret_borrow<py::dict>(result)));
    }
}

TEST_CASE("pattern_match_batch covers masks, extremes, and deterministic features") {
    SUBCASE("empty prices and indices return shapes zero by fifteen and zero") {
        const py::tuple result = run_pattern_batch({}, {});
        const ArrD features = result[0].cast<ArrD>();
        const py::array_t<bool> mask = result[1].cast<py::array_t<bool>>();
        CHECK(features.ndim() == 2);
        CHECK(features.shape(0) == 0);
        CHECK(features.shape(1) == 15);
        CHECK(mask.shape(0) == 0);
    }

    SUBCASE("one price yields no feature row and a false validity mask") {
        const py::tuple result = run_pattern_batch({1.0}, {0});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("NaN and Inf in the query window produce false masks") {
        const double nan = std::numeric_limits<double>::quiet_NaN();
        const double inf = std::numeric_limits<double>::infinity();

        for (const double bad_value : {nan, inf}) {
            std::vector<double> prices = make_periodic_prices(1.0);
            prices[kPatternTIdx] = bad_value;
            const py::tuple result = run_pattern_batch(prices, {kPatternTIdx});
            const ArrD features = result[0].cast<ArrD>();
            const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
            CHECK(features.shape(0) == 0);
            REQUIRE(mask.shape(0) == 1);
            CHECK_FALSE(mask(0));
        }
    }

    SUBCASE("very large powers of two preserve one known feature row") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, 900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }

    SUBCASE("very small prices produce no feature rows and a false mask") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(std::ldexp(1.0, -900)), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        CHECK(features.shape(0) == 0);
        REQUIRE(mask.shape(0) == 1);
        CHECK_FALSE(mask(0));
    }

    SUBCASE("periodic prices have the same hand-derived feature row as single mode") {
        const py::tuple result = run_pattern_batch(
            make_periodic_prices(1.0), {kPatternTIdx});
        const ArrD features = result[0].cast<ArrD>();
        const auto mask = result[1].cast<py::array_t<bool>>().unchecked<1>();
        REQUIRE(features.shape(0) == 1);
        REQUIRE(features.shape(1) == 15);
        REQUIRE(mask.shape(0) == 1);
        CHECK(mask(0));
        check_periodic_expected_features(values_from_batch_row(features, 0));
    }
}