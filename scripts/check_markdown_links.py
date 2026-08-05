#!/usr/bin/env python3
"""Check markdown absolute HTTP links and relative file paths. Exit 1 on failures."""
from __future__ import annotations

import re
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def collect():
    abs_urls = set()
    rel = []
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"https?://[^\s\)\]\>\"\'<>]+", text):
            u = m.group(0).rstrip(".,;:")
            while u and u[-1] in ".,;:)]}>\"'":
                u = u[:-1]
            abs_urls.add((str(p.relative_to(ROOT)), u))
        for m in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", text):
            target = m.group(2).strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#")[0]
            if not path_part:
                continue
            rel.append((p, m.group(1), path_part))
    return abs_urls, rel


def check_url(url: str, timeout: int = 20):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MindsetLinkCheck/1.0)"}
    try:
        req = urllib.request.Request(url, method="GET", headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=ssl.create_default_context()) as resp:
            code = resp.getcode()
            return url, code, None if code < 400 else f"HTTP {code}"
    except Exception as e:
        return url, None, f"{type(e).__name__}: {e}"


def main() -> int:
    abs_urls, rel = collect()
    unique = sorted({u for _, u in abs_urls})
    print(f"absolute_urls={len(unique)} relative_links={len(rel)}")

    bad_abs = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for url, code, err in ex.map(check_url, unique):
            if code and code < 400:
                print(f"OK  {code} {url}")
            else:
                print(f"BAD {code} {url} :: {err}")
                bad_abs.append((url, err))

    bad_rel = []
    for p, label, path_part in rel:
        resolved = (p.parent / path_part).resolve()
        if not resolved.exists():
            bad_rel.append((str(p.relative_to(ROOT)), label, path_part))
            print(f"REL_BAD {p.relative_to(ROOT)} -> {path_part}")

    print(f"SUMMARY abs_bad={len(bad_abs)} rel_bad={len(bad_rel)}")
    if bad_abs or bad_rel:
        return 1
    print("PASS all markdown links reachable / relative paths exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
