# Research notes — sources surveyed

**Purpose:** Provenance for the skill corpus. Every skill file cites at least one concrete source with URL.

**Survey window:** 2026-08 (web search + full-page fetch of key articles).

**Scope of survey:** Tech engineering-management blogs, staff-engineer career guides, executive-communication frameworks used by EMs/PMs/ICs, product cross-functional conflict writeups, plus **public Amazon sources** (shareholder letters, author-site concepts, AWS COE). Chinese + English both acceptable. Amazon mechanisms fold into a–f via `shared/amazon-mapping.md` — not a seventh theme.

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
| 13 | 2015 letter to shareholders (Type 1 / Type 2 doors) — SEC EX-99.1 | https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm | a, c |
| 14 | 2016 letter to shareholders (Disagree and commit; escalate misalignment) | https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders | a, c, f |
| 15 | 2017 letter to shareholders (six-page narratives + study hall) | https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders | a, c |
| 16 | Working Backwards concepts (PR/FAQ, input metrics, STO, operating cadence, narratives) | https://workingbackwards.com/concepts/ | a–f (see amazon-mapping) |
| 17 | Working Backwards PR/FAQ process | https://workingbackwards.com/concepts/working-backwards-pr-faq-process/ | d, b, a |
| 18 | AWS Correction of Error (COE) | https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/ | c |


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
| (a) Present goals/difficulties/solutions/benefits + manager decisions | `executive-communication/decision-ready-updates.md` | 1, 2, 3, 4, 13, 14, 15 |
| (b) Secure resources upward | `resource-advocacy/securing-resources-upward.md` | 4, 5, 6, 10, 16, 17 |
| (c) Meeting + post-meeting actions | `meetings/in-meeting-and-follow-through.md` | 1, 3, 12, 13, 14, 15, 18 |
| (d) Roadmap / “already planned” | `roadmap-planning/planning-sense-proactive-framing.md` | 2, 5, 7, 8, 16, 17 |
| (e) Department value | `department-value/presenting-department-value.md` | 1, 4, 7, 16 |
| (f) Cross-dept conflict | `cross-team/conflict-and-coordination.md` | 8, 9, 10, 11, 14, 16 |

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
| **Amazon mechanism map** | `shared/amazon-mapping.md` | PR/FAQ vs six-pager; doors; STO; input metrics; exclusions (punt-labs / Cagan / Bar Raiser) |


Presentation layer is **application of** skills a–f (not a seventh upward theme). Style is synthesized from public QBR/roadmap practice + semiconductor milestone vocabulary—not internal Google/MTK templates.

## Method notes

- Prefer **actionable** extracts (templates, phrases, checklists) over summary abstracts.
- Skills synthesize multiple sources into one playbook; claims that are source-specific keep the link inline.
- No fabricated podcast quotes or invented case numbers.
- Capacity percentages are **harmonized** in `shared/capacity-model.md` (do not re-fork %).

## Amazon pass (2026-08)

Public letters + https://workingbackwards.com/concepts/ only. No pirate copy of *Working Backwards*.

**Explicitly not imported**
- punt-labs/prfaq (LaTeX factory, four meeting personas)
- Cagan four-risks labels; Kahneman decision-quality checklist (punt-labs overlay)
- Bar Raiser hiring loop (no hiring theme in a–f)
