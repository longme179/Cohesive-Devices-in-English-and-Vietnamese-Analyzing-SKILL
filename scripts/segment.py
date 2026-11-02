#!/usr/bin/env python3
"""Sentence segmentation for ST.txt / TT.txt.

Splits paragraphs into sentences, numbering S001, S002...
Abbreviations/numbers are protected (U.S., Mr., Dr., Jr., F., 1.5, TP.HCM,
472.088, e.g., v.v., ...). Ellipsis (… or spaced ...) does not split.
Manual fixes (merges) are read from <X>_seg_fixes.json and applied after
automatic splitting; the fixes never touch ST.txt/TT.txt.
Each sentence records its character span (fa, fb) in the canonical flow text
(paragraphs joined by newline == the .txt content) so that highlight markers
can be inserted at exact positions.
Output: out/pairs/PXX/ST_seg.json / TT_seg.json
        {paras: [...], sentences: [{id, para, text, fa, fb}]}
"""
import json, os, re, sys

OUT = '/home/z/my-project/out'

PROTECT = [
    r'(?:U\.S|U\.K|U\.N|E\.U|D\.C|N\.C|S\.C|Ph\.D|M\.S|B\.S)',
    r'(?:Mr|Mrs|Ms|Dr|Prof|St|Sen|Rep|Gen|Gov|Sgt|Capt|Lt|Col|Rev|Hon|Co|Inc|Ltd|Corp|vs|etc|approx|no)\.',
    r'\b(?:e\.g|i\.e|a\.m|p\.m)\.',
    r'\b[JrSr]\.',
    r'\b(?:TP|Tp|tp)\.HCM\b',
    r'\bv\.v\.',
    r'\d+\.\d+',          # 1.5, 3.5
    r'\d+\.\d{3}\b',      # 472.088 (VI thousands)
    r'\d{1,2}\.\d{1,2}\.\d{4}',  # 30.11.2024
    r'\b[A-Z]\.',         # initials F.
]
PROTECT_RE = [re.compile(p) for p in PROTECT]
CLOSERS = '\u201d"\u2019\')]' + '\u2026'

def protect(text):
    for rx in PROTECT_RE:
        out, last = [], 0
        for m in rx.finditer(text):
            out.append(text[last:m.start()])
            out.append(m.group().replace('.', '\x00'))
            last = m.end()
        out.append(text[last:])
        text = ''.join(out)
    text = text.replace('...', '\x01\x01\x01').replace('\u2026', '\x01')
    return text

def restore(text):
    return text.replace('\x00', '.').replace('\x01\x01\x01', '...').replace('\x01', '\u2026')

def segment(path_in, path_out, fixes_path):
    raw = open(path_in).read()
    paras = [p.strip() for p in raw.split('\n') if p.strip()]
    flow = '\n'.join(paras)
    offs, pos = [], 0
    for p in paras:
        offs.append(pos)
        pos += len(p) + 1
    # Soft-join paragraphs: fragments without terminal punctuation join the
    # next paragraph; real paragraph ends start new blocks.
    blocks = []  # (start_para, end_para, text)
    for pi, para in enumerate(paras):
        if blocks and not re.search(r'[.?!\u2026][' + re.escape(CLOSERS) + r']*$', blocks[-1][2]):
            b = blocks[-1]
            blocks[-1] = (b[0], pi, b[2] + ' ' + para)
        else:
            blocks.append((pi, pi, para))
    sentences = []
    for b0, b1, block in blocks:
        block_off = offs[b0]
        prot = protect(block)
        parts, cur, s0 = [], '', None
        i = 0
        while i < len(prot):
            c = prot[i]
            if s0 is None:
                s0 = i
            cur += c
            if c in '.?!':
                j = i + 1
                while j < len(prot) and prot[j] in CLOSERS:
                    cur += prot[j]; j += 1
                i = j
                if i >= len(prot) or prot[i] in ' \n\t':
                    parts.append((s0, s0 + len(cur)))
                    cur = ''
                    s0 = None
                    while i < len(prot) and prot[i] in ' \n\t':
                        i += 1
                continue
            i += 1
        if cur.strip():
            parts.append((s0, s0 + len(cur)))
        for (a, b) in parts:
            frag = block[a:b]
            t = restore(frag).strip()
            if not t:
                continue
            lead = len(frag) - len(frag.lstrip())
            trail = len(frag) - len(frag.rstrip())
            fa = block_off + a + lead
            fb = block_off + b - trail
            span = flow[fa:fb]
            if span != t:
                # sentences spanning paragraph joins differ only by ' ' vs '\n'
                ok = len(span) == len(t) and all(
                    (c1 == c2) or (c1 in ' \n' and c2 in ' \n')
                    for c1, c2 in zip(span, t))
                if not ok:
                    print(f'WARN: sentence span mismatch, cannot verify {t[:50]!r}')
                    fa = fb = -1
            sentences.append({'para': b0, 'text': t, 'fa': fa, 'fb': fb})
    # apply manual merge fixes
    if os.path.exists(fixes_path):
        fixes = json.load(open(fixes_path))
        for fx in fixes.get('merges', []):
            a, b = fx['from'], fx['to']
            i1, i2 = a - 1, b - 1
            if 0 <= i1 <= i2 < len(sentences):
                s1, s2 = sentences[i1], sentences[i2]
                merged = re.sub(r'\s+', ' ', flow[s1['fa']:s2['fb']]).strip()
                sentences[i1:i2+1] = [{'para': s1['para'], 'text': merged,
                                       'fa': s1['fa'], 'fb': s2['fb']}]
    for k, s in enumerate(sentences):
        s['id'] = f'S{k+1:03d}'
    json.dump({'paras': paras, 'sentences': sentences},
              open(path_out, 'w'), ensure_ascii=False, indent=1)
    return len(paras), len(sentences)

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    for i in range(1, 21):
        pid = f'P{i:02d}'
        if which not in ('all', pid):
            continue
        d = f'{OUT}/pairs/{pid}'
        for lang, pref in (('EN', 'ST'), ('VI', 'TT')):
            np_, ns = segment(f'{d}/{pref}.txt', f'{d}/{pref}_seg.json',
                              f'{d}/{pref}_seg_fixes.json')
            print(f'{pid} {lang}: {np_} paras -> {ns} sentences')
