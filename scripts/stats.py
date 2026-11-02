#!/usr/bin/env python3
"""Compute stats.csv, shifts.csv, spot_check.csv from ties + align files."""
import json, os, csv, random, re
from collections import Counter, defaultdict

OUT = '/home/z/my-project/out'
random.seed(42)

from pyvi import ViTokenizer

def count_words_en(text):
    return len(re.findall(r"[A-Za-z0-9]+(?:['\u2019-][A-Za-z0-9]+)*", text))

def count_words_vi(text):
    toks = ViTokenizer.tokenize(text).split()
    return len(toks)

# ---- stats.csv ----
rows = []
for i in range(1, 21):
    pid = f'P{i:02d}'
    d = f'{OUT}/pairs/{pid}'
    stt = json.load(open(f'{d}/ST_ties.json'))['ties']
    ttt = json.load(open(f'{d}/TT_ties.json'))['ties']
    sts = json.load(open(f'{d}/ST_seg.json'))['sentences']
    tts = json.load(open(f'{d}/TT_seg.json'))['sentences']
    st_txt = ' '.join(s['text'] for s in sts)
    tt_txt = ' '.join(s['text'] for s in tts)
    sc, tc = Counter(t['cat'] for t in stt), Counter(t['cat'] for t in ttt)
    scon = Counter(t['conf'] for t in stt)
    tcon = Counter(t['conf'] for t in ttt)
    for lang, cats, n_sent, n_words, ties, conf in (
        ('EN', sc, len(sts), count_words_en(st_txt), len(stt), scon),
        ('VI', tc, len(tts), count_words_vi(tt_txt), len(ttt), tcon)):
        rows.append({
            'pair': pid, 'language': lang, 'sentences': n_sent, 'words': n_words,
            'R': cats.get('R', 0), 'S': cats.get('S', 0), 'E': cats.get('E', 0),
            'C': cats.get('C', 0), 'L': cats.get('L', 0), 'total_ties': ties,
            'ties_per_sentence': round(ties / n_sent, 2) if n_sent else 0,
            'conf_high': conf.get('high', 0), 'conf_med': conf.get('med', 0),
            'conf_low': conf.get('low', 0),
        })
os.makedirs(f'{OUT}/appendix2', exist_ok=True)
with open(f'{OUT}/appendix2/stats.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print('stats.csv:', len(rows), 'rows')

# ---- shifts.csv ----
srows = []
for i in range(1, 21):
    pid = f'P{i:02d}'
    al = json.load(open(f'{OUT}/pairs/{pid}/align.json'))['alignments']
    for r in al:
        srows.append({'pair': pid, 'st_tie': r['st_tie'] or '', 'tt_tie': r['tt_tie'] or '',
                      'outcome': r['outcome'], 'shift': r['shift'] or '', 'note': r['note'] or ''})
with open(f'{OUT}/appendix2/shifts.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['pair', 'st_tie', 'tt_tie', 'outcome', 'shift', 'note'])
    w.writeheader(); w.writerows(srows)
print('shifts.csv:', len(srows), 'rows')

# ---- spot_check.csv ----
spot = []
for i in range(1, 21):
    pid = f'P{i:02d}'
    d = f'{OUT}/pairs/{pid}'
    for pref, lang in (('ST', 'EN'), ('TT', 'VI')):
        seg = json.load(open(f'{d}/{pref}_seg.json'))['sentences']
        sents = {s['id']: s['text'] for s in seg}
        ties = json.load(open(f'{d}/{pref}_ties.json'))['ties']
        for t in ties:
            if t['conf'] == 'low':
                spot.append({'pair': pid, 'language': lang, 'tie_id': t['id'],
                             'sent': t['sent'], 'sentence': sents.get(t['sent'], '')[:120],
                             'text': t['text'] or '(ellipsis)', 'cat': t['cat'], 'sub': t['sub'],
                             'ante': t['ante'], 'conf': t['conf'], 'reason': 'low confidence'})
# random sample of 6 per language x category
by_lc = defaultdict(list)
for i in range(1, 21):
    pid = f'P{i:02d}'
    d = f'{OUT}/pairs/{pid}'
    for pref, lang in (('ST', 'EN'), ('TT', 'VI')):
        seg = json.load(open(f'{d}/{pref}_seg.json'))['sentences']
        sents = {s['id']: s['text'] for s in seg}
        ties = json.load(open(f'{d}/{pref}_ties.json'))['ties']
        for t in ties:
            by_lc[(lang, t['cat'])].append((pid, t, sents))
sampled_ids = set()
for (lang, cat), items in sorted(by_lc.items()):
    sample = random.sample(items, min(6, len(items)))
    for pid, t, sents in sample:
        sampled_ids.add(t['id'])
        spot.append({'pair': pid, 'language': lang, 'tie_id': t['id'],
                     'sent': t['sent'], 'sentence': sents.get(t['sent'], '')[:120],
                     'text': t['text'] or '(ellipsis)', 'cat': t['cat'], 'sub': t['sub'],
                     'ante': t['ante'], 'conf': t['conf'], 'reason': 'random sample'})
with open(f'{OUT}/appendix2/spot_check.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['pair', 'language', 'tie_id', 'sent', 'sentence', 'text',
                                      'cat', 'sub', 'ante', 'conf', 'reason'])
    w.writeheader(); w.writerows(spot)
print('spot_check.csv:', len(spot), 'rows')

# ---- aggregate printout for Appendix 2 ----
agg = defaultdict(lambda: Counter())
for r in rows:
    for k in ('R', 'S', 'E', 'C', 'L', 'total_ties'):
        agg[r['language']][k] += r[k]
    agg[r['language']]['sentences'] += r['sentences']
    agg[r['language']]['words'] += r['words']
    agg[r['language']]['conf_med'] += r['conf_med']
    agg[r['language']]['conf_low'] += r['conf_low']
print(json.dumps({k: dict(v) for k, v in agg.items()}, indent=1))
# outcome aggregate
oc = Counter()
sh = Counter()
for r in srows:
    oc[r['outcome']] += 1
    if r['shift']:
        sh[r['shift']] += 1
print('outcomes:', dict(oc))
print('top shifts:', sh.most_common(12))
# med/low share
for lang in ('EN', 'VI'):
    tot = agg[lang]['total_ties']
    ml = agg[lang]['conf_med'] + agg[lang]['conf_low']
    print(f'{lang}: total {tot}, med+low {ml} ({100*ml/tot:.1f}%)')
json.dump({k: dict(v) for k, v in agg.items()}, open(f'{OUT}/appendix2/_aggregate.json', 'w'), indent=1)
json.dump({'outcomes': dict(oc), 'shifts': dict(sh)}, open(f'{OUT}/appendix2/_outcomes.json', 'w'), indent=1)
