#!/usr/bin/env python3
"""Row-level trace: kind, range, markers consumed per row."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_appendix_md import (HighlightExtractor, parse_raw_file, normalize_for_match,
                               PAIRS_DIR, _title_match)

PAIR = sys.argv[1] if len(sys.argv) > 1 else 'P15'
PREFS = sys.argv[2:] or ['ST', 'TT']

raw_pairs = parse_raw_file()
meta = json.load(open(os.path.join(PAIRS_DIR, PAIR, 'meta.json')))
raw = raw_pairs[PAIR]
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

for pref in PREFS:
    ext = HighlightExtractor(os.path.join(PAIRS_DIR, PAIR, f'{pref}_highlighted.md'), PAIR, pref)
    print(f'\n===== {PAIR} {pref} =====')
    prev_end = 0
    for idx, (en_raw, vi_raw) in enumerate(filtered):
        r = en_raw if pref == 'ST' else vi_raw
        if r == 'none':
            print(f'  r{idx:02d} none')
            continue
        if ext.is_duplicate(r):
            rng = ext.find_range(r)
            mk = ext.markers_in(rng[0], rng[1]) if rng else []
            if rng and mk:
                ext.search_pos = rng[1]
                segs = ext.segments(rng[0], rng[1])
                got = [m for _, m in mk]
                print(f'  r{idx:02d} DUP->segs [{rng[0]},{rng[1]}] markers={[m["cat"] for m in got]}')
            else:
                print(f'  r{idx:02d} DUP (rng={rng[:2] if rng else None})')
            continue
        rng = ext.find_range(r)
        if not rng:
            print(f'  r{idx:02d} RAW   sp={ext.search_pos} {normalize_for_match(r)[:60]!r}')
            continue
        a, b, off, rp = rng
        rep = ext.repair_gap(rng, r)
        ext.search_pos = b
        if rep:
            a2, rp2 = rep
            segs = ext.segments(a2, b)
            tag = f'segs+GAP[{a2},{b}] off={off} rp={rp2[:30]!r}'
        else:
            segs = ext.segments(a, b)
            tag = f'segs[{a},{b}] off={off}' + (f' rp={rp[:30]!r}' if rp else '')
        nmk = ext.rendered
        print(f'  r{idx:02d} {tag} rendered={ext.rendered} {normalize_for_match(r)[:55]!r}')
