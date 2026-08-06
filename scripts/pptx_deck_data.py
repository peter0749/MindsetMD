#!/usr/bin/env python3
"""Deck content packs: placeholder templates + filled Aurora/NovaSemi examples.

Shared fiction for examples:
  Company  NovaSemi (IC design)
  Program  Project Aurora — 5nm connectivity SoC
  Team     Atlas Platform (DV, integration, bring-up)
  Lead     Alex Chen (EM) → reports to VP Eng Morgan Lee

Master chronology (must stay consistent across examples):
  2026-03-16  01 tech review presented; decide AON Option B by 2026-03-20
  2026-04-10  RTL freeze held (enabled by Option B)
  2026-04-28  Tape-out
  2026-05-12  First silicon in lab
  2026-05-15  Day-3 boot
  2026-05-16  02 results readout; sample plan ask by 2026-05-22; sample ship 2026-06-30
  2026-05-18  03 org health 1:1
  2026-05-20  06 +1 senior DV request
  2026-05-25  04 farm ROI (lagging KPIs: freeze 4/10, boot 5/15); expand ask by 2026-05-30
  2026-05-28  05 HelixSim procurement; decide by 2026-06-05
  2026-06-12  07 H2 roadmap
  2026-06-26  09 Q2 QBR lookback
  2026-07-01  08 Q3 period-start kickoff
"""
from __future__ import annotations

from datetime import date
from typing import Any

# --- shared example universe constants ---
EX_META = "Atlas Platform  ·  Project Aurora  ·  NovaSemi  ·  2026  ·  CONTENT-EXAMPLE"
EX_FOOTER = "Content example only (not visual design) — fictional program data"

# Machine-checkable anchors (tests import these)
AURORA_TIMELINE = {
    "01_decide_by": date(2026, 3, 20),
    "01_freeze_target": date(2026, 4, 10),
    "rtl_freeze_held": date(2026, 4, 10),
    "tape_out": date(2026, 4, 28),
    "first_silicon": date(2026, 5, 12),
    "day3_boot": date(2026, 5, 15),
    "02_present": date(2026, 5, 16),
    "02_sample_ask_by": date(2026, 5, 22),
    "sample_ship": date(2026, 6, 30),
    "04_present": date(2026, 5, 25),
    "04_ask_by": date(2026, 5, 30),
    "06_decide_by": date(2026, 5, 20),
    "09_qbr": date(2026, 6, 26),
    "08_q3_kickoff": date(2026, 7, 1),
}


def T(kicker, title, subtitle, bluf_title, bluf_status, bluf_body, body_slides, options, ask, ask_notes):
    return {
        "kicker": kicker,
        "title": title,
        "subtitle": subtitle,
        "meta": "Team X  ·  Program Alpha  ·  Qn YYYY  ·  CONTENT-TEMPLATE — replace placeholders (not visual design)",
        "bluf_title": bluf_title,
        "bluf_status": bluf_status,
        "bluf_body": bluf_body,
        "body_slides": body_slides,
        "options_table": options,
        "ask_lines": ask,
        "ask_notes": ask_notes,
        "kind": "template",
    }


def E(kicker, title, subtitle, bluf_title, bluf_status, bluf_body, body_slides, options, ask, ask_notes, story):
    return {
        "kicker": kicker,
        "title": title,
        "subtitle": subtitle,
        "meta": EX_META,
        "bluf_title": bluf_title,
        "bluf_status": bluf_status,
        "bluf_body": bluf_body,
        "body_slides": body_slides,
        "options_table": options,
        "ask_lines": ask,
        "ask_notes": ask_notes,
        "kind": "example",
        "story": story,
    }



# Public pattern provenance per scenario (structure only — not confidential decks)
SCENARIO_PATTERNS: dict[str, dict] = {
    "01-technical-review": {
        "label": "Design-doc / RFC options table + residual risk",
        "sources": [
            ("StaffEng — Writing engineering strategy", "https://staffeng.com/guides/engineering-strategy/"),
            ("Utterskills — options instead of single conclusion", "https://utterskills.com/blog/communication-skills-for-software-engineers"),
        ],
    },
    "02-results-demo": {
        "label": "Launch / silicon bring-up readout (impact first)",
        "sources": [
            ("MediaTek public 2nm tape-out milestone language", "https://www.mediatek.com/press-room/mediatek-develops-chip-utilizing-tsmcs-2nm-process-achieving-milestones-in-performance-andpower-efficiency"),
            ("SRE Book — example postmortem impact summary shape", "https://sre.google/sre-book/example-postmortem/"),
        ],
    },
    "03-management-effectiveness": {
        "label": "Team health + capacity scorecard (managing up)",
        "sources": [
            ("The Engineering Manager — Managing upwards", "https://www.theengineeringmanager.com/management-101/managing-upwards/"),
            ("Netflix culture (public) — talent density language only", "https://jobs.netflix.com/culture"),
        ],
    },
    "04-benefit-value": {
        "label": "Platform / shared infra investment impact chain",
        "sources": [
            ("EM Tools — executive communication / impact framing", "https://www.em-tools.io/engineering-manager-responsibilities/executive-communication"),
            ("StaffEng — strategy as leverage (not ticket dumps)", "https://staffeng.com/guides/engineering-strategy/"),
        ],
    },
    "05-procurement-proposal": {
        "label": "Vendor TCO options + procurement lead time",
        "sources": [
            ("Industry EDA/tool buy case shape (must/should + lead time)", "https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning"),
        ],
    },
    "06-resource-request": {
        "label": "Roadmap-backed headcount / resource business case",
        "sources": [
            ("EM Tools — Headcount planning", "https://www.em-tools.io/engineering-manager-responsibilities/headcount-planning"),
            ("TPM influence without authority (when no budget ownership)", "https://www.mariogerard.com/how-to-influence-without-authority-as-a-tpm/"),
        ],
    },
    "07-roadmap": {
        "label": "Outcome themes + not-doing + capacity-honest plan",
        "sources": [
            ("EM Tools — Roadmap planning", "https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning"),
            ("StaffEng — engineering strategy", "https://staffeng.com/guides/engineering-strategy/"),
        ],
    },
    "08-period-start-planning": {
        "label": "Commit / stretch / out period kickoff",
        "sources": [
            ("EM Tools — Roadmap / planning kickoff norms", "https://www.em-tools.io/engineering-manager-responsibilities/roadmap-planning"),
            ("BLUF executive framing", "https://www.getorvo.com/learn/executive-communication-strategy"),
        ],
    },
    "09-period-end-review": {
        "label": "Leadership QBR scorecard → risks → asks",
        "sources": [
            ("SRE Book — example postmortem (impact honesty)", "https://sre.google/sre-book/example-postmortem/"),
            ("EM Tools — executive communication updates", "https://www.em-tools.io/engineering-manager-responsibilities/executive-communication"),
        ],
    },
}

# ============================================================================
# Scenario packs: each key has template + example
# ============================================================================


# Cold-reader situation cards (examples only) — human/agent parse without inventing facts
EXAMPLE_SITUATIONS: dict[str, dict[str, str]] = {
    "01-technical-review": {
        "presenter": "Alex Chen — EM, Atlas Platform (NovaSemi)",
        "decision_maker": "Morgan Lee — VP Engineering (final call on freeze architecture)",
        "audience": "VP Eng + clock/analog/DV leads; PMIC IP liaison Ken optional",
        "what_happened": "Aurora AON clock architecture is still open 3 weeks before RTL freeze 2026-04-10. Full dual-source glitchless mux needs +3 eng-weeks and puts freeze at risk. DV cannot lock sleep-exit assertions until the architecture is frozen.",
        "stakes": "If freeze slips: tape-out and first-silicon slip → Tier-1 sample window for 6/30 compresses. If we ship dual mux unfinished: brown-out risk on deep-sleep exit for mobile SKUs.",
        "decision": "Choose AON clock path for freeze: A full dual mux now / B phased strap (REC) / C keep dual unfinished in RTL.",
        "recommend": "Option B — XO-only AON at freeze; dual-source behind DUAL_SRC_EN strap for revB.",
        "if_yes": "Freeze 4/10 holds; DV locks assertions; revB dual-mux enters H2 roadmap.",
        "if_no_or_delay": "Default C = freeze slip risk accepted; or A burns +3 eng-wk and still may miss 4/10.",
        "decide_by": "2026-03-20 EOD",
        "prior_arc": "(arc start) no prior deck",
        "next_arc": "02 results after first silicon if freeze holds → day-3 boot story",
    },
    "02-results-demo": {
        "presenter": "Alex Chen — EM, Atlas Platform",
        "decision_maker": "Morgan Lee — VP Eng (sample plan endorsement)",
        "audience": "VP Eng, program PM, package/IO leads",
        "what_happened": "Aurora A0 returned from fab 2026-05-12. Bring-up hit Linux prompt on day 3 (target was day 5). AON Option B (decided 3/20) held freeze 4/10 → TO 4/28 → this silicon.",
        "stakes": "Tier-1 wants samples by 2026-06-30 for design-win demo. Delay on sample plan blocks customer schedule; USB3 still yellow but not sample-critical.",
        "decision": "Approve customer sample plan targeting 2026-06-30 shipment (yes/no).",
        "recommend": "YES — approve sample plan; keep USB3 as parallel non-blocking work.",
        "if_yes": "Checklist owners fire; golden + 1 variant boards for Tier-1.",
        "if_no_or_delay": "Design-win demo slips; competitive window narrows.",
        "decide_by": "2026-05-22 steering",
        "prior_arc": "01 AON Option B → freeze 4/10 → TO 4/28 → silicon 5/12",
        "next_arc": "03 org health (people yellow) · 06 +1 DV if sample surge",
    },
    "03-management-effectiveness": {
        "presenter": "Alex Chen — EM, Atlas (1:1 with manager)",
        "decision_maker": "Morgan Lee — VP Eng (endorse hire path + air cover)",
        "audience": "Manager 1:1 (not full staff meeting)",
        "what_happened": "Q2 delivery is GREEN (freeze, day-3 boot) but people are YELLOW: Priya is single-threaded on HS IO DV; unplanned work hit ~20% vs 10–15% plan; USB3 only partial.",
        "stakes": "Without senior backup, sample surge + USB3 + burnout risk; Morgan may only hear good silicon news and under-invest in capacity.",
        "decision": "Endorse opening +1 senior DV req (detail in deck 06) and restate sample priority in steering.",
        "recommend": "Endorse hire path + air cover; do not wait for red attrition.",
        "if_yes": "Req opens ~5/22; people risk can return to green in H2.",
        "if_no_or_delay": "People stay yellow; USB3 and sample polish compete for one senior.",
        "decide_by": "2026-05-18 1:1",
        "prior_arc": "02 first-silicon green just landed",
        "next_arc": "06 formal HC business case same week",
    },
    "04-benefit-value": {
        "presenter": "Alex Chen — EM, Atlas (with farm utilization data)",
        "decision_maker": "Morgan Lee + Finance (seat budget)",
        "audience": "VP Eng, finance partner, program leads sharing the farm",
        "what_happened": "Shared DV farm has run ~2 quarters. Median regression 18h→6h. Pre-silicon farm loops helped catch DDR training bug before A0. Deck presented ~2026-05-25 AFTER freeze 4/10 and day-3 boot 5/15 (lagging KPIs already real).",
        "stakes": "H2 multi-program load (Aurora revB + WiFi IP) will re-queue the farm without +20 seats; freeze-class slips return.",
        "decision": "Continue only vs Expand +20 seats (REC) vs shrink.",
        "recommend": "EXPAND +20 seats; ~5-month payback envelope on avoided spin risk (assumptions labeled).",
        "if_yes": "PO path with deck 05 HelixSim seats; H2 capacity honest.",
        "if_no_or_delay": "Queue wait spikes in H2; sample/revB compete for sim slots.",
        "decide_by": "2026-05-30 finance window",
        "prior_arc": "02 silicon success used farm; 01 freeze held partly due to faster regressions",
        "next_arc": "05 procurement renews/expands sim licenses to match seats",
    },
    "05-procurement-proposal": {
        "presenter": "Alex Chen — EM (with procurement/finance)",
        "decision_maker": "Morgan → Finance → Procurement chain",
        "audience": "Eng + finance + procurement",
        "what_happened": "HelixSim contract ends 2026-07-31. Farm expand (deck 04 ask by 5/30) needs concurrent seats. Vendor lead time ~45 days → decide by 2026-06-05 or miss deploy before H2 peak.",
        "stakes": "Late PO = sim queue explosion during revB/sample support; switching to NovaSim costs 4–6 months port.",
        "decision": "HelixSim 3yr +20 (REC) vs switch NovaSim vs short 6-mo extend.",
        "recommend": "HelixSim 3-year +20 seats; start PO immediately.",
        "if_yes": "Seats land ~3 weeks after PO; p95 queue target <30 min in freeze windows.",
        "if_no_or_delay": "Short extend is expensive band-aid; switch burns schedule.",
        "decide_by": "2026-06-05 (includes vendor lead time)",
        "prior_arc": "04 farm expand decision (5/25–5/30); 02 silicon/sample load growth",
        "next_arc": "07 H2 roadmap assumes seats available",
    },
    "06-resource-request": {
        "presenter": "Alex Chen — EM, Atlas",
        "decision_maker": "Morgan Lee — VP Eng (HC approval)",
        "audience": "VP Eng; HRBP optional",
        "what_happened": "Post-silicon (5/15 boot) sample path is live. Priya is sole senior on HS IO DV. Q2 unplanned ~20%. USB3, sample board variants, and H2 WiFi DV collide on one person.",
        "stakes": "If no hire: USB3 → 7/15 (misses sample polish); Tier-1 may get only golden board; people yellow stays (deck 03).",
        "decision": "Full +1 senior DV (REC) vs 6-mo contractor vs no hire + descope USB3 from sample.",
        "recommend": "Full +1 senior DV; open req by 2026-05-22.",
        "if_yes": "Offer ~6 weeks; productive mid-Q3; sample + USB3 + backup for Priya.",
        "if_no_or_delay": "Explicit trade-off: drop USB3 from sample or accept slip — not silent heroics.",
        "decide_by": "2026-05-20 (post-silicon week)",
        "prior_arc": "02 green silicon · 03 people yellow",
        "next_arc": "Later decks 04–05/07/09/08 assume req opened; H2 uses productive hire",
    },
    "07-roadmap": {
        "presenter": "Alex Chen — EM + program PM",
        "decision_maker": "Morgan Lee + steering (endorse map + priority rule)",
        "audience": "Steering: eng, PM, IP/package partners",
        "what_happened": "H1 delivered freeze, silicon, sample path. H2 must choose: sample support vs early WiFi IP integrate if capacity conflicts. RevB dual-mux AON still owed from Option B residual.",
        "stakes": "Without an explicit priority rule, partner teams will dual-commit Atlas and break sample SLA.",
        "decision": "Endorse H2 themes; confirm default sample > WiFi on conflict.",
        "recommend": "Endorse map; sample-first; revB AON in investment band; WiFi stretch.",
        "if_yes": "Intake rule enforceable; partners plan against the same not-doing list.",
        "if_no_or_delay": "Hallway commits return; sample and WiFi thrash.",
        "decide_by": "2026-06-12 roadmap review",
        "prior_arc": "01 residual revB · 02 sample · 04/05 farm/seats · 06 hire",
        "next_arc": "09 Q2 QBR (6/26) then 08 Q3 commit locks this map",
    },
    "08-period-start-planning": {
        "presenter": "Alex Chen — EM, Atlas kickoff",
        "decision_maker": "Morgan Lee (endorse Option B period plan)",
        "audience": "Atlas team + VP Eng + key deps (PMIC, package, WiFi IP)",
        "what_happened": "Q3 starts 2026-07-01. Samples shipped/plan 6/30. Need shared commit vs stretch vs out so the team does not treat WiFi as silent commit.",
        "stakes": "Ambiguous commits → over-promise to WiFi partners or under-serve Tier-1 sample SLA.",
        "decision": "Endorse period plan Option B (balanced) vs A aggressive vs C sample-only.",
        "recommend": "Option B: COMMIT sample SLA + revB AON start + USB3 close; STRETCH WiFi; OUT sensor hub.",
        "if_yes": "Team executes one scoreboard; stretch only if sample green.",
        "if_no_or_delay": "A needs more HC/contractor; C abandons revB residual from 01.",
        "decide_by": "2026-07-01 kickoff",
        "prior_arc": "09 QBR asked for Q3 B; 07 roadmap themes; 06 hire in flight",
        "next_arc": "(feeds next QBR) execute against this commit table",
    },
    "09-period-end-review": {
        "presenter": "Alex Chen — EM, Atlas Q2 QBR",
        "decision_maker": "Morgan Lee + leadership forum",
        "audience": "VP Eng, peer EMs, program",
        "what_happened": "Q2 closed ~2026-06-26 lookback: AON B 3/20, freeze 4/10, TO 4/28, day-3 boot 5/15, sample on track 6/30. USB3 partial; unplanned ~20%; IO single-thread carried yellow.",
        "stakes": "If leadership only hears GREEN silicon, they may underfund Q3 hire/intake discipline and recreate unplanned overload.",
        "decision": "Endorse next priorities P1 sample SLA + P2 revB; keep WiFi stretch; support DV hire + Q3 plan B.",
        "recommend": "Overall GREEN with explicit carry risks; approve P1/P2 and HC path.",
        "if_yes": "Q3 kickoff (08) has air cover; hire continues; intake rule enforced.",
        "if_no_or_delay": "Same single-thread risk into sample support peak.",
        "decide_by": "This QBR (~2026-06-26) + follow-up into 7/01 kickoff",
        "prior_arc": "H1 arc so far: 01→02→03/06→04→05→07 (not 08 — Q3 kickoff is after this QBR)",
        "next_arc": "08 Q3 kickoff 7/01 under endorsed commits",
    },
}

SCENARIOS: dict[str, dict[str, Any]] = {
    "01-technical-review": {
        "template": T(
            "SCENARIO 01  ·  DESIGN / TECH REVIEW",
            "Technical review: decision package",
            "Architecture / design freeze / major change — options before deep walkthrough",
            "BLUF — decision needed",
            "Status: YELLOW  ·  Decision: Approve Option B (phased) by Friday",
            "Goal: ship Program Alpha milestone without silent risk acceptance.\n\n"
            "Difficulty: [constraint — e.g. interface freeze / PPA / schedule].\n\n"
            "Recommendation: Option B — phased rollout with feature flags / limited cohort.\n\n"
            "If no decision: default equals Option C (do nothing) with accepted risk documented.",
            [
                (
                    "Problem, goal, constraints",
                    "Problem: [who is hurt / what fails].\n\n"
                    "Success looks like: [measurable exit criteria].\n\n"
                    "Constraints: schedule gate  |  PPA or SLO  |  capacity  |  dependency (IP / platform / team).\n\n"
                    "IC note: map to Arch → RTL freeze → DV exit → Tape-out as applicable.",
                    "State constraints before solution.",
                ),
                (
                    "Design sketch (one page)",
                    "Keep one block diagram or interface table here.\n\n"
                    "• Boundary / responsibility\n"
                    "• Data or signal path at a glance\n"
                    "• What is explicitly out of scope this review\n\n"
                    "Details → backup annex if asked.",
                    "One visual idea; deep-dive only on request.",
                ),
                (
                    "Risks & mitigations (top 3)",
                    "1. [Risk] — mitigation: … — owner: …\n"
                    "2. [Risk] — mitigation: … — owner: …\n"
                    "3. [Risk] — mitigation: … — owner: …\n\n"
                    "Residual risk after recommendation: [one sentence].",
                    "Every risk needs an owner.",
                ),
            ],
            [
                ["Option", "Outcome", "Schedule", "Risk", "Capacity"],
                ["A Fast", "Full scope now", "On date", "High", "Low extra"],
                ["B Phased (REC)", "Core first", "+1 gate buffer", "Med", "Med"],
                ["C Do nothing", "Status quo", "—", "Accepted", "—"],
            ],
            "Decision: Approve B / A / C\nOwner: [Name / role]\nBy: [date]\n\n"
            "Follow-ups: update design doc; notify dependent teams; schedule next gate.",
            "Close with decision sentence. Capture owner and date live.",
        ),
        "example": E(
            "SCENARIO 01  ·  EXAMPLE  ·  AURORA POWER DOMAIN",
            "Aurora: always-on domain clock decision",
            "Design freeze for AON clock mux — needed before RTL freeze 2026-04-10",
            "BLUF — approve phased clock mux",
            "Status: YELLOW  ·  Recommend Option B  ·  Decide by Fri 2026-03-20 (Morgan)",
            "Goal: freeze AON clock architecture so DV can lock assertions before RTL freeze.\n\n"
            "Difficulty: Full dual-source mux + glitchless switch needs +3 eng-weeks and threatens 4/10 freeze.\n\n"
            "Recommendation: Option B — single-source AON at freeze; dual-source behind feature strap for revB.\n\n"
            "If no decision by Friday: default is Option C (keep dual mux in RTL) with accepted freeze slip risk.",
            [
                (
                    "Problem, goal, constraints",
                    "Problem: Always-on domain can brown-out during deep-sleep exit if clock source switches mid-transition; "
                    "field risk on mobile SKUs.\n\n"
                    "Success: AON boots glitch-free across 3 corners in UVM; RTL freeze stays 4/10.\n\n"
                    "Constraints: freeze 4/10 · package power budget · PMIC IP delivers 3/28 · Atlas has 2 clock experts.",
                    "Customer SKU power-exit is the business hook.",
                ),
                (
                    "Design sketch (one page)",
                    "AON island ← clock mux ← {XO, RCOSC}\n"
                    "   └─ strap: DUAL_SRC_EN (default 0 at freeze)\n\n"
                    "RevA (freeze): XO only + monitored RCOSC free-run (no switch).\n"
                    "RevB: enable glitchless mux after silicon learnings.\n\n"
                    "Out of scope today: full PMIC firmware; DV scoreboard details (annex).",
                    "One page; point to RFC-AURORA-117 for waveforms.",
                ),
                (
                    "Risks & mitigations (top 3)",
                    "1. RCOSC accuracy in cold boot — mitigate: characterize in bring-up; owner: Mina (analog).\n"
                    "2. Late PMIC IP change — mitigate: freeze interface table 3/28; owner: Ken (IP).\n"
                    "3. DV coverage hole on sleep-exit — mitigate: 2 dedicated sequences this sprint; owner: Priya.\n\n"
                    "Residual after B: no glitchless dual-switch on first silicon (accepted for revA).",
                    "Residual risk is explicit for silicon.",
                ),
            ],
            [
                ["Option", "Outcome", "Schedule", "Risk", "Capacity"],
                ["A Full dual mux now", "Complete AON switch", "Freeze → 5/01", "High DV", "+3 eng-wk"],
                ["B Phased strap (REC)", "XO path frozen", "Freeze 4/10 holds", "Med", "+0.5 eng-wk"],
                ["C Keep dual in RTL", "No scope cut", "Likely slip", "Accepted freeze risk", "0"],
            ],
            "Decision needed: Approve Option B for Aurora AON clock at freeze.\n"
            "Owner: Morgan Lee (VP Eng) with Alex Chen executing.\n"
            "By: Friday 2026-03-20 EOD.\n\n"
            "Follow-ups: publish RFC-AURORA-117 rev; notify PMIC + package; add revB dual-mux to H2 roadmap.",
            "Land B; do not re-open full dual-mux design in this room.",
            "Aurora AON clock: freeze on time via phased strap, dual-mux deferred to revB.",
        ),
    },
    "02-results-demo": {
        "template": T(
            "SCENARIO 02  ·  RESULTS / DEMO / LAUNCH",
            "Results readout",
            "What shipped, vs commitment, why it mattered — not a sprint diary",
            "BLUF — result & impact",
            "Status: GREEN  ·  Result: [X] delivered on [date]  ·  Ask: none / next-phase approve",
            "Outcome: [one line].\nImpact: [metric baseline → actual].\n"
            "Linked OKR / program goal: [one line].\n\nResidual risk or follow-ups: [or none].",
            [
                (
                    "Goal recall (period start)",
                    "Original commit: [promise].\nSuccess metric: target [T].\n\n"
                    "Avoid moving the goalposts — show the same definition of done.",
                    "Re-anchor to original commitment first.",
                ),
                (
                    "Outcome metrics",
                    "Metric A: target … / actual … / Δ …\nMetric B: …\n\n"
                    "IC examples: power −N% at iso-perf; bring-up day-k boot; coverage gate met.",
                    "Few metrics, high signal.",
                ),
                (
                    "How we got here + learnings",
                    "Three decisions that mattered:\n1. …\n2. …\n3. …\n\nKeep / stop / start (one each).",
                    "Only process insight that changes next quarter.",
                ),
            ],
            None,
            "Ask: [visibility only / approve next phase / fund follow-on]\n"
            "Or: No decision required — FYI readout.\n\nNext milestone: [date + gate].",
            "If pure celebration, still name residual risk.",
        ),
        "example": E(
            "SCENARIO 02  ·  EXAMPLE  ·  FIRST SILICON",
            "Aurora first silicon: day-3 boot achieved",
            "Bring-up readout for VP Eng + program — sample path unlocked",
            "BLUF — first silicon green on critical path",
            "Status: GREEN  ·  Day-3 Linux boot on A0 (silicon 5/12)  ·  Ask: sample plan for 6/30",
            "Outcome: Aurora A0 (fab return 2026-05-12) brought up; UART + DDR + Linux prompt on day 3 (target day 5).\n\n"
            "Impact: unlocks Tier-1 sample commit for end of June; de-risks H2 design-win demo.\n\n"
            "Residual: USB3 not yet stable (ECO-22); not on sample critical path.\n"
            "Prior: AON Option B (3/20) held RTL freeze 4/10 → tape-out 4/28 → this bring-up.",
            [
                (
                    "Goal recall (period start)",
                    "Q2 commit (period-start deck): first silicon bring-up with day-5 boot target; "
                    "UART+DDR minimum for internal validation.\n\n"
                    "Definition of done unchanged — no goalpost move.",
                    "Same DoD as kickoff.",
                ),
                (
                    "Outcome metrics",
                    "Boot day: target ≤5 / actual 3  (Δ −2 days)\n"
                    "Critical open bugs at handoff: target ≤5 / actual 4\n"
                    "AON sleep-exit (from tech review B): pass on 2/3 corners; cold corner in flight\n"
                    "Power (idle AON): target ≤2.1 mW / measured 1.9 mW at iso-perf",
                    "Lead with boot and sample path.",
                ),
                (
                    "How we got here + learnings",
                    "1. Phased AON clock (Option B, decided 3/20) held freeze 4/10 — paid off in clean bring-up.\n"
                    "2. Pre-silicon FPGA catch of DDR training bug avoided day-1 hang.\n"
                    "3. Shared DV farm cut regression from 18h → 6h (see benefit deck).\n\n"
                    "Keep: freeze discipline. Stop: ad-hoc board rework without ECO. Start: sample checklist owner.",
                    "Connect back to prior decisions.",
                ),
            ],
            [
                ["Next step", "Owner", "Date", "Note"],
                ["Customer sample plan (REC)", "Alex + PM", "2026-05-22", "Needs Morgan approve"],
                ["USB3 stabilize", "IO team", "2026-06-10", "Not sample-blocking"],
                ["Cold-corner AON retest", "Priya", "2026-05-25", "From tech residual"],
            ],
            "Ask: Approve customer sample plan targeting 2026-06-30 shipment to Tier-1.\n"
            "Owner: Morgan Lee endorsement; Alex executes checklist.\n"
            "By: 2026-05-22 steering (presentation date ~2026-05-16).\n\nNo HC ask here (see resource deck if sample surge).",
            "Celebrate briefly; land sample approval.",
            "First silicon day-3 boot → ask for Tier-1 sample plan approval.",
        ),
    },
    "03-management-effectiveness": {
        "template": T(
            "SCENARIO 03  ·  MANAGEMENT EFFECTIVENESS",
            "Org & people effectiveness",
            "Delivery + system health + people — for your manager 1:1 / org review",
            "BLUF — team health",
            "Delivery: GREEN/YELLOW  ·  People: …  ·  Ask: [hire / reprioritize / none]",
            "Mandate we own: [one sentence].\n\nTop outcomes this period: (1) … (2) … (3) …\n\n"
            "Top risk to the org: [single point / load / skill gap].",
            [
                (
                    "Outcomes vs commits",
                    "Commit A — Hit / Partial / Miss — evidence\nCommit B — …\nCommit C — …",
                    "Scorecard language.",
                ),
                (
                    "Capacity reality (context A)",
                    "Quarterly allocation (capacity model A):\n"
                    "• Planned outcomes ~60–70%\n• Tech investment ~15–20%\n• Unplanned ~10–15%\n\n"
                    "If HC gap: open separate context B discussion.",
                    "Do not mix B into this pie unlabeled.",
                ),
                (
                    "People & capability",
                    "Structure / critical roles / backup risk.\nSkill gaps for next horizon.\n"
                    "Hiring funnel status (if any).",
                    "No public naming/shaming.",
                ),
            ],
            [
                ["Ask type", "What changes", "If deferred"],
                ["Hire / backfill", "Close capability gap", "Descope X"],
                ["Reprioritize", "Protect Y", "Accept slip on Z"],
                ["None this cycle", "Continue plan", "—"],
            ],
            "Primary ask: …\nDecision by: …\nSupport needed from manager: air cover / intro / budget path.",
            "End with one clear ask or explicit none.",
        ),
        "example": E(
            "SCENARIO 03  ·  EXAMPLE  ·  ATLAS HEALTH",
            "Atlas Platform — Q2 org effectiveness",
            "1:1 pack for Morgan Lee — delivery green, people yellow",
            "BLUF — delivery green, capacity tight",
            "Delivery: GREEN  ·  People: YELLOW  ·  Ask: endorse +1 DV req (see resource deck)",
            "Mandate: own Aurora integration DV + first-silicon bring-up for NovaSemi connectivity SoC.\n\n"
            "Outcomes: (1) RTL freeze held 4/10 (2) day-3 boot 5/15 (3) DV farm ROI visible.\n\n"
            "Top risk: single-threaded on high-speed IO DV (Priya overloaded); backup is junior only.",
            [
                (
                    "Outcomes vs commits",
                    "Freeze-ready AON decision — Hit — Option B landed Mar 20\n"
                    "RTL freeze 4/10 — Hit — held\n"
                    "Day-5 boot target — Hit — actual day 3 (silicon 5/12)\n"
                    "USB3 bring-up complete — Partial — stable path slipped to June 10\n"
                    "Team voluntary attrition — Hit — 0 exits in Q2",
                    "Honest partial on USB3.",
                ),
                (
                    "Capacity reality (context A)",
                    "Q2 actual mix (Atlas 12 FTE):\n"
                    "• Planned Aurora outcomes ~62%\n"
                    "• Tech investment (DV farm, assertions) ~18%\n"
                    "• Unplanned (board issues, ECO-22) ~20%  ← above 10–15% plan\n\n"
                    "Unplanned overrun is why USB3 is partial — not thrash for its own sake.",
                    "Explain A vs planned; HC uses B in deck 06.",
                ),
                (
                    "People & capability",
                    "Critical path: Priya (HS IO DV) has no senior backup.\n"
                    "Mina (analog liaison) 0.5 FTE borrowed from IP team through mid-Q2.\n"
                    "Hiring: 1 req open 4 weeks — pipeline thin for senior DV.\n\n"
                    "Ask is structural, not a complaint: protect sample path with +1 DV.",
                    "Facts + ask, no blame.",
                ),
            ],
            [
                ["Ask type", "What changes", "If deferred"],
                ["+1 DV (REC)", "Backup Priya; USB3 + sample surge", "USB3 slip & burnout risk"],
                ["Reprioritize only", "Drop non-Aurora support", "Partner friction"],
                ["None", "Continue", "Accept yellow people risk"],
            ],
            "Primary ask: Endorse opening senior DV requisition (detail in resource request ~2026-05-20).\n"
            "Decision by: 2026-05-18 1:1 (after first-silicon readout).\n"
            "Air cover: restate Aurora sample > internal tool polish in Thursday steering.",
            "One ask; point to deck 06 for business case.",
            "Atlas healthy on delivery; yellow on IO DV single-thread → endorse hire.",
        ),
    },
    "04-benefit-value": {
        "template": T(
            "SCENARIO 04  ·  BENEFIT / ROI / VALUE",
            "Benefit & value case",
            "Investment → impact chain → continue / expand / stop",
            "BLUF — investment vs benefit",
            "Recommend: CONTINUE  ·  Payback sketch: ~N months (assumptions labeled)",
            "Investment: [project] cost [eng-quarters / $ example].\n"
            "Benefit realized: [metric] → [business/risk language].\nAsk: continue / expand / stop.",
            [
                (
                    "Business problem attacked",
                    "Customer / revenue / cost / risk framing.\nWhy engineering capacity was the right lever.",
                    "No jargon without translation.",
                ),
                (
                    "Impact chain",
                    "Technical result → process/behavior change → business metric.\n\n"
                    "Example: shared DV farm → regression 18h→6h → more test loops → fewer escapes.",
                    "Mark correlation vs causation.",
                ),
                (
                    "Counterfactual & what we will not claim",
                    "If we had not done this: [extra cost / delay / risk].\n\nOut of bounds claims: …",
                    "Credibility > inflated ROI.",
                ),
            ],
            [
                ["Option", "Scope", "Cost", "Expected lift"],
                ["Continue (REC)", "Steady state", "$ / capacity", "Sustain metric"],
                ["Expand", "Next module", "Higher", "Faster lift"],
                ["Stop", "Wind down", "0 new", "Accept regression risk"],
            ],
            "Decision: Continue / Expand / Stop\nOwner: …\nBy: …\nAssumptions doc link: …",
            "Land a clear portfolio decision.",
        ),
        "example": E(
            "SCENARIO 04  ·  EXAMPLE  ·  SHARED DV FARM",
            "Shared DV farm — value after 2 quarters",
            "Continue vs expand license seats for Aurora + next program",
            "BLUF — continue farm; expand +20 seats",
            "Recommend: EXPAND  ·  Payback ~5 months on avoided spin risk (assumptions labeled)",
            "Presentation window: ~2026-05-25 (after freeze 4/10 and day-3 boot 5/15).\n\n"
            "Investment: 1.5 eng-q build + $180K/yr licenses (example dollars).\n\n"
            "Benefit: regression wall-clock 18h → 6h; enabled extra sleep-exit coverage that caught AON bug pre-silicon.\n\n"
            "Ask: expand seat pool +20 for H2 multi-program use (decide by 2026-05-30).",
            [
                (
                    "Business problem attacked",
                    "Pre-farm: overnight regressions serialized Aurora + WiFi IP tests; freezes slipped when queues stacked.\n\n"
                    "Business lever: schedule integrity for tape-out and sample commits — not vanity CI.",
                    "Schedule = money on spin.",
                ),
                (
                    "Impact chain",
                    "Farm online → 3× parallel regressions → more loops per week → "
                    "DDR training bug found on FPGA+farm combo → avoided likely day-1 hang on A0.\n\n"
                    "Leading metric: median regression 6h (n=12 weeks through 2026-05-20).\n"
                    "Lagging (already realized before this deck): RTL freeze held 2026-04-10; day-3 boot 2026-05-15.",
                    "Causal language carefully: farm contributed; not sole cause.",
                ),
                (
                    "Counterfactual & what we will not claim",
                    "Without farm: estimate +2–3 weeks freeze pressure (range, not point).\n\n"
                    "Will not claim: full spin cost saved as certainty; only risk reduction with labeled assumption "
                    "($2–4M spin class, 15–25% probability avoided — planning range).",
                    "Honest envelope.",
                ),
            ],
            [
                ["Option", "Scope", "Cost", "Expected lift"],
                ["Continue only", "Current seats", "$180K/yr", "Sustain 6h median"],
                ["Expand +20 (REC)", "Aurora + next SoC", "+$60K/yr", "Queue wait −40%"],
                ["Stop / shrink", "Cut night pool", "−$40K", "Freeze risk returns"],
            ],
            "Decision: Approve Expand +20 seats for H2.\n"
            "Owner: Morgan (budget) / Alex (utilization report quarterly).\n"
            "By: 2026-05-30 finance window (after this 5/25 readout; before H2 planning).\n"
            "Assumption sheet: DOC-FARM-ROI-04.\n"
            "Note: lagging KPIs (4/10 freeze, 5/15 boot) pre-date the ask deadline.",
            "Portfolio decision with labeled assumptions.",
            "DV farm ROI → expand seats for H2 multi-program.",
        ),
    },
    "05-procurement-proposal": {
        "template": T(
            "SCENARIO 05  ·  PROCUREMENT / VENDOR / LICENSE",
            "Procurement proposal",
            "Buy / renew / switch — TCO, lead time, if-no impact",
            "BLUF — purchase decision",
            "Recommend: Vendor A  ·  Term: 3yr  ·  Decide by: [date] (lead time!)",
            "Buy: [tool/IP/cloud/service] for [use case].\n"
            "Why now: license expiry / project gate / capacity.\nIf no: [schedule or compliance impact].",
            [
                (
                    "Requirements (must / should)",
                    "Must: …\nShould: …\nSecurity / compliance / local support / export control if relevant.",
                    "Must list drives fair comparison.",
                ),
                (
                    "Implementation plan",
                    "POC → pilot → full seats.\nOwner, training, success criteria, rollback.",
                    "Adoption is part of the ask.",
                ),
            ],
            [
                ["Option", "TCO sketch", "Time-to-value", "Risk", "Fit"],
                ["Vendor A (REC)", "$…", "Fast", "Med", "High"],
                ["Vendor B", "$…", "Med", "Low", "Med"],
                ["Status quo", "0 cash", "—", "High schedule", "Low"],
            ],
            "Approve Option A and start procurement path.\n"
            "Sign-off chain: eng manager → finance → procurement.\n"
            "Decision date must include vendor lead time.",
            "Never set decide-by equal to need-by.",
        ),
        "example": E(
            "SCENARIO 05  ·  EXAMPLE  ·  SIM LICENSE RENEWAL",
            "Logic sim license renewal + expand",
            "Vendor HelixSim 3-year renewal aligned to Aurora H2 + next node",
            "BLUF — renew HelixSim 3yr +20 seats",
            "Recommend: HelixSim  ·  Term: 3yr  ·  Decide by 2026-06-05 (45-day vendor lead)",
            "Buy: HelixSim concurrent licenses for RTL/gate sim (Aurora + WiFi IP).\n\n"
            "Why now: contract ends 2026-07-31; farm expand approved path (deck 04, ask by 5/30) needs seats.\n\n"
            "If no / late: sim queue >> overnight; H2 multi-program slips (post-sample).",
            [
                (
                    "Requirements (must / should)",
                    "Must: SystemVerilog UVM; regress CLI; Asia support hours; quote ≤ budget envelope.\n"
                    "Should: cloud burst option; usage telemetry.\n"
                    "Export: standard commercial ECCN path already cleared for HelixSim.",
                    "Musts first.",
                ),
                (
                    "Implementation plan",
                    "Week 0: PO\nWeek 2–3: seat deploy on farm\nWeek 4: utilization dashboard to Alex\n\n"
                    "Success: p95 queue wait < 30 min during freeze windows.\n"
                    "Rollback: keep 10 emergency seats on prior contract short extension (costly).",
                    "Adoption metrics explicit.",
                ),
            ],
            [
                ["Option", "TCO 3yr", "Time-to-value", "Risk", "Fit"],
                ["HelixSim +20 (REC)", "$720K", "3 weeks", "Med lock-in", "High — current flow"],
                ["Switch to NovaSim", "$640K", "4–6 mo port", "High schedule", "Med"],
                ["Short extend 6 mo", "$160K", "1 week", "Revisit mid-H2", "Low strategic"],
            ],
            "Approve HelixSim 3-year +20 seats; start PO by 2026-06-05.\n"
            "Chain: Alex → Morgan → Finance → Procurement.\n"
            "Lead time: 45 days vendor — do not wait until July.",
            "Date includes lead time.",
            "Renew HelixSim with expand to match farm and freeze queues.",
        ),
    },
    "06-resource-request": {
        "template": T(
            "SCENARIO 06  ·  HEADCOUNT / BUDGET / AIR COVER",
            "Resource request",
            "Outcome-linked capacity — context B staffing math",
            "BLUF — resource ask",
            "Ask: +N [role]  ·  If no: [commit X slips]  ·  Decide by: [date]",
            "Outcome unlocked: [milestone / OKR].\n"
            "Role closes capability gap: [what nobody can do today].\n"
            "Capacity math: headcount context B — include unplanned 20–30% in demand.\n"
            "(Quarter plan still uses context A once staffed.)",
            [
                (
                    "Linked roadmap outcomes",
                    "Roadmap items blocked without capacity:\n• …\n• …\n\n"
                    "Hiring lag assumption: 3–6 months to productive.",
                    "Backwards from roadmap.",
                ),
                (
                    "If declined (explicit)",
                    "Slip / descope table:\n• Project P → next half\n• Goal G at risk",
                    "Make leadership choose trade-offs.",
                ),
            ],
            [
                ["Option", "Deliverable", "Cost", "Risk"],
                ["Full approve (REC)", "All named outcomes", "N HC / $", "Lowest schedule risk"],
                ["Partial", "Subset", "N-1", "Medium"],
                ["No hire + descope", "Cut scope", "0 HC", "Miss original commit"],
            ],
            "Decision: Full / Partial / Descope\nOpen req by: …\n"
            "Air cover needed in steering: restate priority of [initiative].",
            "Trade-off decision, not comfort request.",
        ),
        "example": E(
            "SCENARIO 06  ·  EXAMPLE  ·  +1 SENIOR DV",
            "Atlas: +1 senior DV for Aurora sample surge",
            "Context B staffing — unplanned 20–30% already burning the plan",
            "BLUF — approve 1 senior DV req",
            "Ask: +1 senior DV  ·  If no: USB3 + sample surge slip  ·  Decide by 2026-05-20 (post-silicon)",
            "Outcome unlocked: Tier-1 sample 6/30 with HS IO coverage and senior backup for Priya.\n\n"
            "Gap: high-speed IO DV is single-threaded; Q2 unplanned already ~20% (context A lookback).\n\n"
            "Headcount math (context B): demand includes 25% unplanned buffer — we are understaffed vs sample path.",
            [
                (
                    "Linked roadmap outcomes",
                    "Blocked / at risk without hire:\n"
                    "• USB3 stabilize by 6/10\n"
                    "• Sample checklist surge (board variants ×2)\n"
                    "• H2 WiFi IP integration DV kickoff\n\n"
                    "Hiring lag: target offer 6 weeks; productive ~Q3 mid — start now for H2.",
                    "Roadmap-backed.",
                ),
                (
                    "If declined (explicit)",
                    "• USB3 complete → 7/15 (misses sample polish window)\n"
                    "• Sample only on golden board (Tier-1 may reject)\n"
                    "• People risk stays yellow (deck 03)\n\n"
                    "Not a threat — a transparent trade-off for Morgan.",
                    "Explicit if-no.",
                ),
            ],
            [
                ["Option", "Deliverable", "Cost", "Risk"],
                ["Full +1 senior (REC)", "Sample + USB3 + backup", "1 HC", "Lowest"],
                ["Contractor 6 mo", "Sample surge only", "Cash / no FTE", "Knowledge leave"],
                ["No hire + descope", "Drop USB3 from sample", "0", "SKU feature miss"],
            ],
            "Decision: Approve full +1 senior DV requisition.\n"
            "Open req by: 2026-05-22 (same week as sample-plan steering).\n"
            "Air cover: in 5/22 steering, restate Aurora sample > non-Aurora support tickets.",
            "One role, crisp if-no.",
            "Single-thread IO DV → +1 senior req with explicit sample slips if no.",
        ),
    },
    "07-roadmap": {
        "template": T(
            "SCENARIO 07  ·  ROADMAP REVIEW",
            "Roadmap & planning sense",
            "Themes, capacity A, not-doing list, intake rule",
            "BLUF — plan confidence",
            "Themes T1–T3  ·  Capacity A: 60–70 / 15–20 / 10–15  ·  Decisions today: 1–2",
            "Outcomes this horizon: …\nExplicit not-doing: …\nDependencies: …\n"
            "Ask: endorse plan / choose priority call between X and Y.",
            [
                (
                    "Now / Next / Later",
                    "NOW: …\nNEXT: …\nLATER: …\n\nIC gates: RTL freeze / DV exit / Tape-out / sample as fits.",
                    "Themes over epic dumps.",
                ),
                (
                    "Capacity & assumptions (A)",
                    "Planned outcomes 60–70% | Tech investment 15–20% | Unplanned 10–15%.\n"
                    "Assumptions: headcount stable, dep dates hold, no unfunded scope.",
                    "Quote capacity-model A only.",
                ),
                (
                    "Intake rule",
                    "New work enters only if:\n1) Named priority owner, and\n"
                    "2) Displaces something, or\n3) New capacity is funded.",
                    "Teach the room the rule once.",
                ),
            ],
            [
                ["Priority call", "Keep", "Displace", "Note"],
                ["Call 1", "Theme T1", "Theme T2 slot", "Customer commit"],
                ["Call 2", "Debt tranche", "Feature Z", "Risk reduction"],
            ],
            "Endorse roadmap for Qn.\nResolve priority calls above.\nConfirm dependency owners.",
            "Leave with endorsed map.",
        ),
        "example": E(
            "SCENARIO 07  ·  EXAMPLE  ·  AURORA H2 ROADMAP",
            "Atlas H2 2026 roadmap",
            "Post-sample path: revB, WiFi IP, platform hardening",
            "BLUF — endorse H2 themes; pick sample vs WiFi priority",
            "Themes: Sample · RevB · Platform  ·  Capacity A planned  ·  Decision: sample > WiFi if conflict",
            "Outcomes H2: (1) Tier-1 sample support (2) revB dual-clock AON (3) WiFi IP integrate-or-park.\n\n"
            "Not-doing: new sensor hub SKU support; non-Aurora bring-up consulting.\n\n"
            "Ask: endorse map; if conflict, sample path outranks WiFi IP by default.",
            [
                (
                    "Now / Next / Later",
                    "NOW (through June): sample checklist (ship 6/30), USB3, cold-corner AON.\n"
                    "NEXT (Q3): revB AON dual mux; farm/seat expand; +1 DV ramp.\n"
                    "LATER (Q4): WiFi IP integration or explicit park; next-node exploration spike.\n\n"
                    "Gates: sample 6/30 · revB RTL target 9/15 · WiFi decision gate 8/01.\n"
                    "Already done earlier H1: AON B (3/20), freeze 4/10, TO 4/28, day-3 boot 5/15.",
                    "Time-ordered themes.",
                ),
                (
                    "Capacity & assumptions (A)",
                    "H2 plan (assuming +1 DV mid-Q3 productive):\n"
                    "• Outcomes ~65%\n• Investment (revB, farm) ~20%\n• Unplanned ~15%\n\n"
                    "Assumptions: HelixSim seats land; PMIC revB on time; no second silicon spin.",
                    "A only; HC already requested.",
                ),
                (
                    "Intake rule",
                    "Partner asks for non-Aurora bring-up help enter only with:\n"
                    "owner + displace (usually non-critical polish) + Alex ack.\n\n"
                    "Silent hallway commits are invalid — restate in steering.",
                    "Protect the map.",
                ),
            ],
            [
                ["Priority call", "Keep", "Displace", "Note"],
                ["Sample vs WiFi (REC sample)", "Sample path", "WiFi early integrate", "Design-win"],
                ["RevB AON vs polish", "RevB dual mux", "Nice-to-have tools", "From tech residual"],
            ],
            "Endorse Atlas H2 roadmap as shown.\n"
            "Confirm default: sample > WiFi on capacity conflict.\n"
            "Dependency owners: PMIC Ken; Package Rui; WiFi IP lead Sam.",
            "Endorsed map, not wishlist.",
            "H2 map with sample-first priority rule.",
        ),
    },
    "08-period-start-planning": {
        "template": T(
            "SCENARIO 08  ·  PERIOD START / KICKOFF",
            "Period-start planning commit",
            "Commit vs stretch vs out — shared endorsement",
            "BLUF — period commit",
            "Period goal: [1–3 outcomes]  ·  Ask: Endorse plan Option B",
            "Commit level clarity:\n• COMMIT — must hit\n• STRETCH — conditional\n• OUT — explicit not doing\n\n"
            "Resource assumptions and gaps flagged.",
            [
                (
                    "Outcomes & success metrics",
                    "Outcome 1 — metric — owner\nOutcome 2 — …\nOutcome 3 — …",
                    "Verifiable definitions of done.",
                ),
                (
                    "Milestones & working agreements",
                    "Gates / launch trains / IC freezes.\nMeeting cadence, intake, escalation path.",
                    "Operating system, not just goals.",
                ),
            ],
            [
                ["Plan option", "Scope", "Risk", "Resource need"],
                ["A Aggressive", "Max features", "High", "Needs +HC"],
                ["B Balanced (REC)", "Commit set", "Med", "Current + buffer A"],
                ["C Conservative", "Minimal", "Low", "Current"],
            ],
            "Endorse Option B for the period.\nConfirm dependency contracts.\nOpen resource path if gap remains.",
            "Shared commitment, not a wish list.",
        ),
        "example": E(
            "SCENARIO 08  ·  EXAMPLE  ·  Q3 2026 KICKOFF",
            "Atlas Q3 2026 period commit",
            "Kickoff after sample path — revB + harden",
            "BLUF — endorse balanced Q3 plan (Option B)",
            "Period goal: sample support + revB AON start  ·  Ask: Endorse Option B on 2026-07-01 kickoff",
            "COMMIT: Tier-1 sample support SLA (samples shipped 6/30); revB AON dual-mux RTL start; USB3 closed.\n"
            "STRETCH: WiFi IP bring-up spike.\n"
            "OUT: sensor hub; second customer custom board.\n\n"
            "Assumes +1 DV offer accepted by mid-July (req opened ~5/22).",
            [
                (
                    "Outcomes & success metrics",
                    "1. Sample support — critical tickets < 48h response — owner Alex\n"
                    "2. RevB AON dual mux — RTL ready review 9/15 — owner clock guild\n"
                    "3. USB3 — exit criteria signed 7/15 — owner Priya (+ new DV)\n\n"
                    "Stretch: WiFi IP smoke on FPGA — only if sample green.",
                    "Clear commit/stretch/out.",
                ),
                (
                    "Milestones & working agreements",
                    "Milestones after sample: 7/15 USB3 exit · 8/01 WiFi gate · 9/15 revB RTL review\n\n"
                    "Weekly Atlas ops Mon; steering Thu; yellow risks in BLUF form to Morgan same day.\n"
                    "Intake rule from H2 roadmap remains law.",
                    "OS + gates.",
                ),
            ],
            [
                ["Plan option", "Scope", "Risk", "Resource need"],
                ["A Aggressive", "Sample+revB+WiFi full", "High", "+1 must + contractor"],
                ["B Balanced (REC)", "Sample+revB; WiFi stretch", "Med", "+1 as planned"],
                ["C Conservative", "Sample only", "Low", "Current only"],
            ],
            "Endorse Option B for Atlas Q3 2026.\n"
            "Confirm Morgan air cover on intake rule.\n"
            "HC path: keep senior DV req on track (deck 06).",
            "Balanced commit with stretch labeled.",
            "Q3 kickoff balanced: sample+revB commit, WiFi stretch.",
        ),
    },
    "09-period-end-review": {
        "template": T(
            "SCENARIO 09  ·  PERIOD END / QBR",
            "Period-end review (QBR)",
            "Exec summary → scorecard → learnings → next ask",
            "BLUF — quarter / period status",
            "Overall: GREEN/YELLOW/RED  ·  3 wins  ·  1 carried risk  ·  Next ask: …",
            "Top outcomes with metrics.\nTop miss + disposition (not blame theater).\n"
            "Proposed next priorities (link to period-start draft).",
            [
                (
                    "Scorecard vs commits",
                    "Commit | Result | Metric | Note\n… | Hit / Partial / Miss | … | …",
                    "Answer-first QBR spine.",
                ),
                (
                    "What slipped & why",
                    "Assumption that broke: …\nOptions considered mid-period: …\nWhat we will change next period: …",
                    "Root cause → system fix.",
                ),
                (
                    "Risks into next period",
                    "Risk 1 — mitigation — owner\nRisk 2 — …\nCapacity A lookback: outcomes / debt / unplanned actuals vs plan.",
                    "Carry-forward must be owned.",
                ),
            ],
            [
                ["Next priority", "Why", "Capacity note"],
                ["P1 (REC)", "Highest leverage", "Fits A"],
                ["P2", "Strategic bet", "Needs displace"],
                ["P3", "Park", "Later"],
            ],
            "Endorse next priorities P1/P2.\nResource decision if any (see 06).\n"
            "If only three takeaways: achieved A/B; root cause of C; support D.",
            "Classic leadership QBR close.",
        ),
        "example": E(
            "SCENARIO 09  ·  EXAMPLE  ·  Q2 2026 QBR",
            "Atlas Q2 2026 QBR",
            "Leadership review — freeze, silicon, farm; people yellow carried",
            "BLUF — Q2 overall GREEN",
            "Overall: GREEN  ·  Wins: freeze 4/10, day-3 boot 5/15, farm ROI  ·  Carry: IO single-thread  ·  Ask: Q3 B + HC",
            "Q2 lookback (QBR ~2026-06-26): AON Option B (3/20); RTL freeze 4/10; TO 4/28; day-3 boot 5/15; sample plan on track 6/30.\n"
            "Miss/partial: USB3 complete (to 6/10) — capacity unplanned ~20%.\n"
            "Next: endorse Q3 balanced plan + senior DV req (opened 5/22).",
            [
                (
                    "Scorecard vs commits",
                    "AON freeze-ready decision — Hit — B approved 3/20\n"
                    "RTL freeze 4/10 — Hit\n"
                    "Day-5 boot — Hit — day 3 actual (silicon 5/12)\n"
                    "USB3 bring-up done Q2 — Partial — 6/10 forecast\n"
                    "0 attrition — Hit\n"
                    "Unplanned ≤15% — Miss — actual ~20%",
                    "Same commits as kickoff.",
                ),
                (
                    "What slipped & why",
                    "Assumption broken: unplanned load would stay ≤15%; board+ECO-22 consumed more.\n\n"
                    "Mid-Q we chose sample path over USB3 perfection (correct call).\n\n"
                    "Change Q3: +1 DV; stricter intake; unplanned budget 15% explicit in plan.",
                    "System fix, not blame.",
                ),
                (
                    "Risks into next period",
                    "1. IO DV single-thread — +1 hire / contractor bridge — Alex\n"
                    "2. Sample customer change requests — intake rule — Alex+PM\n"
                    "3. HelixSim PO timing — procurement 6/05 — Finance\n\n"
                    "Lookback A: outcomes 62% / invest 18% / unplanned 20%.",
                    "Owned carry-forward.",
                ),
            ],
            [
                ["Next priority", "Why", "Capacity note"],
                ["P1 Sample SLA (REC)", "Design-win", "Fits A with hire"],
                ["P2 RevB AON", "Tech residual", "Investment band"],
                ["P3 WiFi stretch", "Optional", "Only if P1 green"],
            ],
            "Three takeaways: freeze+boot green; unplanned drove USB3 partial; support Q3 B + DV hire.\n"
            "Endorse P1/P2; WiFi remains stretch.\n"
            "Decisions by: this QBR (~6/26) + follow-up 1:1 into Q3 kickoff 7/01.",
            "QBR classic close.",
            "Q2 green overall; carry people risk; ask Q3 plan + HC.",
        ),
    },
}
