#!/usr/bin/env python3
"""Row-preserving sentence segmentation for one ingested pair.

Unlike a plain paragraph splitter, this keeps the original EN/VI table rows as
``paras`` (including empty rows) and records each sentence's character span in
the canonical flow text (rows joined by newline).  The Appendix builder can then
put every marked span back into its original two-column row.

Output: work/pairs/PXX/{ST,TT}_seg.json
        {paras: [...], rows: [...], sentences: [{id, para, text, fa, fb}]}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from .common import dump_json, load_json, pair_ids

PROTECT = [
    r"(?:U\.S|U\.K|U\.N|E\.U|D\.C|N\.C|S\.C|Ph\.D|M\.S|B\.S)",
    r"(?:Mr|Mrs|Ms|Dr|Prof|St|Sen|Rep|Gen|Gov|Sgt|Capt|Lt|Col|Rev|Hon|Co|Inc|Ltd|Corp|vs|etc|approx|no)\.",
    r"\b(?:e\.g|i\.e|a\.m|p\.m)\.",
    r"\b[JrSr]\.",
    r"\b(?:TP|Tp|tp)\.HCM\b",
    r"\bv\.v\.",
    r"\d+\.\d+",
    r"\d+\.\d{3}\b",
    r"\d{1,2}\.\d{1,2}\.\d{4}",
    r"\b[A-Z]\.",
]
PROTECT_RE = [re.compile(p) for p in PROTECT]
CLOSERS = "\u201d\"\u2019')]" + "\u2026"


def protect(text: str) -> str:
    for rx in PROTECT_RE:
        out, last = [], 0
        for m in rx.finditer(text):
            out.append(text[last:m.start()])
            out.append(m.group().replace(".", "\x00"))
            last = m.end()
        out.append(text[last:])
        text = "".join(out)
    return text.replace("...", "\x01\x01\x01").replace("\u2026", "\x01")


def restore(text: str) -> str:
    return text.replace("\x00", ".").replace("\x01\x01\x01", "...").replace(
        "\x01", "\u2026")


def split_spans(text: str) -> list[tuple[int, int]]:
    prot = protect(text)
    parts: list[tuple[int, int]] = []
    cur, s0, i = "", None, 0
    while i < len(prot):
        c = prot[i]
        if s0 is None:
            s0 = i
        cur += c
        if c in ".?!":
            j = i + 1
            while j < len(prot) and prot[j] in CLOSERS:
                cur += prot[j]
                j += 1
            i = j
            if i >= len(prot) or prot[i] in " \n\t":
                parts.append((s0, s0 + len(cur)))
                cur, s0 = "", None
                while i < len(prot) and prot[i] in " \n\t":
                    i += 1
            continue
        i += 1
    if cur.strip():
        parts.append((s0, s0 + len(cur)))
    return parts


def segment_rows(rows: list[dict], side: str) -> dict:
    texts = [r[side] for r in rows]
    flow_parts, offsets, pos = [], [], 0
    for t in texts:
        offsets.append(pos)
        flow_parts.append(t)
        pos += len(t) + 1
    flow = "\n".join(flow_parts)

    sentences = []
    for pi, text in enumerate(texts):
        if not text.strip():
            continue
        for a, b in split_spans(text):
            frag = text[a:b]
            lead = len(frag) - len(frag.lstrip())
            trail = len(frag) - len(frag.rstrip())
            fa = offsets[pi] + a + lead
            fb = offsets[pi] + b - trail
            t = text[a + lead:b - trail]
            if not t:
                continue
            sentences.append({"para": pi, "text": t, "fa": fa, "fb": fb})
    for k, s in enumerate(sentences):
        s["id"] = f"S{k + 1:03d}"

    # Safety: every span must reproduce its sentence exactly in the flow.
    for s in sentences:
        span = flow[s["fa"]:s["fb"]]
        if span != s["text"]:
            raise SystemExit(
                f"INTERNAL ERROR: span mismatch at {s['id']}: "
                f"{span[:40]!r} vs {s['text'][:40]!r}")
    return {"paras": texts, "flow": flow, "sentences": sentences}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Segment ingested pairs")
    ap.add_argument("--work", default="work")
    ap.add_argument("--pair", default=None, help="only this pair (default: all)")
    args = ap.parse_args(argv)

    pids = [args.pair] if args.pair else pair_ids(args.work)
    if not pids:
        print(f"ERROR: no pairs under {args.work}/pairs", file=sys.stderr)
        return 2
    for pid in pids:
        d = Path(args.work) / "pairs" / pid
        rows = load_json(d / "rows.json")
        for side, pref in (("en", "ST"), ("vi", "TT")):
            seg = segment_rows(rows, side)
            dump_json(d / f"{pref}_seg.json", seg)
            print(f"{pid} {pref}: {len(seg['paras'])} rows -> "
                  f"{len(seg['sentences'])} sentences")
    print("\nNext: read ST/TT + seg.json, write the manual analysis and tie table.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
