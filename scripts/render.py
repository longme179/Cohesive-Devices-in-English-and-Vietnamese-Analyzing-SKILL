#!/usr/bin/env python3
"""Render highlighted .md / .html for a pair and run QC. Reused for all pairs.

Renders (into out/pairs/PXX/):
  ST_highlighted.md / TT_highlighted.md  - notation: emoji + double brackets
  PXX.html                                - real background colours + tooltips
  qc.txt                                  - QC results

QC gates (all must pass):
  (a) each tie's text is found at its stated occurrence in its sentence
  (b) no marker spans overlap
  (c) removing all markers reproduces the .txt exactly, character for character
  (d) every antecedent sentence precedes the tie (follows it for cataphora)
  (e) counts per category are printed
Usage: python3 render.py P01
"""
import json, os, re, sys, html as htmlmod
from collections import Counter

OUT = '/home/z/my-project/out'

CATS = {
 'R': {'emoji': '\U0001F7E8', 'color': '#FFF176', 'name': 'Reference'},
 'S': {'emoji': '\U0001F7E9', 'color': '#A5D6A7', 'name': 'Substitution'},
 'E': {'emoji': '\U0001F7E6', 'color': '#90CAF9', 'name': 'Ellipsis'},
 'C': {'emoji': '\U0001F7E7', 'color': '#FFCC80', 'name': 'Conjunction'},
 'L': {'emoji': '\U0001F7EA', 'color': '#CE93D8', 'name': 'Lexical cohesion'},
}
SENT_RE = re.compile(r'S(\d{3})')

def span_ok(flow_span, text):
    if flow_span == text: return True
    return len(flow_span) == len(text) and all(
        (a == b) or (a in ' \n' and b in ' \n')
        for a, b in zip(flow_span, text))

def render_side(pid, pref, lang):
    d = f'{OUT}/pairs/{pid}'
    seg = json.load(open(f'{d}/{pref}_seg.json'))
    ties = json.load(open(f'{d}/{pref}_ties.json'))['ties']
    meta = json.load(open(f'{d}/meta.json'))
    flow = '\n'.join(seg['paras'])
    sents = {s['id']: s for s in seg['sentences']}
    qc = []
    fail = False

    # ---- compute marker positions in flow coordinates ----
    markers = []  # (a, b, tie) for text; (pos, pos, tie) for ellipsis
    for t in ties:
        s = sents.get(t['sent'])
        if s is None:
            qc.append(f'FAIL (a): {t["id"]}: sentence {t["sent"]} missing'); fail = True; continue
        if t['text'] is None:
            ga = t['gap_after']
            pos, found = -1, 0
            p = -1
            while True:
                p = s['text'].find(ga, p + 1)
                if p < 0: break
                found += 1
                if found == t['occ']:
                    pos = p + len(ga); break
            if pos < 0:
                qc.append(f'FAIL (a): {t["id"]}: gap_after {ga!r} occ {t["occ"]} not found'); fail = True; continue
            markers.append((s['fa'] + pos, s['fa'] + pos, t))
            continue
        # find occurrence t['occ'] of text within sentence text
        p, found = -1, 0
        a = b = -1
        while True:
            p = s['text'].find(t['text'], p + 1)
            if p < 0: break
            found += 1
            if found == t['occ']:
                a, b = p, p + len(t['text']); break
        if a < 0:
            qc.append(f'FAIL (a): {t["id"]}: occurrence {t["occ"]} of {t["text"]!r} not in {t["sent"]}'); fail = True; continue
        fa, fb = s['fa'] + a, s['fa'] + b
        if not span_ok(flow[fa:fb], t['text']):
            qc.append(f'FAIL (a): {t["id"]}: flow span mismatch for {t["text"]!r}'); fail = True; continue
        markers.append((fa, fb, t))

    # ---- overlap check (b) ----
    markers.sort(key=lambda m: (m[0], m[1]))
    for i in range(len(markers) - 1):
        a1, b1, t1 = markers[i]
        a2, b2, t2 = markers[i + 1]
        if a2 < b1:
            qc.append(f'FAIL (b): overlap {t1["id"]} [{a1},{b1}) vs {t2["id"]} [{a2},{b2})')
            fail = True
        elif a1 == b1 and a2 == b1 and a1 == a2:
            pass  # two point markers at same spot: allowed only if distinct
    # point marker inside a text marker?
    text_ms = [m for m in markers if m[0] < m[1]]
    point_ms = [m for m in markers if m[0] == m[1]]
    for pa, pb, pt in point_ms:
        for ta, tb, tt in text_ms:
            if ta < pa < tb:
                qc.append(f'FAIL (b): ellipsis {pt["id"]} inside span of {tt["id"]}')
                fail = True

    # ---- antecedent direction check (d) ----
    for t in ties:
        nums = [int(n) for n in SENT_RE.findall(t.get('ante') or '')]
        if not nums:
            qc.append(f'FAIL (d): {t["id"]}: ante has no sentence id: {t.get("ante")!r}')
            fail = True; continue
        tnum = int(SENT_RE.match(t['sent']).group(1))
        if t.get('dir', 'ana') == 'ana' and max(nums) >= tnum:
            qc.append(f'FAIL (d): {t["id"]}: ana antecedent {t["ante"]!r} not before {t["sent"]}')
            fail = True
        if t.get('dir') == 'cata' and min(nums) <= tnum:
            qc.append(f'FAIL (d): {t["id"]}: cata antecedent {t["ante"]!r} not after {t["sent"]}')
            fail = True

    # ---- insert markers (build marked flow) ----
    # insert from the end to keep positions valid; ties at same start: text first
    out = flow
    for a, b, t in sorted(markers, key=lambda m: (-m[0], -(m[1] if m[1] > m[0] else m[0]))):
        if a == b:  # ellipsis point
            out = out[:a] + f"{CATS['E']['emoji']}\u27E6\u2205\u27E7" + out[a:]
        else:
            out = out[:b] + '\u27E7' + out[b:]
            out = out[:a] + f"{CATS[t['cat']]['emoji']}\u27E6" + out[a:]

    # ---- QC (c): strip markers, compare ----
    stripped = out
    stripped = stripped.replace(CATS['E']['emoji'] + '\u27E6\u2205\u27E7', '')
    for c in CATS.values():
        stripped = stripped.replace(c['emoji'] + '\u27E6', '')
    stripped = stripped.replace('\u27E7', '')
    if stripped != flow:
        # locate first difference for the report
        i = 0
        while i < min(len(stripped), len(flow)) and stripped[i] == flow[i]:
            i += 1
        qc.append(f'FAIL (c): marker stripping changes text at char {i}: '
                  f'{stripped[max(0,i-30):i+30]!r} vs {flow[max(0,i-30):i+30]!r}')
        fail = True

    # ---- counts (e) ----
    counts = Counter(t['cat'] for t in ties)
    confs = Counter(t['conf'] for t in ties)

    # ---- write .md ----
    title = meta['title_en'] if lang == 'EN' else meta['title_vi']
    legend = ('**Legend:** ' + ' | '.join(
        f"{c['emoji']} {c['name']} (`{k}`)" for k, c in CATS.items()) +
        ' — ellipsis gap: \U0001F7E6\u27E6\u2205\u27E7')
    header = (f'# {pid} — {"Source text (ST, English)" if lang=="EN" else "Target text (TT, Vietnamese)"}\n\n'
              f'**Title:** {title}\n\n'
              f'**Framework:** ' + ('Halliday & Hasan (1976)' if lang == 'EN'
                                    else 'Trần Ngọc Thêm (2006), as cited in Nguyễn Thanh Tùng (2020)') + '\n\n'
              f'{legend}\n\n---\n\n')
    with open(f'{d}/{pref}_highlighted.md', 'w') as f:
        f.write(header + out + '\n')

    # ---- write .html ----
    # rebuild with html spans: walk markers again on flow
    parts = []
    last = 0
    events = []
    for a, b, t in markers:
        if a == b:
            events.append((a, b, t, 'point'))
        else:
            events.append((a, b, t, 'span'))
    # process left-to-right, tracking open spans (no overlaps guaranteed)
    for a, b, t, kind in events:
        if kind == 'point':
            parts.append(htmlmod.escape(flow[last:a]))
            tip = f"{CATS[t['cat']]['name']} ({t['cat']}/{t['sub']}) | gap after: {t.get('gap_after')} | recovered: {t.get('recovered')} | {t.get('ante','')}"
            parts.append(f'<span class="tie" style="background-color:{CATS["E"]["color"]}" title="{htmlmod.escape(tip)}">\u2205</span>')
            last = a
        else:
            parts.append(htmlmod.escape(flow[last:a]))
            tip = f"{CATS[t['cat']]['name']} ({t['cat']}/{t['sub']}) | {t.get('ante','')} | conf={t['conf']}"
            if t.get('alt'): tip += f" | alt: {t['alt']}"
            parts.append(f'<span class="tie" style="background-color:{CATS[t['cat']]['color']}" title="{htmlmod.escape(tip)}">{htmlmod.escape(flow[a:b])}</span>')
            last = b
    parts.append(htmlmod.escape(flow[last:]))
    body = ''.join(parts).replace('\n', '<br>\n')
    legend_html = '<p class="legend">' + ' '.join(
        f'<span class="tie" style="background-color:{c["color"]}">{c["emoji"]} {c["name"]}</span>'
        for k, c in CATS.items()) + '</p>'
    html_doc = f'''<!DOCTYPE html>
<html lang="{'en' if lang=='EN' else 'vi'}">
<head>
<meta charset="utf-8">
<title>{pid} — {htmlmod.escape(title)}</title>
<style>
body {{ font-family: Georgia, serif; max-width: 900px; margin: 2em auto; padding: 0 1em; line-height: 1.7; }}
h1 {{ font-size: 1.4em; }}
.legend span.tie {{ margin-right: 1em; padding: 0 .3em; }}
span.tie {{ padding: 0 1px; border-radius: 3px; cursor: help; }}
.meta {{ color: #555; font-size: .9em; }}
</style>
</head>
<body>
<h1>{pid} — {'Source text (ST, English)' if lang=='EN' else 'Target text (TT, Vietnamese)'}</h1>
<p class="meta"><b>Title:</b> {htmlmod.escape(title)}<br>
<b>Framework:</b> {htmlmod.escape('Halliday & Hasan (1976)' if lang=='EN' else 'Trần Ngọc Thêm (2006), as cited in Nguyễn Thanh Tùng (2020)')}<br>
<b>Ties:</b> {len(ties)} ({', '.join(f'{k}={v}' for k, v in sorted(counts.items()))})</p>
{legend_html}
<hr>
<p>
{body}
</p>
</body>
</html>
'''
    with open(f'{d}/{pid}.html', 'w') as f:
        f.write(html_doc)

    # ---- qc.txt ----
    status = 'PASS' if not fail else 'FAIL'
    qc.insert(0, f'QC {pid} {lang} ({pref}): {status}')
    qc.append(f'(e) counts: {dict(sorted(counts.items()))}')
    qc.append(f'confidence: {dict(sorted(confs.items()))}')
    qc.append(f'sentences: {len(seg["sentences"])}, ties: {len(ties)}')
    with open(f'{d}/{pref}_qc.txt', 'w') as f:
        f.write('\n'.join(qc) + '\n')
    print(f'{pid} {lang}: {status} — {len(ties)} ties, counts {dict(sorted(counts.items()))}')
    if fail:
        for line in qc[:12]:
            print('   ', line)
    return not fail

if __name__ == '__main__':
    pid = sys.argv[1]
    ok1 = render_side(pid, 'ST', 'EN')
    ok2 = render_side(pid, 'TT', 'VI')
    sys.exit(0 if (ok1 and ok2) else 1)
