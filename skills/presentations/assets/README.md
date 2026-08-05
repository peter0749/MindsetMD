# Presentation PPTX assets

Two packs per scenario (01–09):

| Pack | Path | Purpose |
|------|------|---------|
| **Template** | [`templates/`](templates/) | Placeholder structure — copy and fill |
| **Example** | [`examples/`](examples/) | Filled **Aurora / NovaSemi / Atlas** storyline simulation |

**Out of scope:** personal performance / annual self-review.

## Shared example universe

| Field | Value |
|-------|--------|
| Company | NovaSemi (fictional IC design) |
| Program | **Project Aurora** — 5nm connectivity SoC |
| Team | **Atlas Platform** (DV, integration, bring-up) |
| Lead | Alex Chen (EM) → VP Eng Morgan Lee |
| Arc | Tech decision → silicon results → org health → farm ROI → sim licenses → +1 DV → H2 roadmap → Q3 kickoff → Q2 QBR |

Stories cross-link (e.g. AON Option B in 01 pays off in 02/09; hire ask in 03/06).

## Index

| # | Scenario | Template | Example |
|---|----------|----------|---------|
| 01 | Technical review | [templates/01-technical-review.pptx](templates/01-technical-review.pptx) | [examples/01-technical-review.pptx](examples/01-technical-review.pptx) |
| 02 | Results / demo | [templates/02-results-demo.pptx](templates/02-results-demo.pptx) | [examples/02-results-demo.pptx](examples/02-results-demo.pptx) |
| 03 | Management effectiveness | [templates/03-management-effectiveness.pptx](templates/03-management-effectiveness.pptx) | [examples/03-management-effectiveness.pptx](examples/03-management-effectiveness.pptx) |
| 04 | Benefit / ROI | [templates/04-benefit-value.pptx](templates/04-benefit-value.pptx) | [examples/04-benefit-value.pptx](examples/04-benefit-value.pptx) |
| 05 | Procurement | [templates/05-procurement-proposal.pptx](templates/05-procurement-proposal.pptx) | [examples/05-procurement-proposal.pptx](examples/05-procurement-proposal.pptx) |
| 06 | Resource / HC | [templates/06-resource-request.pptx](templates/06-resource-request.pptx) | [examples/06-resource-request.pptx](examples/06-resource-request.pptx) |
| 07 | Roadmap | [templates/07-roadmap.pptx](templates/07-roadmap.pptx) | [examples/07-roadmap.pptx](examples/07-roadmap.pptx) |
| 08 | Period start | [templates/08-period-start-planning.pptx](templates/08-period-start-planning.pptx) | [examples/08-period-start-planning.pptx](examples/08-period-start-planning.pptx) |
| 09 | Period end / QBR | [templates/09-period-end-review.pptx](templates/09-period-end-review.pptx) | [examples/09-period-end-review.pptx](examples/09-period-end-review.pptx) |

## Layout rules (optimized)

- No default title placeholder on content/BLUF slides (prevents kicker collision).
- Title band → status bar (BLUF) → card body → footer meta.
- Margins ≥ 1.4cm; navy status bar; options tables with navy header.
- Real newlines only (never literal `\n` in text).

## Regenerate

```bash
python3 scripts/generate_report_pptx_templates.py
python3 scripts/test_pptx_assets.py
```

Content data: `scripts/pptx_deck_data.py` · Generator: `scripts/generate_report_pptx_templates.py`  
Research norms: [../research-deck-norms.md](../research-deck-norms.md)
