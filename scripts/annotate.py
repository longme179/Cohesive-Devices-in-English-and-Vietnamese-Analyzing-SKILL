#!/usr/bin/env python3
"""Build ST_ties.json / TT_ties.json for a pair from a compact tie table.

A tie table is a list of rows:
  (sent, text, cat, sub, ante, conf, alt, note, occ_or_None)
Ellipsis ties use text=None with (gap_after, recovered) instead:
  (sent, None, cat='E', sub, ante, conf, alt, note, occ, gap_after, recovered)
This script validates every substring against the sentence text and computes
occ automatically when occ is None (first occurrence). It REFUSES to write
if any tie's stated occurrence does not exist.
Usage: python3 annotate.py P01   (imports tables from tie_tables/P01.py)
"""
import json, os, sys, importlib

OUT = '/home/z/my-project/out'

def build(pid, lang, pref, table):
    seg = json.load(open(f'{OUT}/pairs/{pid}/{pref}_seg.json'))
    sents = {s['id']: s['text'] for s in seg['sentences']}
    ties, errors = [], []
    n = 0
    for row in table:
        (sent, text, cat, sub, ante, conf, alt, note, occ) = row[:9]
        gap_after = recovered = None
        if len(row) > 9 and row[9] is not None:
            gap_after = row[9]
        if len(row) > 10 and row[10] is not None:
            recovered = row[10]
        n += 1
        tid = f'{pid}-{lang}-{n:03d}'
        stext = sents.get(sent)
        if stext is None:
            errors.append(f'{tid}: sentence {sent} not found'); continue
        if text is None:  # ellipsis
            if gap_after is None or recovered is None:
                errors.append(f'{tid}: ellipsis needs gap_after and recovered'); continue
            # verify gap_after exists in sentence, compute occ
            occ_g = occ or 1
            pos = -1
            for _ in range(occ_g):
                pos = stext.find(gap_after, pos + 1)
                if pos < 0:
                    errors.append(f'{tid}: gap_after {gap_after!r} occ {occ_g} not found in {sent}')
                    break
            ties.append({'id': tid, 'sent': sent, 'text': None, 'occ': occ_g,
                         'gap_after': gap_after, 'recovered': recovered,
                         'cat': cat, 'sub': sub, 'dir': 'ana',
                         'ante': ante, 'conf': conf, 'alt': alt, 'note': note})
            continue
        if text not in stext:
            errors.append(f'{tid}: text {text!r} not found in {sent}: {stext[:80]!r}...')
            continue
        if occ is None:
            occ = stext.count(text) and 1
            # default: first occurrence; if the text occurs multiple times the
            # caller must give explicit occ for all ties of that text
        else:
            pos, found = -1, 0
            while True:
                pos = stext.find(text, pos + 1)
                if pos < 0: break
                found += 1
                if found == occ: break
            if found < occ:
                errors.append(f'{tid}: occurrence {occ} of {text!r} not found in {sent}')
                continue
        ties.append({'id': tid, 'sent': sent, 'text': text, 'occ': occ,
                     'cat': cat, 'sub': sub, 'dir': 'ana', 'ante': ante,
                     'conf': conf, 'alt': alt, 'note': note})
    if errors:
        print(f'== {pid} {lang}: {len(errors)} ERRORS ==')
        for e in errors: print('  ', e)
        return None
    json.dump({'pair': pid, 'lang': lang, 'ties': ties},
              open(f'{OUT}/pairs/{pid}/{pref}_ties.json', 'w'),
              ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(t['cat'] for t in ties)
    print(f'{pid} {lang}: {len(ties)} ties, by cat: {dict(c)}')
    return ties

if __name__ == '__main__':
    pid = sys.argv[1]
    mod = importlib.import_module(f'tie_tables.{pid}')
    build(pid, 'EN', 'ST', mod.ST)
    build(pid, 'VI', 'TT', mod.TT)
