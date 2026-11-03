#!/usr/bin/env python3
"""Mechanical locator for a literal the analyst has already chosen.

This never decides a tie.  It reports sentence id, local offset and context so
the hand-written tie row can use exact text / gap_after / occ.

  python -m pipeline.locate --work work --pair P01 --side ST "to test the technology"
  python -m pipeline.locate --work work --pair P01 --side TT "Gần như" --all
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .common import load_json, pair_dir


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Locate a literal in segmented sentences")
    ap.add_argument("--work", default="work")
    ap.add_argument("--pair", required=True)
    ap.add_argument("--side", choices=["ST", "TT"], required=True)
    ap.add_argument("literal")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--context", type=int, default=70)
    args = ap.parse_args(argv)

    seg = load_json(pair_dir(args.work, args.pair) / f"{args.side}_seg.json")
    hits = []
    for s in seg["sentences"]:
        start = 0
        while True:
            p = s["text"].find(args.literal, start)
            if p < 0:
                break
            hits.append((s, p))
            start = p + max(1, len(args.literal))
    if not hits:
        print(f"NO MATCH for {args.literal!r} in {args.pair} {args.side}")
        return 1
    limit = len(hits) if args.all else min(12, len(hits))
    for i, (s, p) in enumerate(hits[:limit], 1):
        a = max(0, p - args.context)
        b = min(len(s["text"]), p + len(args.literal) + args.context)
        print(f"[{i}] {s['id']} @{p} (len {len(s['text'])})")
        print(f"    ...{s['text'][a:p]}⟦{args.literal}⟧"
              f"{s['text'][p + len(args.literal):b]}...")
    if len(hits) > limit:
        print(f"... {len(hits) - limit} more; use --all")
    return 0


if __name__ == "__main__":
    sys.exit(main())
