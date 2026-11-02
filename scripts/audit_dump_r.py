#!/usr/bin/env python3
"""Dump all Reference (R) ties with sentence context for A/C/E review.

Tier 1 (needs careful reading): demonstrative, comparative, quantified,
1st/2nd-person pronouns, or any tie whose note mentions deixis/time/reader.
Tier 2 (compact): 3rd-person personal pronouns with a textual antecedent.
"""
import json
import os
import glob
import re

OUT = '/home/z/my-project/out'
AUD = '/home/z/my-project/out/audit'
os.makedirs(AUD, exist_ok=True)

FIRST_SECOND = {
    'i', 'we', 'us', 'our', 'ours', 'you', 'your', 'yours',
    'tôi', 'chúng tôi', 'chúng ta', 'chúng', 'mình', 'bạn', 'các bạn',
}

DEIXIS_HINT = re.compile(
    r'(this|that|these|those|here|now|today|tonight|week|month|year|decade|'
    r'century|này|đó|đây|kia|nay|hôm nay|tuần này|tháng này|năm nay|'
    r'hiện nay|hiện tại|reader|you|we|chúng ta|bạn)', re.I)


def sent_text(seg, sid):
    for s in seg['sentences']:
        if s['id'] == sid:
            return s['text']
    return ''


tier1, tier2 = [], []
for path in sorted(glob.glob(f'{OUT}/pairs/P*/ST_ties.json')) + \
             sorted(glob.glob(f'{OUT}/pairs/P*/TT_ties.json')):
    d = json.load(open(path))
    pid, lang = d['pair'], d['lang']
    pref = 'ST' if lang == 'EN' else 'TT'
    seg = json.load(open(path.replace('_ties.json', '_seg.json')))
    for t in d['ties']:
        if t['cat'] != 'R':
            continue
        stext = sent_text(seg, t['sent'])
        item = t['text'] or '∅'
        low = item.lower().strip()
        sub = t.get('sub', '')
        needs_context = (
            sub in ('demonstrative', 'comparative', 'quantified')
            or low in FIRST_SECOND
            or (t.get('note') and DEIXIS_HINT.search(t['note']))
            or (t.get('ante') and DEIXIS_HINT.search(str(t['ante'])) and sub != 'personal')
        )
        rec = {
            'id': t['id'], 'pid': pid, 'lang': lang, 'sub': sub,
            'item': item, 'sent': t['sent'], 'ante': t.get('ante', ''),
            'note': t.get('note') or '', 'alt': t.get('alt') or '',
            'conf': t.get('conf', ''), 'sentence': stext,
        }
        (tier1 if needs_context else tier2).append(rec)

with open(f'{AUD}/r_ties_tier1.txt', 'w', encoding='utf-8') as f:
    for r in tier1:
        s = r['sentence'].replace('\n', ' ')
        if len(s) > 360:
            # keep a window around the item
            i = s.lower().find(r['item'].lower())
            i = max(0, i - 160)
            s = ('…' if i else '') + s[i:i + 340] + '…'
        f.write(f"[{r['id']}] {r['sub']} | item={r['item']!r} | {r['sent']} "
                f"| ante={r['ante']!r} | conf={r['conf']}"
                + (f" | alt={r['alt']!r}" if r['alt'] else '')
                + (f" | note={r['note']}" if r['note'] else '') + '\n')
        f.write(f"    SENT: {s}\n\n")

with open(f'{AUD}/r_ties_tier2.txt', 'w', encoding='utf-8') as f:
    cur = None
    for r in sorted(tier2, key=lambda x: x['id']):
        if r['pid'] != cur:
            cur = r['pid']
            f.write(f"\n===== {cur} =====\n")
        f.write(f"[{r['id']}] {r['sub']} {r['item']!r} {r['sent']} "
                f"ante={r['ante']!r}"
                + (f" | note: {r['note']}" if r['note'] else '') + '\n')

print(f'tier1 (context review): {len(tier1)}')
print(f'tier2 (compact scan):  {len(tier2)}')
from collections import Counter
print('tier1 by sub:', Counter(r['sub'] for r in tier1))
print('tier2 by sub:', Counter(r['sub'] for r in tier2))
