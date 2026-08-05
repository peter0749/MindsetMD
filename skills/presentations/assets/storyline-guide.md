# Aurora multi-deck storyline guide

**Universe:** NovaSemi · **Project Aurora** (5nm connectivity SoC) · **Atlas Platform** team  
**Presenter (examples):** Alex Chen (EM) → **Decision-maker:** Morgan Lee (VP Eng) unless noted  

Cold rule for humans/agents: open each **example** deck → slide **Situation & decision card** → then BLUF. You should be able to decide without inventing facts.

Full chronology anchors: `AURORA_TIMELINE` in `scripts/pptx_deck_data.py`.

---

## Plot in one page

```text
01 Tech review (3/20)  AON clock: pick Option B (phased) so freeze 4/10 holds
        ↓ freeze held 4/10 → tape-out 4/28 → silicon 5/12
02 Results (5/16)      Day-3 boot green → approve sample plan for 6/30
        ↓
03 Org health (5/18)   Delivery green, people yellow (Priya single-thread) → endorse hire path
06 HC request (5/20)   Formal +1 senior DV; if no → USB3/sample slips explicit
        ↓
04 Farm ROI (5/25)     Lagging proof: freeze+boot already happened → expand +20 seats by 5/30
05 Procurement (6/05)  HelixSim renew+expand seats to match farm (lead time!)
        ↓
07 H2 roadmap (6/12)   Sample > WiFi priority rule; revB AON residual from 01
09 Q2 QBR (6/26)       Scorecard GREEN with USB3 partial + unplanned 20%; ask Q3 B + HC
08 Q3 kickoff (7/01)   Commit sample SLA + revB; WiFi stretch; out sensor hub
```

---

## Per scenario — what happened / what to decide

| # | What happened (one line) | What to decide | REC | Decide by |
|---|--------------------------|----------------|-----|-----------|
| **01** | AON clock architecture still open before freeze 4/10; dual mux costs +3 eng-wk | A full dual / **B phased strap** / C keep dual unfinished | **B** | 2026-03-20 |
| **02** | A0 silicon 5/12; Linux day-3 boot (beat day-5); USB3 yellow non-blocking | Approve Tier-1 sample plan for 6/30 ship? | **Yes** | 2026-05-22 |
| **03** | Delivery green but HS IO DV single-threaded; unplanned ~20% | Endorse +1 DV path + sample air cover? | **Yes** | 2026-05-18 |
| **04** | DV farm cut regress 18h→6h; helped pre-si catch; H2 load rising | Continue / **Expand +20 seats** / shrink | **Expand** | 2026-05-30 |
| **05** | HelixSim ends 7/31; farm expand needs seats; 45-day vendor lead | HelixSim 3yr+20 / switch / short extend | **HelixSim+20** | 2026-06-05 |
| **06** | Same people gap as 03; sample surge + USB3 + WiFi collide | +1 senior DV / contractor / descope USB3 | **+1 FTE** | 2026-05-20 |
| **07** | H1 done; H2 must not dual-commit sample vs WiFi | Endorse map; **sample > WiFi** on conflict? | **Endorse** | 2026-06-12 |
| **08** | Q3 start; samples shipping; need commit vs stretch clarity | Period plan A aggressive / **B balanced** / C sample-only | **B** | 2026-07-01 |
| **09** | Q2 lookback: freeze+boot green; USB3 partial; people yellow carried | Endorse P1/P2 + HC + Q3 plan B? | **Yes** | ~2026-06-26 |

---

## Decision package checklist (every example)

Each example’s **Situation card + BLUF + Options + Ask** should answer:

1. Who presents / who decides?  
2. What is at risk (business or silicon/schedule)?  
3. What are the mutually exclusive options (or explicit FYI)?  
4. What is REC and what changes on yes vs no?  
5. Deadline?  
6. How this links to prior/next deck in the arc?

---

## Files

| Pack | Path |
|------|------|
| Templates | [pptx/templates/](pptx/templates/) |
| Examples | [pptx/examples/](pptx/examples/) |
| Situation data | `scripts/pptx_deck_data.py` → `EXAMPLE_SITUATIONS` |
| Patterns | [../classic-public-cases.md](../classic-public-cases.md) |
