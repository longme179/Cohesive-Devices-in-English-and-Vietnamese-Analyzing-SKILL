#!/usr/bin/env python3
"""Assemble Appendix1.md and Appendix1.html from per-pair outputs."""
import json, os, html as H

OUT = '/home/z/my-project/out'

def read(p):
    return open(p).read()

parts_md, parts_html = [], []
for i in range(1, 21):
    pid = f'P{i:02d}'
    d = f'{OUT}/pairs/{pid}'
    meta = json.load(open(f'{d}/meta.json'))
    st_md = read(f'{d}/ST_highlighted.md')
    tt_md = read(f'{d}/TT_highlighted.md')
    summ = read(f'{d}/summary.md')
    # strip the top-level header of TT md and summary to keep one H1 per pair
    tt_md_body = tt_md.split('---\n', 1)[1] if '---\n' in tt_md else tt_md
    summ_body = '\n'.join(summ.split('\n')[2:])  # drop '# Pxx — Pair summary' + blank
    parts_md.append(f"\n\n---\n\n{st_md}\n\n{tt_md_body}\n\n{summ_body}\n")
    # html: reuse each pair html body inside a wrapper
    st_html = read(f'{d}/{pid}.html')
    # extract body content between <p> after <hr> and </p></body>
    body = st_html.split('<hr>', 1)[1].rsplit('</p>\n</body>', 1)[0]
    parts_html.append(f'<section class="pair" id="{pid}"><h1>{pid}</h1>'
                      f'<p class="meta">{H.escape(meta["title_en"])}<br>{H.escape(meta["title_vi"])}</p>'
                      f'{body}</section>\n')

legend_html = ('<p class="legend">' + ' '.join(
    f'<span class="tie" style="background-color:{c}">{n}</span>'
    for c, n in (('#FFF176','Reference'),('#A5D6A7','Substitution'),('#90CAF9','Ellipsis'),
                 ('#FFCC80','Conjunction'),('#CE93D8','Lexical cohesion'))) + '</p>')
doc = f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Appendix 1 — Highlighted texts (20 pairs)</title>
<style>
body {{ font-family: Georgia, serif; max-width: 950px; margin: 2em auto; padding: 0 1em; line-height: 1.7; }}
h1 {{ font-size: 1.3em; border-bottom: 2px solid #333; padding-bottom: .3em; }}
section.pair {{ margin-bottom: 4em; }}
.legend span.tie {{ margin-right: 1em; padding: 0 .3em; }}
span.tie {{ padding: 0 1px; border-radius: 3px; cursor: help; }}
.meta {{ color: #555; }}
</style></head>
<body>
<h1>Appendix 1 — Highlighted texts, 20 English–Vietnamese pairs</h1>
<p>Source texts (ST, English) annotated with Halliday &amp; Hasan (1976);
target texts (TT, Vietnamese) annotated with Trần Ngọc Thêm (2006, as cited in
Nguyễn Thanh Tùng 2020), mapped onto the same five colours. Intersentential ties only.</p>
{legend_html}
{''.join(parts_html)}
</body></html>'''
os.makedirs(f'{OUT}/appendix1', exist_ok=True)
open(f'{OUT}/appendix1/Appendix1.html', 'w').write(doc)
header = '''# Appendix 1 — Highlighted texts, 20 English–Vietnamese pairs

Source texts (ST, English) annotated with Halliday & Hasan (1976); target texts (TT,
Vietnamese) annotated with Trần Ngọc Thêm (2006, as cited in Nguyễn Thanh Tùng 2020),
mapped onto the same five colours. Intersentential ties only.

**Legend:** 🟨 Reference (R) | 🟩 Substitution (S) | 🟦 Ellipsis (E) | 🟧 Conjunction (C) | 🟪 Lexical cohesion (L) — ellipsis gap: 🟦⟦∅⟧
'''
open(f'{OUT}/appendix1/Appendix1.md', 'w').write(header + '\n'.join(parts_md))
print('Appendix1.md/html written:',
      os.path.getsize(f'{OUT}/appendix1/Appendix1.md'), 'bytes md,',
      os.path.getsize(f'{OUT}/appendix1/Appendix1.html'), 'bytes html')
