#!/usr/bin/env python3
"""Mechanical locator for manually chosen tie spans.

This script does NOT decide ties. It only reports where a literal human-chosen
substring occurs inside the segmented sentences of one pair, so that the
annotator can copy the exact sentence id / offset into a hand-written tie row.

Usage:
  python3 scripts/find_quote.py P01 ST "đưa nước qua"
  python3 scripts/find_quote.py P01 TT "Gần như chắc chắn" --all
  python3 scripts/find_quote.py P01 ST "to test the technology" --context 2
"""
import argparse
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = os.path.join(BASE, 'out', 'pairs')


def load(pid, pref):
    seg = json.load(open(os.path.join(PAIRS, pid, f'{pref}_seg.json')))
    return seg['sentences']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pair')
    ap.add_argument('side', choices=['ST', 'TT'])
    ap.add_argument('literal')
    ap.add_argument('--all', action='store_true',
                    help='show every occurrence (default: first 12)')
    ap.add_argument('--context', type=int, default=60,
                    help='characters of left/right context')
    args = ap.parse_args()

    sents = load(args.pair, args.side)
    literal = args.literal
    hits = []
    for s in sents:
        start = 0
        while True:
            p = s['text'].find(literal, start)
            if p < 0:
                break
            hits.append((s, p))
            start = p + max(1, len(literal))
    if not hits:
        print(f'NO MATCH for {literal!r} in {args.pair} {args.side}')
        return 1
    limit = len(hits) if args.all else min(12, len(hits))
    for i, (s, p) in enumerate(hits[:limit], 1):
        a = max(0, p - args.context)
        b = min(len(s['text']), p + len(literal) + args.context)
        print(f"[{i}] {s['id']} @{p} (sentence len {len(s['text'])})")
        print(f"    ...{s['text'][a:p]}⟦{literal}⟧{s['text'][p + len(literal):b]}...")
    if len(hits) > limit:
        print(f'... {len(hits) - limit} more occurrence(s); use --all')
    return 0


if __name__ == '__main__':
    sys.exit(main())
