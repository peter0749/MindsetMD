# Presentation scenarios — 向上 / 部門內簡報 **內容模板**

## 給 Agent / 使用者：內容模板 ≠ 美工排版

| 標示 | 含義 |
|------|------|
| **內容模板 (content template)** | 報告**說什麼、怎麼決策**：BLUF、stakes、options、REC、期限、故事線、外商/IC 敘事風格 |
| **不是預設美工排版 (not default visual design)** | **不是**公司母片／品牌規範／design system；色票、字級、版心、座標可全部丟掉 |

**一句話：** 學「內容風格與決策結構」；**不要**把 sample PPTX 當美編規範照抄。

**Agent 行為：**

1. **要學／要產出的：** 章節意圖、決策包、外商/IC 敘事風格（decision-first、metric、milestone）。  
2. **不要照抄的：** PPTX 視覺排版、officecli 座標、navy 裝飾、badge 文字、精確間距。  
3. 真實交付：用**使用者指定的母片/品牌**；只遷移**內容結構與話術**。  
4. 權威優先序：**playbook skill (a–f)** → **本目錄 outline MD** → **storyline / situation 欄位** → PPTX 僅作可開啟示範（載體，非美工 SoT）。

**用途：** 依「情境」套用 **內容骨架**（MD outline + 示範 PPTX）。風格對齊 **科技業外商**（decision-first、metric-heavy、options+ask）與 **竹科 IC**（里程碑 / silicon / customer / PPA·schedule 語彙）。

**不是：** 美工模板、預設排版系統、公司機密範本翻版、不可改的 design system。  
**是：** 每頁**放什麼內容**、結尾**要什麼決策**、example 裡**發生什麼事**。

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

**可編輯 PPTX（內容載體，非美工）：** [assets/README.md](assets/README.md)  
- 內容骨架占位：`assets/pptx/templates/01`–`09`  
- 內容範例（Aurora/NovaSemi 連貫故事）：`assets/pptx/examples/01`–`09`  
- 兩者皆 **content template**；勿當公司 design system。
**產業簡報結構研究筆記：** [research-deck-norms.md](research-deck-norms.md)  
**經典公開案例對照（軟體/IC）：** [classic-public-cases.md](classic-public-cases.md)

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
3. **Deck = 內容應用層**（不是美編層）；行為細節以 playbook 為準。衝突時以 [consistency-audit](../shared/consistency-audit.md) + index canonical 表為準。  
4. **內容模板優先於 PPTX 外觀** — Agent 生成報告時只保證決策可讀與結構完整，不要求還原 sample 檔的視覺。  
5. **Type 1 / 新產品 go/no-go 可以是 memo 不是 deck** — 六頁 or PR/FAQ；決策句型仍跟 (a)。對照：[amazon-mapping](../shared/amazon-mapping.md)。不要為 Amazon 另做第七套簡報骨架。

---

## 建議閱讀順序

1. [00-style](00-style-mnc-and-hsinchu.md)（10 分鐘）  
2. 對應情境檔  
3. 回鏈 skill 補話術  

**Index 上層：** [../README.md](../README.md)
