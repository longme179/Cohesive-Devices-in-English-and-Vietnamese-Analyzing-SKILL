#!/usr/bin/env python3
"""Write summary.md for a pair and update progress.json. Usage: summarize.py P01"""
import json, sys, os
from collections import Counter

OUT = '/home/z/my-project/out'

def main(pid):
    d = f'{OUT}/pairs/{pid}'
    meta = json.load(open(f'{d}/meta.json'))
    st = json.load(open(f'{d}/ST_ties.json'))['ties']
    tt = json.load(open(f'{d}/TT_ties.json'))['ties']
    stseg = json.load(open(f'{d}/ST_seg.json'))['sentences']
    ttseg = json.load(open(f'{d}/TT_seg.json'))['sentences']
    al = json.load(open(f'{d}/align.json'))['alignments']
    c_st, c_tt = Counter(t['cat'] for t in st), Counter(t['cat'] for t in tt)
    c_al = Counter(r['outcome'] for r in al)
    conf_st = Counter(t['conf'] for t in st)
    conf_tt = Counter(t['conf'] for t in tt)

    # 3 most informative examples: highest-information shifts + a kept case
    ex_rows = [r for r in al if r['outcome'] == 'shifted']
    kept_rows = [r for r in al if r['outcome'] == 'kept']
    stmap = {t['id']: t for t in st}
    ttmap = {t['id']: t for t in tt}
    def fmt(r):
        s = stmap.get(r['st_tie'])
        t = ttmap.get(r['tt_tie'])
        return (f"- **{r['outcome']}{' / ' + r['shift'] if r['shift'] else ''}**: "
                f"ST {s['sent']} “{s['text']}” ({s['cat']}/{s['sub']}) → "
                f"TT {t['sent']} “{t['text']}” ({t['cat']}/{t['sub']}) — {r['note']}"
                if s and t else
                f"- **{r['outcome']}{' / ' + r['shift'] if r['shift'] else ''}**: "
                f"ST {s['sent']} “{s['text']}” ({s['cat']}/{s['sub']}) → no TT tie — {r['note']}")
    examples = [fmt(r) for r in ex_rows[:5]]
    if kept_rows:
        examples.append(fmt(kept_rows[0]))

    md = f'''# {pid} — Pair summary

**ST (English):** {meta['title_en']}
**TT (Vietnamese):** {meta['title_vi']}

## Counts

| | sentences | R | S | E | C | L | total | med/low conf |
|---|---|---|---|---|---|---|---|---|
| ST | {len(stseg)} | {c_st.get('R',0)} | {c_st.get('S',0)} | {c_st.get('E',0)} | {c_st.get('C',0)} | {c_st.get('L',0)} | {len(st)} | {conf_st.get('med',0)+conf_st.get('low',0)} |
| TT | {len(ttseg)} | {c_tt.get('R',0)} | {c_tt.get('S',0)} | {c_tt.get('E',0)} | {c_tt.get('C',0)} | {c_tt.get('L',0)} | {len(tt)} | {conf_tt.get('med',0)+conf_tt.get('low',0)} |

Alignment: kept {c_al.get('kept',0)}, shifted {c_al.get('shifted',0)},
omitted {c_al.get('omitted',0)}, added {c_al.get('added',0)}.

## Most informative examples

{chr(10).join(examples)}

## Notes

- No substitution (S) or ellipsis (E) ties in this pair: the only substitute
  items (ST "do the same" / TT "làm như vậy") are intra-sentential, outside the
  intersentential scope.
- Source-document defects kept as-is (see exclusions_log.json): duplicated
  sentence ST S031–S032; missing spaces TT S004, S012; EN S033 pull-quote block
  excluded as display element while its TT translation (TT S019) is body text.
- TT abridges the ending (EN S047–S049 partly unrendered).
'''
    with open(f'{d}/summary.md', 'w') as f:
        f.write(md)

    # progress.json
    prog_path = f'{OUT}/progress.json'
    prog = json.load(open(prog_path)) if os.path.exists(prog_path) else {'pairs': {}}
    prog['pairs'][pid] = {
        'status': 'done',
        'st_sentences': len(stseg), 'tt_sentences': len(ttseg),
        'st_ties': len(st), 'tt_ties': len(tt),
        'st_counts': dict(c_st), 'tt_counts': dict(c_tt),
        'alignment': dict(c_al),
        'qc': 'PASS',
    }
    prog['last_updated'] = 'auto'
    json.dump(prog, open(prog_path, 'w'), ensure_ascii=False, indent=1)
    print(f'{pid}: summary.md + progress.json written')

if __name__ == '__main__':
    main(sys.argv[1])
