# Skill corpus consistency audit

**Date:** 2026-08-06  
**Scope:** `skills/**` — themes (a)–(f), `shared/capacity-model.md`, index canonical ownership, `presentations/**`  
**Purpose:** Durable record that skills are logically consistent; apparent conflicts are **context-separated** or **fixed** in-corpus.  
**Method:** Path-by-path review + grep of capacity % + canonical headers + presentation cross-check.

---

## 1. Executive summary

| Verdict | Detail |
|---------|--------|
| **Overall** | **Consistent** after labeling fixes (see §5) |
| Unlabeled dual directives remaining | **None** on capacity %, SOR ownership, influence, pushback, presentation vs playbook |
| Intentional overlaps | Reuse with single canonical owner (index table) |
| Audit artifact | This file + automated check `scripts/check_skill_consistency.py` |

**Reader rule:** If two files mention the same idea, follow **[../README.md](../README.md) Canonical ownership** first; use this matrix for “which context am I in?”

---

## 2. Corpus map (files reviewed)

| Path | Role |
|------|------|
| `skills/README.md` | Index, op chain, **canonical ownership**, context-split legend |
| `skills/shared/capacity-model.md` | Sole numeric capacity SoT (A/B) |
| `skills/shared/consistency-audit.md` | This audit |
| `skills/executive-communication/decision-ready-updates.md` | (a) BLUF/SOR/GDSB |
| `skills/resource-advocacy/securing-resources-upward.md` | (b) resource cases; capacity **B** |
| `skills/meetings/in-meeting-and-follow-through.md` | (c) room pushback, actions |
| `skills/roadmap-planning/planning-sense-proactive-framing.md` | (d) plan pushback, capacity **A**+link **B** |
| `skills/department-value/presenting-department-value.md` | (e) value/QBR |
| `skills/cross-team/conflict-and-coordination.md` | (f) influence; cross-team fields |
| `skills/presentations/00`–`09` + README | Deck outlines applying a–f |
| `skills/research-notes.md` | Provenance (not behavioral rules) |

---

## 3. Conflict matrix

Status legend: **consistent** (same rule everywhere) · **context-separated** (two rules, labeled by situation) · **fixed** (corpus edited this pass to remove dual-canonical or unlabeled conflict)

| # | Topic | Files checked | Status | Distinguishing rule (in-corpus) |
|---|--------|---------------|--------|----------------------------------|
| 1 | Unplanned buffer **10–15%** vs **20–30%** | `shared/capacity-model.md`, (d), (b), (e), `presentations/06`, `07`, `03` | **context-separated** | **A** = quarterly allocation (commit honesty); **B** = headcount/staffing demand. Phrase in capacity-model §“Why two numbers?” |
| 2 | Debt **15–20%** / features **60–70%** | capacity-model, (d), presentations/07 | **consistent** | Only under context **A** quarterly split |
| 3 | Ops-heavy unplanned up to **15–20%** | capacity-model (A), (d) table | **consistent** | Labeled as ops-heavy variant of **A**, not a third system |
| 4 | BLUF / SOR / GDSB / escalation *shape* | (a), (c), (f), presentations/* | **consistent** | Index + (a) **Canonical for** sentence shape; others link to (a) |
| 5 | Escalation “packet” (a) vs (f) | (a), (f) | **context-separated** → **fixed** header | (a) = Options→Rec→Ask *shape*; (f) = cross-team *fields* only. (f) header now says “Not canonical for sentence shape” |
| 6 | Resource capacity math vs roadmap | (b), (d), capacity-model | **context-separated** | (b) forces **B** 20–30%; (d) defaults **A** for plans, points HC to (b) |
| 7 | 對上說不 (c) vs (d) | (c), (d), index | **context-separated** → **fixed** index rows | **Room/live** → (c); **plan/intake/one-pager** → (d); same displace logic |
| 8 | Influence (b) vs (f) | (b) short section, (f) full | **context-separated** | (b): “Short list only—full playbook is (f)”; (f) owns stakeholder/RACI |
| 9 | Displace / infinite capacity | (c)(d)(b) presentations | **consistent** | Canonical intake/displace in (d); scripts reuse, don’t redefine |
| 10 | Pre-wire manager vs pre-wire peers | (a)(c) vs (f) | **consistent** | Same habit, different target (boss vs partner stakeholders) |
| 11 | Department value vs decision-ready | (e), (a) | **consistent** | (e) owns metrics/QBR; (a) owns sentence structure (linked) |
| 12 | Presentation decks vs a–f playbooks | `presentations/**`, index | **context-separated** → **fixed** | Decks = page order; playbooks = behavior. presentations/README “簡報層紀律”; no third % |
| 13 | QBR narrative (e) vs period-end deck 09 | (e), presentations/09 | **consistent** | 09 applies (e)+(a); same answer-first QBR spine |
| 14 | Resource deck 06 vs skill (b) | 06, (b) | **consistent** | 06 labels capacity model **B** 20–30% |
| 15 | Roadmap deck 07 vs skill (d) | 07, (d) | **consistent** | 07 quotes model **A** 60–70 / 15–20 / 10–15 |
| 16 | “Never surprise boss” vs “healthy public conflict” | (a)(c) vs (f) | **context-separated** | Public *peer* challenge OK when pre-wired; **do not** blindside *your manager* in steering |
| 17 | When *not* to manage up hard (a) vs always-BLUF | (a) safety valve | **consistent** | Throttle is situational; does not revoke BLUF when you *do* communicate |
| 18 | Dual “canonical for escalation” wording | (f) old header vs index | **fixed** | (f) no longer claims sole “escalation packet” ownership |

---

## 4. Topic deep-dives

### 4.1 Capacity buffers

**SoT:** `skills/shared/capacity-model.md`

| Context | When | Unplanned | Debt | Outcomes |
|---------|------|-----------|------|----------|
| **A** | Quarter plan, roadmap deck, value brief capacity pie | 10–15% (ops-heavy → 15–20%) | 15–20% | 60–70% |
| **B** | Headcount / annual staffing / resource deck | 20–30% of demand | In demand themes | Don’t staff 100% feature |

**Not a contradiction:** staffing with B still *allocates* the quarter with A once people are on board.

### 4.2 Decision / escalation language

1. Write **Situation → Impact → Options → Recommendation → Ask by date** per **(a)**.  
2. If parties are multi-team, add **(f)** fields (shared goal, each metric, what we tried).  
3. Close loop with **(c)** owner+date writeback.

### 4.3 Pushback / 對上說不

| Situation | Skill | Artifact |
|-----------|-------|----------|
| Boss dumps work *in a meeting* | (c) | Spoken script + post-meeting decision writeback |
| Protecting the published plan / intake | (d) | One-pager, displace table, wiki intake rule |
| Need headcount because plan is full | (b) + capacity **B** | Business case, not only “no” |

### 4.4 Influence without authority

| Situation | Skill |
|-----------|--------|
| Multi-team priority / RACI / coalition | **(f)** full |
| You need budget but don’t own purse; short tips | **(b)** “Influence when you don’t own the budget” → then (f) if multi-party |

### 4.5 Presentations layer

| Deck | Primary skills | Capacity context |
|------|----------------|------------------|
| 01 technical | a, d, f | n/a or A if capacity hit |
| 02 results | a, e | n/a |
| 03 management | e, a, b | **A** (B only if HC ask) |
| 04 benefit | e, a | n/a |
| 05 procurement | b, a | n/a (TCO, not eng % buffer) |
| 06 resource | b, d, a | **B** |
| 07 roadmap | d, a, f | **A** |
| 08 period start | d, a, b | **A** (+ B if gap) |
| 09 period end | e, a, d | **A** for lookback pie |

---

## 5. Fixes applied this pass

| Change | Why |
|--------|-----|
| (f) Canonical header: fields vs (a) shape | Remove dual-canonical “escalation packet” |
| (d) Canonical: plan-version 對上說不; not room scripts | Match (c) room ownership |
| Index: expanded canonical table + intentional-split legend | Reader can resolve without re-audit |
| presentations/README 簡報層紀律 | Decks must not invent % or SOR |
| presentations/03 capacity line labels **A** (and when **B**) | Unlabeled “unplanned %” risk |
| capacity-model “Also used by” presentations A/B map | SoT points to deck usage |

---

## 6. How to re-verify (for humans or CI)

```bash
# From repo root
python3 scripts/check_skill_consistency.py
```

Manual: re-read matrix §3; open every path in “Files checked”; confirm distinguishing rule still present.

---

## 7. Residual non-conflicts (not fixed, by design)

- Example metrics (e.g. “−30% tickets”, “on-call ~15%”) are **illustrations**, not alternate capacity models.  
- research-notes may restate A/B numbers as documentation of SoT.  
- MNC vs Hsinchu *style* differences in presentations/00 are tone/vocabulary, not rule conflicts.

---

## 8. Sign-off

| Criterion (plan AC) | Met? |
|---------------------|------|
| Durable multi-section audit with concrete paths | Yes — this file |
| Every apparent conflict context-separated or fixed | Yes — matrix §3 |
| No unlabeled mutually exclusive directives on same decision | Yes — after §5 |
| Conflict matrix topic → status | Yes — §3 |
