# 情境簡報：成果發表 / Demo · Launch readout

> **標示：內容模板 (content template) — 不是預設美工排版**  
> Agent **只學**報告內容與決策風格：BLUF、stakes、options、REC、期限、章節意圖、故事線。  
> **不要**照抄 sample PPTX 的配色、字級、版心、座標或裝飾；真實交付用公司母片，只遷移本檔結構與話術。詳見 [presentations/README](README.md)「內容模板 ≠ 美工」。

**場合：** 功能上線、專案階段完成、first silicon / sample 成功、對內 demo day  
**聽眾：** 部門內 + 主管；可能有產品/業務  
**時長：** 20–30 min（demo 另計）  
**Skills：** (a) · (e) department value  

---

## BLUF

> **Result:** [X] shipped / achieved on [date]; **impact:** [metric vs baseline].  
> **Status:** Green (or Yellow with residual risk…).  
> **Not asking for money today** / **Asking for:** [visibility / next-phase approval].

成果會也要有「所以呢」— 否則像活動錄影帶。

---

## Slide outline

| # | 標題句 | 內容 |
|---|--------|------|
| 1 | **BLUF：我們交付了什麼 + 為何重要** | 對齊公司/部門 OKR 一句 |
| 2 | **Goal recall** | 期初承諾是什麼（避免移動門柱） |
| 3 | **Outcome metrics** | Target / Actual / Δ；1–4 個 KPI 即可 |
| 4 | **Demo or evidence** | 截圖、log、silicon photo、客戶引言—**短** |
| 5 | **How we got here** | 3 個關鍵決策/取捨（不是流水帳） |
| 6 | **What we learned** | 可複製的 2 點 + 1 個 stop-doing |
| 7 | **Residual risk / follow-ups** | 未完項、技術債、監控 |
| 8 | **Next + ask** | 下一階段 / 需要的支持或「無 ask」 |
| B | Timeline detail, full metrics | |

---

## Metric 寫法（外商 / 竹科）

| 類型 | 示例 |
|------|------|
| 產品/軟體 | p95 latency 400ms → 120ms；adoption 12% WAU |
| 平台 | 部署頻率 ×2；change fail −30% |
| IC | Power −8% at iso-perf；bring-up day-3 boot；test coverage gate met |
| 客戶 | Sample 如期交 Tier-1；critical bug 0 open |

---

## 講稿注意

- **先結果再過程**（金字塔）  
- Demo 失敗備案：預錄 60 秒 + 指標頁  
- 點名貢獻可以 30 秒，不要變頒獎典禮擠掉 impact  

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| 對照期初承諾 | 只秀忙碌的 sprint 圖 |
| 講清楚「還沒做完什麼」 | 粉飾後被追問崩盤 |
| 結束有 next step | 掌聲結束、零決策、零追蹤 |

---

## Pattern provenance (public)

**Pattern:** Launch / silicon bring-up readout (impact first)

| Source | URL |
|--------|-----|
| MediaTek public 2nm tape-out milestone language | https://www.mediatek.com/press-room/mediatek-develops-chip-utilizing-tsmcs-2nm-process-achieving-milestones-in-performance-andpower-efficiency |
| SRE Book — example postmortem impact summary shape | https://sre.google/sre-book/example-postmortem/ |

Synthetic example deck uses NovaSemi/Aurora story; structure follows the sources above. Full map: [classic-public-cases.md](classic-public-cases.md).

## See also

- [00-style](00-style-mnc-and-hsinchu.md) · [(e)](../department-value/presenting-department-value.md) · [(a)](../executive-communication/decision-ready-updates.md) · 期末版 [09](09-period-end-review.md)
