# 情境簡報：採購提案 / Vendor · Tool · License · 設備

> **標示：內容模板 (content template) — 不是預設美工排版**  
> Agent **只學**報告內容與決策風格：BLUF、stakes、options、REC、期限、章節意圖、故事線。  
> **不要**照抄 sample PPTX 的配色、字級、版心、座標或裝飾；真實交付用公司母片，只遷移本檔結構與話術。詳見 [presentations/README](README.md)「內容模板 ≠ 美工」。

**場合：** EDA/IP/雲/儀器/服務合約、續約或新購  
**聽眾：** 直屬主管、採購、finance、有時資安/法務  
**時長：** 25–40 min  
**Skills：** (b) · (a)  

---

## BLUF

> **Buy:** [vendor/product] for [use case], **\$Y** over [term], **recommend Option A**.  
> **Why now:** [license expiry / project gate / capacity].  
> **If no:** [schedule/risk/compliance impact].  
> **Decision by:** [date] (procurement lead time!).

---

## Slide outline

| # | 標題句 | 內容 |
|---|--------|------|
| 1 | **BLUF + 金額 + 時限** | 決策截止日期 |
| 2 | **Business / eng need** | 不用工具會卡哪個 milestone |
| 3 | **Requirements** | Must / should；合規、資安、在地支援 |
| 4 | **Options** | Vendor A/B/C 或 build vs buy vs do nothing |
| 5 | **TCO comparison** | 授權 + 維護 + 訓練 + 隱藏人力 |
| 6 | **Risk & vendor lock** | 退出成本、資料可攜、單一供應 |
| 7 | **Implementation plan** | 導入時程、owner、成功標準 |
| 8 | **Ask** | 簽核路徑、試用/POC 是否先做 |
| B | 報價單摘要、資安問卷、參考客戶 | |

### Options 表示例

| Option | Capex/Opex | Time-to-value | Risk | Fit |
|--------|------------|---------------|------|-----|
| A Vendor X 3yr | \$ | Fast | Med | **Rec** |
| B Vendor Y | \$ | Med | Low | |
| C Status quo | 0 cash | — | High schedule | |

---

## 竹科 / 半導體特別項

- License seat 與 tape-out / 專案峰值是否匹配  
- Export control / 國別限制（若適用）  
- 與既有 flow（synthesis/PD/DV）整合成本  
- 維護 window 是否擋 milestone  

外商 SaaS 另加：資料 residency、SSO、SLA 賠償。

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| 給「不買」後果 | 只貼 vendor 原文簡報 |
| 多方案比較 | 單一廠商情緒綁架 |
| 標 lead time | 決策日 = 要用的前一天 |

---

## Pattern provenance (public)

**Pattern:** Vendor TCO options + procurement lead time

| Source | URL |
|--------|-----|
| Industry EDA/tool buy case shape (must/should + lead time) | https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning |

Synthetic example deck uses NovaSemi/Aurora story; structure follows the sources above. Full map: [classic-public-cases.md](classic-public-cases.md).

## See also

- [(b)](../resource-advocacy/securing-resources-upward.md) · [(a)](../executive-communication/decision-ready-updates.md) · [04 效益](04-benefit-value.md)
