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
| Unlabeled dual directives remaining | **None** on capacity %, SOR ownership, influence, pushback, presentation vs playbook/design, example arcs |
| Intentional overlaps | Reuse with single canonical owner (index table) |
| Audit artifact | This file + automated checks `scripts/check_skill_consistency.py`, `scripts/test_pptx_assets.py` |

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
| `skills/presentations/00`–`09` + README | Deck **content templates** applying a–f (not visual design) |
| `skills/presentations/assets/README.md` + `storyline-guide.md` | PPTX content carriers + Aurora multi-deck plot |
| `scripts/pptx_deck_data.py` (`EXAMPLE_SITUATIONS`, `AURORA_TIMELINE`) | Situation cards + arc chronology SoT for examples |
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
| 12 | Presentation decks vs a–f playbooks | `presentations/**`, index | **context-separated** → **fixed** | Decks = **content** page order; playbooks = behavior. presentations/README “簡報層紀律”; no third % |
| 12b | Content template vs visual design | `presentations/**`, assets, root README | **context-separated** → **fixed** | Corpus labels decks as **內容模板** only; Agent must copy content style (BLUF/options/REC/arc), **not** sample PPTX chrome (colors/margins/fonts). Banner on `00`–`09` + assets README |
| 13 | QBR narrative (e) vs period-end deck 09 | (e), presentations/09 | **consistent** | 09 applies (e)+(a); same answer-first QBR spine |
| 14 | Resource deck 06 vs skill (b) | 06, (b) | **consistent** | 06 labels capacity model **B** 20–30% |
| 15 | Roadmap deck 07 vs skill (d) | 07, (d) | **consistent** | 07 quotes model **A** 60–70 / 15–20 / 10–15 |
| 16 | “Never surprise boss” vs “healthy public conflict” | (a)(c) vs (f), index intentional splits | **context-separated** → **fixed** labels | Public *peer* challenge OK when pre-wired [(f)]; **do not** blindside *your manager* in steering [(a)(c)]. Index row + “Context split” callouts in (a)(c)(f) |
| 17 | When *not* to manage up hard (a) vs always-BLUF | (a) safety valve | **consistent** | Throttle is situational; does not revoke BLUF when you *do* communicate |
| 18 | Dual “canonical for escalation” wording | (f) old header vs index | **fixed** | (f) no longer claims sole “escalation packet” ownership |
| 19 | Example `prior_arc` / `next_arc` vs presentation catalog order `01`–`09` | `pptx_deck_data.EXAMPLE_SITUATIONS`, `storyline-guide.md`, `test_pptx_assets.py` | **context-separated** | **Story chronology ≠ catalog number order.** Aurora presentation order is **01→02→03→06→04→05→07→09→08** (`AURORA_PRESENTATION_ORDER`). prior_arc must not cite a later deck as already done (e.g. 09 must not claim 08 as prior). Enforced by asset tests |
| 20 | Lagging KPI dates vs deck ask deadlines | `EXAMPLE_SITUATIONS`, `AURORA_TIMELINE` | **consistent** | Evidence dates always pre-date that deck’s `decide_by` / ask deadline (asset tests) |

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

### 4.4b Never-surprise boss vs healthy peer conflict (matrix 16)

| Target of the room | Rule | Canonical |
|--------------------|------|-----------|
| **Your manager** / skip-level / steering that can ambush them | Never blindside; pre-wire 1:1 first | **(a)** + **(c)** |
| **Peer / partner** technical debate | Public challenge OK if pre-wired, idea-not-person | **(f)** healthy conflict |

In-corpus: `skills/README.md` intentional-split row; “Context split” paragraphs in (a) managing-up, (c) intro, (f) healthy-conflict.

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

**Content template vs visual design (matrix 12b):**  
Every deck outline (`00`–`09`), `presentations/README`, and `assets/README` labels packs as **內容模板 (content template)** — Agent copies **content style** (BLUF / options / REC / arc / IC·MNC narrative), **not** sample PPTX chrome. Real delivery uses the company slide master. Enforced by `check_skill_consistency.py` → `check_content_template_labeling`.

### 4.6 Example storyline arcs (matrix 19–20)

| Rule | In-corpus location |
|------|--------------------|
| Multi-deck plot order | `skills/presentations/assets/storyline-guide.md` + `AURORA_PRESENTATION_ORDER` in `scripts/test_pptx_assets.py` |
| Per-deck prior/next prose | `EXAMPLE_SITUATIONS[*].prior_arc` / `next_arc` in `scripts/pptx_deck_data.py` |
| Master calendar | `AURORA_TIMELINE` in `scripts/pptx_deck_data.py`; mirrored in assets README chronology table |
| Catalog `01`–`09` vs story order | Catalog is **scenario type index**; story order is **calendar + decision dependency** (08 after 09 is intentional: Q3 kickoff follows Q2 QBR) |

**Not a conflict:** Opening only `07-roadmap.md` does not require knowing 03→06 sequencing; arcs apply when using **filled example** packs / storyline guide for agent decision practice.

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
| Banner on `00`–`09` + indexes: **內容模板 ≠ 預設美工排版** | Agent must not treat sample PPTX as design system |
| Checker: `check_content_template_labeling` | Regressions on missing content-template notice |
| Matrix rows 19–20 + §4.6 for example arcs | Catalog order ≠ story chronology; tests enforce prior_arc |
| Matrix 16: Context-split callouts in (a)(c)(f) + index row | Never-surprise boss ≠ ban on healthy peer conflict |

---

## 6. How to re-verify (for humans or CI)

```bash
# From repo root
python3 scripts/check_skill_consistency.py
python3 scripts/test_pptx_assets.py
# optional: python3 scripts/check_markdown_links.py
```

Manual: re-read matrix §3; open every path in “Files checked”; confirm distinguishing rule still present.

---

## 7. Residual non-conflicts (not fixed, by design)

- Example metrics (e.g. “−30% tickets”, “on-call ~15%”) are **illustrations**, not alternate capacity models.  
- research-notes may restate A/B numbers as documentation of SoT.  
- MNC vs Hsinchu *style* differences in presentations/00 are tone/vocabulary, not rule conflicts.  
- Sample PPTX navy palette / officecli layout tokens are **generator-only** chrome, not skill policy (matrix 12b).

---

## 8. Sign-off

| Criterion (plan AC) | Met? |
|---------------------|------|
| Durable multi-section audit with concrete paths | Yes — this file (§1–8) |
| Every apparent conflict context-separated or fixed | Yes — matrix §3 incl. 12b, 19–20 |
| No unlabeled mutually exclusive directives on same decision | Yes — after §5 |
| Conflict matrix topic → status | Yes — §3 |
| Capacity A/B · SOR/escalation · 對上說不 · influence b/f · content-template · arcs | Yes — §3 rows 1,5,7,8,12/12b,19 + deep-dives §4 |
