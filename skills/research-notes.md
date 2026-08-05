# Research notes — sources surveyed

**Purpose:** Provenance for the skill corpus. Every skill file cites at least one concrete source with URL.

**Survey window:** 2026-08 (web search + full-page fetch of key articles).

**Scope of survey:** Tech engineering-management blogs, staff-engineer career guides, executive-communication frameworks used by EMs/PMs/ICs, product cross-functional conflict writeups. Chinese + English both acceptable; corpus below is primarily English high-signal sources with transferable tactics.

---

## Sources consulted (primary)

| # | Title | URL | Used in theme(s) |
|---|--------|-----|------------------|
| 1 | Managing upwards — The Engineering Manager | https://www.theengineeringmanager.com/management-101/managing-upwards/ | a, c, e |
| 2 | Communication Skills for Software Engineers: 5 Frameworks — Utterskills | https://utterskills.com/blog/communication-skills-for-software-engineers | a, d |
| 3 | How to Communicate With Executives — Orvo / getorvo | https://www.getorvo.com/learn/executive-communication-strategy | a, c |
| 4 | Executive Communication: Unlock Resources and Trust — EM Tools | https://www.em-tools.io/engineering-manager-responsibilities/executive-communication | a, b, e |
| 5 | Roadmap Planning: Turn Business Goals into Deliverable Plans — EM Tools | https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning | d, b |
| 6 | Headcount Planning: Get the Right People Early — EM Tools | https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning | b |
| 7 | Writing engineering strategy — StaffEng / Will Larson | https://staffeng.com/guides/engineering-strategy/ | d, e |
| 8 | The Staff Engineer Toolkit — Hands-on Architects | https://handsonarchitects.com/blog/2025/staff-engineer-toolkit/ | d, f |
| 9 | 8 Rules for Managing Conflict in Cross-Functional Teams — Product School | https://productschool.com/blog/product-strategy/conflict-resolution-cross-functional-teams | f |
| 10 | How To Influence Without Authority As A TPM — Mario Gerard | https://www.mariogerard.com/how-to-influence-without-authority-as-a-tpm/ | f, b |
| 11 | The PM's Guide to Influence Without Authority — QuestWorks | https://www.questworks.io/blog/product-manager-influence-without-authority.html | f |
| 12 | Capture action items in meetings (who/what/when) — Ticnote guide | https://ticnote.com/en/blog/action-items-in-meeting-minutes-guide | c |

## Secondary / landscape (titles noted; lighter use)

- Square Growth Framework for Engineers and EMs — https://developer.squareup.com/blog/squares-growth-framework-for-engineers-and-engineering-managers/
- Engineering management frameworks overview — https://www.em-tools.io/engineering-management-frameworks
- How to Be a Great Engineering Manager — https://waydev.co/becoming-a-great-engineering-manager/
- Conflict resolution bridging perspectives — https://www.oneeighty.io/resources/conflict-resolution-in-cross-functional-teams-bridging-perspectives
- Status / escalate formula patterns common across EM blogs (situation → impact → options → recommendation → deadline)

## Podcast / long-form landscape (not transcribed; tactics folded via written analogues)

Full episode transcripts were **out of scope** (plan non-goal). Equivalent frameworks appear in written form from the same community of practice:

- Engineering Manager / staff-eng style shows often restate: contract with your manager, BLUF updates, capacity-based roadmaps, business-case headcount — covered via sources 1–6.
- Staff+ influence content maps to sources 7–8, 10–11.

## Theme coverage map (for verification)

| Theme | Skill path | Grounded by sources |
|-------|------------|---------------------|
| (a) Present goals/difficulties/solutions/benefits + manager decisions | `executive-communication/decision-ready-updates.md` | 1, 2, 3, 4 |
| (b) Secure resources upward | `resource-advocacy/securing-resources-upward.md` | 4, 5, 6, 10 |
| (c) Meeting + post-meeting actions | `meetings/in-meeting-and-follow-through.md` | 1, 3, 12 |
| (d) Roadmap / “already planned” | `roadmap-planning/planning-sense-proactive-framing.md` | 2, 5, 7, 8 |
| (e) Department value | `department-value/presenting-department-value.md` | 1, 4, 7 |
| (f) Cross-dept conflict | `cross-team/conflict-and-coordination.md` | 8, 9, 10, 11 |

## Corpus wiring (post self-audit)

| Shared / meta | Path | Role |
|---------------|------|------|
| Capacity % (single source of truth) | `shared/capacity-model.md` | Quarterly A: unplanned 10–15%, debt 15–20%, features 60–70%; Headcount B: unplanned 20–30% |
| Index + reading order + op chain | `README.md` | Navigation + canonical ownership |
| Canonical: decision language | skill (a) | BLUF / SOR / GDSB |
| Canonical: capacity / intake | skill (d) + shared model | displace-not-add |
| Canonical: influence | skill (f) | stakeholder / RACI |
| Cross-links | See also on every skill | Relative paths |
| **Presentation scenarios** | `presentations/` | Slide outlines for tech review, demo, mgmt effectiveness, ROI, procurement, HC, roadmap, period start/end; MNC + Hsinchu IC style note |
| **Consistency audit** | `shared/consistency-audit.md` | Conflict matrix; context A/B; canonical dual-use rules |
| **Automated check** | `scripts/check_skill_consistency.py` | Capacity labeling + audit structure + matrix spot-checks |

Presentation layer is **application of** skills a–f (not a seventh upward theme). Style is synthesized from public QBR/roadmap practice + semiconductor milestone vocabulary—not internal Google/MTK templates.

## Method notes

- Prefer **actionable** extracts (templates, phrases, checklists) over summary abstracts.
- Skills synthesize multiple sources into one playbook; claims that are source-specific keep the link inline.
- No fabricated podcast quotes or invented case numbers.
- Capacity percentages are **harmonized** in `shared/capacity-model.md` (do not re-fork %).
