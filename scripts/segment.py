#!/usr/bin/env python3
"""Sentence segmentation for ST.txt / TT.txt.

Splits paragraphs into sentences, numbering S001, S002...
Abbreviations/numbers are protected (U.S., Mr., Dr., Jr., F., 1.5, TP.HCM,
472.088, e.g., v.v., ...). Ellipsis (… or spaced ...) does not split.
Manual fixes (merges) are read from <X>_seg_fixes.json and applied after
automatic splitting; the fixes never touch ST.txt/TT.txt.
Output: out/pairs/PXX/ST_seg.json / TT_seg.json
        {paras: [...], sentences: [{id, para, text}]}
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

def protect(text):
    """Replace '.' in protected contexts with \\x00 placeholder."""
    for rx in PROTECT_RE:
        for m in rx.finditer(text):
            s, e = m.span()
            chunk = text[s:e].replace('.', '\x00')
            text = text[:s] + chunk + text[e:]
    # spaced ellipsis ... and direct …
    text = text.replace('...', '\x01\x01\x01').replace('…', '\x01')
    return text

def restore(text):
    return text.replace('\x00', '.').replace('\x01\x01\x01', '...').replace('\x01', '…')

SPLIT_RE = re.compile(r'(?<=[.?!])(?=[“"‘\'\(\[A-ZÀ-ỸĐ])')

def split_sentence(s):
    """Split one protected sentence string at sentence-final punctuation."""
    # find split points: [.?!]+ followed by optional closing quotes/brackets,
    # then whitespace before next sentence start
    out, buf = [], ''
    i = 0
    tokens = re.split(r'(\s+)', s)
    for tok in tokens:
        if re.fullmatch(r'\s+', tok):
            buf += tok
            continue
        buf += tok
        # does buf now end with sentence-final punct + closing quotes?
        m = re.search(r'([.?!]+[”"’\')\]]*)\s*$', buf)
        if m and m.group(1):
            out.append(buf.rstrip())
            buf = ''
    if buf.strip():
        out.append(buf)
    return [restore(x).strip() for x in out if x.strip()]

def segment(path_in, path_out, fixes_path):
    paras = [p.strip() for p in open(path_in).read().split('\n') if p.strip()]
    # Soft-join paragraphs: line-fragments (no terminal punctuation) join the
    # next paragraph; real paragraph ends (terminal punct) start new blocks.
    blocks = []  # (start_para_idx, text)
    for pi, para in enumerate(paras):
        if blocks and not re.search(r'[.?!…][”"’\')\]]*$', blocks[-1][1]):
            blocks[-1] = (blocks[-1][0], blocks[-1][1] + ' ' + para)
        else:
            blocks.append((pi, para))
    sentences = []
    for pi, block in blocks:
        prot = protect(block)
        parts, cur = [], ''
        i = 0
        while i < len(prot):
            c = prot[i]
            cur += c
            if c in '.?!':
                j = i + 1
                while j < len(prot) and prot[j] in '”"’\')]\u2026':
                    cur += prot[j]; j += 1
                i = j
                if i >= len(prot) or prot[i] in ' \n\t':
                    parts.append(cur)
                    cur = ''
                    while i < len(prot) and prot[i] in ' \n\t':
                        i += 1
                continue
            i += 1
        if cur.strip():
            parts.append(cur)
        for p in parts:
            t = restore(p).strip()
            if t:
                sentences.append({'para': pi, 'text': t})
    # apply manual merge fixes
    if os.path.exists(fixes_path):
        fixes = json.load(open(fixes_path))
        for fx in fixes.get('merges', []):
            a, b = fx['from'], fx['to']  # 1-based indices into sentences
            i1, i2 = a - 1, b - 1
            if 0 <= i1 <= i2 < len(sentences):
                merged = ' '.join(s['text'] for s in sentences[i1:i2+1])
                sentences[i1:i2+1] = [{'para': sentences[i1]['para'], 'text': merged}]
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
