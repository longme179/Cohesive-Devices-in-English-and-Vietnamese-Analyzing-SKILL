#!/usr/bin/env python3
"""Ingest a two-column English–Vietnamese markdown file into a work tree.

Input contract
--------------
Any markdown table with exactly two content columns (EN | VI) is accepted.
A pair may start with:

    | https://en... | https://vi... |
    | **English title** | **Vietnamese title** |
    | body row | body row |

or with a header row ``| Tiếng Anh | Tiếng Việt |`` followed by the title.
Blank lines inside a pair are tolerated.  A new pair starts at a ``##`` heading,
a two-column header row, or a new URL pair.

Output
------
work/pairs/P01/meta.json       title + source URLs
work/pairs/P01/rows.json       [{"en": ..., "vi": ...}, ...]
work/pairs/P01/ST.txt / TT.txt canonical row flow (for reading/inspection)

Next: ``python -m pipeline.segment --work work``
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from .common import (clean_cell, dump_json, is_header, is_separator,
                     is_title_row, is_url, split_table_row)


def parse_blocks(lines: list[str]) -> list[list[tuple[str, list[str]]]]:
    """Group table rows into pair blocks; blank lines do not close a pair."""
    blocks: list[list[tuple[str, list[str]]]] = []
    current: list[tuple[str, list[str]]] = []
    pending_new = False

    def close():
        nonlocal current
        if current:
            blocks.append(current)
        current = []

    for raw in lines:
        line = raw.strip()
        if line.startswith("#"):
            pending_new = True
            continue
        if not line.startswith("|"):
            continue
        cells = split_table_row(line)
        if is_separator(cells):
            continue
        if pending_new and current:
            close()
        pending_new = False
        if is_header(cells):
            close()
            current.append(("header", cells))
            continue
        if len(cells) >= 2 and is_url(cells[0]) and is_url(cells[1]):
            if any(kind == "body" for kind, _ in current):
                close()
            current.append(("url", cells))
            continue
        if len(cells) < 2:
            continue
        current.append(("row", cells))
    close()
    return blocks


def urls_from_row(cells: list[str]) -> tuple[str, str]:
    out = []
    for cell in cells[:2]:
        m = re.search(r"\((https?://[^)]+)\)", cell)
        out.append(m.group(1) if m else (cell.strip() if is_url(cell) else ""))
    return out[0], out[1]


def build_pair(block: list[tuple[str, list[str]]], num: int):
    pid = f"P{num:02d}"
    en_url = vi_url = ""
    rows: list[tuple[str, str]] = []
    title_en = title_vi = ""

    header_cells = None
    for kind, cells in block:
        if kind == "header":
            header_cells = cells
            continue
        if kind == "url":
            en_url, vi_url = urls_from_row(cells)
            continue
        en, vi = clean_cell(cells[0]), clean_cell(cells[1])
        if not en and not vi:
            continue
        # A title row is the first non-header row of the pair.
        if not title_en and not title_vi and not rows and (
                is_title_row(cells) or
                (header_cells is not None and len(en) < 220 and len(vi) < 220)):
            title_en, title_vi = en, vi
            if not en_url or not vi_url:
                eu, vu = urls_from_row(cells)
                en_url = en_url or eu
                vi_url = vi_url or vu
            continue
        rows.append((en, vi))

    if not title_en and not title_vi and rows:
        title_en, title_vi = rows.pop(0)

    return {
        "id": pid,
        "num": num,
        "title_en": title_en,
        "title_vi": title_vi,
        "en_url": en_url,
        "vi_url": vi_url,
        "rows": [{"en": en, "vi": vi} for en, vi in rows],
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Ingest a 2-column EN–VI markdown file")
    ap.add_argument("--input", required=True, help="markdown file with EN|VI tables")
    ap.add_argument("--work", default="work", help="work directory (default: work)")
    args = ap.parse_args(argv)

    text = Path(args.input).read_text(encoding="utf-8")
    blocks = parse_blocks(text.splitlines())
    if not blocks:
        print("ERROR: no 2-column markdown tables found.", file=sys.stderr)
        return 2

    work = Path(args.work)
    pairs = [build_pair(b, i + 1) for i, b in enumerate(blocks)]
    pairs = [p for p in pairs if p["rows"]]
    if not pairs:
        print("ERROR: tables found but no body rows.", file=sys.stderr)
        return 2

    for p in pairs:
        d = work / "pairs" / p["id"]
        d.mkdir(parents=True, exist_ok=True)
        dump_json(d / "meta.json", {k: p[k] for k in
                                    ("id", "num", "title_en", "title_vi",
                                     "en_url", "vi_url")})
        dump_json(d / "rows.json", p["rows"])
        st = "\n".join(r["en"] for r in p["rows"])
        tt = "\n".join(r["vi"] for r in p["rows"])
        (d / "ST.txt").write_text(st + ("\n" if st else ""), encoding="utf-8")
        (d / "TT.txt").write_text(tt + ("\n" if tt else ""), encoding="utf-8")
        print(f'{p["id"]}: {len(p["rows"])} rows | EN {len(st)} chars | '
              f'VI {len(tt)} chars | {p["title_en"][:60]}')

    print(f"\nWrote {len(pairs)} pair(s) under {work}/pairs/")
    print("Next: python -m pipeline.segment --work", work)
    return 0


if __name__ == "__main__":
    sys.exit(main())
