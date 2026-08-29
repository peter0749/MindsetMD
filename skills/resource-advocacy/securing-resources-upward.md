# Skill: Securing resources upward (headcount, budget, tools, air cover)

**Category:** Resource advocacy  
**Theme:** (b) Secure resources from leadership  
**Audience:** EMs, tech leads, staff ICs building a case for people, money, time, or priority  
**Canonical for:** headcount / budget / air-cover business cases  
**Depends on:** [(a) framing](../executive-communication/decision-ready-updates.md), [(d) + capacity model](../shared/capacity-model.md)  
**Influence playbook (full):** [(f) cross-team](../cross-team/conflict-and-coordination.md)

---

## Mindset shift

Resources are not awarded for busyness or pain alone. Leadership funds **outcomes** and **tradeoffs they can defend**. Frame every ask as an **investment with expected return** (or a risk the org is explicitly accepting if declined)—not “my team is tired.”

Your credibility is the compound interest of **precise, justified asks** over inflated wish lists.

**Framing of every ask** uses [(a) BLUF / SOR](../executive-communication/decision-ready-updates.md)—this skill is the *business case content*, not a second communication system.

---

## What “resources” means

| Type | Examples | Decision-maker lens |
|------|----------|---------------------|
| Headcount | eng, TPM, SRE, contractor | Capacity vs roadmap milestones; cost vs delay |
| Budget | cloud, vendors, tools, training | ROI, risk reduction, unit economics |
| Priority / air cover | freeze other work, exec sponsorship | What gets delayed; political cover |
| Time / focus | discovery, debt, platform | Opportunity cost vs feature promises |
| Access | data, stakeholders, decision rights | Speed of delivery; reduced thrash |

---

## Business case structure (use for any material ask)

### 1. Outcome, not role title

**Weak:** “I need two backend engineers.”  
**Strong:** “Two backend engineers let us finish payment platform migration ~3 months earlier, unlocking ~$500K/quarter revenue impact (or: unblocking partner launch SLA). Assumptions labeled.”

### 2. Connect role → roadmap → business goal

Work **backwards from the roadmap** (capacity rules: [../shared/capacity-model.md](../shared/capacity-model.md)):

1. What initiatives need capacity in next 12–18 months?  
2. Skills required? Current gap?  
3. Capacity after on-call, leave, support, debt, plus **headcount-context unplanned 20–30%** (context **B**—not the quarterly 10–15%)?  
4. Hiring lag: often **3–6 months** to productive engineer—plan early.

> If someone asks why not 10%: “10–15% is how we *allocate the quarter*; 20–30% is how we *size the team* so the quarter plan stays true.”

### 3. Present the “no” world (trade-offs)

Always show **what slips if the ask is denied**:

> If not approved: Project P moves to next half; Goal G is at risk; team sustainability / attrition risk rises (cite burnout signals carefully, with data).

This makes leadership choose between **options**, not yes/no on your comfort.

### 4. Alternatives (shows maturity)

- Hire senior vs junior (mix / mentorship capacity)  
- Contractor / vendor vs FTE  
- Descope / resequence roadmap  
- Automation / platform investment instead of bodies  
- Borrow capacity from adjacent team (with cost)

### 5. Precision over inflation

One well-justified hire beats a vague “need five.” Inflated asks train leadership to discount you.

---

## PR/FAQ and single-threaded owner (resource flavor)

A material new-product or dedicated-owner ask should survive the Internal FAQ list in [amazon-mapping](../shared/amazon-mapping.md) — especially: customer, cost of “no,” alternatives, input metric, and **who is full-time on this**.

**Single-threaded owner as a resource case** (not the RACI playbook — that is [(f)](../cross-team/conflict-and-coordination.md)):

> “This will not move as a side job. We need a named owner at ≥80% and a boundary: they do not also run [other]. If we cannot fund that, we should not pretend we launched a program.”

Use headcount context **B (20–30% unplanned)** for the HC math. Two-pizza history lives under STO in (f); do not open a separate “small team” skill here.

PR/FAQ is the **go/no-go pack** for the investment; the six-pager is for the decision *meeting* — see [(a)](../executive-communication/decision-ready-updates.md). Do not merge them.


## Phrase bank

**Opening the ask:**

> “This is a resource decision tied to [company OKR / launch]. Here’s the case in one page: outcome, cost of delay, options, recommendation.”

**Headcount:**

> “Adding [N] [role] closes [capability gap] so we can deliver [milestone] by [date]. Without it, we must cut [X] or accept [risk].”

**Budget / tool:**

> “Spend of $Y reduces [toil hours / incident MTTR / vendor risk] by Z%, payback in ~N months.”

**Air cover / priority:**

> “I need you to restate in the steering meeting that [initiative] outranks [other], so partner teams stop treating it as optional.”

**Not self-serving:**

> Frame as **org** benefit: “Customer onboarding needs 3 more eng to hit Q3—here is the business case,” not “My team needs more people.”

---

## One-page resource request template

```markdown
## Ask
- What: [role / $ / priority]
- By when: [decision date]
- Recommendation: [option]

## Business outcome
- Goal / OKR linked:
- Metric move expected:

## Why now
- Roadmap dependency:
- Hiring / procurement lag:

## Capacity math (short)  — use shared/capacity-model context B
- Current FTE / available weeks:
- Committed work:
- Buffer for unplanned (headcount math **20–30%**):
- Gap:

## Options
| Option | Deliverable | Cost | Risk |
|--------|-------------|------|------|
| A Approve full | … | … | … |
| B Partial | … | … | … |
| C No hire + descope | … | … | … |

## If declined
- What slips / risk accepted:

## Evidence
- Data / incidents / funnel / customer quotes (links)
```

---

## Headcount-specific tactics

1. **Plan proactively** — don’t wait until the team is already underwater (hiring lag makes pain last months).  
2. **Define the role as a capability gap** — “What will this person do that nobody can today? What changes when they’re productive?”  
3. **Hire for trajectory** — e.g. future squad lead before the split.  
4. **Freeze reality** — if freeze: reassess roadmap, descope, efficiency; communicate impact transparently; be ready when freeze lifts.

---

## Influence when you don’t own the budget

Short list only—full playbook is **[(f)](../cross-team/conflict-and-coordination.md)**:

- Map who is measured on the outcome you unlock; reframe so **their** metric moves.  
- Document: ask / their concern / workarounds / options — writing forces clarity and creates an escalation trail.  
- Pre-wire budget owners with 1:1s before the group meeting.  
- Offer a **pilot** (contractor, one quarter) to lower commitment risk.

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| Tie every role to a measurable outcome | Ask from pain alone (“we’re overwhelmed”) |
| Quantify delay / risk of “no” | Present only the happy path of “yes” |
| Account for hiring lag + unplanned work | Assume 100% utilization forever |
| Offer real alternatives | Ultimatums or vague “need more people” |
| Stay precise and evidence-based | Inflate headcount to negotiate down |

---

## Checklist before you submit a requisition / budget pack

- [ ] Outcome sentence works without internal jargon  
- [ ] Roadmap line items named that this resource unblocks  
- [ ] “If no” consequences explicit and fair  
- [ ] At least one alternative path  
- [ ] Timeline accounts for hire / vendor lag  
- [ ] Manager pre-wired; no public ambush  
- [ ] Numbers have a source (even rough + labeled assumption)  
- [ ] Unplanned % matches **context B (20–30%)**, not quarterly A alone  

---

## Success signals

- [ ] Asks come back with a decision (yes / no / later), not “unclear”  
- [ ] Leadership quotes *your* trade-off language in planning  
- [ ] You are not punished for precise “if no” scenarios (trust rising)  
- [ ] Freeze responses are descope plans, not silent heroics  

---

## See also

- **Capacity model (canonical %):** [../shared/capacity-model.md](../shared/capacity-model.md)  
- **How to phrase the ask:** [../executive-communication/decision-ready-updates.md](../executive-communication/decision-ready-updates.md)  
- **Roadmap that justifies the hire:** [../roadmap-planning/planning-sense-proactive-framing.md](../roadmap-planning/planning-sense-proactive-framing.md)  
- **No formal budget authority:** [../cross-team/conflict-and-coordination.md](../cross-team/conflict-and-coordination.md)  
- **Index:** [../README.md](../README.md)

---

## Sources

- *Headcount Planning: Get the Right People Early* — EM Tools: https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning  
- *Executive Communication* (advocate without seeming self-serving) — EM Tools: https://www.em-tools.io/engineering-manager-responsibilities/executive-communication  
- *Roadmap Planning* (capacity, trade-offs) — EM Tools: https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning  
- *How To Influence Without Authority As A TPM* — Mario Gerard: https://www.mariogerard.com/how-to-influence-without-authority-as-a-tpm/  
- Working Backwards PR/FAQ — https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- Single-threaded leadership (concept) — https://workingbackwards.com/concepts/
- Amazon mapping: [../shared/amazon-mapping.md](../shared/amazon-mapping.md)
