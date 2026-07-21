# etf-pattern-match-pybind11 Fork 修改方向全景分析

> 生成日期: 2026-07-20 · 修訂: 2026-07-21
> 模型 provenance: DeepSeek-V4-Pro (via Claude Code CLI) · 審查: GPT-5.6-Sol (via Codex CLI)
> 基於: 項目 README/CLAUDE.md/src 全量源碼 + project_status.md
> 審查報告: `_review/conclusions/GPT-5.6-Sol_fork-directions-review_2026-07-21.md`
>
> 📖 **其他語言版本**: [简体中文](../docs/fork-modification-directions.md) | [English](../en/fork-modification-directions.md)

## 項目現狀速覽

- **核心**: 從 3836 行 ETF 形態匹配策略 V3.3 提取純計算模塊，pybind11 + C++20 加速
- **加速**: DTW 單次 34× (96µs→2.8µs) / 形態匹配單次 53× (14.0ms→0.26ms) / 批量接口開銷縮減 2.2× (100 次 C++ 單次調用 → 1 次 C++ 批量調用)；Python batch vs C++ batch 端到端約 93×（見 benchmark JSON）
- **算法**: 餘弦預篩選 → DTW 精排 → 綜合得分(0.5×norm_dtw + 0.5×norm_cos) → 15 維特徵
- **模塊**: 6 個 Python 純計算模塊 + 1 個 C++ 統一加速模塊(8 函數，~1100 行)
- **測試**: 54 單元測試 + 2 驗證腳本 + 交互 Notebook
- **工具鏈**: MSVC 19.51 + pybind11 3.0.4 + C++20 + CMake 3.20+
- **許可證**: MIT（僅覆蓋本倉庫發佈的代碼；外部 SDK、數據源、第三方模型須單獨核查許可）
- **明確排除**: 實盤交易代碼、掘金 SDK 綁定、回測結果/績效聲明（本倉庫不提供這些結論；fork 可新增相關功能，但須獨立標註數據來源、樣本區間、交易成本假設和驗證方法）

---

## 前置知識假設

本文檔假設 fork 貢獻者：
- 熟悉 Python/NumPy 和 C++ 基礎
- 了解 pybind11 的基本概念（GIL 管理、`py::array_t`、`py::object`）
- 能閱讀 CMake 構建配置
- 對量化金融中"前視偏差""時序交叉驗證""交易成本"有基本認知

對於標註"需要外部資料"或"需要平臺訪問"的方向，文檔會顯式列出阻塞項。**開工前請先閱讀各方向的前置條件——標註爲"低"或"中"改動量的方向也可能有未解決的前置依賴。**

---

## 一、算法內核方向

### 1.1 DTW 變體替換

當前使用標準 DTW + Sakoe-Chiba band(window=5)。`dtw_distance_span()` 是純函數，接口清晰——替換距離度量是最低門檻的 fork。

| 變體 | 適用場景 | 實現複雜度 | 關鍵風險 |
|------|---------|-----------|---------|
| **Derivative DTW (DDTW)** | 匹配形態"形狀"而非絕對水平，先對序列差分再 DTW | 低(預處理即可) | 差分放大噪聲；需驗證短序列(L≈19)上的數值穩定性 |
| **Weighted DTW** | 對近期數據點加權，匹配"近期更重要"的市場直覺 | 低(DP 遞推式加權重因子) | 權重衰減率是額外超參；窗口邊界處權重不連續 |
| **Soft-DTW** | 數值可微（數學上）；但**當前 pybind11 函數返回 NumPy/float，不攜帶自動微分圖**——若要用於訓練，需額外實現 PyTorch custom autograd、JAX custom VJP 或採用現有可微 DTW 庫 | 中(需改 DP 遞推式爲 softmin + 微分框架適配) | 可微性 ≠ 訓練就緒；需梯度數值驗證；γ 參數敏感 |
| **ShapeDTW** | 先提取局部形狀描述符(subsequence→descriptor)再 DTW | 中(需新增描述符提取模塊) | 描述符選擇無通用標準；L_query=20 下子序列極短 |
| **FastDTW** | 近似線性時間 O(L)；**適用於 L_query 本身較長(數百點以上)的場景**；若僅增加 T_back(候選數量增多)，應優先評估候選索引和剪枝，而非替換 DTW 算法 | 中(粗化→投影→細化三層遞歸) | 近似誤差 vs Top-K 穩定性需單獨 benchmark；當前 L_query=20 時 FastDTW 優勢有限 |

**入口點**: C++ `src/cpp/etf_core.cpp` `dtw_distance_span()`(行 ~150-180)；Python 參考 `src/core/dtw.py`。改動算法後須同步 Python 參考實現並通過 `verify_etf_core.py` 一致性驗證。

**驗收標準**: (a) `verify_etf_core.py` 全 PASS；(b) 新增 DTW 變體的獨立單元測試；(c) benchmark 比較變體與標準 DTW 的速度和 Top-K 召回率。

### 1.2 綜合得分公式重設計

當前: `combined_score = 0.5 × norm_dtw + 0.5 × norm_cos`，等權 min-max 歸一化後合併。

可替換爲:
- **自適應權重**: 根據 cos 候選分佈(如基尼係數)動態調整 DTW/Cos 權重
- **秩聚合**: 用 Spearman footrule 距離或 Borda count 替代加權平均
- **帕累託前沿**: 不合並，保留 DTW 和 Cos 兩個維度，在二維空間中選取非支配解
- **概率校準**: 用歷史匹配的**歷史後續收益統計**校準相似度得分（注意：此爲統計特徵而非預測概率——詳見 §關鍵約束與注意點 術語說明）

**入口點**: C++ `src/cpp/etf_core.cpp:551–707`（`pattern_match_core()`，其中 `Scored` 結構體和綜合得分位於 680–690 行）；Python 參考 `src/core/pattern_match.py:192–200`。

### 1.3 多變量形態匹配

當前僅基於標準化收益率序列(1 維)做匹配。擴展爲多維:
- 同時匹配: 價格趨勢 + 成交量模式 + 波動率形態 + ADX 方向
- DTW 從一維擴展到多維: `cost = Σⱼ wⱼ × (x[i][j] - y[i][j])²`
- 距離聚合策略: 加權和 / Pareto 前沿 / 馬氏距離歸一化各維度後再 DTW

**入口點**: `dtw_distance_span()` 當前只接受 `const double*`，改爲多維需同時修改函數簽名和 DP 遞推式。需新增 C++ 多維數組輸入接口和 Python 端數據組裝邏輯。

### 1.4 候選檢索加速

當前餘弦預篩選是全量掃描(`for hist_end in range(search_start, search_end+1, match_step)`)。可用:
- **k-NN 索引**: FLANN / HNSW / FAISS 對歷史窗口收益率向量建索引——有可證明的召回率保證
- **近似索引(LSH)**: 明確標註召回率與速度的 trade-off，附帶 Top-K 召回率測試
- **分塊點積上界剪枝**: 預先計算範數，使用部分累積點積上界安全剪枝——**不同於簡單的"找到滿意結果就停止"**（後者會改變 Top-K 結果，屬於近似搜索而非安全剪枝）

每種檢索方式均應測試: Top-K 召回率、綜合得分變化、15 維特徵穩定性、端到端速度。

**入口點**: `pattern_match_core()` 中"第 1 遍: 餘弦相似度"的 for 循環

---

## 二、加速平臺方向

### 2.1 GPU 加速(CUDA/ROCm)

DTW 的批量計算天然適合 GPU: `dtw_distance_batch` 將一個 query 對 N 個 candidate 做一對多循環，可映射到 CUDA kernel。

- **CUDA C++**: 替換 `pattern_match_core` 的 CPU 循環爲手寫 kernel
- **cuBLAS**: 餘弦相似度計算可轉爲矩陣乘法(candidates × query = batched dot product)
- **性能預期**: 批量場景下端到端加速比**待驗證**——需在明確 n_samples、候選數、序列長度的條件下分別測量 host→device 傳輸、餘弦、DTW、排序、特徵聚合各階段耗時，以當前 Python 版本爲數值和結果基線
- **挑戰**: `pattern_match_core` 中的控制流(`if cos_s > 0`, `if fut_end < T_idx`)在 GPU 上需要 warp-level 分支處理；host-device 數據傳輸和 Python API 邊界可能成爲主導開銷

**入口點**: `dtw_distance_batch()` 和 `pattern_match_core()` 中的循環段。

**驗收標準**: (a) 與當前 Python/C++ 參考實現數值一致(浮點容差 1e-6)；(b) 分階段 benchmark 報告；(c) CPU fallback 路徑；(d) Top-K 和 15 維特徵一致性測試。

### 2.2 SIMD 向量化

當前 C++ 代碼無顯式 SIMD。SIMD 友好熱點:
- `cosine_similarity_vec()` 的點積循環 → `_mm512_fmadd_pd`
- `dtw_distance_span()` 內層循環 → 可向量化但受限於 DP 的數據依賴
- `standardize_returns_cpp()` 的 `std::accumulate` → SIMD reduce
- 需調整數據結構爲 **SoA**(Structure of Arrays)以獲得連續內存訪問

**關鍵——CPU 能力分發**: 直接以 `/arch:AVX512` 編譯會導致無 AVX512 的 CPU 無法運行。應實現:
- CPUID 運行時檢測
- AVX512 / AVX2 / 標量多級 fallback
- 不同 CPU 的分別 benchmark
- SIMD 與標量結果誤差測試（FMA 和 reduction 順序可能導致浮點差異，需驗證是否在 1e-8/1e-6 容差內）

**編譯選項**: MSVC `/arch:AVX512`（僅 AVX512 路徑）/ GCC `-mavx512f` / 手寫 intrinsics with runtime dispatch。

### 2.3 多線程批量處理

當前 `pattern_match_batch` 對多個 T_idx 的循環是串行的(GIL 已釋放但無多線程)。

**推薦安全模式**（避免數據競爭和結果順序錯亂）:
1. 工作線程只寫 C++ 數據，不創建 Python 對象
2. 爲每個 sample 預分配固定位置（如 `features[n_samples][15]`）
3. 每個線程只寫自己的 sample 槽位
4. `valid_mask` 與特徵矩陣按輸入 `t_indices` 順序保持一致
5. 主線程重新獲取 GIL 後**統一**創建 NumPy 返回對象
6. 增加併發正確性、輸出順序穩定性和異常安全測試

**不推薦模式**: 在工作線程中 `gil_scoped_acquire` + 直接創建 Python 對象——會引入生命週期、線程安全、異常傳播和 Python allocator 競爭問題。

**入口點**: `pattern_match_batch()` 中 `for (py::ssize_t s = 0; s < n_samples; ++s)` 循環。

### 2.4 pandas → Arrow 零拷貝

當前 `py::array_t<double>` 對 **float64、C-contiguous** 的 NumPy 數組可避免額外複製。但以下情況可能觸發拷貝:
- dtype 不匹配時 `forcecast` 轉換
- 非連續數組（Fortran-contiguous、slice/strided view）
- pandas DataFrame → NumPy 的隱式轉換（取決於底層數據佈局和 dtype）

Arrow 集成需新增適配層，不是僅替換調用入口。建議: 先 benchmark 驗證當前方案中數據搬運佔總耗時的比例，再決定是否值得引入 Arrow 依賴。

---

## 三、策略系統方向

### 3.1 接回回測框架

**前置條件**: 當前項目是"純計算模塊，不含平臺綁定"。**開工前需明確以下阻塞項**:
- 原始 V3.3.py 完整文件**不在本倉庫內**
- 原始訓練數據、模型文件、標籤定義**不在本倉庫內**
- 原始回測配置（時間範圍、交易成本、滑點、停牌規則）**不在本倉庫內**

Fork 可在滿足前置條件後接入:

| 框架 | 方式 | 難度 | 關鍵挑戰 |
|------|------|------|---------|
| **backtrader** | 將 `pattern_match_single` 封裝爲 `bt.Indicator` 子類 | **中¹** | T_idx 與框架 bar 索引映射、warm-up 階段、周頻調倉 vs 日頻 bar、嚴格因果性驗證 |
| **vnpy** | 實現 `CtaTemplate`，在 `on_bar()` 中調用 C++ 模塊 | 中 | 需平臺 API 文檔和測試環境 |
| **zipline-reloaded** | 實現 `CustomFactor`，pipeline API 風格 | 中 | pipeline 語義與 15 維特徵的適配 |
| **bt**(Python) | `Algo` 子類，固定週期調用 `pattern_match_batch` | **中¹** | 同上 backtrader 挑戰 |
| **掘金平臺** | 逆向補回平臺綁定層，恢復原始 V3.3 的完整可運行策略 | **高**(需外部資料) | 原始文件不在倉庫內；需掘金 SDK 和平臺賬號 |

> ¹ 原稿標爲"低"，審查指出需處理 GIL + C++ 對象生命週期 + 多 ETF 數據組織 + 無前視測試，實際爲中。

核心價值: 讓 "C++ 加速的計算核心" 從獨立 demo 變成可回測、可評估的策略。**輸出應標註"具備接入回測框架的能力"，而非"可投產"。** 完整投產需補齊執行層、交易成本建模和樣本外驗證。

### 3.2 多 ETF 截面輪動

原始 V3.3 是"多頭輪動策略"——在 ETF 池中根據形態信號選最優。當前項目只提供單 ETF 的特徵提取。Fork 需分兩階段:

**階段一（可並行）**: 每個 ETF 獨立生成 15 維特徵。當前 `pattern_match_batch()` 只接受單個 ETF 的一維 `prices` 和一組 `t_indices`——需新增多 ETF 批量輸入接口（不同 ETF 可能有不同序列長度和缺失值策略）。

**階段二（不可簡單並行）**: 收集所有 ETF 特徵後，做截面 rank/z-score 標準化、排序和持倉決策。此階段依賴全部 ETF 的結果，不是各 ETF 間獨立任務。

- **截面可比性**: 不同 ETF 的 15 維特徵在截面上 rank / z-score 標準化
- **排序層**: LambdaRank / XGBoost ranker 學習 F1-F15 到持倉權重的映射
- **輪動週期**: 周頻再平衡(與原始策略一致)
- **交易成本建模**: 衝擊成本 + 佣金 + 印花稅

### 3.3 風控執行層

當前項目中的風控相關代碼分佈在多個模塊——**不是單一風控系統**:

| 功能 | 實際位置 | 當前狀態 |
|------|---------|---------|
| 滾動波動率風控(分位數減倉) | `src/core/risk_controls.py` | ✅ 已實現 |
| MA 趨勢過濾 | `src/core/risk_controls.py` | ✅ 已實現 |
| 倉位上限約束 | `src/core/risk_controls.py` | ✅ 已實現 |
| ATR | `src/core/technical.py` / C++ 模塊 | ✅ 已實現 |
| 最大回撤 | `src/core/metrics.py` | ✅ 已實現 |
| VaR | — | ❌ 未實現 |
| 止損/止盈觸發 | — | ❌ 未實現 |
| 倉位再平衡調度器 | — | ❌ 未實現 |
| 最大回撤熔斷(賬戶+ETF雙層) | — | ❌ 未實現 |

Fork 可添加的**執行層**（區別於現有的**計算層**）:
- 止損/止盈觸發: trailing stop / time stop / volatility stop
- 倉位再平衡調度器: 偏離目標權重超過閾值 → 觸發調倉
- 黑名單: 連續 N 次形態匹配失敗 → 該 ETF 暫停交易
- 最大回撤熔斷: 賬戶級別和 ETF 級別雙層限制

### 3.4 信號服務器(微服務化)

建議拆爲兩層——當前 `etf_core` 輸出的是 15 維特徵，不是交易信號:

**計算服務**（與當前模塊直接對應）:
- HTTP/gRPC 接收價格數據 → 返回 15 維特徵 + 版本信息
- Redis 緩存預計算窗口和中間結果
- 定義 API schema、參數版本、數據時間戳、緩存失效策略

**策略服務**（需額外實現）:
- 輸入多個 ETF 的特徵 → 執行排序、風控和調倉規則 → 輸出信號及解釋
- 信號閾值、持倉規則、調倉週期、交易成本、執行狀態

**技術選型**: FastAPI + uvicorn 即可快速原型；任何語言可通過 HTTP/gRPC 調用(Python/C++/Go/Rust)。

---

## 四、語言生態拓展方向

### 4.1 Rust + PyO3 重寫

保持相同 Python API，用 Rust 實現計算核心:
- `numpy` crate 零拷貝互操作(對標 `py::array_t`)
- 所有權系統避免 C++ 的內存管理陷阱
- `rayon` crate 替代 OpenMP 做並行
- 對比 pybind11 vs PyO3 的 DX(Developer Experience)差異

### 4.2 Numba/Cython 純 Python 加速

爲不想裝 C++ 編譯器的用戶提供替代方案:
- **Numba CPU JIT**: `@jit(nopython=True)` 裝飾核心循環，加速 CPU 端計算
- **Numba CUDA**: 需顯式使用 `@cuda.jit` 和 CUDA Array API，重新設計 kernel、線程佈局和內存訪問——**不是 `@jit` 自動獲得 GPU 加速**
- **Cython**: 在 `.pyx` 中聲明 C 類型，構建更簡單(無需 CMake)但性能接近 C++
- 與 C++ 版本的性能對比需在相同硬件和輸入下分別 benchmark

### 4.3 其他語言綁定

**前置條件——當前 C++ 核心不是獨立於 Python 的純 C++ 庫。** 它大量直接依賴 pybind11 類型: `py::array_t`、`py::object`、`py::dict`、`py::tuple`、`py::gil_scoped_release` 等。因此不能"只需新綁定層"。

**階段一: 核心抽象**（先決條件）:
- 抽取不依賴 pybind11 的 C++ 算法庫
- 使用 `std::span`、裸指針+長度或獨立 C ABI
- 定義錯誤碼、內存所有權和線程安全規則
- 保留現有 pybind11 作爲 Python 適配層

**階段二: 語言綁定**（在階段一完成後）:
- **R 綁定**(Rcpp): 量化金融領域 R 用戶羣大，`Rcpp::NumericVector` ↔ C ABI 概念對應
- **Node.js**(node-addon-api): Web 量化平臺常用 Node 後端
- **WASM**(Emscripten): 瀏覽器內運行，配合 Streamlit/Observable 前端
- **Go**(cgo): 高性能微服務場景

> 注意: R/Node/WASM/Go 四條路徑的工作量和風險獨立且差異大，不建議合併爲單一"中等"項目評估。

---

## 五、特徵工程方向

### 5.1 F16-F21 特徵集成

**當前實際實現狀態**（非文檔聲稱的"6 個市場環境特徵"）:

| 特徵 | 功能 | 位置 | 狀態 |
|------|------|------|------|
| F16 | 近 20 日市場波動率 | `src/core/market_features.py` `compute_market_volatility()` | ✅ 已實現 |
| F17 | 大小盤相對強度 | `src/core/market_features.py` `compute_size_relative_strength()` | ✅ 已實現 |
| F18 | — | — | ❌ 未實現 |
| F19 | — | — | ❌ 未實現 |
| F20 | 成交量異常 | `src/core/market_features.py` `compute_volume_anomaly()` | ✅ 已實現 |
| F21 | 波動率變化 | `src/core/market_features.py` `compute_vol_change()` | ✅ 已實現 |

板塊輪動邏輯位於 `src/core/technical.py`（`compute_sector_rotation()`），獨立於 `market_features.py`。"市場寬度"和"資金流"在當前代碼中無對應實現。

因此將 15 維擴展爲 21 維不是簡單拼接，而是至少包含:
1. F18/F19 的定義或恢復（需確定指標含義和數據源）
2. 各模塊特徵 ID 的對齊
3. 外部數據輸入設計（部分特徵依賴非價格數據）
4. Python 與 C++ 雙端實現
5. 21 維輸出契約和 `FEATURE_KEYS` 更新

**前置條件**: 確定 F18/F19 的定義、數據源、頻率和時間對齊規則。

### 5.2 新增特徵類別

| 類別 | 示例特徵 | 數據依賴 |
|------|---------|---------|
| 波動率曲面 | ATM IV、偏度、期限結構斜率 | 期權數據（需數據源+許可） |
| 宏觀因子 | 利率期限結構、信用利差、VIX、美元指數 | 多源宏觀數據（頻率/時區/交易日曆各不同） |
| 資金流 | ETF 淨流入/流出、大單資金流向 | 資金流數據（商業數據源，許可限制） |
| 相關性 | 與基準 ETF(如 SPY/510050)的滾動相關性 | 基準 ETF 價格數據 |
| 流動性 | Amihud 非流動性指標、買賣價差 | 日內數據（頻率遠高於日頻） |

**數據契約要求**（每個數據相關方向均應明確）:

| 字段 | 說明 |
|------|------|
| 數據源 | 具體服務或文件格式 |
| 頻率 | 日頻/分鐘/實時 |
| 時區 | UTC/北京時間等 |
| 可用時間 | 收盤後/盤中/T+1（防止前視偏差） |
| 缺失策略 | 丟棄/前值/插值 |
| 許可 | 是否允許商業使用和再分發 |
| 防前視 | 數據實際可獲得時間 vs 信號生成時間 |

### 5.3 特徵交互與自動選擇

- **交互項**: F1×F6(高相似度 + 高歷史後續收益的聯合信號)、F3×F12(相似度衰減 × 時間跨度)
- **Boruta / SHAP**: 特徵重要性分析和約簡
- **RFE**(遞歸特徵消除): 找到最小有效特徵子集
- **遺傳編程**: 自動生成非線性特徵組合

---

## 六、ML 增強方向

### 6.1 恢復原始 ML Stacking

**前置條件（阻塞項）**:
- 原始 V3.3 的 RF/SVM 訓練代碼、模型參數和訓練數據**不在本倉庫內**
- 原始標籤定義、特徵工程步驟和交叉驗證方案需從歸檔基線恢復
- 時序交叉驗證(purged k-fold)的具體實現需獨立設計

原始 V3.3 做了 RF/SVM Stacking → 15 維特徵 → 綜合信號。在滿足前置條件後，Fork 可:
- 恢復 RF+SVM 兩層 Stacking
- 升級爲 XGBoost + LightGBM + CatBoost Stacking(三模型投票)
- 添加深度學習層(LSTM/Transformer 替代 DTW 做序列匹配)
- **關鍵**: 時序交叉驗證(purged k-fold)防止前視偏差
- **驗收**: 樣本外測試集上的風險調整後收益 + 與原始 V3.3 的對比（如有原始結果）

> 標註爲"需要外部資料"——不完全依賴外部不代表可以忽略前置條件。此方向的實際開工門檻遠高於"高改動量"的標籤。

### 6.2 參數自適應/在線學習

當前所有參數(L_query=20, T_back=750, M_forward=5, k=10, cos_prefilter_top=50)硬編碼。
- **Walk-forward 優化**: Optuna/Hyperopt 在滾動窗口上做超參搜索
- **在線自適應**: EWMA 更新 `cos_prefilter_top`(市場波動大 → 減少候選，波動小 → 增加候選)
- **Regime 切換**: 檢測波動率 Regime → 切換參數集(高波動參數組 vs 低波動參數組)

### 6.3 強化學習持倉管理

將形態匹配作爲狀態編碼器，強化學習做持倉決策:
- **State**: 15 維特徵 + 當前持倉 + 賬戶狀態
- **Action**: 調倉方向(增加/減少/清倉 ETF)
- **Reward**: 風險調整後收益 + 交易成本懲罰
- 形態匹配提供特徵提取，RL 提供決策規則——兩個系統的接口是 15 維特徵向量

---

## 七、資產類別擴展

### 7.1 加密貨幣

加密市場與 ETF 有截然不同的微觀結構:
- 24/7 交易、無漲跌停 → 需調整 M_forward 和 T_back 參數(更高頻)
- 永續合約 → funding rate 可作爲額外特徵（注意數據源許可）
- 缺失數據處理: 交易所宕機 / 數據源不連續

### 7.2 A 股個股

從 ETF 擴展到個股需額外處理:
- 停牌/漲跌停/ST 導致的缺失數據 → 需增強 `standardize_returns_cpp` 的健壯性
- 除權除息 → 前復權價格處理
- 行業中性化 → 個股形態相似性可能僅是行業 β，需截面去均值

### 7.3 跨資產類別

- **商品期貨**: 期限結構特徵 + contango/backwardation
- **外匯**: 利差 + 央行政策日曆
- **可轉債**: 轉股溢價率 + 純債價值

> 以上方向均涉及外部數據源——參照 §5.2 數據契約要求。

---

## 八、基礎設施方向

### 8.1 預編譯 Wheel 分發

**前置條件（開工前須解決）**:
1. **Python 版本矛盾**: `pyproject.toml` 聲明 `requires-python = ">=3.10"`，但頂層 `CMakeLists.txt` 使用 `find_package(Python 3.12 REQUIRED ...)`——Python 3.10/3.11 無法通過 CMake 構建。須統一: 要麼限制爲 Python 3.12+，要麼修改 CMake 兼容聲明版本矩陣。
2. **包佈局**: `wheel.packages = ["src/cpp"]` 未顯式包含 `src/core`（Python 參考實現），需明確打包範圍。
3. **驗證**: 在 clean virtualenv 中驗證 `pip install dist/*.whl && python -c "import etf_core"`。

Fork 可在解決前置條件後:
- **cibuildwheel**: 構建 Windows/Linux/macOS × x86_64/ARM64 全平臺 wheel（注意: 當前 CI 雖覆蓋三平臺但僅測 Python 3.12，不等於已驗證全矩陣）
- **PyPI 發佈**: `pip install etf-core` 一行安裝
- **conda-forge**: conda 生態分發

**驗收條件**: 構建成功 + 安裝成功 + `import etf_core` 通過 + `import core` 可導入 + 類型 stub 可用 + 至少 smoke test 通過。

### 8.2 實時數據管線

從"離線批量跑特徵"變成"每日自動信號生成":
- WebSocket 實時數據(AKShare/Tushare/Binance)——注意各數據源的許可和再分發限制
- Redis 緩存預計算窗口(避免重複標準化)
- Cron/Airflow 定時任務: 每日收盤後自動生成 signals
- 消息推送: Slack/DingTalk/企業微信

**數據契約**: 參照 §5.2 數據契約要求——頻率、時區、可用時間、缺失策略、防前視。

### 8.3 性能回歸監控

在現有 `benchmarks/` 框架上擴展:
- CI 中自動比較不同 commit 的 benchmark JSON
- 單邊減速閾值 → 自動告警
- 多硬件基線(不同 CPU 世代的參考值)

---

## 九、學術/教育方向

### 9.1 交互式可視化平臺

**前置條件**: 當前 `pattern_match_single()` 主要返回 15 維聚合特徵字典——沒有穩定的公開接口返回候選窗口索引、每個候選的 cosine/DTW/綜合得分/歷史後續收益/DTW 對齊路徑。可視化 Top-5 匹配和 DTW path 需先新增可選 debug/trace API。

將 Jupyter Notebook 擴展爲完整體驗:
- **Streamlit/Gradio Web App**: 選 ETF → 調參數 → 看歷史 Top-5 匹配 → 看後續表現
- **Plotly 可視化**: 查詢窗口與匹配窗口疊加圖 + DTW 對齊路徑熱力圖
- **參數沙盒**: 實時調整 L_query/T_back/k 等參數並觀察結果變化

**前置 API 需求**（建議先於可視化工作完成）:
```python
pattern_match_single(..., return_details=True)
# 返回: query_range, candidate_ranges, cosine_scores,
#        dtw_distances, combined_scores, future_returns, dtw_paths
```
同步更新 `src/cpp/pyi/etf_core.pyi`、Python 參考實現、C++ 實現和測試。

### 9.2 DTW 變體系統基準測試

純學術 fork:
- 在統一數據集上跑標準 DTW / Soft-DTW / DDTW / Weighted DTW / ShapeDTW / FastDTW
- 比較維度: **歷史匹配窗口後續收益統計** + 計算速度 + 參數敏感性
- 現有 `benchmarks/run_benchmark.py` + JSON 結果格式天然支持多算法對比
- 產出: 一篇方法論比較文章或技術報告

### 9.3 算法可視化教材

將 15 維特徵(F1-F15)每個維度做成獨立可視化:
- 高相似度→高收益的 case vs 高相似度→低收益的 case，形成對比教學
- DTW 對齊路徑的動態演示(animations)
- "形態匹配失敗"的典型案例分析

---

## 十、方法論改進方向

### 10.1 復現原始 V3.3 性能

**⚠️ 外部資料阻塞——開工前必須獲得**:
- [ ] 原始 V3.3.py 完整文件（含掘金平臺綁定和策略邏輯）
- [ ] 原始訓練數據（或等效數據集 + 數據版本）
- [ ] RF/SVM 模型超參數和序列化文件（如有）
- [ ] 原始回測配置（時間範圍、交易成本、滑點、停牌規則）
- [ ] 原始回測結果統計口徑（用於對比驗證）
- [ ] 掘金 SDK 和平臺賬號

當前項目明確說"不能重跑原始回測，不含完整平臺綁定策略"。在獲得上述資料前，此方向無法獨立開工。一旦獲得資料，這是典型的學術復現研究——對理解策略真實有效性有方法論價值。

### 10.2 審查方法論泛化

本項目的核心方法學價值在於其**審查流程**(多輪跨後端審查 + 0 回歸)。Fork 將這套 SOP 應用於:
- 其他量化策略的 C++ 加速 → 通用框架: 提取純計算 → pybind11 加速 → 跨後端一致性驗證
- 不同加速方式之間的對比審查(C++ vs Rust vs Numba vs 純 NumPy)
- 建立 "AI 輔助量化策略代碼審查 checklist"

### 10.3 與原始策略的差異量化

定量分析提取前後的差異:
- 在相同輸入下，C++ 版本的輸出與 Python 版本的浮點級差異分佈
- 這些差異在策略層面的累積效應(是否影響最終的持倉決策?)
- 這是 "AI 輔助代碼遷移保真度" 研究的一個案例

---

## 十一、正確性與跨後端契約驗證

> 此方向由 GPT-5.6-Sol 審查提出——項目的獨特優勢不僅是 C++ 加速，還包括 Python 參考實現 + 嚴格一致性驗證 + 54 測試 + 多後端審查流程。當前方向列表偏重性能和功能，遺漏了正確性驗證這條獨立線索。

將本項目的驗證體系泛化爲可複用的 fork 方向:
- **Property-based testing**: 使用 Hypothesis 生成隨機輸入(含 NaN/Inf/零長度/常數序列/非連續數組/dtype 變化)，驗證 Python/C++/替代後端在數值、異常和返回結構上的一致性
- **模糊測試**: 隨機輸入 + 固定種子，跨後端差分測試
- **邊界輸入目錄**: 零長度序列、單元素、常數序列、全 NaN、極大/極小值、非連續佈局
- **跨後端一致性矩陣**: Python vs C++ vs Rust vs Numba vs Cython——統一的數值容差(距離 1e-8, 得分 1e-6)、異常語義和返回結構契約
- **回歸測試自動化**: 每次算法改動自動觸發全量一致性驗證

**關聯文件**: `src/core/dtw.py`、`src/core/pattern_match.py`、`src/cpp/etf_core.cpp`、`src/cpp/pyi/etf_core.pyi`、`verify_etf_core.py`、`verify_batch.py`、`tests/`

---

## 按實現門檻與外部依賴排序的 Fork 方向

> 排序邏輯: 先按"可直接開工"分組，組內按改動量排序。"可直接開工" = 所有入口文件和數據在本倉庫內可用 + 無需外部平臺/賬號。

### 可直接開工

| 方向 | 改動量 | 技術風險 | 驗收清晰度 | 獨立價值 | 入口文件 |
|------|--------|---------|-----------|---------|---------|
| DTW 變體替換(DDTW/Weighted DTW) | 低 | 中 | 高 | 中 | `src/cpp/etf_core.cpp` `dtw_distance_span()` |
| 候選檢索加速(剪枝/索引) | 低-中 | 中 | 中 | 中 | `pattern_match_core()` 餘弦循環 |
| 得分公式重設計 | 低-中 | 中 | 中 | 中 | `etf_core.cpp:680–690` |
| 多線程並行化批量 | 中 | 高(數據競爭) | 高 | 中 | `pattern_match_batch()` 循環 |
| 正確性與跨後端契約驗證 | 中 | 中 | 高 | 高 | `verify_etf_core.py` + `tests/` |

### 需要外部資料或平臺

| 方向 | 改動量 | 外部依賴 | 技術風險 | 獨立價值 | 阻塞項 |
|------|--------|---------|---------|---------|--------|
| Streamlit 可視化 Web App | **中¹** | 無 | 中 | 高 | 需先實現 debug/trace API(§9.1) |
| 預編譯 Wheel + PyPI 發佈 | **中¹** | 無 | 中 | 高 | Python 版本矛盾 + 包佈局(§8.1) |
| 接回回測框架 | 中 | 回測框架 | 中 | 高 | 原始數據/配置不在倉庫內 |
| 擴展到加密貨幣/A股個股 | 中 | 新市場數據源+許可 | 中 | 中 | 數據契約待確定 |
| 風控執行層(止損/熔斷/調度) | 中 | 無 | 中 | 中 | 需先明確與計算層的接口 |
| 信號服務器(計算服務層) | 中 | 無 | 中 | 中 | 需定義 API schema |
| F16-F21 完整集成 | 中-高 | F18/F19 定義+數據源 | 中 | 中 | 缺失特徵定義和數據 |
| 多 ETF 截面輪動 | 高 | 回測框架+交易成本模型 | 高 | 高 | 需多 ETF 批量接口 + 截面排序層 |
| 多語言綁定(R/Node/WASM/Go) | **高¹** | 無 | 高 | 中 | 需先抽取不依賴 pybind11 的 C ABI 核心(§4.3) |
| GPU 加速(CUDA) | 高 | CUDA 工具鏈+硬件 | 高 | 高 | 無;但 10-20× 爲待驗證假設 |
| ML Stacking 恢復 | 高 | 原始代碼/數據/模型 | 高 | 高 | 原始文件不在倉庫內 |
| SIMD 向量化 + SoA | 高 | 無 | 高 | 中 | CPU 分發+數值一致性待設計 |
| 復現原始 V3.3 完整策略 | 高 | 原始文件+掘金 SDK+數據 | 很高 | 高 | **外部資料阻塞——無法獨立開工** |
| 強化學習持倉管理 | 高 | RL 框架+回測環境 | 高 | 中 | 需回測框架就緒 |
| 實時數據管線 | 中-高 | 數據源+消息推送服務 | 中 | 中 | 數據源許可+可用時間待確認 |

> ¹ 原稿標爲"低"或"中-"，審查後上調（Streamlit 需前置 debug API，Wheel 有構建配置矛盾，多語言綁定需架構重構）。

### 純學術/教育方向（獨立價值以學術意義爲主）

| 方向 | 改動量 | 外部依賴 | 產出類型 |
|------|--------|---------|---------|
| Numba/Cython 加速對比 | 中 | 無 | 技術報告/博客 |
| DTW 變體系統基準測試 | 中 | 無 | 方法論比較文章 |
| Rust + PyO3 重寫對比 | 高 | 無 | 工程對比報告 |
| 算法可視化教材 | 中 | 需 debug API | 教學材料 |
| 審查方法論泛化 | 低(文檔爲主) | 無 | SOP 框架 |
| 與原始策略差異量化 | 中 | 原始 V3.3 歸檔 | 保真度研究 |

---

## 關鍵約束與注意點

### 許可證與外部依賴邊界

1. **MIT 許可證**僅覆蓋本倉庫發佈的代碼。以下不在 MIT 覆蓋範圍內，須單獨核查許可:
   - 掘金 SDK 及平臺服務條款
   - AKShare / Tushare / Binance 等外部數據源（含商業使用限制）
   - 歷史行情數據的再分發權利
   - 原始策略中不屬於本倉庫的文件
   - 第三方模型（如 XGBoost/LightGBM 訓練出的模型文件）和依賴庫

2. **無掘金 SDK**: 原始平臺綁定不在倉庫內，任何"恢復完整策略"的 fork 需自行處理平臺適配和許可。

3. **單平臺基準測試**: 當前 benchmark 數值(34×/53×/2.2×/93×)來自 Windows + MSVC，不同平臺/編譯器需重新校準。

### 術語約定

爲避免從"歷史統計特徵"到"策略預測能力"的過度推斷，本文檔使用以下術語區分:

| 術語 | 含義 | 不等於 |
|------|------|--------|
| **歷史匹配片段後續收益** | 歷史匹配窗口在其後 M_forward 個時間點的收益統計（即當前 F6-F11 的本質） | 未來收益 / 策略收益 |
| **歷史統計特徵** | 基於歷史數據計算的描述性指標 | 預測信號 |
| **模型預測** | 經時序交叉驗證和樣本外測試的 ML 模型輸出 | 未經校準的統計值 |
| **回測實現收益** | 在明確交易成本、滑點和執行規則下的回測結果 | 實盤收益 |
| **交易後淨收益** | 扣除全部成本後的實現收益 | 回測模擬收益 |

"可投產""策略提升""驗證原始性能"等表述在本文檔中均指**在補齊執行層、交易成本建模和樣本外驗證後的可能性**，非對當前倉庫代碼的績效聲明。

### 浮點與契約

4. **15 維特徵順序**: `etf_core.FEATURE_KEYS` 已固定爲模塊常量，修改特徵須同步更新該常量 + 所有引用處。

5. **GIL 釋放邊界**: 添加新函數時注意 `py::gil_scoped_release/acquire` 的正確位置。**工作線程不應直接創建 Python 對象**——詳見 §2.3 和 CLAUDE.md。

6. **浮點容差**: C++ vs Python 一致性驗證的容差標準(距離 1e-8, 得分 1e-6)，改動算法後需重新驗證。**SIMD/GPU 等改變計算順序的優化可能破壞此容差**——性能驗收和數值驗收須分開。

---

## 關聯文件

### 源碼
- `src/cpp/etf_core.cpp` — 全部 C++ 加速邏輯(~1100 行，註釋詳細)
- `src/cpp/pyi/etf_core.pyi` — C++ 類型存根(API 契約)
- `src/core/dtw.py` — DTW 距離 + 序列標準化(Python 參考)
- `src/core/pattern_match.py` — 形態匹配引擎 15 維特徵(Python 參考)
- `src/core/technical.py` — ADX / ATR / 板塊輪動
- `src/core/market_features.py` — F16/F17/F20/F21 市場環境特徵
- `src/core/risk_controls.py` — 滾動波動率分位數 / MA 趨勢 / 倉位上限
- `src/core/metrics.py` — Sortino / Calmar / 最大回撤 / IC 統計

### 構建與 CI
- `pyproject.toml` — Python 構建配置(scikit-build-core)
- `CMakeLists.txt` — 項目構建配置(頂層)
- `src/cpp/CMakeLists.txt` — C++ 模塊構建配置
- `.github/workflows/ci.yml` — 三平臺 CI(Windows/Linux/macOS, Python 3.12)
- `.github/workflows/benchmark.yml` — 性能回歸 CI
- `.github/workflows/sanitizer.yml` — ASAN+UBSAN CI

### 測試與驗證
- `tests/test_dtw.py` — DTW 模塊測試(27 項)
- `tests/test_pattern_match.py` — 形態匹配測試(15 項)
- `tests/test_technical.py` — 技術指標測試(12 項)
- `tests/test_etf_core.cpp` — C++ 原生測試(58 cases)
- `verify_etf_core.py` — C++ vs Python 一致性驗證
- `verify_batch.py` — 批量形態匹配驗證

### 文檔
- `CLAUDE.md` — pybind11 實戰經驗、GIL 管理、ABI 排錯
- `project_status.md` — 審查鏈譜系、會話歷史
- `benchmarks/run_benchmark.py` — 可復現基準測試
- `benchmarks/results/` — 歷史 benchmark JSON
