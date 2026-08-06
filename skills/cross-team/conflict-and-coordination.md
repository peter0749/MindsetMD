# Skill: Cross-department conflict coordination & resolution

**Category:** Cross-team  
**Theme:** (f) Coordinate and resolve inter-department conflict  
**Audience:** Tech leads, EMs, staff ICs, TPMs who depend on other teams without authority  
**Canonical for:** influence without authority, stakeholder mapping, RACI, healthy conflict, **cross-team escalation *fields*** (shared goal / each side’s metric / what we tried)  
**Not canonical for:** BLUF/SOR *sentence shape* — that is always [(a)](../executive-communication/decision-ready-updates.md)  
**Decision sentence shape:** [(a) SOR](../executive-communication/decision-ready-updates.md)  
**Action close-out:** [(c) meetings](../meetings/in-meeting-and-follow-through.md)

---

## Mindset shift

Most cross-team conflict is **not malice**. Different functions optimize different metrics (ship date vs brand vs reliability vs pipeline). Functional conflict is useful; chronic conflict is usually **missing shared purpose, late alignment, or unclear decision rights**.

You win by **influence without authority**: stakeholder maps, pre-wiring, trade-off frames, and written options—not by escalating first.

Resource asks that need budget owners still use **[(b)](../resource-advocacy/securing-resources-upward.md)** for the case and **this skill** for the multi-party politics.

---

## Diagnose before you “resolve”

Ask:

1. Is this **goal conflict** (different OKRs), **resource conflict** (same people/time), **process conflict** (handoffs), or **relationship debt**?  
2. Who is measured on what?  
3. Who can actually decide / block? (formal ≠ real influencer)  
4. Is the product/feature purpose clear to all parties?

**Working assumption (Product School):** nobody wakes up intending to sabotage; execution and context differ.

---

## Prevention system (cheaper than mediation)

### 1. Align early on strategy & roadmap

Walk partner leads through vision, roadmap, customer value, business value, KPIs **before** their planning locks. Invite feedback; surface dependencies.

### 2. Build a coalition

Allies on partner teams who trust you will carry context when you’re not in the room. Coffee chats / 1:1s are not fluff—they are infrastructure.

### 3. Storytelling over pure mandates

Bring partners on the journey; even when you reject a suggestion, **explain why**. Feeling unheard hardens conflict.

### 4. Clarify decision rights (lightweight RACI)

For each major cross-team initiative:

| Decision | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Scope freeze | … | … | … | … |
| Launch date | … | … | … | … |
| Tech approach | … | … | … | … |

Ambiguity is a conflict factory.

### 5. Shared definition of done & SLAs for handoffs

Document interfaces: what “ready for eng / ready for marketing / ready for support” means.

---

## Influence without authority (playbook)

Synthesized from TPM / PM / staff-eng practice:

1. **Clarify the business outcome** first (not the task).  
2. **Map stakeholders by risk** — who can slow/accelerate; who needs ownership feeling.  
3. **Lead with curiosity** — understand their constraints and scorecards.  
4. **Reframe so your ask advances *their* goals** when possible.  
5. **Write it down:** ask / their concern / options / tradeoffs → basis for alignment or escalation.  
6. **Pre-wire** decision meetings with 1:1s so the room is not a first hearing.  
7. **Consistent follow-through** — trust compounds.

**When they won’t prioritize you:**

> Understand their success metrics. If your program doesn’t help them win, it stays optional. Reframe, document tradeoffs, then escalate with a clean packet—not emotion.

---

## In-conflict meeting scripts

**Open with shared goal:**

> “We both need [customer / launch / reliability outcome]. Let’s map constraints, then pick a trade-off we can defend.”

**Separate positions from interests:**

> Position: “We can’t start until Q4.”  
> Interest: “We can’t risk peak-season stability.”  
> → Possible bridge: feature flag + limited cohort + extra on-call coverage.

**Make trade-offs explicit:**

> “Option A optimizes date; Option B optimizes risk; Option C splits scope. I recommend … because …”

**Timebox disagreement:**

> “Fifteen minutes to options; if we can’t align, we escalate to [decision owner] with this writeup.”

**Healthy conflict (keep it constructive):**

- Critique ideas/plans, not people  
- Invite dissent early (cheaper than silent failure)  
- Stay malleable; partners flag issues because they’re invested  

**Context split vs “never surprise the boss”:**  
Public peer/partner challenge (when pre-wired, idea-focused) is **healthy conflict**—this skill owns that.  
It does **not** license blindsiding **your manager** in steering or skip-level; that rule lives in [(a)](../executive-communication/decision-ready-updates.md) and [(c)](../meetings/in-meeting-and-follow-through.md). Pre-wire peers *and* pre-wire your boss when bad news will land in a room they attend.

---

## Escalation packet (when stuck)

Use only after good-faith bilateral attempt. Shape matches [(a) decision package](../executive-communication/decision-ready-updates.md); fields below are the cross-team fill-in.

```text
Escalation: [topic]
Shared goal:
Each side’s constraint / metric:
What we tried:
Options (A/B/C) with org-level tradeoffs:
Recommendation:
Decision needed from: [name] by: [date]
```

Escalate to **solve a trade-off**, not to “win.” After the decision: [(c) 2-hour writeback](../meetings/in-meeting-and-follow-through.md).

---

## Staff-eng coordination tools

- Stakeholder map / network (not only org chart)  
- ADRs / RFCs for technical disputes (context, options, rationale)  
- Regular async updates so partners aren’t surprised  
- MOI lens: Motivation, Organization, Ideas—align drive, navigate politics, plant clear proposals  

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| Align on purpose and KPIs early | Spring large asks after partners’ plans freeze |
| Map real influencers | Only talk to formal titles |
| Document options and tradeoffs | Escalate as first move |
| Pre-wire then meet | Use big meetings for first contact on hot issues |
| Assume positive intent; test with data | Personalize conflict |
| Close with owners and dates | “We’ll stay loosely aligned” forever |

---

## Checklists

### Before a cross-team kickoff

- [ ] Shared outcome sentence agreed  
- [ ] Decision rights sketched  
- [ ] Dependencies named with owners  
- [ ] Comms cadence set  
- [ ] “How we disagree” rule stated  

### When conflict appears

- [ ] Type diagnosed (goal/resource/process/relationship)  
- [ ] Each side’s metric understood  
- [ ] Options written  
- [ ] Pre-wires done  
- [ ] Escalation path known if timebox fails  

### After resolution

- [ ] Decision logged  
- [ ] Plans updated on both sides  
- [ ] Relationship repair if heat was high (1:1)  

---

## Success signals

- [ ] Partners bring you in *before* their plans freeze  
- [ ] Escalations are rare and come with a written packet both sides recognize  
- [ ] RACI is boring (good)—few “who decides?” loops  
- [ ] You are trusted as fair broker, not a faction captain  

---

## See also

- **SOR / escalation language:** [../executive-communication/decision-ready-updates.md](../executive-communication/decision-ready-updates.md)  
- **Meeting scripts + follow-through:** [../meetings/in-meeting-and-follow-through.md](../meetings/in-meeting-and-follow-through.md)  
- **Early roadmap alignment:** [../roadmap-planning/planning-sense-proactive-framing.md](../roadmap-planning/planning-sense-proactive-framing.md)  
- **Budget / headcount politics tip only:** [../resource-advocacy/securing-resources-upward.md](../resource-advocacy/securing-resources-upward.md)  
- **Index:** [../README.md](../README.md)

---

## Sources

- *8 Rules for Managing Conflict in Cross-Functional Teams* — Product School (Ronke Majekodunmi): https://productschool.com/blog/product-strategy/conflict-resolution-cross-functional-teams  
- *How To Influence Without Authority As A TPM* — Mario Gerard: https://www.mariogerard.com/how-to-influence-without-authority-as-a-tpm/  
- *The PM's Guide to Influence Without Authority* — QuestWorks: https://www.questworks.io/blog/product-manager-influence-without-authority.html  
- *The Staff Engineer Toolkit* (org awareness, influence, ADRs) — Hands-on Architects: https://handsonarchitects.com/blog/2025/staff-engineer-toolkit/  
