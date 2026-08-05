# Research notes: how tech MNC & IC-design decks are usually structured

**Purpose:** Ground the standard PPTX report templates (scenarios 01–09). Not a literature survey.  
**Sources:** Public QBR/roadmap practice writeups + semiconductor milestone language (tape-out / design review flows). Internal Google/MediaTek templates are **not** copied.

---

## 1. Tech MNC / product-engineering upward decks

### Shared spine (QBR, roadmap, exec update)

| Pattern | Practice |
|---------|----------|
| **Answer first (BLUF)** | Exec summary on slide 1–2: status RAG + 3 outcomes + 1 challenge + **the ask** |
| **Status → risks → decisions → priorities** | Main flow; activity dumps and shout-outs go to appendix |
| **Scorecard** | Commit / target / actual / RAG — not vanity activity metrics |
| **Length** | Executive internal: often **8–12** content slides; 10–20 only if departmental deep-dive |
| **Options + recommendation** | Material decisions: 2–3 options with trade-offs, clear rec, owner + date |
| **Visual density** | One idea per slide; large title (≥36pt culture); tables for options/scorecards |

Public QBR guides consistently push: executive summary → scorecard → initiatives → risks → asks; avoid chronological recaps in the main path.

### Roadmap decks

- Decision-first one-pager: themes, 3–7 milestones, **explicit not-doing**, trade-offs  
- Time windows (quarters / trains), not only Jira epic lists  
- Capacity honesty when eng owns the “when”

### Resource / headcount / procurement

- Outcome-linked ask (not “we are busy”)  
- Cost of “no” / slips  
- Alternatives (partial hire, descope, vendor B)  
- Lead time (hire lag / procurement cycle) on the decision date

---

## 2. Domestic IC design / semiconductor program decks

### Milestone language (what the room expects)

Common gates (names vary by company):

```text
Arch / Spec freeze → RTL freeze → DV exit / coverage gate
  → PD / timing / PPA check → Tape-out → First silicon / bring-up
  → Customer sample / design-win support
```

Reviews and status decks typically surface:

| Topic | How it shows up |
|-------|-----------------|
| **Schedule** | Gate date + slip risk + dependency (IP, foundry, package, tool license) |
| **PPA** | Power / Performance / Area vs target (or “at iso-perf”) |
| **Quality** | Coverage, open critical bugs, ECO storm risk |
| **Cross-team** | IP provider, PD, package, software, customer program name |
| **Money** | Spin cost as risk of delay (when relevant)—without fake precision |

Tape-out is treated as a **gated decision** (checks, reviews, sign-off), not a casual calendar event—decks that skip residual risk after “green” lose credibility.

### Cultural / room norms (Hsinchu-style, generalized)

- **Pre-wire** bad news before large forums  
- Public challenge OK on technical content; leave personal blame out  
- Dual audience: Chinese discussion + English titles/BLUF for HQ or mixed rooms  
- Backup annex for deep tech; main path stays decision-oriented  

---

## 3. Mapping to our templates (01–09)

| ID | Scenario | Norm applied |
|----|----------|--------------|
| 01 | Technical review | Options table + rec + residual risk; IC: gate criteria |
| 02 | Results / demo | Goal recall → metric Δ → residual risk (not activity list) |
| 03 | Management effectiveness | Delivery + people + capacity pie; asks to manager |
| 04 | Benefit / ROI | Impact chain + counterfactual + continue/stop options |
| 05 | Procurement | TCO options, lead time, if-no impact |
| 06 | Resource / HC | Business outcome, capacity **B**, if-declined slips |
| 07 | Roadmap | Themes, capacity **A**, not-doing, intake rule |
| 08 | Period start | Commit vs stretch vs out; endorse plan |
| 09 | Period end / QBR | Exec summary → scorecard → miss root cause → next ask |

**Explicitly out of scope:** personal annual self-review templates.

---

## 4. Design system used in shipped PPTX assets

- Palette **Midnight Executive**: primary `1E2761`, light panels `F4F7FC`, accent highlight `2B6CB0`, text `1A202C`, muted `718096`, white text on navy.  
- Fonts: titles **Calibri** bold large; body **Calibri** ≥18pt.  
- Placeholders: Team X, Program Alpha, Qn, $ amounts labeled **example only**.  
- Every deck: Cover → BLUF → body → Decision/Ask → (optional) Backup cue.

---

## 5. References (public)

- QBR structure: status–risks–decisions–priorities; exec summary + scorecard (industry QBR guides, e.g. Slideworks / Deckary-style leadership QBR patterns).  
- Roadmap: decision-first executive view with themes and trade-offs.  
- IC: tape-out / design-review milestone sequences (public semiconductor process explainers; design-flow milestone lists).  

In-repo outline sources: `skills/presentations/01`–`09` markdown + `00-style-mnc-and-hsinchu.md`.
