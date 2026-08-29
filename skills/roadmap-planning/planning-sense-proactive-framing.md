# Skill: Roadmap & planning sense (“we already know / already planned”)

**Category:** Roadmap planning  
**Theme:** (d) Give boss and peers planning confidence—not pure reactivity to assigned actions  
**Audience:** Tech leads, EMs, staff ICs who get “helicoptered” tasks and want to reframe as planned work  
**Canonical for:** capacity allocation, intake rule, displace-not-add, “already on the plan” framing, **對上說不 (plan / artifact version)**  
**Not canonical for:** live meeting scripts — those are [(c)](../meetings/in-meeting-and-follow-through.md)  
**Shared model:** [../shared/capacity-model.md](../shared/capacity-model.md)

---

## Mindset shift

Bosses and teammates feel safe when they believe **you see around corners**.  
Reactive mode: “Tell me what to do.”  
Planning mode: “Here’s the map, capacity, risks, and where your ask already sits—or what it displaces.”

A roadmap is a **promise with incomplete information**. Credibility comes from capacity honesty, explicit trade-offs, and updating early—not from false certainty.

---

## What “planning sense” looks like upward

| Reactive signal | Planning signal |
|-----------------|-----------------|
| Wait for tickets from boss | Publish a rolling plan they can inspect |
| “We’ll see” on every ask | “On the roadmap under theme T; slot is W3—or swap with X” |
| Only escalate when late | Flag risks when assumptions break |
| Activity reports | Outcome + capacity + next decision |
| Hidden buffer | Explicit buffer (see capacity model: quarterly **10–15%** unplanned) |

**Core reframe phrase:**

> “We’re not starting from zero—this is already on our plan under [theme]. Here’s status, dependencies, and what would need to move if we accelerate.”

If it’s *not* on the plan:

> “It’s not on the current roadmap. We can take it by displacing [item] or by adding capacity. Which priority wins?”

---

## Build a credible plan (EM / TL view)

### 1. Start with capacity, not wishlists

Use the **canonical model** ([../shared/capacity-model.md](../shared/capacity-model.md)):

| Context | Unplanned | Tech investment | Planned outcomes |
|---------|-----------|-----------------|------------------|
| **Quarterly roadmap (A)** | **10–15%** (ops-heavy → up to **15–20%**) | **15–20%** | **60–70%** |
| **Headcount math (B)** | **20–30%** in demand | In roadmap demand | Don’t staff at 100% feature load |

- Available eng time after: on-call, leave, support, meetings  
- Never allocate 100% of capacity to features  
- Headcount / resource asks: link to (b); **do not** invent a third % table

### 2. Sequence deliberately

- Dependencies first  
- High-risk work **early** in the quarter (time to recover)  
- Skill bottlenecks explicit  

### 3. Horizons

- **Detailed:** ~rolling 3 months  
- **Directional:** 6–12 months themes (not fake feature lists)  

### 4. Document assumptions & risks

When reality breaks the plan, you explain *which assumption failed*—not “we failed.”

### 5. Joint ownership

Product owns more of **what/why**; engineering owns **how/when** feasibility. Neither unilaterally dictates a trustworthy roadmap.

---

## Working backwards vs skills-forward

**Skills-forward:** start from what the team already knows how to build, then look for a customer.  
**Working backwards:** start from a specific customer experience, then discover what must be built (and what you will **not** build).

For a **new product or new theme**, write a short **PR/FAQ** *before* the roadmap line exists:

1. Future press release (&lt;1 page, customer language, as if it already shipped).  
2. Internal FAQ that survives the [must-answer list](../shared/amazon-mapping.md).  
3. Then sequence it on the plan with capacity **A**, or send the resource case to [(b)](../resource-advocacy/securing-resources-upward.md).

This is a go/no-go thinking tool — **not** a slide factory and **not** the six-pager used in decision meetings (that lives in [(a)](../executive-communication/decision-ready-updates.md) + [(c)](../meetings/in-meeting-and-follow-through.md)).

**Operating cadence (OP1/OP2-style):** once or twice a year, teams propose initiatives against **input-metric** goals; leadership approves/denies and allocates people/money. That is this skill’s planning loop. Weekly metric *meetings* are [(c)](../meetings/in-meeting-and-follow-through.md); metric *definitions* are [(e)](../department-value/presenting-department-value.md). Author-site cadence: https://workingbackwards.com/concepts/

**Phrase:**
> “We’re working backwards from [customer outcome], not from the stack we already have. PR draft in the FAQ pack; if we fund it, it displaces [X] on the quarter plan.”


## Writing that creates planning presence

From staff-eng practice: **writing is thinking**. Use short docs with:

- TL;DR  
- Audience / approvers  
- Context  
- Problem  
- Options  
- Decision + consequences  

Strategy emerges from repeated design docs / RFCs—not one grand PDF nobody reads.

**Engineering strategy components (Larson-style readability):** explore → diagnose → refine (map & model) → policy → operation—keep documents decision-oriented.

---

## Phrases that create “already planned” calm

**When leadership dumps a task:**

> “Got it. Mapping to our Q plan: closest bucket is [theme]. If we pull it into this sprint, we pause [X]. Confirm?”

**When asked “do we have a plan?”:**

> “Yes—one-pager: goals, sequenced milestones, capacity, risks, open decisions. I’ll send in 10 minutes / link here.”

**When scope creeps:**

> “We can add this. Explicit trade-off: [deliverable] moves out. I’ll update the roadmap and notify stakeholders today.”

**When you need discovery before dates:**

> “I won’t commit a date before a short discovery on scope and risks. Proposal: 3–5 days spike, then date with confidence band.”

**When plan changes:**

> “Assumption A broke ([evidence]). Options: … Recommend … Updated roadmap: …”

---

## Operating system: stay proactive week to week

1. **Maintain a living roadmap artifact** (doc/board) boss can open anytime.  
2. **Weekly upward note:** progress / risks / decisions — framing from [(a) decision-ready](../executive-communication/decision-ready-updates.md).  
3. **Pre-wire** next month’s hard choices before they become fires.  
4. **Carry a “decision log”** — past calls + why (reduces re-litigation).  
5. **Staff toolkit habits:** milestones with explicit risks/deps; async dashboards; iterate plan often.

---

## Pushback without looking obstructive (“對上說不” — plan version)

Goal: protect the plan **and** look like a partner, not a blocker.

| Move | Phrase |
|------|--------|
| Affirm intent | “We want the same outcome: [goal].” |
| Show the map | “Current commit is [A, B]. This ask maps to [theme / not on plan].” |
| Force trade-off | “To take it this quarter we displace [X] or slip [Y]. Your call on priority.” |
| Offer a controlled yes | “We can spike 2–3 days, then re-estimate—without a silent full commit.” |
| Document | “I’ll write the decision: keep A / swap to new / accept delay.” |

**Weak no:** “We can’t, team is busy.”  
**Strong no:** “We can if [X] moves out; otherwise we accept not doing this until [slot].”

Room scripts and post-meeting writeback: [(c) meetings](../meetings/in-meeting-and-follow-through.md).

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| Show themes + capacity + trade-offs | Promise dates before scope is known |
| Make every add a displace | Pretend capacity is infinite |
| Update early when assumptions fail | Hide yellow until it’s red |
| Present outcomes, not only tickets | Roadmap = dump of Jira epics with no “why” |
| Keep tech investment as first-class | “Debt in the margins if time left” |

---

## Checklists

### Roadmap review with your manager (30 min)

- [ ] Top outcomes this quarter (3–5)  
- [ ] Capacity math visible  
- [ ] Explicit “not doing” list  
- [ ] Risks / deps / open decisions  
- [ ] How new requests enter (intake rule)  

### Intake rule (post on team wiki)

```
New work enters only if:
1) Named priority owner, and
2) Displaces something of equal/less priority, or
3) New capacity is funded.
Silent “just this one small thing” is not a process.
```

### “Planning sense” self-audit

- [ ] Can I point to a doc that answers “what’s next and why”?  
- [ ] Would my boss say we drive vs wait?  
- [ ] Do partners know how to request work without side-channels only?

---

## Mini one-pager skeleton (send upward anytime)

```markdown
# Plan: [Team] — [Quarter]
## Outcomes we own
## Now / Next / Later (themes)
## Capacity assumptions  (link: shared/capacity-model — quarterly A)
## Explicit not-doing
## Risks & deps
## Decisions needed from you
```

---

## Success signals

- [ ] Boss stops assigning random work without asking “what slips?”  
- [ ] You can open one doc that answers “what’s next and why” in &lt;2 minutes  
- [ ] New requests hit intake (displace / fund) more often than side-channel panic  
- [ ] Yellow risks appear before red surprises  

---

## See also

- **Capacity numbers (canonical):** [../shared/capacity-model.md](../shared/capacity-model.md)  
- **Decision language:** [../executive-communication/decision-ready-updates.md](../executive-communication/decision-ready-updates.md)  
- **Meeting pushback + follow-through:** [../meetings/in-meeting-and-follow-through.md](../meetings/in-meeting-and-follow-through.md)  
- **Headcount / budget from the plan:** [../resource-advocacy/securing-resources-upward.md](../resource-advocacy/securing-resources-upward.md)  
- **Index / reading order:** [../README.md](../README.md)

---

## Sources

- *Roadmap Planning: Turn Business Goals into Deliverable Plans* — EM Tools: https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning  
- *Communication Skills for Software Engineers* (decision-first, options, cost of inaction) — Utterskills: https://utterskills.com/blog/communication-skills-for-software-engineers  
- *Writing engineering strategy* — StaffEng / Will Larson: https://staffeng.com/guides/engineering-strategy/  
- *The Staff Engineer Toolkit* (writing, milestones, org awareness) — Hands-on Architects: https://handsonarchitects.com/blog/2025/staff-engineer-toolkit/  
- Working Backwards PR/FAQ — https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- Amazon operating cadence / concepts — https://workingbackwards.com/concepts/
- Amazon mapping: [../shared/amazon-mapping.md](../shared/amazon-mapping.md)
