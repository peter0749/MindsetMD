#!/usr/bin/env python3
"""Validate mindset skill corpus consistency rules (capacity A/B, audit present, canonicals).

Exit 0 on success; non-zero on failure. Run from repo root or any cwd.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# Absolute capacity-band claims that must not appear without context labels nearby
# We allow them only when within N chars of context markers.
UNPLANNED_BANDS = [
    (r"20\s*[–\-]\s*30\s*%", "B", ("context **b**", "context b", "headcount", "model b", "capacity model b", "staffing", "hiring")),
    (r"10\s*[–\-]\s*15\s*%", "A", ("context **a**", "context a", "quarter", "model a", "capacity model a", "quarterly", "roadmap allocation")),
]


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)


def check_required_files(errors: list[str]) -> None:
    required = [
        SKILLS / "shared" / "capacity-model.md",
        SKILLS / "shared" / "consistency-audit.md",
        SKILLS / "shared" / "amazon-mapping.md",
        SKILLS / "README.md",
        SKILLS / "executive-communication" / "decision-ready-updates.md",
        SKILLS / "resource-advocacy" / "securing-resources-upward.md",
        SKILLS / "meetings" / "in-meeting-and-follow-through.md",
        SKILLS / "roadmap-planning" / "planning-sense-proactive-framing.md",
        SKILLS / "department-value" / "presenting-department-value.md",
        SKILLS / "cross-team" / "conflict-and-coordination.md",
        SKILLS / "presentations" / "README.md",
    ]
    for p in required:
        if not p.is_file():
            fail(f"missing required file: {p.relative_to(ROOT)}", errors)


def check_audit_structure(errors: list[str]) -> None:
    audit = read(SKILLS / "shared" / "consistency-audit.md")
    for heading in (
        "## 1. Executive summary",
        "## 3. Conflict matrix",
        "## 4. Topic deep-dives",
        "capacity",
        "BLUF",
        "presentations",
        "對上說不",
        "influence",
    ):
        if heading not in audit and heading.lower() not in audit.lower():
            # Chinese/English mixed — case-sensitive for ## headers
            if heading.startswith("##") and heading not in audit:
                fail(f"audit missing section/marker: {heading!r}", errors)
            elif not heading.startswith("##") and heading.lower() not in audit.lower():
                fail(f"audit missing topic marker: {heading!r}", errors)
    # Matrix must have multiple rows
    rows = [ln for ln in audit.splitlines() if ln.startswith("|") and "context-separated" in ln or (ln.startswith("|") and "consistent" in ln)]
    if len(rows) < 8:
        fail(f"audit conflict matrix too thin ({len(rows)} status rows)", errors)


def check_canonical_headers(errors: list[str]) -> None:
    """Each playbook skill declares Canonical for; (a) owns SOR shape; (f) must not sole-own shape."""
    a = read(SKILLS / "executive-communication" / "decision-ready-updates.md")
    if "Canonical for:" not in a or "BLUF" not in a.split("Canonical for:")[1][:200]:
        fail("(a) must Canonical-for BLUF/SOR", errors)

    f = read(SKILLS / "cross-team" / "conflict-and-coordination.md")
    if "Not canonical for:" not in f and "sentence shape" not in f[:1200]:
        fail("(f) must disclaim SOR sentence-shape ownership", errors)
    # Must not claim sole escalation packet without fields qualifier
    head = f[:800]
    if re.search(r"Canonical for:.*cross-team escalation packet\s*$", head, re.M):
        fail("(f) still claims bare 'escalation packet' as sole canonical", errors)

    index = read(SKILLS / "README.md")
    for concept in ("BLUF", "Capacity", "Influence", "對上說不", "presentations"):
        if concept not in index and concept.lower() not in index.lower():
            fail(f"index missing concept: {concept}", errors)


def _normalize(s: str) -> str:
    # Strip markdown bold/italics so "model **A**" matches marker "model a"
    return re.sub(r"[*_`]", "", s).lower()


def window_has_context(text: str, pos: int, markers: tuple[str, ...], radius: int = 280) -> bool:
    lo = max(0, pos - radius)
    hi = min(len(text), pos + radius)
    chunk = _normalize(text[lo:hi])
    return any(m in chunk for m in markers)


def check_capacity_claims(errors: list[str], report_lines: list[str]) -> None:
    """Every unplanned 10-15 or 20-30 claim near skills tree must sit near context markers.

    Skip: consistency-audit.md and research-notes.md (documentation of the model).
    capacity-model.md is the SoT and defines both — always OK.
    """
    skip_names = {"consistency-audit.md", "research-notes.md"}
    for path in sorted(SKILLS.rglob("*.md")):
        if path.name in skip_names:
            continue
        text = read(path)
        rel = str(path.relative_to(ROOT))
        if path.name == "capacity-model.md":
            report_lines.append(f"OK  {rel}  (SoT — both A/B defined)")
            continue
        for pattern, ctx_label, markers in UNPLANNED_BANDS:
            for m in re.finditer(pattern, text):
                # Ignore pure feature/debt tables that aren't "unplanned" — require nearby unplanned|buffer|headcount|capacity context
                lo = max(0, m.start() - 120)
                hi = min(len(text), m.end() + 80)
                local = text[lo:hi].lower()
                if "unplanned" not in local and "buffer" not in local and "headcount" not in local:
                    # e.g. random "10–15%" elsewhere
                    if "capacity" not in local and "model" not in local:
                        continue
                ok = window_has_context(text, m.start(), markers)
                # Also accept explicit "context A/B" unicode variants already in markers
                line_no = text.count("\n", 0, m.start()) + 1
                snippet = text[m.start() : m.end()]
                if ok:
                    report_lines.append(f"OK  {rel}:{line_no}  {snippet!r} ~ctx {ctx_label}")
                else:
                    fail(
                        f"unlabeled capacity claim {snippet!r} at {rel}:{line_no} "
                        f"(expected nearby markers for context {ctx_label}: {markers[:3]}…)",
                        errors,
                    )
                    report_lines.append(f"BAD {rel}:{line_no}  {snippet!r} missing ctx {ctx_label}")


def check_content_template_labeling(errors: list[str]) -> None:
    """Presentations must be labeled content templates, not visual design systems."""
    pres = SKILLS / "presentations"
    # Index + assets entry points
    for path, needles in (
        (pres / "README.md", ("內容模板", "美工", "content template")),
        (pres / "assets" / "README.md", ("內容模板", "美工", "content template")),
        (pres / "00-style-mnc-and-hsinchu.md", ("內容模板", "預設美工")),
        (SKILLS / "README.md", ("內容模板", "預設美工排版")),
    ):
        body = read(path)
        for needle in needles:
            if needle not in body and needle.lower() not in body.lower():
                fail(f"content-template label missing {needle!r} in {path.relative_to(ROOT)}", errors)

    # Each scenario deck 01–09 must carry the agent banner near the top
    banner_bits = ("內容模板", "預設美工排版")
    for n in range(1, 10):
        matches = list(pres.glob(f"{n:02d}-*.md"))
        if not matches:
            fail(f"missing scenario file for {n:02d}", errors)
            continue
        path = matches[0]
        head = read(path)[:900]
        for bit in banner_bits:
            if bit not in head:
                fail(f"{path.relative_to(ROOT)} missing top-of-file banner bit {bit!r}", errors)


def check_matrix_topics_in_files(errors: list[str]) -> None:
    """Spot-check that distinguishing rules still exist where matrix claims them."""
    checks = [
        (SKILLS / "shared" / "capacity-model.md", "Two planning contexts"),
        (SKILLS / "shared" / "capacity-model.md", "20–30%"),
        (SKILLS / "shared" / "capacity-model.md", "10–15%"),
        (SKILLS / "resource-advocacy" / "securing-resources-upward.md", "context **B**"),
        (SKILLS / "meetings" / "in-meeting-and-follow-through.md", "對上說不"),
        (SKILLS / "roadmap-planning" / "planning-sense-proactive-framing.md", "plan version"),
        (SKILLS / "cross-team" / "conflict-and-coordination.md", "Not canonical for"),
        (SKILLS / "presentations" / "README.md", "不發明第三套 capacity"),
        (SKILLS / "presentations" / "README.md", "內容模板"),
        (SKILLS / "presentations" / "06-resource-request.md", "model B"),
        (SKILLS / "presentations" / "07-roadmap.md", "model A"),
        (SKILLS / "README.md", "Apparent “conflicts” that are intentional"),
        (SKILLS / "README.md", "Never surprise boss"),
        (SKILLS / "README.md", "healthy public peer conflict"),
        (SKILLS / "executive-communication" / "decision-ready-updates.md", "Context split"),
        (SKILLS / "meetings" / "in-meeting-and-follow-through.md", "Context split"),
        (SKILLS / "cross-team" / "conflict-and-coordination.md", "Context split vs"),
        (SKILLS / "shared" / "consistency-audit.md", "Content template vs visual design"),
        (SKILLS / "shared" / "amazon-mapping.md", "Two Amazon artifacts"),
        (SKILLS / "shared" / "amazon-mapping.md", "punt-labs"),
        (SKILLS / "README.md", "Deck BLUF"),
        (SKILLS / "executive-communication" / "decision-ready-updates.md", "Type 1"),
        (SKILLS / "meetings" / "in-meeting-and-follow-through.md", "study hall"),
        (SKILLS / "roadmap-planning" / "planning-sense-proactive-framing.md", "Working backwards"),
        (SKILLS / "department-value" / "presenting-department-value.md", "Input metrics"),
        (SKILLS / "cross-team" / "conflict-and-coordination.md", "Single-threaded owner"),
        (SKILLS / "presentations" / "README.md", "amazon-mapping"),
    ]
    for path, needle in checks:
        body = read(path)
        if needle not in body and needle.lower() not in body.lower():
            # try flexible dash
            alt = needle.replace("–", "-")
            if alt not in body and needle not in body:
                fail(f"matrix spot-check failed: {path.relative_to(ROOT)} missing {needle!r}", errors)


def main() -> int:
    errors: list[str] = []
    report: list[str] = []
    check_required_files(errors)
    check_audit_structure(errors)
    check_canonical_headers(errors)
    check_capacity_claims(errors, report)
    check_content_template_labeling(errors)
    check_matrix_topics_in_files(errors)

    print("=== capacity claim scan ===")
    for ln in report:
        print(ln)
    print("=== result ===")
    if errors:
        print(f"FAIL ({len(errors)} errors)")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
