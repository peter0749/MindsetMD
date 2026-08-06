# Presentation PPTX assets

## Agent / reader notice — **內容模板**，不是預設美工排版

| 這是 | 這不是 |
|------|--------|
| **內容模板 (content template)**：章節順序、BLUF、決策包、話術風格、故事線 | **預設美工排版 (visual design system)**：不可改的母片、品牌色、字級、間距 |
| 要學／要輸出的：**報告內容怎麼寫、怎麼決策** | 不要照抄：顏色、版心、字體、裝飾框、精確座標 |
| PPTX 僅作 **可打開的示範載體** | 不是公司官方 slide master 或 design library |

**一句話：** 檔名雖有 template/example，語意是 **content template / content example**，**不是**美工範本。

**給 AI Agent 的規則：**

1. 優先複製 **內容風格**：誰講、誰拍板、stakes、options、REC、deadline、arc。  
2. **不要**把 navy 色塊、card 高度、footer 座標、officecli 版面當成必須還原的規格。  
3. 產出真實簡報時：套用使用者／公司的母片與品牌；只保留本 skill 的 **敘事與決策結構**。  
4. Markdown outline（`01`–`09`）與 [storyline-guide.md](storyline-guide.md) 比 PPTX 美編更「權威」於內容。  
5. 成功標準 = 決策可讀、結構完整；**不是** pixel-match sample 檔。

---

Two packs per scenario (01–09):

| Pack | Path | Purpose |
|------|------|---------|
| **Content template** | [`pptx/templates/`](pptx/templates/) | Placeholder **sections & phrases** — fill with real program data |
| **Content example** | [`pptx/examples/`](pptx/examples/) | Filled **Aurora / NovaSemi / Atlas** storyline (decision-readable) |

**Out of scope:** personal performance / annual self-review.

**Pattern provenance:** each deck’s cover + “Pattern provenance” slide name the public tech/IC pattern; full table in [../classic-public-cases.md](../classic-public-cases.md).

**Storyline (examples):** [storyline-guide.md](storyline-guide.md) — multi-deck plot + per-scenario “what to decide.” Each example PPTX also has a **Situation & decision card** slide (presenter, decision-maker, stakes, yes/no).

## Shared example universe

| Field | Value |
|-------|--------|
| Company | NovaSemi (fictional IC design) |
| Program | **Project Aurora** — 5nm connectivity SoC |
| Team | **Atlas Platform** (DV, integration, bring-up) |
| Lead | Alex Chen (EM) → VP Eng Morgan Lee |

### Master chronology (tests enforce)

| Date | Event |
|------|--------|
| 2026-03-20 | 01: AON Option B decided (freeze target 4/10) |
| 2026-04-10 | RTL freeze held |
| 2026-04-28 | Tape-out |
| 2026-05-12 | First silicon |
| 2026-05-15 | Day-3 boot |
| 2026-05-16 | 02: results readout; sample ask by 5/22; ship 6/30 |
| 2026-05-18–20 | 03 org health + 06 +1 DV |
| 2026-05-25 | 04 farm ROI (lagging: freeze 4/10, boot 5/15); ask-by 5/30 |
| 2026-06-05 | 05 HelixSim decide-by |
| 2026-06-12 | 07 H2 roadmap |
| 2026-06-26 | 09 Q2 QBR |
| 2026-07-01 | 08 Q3 kickoff |

Stories cross-link; **lagging KPIs always pre-date the deck’s ask deadline**.

### Scenario → public pattern (explicit)

| # | Scenario | Pattern (public) | Key sources |
|---|----------|------------------|-------------|
| 01 | Technical review | Design-doc / RFC options + residual risk | [StaffEng strategy](https://staffeng.com/guides/engineering-strategy/) · [Utterskills options framing](https://utterskills.com/blog/communication-skills-for-software-engineers) |
| 02 | Results / demo | Launch / bring-up readout (impact first) | Public silicon/GA style + [MediaTek 2nm TO press](https://www.mediatek.com/press-room/mediatek-develops-chip-utilizing-tsmcs-2nm-process-achieving-milestones-in-performance-andpower-efficiency) for IC milestone language |
| 03 | Management effectiveness | Team health + capacity scorecard | [Managing upwards](https://www.theengineeringmanager.com/management-101/managing-upwards/) · [Netflix culture (public)](https://jobs.netflix.com/culture) (talent-density language only) |
| 04 | Benefit / ROI | Platform investment impact chain | Eng platform/CI farm ROI narrative pattern |
| 05 | Procurement | TCO options + lead time | Industry EDA/tool buy case shape |
| 06 | Resource / HC | Roadmap-backed headcount case | [EM Tools headcount](https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning) |
| 07 | Roadmap | Themes + not-doing + intake | [EM Tools roadmap](https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning) · StaffEng |
| 08 | Period start | Commit / stretch / out | Planning kickoff norm |
| 09 | Period end / QBR | Scorecard Hit/Partial/Miss → asks | Leadership QBR pattern; [SRE postmortem structure](https://sre.google/sre-book/example-postmortem/) for impact honesty |

Full case list: [../classic-public-cases.md](../classic-public-cases.md) · norms: [../research-deck-norms.md](../research-deck-norms.md).

## Index

| # | Scenario | Template | Example |
|---|----------|----------|---------|
| 01 | Technical review | [pptx/templates/01-technical-review.pptx](pptx/templates/01-technical-review.pptx) | [pptx/examples/01-technical-review.pptx](pptx/examples/01-technical-review.pptx) |
| 02 | Results / demo | [pptx/templates/02-results-demo.pptx](pptx/templates/02-results-demo.pptx) | [pptx/examples/02-results-demo.pptx](pptx/examples/02-results-demo.pptx) |
| 03 | Management effectiveness | [pptx/templates/03-management-effectiveness.pptx](pptx/templates/03-management-effectiveness.pptx) | [pptx/examples/03-management-effectiveness.pptx](pptx/examples/03-management-effectiveness.pptx) |
| 04 | Benefit / ROI | [pptx/templates/04-benefit-value.pptx](pptx/templates/04-benefit-value.pptx) | [pptx/examples/04-benefit-value.pptx](pptx/examples/04-benefit-value.pptx) |
| 05 | Procurement | [pptx/templates/05-procurement-proposal.pptx](pptx/templates/05-procurement-proposal.pptx) | [pptx/examples/05-procurement-proposal.pptx](pptx/examples/05-procurement-proposal.pptx) |
| 06 | Resource / HC | [pptx/templates/06-resource-request.pptx](pptx/templates/06-resource-request.pptx) | [pptx/examples/06-resource-request.pptx](pptx/examples/06-resource-request.pptx) |
| 07 | Roadmap | [pptx/templates/07-roadmap.pptx](pptx/templates/07-roadmap.pptx) | [pptx/examples/07-roadmap.pptx](pptx/examples/07-roadmap.pptx) |
| 08 | Period start | [pptx/templates/08-period-start-planning.pptx](pptx/templates/08-period-start-planning.pptx) | [pptx/examples/08-period-start-planning.pptx](pptx/examples/08-period-start-planning.pptx) |
| 09 | Period end / QBR | [pptx/templates/09-period-end-review.pptx](pptx/templates/09-period-end-review.pptx) | [pptx/examples/09-period-end-review.pptx](pptx/examples/09-period-end-review.pptx) |

## Content spine (what to keep) vs layout (what to ignore)

**Keep (content template):**

```text
Cover (context)
→ Pattern provenance (optional for real decks)
→ Situation & decision card (examples; real decks: who/stakes/decision)
→ BLUF / status / recommendation
→ Body evidence
→ Options + REC (if a choice is required)
→ Decision & ask (owner + date)
```

**Ignore when producing for a real company (layout chrome):**

- Midnight navy palette, card fills, exact cm margins, footer styling  
- officecli shape stacking quirks  
- Decorative “TEMPLATE / EXAMPLE” badges  

Generator layout notes below are **only** for regenerating these sample PPTX files.

### Sample-file layout rules (generator only)

- No default title placeholder on content/BLUF slides (prevents kicker collision).
- Cover → **Pattern provenance** → (examples: Situation card) → BLUF → body → options → ask.
- Margins ≥ 1.4cm; navy status bar; options tables with navy header.
- Real newlines only (never literal `\n` in text).

## Regenerate

```bash
python3 scripts/generate_report_pptx_templates.py
python3 scripts/test_pptx_assets.py
python3 scripts/check_markdown_links.py
```

Content data: `scripts/pptx_deck_data.py` · Generator: `scripts/generate_report_pptx_templates.py`
