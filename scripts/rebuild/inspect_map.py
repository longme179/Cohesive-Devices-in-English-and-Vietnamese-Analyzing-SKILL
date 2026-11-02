#!/usr/bin/env python3
"""Soát tay các câu tranh chấp trong sent_map draft: in câu EN (đánh dấu CUT?)
   kèm câu VI được map liền kề."""
import json
import sys

BASE = '/home/z/my-project'


def show(pid, en_ids, ctx=2):
    d = json.load(open(f'{BASE}/out/align_v2/{pid}_sent_map_draft.json'))
    st = {s['id']: s['text'] for s in json.load(
        open(f'{BASE}/out/pairs/{pid}/ST_seg.json'))['sentences']}
    tt = {s['id']: s['text'] for s in json.load(
        open(f'{BASE}/out/pairs/{pid}/TT_seg.json'))['sentences']}
    en2vi = d['en2vi']
    print(f'########## {pid}')
    for e in en_ids:
        tag = 'CUT' if e in d['cut_en'] else ('MAP->' + ','.join(en2vi.get(e, [])))
        print(f'--- EN {e} [{tag}]')
        print('  EN:', st.get(e, '??')[:200])
        # câu EN liền trước có map: in đối chiếu để phán đoán trôi
        for v in en2vi.get(e, []):
            print('  VI:', tt.get(v, '??')[:200])


if __name__ == '__main__':
    pid = sys.argv[1]
    ids = sys.argv[2:]
    show(pid, ids)
