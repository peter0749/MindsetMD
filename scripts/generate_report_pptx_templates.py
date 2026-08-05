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
from pptx_deck_data import SCENARIOS  # noqa: E402
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
    badge = "EXAMPLE" if kind == "example" else "TEMPLATE"

    # --- 1 Cover ---
    cmds.append(add_slide(pack["title"], NAVY))
    cmds += [
        shape(1, pack["kicker"], MARGIN, "2.8cm", CONTENT_W, "0.9cm", size=14, color="CADCFC", bold=True),
        shape(1, pack["title"], MARGIN, "4.0cm", CONTENT_W, "2.6cm", size=34, color=WHITE, bold=True),
        shape(1, pack["subtitle"], MARGIN, "7.0cm", CONTENT_W, "2.0cm", size=17, color="CADCFC"),
        shape(1, f"{badge}  ·  {pack['meta']}", MARGIN, "16.6cm", CONTENT_W, "1.1cm", size=12, color="A0AEC0"),
        notes(1, f"Cover ({kind}). {pack.get('story', pack['title'])}"),
    ]

    # --- 2 BLUF (no default title PH) ---
    cmds.append(add_slide(pack["bluf_title"], LIGHT))
    cmds += title_block(2, pack["bluf_title"], "BOTTOM LINE UP FRONT")
    cmds += [
        shape(2, pack["bluf_status"], MARGIN, "3.5cm", CONTENT_W, "1.75cm", size=14, color=WHITE, bold=True, fill=NAVY),
        shape(2, pack["bluf_body"], MARGIN, "5.5cm", CONTENT_W, "11.7cm", size=16, color=TEXT, fill=CARD),
        footer(2, pack["meta"]),
        notes(2, pack.get("ask_notes", "Lead with BLUF.")),
    ]

    # --- Body ---
    s = 3
    for bt, body, ntxt in pack["body_slides"]:
        cmds.append(add_slide(bt, LIGHT))
        cmds += title_block(s, bt)
        cmds += [
            shape(s, body, MARGIN, "3.5cm", CONTENT_W, "13.5cm", size=16, color=TEXT, fill=CARD),
            footer(s, pack["meta"]),
            notes(s, ntxt),
        ]
        s += 1

    # --- Options ---
    if pack.get("options_table"):
        cmds.append(add_slide("Options & recommendation", LIGHT))
        cmds += title_block(s, "Options & recommendation")
        cmds += [
            shape(
                s,
                "Compare paths; recommendation is marked REC. Decision owner picks by the date on the Ask slide.",
                MARGIN,
                "3.4cm",
                CONTENT_W,
                "1.1cm",
                size=13,
                color=MUTED,
            ),
        ]
        cmds += table_cmds(s, pack["options_table"], y="4.7cm", h="11.5cm")
        cmds += [footer(s, pack["meta"]), notes(s, "Walk trade-offs; land recommendation.")]
        s += 1

    # --- Ask ---
    cmds.append(add_slide("Decision & ask", LIGHT))
    cmds += title_block(s, "Decision & ask", "WHAT WE NEED FROM THIS ROOM")
    cmds += [
        shape(s, pack["ask_lines"], MARGIN, "3.5cm", CONTENT_W, "13.5cm", size=17, color=TEXT, fill=CARD),
        footer(s, pack["meta"]),
        notes(s, pack.get("ask_notes", "Close with owner + date.")),
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
        if args.kind in ("template", "both"):
            path = tpl_dir / f"{key}.pptx"
            print("template", path.name)
            build_deck(path, packs["template"])
            run(["validate", str(path)])
        if args.kind in ("example", "both"):
            path = ex_dir / f"{key}.pptx"
            print("example ", path.name)
            build_deck(path, packs["example"])
            run(["validate", str(path)])

    print("Done →", tpl_dir, "and", ex_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
