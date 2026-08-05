#!/usr/bin/env python3
"""Generate standard upward-report PPTX templates via officecli (scenarios 01-09).

Run from repo root:
  python3 scripts/generate_report_pptx_templates.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "skills" / "presentations" / "assets" / "pptx"
OFFICECLI = Path.home() / ".local" / "bin" / "officecli"

# Midnight Executive-ish
NAVY = "1E2761"
LIGHT = "F4F7FC"
CARD = "FFFFFF"
ACCENT = "2B6CB0"
TEXT = "1A202C"
MUTED = "718096"
WHITE = "FFFFFF"
GREEN = "276749"
YELLOW = "B7791F"
RED = "C53030"


def run(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    cmd = [str(OFFICECLI), *args]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise RuntimeError(f"officecli failed ({r.returncode}): {args[:4]}...")
    return r


def batch(path: Path, commands: list[dict]) -> None:
    payload = json.dumps(commands, ensure_ascii=False)
    r = subprocess.run(
        [str(OFFICECLI), "batch", str(path), "--json"],
        input=payload,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        sys.stderr.write(r.stdout + "\n" + r.stderr)
        raise RuntimeError(f"batch failed for {path.name}")


def add_slide(title: str, bg: str = LIGHT, *, with_title: bool = True) -> dict:
    """Add a slide. with_title=False avoids the default title placeholder (use for custom layout)."""
    # Dark covers: avoid default black title placeholder (low contrast).
    if bg.upper().lstrip("#") == NAVY or not with_title:
        return {
            "command": "add",
            "path": "/",
            "type": "slide",
            "props": {"background": bg, "name": title},
        }
    return {
        "command": "add",
        "path": "/",
        "type": "slide",
        "props": {"title": title, "background": bg},
    }


def shape(
    slide: int,
    text: str,
    x: str,
    y: str,
    w: str,
    h: str,
    *,
    size: int = 18,
    bold: bool = False,
    color: str = TEXT,
    fill: str | None = None,
    font: str = "Calibri",
    align: str | None = None,
) -> dict:
    props = {
        "text": text,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "size": str(size),
        "font": font,
        "color": color,
        "bold": "true" if bold else "false",
    }
    if fill:
        props["fill"] = fill
    if align:
        props["align"] = align
    return {
        "command": "add",
        "path": f"/slide[{slide}]",
        "type": "shape",
        "props": props,
    }


def notes(slide: int, text: str) -> dict:
    return {
        "command": "add",
        "path": f"/slide[{slide}]",
        "type": "notes",
        "props": {"text": text},
    }


def table(
    slide: int,
    rows: int,
    cols: int,
    data: list[list[str]],
    x: str,
    y: str,
    w: str,
    h: str,
) -> list[dict]:
    """Add table then set cells. data is row-major including header."""
    cmds: list[dict] = [
        {
            "command": "add",
            "path": f"/slide[{slide}]",
            "type": "table",
            "props": {
                "rows": str(rows),
                "cols": str(cols),
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "headerFill": NAVY,
                "bodyFill": CARD,
                "firstRow": "true",
            },
        }
    ]
    # Cell set after table exists — use path /slide[N]/table[1]/tr[r]/tc[c]
    for ri, row in enumerate(data, start=1):
        for ci, val in enumerate(row, start=1):
            color = WHITE if ri == 1 else TEXT
            bold = "true" if ri == 1 else "false"
            size = "14" if ri == 1 else "13"
            cmds.append(
                {
                    "command": "set",
                    "path": f"/slide[{slide}]/table[1]/tr[{ri}]/tc[{ci}]",
                    "props": {
                        "text": val,
                        "color": color,
                        "bold": bold,
                        "size": size,
                        "font": "Calibri",
                    },
                }
            )
    return cmds


def deck_shell(path: Path) -> None:
    if path.exists():
        path.unlink()
    run(["create", str(path)])


def build_generic(
    path: Path,
    *,
    kicker: str,
    title: str,
    subtitle: str,
    bluf_title: str,
    bluf_body: str,
    bluf_status: str,
    body_slides: list[tuple[str, str, str]],  # title, body, notes
    options_table: list[list[str]] | None,
    ask_lines: str,
    ask_notes: str,
) -> None:
    deck_shell(path)
    cmds: list[dict] = []

    # Slide 1 cover
    cmds.append(add_slide(title, NAVY))
    cmds += [
        shape(1, kicker, "1.5cm", "3.0cm", "30cm", "1cm", size=16, color="CADCFC", bold=True),
        shape(1, title, "1.5cm", "4.3cm", "30cm", "2.8cm", size=36, color=WHITE, bold=True),
        shape(1, subtitle, "1.5cm", "7.5cm", "30cm", "2.2cm", size=18, color="CADCFC"),
        shape(
            1,
            "Team X  ·  Program Alpha  ·  Qn YYYY  ·  TEMPLATE — replace placeholders",
            "1.5cm",
            "16.8cm",
            "30cm",
            "1.2cm",
            size=13,
            color="A0AEC0",
        ),
        notes(1, f"Cover for {title}. State purpose in 10 seconds."),
    ]

    # Slide 2 BLUF — no default title placeholder (it collided with kicker at y≈1.5cm)
    cmds.append(add_slide(bluf_title, LIGHT, with_title=False))
    cmds += [
        shape(2, bluf_title, "1.5cm", "1.2cm", "30.5cm", "2.0cm", size=32, color=TEXT, bold=True),
        shape(2, "BOTTOM LINE UP FRONT", "1.5cm", "3.3cm", "16cm", "0.85cm", size=12, color=ACCENT, bold=True),
        shape(2, bluf_status, "1.5cm", "4.2cm", "30.5cm", "1.6cm", size=18, color=WHITE, bold=True, fill=NAVY),
        shape(2, bluf_body, "1.5cm", "6.1cm", "30.5cm", "11.2cm", size=17, color=TEXT, fill=CARD),
        notes(2, "Read BLUF first. Do not walk chronology before the ask is clear."),
    ]

    # Body slides
    s = 3
    for bt, body, ntxt in body_slides:
        cmds.append(add_slide(bt, LIGHT))
        cmds += [
            shape(s, body, "1.5cm", "4.0cm", "30.5cm", "13cm", size=18, color=TEXT, fill=CARD),
            notes(s, ntxt),
        ]
        s += 1

    # Options
    if options_table:
        cmds.append(add_slide("Options & recommendation", LIGHT))
        cmds += [
            shape(
                s,
                "Compare paths; recommendation is bold in the table. Decision owner must pick by the date on the Ask slide.",
                "1.5cm",
                "3.9cm",
                "30.5cm",
                "1.3cm",
                size=14,
                color=MUTED,
            ),
        ]
        cmds += table(s, len(options_table), len(options_table[0]), options_table, "1.5cm", "5.4cm", "30.5cm", "10cm")
        cmds.append(notes(s, "Walk trade-offs; land on recommendation. Avoid re-deriving analysis aloud."))
        s += 1

    # Ask
    cmds.append(add_slide("Decision & ask", LIGHT))
    cmds += [
        shape(
            s,
            "WHAT WE NEED FROM THIS ROOM",
            "1.5cm",
            "3.9cm",
            "30.5cm",
            "0.8cm",
            size=12,
            color=ACCENT,
            bold=True,
        ),
        shape(s, ask_lines, "1.5cm", "4.9cm", "30.5cm", "11cm", size=18, color=TEXT, fill=CARD),
        notes(s, ask_notes),
    ]

    batch(path, cmds)
    run(["close", str(path)], check=False)


def main() -> int:
    if not OFFICECLI.is_file():
        print("officecli not found at", OFFICECLI, file=sys.stderr)
        return 1
    OUT.mkdir(parents=True, exist_ok=True)

    decks: list[tuple[str, callable]] = []

    def d01():
        build_generic(
            OUT / "01-technical-review.pptx",
            kicker="SCENARIO 01  ·  DESIGN / TECH REVIEW",
            title="Technical review: decision package",
            subtitle="Architecture / design freeze / major change — options before deep walkthrough",
            bluf_title="BLUF — decision needed",
            bluf_status="Status: YELLOW  ·  Decision: Approve Option B (phased) by Friday",
            bluf_body=(
                "Goal: ship Program Alpha milestone without silent risk acceptance.\n\n"
                "Difficulty: [constraint — e.g. interface freeze / PPA / schedule].\n\n"
                "Recommendation: Option B — phased rollout with feature flags / limited cohort.\n\n"
                "If no decision: default equals Option C (do nothing) with accepted risk documented."
            ),
            body_slides=[
                (
                    "Problem, goal, constraints",
                    "Problem: [who is hurt / what fails].\n\n"
                    "Success looks like: [measurable exit criteria].\n\n"
                    "Constraints: schedule gate  |  PPA or SLO  |  capacity  |  dependency (IP / platform / team).\n\n"
                    "IC note: map to Arch → RTL freeze → DV exit → Tape-out as applicable.",
                    "State constraints before solution. Do not open with micro-architecture.",
                ),
                (
                    "Design sketch (one page)",
                    "Keep one block diagram or interface table here.\n\n"
                    "• Boundary / responsibility\n"
                    "• Data or signal path at a glance\n"
                    "• What is explicitly out of scope this review\n\n"
                    "Details → backup annex if asked.",
                    "One visual idea. Offer deep-dive only on request.",
                ),
                (
                    "Risks & mitigations (top 3)",
                    "1. [Risk] — mitigation: … — owner: …\n"
                    "2. [Risk] — mitigation: … — owner: …\n"
                    "3. [Risk] — mitigation: … — owner: …\n\n"
                    "Residual risk after recommendation: [one sentence].",
                    "Every risk needs owner. Residual risk must be explicit.",
                ),
            ],
            options_table=[
                ["Option", "Outcome", "Schedule", "Risk", "Capacity"],
                ["A Fast", "Full scope now", "On date", "High", "Low extra"],
                ["B Phased (REC)", "Core first", "+1 gate buffer", "Med", "Med"],
                ["C Do nothing", "Status quo", "—", "Accepted", "—"],
            ],
            ask_lines=(
                "Decision: Approve B / A / C\n"
                "Owner: [Name / role]\n"
                "By: [date]\n\n"
                "Follow-ups: update design doc; notify dependent teams; schedule next gate."
            ),
            ask_notes="Close with decision sentence. Capture owner and date live.",
        )

    def d02():
        build_generic(
            OUT / "02-results-demo.pptx",
            kicker="SCENARIO 02  ·  RESULTS / DEMO / LAUNCH",
            title="Results readout",
            subtitle="What shipped, vs commitment, why it mattered — not a sprint diary",
            bluf_title="BLUF — result & impact",
            bluf_status="Status: GREEN  ·  Result: [X] delivered on [date]  ·  Ask: none / next-phase approve",
            bluf_body=(
                "Outcome: [one line].\n"
                "Impact: [metric baseline → actual].\n"
                "Linked OKR / program goal: [one line].\n\n"
                "Residual risk or follow-ups: [or none]."
            ),
            body_slides=[
                (
                    "Goal recall (period start)",
                    "Original commit: [promise].\n"
                    "Success metric: target [T].\n\n"
                    "Avoid moving the goalposts — show the same definition of done.",
                    "Re-anchor to original commitment first.",
                ),
                (
                    "Outcome metrics",
                    "Metric A: target … / actual … / Δ …\n"
                    "Metric B: …\n\n"
                    "IC examples: power −N% at iso-perf; bring-up day-k boot; coverage gate met.\n"
                    "SW examples: p95 latency; adoption %; change-fail rate.",
                    "Few metrics, high signal. Label data as-of date.",
                ),
                (
                    "How we got here + learnings",
                    "Three decisions that mattered:\n1. …\n2. …\n3. …\n\n"
                    "Keep / stop / start (one each).",
                    "Process insight only if it changes next quarter behavior.",
                ),
            ],
            options_table=None,
            ask_lines=(
                "Ask: [visibility only / approve next phase / fund follow-on]\n"
                "Or: No decision required — FYI readout.\n\n"
                "Next milestone: [date + gate]."
            ),
            ask_notes="If pure celebration, still name residual risk.",
        )

    def d03():
        build_generic(
            OUT / "03-management-effectiveness.pptx",
            kicker="SCENARIO 03  ·  MANAGEMENT EFFECTIVENESS",
            title="Org & people effectiveness",
            subtitle="Delivery + system health + people — for your manager 1:1 / org review",
            bluf_title="BLUF — team health",
            bluf_status="Delivery: GREEN/YELLOW  ·  People: …  ·  Ask: [hire / reprioritize / none]",
            bluf_body=(
                "Mandate we own: [one sentence].\n\n"
                "Top outcomes this period: (1) … (2) … (3) …\n\n"
                "Top risk to the org: [single point / load / skill gap]."
            ),
            body_slides=[
                (
                    "Outcomes vs commits",
                    "Commit A — Hit / Partial / Miss — evidence\n"
                    "Commit B — …\n"
                    "Commit C — …",
                    "Scorecard language, not ceremony counts.",
                ),
                (
                    "Capacity reality (context A)",
                    "Quarterly allocation (capacity model A):\n"
                    "• Planned outcomes ~60–70%\n"
                    "• Tech investment ~15–20%\n"
                    "• Unplanned ~10–15%\n\n"
                    "If HC gap: open separate context B discussion (see resource template).",
                    "Do not mix headcount math into this pie without labeling B.",
                ),
                (
                    "People & capability",
                    "Structure / critical roles / backup risk.\n"
                    "Skill gaps for next horizon.\n"
                    "Hiring funnel status (if any).\n\n"
                    "No public naming/shaming — facts and asks only.",
                    "People issues go deep offline if sensitive.",
                ),
            ],
            options_table=[
                ["Ask type", "What changes", "If deferred"],
                ["Hire / backfill", "Close capability gap", "Descope X"],
                ["Reprioritize", "Protect Y", "Accept slip on Z"],
                ["None this cycle", "Continue plan", "—"],
            ],
            ask_lines=(
                "Primary ask: …\n"
                "Decision by: …\n"
                "Support needed from manager: air cover / intro / budget path."
            ),
            ask_notes="End with one clear ask or explicit none.",
        )

    def d04():
        build_generic(
            OUT / "04-benefit-value.pptx",
            kicker="SCENARIO 04  ·  BENEFIT / ROI / VALUE",
            title="Benefit & value case",
            subtitle="Investment → impact chain → continue / expand / stop",
            bluf_title="BLUF — investment vs benefit",
            bluf_status="Recommend: CONTINUE  ·  Payback sketch: ~N months (assumptions labeled)",
            bluf_body=(
                "Investment: [project] cost [eng-quarters / $ example].\n"
                "Benefit realized: [metric] → [business/risk language].\n"
                "Ask: continue / expand / stop."
            ),
            body_slides=[
                (
                    "Business problem attacked",
                    "Customer / revenue / cost / risk framing.\n"
                    "Why engineering capacity was the right lever.",
                    "No jargon without translation.",
                ),
                (
                    "Impact chain",
                    "Technical result → process/behavior change → business metric.\n\n"
                    "Example: shared DV farm → regression 18h→6h → more test loops → fewer escapes → lower spin risk.",
                    "Mark correlation vs causation honestly.",
                ),
                (
                    "Counterfactual & what we will not claim",
                    "If we had not done this: [extra cost / delay / risk].\n\n"
                    "Out of bounds claims (do not oversell): …",
                    "Credibility > inflated ROI.",
                ),
            ],
            options_table=[
                ["Option", "Scope", "Cost", "Expected lift"],
                ["Continue (REC)", "Steady state", "$ / capacity", "Sustain metric"],
                ["Expand", "Next module", "Higher", "Faster lift"],
                ["Stop", "Wind down", "0 new", "Accept regression risk"],
            ],
            ask_lines="Decision: Continue / Expand / Stop\nOwner: …\nBy: …\nAssumptions doc link: …",
            ask_notes="Land a clear portfolio decision.",
        )

    def d05():
        build_generic(
            OUT / "05-procurement-proposal.pptx",
            kicker="SCENARIO 05  ·  PROCUREMENT / VENDOR / LICENSE",
            title="Procurement proposal",
            subtitle="Buy / renew / switch — TCO, lead time, if-no impact",
            bluf_title="BLUF — purchase decision",
            bluf_status="Recommend: Vendor A  ·  Term: 3yr  ·  Decide by: [date] (lead time!)",
            bluf_body=(
                "Buy: [tool/IP/cloud/service] for [use case].\n"
                "Why now: license expiry / project gate / capacity.\n"
                "If no: [schedule or compliance impact]."
            ),
            body_slides=[
                (
                    "Requirements (must / should)",
                    "Must: …\nShould: …\n"
                    "Security / compliance / local support / export control if relevant.",
                    "Must list drives fair comparison.",
                ),
                (
                    "Implementation plan",
                    "POC → pilot → full seats.\n"
                    "Owner, training, success criteria, rollback.",
                    "Adoption is part of the ask.",
                ),
            ],
            options_table=[
                ["Option", "TCO sketch", "Time-to-value", "Risk", "Fit"],
                ["Vendor A (REC)", "$…", "Fast", "Med", "High"],
                ["Vendor B", "$…", "Med", "Low", "Med"],
                ["Status quo", "0 cash", "—", "High schedule", "Low"],
            ],
            ask_lines=(
                "Approve Option A and start procurement path.\n"
                "Sign-off chain: eng manager → finance → procurement.\n"
                "Decision date must include vendor lead time."
            ),
            ask_notes="Never set decide-by equal to need-by.",
        )

    def d06():
        build_generic(
            OUT / "06-resource-request.pptx",
            kicker="SCENARIO 06  ·  HEADCOUNT / BUDGET / AIR COVER",
            title="Resource request",
            subtitle="Outcome-linked capacity — context B staffing math",
            bluf_title="BLUF — resource ask",
            bluf_status="Ask: +N [role]  ·  If no: [commit X slips]  ·  Decide by: [date]",
            bluf_body=(
                "Outcome unlocked: [milestone / OKR].\n"
                "Role closes capability gap: [what nobody can do today].\n"
                "Capacity math: headcount context B — include unplanned 20–30% in demand.\n"
                "(Quarter plan still uses context A once staffed.)"
            ),
            body_slides=[
                (
                    "Linked roadmap outcomes",
                    "Roadmap items blocked without capacity:\n• …\n• …\n\n"
                    "Hiring lag assumption: 3–6 months to productive (adjust to market).",
                    "Backwards from roadmap, not from busyness.",
                ),
                (
                    "If declined (explicit)",
                    "Slip / descope table:\n"
                    "• Project P → next half\n"
                    "• Goal G at risk\n"
                    "• Sustainability signal (facts only)",
                    "Make leadership choose trade-offs.",
                ),
            ],
            options_table=[
                ["Option", "Deliverable", "Cost", "Risk"],
                ["Full approve (REC)", "All named outcomes", "N HC / $", "Lowest schedule risk"],
                ["Partial", "Subset", "N-1", "Medium"],
                ["No hire + descope", "Cut scope", "0 HC", "Miss original commit"],
            ],
            ask_lines=(
                "Decision: Full / Partial / Descope\n"
                "Open req by: …\n"
                "Air cover needed in steering: restate priority of [initiative]."
            ),
            ask_notes="This is a trade-off decision, not a comfort request.",
        )

    def d07():
        build_generic(
            OUT / "07-roadmap.pptx",
            kicker="SCENARIO 07  ·  ROADMAP REVIEW",
            title="Roadmap & planning sense",
            subtitle="Themes, capacity A, not-doing list, intake rule",
            bluf_title="BLUF — plan confidence",
            bluf_status="Themes T1–T3  ·  Capacity A: 60–70 / 15–20 / 10–15  ·  Decisions today: 1–2",
            bluf_body=(
                "Outcomes this horizon: …\n"
                "Explicit not-doing: …\n"
                "Dependencies: …\n"
                "Ask: endorse plan / choose priority call between X and Y."
            ),
            body_slides=[
                (
                    "Now / Next / Later",
                    "NOW: …\nNEXT: …\nLATER: …\n\n"
                    "IC gates on timeline: RTL freeze / DV exit / Tape-out / sample as fits.",
                    "Themes over epic dumps.",
                ),
                (
                    "Capacity & assumptions (A)",
                    "Planned outcomes 60–70% | Tech investment 15–20% | Unplanned 10–15%.\n"
                    "Assumptions: headcount stable, dep dates hold, no unfunded scope.\n"
                    "When assumption breaks → options, not silent heroics.",
                    "Quote capacity-model context A only.",
                ),
                (
                    "Intake rule",
                    "New work enters only if:\n"
                    "1) Named priority owner, and\n"
                    "2) Displaces something, or\n"
                    "3) New capacity is funded.\n\n"
                    "No silent squeeze.",
                    "Teach the room the rule once.",
                ),
            ],
            options_table=[
                ["Priority call", "Keep", "Displace", "Note"],
                ["Call 1", "Theme T1", "Theme T2 slot", "Customer commit"],
                ["Call 2", "Debt tranche", "Feature Z", "Risk reduction"],
            ],
            ask_lines="Endorse roadmap for Qn.\nResolve priority calls above.\nConfirm dependency owners.",
            ask_notes="Leave with endorsed map, not a wish list.",
        )

    def d08():
        build_generic(
            OUT / "08-period-start-planning.pptx",
            kicker="SCENARIO 08  ·  PERIOD START / KICKOFF",
            title="Period-start planning commit",
            subtitle="Commit vs stretch vs out — shared endorsement",
            bluf_title="BLUF — period commit",
            bluf_status="Period goal: [1–3 outcomes]  ·  Ask: Endorse plan Option B",
            bluf_body=(
                "Commit level clarity:\n"
                "• COMMIT — must hit\n"
                "• STRETCH — conditional\n"
                "• OUT — explicit not doing\n\n"
                "Resource assumptions and gaps flagged."
            ),
            body_slides=[
                (
                    "Outcomes & success metrics",
                    "Outcome 1 — metric — owner\n"
                    "Outcome 2 — …\n"
                    "Outcome 3 — …",
                    "Verifiable definitions of done.",
                ),
                (
                    "Milestones & working agreements",
                    "Gates / launch trains / IC freezes.\n"
                    "Meeting cadence, intake, escalation path.\n"
                    "How yellow becomes visible early.",
                    "Operating system, not just goals.",
                ),
            ],
            options_table=[
                ["Plan option", "Scope", "Risk", "Resource need"],
                ["A Aggressive", "Max features", "High", "Needs +HC"],
                ["B Balanced (REC)", "Commit set", "Med", "Current + buffer A"],
                ["C Conservative", "Minimal", "Low", "Current"],
            ],
            ask_lines="Endorse Option B for the period.\nConfirm dependency contracts.\nOpen resource path if gap remains.",
            ask_notes="Shared commitment, not a wish list.",
        )

    def d09():
        build_generic(
            OUT / "09-period-end-review.pptx",
            kicker="SCENARIO 09  ·  PERIOD END / QBR",
            title="Period-end review (QBR)",
            subtitle="Exec summary → scorecard → learnings → next ask",
            bluf_title="BLUF — quarter / period status",
            bluf_status="Overall: GREEN/YELLOW/RED  ·  3 wins  ·  1 carried risk  ·  Next ask: …",
            bluf_body=(
                "Top outcomes with metrics.\n"
                "Top miss + disposition (not blame theater).\n"
                "Proposed next priorities (link to period-start draft)."
            ),
            body_slides=[
                (
                    "Scorecard vs commits",
                    "Commit | Result | Metric | Note\n"
                    "… | Hit / Partial / Miss | … | …\n\n"
                    "Use the same commits frozen at period start.",
                    "Answer-first QBR spine.",
                ),
                (
                    "What slipped & why",
                    "Assumption that broke: …\n"
                    "Options considered mid-period: …\n"
                    "What we will change next period: …",
                    "Root cause → system fix.",
                ),
                (
                    "Risks into next period",
                    "Risk 1 — mitigation — owner\n"
                    "Risk 2 — …\n"
                    "Capacity A lookback: outcomes / debt / unplanned actuals vs plan.",
                    "Carry-forward must be owned.",
                ),
            ],
            options_table=[
                ["Next priority", "Why", "Capacity note"],
                ["P1 (REC)", "Highest leverage", "Fits A"],
                ["P2", "Strategic bet", "Needs displace"],
                ["P3", "Park", "Later"],
            ],
            ask_lines=(
                "Endorse next priorities P1/P2.\n"
                "Resource decision if any (see 06).\n"
                "If only three takeaways: achieved A/B; root cause of C; support D."
            ),
            ask_notes="Classic leadership QBR close.",
        )

    for name, fn in [
        ("01", d01),
        ("02", d02),
        ("03", d03),
        ("04", d04),
        ("05", d05),
        ("06", d06),
        ("07", d07),
        ("08", d08),
        ("09", d09),
    ]:
        print(f"Building {name}...")
        fn()
        p = next(OUT.glob(f"{name}-*.pptx"))
        v = run(["validate", str(p)])
        print(v.stdout.strip() or "validate ok", p.name)

    print("Done. Assets in", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
