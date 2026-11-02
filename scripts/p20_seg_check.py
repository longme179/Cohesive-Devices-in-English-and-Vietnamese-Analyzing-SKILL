#!/usr/bin/env python3
"""Verify P20 segmentation + counts for the semantic analysis."""
import json
from collections import Counter

BASE = "/home/z/my-project/out/pairs/P20"

for lang, segf, tief in (("EN", "ST_seg.json", "ST_ties.json"), ("VI", "TT_seg.json", "TT_ties.json")):
    seg = json.load(open(f"{BASE}/{segf}"))
    sents = seg["sentences"] if isinstance(seg, dict) and "sentences" in seg else seg
    print(f"===== {lang} segments: {len(sents)} =====")
    for s in sents:
        sid = s.get("id") or s.get("sid")
        txt = (s.get("text") or "").replace("\n", " ")
        print(f"{sid}: {txt[:110]}")
    ties = json.load(open(f"{BASE}/{tief}"))["ties"]
    print(f"{lang} cat counts:", Counter(t["cat"] for t in ties), "total", len(ties))
    print()
