#!/usr/bin/env python3
"""Compact dump of P20 tie tables + alignment + exclusions for semantic analysis."""
import json

BASE = "/home/z/my-project/out/pairs/P20"

for lang, f in (("EN", "ST_ties.json"), ("VI", "TT_ties.json")):
    d = json.load(open(f"{BASE}/{f}"))
    print(f"===== {lang} ties ({len(d['ties'])}) =====")
    for t in d["ties"]:
        alt = f" ALT={t['alt']}" if t.get("alt") else ""
        note = f" NOTE={t['note']}" if t.get("note") else ""
        print(f"{t['id']} | {t['sent']} | {t['cat']}/{t['sub']} | {t['dir']} | "
              f"ante: {t['ante']} | conf={t['conf']}{alt}{note} | text: {t['text']}")
    print()

print("===== align.json =====")
al = json.load(open(f"{BASE}/align.json"))
print(json.dumps(al, ensure_ascii=False, indent=1)[:6000])
