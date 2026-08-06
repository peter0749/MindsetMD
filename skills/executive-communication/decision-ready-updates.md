# Skill: Decision-ready updates (goals → difficulties → solutions → benefits)

**Category:** Executive communication / managing up  
**Theme:** (a) Present goals, difficulties, solutions, benefits; support manager decisions  
**Audience:** Engineers, tech leads, EMs writing status, escalations, or 1:1 updates  
**Canonical for:** BLUF, pyramid, SOR / decision package, GDSB, escalation sentence shape

---

## Mindset shift

Being technically correct is not enough. Decision-makers choose among **tradeoffs** (risk, time, cost, opportunity). Your job is to make technical reality **usable at decision time**—not to walk them through your research journey.

Leaders form an opinion fast; bury the ask and you lose the room.

Other skills **reuse this language**—they should not invent a second escalation template.

---

## Core frameworks

### 1. BLUF — Bottom Line Up Front

Structure every executive-facing message as:

1. **Bottom line** — key message or recommendation  
2. **So what** — why it matters to *their* priorities  
3. **The ask** — decision, resource, or explicit risk acceptance  
4. **Evidence** — only what is needed to decide  

**Weak email:** long timeline story → capacity issues → meetings with Tom → …  
**Strong email:**

> Q3 launch delayed 2 weeks (Aug 15 → Aug 29) due to eng capacity.  
> Impact: miss back-to-school window by ~3 days.  
> Options: (A) pull 2 eng from maintenance, or (B) cut mobile feature to hold Aug 15.  
> **I recommend A. Need decision by Thursday.**

### 2. Pyramid principle

Recommendation first → supporting evidence → context only if asked.  
Do **not** communicate bottom-up (context → analysis → finding → recommendation) to execs.

### 3. Status → Options → Recommendation (SOR / decision package)

Use when something is blocked or you need a call:

| Block | Content |
|-------|---------|
| **Status / Goal** | What we committed to; current state in one line |
| **Difficulty** | Constraint, risk, or gap (mechanism **and** business impact) |
| **Options** | 2–3 paths with tradeoffs (not one demand) |
| **Recommendation** | Clear pick + why |
| **Ask** | Decision by date; what you need from them |

**Phrase template:**

> **Situation:** We are on track for X, except Y.  
> **Impact if we do nothing:** …  
> **Options:**  
> - A — Fast / higher risk — …  
> - B — Slower / safer — …  
> - C — Partial mitigation — …  
> **Recommendation:** B because …  
> **Need your decision by [date].**

### 4. Five engineer communication moves

1. **Decision-first framing** — name the decision before the architecture story.  
2. **Technical risk → business impact** — mechanism explains *why*; impact explains *why care*.  
3. **Cost of inaction** — make the default explicit: “If we do nothing, we are accepting …”  
4. **Options, not lone conclusions** — invite collaborative decision-making.  
5. **Close with a clear ask** — decision, accepted risk, or owner.

**Instead of:** “Race condition in payments.”  
**Try:** “Race condition can drop transactions silently → manual reconciliation + support load. Decide: accept risk until Q4, or schedule a 1-sprint fix before launch.”

---

## Goal → difficulty → solution → benefit (GDSB stack)

When presenting an initiative or defending a plan:

| Layer | Question | Example |
|-------|----------|---------|
| **Goal** | What outcome / commitment? | “Ship self-serve onboarding by Q3” |
| **Difficulty** | What’s in the way? | “Legacy auth blocks 40% of signup paths; on-call eats ~15% capacity” |
| **Solution** | What will we do? | “Option B: thin compatibility layer + flag rollout” |
| **Benefit** | Why org wins | “Support tickets −30%; unlocks sales demo path; de-risks Q4 growth target” |

Always end with **what you need from the manager** (decision, air cover, intro, budget, scope cut).

---

## Supporting your manager’s decision (managing up)

From “contracting” with your manager:

- **Ask how they want to be informed** for: weekly progress, emergencies, people issues, admin noise.  
- **Learn how *they* are measured** — then frame your work as feeding *their* scorecard.  
- **Don’t wait for them to set the agenda** at higher levels; you drive clarity.  
- **Never surprise them in a public meeting** — pre-wire bad news 1:1 first.

**Context split (not a conflict with healthy peer debate):**  
“Never surprise” applies to **your manager** (and steering that could ambush them).  
Public technical challenge with **peer / partner teams** is fine under [(f)](../cross-team/conflict-and-coordination.md) when pre-wired and idea-focused—do **not** use “never surprise boss” as a reason to avoid honest partner conflict. Target of the rule = **boss**, not every stakeholder.

**1:1 opening that builds trust:**

> “Three items: (1) green on X, (2) yellow risk on Y with options, (3) ask for decision on Z this week.”

---

## When *not* to manage up hard (safety valve)

Managing up is a tool, not a personality. **Throttle** when:

| Signal | Better move |
|--------|-------------|
| You lack facts; pressure is high | “I’ll confirm by [time]” — don’t invent BLUF numbers |
| Relationship is cold / new manager | Contract first (how they want news); smaller asks |
| Political minefield (re-org, RIF rumor) | Align privately with your manager; no public campaigning |
| You’re optimizing for ego / being right | Switch to shared goal + options; drop the lecture |
| The decision is already closed for real reasons | Document accepted risk; don’t re-litigate weekly |
| Skip-level would undermine your manager | Pre-wire *your* manager; never ambush them via their boss |

**Rule:** Clarity and options build trust; volume and surprise burn it.

---

## Do / Don’t

| Do | Don’t |
|----|--------|
| Lead with conclusion + ask | Bury the ask after 8 slides of context |
| Quantify impact when possible | “We improved performance” with no number |
| Offer 2–3 options with tradeoffs | Only dump problems without paths |
| Translate tech into capacity / risk / revenue / customer | Lead with framework names and internal jargon |
| Surface accepted risk explicitly | Leave silence that later becomes blame |
| Balance wins + risks + requests | Only show up when something is on fire |

---

## Checklists

### Pre-send / pre-meeting (2 minutes)

- [ ] Can someone skim only the first 3 sentences and know the decision?  
- [ ] Is impact stated in business/org language?  
- [ ] Are options real (each has a cost)?  
- [ ] Is the ask dated?  
- [ ] Would my manager be blindsided if this is the first time they hear it?

### Status update skeleton (Slack / email / weekly)

```
Progress: …
Risks / blockers: …
Decision / resource needed: … (or “none this week”)
```

---

## Success signals

- [ ] Manager replies with a decision or explicit “accept risk,” not “let’s discuss sometime”  
- [ ] You are asked for options more often than for status dumps  
- [ ] Bad news delivered early still preserves trust  
- [ ] Skip-level / steering rarely surprises your boss  

---

## Worked mini-example (instability → decision)

**Technical-only (fails):** “User service is tightly coupled; tests flaky; need refactor.”  
**Decision-ready (works):**

> Instability is driving on-call load and slowing releases. If we do nothing, risk carries into next launch.  
> Options: (A) accept risk, (B) 1 sprint stabilize pre-launch, (C) partial fix + known gaps.  
> **Recommend B if launch can move 1 week; else C with written accepted risk.**  
> Decision needed by Friday.

---

## See also

- **Meetings / 對上說不 / follow-through:** [../meetings/in-meeting-and-follow-through.md](../meetings/in-meeting-and-follow-through.md)  
- **Plan + capacity:** [../roadmap-planning/planning-sense-proactive-framing.md](../roadmap-planning/planning-sense-proactive-framing.md) · [../shared/capacity-model.md](../shared/capacity-model.md)  
- **Resource asks (content of the case):** [../resource-advocacy/securing-resources-upward.md](../resource-advocacy/securing-resources-upward.md)  
- **Department value narrative:** [../department-value/presenting-department-value.md](../department-value/presenting-department-value.md)  
- **Index / reading order:** [../README.md](../README.md)

---

## Sources

- *Managing upwards* — The Engineering Manager: https://www.theengineeringmanager.com/management-101/managing-upwards/  
- *Communication Skills for Software Engineers: 5 Frameworks* — Utterskills: https://utterskills.com/blog/communication-skills-for-software-engineers  
- *How to Communicate With Executives* (BLUF, pre-read, escalation formula) — Orvo: https://www.getorvo.com/learn/executive-communication-strategy  
- *Executive Communication: Unlock Resources and Trust* — EM Tools: https://www.em-tools.io/engineering-manager-responsibilities/executive-communication  
