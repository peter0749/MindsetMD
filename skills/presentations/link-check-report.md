# Markdown link check report

**Tool:** `python3 scripts/check_markdown_links.py`  
**Last run:** pass (absolute HTTP GET + relative path existence)

## Results

| Check | Result |
|-------|--------|
| Absolute URLs | 22 unique — all HTTP 200 |
| Relative links | all resolve to existing files/dirs |

## Fixed in this pass

| Issue | Fix |
|-------|-----|
| `assets/README.md` linked `templates/` / `examples/` at wrong level | Now `pptx/templates/` and `pptx/examples/` |

## Command

```bash
python3 scripts/check_markdown_links.py
```

Exit code 0 required for CI-style acceptance.
