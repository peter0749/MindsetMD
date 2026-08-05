# Deck style: 外商科技 × 竹科 IC 設計

**Audience of this note:** 做向上 / 部門內簡報的 tech lead、EM、PM、設計/驗證主管。

---

## 兩種「口音」，同一套決策邏輯

| 維度 | 外商（Google / Qualcomm / AMD 類） | 竹科 IC 台商（聯發科類） |
|------|-----------------------------------|---------------------------|
| 開場 | Bottom line / OKR / Green-Yellow-Red | 結論 + 時程/客戶/風險一句話 |
| 證據 | 產品/系統 metric、DORA-ish、customer | Spec、milestone（RTL freeze、tape-out）、PPA、yield、customer sample |
| 風險語言 | Reliability、security、debt、capacity | Schedule、ECO、IP、foundry、silicon spin、dependency |
| 簡報長度 | 少頁 + thick appendix | 也要少頁；細節常被要求進「附件/技術附錄」 |
| 語言 | 多英文 deck；中文講解 | 中英混用常見；對上英文 title + 中文口語 |
| 文化雷達 | 公開 challenge 較直接 | 公開場合留面子；**會前 pre-wire** 更重要 |
| 決策期待 | Options + recommendation + owner | 同上；常多一層「需不需再報上層/客端」 |

**共通鐵律（兩邊都成立）：**

1. **結論在第一頁**（不是最後一頁驚喜）  
2. **今天要什麼決策寫清楚**  
3. **數字有 baseline / target / actual**  
4. **風險附 mitigation 或 accepted risk**  
5. **主軸 ≤ 8–12 頁**；其餘 backup  
6. **會前 pre-wire 老闆**（尤其壞消息）— 見 skill (a)(c)

---

## 投影片版面紀律（兩種口音共用）

| 規則 | 做法 |
|------|------|
| 一頁一訊息 | 標題 = 完整句子結論，不是「Overview」 |
| 標題句示例 | 「Q2 tape-out 風險：package 供應延 3 週 → 建議切 revB 範圍」 |
| 少字 | 口頭講故事；投影片只放骨架與數字 |
| RAG 狀態 | Green / Yellow / Red + **一句 why** |
| 表格優於段落 | Options、trade-off、里程碑用表 |
| 來源角標 | 圖表角標 data as of / owner |
| 決策頁固定 | Options / Rec / Need by date / Owner |

**標題壞：** `Update` / `Progress` / `Discussion`  
**標題好：** `Authentication rewrite: on track for 6/15; need product call on scope cut`

---

## 半導體 / 系統常用「聽得懂」的詞（可混進外商 deck）

| 概念 | 簡報上怎麼寫 |
|------|----------------|
| 節點 / 製程 | N3 / N4 / process risk to schedule |
| PPA | Power / Performance / Area vs target |
| 里程碑 | Arch freeze → RTL freeze → DV exit → Tape-out → First silicon → Customer sample |
| 風險 | ECO storm、IP late、IP reuse、foundry slot、tool license、人力 skill gap |
| 品質 | Bug escape、coverage gate、silicon fail rate、RMA 類比 |
| 客戶 | Tier-1 design-win / sample 交付 / field trial |

軟體/平台外商則把里程碑換成：**Design doc → RFC → Launch → SLO**。

---

## 時間盒（向上 30 / 45 / 60 分）

| 長度 | 主軸頁數 | 分配 |
|------|----------|------|
| 30 min | 6–8 | 5' BLUF+agenda → 15' evidence → 8' options/decision → 2' next |
| 45 min | 8–10 | 多 1 頁 risk deep-dive 或 demo |
| 60 min | 10–12 | 可加 1 個 appendix walk only if asked |

超時通常因為：**沒有 Decision 頁** 或 **主軸塞滿 backup**。

---

## 雙語簡報速成

- **Deck 標題 / BLUF / Options：英文**（方便 HQ / 外籍主管轉寄）  
- **口頭解釋：中文或中英**  
- 數字單位先統一（mW、mm²、ms、%、USD）  
- 避免整頁中文長句 + 整頁英文長句混戰—選一種主語言做標題句  

---

## 會前 / 會後（強制）

| 時機 | 動作 |
|------|------|
| T-24h | 1-page pre-read 或 deck 連結；標「請決策頁」 |
| T-2h | 老闆 pre-wire 黃燈/紅燈 |
| 會中 | 最難決策先講 |
| ≤2h 後 | Decisions + Actions 表（owner / date） |

詳見 [(a)](../executive-communication/decision-ready-updates.md) [(c)](../meetings/in-meeting-and-follow-through.md)。

---

## 來源與風格依據（非公司內部模板）

- Decision-first / BLUF executive decks — 與 corpus skill (a) 及常見 QBR「status → risks → decisions」結構一致  
- QBR answer-first structure — 業界 QBR 寫作慣例（exec summary → metrics → initiatives → asks）  
- Roadmap decision-first one-slide executive view — 常見 product/eng roadmap 簡報實踐  
- IC 里程碑與 PPA 語彙 — 半導體工程管理通用語言（非任一公司機密模板）  

本系列為 **合成實用骨架**，請換成你司 metric 名稱與 stage-gate 名稱。
