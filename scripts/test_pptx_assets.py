#!/usr/bin/env python3
"""Structural tests for shipped report PPTX assets (real officecli entry points)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills" / "presentations" / "assets" / "pptx"
OFFICECLI = Path.home() / ".local" / "bin" / "officecli"

EXPECTED = [
    "01-technical-review.pptx",
    "02-results-demo.pptx",
    "03-management-effectiveness.pptx",
    "04-benefit-value.pptx",
    "05-procurement-proposal.pptx",
    "06-resource-request.pptx",
    "07-roadmap.pptx",
    "08-period-start-planning.pptx",
    "09-period-end-review.pptx",
]


def ocli(*args: str) -> str:
    r = subprocess.run(
        [str(OFFICECLI), *args],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        raise AssertionError(f"officecli {' '.join(args)} failed: {r.stderr or r.stdout}")
    return r.stdout


def main() -> int:
    assert OFFICECLI.is_file(), f"officecli missing at {OFFICECLI}"
    assert ASSETS.is_dir(), f"assets dir missing: {ASSETS}"
    files = sorted(p.name for p in ASSETS.glob("*.pptx"))
    assert files == EXPECTED, f"unexpected pptx set: {files}"

    for name in EXPECTED:
        path = ASSETS / name
        out = ocli("validate", str(path))
        assert "passed" in out.lower() or "no errors" in out.lower(), out
        text = ocli("view", str(path), "text")
        assert r"\n" not in text.replace("\n", ""), "literal backslash-n should not appear"
        # BLUF title collision regression: default title + kicker used to merge into FRONTF/FRONTBLUF
        compact = "".join(text.split()).upper()
        assert "FRONTF" not in compact and "FRONTBLUF" not in compact, (
            f"{name}: BLUF title collision (garbled BOTTOM LINE + BLUF title)"
        )
        assert "BOTTOMLINEUPFRONT" in compact or "BLUF" in compact, f"{name} missing BLUF band"
        # content guidance
        low = text.lower()
        assert "bluf" in low or "bottom line" in low or "status" in low, f"{name} missing BLUF/status"
        assert "decision" in low or "ask" in low or "recommend" in low, f"{name} missing decision language"
        print("OK", name)
    print("PASS", len(EXPECTED), "decks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
