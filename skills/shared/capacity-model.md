# Canonical capacity model

**Status:** Single source of truth for % buffers used across this corpus.  
**Owning skill:** [roadmap-planning/planning-sense-proactive-framing.md](../roadmap-planning/planning-sense-proactive-framing.md)  
**Also used by:** [resource-advocacy](../resource-advocacy/securing-resources-upward.md), [department-value](../department-value/presenting-department-value.md), [presentations/](../presentations/README.md) (07/08 → **A**; 06 → **B**; 03 reports **A**, HC ask → **B**)

Do **not** invent competing % ranges in other skills or decks—link here or quote this table with **context A or B labeled**.

---

## Two planning contexts (do not mix)

| Context | Horizon | Question | Unplanned buffer | Tech investment / debt |
|---------|---------|----------|------------------|------------------------|
| **A. Quarterly roadmap allocation** | ~1 quarter, execution | How do we split *available* eng weeks this quarter? | **10–15%** (min **10%**; if ops-heavy, push toward **15–20%**) | **15–20%** first-class |
| **B. Headcount / annual capacity math** | 12–18 months, staffing | How many people do we need so the roadmap is still real? | **20–30%** (attrition, spikes, unknown work, ramp) | Include debt themes in demand; don’t staff to 100% feature load |

### Why two numbers?

- **Quarterly (A)** is about *committing* work with a visible buffer so you don’t promise 100% features.  
- **Headcount (B)** is about *hiring enough* that after leave, on-call, learning, incidents, and surprises, you can still deliver the plan. Staffing with only a 10% buffer under-hires.

### Default quarterly split (healthy team)

| Bucket | Share of available capacity | Notes |
|--------|----------------------------|--------|
| Planned product / roadmap outcomes | **60–70%** | Named commitments |
| Tech investment / platform / debt | **15–20%** | First-class, not “if time left” |
| Unplanned / ops / interrupt | **10–15%** | Incidents, urgent asks; ops-heavy teams → **15–20%** |
| **Sum** | **~100%** | Never plan features at 100% |

### Headcount demand sketch

```
Required capacity ≈ roadmap demand
                   + debt/platform demand
                   + unplanned 20–30%
                   + hiring/ramp lag (often 3–6 months to productive)
```

If leadership freezes headcount: **descope roadmap** (context A), don’t pretend buffer math changed.

---

## Phrase when challenged on the %

> “We use ~10–15% unplanned in the *quarter plan* so commits are honest, and 20–30% in *headcount math* so we don’t staff for a fantasy of zero firefighting. Same model, two decisions.”

---

## See also

- Full planning playbook: [../roadmap-planning/planning-sense-proactive-framing.md](../roadmap-planning/planning-sense-proactive-framing.md)  
- Resource asks: [../resource-advocacy/securing-resources-upward.md](../resource-advocacy/securing-resources-upward.md)  
