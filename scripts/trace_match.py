#!/usr/bin/env python3
"""Trace row matching with fallback-level logging for failing pairs."""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_appendix_md as B

TARGET = sys.argv[1:] if len(sys.argv) > 1 else ['P01', 'P07', 'P08', 'P10', 'P15', 'P18']

# instrument find_range to log level
orig_find_range = B.HighlightExtractor.find_range
LEVEL = ['exact', 'heading', 'pfx60', 'pfx35', 'skipw', 'lastsent']

def traced_find_range(self, raw_text):
    q = B.normalize_for_match(raw_text)
    sp_before = self.search_pos
    res = orig_find_range(self, raw_text)
    if res:
        # determine level by comparing
        lvl = '?'
        nq = self.norm_text.find(q, sp_before)
        if nq == res[0]:
            lvl = 'exact'
        self._log.append((sp_before, res[0], res[1], lvl, q[:70]))
    else:
        self._log.append((sp_before, None, None, 'FAIL', q[:70]))
    return res

B.HighlightExtractor._log = []
B.HighlightExtractor.find_range = traced_find_range

raw_pairs = B.parse_raw_file()
for pair_id in TARGET:
    meta = json.load(open(os.path.join(B.PAIRS_DIR, pair_id, 'meta.json')))
    raw = raw_pairs[pair_id]
    title_en_norm = B.normalize_for_match(meta.get('title_en', ''))
    title_vi_norm = B.normalize_for_match(meta.get('title_vi', ''))
    filtered = []
    for en_raw, vi_raw in raw['rows']:
        en_n = B.normalize_for_match(en_raw) if en_raw != 'none' else ''
        vi_n = B.normalize_for_match(vi_raw) if vi_raw != 'none' else ''
        en_t = bool(title_en_norm) and len(en_n) > 10 and (en_n == title_en_norm or title_en_norm.startswith(en_n) or en_n.startswith(title_en_norm))
        vi_t = bool(title_vi_norm) and len(vi_n) > 10 and (vi_n == title_vi_norm or title_vi_norm.startswith(vi_n) or vi_n.startswith(title_vi_norm))
        if en_t and vi_t: continue
        if (en_t and vi_raw == 'none') or (vi_t and en_raw == 'none'): continue
        filtered.append((en_raw, vi_raw))
    for pref in ('ST', 'TT'):
        ext = B.HighlightExtractor(os.path.join(B.PAIRS_DIR, pair_id, f'{pref}_highlighted.md'), pair_id, pref)
        ext._log = []
        print(f'\n===== {pair_id} {pref} =====')
        for idx, (en_raw, vi_raw) in enumerate(filtered):
            r = en_raw if pref == 'ST' else vi_raw
            if r == 'none':
                continue
            dup = ext.is_duplicate(r)
            rng = ext.find_range(r)
            entry = ext._log[-1]
            if dup:
                kind = 'DUP'
                if rng: ext.search_pos = entry[0]  # find_range moved pos; undo for dup
            elif rng:
                segs = ext.segments(rng[0], rng[1])
                kind = f'segs[{entry[3]}]' if segs else 'EMPTY'
            else:
                kind = 'RAW'
            print(f'  r{idx:02d} {kind:12s} sp{entry[0]:5d}->{entry[1]} {B.normalize_for_match(r)[:60]!r}')
        miss = [i for i in range(len(ext.markers)) if i not in ext.consumed]
        print(f'  -> missing markers: {miss}')
