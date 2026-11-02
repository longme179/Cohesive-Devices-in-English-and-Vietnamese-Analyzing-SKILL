#!/usr/bin/env python3
"""Extract 20 EN/VI pairs from the parallel PDF. v7.

Fixes over v6:
- Split: VI cell edge = min(vi_x0) (diacritic fragments start further right);
  EN edge = max(en_x1) among spans ending before vi_left+10 (excludes merged
  title-row spans that cross the whole table).
- Span join within a line: concatenate directly when x-gap <= 1.5pt (diacritic
  fragments), insert a space only for larger gaps.
- URL-fragment paragraphs (lowercase ASCII, no diacritics, contains '/') dropped.
- Title rows inside the table are NOT auto-dropped; handled per-pair in review.
Output: out/raw_pairs/PXX.json {en:[...], vi:[...], dropped:[...]} + _table.json
"""
import fitz, json, re, os, statistics

PDF = '/home/z/my-project/upload/Appendix 1 - 20 pairs of articles.pdf'
OUT = '/home/z/my-project/out'

PAIRS = [
    ('P01', 0, 9), ('P02', 9, 15), ('P03', 15, 21), ('P04', 21, 25),
    ('P05', 25, 31), ('P06', 31, 35), ('P07', 35, 40), ('P08', 40, 43),
    ('P09', 43, 48), ('P10', 48, 52), ('P11', 52, 58), ('P12', 58, 59),
    ('P13', 59, 62), ('P14', 62, 65), ('P15', 65, 73), ('P16', 73, 75),
    ('P17', 75, 78), ('P18', 78, 81), ('P19', 81, 83), ('P20', 83, 89),
]

BODY = {(11.0,'ArialMT'), (12.0,'ArialMT'), (12.0,'Roboto-Regular'),
        (13.5,'Roboto-Regular'), (10.5,'Roboto-Regular'), (15.0,'Georgia'),
        (15.0,'TimesNewRomanPSMT')}

JUNK_CHARS = '\u200b\ufeff\u00ad'
HEADER_VARIANTS = {'tiếng anh tiếng việt', 'en vi', 'eng vie'}

def clean(t):
    for c in JUNK_CHARS: t = t.replace(c, '')
    return t

def norm_head(t):
    t = re.sub(r'^(SL|TL):\s*', '', t)
    t = re.sub(r'[^a-z0-9àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ ]', '', t.lower())
    return re.sub(r'\s+', ' ', t).strip()[:40]

def page_spans(pno):
    """All spans: (y, x0, x1, style, text_raw). Leading/trailing spaces in
    span text are ESSENTIAL (word boundaries); only junk chars removed."""
    out = []
    for b in doc[pno].get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = clean(s['text'])
                if not t.strip(): continue
                style = (round(s['size'],1), s['font'])
                out.append((s['bbox'][1], s['bbox'][0], s['bbox'][2], style, t))
    out.sort(key=lambda t: (t[0], t[1]))
    return out

def header_y(spans):
    rows = {}
    for y, x0, x1, st, t in spans:
        rows.setdefault(round(y), []).append(t)
    for y in sorted(rows):
        joined = re.sub(r'\s+', ' ', ' '.join(rows[y])).strip().lower()
        if joined in HEADER_VARIANTS:
            return y
    return None

def extract(pid, start, end):
    dropped, en_stream, vi_stream = [], [], []
    for pno in range(start, end):
        spans = page_spans(pno)
        if not spans: continue
        hy = header_y(spans)
        # collect above-table headline text for title-row comparison
        above_head = ''
        kept = []
        for y, x0, x1, st, t in spans:
            ts = t.strip()
            if hy is not None and y < hy - 3:
                if not above_head: above_head = ts
                dropped.append({'page': pno, 'kind': 'above-table headline', 'text': ts[:90]})
                continue
            if st not in BODY: continue
            kept.append((y, x0, x1, st, t))
        spans = kept
        if not spans: continue
        # column split: VI cell edge = mode of vi x0 (every VI line starts at
        # the cell margin; diacritic fragments and EN strays are one-offs);
        # EN edge = max en x1 among spans ending before vi_left+10
        from collections import Counter
        vi_cands = [round(s[1]) for s in spans if 200 <= s[1] < 400]
        if vi_cands:
            cnt = Counter(vi_cands)
            mode_val, mode_n = cnt.most_common(1)[0]
            vi_left = float(mode_val) if mode_n >= 3 else float(min(vi_cands))
            en_x1 = [s[2] for s in spans if s[1] < 200 and s[2] < vi_left + 10]
            en_right = max(en_x1) if en_x1 else vi_left - 20
            sx = (en_right + vi_left) / 2
            if sx > vi_left - 0.5: sx = vi_left - 0.5
        else:
            sx = 296
        for y, x0, x1, st, t in spans:
            ts = t.strip()
            if re.match(r'^https?://', ts):
                dropped.append({'page': pno, 'kind': 'url', 'text': ts[:90]}); continue
            if ts in ('none', '(?)', '?'):
                dropped.append({'page': pno, 'kind': 'none-cell', 'text': ts}); continue
            if ts.lower() in ('tiếng anh', 'tiếng việt', 'en', 'vi', 'eng', 'vie'):
                dropped.append({'page': pno, 'kind': 'table-header', 'text': ts}); continue
            (en_stream if x0 < sx else vi_stream).append((pno, y, x0, x1, t))
    def to_paras(stream):
        # cluster to lines; join spans by x-gap (<=1.5pt = same word, no space)
        lines, cur, cur_y = [], [], None
        for pno, y, x0, x1, t in stream:
            if cur_y is None or abs(y - cur_y) <= 4.0:
                cur.append((x0, x1, t)); cur_y = y if cur_y is None else cur_y
            else:
                lines.append((cur_y, cur)); cur, cur_y = [(x0, x1, t)], y
        if cur: lines.append((cur_y, cur))
        # adaptive paragraph gaps
        gaps = [lines[i+1][0] - lines[i][0] for i in range(len(lines)-1)]
        med = statistics.median(gaps) if gaps else 15
        thr = med + 5
        paras, cur, prev = [], [], None
        for y, ws in lines:
            if prev is not None and (y - prev) > thr:
                paras.append(cur); cur = []
            cur.append(ws)
            prev = y
        if cur: paras.append(cur)
        res = []
        for p in paras:
            # join line-words with gap rule
            parts = []
            for ws in p:
                ws = sorted(ws)
                txt = ws[0][2]
                for i in range(1, len(ws)):
                    if ws[i][0] - ws[i-1][1] > 1.5:
                        txt += ' '
                    txt += ws[i][2]
                parts.append(txt)
            txt = re.sub(r'\s+', ' ', ' '.join(parts)).strip()
            if not txt: continue
            if txt in ('none', '(?)', '?'): continue
            if re.match(r'^https?://', txt): continue
            # URL fragment: pure ASCII lowercase-ish, has '/', no diacritics
            if '/' in txt and not re.search(r'[A-ZÀ-ỹ]', txt) and re.match(r'^[a-z0-9 ./_%-]+$', txt):
                continue
            res.append(txt)
        return res
    return to_paras(en_stream), to_paras(vi_stream), dropped

doc = fitz.open(PDF)
os.makedirs(f'{OUT}/raw_pairs', exist_ok=True)
table = []
for pid, start, end in PAIRS:
    en, vi, dropped = extract(pid, start, end)
    json.dump({'en': en, 'vi': vi, 'dropped': dropped},
              open(f'{OUT}/raw_pairs/{pid}.json','w'), ensure_ascii=False, indent=1)
    table.append({'pair': pid, 'pages': f'{start}-{end-1}',
                  'en_paras': len(en), 'vi_paras': len(vi),
                  'en_chars': sum(len(p) for p in en), 'vi_chars': sum(len(p) for p in vi),
                  'dropped': len(dropped)})
    print(f"{pid} pages {start}-{end-1}: EN {len(en)}p/{sum(len(p) for p in en)}ch, "
          f"VI {len(vi)}p/{sum(len(p) for p in vi)}ch, dropped {len(dropped)}")
json.dump(table, open(f'{OUT}/raw_pairs/_table.json','w'), ensure_ascii=False, indent=1)
