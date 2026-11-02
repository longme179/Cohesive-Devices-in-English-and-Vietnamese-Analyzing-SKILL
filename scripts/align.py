#!/usr/bin/env python3
"""Align ST and TT ties for a pair; write align.json.

Validates that every st_tie / tt_tie id exists, that outcomes are one of
kept/shifted/omitted, and auto-adds rows for TT ties never referenced
(outcome=added).
Usage: python3 align.py P01
"""
import json, sys, importlib

OUT = '/home/z/my-project/out'

def main(pid):
    st = json.load(open(f'{OUT}/pairs/{pid}/ST_ties.json'))['ties']
    tt = json.load(open(f'{OUT}/pairs/{pid}/TT_ties.json'))['ties']
    st_ids = {t['id'] for t in st}
    tt_ids = {t['id'] for t in tt}
    mod = importlib.import_module(f'align_tables.{pid}')
    added_notes = getattr(mod, 'ADDED_NOTES', {})
    rows, errors = [], []
    used_tt = set()
    for r in mod.A:
        st_id, tt_id, outcome, shift, note = r
        if st_id not in st_ids:
            errors.append(f'st_tie {st_id} not found'); continue
        if tt_id is not None and tt_id not in tt_ids:
            errors.append(f'tt_tie {tt_id} not found'); continue
        if outcome not in ('kept', 'shifted', 'omitted'):
            errors.append(f'bad outcome {outcome} for {st_id}'); continue
        if tt_id is None and outcome != 'omitted':
            errors.append(f'{st_id}: null tt_tie requires outcome=omitted'); continue
        if tt_id is not None: used_tt.add(tt_id)
        rows.append({'st_tie': st_id, 'tt_tie': tt_id, 'outcome': outcome,
                     'shift': shift, 'note': note})
    # added = TT ties never referenced
    stt = {t['id']: t for t in tt}
    for t in tt:
        if t['id'] not in used_tt:
            rows.append({'st_tie': None, 'tt_tie': t['id'], 'outcome': 'added',
                         'shift': None,
                         'note': added_notes.get(t['id'], 'no ST counterpart')})
    if errors:
        print(f'== {pid} ALIGN ERRORS ==')
        for e in errors: print('  ', e)
        return
    json.dump({'pair': pid, 'alignments': rows},
              open(f'{OUT}/pairs/{pid}/align.json', 'w'), ensure_ascii=False, indent=1)
    from collections import Counter
    c = Counter(r['outcome'] for r in rows)
    print(f'{pid}: {len(rows)} alignments, {dict(c)}')
    for t in tt:
        if t['id'] not in used_tt:
            print(f"  added: {t['id']} {t['sent']} {t['text']!r}")

if __name__ == '__main__':
    main(sys.argv[1])
