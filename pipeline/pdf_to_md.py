#!/usr/bin/env python3
"""Best-effort PDF -> 2-column markdown using Poppler's layout text.

Why layout text: a PDF is layout, not a table.  ``pdftotext -layout`` keeps the
two visual columns aligned far better than generic "table" detectors, and it is
available on most Linux/macOS systems.  The generated markdown is a **draft**:
always read it, repair merged cells / line order / missing spaces, then analyse.

If ``pdftotext`` is unavailable, falls back to PyMuPDF word positions.

  python -m pipeline.pdf_to_md --pdf input.pdf --out input.md
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def layout_text(pdf: str) -> str | None:
    exe = shutil.which("pdftotext")
    if not exe:
        return None
    try:
        return subprocess.run(
            [exe, "-layout", "-enc", "UTF-8", pdf, "-"],
            check=True, capture_output=True, text=True).stdout
    except Exception:
        return None


def split_columns(line: str) -> tuple[str, str]:
    """Split a layout line at the widest run of spaces (the column gutter)."""
    runs = [(m.start(), m.end()) for m in re.finditer(r"\s{3,}", line)]
    if not runs:
        return line.strip(), ""
    a, b = max(runs, key=lambda r: r[1] - r[0])
    return line[:a].strip(), line[b:].strip()


def parse_layout(text: str) -> list[list[tuple[str, str]]]:
    pairs: list[list[tuple[str, str]]] = []
    current: list[tuple[str, str]] | None = None
    in_table = False

    def new_pair():
        nonlocal current, in_table
        current = []
        pairs.append(current)
        in_table = False

    for raw in text.splitlines():
        line = raw.rstrip()
        if re.match(r"^\s*(Pair|##)\s*\d+", line):
            new_pair()
            continue
        # table header: EN ... VI on one line
        if re.match(r"^\s*EN\b.*\bVI\s*$", line):
            if current is None or current:
                new_pair()
            in_table = True
            continue
        if not in_table or not line.strip():
            continue
        left, right = split_columns(line)
        if not left and not right:
            continue
        if left.lower() in {"en", "tiếng anh"} or right.lower() in {"vi", "tiếng việt"}:
            continue
        current.append((left, right))  # type: ignore[union-attr]
    return [p for p in pairs if p]


def parse_layout_loose(text: str) -> list[list[tuple[str, str]]]:
    """Fallback for PDFs without an explicit EN/VI header row.

    Each line is split at its widest whitespace gutter.  A line containing a
    URL starts a new pair (the source PDFs often repeat the URL row at the top
    of each pair).  Consecutive visual lines become rows; the analyst must merge
    sentence fragments during repair.
    """
    pairs: list[list[tuple[str, str]]] = []
    current: list[tuple[str, str]] | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        left, right = split_columns(line)
        if not left and not right:
            continue
        if "http" in line and (left or right):
            current = []
            pairs.append(current)
        if current is None:
            current = []
            pairs.append(current)
        current.append((left, right))
    return [p for p in pairs if p]


def word_fallback(pdf: str) -> list[list[tuple[str, str]]]:
    try:
        import pymupdf
    except ImportError:
        return []
    doc = pymupdf.open(pdf)
    pairs = []
    for page in doc:
        words = page.get_text("words")
        if not words:
            continue
        mid = page.rect.width / 2
        lines = {}
        for x0, y0, x1, y1, w, *_ in words:
            key = round((y0 + y1) / 2 / 4) * 4
            lines.setdefault(key, []).append((x0, x1, w))
        rows = []
        for y in sorted(lines):
            left = " ".join(w for x0, x1, w in lines[y] if x0 < mid)
            right = " ".join(w for x0, x1, w in lines[y] if x0 >= mid)
            if left or right:
                rows.append((left.strip(), right.strip()))
        if rows:
            pairs.append(rows)
    return pairs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="PDF -> 2-column markdown (draft)")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    text = layout_text(args.pdf)
    blocks = parse_layout(text) if text else []
    if not blocks and text:
        blocks = parse_layout_loose(text)
        if blocks:
            print("NOTE: no explicit EN/VI header found; used loose line pairing.")
    if not blocks:
        blocks = word_fallback(args.pdf)
    if not blocks:
        print("ERROR: no two-column text found. Install poppler (pdftotext) or\n"
              "transcribe the table manually.", file=sys.stderr)
        return 2

    lines = ["# Extracted from PDF — REVIEW BEFORE ANALYSIS", ""]
    for i, rows in enumerate(blocks, 1):
        lines += [f"## Pair {i:02d}", "", "| EN | VI |", "| :--- | :--- |"]
        for a, b in rows:
            a = a.replace("|", "\\|")
            b = b.replace("|", "\\|")
            lines.append(f"| {a} | {b} |")
        lines.append("")
    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.out}: {len(blocks)} table block(s)")
    print("DRAFT ONLY: repair merged cells, row order, missing spaces, then ingest.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
