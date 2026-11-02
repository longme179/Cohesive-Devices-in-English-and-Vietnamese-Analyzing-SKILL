#!/usr/bin/env python3
"""Extract EN/VI parallel columns from Appendix 1 PDF (89 pages, 2-col layout)."""
import fitz, json, re, sys

PDF = '/home/z/my-project/upload/Appendix 1 - 20 pairs of articles.pdf'
SPLIT_X = 296  # boundary between EN (left) and VI (right) columns

def column_lines(page):
    """Return (left_lines, right_lines): each line = (y0, text)."""
    words = page.get_text('words')
    left, right = [], []
    for w in words:
        x0, y0, x1, y1, txt = w[0], w[1], w[2], w[3], w[4]
        # a word belongs to right col if its START is past the split
        (right if x0 >= SPLIT_X else left).append((y0, x0, txt))
    def to_lines(ws):
        ws.sort(key=lambda t: (round(t[0], 1), t[1]))
        lines, cur, cur_y = [], [], None
        for y, x, t in ws:
            if cur_y is None or abs(y - cur_y) <= 2.5:
                cur.append(t); cur_y = y if cur_y is None else cur_y
            else:
                lines.append((cur_y, ' '.join(cur))); cur, cur_y = [t], y
        if cur: lines.append((cur_y, ' '.join(cur)))
        return lines
    return to_lines(left), to_lines(right)

def lines_to_paras(lines):
    """Group column lines into paragraphs using y-gaps."""
    paras, cur, prev_y = [], [], None
    for y, txt in lines:
        if prev_y is not None and (y - prev_y) > 13.5:  # paragraph gap
            paras.append(' '.join(cur)); cur = []
        cur.append(txt); prev_y = y
    if cur: paras.append(' '.join(cur))
    return [re.sub(r'\s+', ' ', p).strip() for p in paras if p.strip()]

doc = fitz.open(PDF)
en_all, vi_all = [], []  # list of paragraphs in reading order per column
for pno in range(len(doc)):
    l, r = column_lines(doc[pno])
    en_all.extend(lines_to_paras(l))
    vi_all.extend(lines_to_paras(r))

print(f'EN paras: {len(en_all)}, VI paras: {len(vi_all)}', file=sys.stderr)
json.dump({'en': en_all, 'vi': vi_all}, open('/home/z/my-project/out/extracted_raw.json', 'w'), ensure_ascii=False, indent=1)
