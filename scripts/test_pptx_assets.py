#!/usr/bin/env python3
"""Structural tests for shipped report PPTX templates + examples (real officecli path)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills" / "presentations" / "assets" / "pptx"
TPL = ASSETS / "templates"
EX = ASSETS / "examples"
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
    r = subprocess.run([str(OFFICECLI), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise AssertionError(f"officecli failed: {args} :: {r.stderr or r.stdout}")
    return r.stdout


def check_deck(path: Path, *, expect_example: bool) -> None:
    out = ocli("validate", str(path))
    assert "passed" in out.lower() or "no errors" in out.lower(), out
    text = ocli("view", str(path), "text")
    assert r"\n" not in text.replace("\n", ""), f"literal backslash-n in {path.name}"
    # Real collision garble was a single line like "BOTTOM LINE UP FRONTF BLUF — …"
    joined = " ".join(text.split())
    up = joined.upper()
    assert "FRONTF BLUF" not in up and "UP FRONTF" not in up, f"title collision garble in {path.name}: {joined[:120]}"
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    assert any("BOTTOM LINE UP FRONT" in ln.upper() for ln in lines), f"missing BLUF kicker line in {path.name}"
    assert any("BLUF" in ln.upper() for ln in lines), f"missing BLUF title line in {path.name}"
    low = text.lower()
    assert "decision" in low or "ask" in low or "recommend" in low, f"missing decision language {path.name}"
    if expect_example:
        assert "aurora" in low or "atlas" in low or "novasemi" in low, f"example missing story world {path.name}"
        # templates are full of [placeholders]; examples should be mostly filled
        assert text.count("[") < 12, f"example still looks too placeholder-heavy {path.name}"
    print("OK", path.relative_to(ASSETS))


def main() -> int:
    assert OFFICECLI.is_file(), f"missing officecli {OFFICECLI}"
    assert TPL.is_dir() and EX.is_dir(), "templates/ and examples/ required"
    tpl = sorted(p.name for p in TPL.glob("*.pptx"))
    ex = sorted(p.name for p in EX.glob("*.pptx"))
    assert tpl == EXPECTED, f"templates mismatch: {tpl}"
    assert ex == EXPECTED, f"examples mismatch: {ex}"
    assert len(tpl) + len(ex) >= 18

    for name in EXPECTED:
        check_deck(TPL / name, expect_example=False)
        check_deck(EX / name, expect_example=True)

    # Index must map both
    idx = (ASSETS.parent / "README.md").read_text()
    assert "templates/" in idx and "examples/" in idx
    print("PASS", len(EXPECTED), "templates +", len(EXPECTED), "examples")
    return 0


if __name__ == "__main__":
    sys.exit(main())
