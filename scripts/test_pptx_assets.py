#!/usr/bin/env python3
"""Structural + timeline tests for shipped report PPTX templates + examples."""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills" / "presentations" / "assets" / "pptx"
TPL = ASSETS / "templates"
EX = ASSETS / "examples"
OFFICECLI = Path.home() / ".local" / "bin" / "officecli"
sys.path.insert(0, str(ROOT / "scripts"))
from pptx_deck_data import AURORA_TIMELINE, SCENARIOS  # noqa: E402

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
    joined = " ".join(text.split())
    up = joined.upper()
    assert "FRONTF BLUF" not in up and "UP FRONTF" not in up, f"title collision in {path.name}"
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    assert any("BOTTOM LINE UP FRONT" in ln.upper() for ln in lines), path.name
    assert any("BLUF" in ln.upper() for ln in lines), path.name
    low = text.lower()
    assert "decision" in low or "ask" in low or "recommend" in low, path.name
    if expect_example:
        assert "aurora" in low or "atlas" in low or "novasemi" in low, path.name
        assert text.count("[") < 12, path.name
    print("OK", path.relative_to(ASSETS))


def _flatten_example(key: str) -> str:
    ex = SCENARIOS[key]["example"]
    parts = [
        ex["subtitle"],
        ex["bluf_status"],
        ex["bluf_body"],
        ex["ask_lines"],
        ex.get("story", ""),
    ]
    for _t, body, _n in ex["body_slides"]:
        parts.append(body)
    if ex.get("options_table"):
        for row in ex["options_table"]:
            parts.extend(row)
    return "\n".join(parts)


def _parse_mdy_slash(s: str) -> list[date]:
    """Parse M/D or M/D/YY fragments that appear as calendar dates in 2026 context."""
    out = []
    for m in re.finditer(r"\b(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?\b", s):
        mo, d, y = int(m.group(1)), int(m.group(2)), m.group(3)
        year = 2026 if y is None else (2000 + int(y) if int(y) < 100 else int(y))
        if year != 2026:
            continue
        if 1 <= mo <= 12 and 1 <= d <= 31:
            try:
                out.append(date(year, mo, d))
            except ValueError:
                pass
    for m in re.finditer(r"\b(2026)-(\d{2})-(\d{2})\b", s):
        out.append(date(int(m.group(1)), int(m.group(2)), int(m.group(3))))
    return out


def check_aurora_timeline_data() -> None:
    """Honest checks on example *data* (source of truth before pptx gen)."""
    t = AURORA_TIMELINE
    assert t["01_decide_by"] < t["01_freeze_target"]
    assert t["rtl_freeze_held"] <= t["01_freeze_target"]
    assert t["rtl_freeze_held"] < t["tape_out"] < t["first_silicon"] < t["day3_boot"]
    assert t["day3_boot"] <= t["02_present"] < t["02_sample_ask_by"] < t["sample_ship"]
    assert t["rtl_freeze_held"] < t["04_present"] < t["04_ask_by"]
    assert t["day3_boot"] < t["04_present"], "farm ROI deck must be after boot if it cites boot as lagging"
    assert t["04_ask_by"] > t["04_present"] or t["04_ask_by"] >= t["04_present"]

    # 01 text: freeze target 4/10, decide 3/20; may mention "first silicon" only as future residual, not achieved boot
    ex01 = _flatten_example("01-technical-review")
    assert "4/10" in ex01 or "2026-04-10" in ex01
    assert "3/20" in ex01 or "2026-03-20" in ex01
    low01 = ex01.lower()
    assert "day-3 boot" not in low01 and "day 3 boot" not in low01
    assert "brought up" not in low01 and "fab return" not in low01

    # 02 text: post-freeze silicon; references prior freeze
    ex02 = _flatten_example("02-results-demo")
    assert "4/10" in ex02 or "freeze" in ex02.lower()
    assert "5/12" in ex02 or "2026-05-12" in ex02 or "silicon" in ex02.lower()
    assert "freeze 6/20" not in ex02.lower() and "freeze stays 6/20" not in ex02.lower()
    assert "threatens 6/20" not in ex02.lower()

    # 04: lagging freeze/boot dates must be before ask-by (2026-05-30)
    ex04 = _flatten_example("04-benefit-value")
    assert "2026-04-10" in ex04 or "4/10" in ex04
    assert "2026-05-15" in ex04 or "5/15" in ex04
    assert "2026-05-30" in ex04 or "5/30" in ex04
    # Forbidden: claiming 6/20 freeze as already held while asking by 5/30
    assert "freeze held 6/20" not in ex04.lower()
    assert "freeze held 2026-06-20" not in ex04.lower()
    assert not re.search(r"lagging[^\n]{0,80}6/20", ex04, re.I)
    # Parse: any "held" freeze date mentioned near lagging should be < ask_by
    ask_by = t["04_ask_by"]
    for dm in re.finditer(
        r"(?:freeze held|RTL freeze held|held)\s*(?:2026-)?(\d{1,2})/(\d{1,2})",
        ex04,
        re.I,
    ):
        held = date(2026, int(dm.group(1)), int(dm.group(2)))
        assert held < ask_by, f"example 04 claims freeze held {held} but ask-by is {ask_by}"

    # Cross-arc: 02 presentation after 01 freeze
    assert t["02_present"] > t["rtl_freeze_held"]
    print("OK aurora timeline data checks")


def check_generated_example_04_text() -> None:
    """Drive real officecli extract: 04 must not claim post-ask freeze as lagging."""
    path = EX / "04-benefit-value.pptx"
    text = ocli("view", str(path), "text")
    low = text.lower()
    assert "freeze held 6/20" not in low
    assert "2026-06-20" not in text or "ask" in low
    # if both 4/10 freeze and 5/30 ask appear, good
    assert "4/10" in text or "2026-04-10" in text
    assert "5/30" in text or "2026-05-30" in text
    print("OK generated example 04 timeline extract")


def main() -> int:
    assert OFFICECLI.is_file(), f"missing officecli {OFFICECLI}"
    assert TPL.is_dir() and EX.is_dir(), "templates/ and examples/ required"
    tpl = sorted(p.name for p in TPL.glob("*.pptx"))
    ex = sorted(p.name for p in EX.glob("*.pptx"))
    assert tpl == EXPECTED, f"templates mismatch: {tpl}"
    assert ex == EXPECTED, f"examples mismatch: {ex}"

    check_aurora_timeline_data()

    for name in EXPECTED:
        check_deck(TPL / name, expect_example=False)
        check_deck(EX / name, expect_example=True)

    check_generated_example_04_text()

    idx = (ASSETS.parent / "README.md").read_text()
    assert "templates/" in idx and "examples/" in idx
    print("PASS", len(EXPECTED), "templates +", len(EXPECTED), "examples + timeline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
