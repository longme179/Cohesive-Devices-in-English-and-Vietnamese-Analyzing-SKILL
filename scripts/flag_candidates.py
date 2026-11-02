#!/usr/bin/env python3
"""Flag subheading/title/caption candidates in extracted pairs for review."""
import json, re

for i in range(1, 21):
    pid = f'P{i:02d}'
    d = json.load(open(f'/home/z/my-project/out/raw_pairs/{pid}.json'))
    print(f'===== {pid} =====')
    for lab, arr in (('EN', d['en']), ('VI', d['vi'])):
        for j, p in enumerate(arr):
            flags = []
            if len(p) < 80 and not re.search(r'[.!?…:”"’\']$', p.strip()):
                flags.append('SHORT-NOEND')
            if re.match(r'^(Photo|Image|Credit|Source|Getty|AAP|Reuters|AP)\b', p):
                flags.append('CREDIT?')
            if len(p) < 45 and re.search(r'[A-ZĐ][a-zà-ỹ]+ [A-ZĐ][a-zà-ỹ]+', p) and not p.endswith('.'):
                flags.append('ATTRIB?')
            if flags:
                print(f'  {lab}[{j}] {",".join(flags)}: {p[:100]}')
    # duplicate paragraphs (pull quotes)
    for lab, arr in (('EN', d['en']), ('VI', d['vi'])):
        seen = {}
        for j, p in enumerate(arr):
            key = re.sub(r'\W+', '', p.lower())[:60]
            if key in seen:
                print(f'  DUP {lab}[{j}] ~= {lab}[{seen[key]}]: {p[:80]}')
            else:
                seen[key] = j
