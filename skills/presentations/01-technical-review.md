# 情境簡報：技術報告 / Design · Tech Review

**場合：** Architecture review、design freeze、重大 refactor RFC、DV/bring-up 技術同步  
**聽眾：** Peer architects、EM、跨隊 tech lead；偶有 skip-level  
**時長：** 30–45 min  
**Skills：** (a) decision-ready · (d) plan · (f) cross-team  
**風格：** 外商 = 選項與 trade-off 清楚；竹科 = 里程碑/依賴/風險寫死  

---

## BLUF（第一頁就寫）

> **Decision needed:** Approve Option **B** (phased rollout) for [system].  
> **Status:** Yellow — [risk] threatens [milestone date].  
> **Ask by:** [date] from [name/role].

---

## Slide outline

| # | 標題句（示例） | 放什麼 |
|---|----------------|--------|
| 1 | **BLUF + 狀態 RAG** | 一句結論、要的決策、今日不討論什麼 |
| 2 | **Problem / Goal** | 誰痛、成功長什麼樣（可測） |
| 3 | **Constraints** | 時程、PPA/SLO、人力、依賴 IP/平台 |
| 4 | **Options compared** | A/B/C 表：cost / risk / schedule / quality |
| 5 | **Recommendation + why** | 選 B 的 2–3 個理由（對齊事業目標） |
| 6 | **Design sketch（1 頁）** | 方塊圖 / 資料流；細節 backup |
| 7 | **Risks & mitigations** | Top 3；每項 owner |
| 8 | **Plan & capacity hit** | 里程碑 + 對其他項目的 displacing |
| 9 | **Decision / Actions** | 核准什麼、open questions、next review |
| B | Appendix | 數據、實驗、反對意見回應、詳細時程 |

### Options 表（建議固定欄）

| Option | Outcome | Schedule | Risk | Capacity | Notes |
|--------|---------|----------|------|----------|-------|
| A Fast | … | … | High | Low | |
| B Phased | … | … | Med | Med | **Rec** |
| C Do nothing | … | … | … | — | Accepted risk? |

---

## 講稿骨架（3 分鐘開場）

1. 「今天只要一個決策：…」  
2. 「若不決策，預設等於選 C，後果是…」  
3. 「我建議 B，因為…；細節在後面，可先跳到決策頁。」  

---

## 外商 vs 竹科著重點

| | 外商 | 竹科 IC |
|--|------|---------|
| 圖 | 服務邊界、SLO、遷移策略 | Block diagram、clock/reset 責任、interface |
| 風險 | Blast radius、rollback | ECO、IP freeze、foundry、tool |
| 結束 | Launch checklist | Gate：exit criteria 給下一階段 |

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| 標題句 = 立場 | 20 頁微架構 walkthrough 當主軸 |
| 明示「決策 vs 資訊同步」 | 開完會大家不知道過了沒 |
| 反對方案寫進 Options | 只推自己最愛、假裝沒人反對 |

---

## Success signals

- [ ] 會後 24h 內有書面 go / no-go  
- [ ] 依賴團隊知道自己的 action  
- [ ] Backup 被問到才翻，不是全程念附件  

---

## Pattern provenance (public)

**Pattern:** Design-doc / RFC options table + residual risk

| Source | URL |
|--------|-----|
| StaffEng — Writing engineering strategy | https://staffeng.com/guides/engineering-strategy/ |
| Utterskills — options instead of single conclusion | https://utterskills.com/blog/communication-skills-for-software-engineers |

Synthetic example deck uses NovaSemi/Aurora story; structure follows the sources above. Full map: [classic-public-cases.md](classic-public-cases.md).

## See also

- [00-style](00-style-mnc-and-hsinchu.md) · [(a)](../executive-communication/decision-ready-updates.md) · [(d)](../roadmap-planning/planning-sense-proactive-framing.md) · [(f)](../cross-team/conflict-and-coordination.md)
