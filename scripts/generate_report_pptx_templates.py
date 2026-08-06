#!/usr/bin/env python3
"""Generate optimized report PPTX templates + filled scenario examples via officecli.

Usage (repo root):
  python3 scripts/generate_report_pptx_templates.py
  python3 scripts/generate_report_pptx_templates.py --only 01-technical-review
  python3 scripts/generate_report_pptx_templates.py --kind example
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pptx_deck_data import (  # noqa: E402
    EXAMPLE_SITUATIONS,
    SCENARIOS,
    SCENARIO_PATTERNS,
)
OUT_ROOT = ROOT / "skills" / "presentations" / "assets" / "pptx"
OFFICECLI = Path.home() / ".local" / "bin" / "officecli"

# Layout tokens (widescreen 33.87 × 19.05 cm)
NAVY = "1E2761"
LIGHT = "F4F7FC"
CARD = "FFFFFF"
ACCENT = "2B6CB0"
TEXT = "1A202C"
MUTED = "718096"
WHITE = "FFFFFF"
MARGIN = "1.4cm"
CONTENT_W = "30.8cm"


def run(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    r = subprocess.run([str(OFFICECLI), *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise RuntimeError(f"officecli failed: {args[:5]}")
    return r


def batch(path: Path, commands: list[dict]) -> None:
    r = subprocess.run(
        [str(OFFICECLI), "batch", str(path), "--json"],
        input=json.dumps(commands, ensure_ascii=False),
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        sys.stderr.write(r.stdout + "\n" + r.stderr)
        raise RuntimeError(f"batch failed for {path.name}")


def add_slide(name: str, bg: str = LIGHT) -> dict:
    """Blank content slide (no default title placeholder — avoids kicker collisions)."""
    return {
        "command": "add",
        "path": "/",
        "type": "slide",
        "props": {"background": bg, "name": name},
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
    return {"command": "add", "path": f"/slide[{slide}]", "type": "shape", "props": props}


def notes(slide: int, text: str) -> dict:
    return {"command": "add", "path": f"/slide[{slide}]", "type": "notes", "props": {"text": text}}


def footer(slide: int, text: str) -> dict:
    return shape(slide, text, MARGIN, "17.85cm", CONTENT_W, "0.85cm", size=11, color=MUTED)


def title_block(slide: int, title: str, eyebrow: str | None = None) -> list[dict]:
    """Title band: optional eyebrow above, main title below — never overlap."""
    cmds = []
    if eyebrow:
        cmds.append(
            shape(slide, eyebrow, MARGIN, "0.75cm", CONTENT_W, "0.75cm", size=11, color=ACCENT, bold=True)
        )
        cmds.append(shape(slide, title, MARGIN, "1.55cm", CONTENT_W, "1.7cm", size=28, color=TEXT, bold=True))
    else:
        cmds.append(shape(slide, title, MARGIN, "1.1cm", CONTENT_W, "1.9cm", size=30, color=TEXT, bold=True))
    return cmds


def table_cmds(slide: int, data: list[list[str]], y: str = "5.2cm", h: str = "9.5cm") -> list[dict]:
    rows, cols = len(data), len(data[0])
    cmds: list[dict] = [
        {
            "command": "add",
            "path": f"/slide[{slide}]",
            "type": "table",
            "props": {
                "rows": str(rows),
                "cols": str(cols),
                "x": MARGIN,
                "y": y,
                "width": CONTENT_W,
                "height": h,
                "headerFill": NAVY,
                "bodyFill": CARD,
                "firstRow": "true",
            },
        }
    ]
    for ri, row in enumerate(data, start=1):
        for ci, val in enumerate(row, start=1):
            cmds.append(
                {
                    "command": "set",
                    "path": f"/slide[{slide}]/table[1]/tr[{ri}]/tc[{ci}]",
                    "props": {
                        "text": val,
                        "color": WHITE if ri == 1 else TEXT,
                        "bold": "true" if ri == 1 else "false",
                        "size": "13" if ri == 1 else "12",
                        "font": "Calibri",
                    },
                }
            )
    return cmds


def deck_shell(path: Path) -> None:
    if path.exists():
        path.unlink()
    run(["create", str(path)])


def build_deck(path: Path, pack: dict) -> None:
    deck_shell(path)
    cmds: list[dict] = []
    kind = pack.get("kind", "template")
    # Badge = content role only (not a visual design system)
    badge = "CONTENT-EXAMPLE" if kind == "example" else "CONTENT-TEMPLATE"
    pattern = pack.get("pattern") or {}
    plabel = pattern.get("label") or "See classic-public-cases.md"
    psources = pattern.get("sources") or []
    pattern_body = f"Public pattern (structure only — not a confidential company deck):\n\n{plabel}\n\n"
    for title, url in psources:
        pattern_body += f"• {title}\n  {url}\n"
    pattern_body += (
        "\nHow to use: copy section order and decision verbs; replace with your metrics.\n"
        "CONTENT TEMPLATE ONLY (內容模板) — NOT default visual design / 不是預設美工排版.\n"
        "Learn: BLUF, stakes, options, REC, deadlines, story arc.\n"
        "Do NOT copy: colors, margins, fonts, coordinates, decorative chrome.\n"
        "Real decks: use your company master; migrate content structure only.\n"
        "In-repo: skills/presentations/classic-public-cases.md · assets/README.md (agent notice)"
    )
    pattern_notes = plabel + "\n" + "\n".join(f"{t}: {u}" for t, u in psources)

    s = 0

    def next_slide(name: str, bg: str = LIGHT) -> int:
        nonlocal s
        s += 1
        cmds.append(add_slide(name, bg))
        return s

    # --- Cover ---
    i = next_slide(pack["title"], NAVY)
    cmds += [
        shape(i, pack["kicker"], MARGIN, "2.6cm", CONTENT_W, "0.85cm", size=14, color="CADCFC", bold=True),
        shape(i, pack["title"], MARGIN, "3.7cm", CONTENT_W, "2.5cm", size=32, color=WHITE, bold=True),
        shape(i, pack["subtitle"], MARGIN, "6.5cm", CONTENT_W, "1.8cm", size=16, color="CADCFC"),
        shape(i, f"Pattern: {plabel}", MARGIN, "9.0cm", CONTENT_W, "1.6cm", size=14, color="A0C4E8"),
        shape(i, f"{badge}  ·  {pack['meta']}", MARGIN, "16.6cm", CONTENT_W, "1.1cm", size=12, color="A0AEC0"),
        notes(i, f"Cover ({kind}). {pack.get('story', pack['title'])}\n\n{pattern_notes}"),
    ]

    # --- Pattern provenance ---
    i = next_slide("Pattern provenance", LIGHT)
    cmds += title_block(i, "Pattern provenance", "WHERE THIS DECK SHAPE COMES FROM")
    cmds += [
        shape(i, pattern_body, MARGIN, "3.5cm", CONTENT_W, "13.5cm", size=15, color=TEXT, fill=CARD),
        footer(i, pack["meta"]),
        notes(i, pattern_notes),
    ]

    # --- Situation card (examples only) — cold reader / agent parse ---
    sit = pack.get("situation") or {}
    if kind == "example" and sit:
        sit_body = (
            f"Presenter: {sit.get('presenter', '—')}\n"
            f"Decision-maker: {sit.get('decision_maker', '—')}\n"
            f"Audience: {sit.get('audience', '—')}\n\n"
            f"What just happened / context:\n{sit.get('what_happened', '—')}\n\n"
            f"Stakes if we get this wrong:\n{sit.get('stakes', '—')}\n\n"
            f"Decision needed:\n{sit.get('decision', '—')}\n\n"
            f"Recommendation: {sit.get('recommend', '—')}\n"
            f"If YES: {sit.get('if_yes', '—')}\n"
            f"If NO / delay: {sit.get('if_no_or_delay', '—')}\n\n"
            f"Decide by: {sit.get('decide_by', '—')}\n"
            f"Arc prior: {sit.get('prior_arc', '—')}\n"
            f"Arc next: {sit.get('next_arc', '—')}"
        )
        i = next_slide("Situation & decision card", LIGHT)
        cmds += title_block(i, "Situation & decision card", "READ THIS BEFORE THE DETAILS")
        cmds += [
            shape(i, sit_body, MARGIN, "3.4cm", CONTENT_W, "13.8cm", size=13, color=TEXT, fill=CARD),
            footer(i, pack["meta"]),
            notes(
                i,
                "Agent/human: answer who/stakes/decision from this slide alone. "
                f"Recommend={sit.get('recommend', '')} by {sit.get('decide_by', '')}.",
            ),
        ]

    # --- BLUF ---
    i = next_slide(pack["bluf_title"], LIGHT)
    cmds += title_block(i, pack["bluf_title"], "BOTTOM LINE UP FRONT")
    cmds += [
        shape(i, pack["bluf_status"], MARGIN, "3.5cm", CONTENT_W, "1.75cm", size=14, color=WHITE, bold=True, fill=NAVY),
        shape(i, pack["bluf_body"], MARGIN, "5.5cm", CONTENT_W, "11.7cm", size=16, color=TEXT, fill=CARD),
        footer(i, pack["meta"]),
        notes(i, pack.get("ask_notes", "Lead with BLUF.")),
    ]

    # --- Body ---
    for bt, body, ntxt in pack["body_slides"]:
        i = next_slide(bt, LIGHT)
        cmds += title_block(i, bt)
        cmds += [
            shape(i, body, MARGIN, "3.5cm", CONTENT_W, "13.5cm", size=16, color=TEXT, fill=CARD),
            footer(i, pack["meta"]),
            notes(i, ntxt),
        ]

    # --- Options ---
    if pack.get("options_table"):
        i = next_slide("Options & recommendation", LIGHT)
        cmds += title_block(i, "Options & recommendation")
        cmds += [
            shape(
                i,
                "Compare paths; recommendation is marked REC. Decision owner picks by the date on the Ask slide.",
                MARGIN,
                "3.4cm",
                CONTENT_W,
                "1.1cm",
                size=13,
                color=MUTED,
            ),
        ]
        cmds += table_cmds(i, pack["options_table"], y="4.7cm", h="11.5cm")
        cmds += [footer(i, pack["meta"]), notes(i, "Walk trade-offs; land recommendation.")]

    # --- Ask ---
    i = next_slide("Decision & ask", LIGHT)
    cmds += title_block(i, "Decision & ask", "WHAT WE NEED FROM THIS ROOM")
    cmds += [
        shape(i, pack["ask_lines"], MARGIN, "3.5cm", CONTENT_W, "13.5cm", size=17, color=TEXT, fill=CARD),
        footer(i, pack["meta"]),
        notes(i, pack.get("ask_notes", "Close with owner + date.")),
    ]

    batch(path, cmds)
    run(["close", str(path)], check=False)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="Scenario key substring, e.g. 01-technical")
    ap.add_argument("--kind", choices=["template", "example", "both"], default="both")
    args = ap.parse_args()

    if not OFFICECLI.is_file():
        print("officecli not found", OFFICECLI, file=sys.stderr)
        return 1

    tpl_dir = OUT_ROOT / "templates"
    ex_dir = OUT_ROOT / "examples"
    tpl_dir.mkdir(parents=True, exist_ok=True)
    ex_dir.mkdir(parents=True, exist_ok=True)

    # Remove legacy flat pptx at OUT_ROOT root to avoid confusion
    for legacy in OUT_ROOT.glob("*.pptx"):
        legacy.unlink()

    keys = sorted(SCENARIOS.keys())
    if args.only:
        keys = [k for k in keys if args.only in k]
        if not keys:
            print("no match", args.only, file=sys.stderr)
            return 1

    for key in keys:
        packs = SCENARIOS[key]
        pattern = SCENARIO_PATTERNS.get(key) or packs.get("pattern") or {}
        if args.kind in ("template", "both"):
            path = tpl_dir / f"{key}.pptx"
            print("template", path.name)
            build_deck(path, {**packs["template"], "pattern": pattern})
            run(["validate", str(path)])
        if args.kind in ("example", "both"):
            path = ex_dir / f"{key}.pptx"
            print("example ", path.name)
            sit = EXAMPLE_SITUATIONS.get(key) or {}
            build_deck(path, {**packs["example"], "pattern": pattern, "situation": sit})
            run(["validate", str(path)])

    print("Done →", tpl_dir, "and", ex_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
