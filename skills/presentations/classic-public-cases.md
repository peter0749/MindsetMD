# Classic public cases for tech/IC report decks

**Principle:** When a **public, well-documented** tech/IC case fits a scenario, prefer its **structure, vocabulary, and decision shape** over pure invention.  
**Hard limit:** We do **not** copy confidential internal Google / MediaTek / Qualcomm decks or invent fake “official” company numbers. Examples remain **synthetic** (e.g. NovaSemi/Aurora) but **anchored** to public patterns below.

---

## Soft tech / internet / platform

| Scenario | Classic public case / artifact | What to steal (structure only) | Primary URL |
|----------|--------------------------------|--------------------------------|-------------|
| Results / impact readout | Google SRE **Shakespeare Search** example postmortem (SRE Book App. D) | Summary → impact → root causes → action items with owners | https://sre.google/sre-book/example-postmortem/ |
| Incident / risk storytelling | Google **postmortem culture** case study (rack decommission / colo) | Blameless systems root cause; widest useful audience | https://sre.google/workbook/postmortem-culture/ |
| External incident comms | **GitLab** 2017 Postgres deletion postmortem | Timeline honesty; backup failure; recovery narrative | https://about.gitlab.com/2017/02/10/postmortem-of-database-outage-of-january-31/ |
| Org / culture / talent density | **Netflix Culture Deck** (public slides / jobs culture memo) | High-talent density; keeper test; freedom & responsibility framing for people slides | https://jobs.netflix.com/culture · classic deck discussion e.g. https://www.slideshare.net/reed2001/culture-1798664 |
| Eng strategy / roadmap | Will Larson / StaffEng **engineering strategy** writing | Design-doc distillation; vision vs specs | https://staffeng.com/guides/engineering-strategy/ |
| QBR / exec update | Industry leadership QBR pattern (status → scorecard → risks → asks) | Answer-first; commit vs actual; not activity dump | See [research-deck-norms.md](research-deck-norms.md) |

---

## IC design / semiconductor (public only)

| Scenario | Classic public signal | What to steal | Primary URL |
|----------|----------------------|---------------|-------------|
| Tape-out / node milestone | **MediaTek + TSMC 2nm** public tape-out / process milestone announcements | Milestone language: tape-out → volume production window; foundry partnership | e.g. https://www.mediatek.com/press-room/mediatek-develops-chip-utilizing-tsmcs-2nm-process-achieving-milestones-in-performance-andpower-efficiency · Reuters/Computex coverage of tape-out timing |
| Process / node roadmap | Public foundry **N3/N2** customer readiness narratives | Gate naming: design tape-out, risk production, volume | Industry press (TSMC tech symposium summaries — use only public claims) |
| Design-win / customer sample | Public OEM design-win press (MediaTek / Qualcomm style) | Sample → design-win → ramp framing without fake unit economics | Company press rooms |

**Note:** Earnings slides and tech-day PDFs from TSMC/MediaTek/Qualcomm are useful for **slide density and milestone vocabulary**, not for inventing internal HC or PPA tables.

---

## Mapping to our nine scenarios (current example pack)

| ID | Our synthetic example | Prefer public pattern |
|----|----------------------|------------------------|
| 01 Technical review | Aurora AON clock options | Google-style design doc / options table + explicit residual risk |
| 02 Results / demo | First silicon day-3 boot | Public bring-up / GA readout shape; silicon milestone press vocabulary |
| 03 Management effectiveness | Atlas org health | Eng-manager capacity + Netflix-style talent density *language* (not Netflix confidential data) |
| 04 Benefit / ROI | Shared DV farm | Platform/CI investment payback narratives (public eng blogs) |
| 05 Procurement | HelixSim licenses | Industry EDA/tool TCO + lead-time discipline |
| 06 Resource / HC | +1 senior DV | Roadmap-backed headcount business case (public EM blogs) |
| 07 Roadmap | H2 themes | Outcome themes + not-doing (StaffEng / product roadmap practice) |
| 08 Period start | Q3 commit | Commit / stretch / out (planning kickoff norm) |
| 09 Period end QBR | Q2 scorecard | Leadership QBR + scorecard Hit/Partial/Miss |

The **Aurora arc** stays one coherent multi-deck story for learning continuity. Each deck’s **decision shape** follows the public pattern above.

---

## How to use a classic case when building a real deck

1. Open the public source; extract **section order** and **decision verbs**, not proprietary metrics.  
2. Replace with **your** program numbers and dates.  
3. Keep BLUF → evidence → options → ask.  
4. Cite the public inspiration in speaker notes if useful (“structure inspired by SRE Book example postmortem”).  
5. Never present synthetic numbers as real company results.

---

## Regenerating examples after case re-anchoring

```bash
python3 scripts/generate_report_pptx_templates.py
python3 scripts/test_pptx_assets.py
```

Content: `scripts/pptx_deck_data.py` · Timeline anchors: `AURORA_TIMELINE` in the same file.
