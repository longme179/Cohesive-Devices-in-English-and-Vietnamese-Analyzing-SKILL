#!/usr/bin/env python3
"""Compact align summary for P20."""
import json
from collections import Counter

BASE = "/home/z/my-project/out/pairs/P20"
en = {t["id"]: t for t in json.load(open(f"{BASE}/ST_ties.json"))["ties"]}
vi = {t["id"]: t for t in json.load(open(f"{BASE}/TT_ties.json"))["ties"]}
al = json.load(open(f"{BASE}/align.json"))["alignments"]

print(f"total alignments: {len(al)}")
print(Counter(a["outcome"] for a in al))
print()
for a in al:
    st = en.get(a["st_tie"], {})
    tt = vi.get(a["tt_tie"], {}) if a["tt_tie"] else {}
    stx = f"{st.get('sent')}:{st.get('text')} ({st.get('cat')})"
    ttx = f"{tt.get('sent')}:{tt.get('text')} ({tt.get('cat')})" if tt else "—"
    sh = a.get("shift") or ""
    nt = a.get("note") or ""
    print(f"[{a['outcome'].upper()}] {a['st_tie']} {stx}  =>  {ttx} {sh} {nt}")
print()
print("EN ties with no alignment entry:")
aligned_st = {a["st_tie"] for a in al}
for i, t in en.items():
    if i not in aligned_st:
        print(f"  {i} {t['sent']}:{t['text']} ({t['cat']})")
print()
print("VI ties never used as tt_tie:")
used_tt = {a["tt_tie"] for a in al if a["tt_tie"]}
for i, t in vi.items():
    if i not in used_tt:
        print(f"  {i} {t['sent']}:{t['text']} ({t['cat']})")
