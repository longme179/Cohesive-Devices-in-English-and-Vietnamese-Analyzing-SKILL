#!/usr/bin/env python3
"""Diagnose unconsumed markers via the REAL side_ir flow."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_appendix_md import (HighlightExtractor, parse_raw_file, normalize_for_match,
                               side_ir, PAIRS_DIR, CATS)

TARGET = sys.argv[1:] if len(sys.argv) > 1 else \
    ['P02', 'P08', 'P10', 'P15']

raw_pairs = parse_raw_file()

for pair_id in TARGET:
    meta = json.load(open(os.path.join(PAIRS_DIR, pair_id, 'meta.json')))
    raw = raw_pairs[pair_id]
    from build_appendix_md import _title_match
    title_en_norm = normalize_for_match(meta.get('title_en', ''))
    title_vi_norm = normalize_for_match(meta.get('title_vi', ''))
    filtered = []
    for en_raw, vi_raw in raw['rows']:
        en_n = normalize_for_match(en_raw) if en_raw != 'none' else ''
        vi_n = normalize_for_match(vi_raw) if vi_raw != 'none' else ''
        en_t = len(en_n) > 10 and _title_match(en_n, title_en_norm)
        vi_t = len(vi_n) > 10 and _title_match(vi_n, title_vi_norm)
        if en_t and vi_t: continue
        if (en_t and vi_raw == 'none') or (vi_t and en_raw == 'none'): continue
        filtered.append((en_raw, vi_raw))

    for pref in ('ST', 'TT'):
        ext = HighlightExtractor(os.path.join(PAIRS_DIR, pair_id, f'{pref}_highlighted.md'), pair_id, pref)
        rows_ir = []
        for en_raw, vi_raw in filtered:
            r = en_raw if pref == 'ST' else vi_raw
            rows_ir.append(side_ir(r, ext))
        missing = [(i, m) for i, m in enumerate(ext.markers) if i not in ext.consumed]
        if not missing:
            continue
        print(f'==== {pair_id} {pref}: {len(missing)} missing ====')
        for i, m in missing:
            txt = '∅' if m['point'] else ext.plain[m['fa']:m['fb']]
            ctx = ext.plain[max(0, m['fa'] - 70):m['fa']]
            print(f'  marker#{i} {m["cat"]} pos={m["fa"]}-{m["fb"]} text={txt!r}')
            print(f'    before: {ctx!r}')
        for idx, ir in enumerate(rows_ir):
            if ir['kind'] == 'raw':
                r = filtered[idx][0] if pref == 'ST' else filtered[idx][1]
                print(f'  row#{idx} [raw] {normalize_for_match(r)[:95]!r}')
            elif ir['kind'] == 'dup':
                r = filtered[idx][0] if pref == 'ST' else filtered[idx][1]
                print(f'  row#{idx} [dup] {normalize_for_match(r)[:95]!r}')
