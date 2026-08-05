# Presentation scenarios — 向上 / 部門內簡報骨架

**用途：** 依「情境」套用 slide outline（非 PowerPoint 檔）。風格對齊 **科技業外商**（Google / Qualcomm / AMD 類：decision-first、metric-heavy、options+ask）與 **台灣竹科 IC 設計台商**（聯發科類：里程碑 / silicon / customer / yield·power·schedule 語彙、期初期末審慎）。

**不是：** 美工模板、公司機密範本翻版。  
**是：** 可直接複製成投影片標題 + 每頁放什麼 + 結尾要什麼決策。

---

## 快速選表

| 情境 | 檔案 | 典型場合 | 核心 skill |
|------|------|----------|------------|
| 技術報告 / Design·Tech Review | [01-technical-review.md](01-technical-review.md) | Architecture review、design freeze、bug bash debrief | (a)(d)(f) |
| 成果發表 / Demo·Launch readout | [02-results-demo.md](02-results-demo.md) | Feature ship、silicon bring-up 成果、demo day | (a)(e) |
| 管理成效 / Org·People health | [03-management-effectiveness.md](03-management-effectiveness.md) | EM 對上 1:1、org review | (e)(a)(b) |
| 效益呈現 / Impact·ROI | [04-benefit-value.md](04-benefit-value.md) | 證明部門/專案價值、續編預算 | (e)(a) |
| 採購提案 / Vendor·Tool buy | [05-procurement-proposal.md](05-procurement-proposal.md) | EDA/cloud/設備/授權採購 | (b)(a) |
| 爭取資源 / HC·Budget | [06-resource-request.md](06-resource-request.md) | Headcount、budget、air cover | (b)(d)(a) |
| 路線圖呈現 / Roadmap | [07-roadmap.md](07-roadmap.md) | 季/半年 roadmap、stakeholder sync | (d)(a)(f) |
| 期初規劃 / Kickoff·AOP start | [08-period-start-planning.md](08-period-start-planning.md) | 年初 / 季初 commit | (d)(a)(b) |
| 期末呈現 / QBR·Close | [09-period-end-review.md](09-period-end-review.md) | 季末 QBR、年終 review | (e)(a)(d) |

風格與投影片紀律： [00-style-mnc-and-hsinchu.md](00-style-mnc-and-hsinchu.md)

**可編輯 PPTX（officecli）：** [assets/README.md](assets/README.md)  
- 模板：`assets/pptx/templates/01`–`09`  
- 情境範例（Aurora/NovaSemi 連貫故事）：`assets/pptx/examples/01`–`09`  
**產業簡報結構研究筆記：** [research-deck-norms.md](research-deck-norms.md)

---

## 所有簡報共用的「外商骨架」（先記這個）

```text
Slide 1  Title + BLUF（結論/狀態/要什麼）
Slide 2  Agenda + 今天要做的 Decision(s)
…
Body     證據（metric / milestone / risk）— 少於 7 頁主軸
Ask      Options A/B/C + Recommendation + 決策期限
Backup   細節進 appendix（被問再翻）
```

會後 2 小時：用 [(c) meetings](../meetings/in-meeting-and-follow-through.md) 寫 Decisions + Actions。

---

## 與 upward skills 的關係

| 簡報類型 | 話術從哪來 |
|----------|------------|
| 任何向上 | [(a) decision-ready](../executive-communication/decision-ready-updates.md) |
| 容量 / 路線 | [(d) roadmap](../roadmap-planning/planning-sense-proactive-framing.md) + [capacity](../shared/capacity-model.md) |
| 要錢要人 | [(b) resources](../resource-advocacy/securing-resources-upward.md) |
| 講價值 | [(e) department value](../department-value/presenting-department-value.md) |
| 跨單位卡關 | [(f) conflict](../cross-team/conflict-and-coordination.md) |

### 簡報層紀律（避免與 a–f 衝突）

1. **不發明第三套 capacity %** — 只引用 [capacity-model](../shared/capacity-model.md)：路線圖/期初/管理負荷用 **A**；HC 簡報用 **B**。  
2. **不發明第二套 SOR** — BLUF / Options / Rec / Ask 一律跟 (a)。  
3. **Deck = 應用層**；行為細節以 playbook 為準。衝突時以 [consistency-audit](../shared/consistency-audit.md) + index canonical 表為準。

---

## 建議閱讀順序

1. [00-style](00-style-mnc-and-hsinchu.md)（10 分鐘）  
2. 對應情境檔  
3. 回鏈 skill 補話術  

**Index 上層：** [../README.md](../README.md)
