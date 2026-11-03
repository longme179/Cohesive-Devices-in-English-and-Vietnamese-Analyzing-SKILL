#!/usr/bin/env python3
"""
Xuất DOCX: APPENDIX 1 — bản TÔ LẠI (v2) theo giao thức mới.

Format GIỮ NGUYÊN như Appendix1.docx vòng trước (mỗi cặp = 1 bảng 2 cột
EN|VI, header có link nguồn), marking chuẩn:
  - nền màu 5 danh mục R/S/E/C/L (đúng màu như Appendix 1);
  - chữ mũ A/C/E trên khối R (3 hướng quy chiếu);
CỘNG THÊM (dựa vào bảng align v2 đã qua cổng kiểm 13):
  - annotation kết quả căn cặp ngay sau mỗi khối đánh dấu (mũ nhỏ màu):
    → giữ · » dịch chuyển · ~ giữ-không-đánh-dấu · × bỏ · + thêm;
    phía VI: nếu nhiều tie EN cùng đáp về một khối VI thì ưu tiên hiển thị
    'giữ' (→) — chi tiết gộp nằm trong comment;
  - comment Word trên TỪNG khối đánh dấu: id tie, danh mục/loại phụ, hướng
    quy chiếu, tiền trạm, độ tin cậy, kết quả căn cặp + đối tác EN/VI, ghi chú.

Đầu vào:
  out/appendix1/appendix1_segments.json  (IR đánh dấu — tầng tin cậy)
  out/align_v2/PXX_align_v2.json         (bảng align v2 — cổng 13 PASS)
  out/pairs/PXX/{ST,TT}_ties.json        (tiền trạm, loại phụ, conf)

Output:
  download/BDNC/Appendix1.docx (thay bản cũ) + out/appendix1/Appendix1.docx
"""
import json
import os
import re
import shutil

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

import os as _os
BASE = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
IR_PATH = os.path.join(BASE, 'out', 'appendix1', 'appendix1_segments.json')
OUT_DL = os.path.join(BASE, 'download', 'BDNC', 'Appendix1.docx')
OUT_ARTIFACT = os.path.join(BASE, 'out', 'appendix1', 'Appendix1.docx')

BODY_FONT = 'Times New Roman'
HEAD_FONT = 'Calibri'

COMMENT_AUTHOR = 'BDNC Group 9'
COMMENT_INITIALS = 'B9'

# ---------------------------------------------------------------- hệ màu
# 5 danh mục: lấy từ IR (R vàng / S xanh lá / E xanh dương / C cam / L tím)

# 7 kết quả căn cặp (align v2) — tag mũ nhỏ ngay sau khối đánh dấu
OUT_STYLE = {
    'kept':            {'bg': 'DCFCE7', 'fg': '14532D', 'vi': 'giữ',
                        'tag': '→', 'tag_fg': '15803D'},
    'shifted':         {'bg': 'FEF3C7', 'fg': '92400E', 'vi': 'dịch chuyển',
                        'tag': '»', 'tag_fg': 'B45309'},
    'kept_unmarked':   {'bg': 'F3F4F6', 'fg': '4B5563',
                        'vi': 'giữ, không đánh dấu',
                        'tag': '~', 'tag_fg': '6B7280'},
    'omitted_cut':     {'bg': 'FEE2E2', 'fg': '991B1B',
                        'vi': 'bỏ — khối cắt', 'tag': '×', 'tag_fg': 'DC2626'},
    'omitted_drop':    {'bg': 'FFE4E6', 'fg': '9F1239',
                        'vi': 'bỏ — vi-lược', 'tag': '×', 'tag_fg': 'BE123C'},
    'added_real':      {'bg': 'EDE9FE', 'fg': '5B21B6', 'vi': 'thêm — tự sinh',
                        'tag': '+', 'tag_fg': '7C3AED'},
    'added_inventory': {'bg': 'F5F3FF', 'fg': '6D28D9',
                        'vi': 'thêm — bất đối xứng kiểm kê',
                        'tag': '+', 'tag_fg': 'A78BFA'},
}

OUT_MEANING = {
    'kept': 'Tie EN có tie VI đối dịch cùng referent (bảng align v2 — đã qua '
            'cổng kiểm ngữ nghĩa).',
    'shifted': 'Có đối dịch nhưng đổi danh mục (vd R>L: đại từ EN → danh từ '
               'láy VI; L>zero: không còn hiện diện).',
    'kept_unmarked': 'Câu VI có dịch nhưng item hiện thực hóa bằng cụm '
                     'không được đánh dấu (first-mention / quy ước từng '
                     'ngôn ngữ) hoặc bị hấp thụ/gộp.',
    'omitted_cut': 'Tie nằm trong câu EN KHÔNG có bản dịch (khối cắt) — cờ '
                   'gắn theo tie, không theo mã câu.',
    'omitted_drop': 'Câu có dịch nhưng item không được render (vi-lược '
                    'trong dịch).',
    'added_real': 'Tie VI tự sinh: câu VI tự sinh (lede/byline/paraphrase), '
                  'câu trùng nguồn, hoặc quy chiếu tự sinh trong câu đã dịch.',
    'added_inventory': 'Bất đối xứng kiểm kê: đối ứng EN tồn tại nhưng không '
                       'được đánh dấu theo quy ước (first-mention không tô).',
}


# ---------------------------------------------------------------- helpers
def shade_run(run, fill, color=None):
    rPr = run._element.get_or_add_rPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    rPr.append(shd)
    if color:
        run.font.color.rgb = RGBColor.from_string(color)


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


def add_hyperlink(paragraph, url, text, size=9, bold=False):
    part = paragraph.part
    r_id = part.relate_to(
        url, 'http://schemas.openxmlformats.org/officeDocument/2006/'
             'relationships/hyperlink', is_external=True)
    link = OxmlElement('w:hyperlink')
    link.set(qn('r:id'), r_id)
    run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), HEAD_FONT)
    rFonts.set(qn('w:hAnsi'), HEAD_FONT)
    rPr.append(rFonts)
    c = OxmlElement('w:color')
    c.set(qn('w:val'), '0B57D0')
    rPr.append(c)
    u = OxmlElement('w:u')
    u.set(qn('w:val'), 'single')
    rPr.append(u)
    sz = OxmlElement('w:sz')
    sz.set(qn('w:val'), str(size * 2))
    rPr.append(sz)
    if bold:
        rPr.append(OxmlElement('w:b'))
    run.append(rPr)
    t = OxmlElement('w:t')
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader')
    el.set(qn('w:val'), 'true')
    trPr.append(el)


def set_cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    mar = OxmlElement('w:tblCellMar')
    for tag, val in (('top', top), ('left', left),
                     ('bottom', bottom), ('right', right)):
        el = OxmlElement(f'w:{tag}')
        el.set(qn('w:w'), str(val))
        el.set(qn('w:type'), 'dxa')
        mar.append(el)
    tblPr.append(mar)


MD_LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def clean_raw(text):
    text = MD_LINK.sub(r'\1', text)
    text = text.replace('\\|', '|').replace('**', '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def add_note_para(doc, text, size=8.5, italic=True, color='555555',
                  space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.italic = italic
    r.font.color.rgb = RGBColor.from_string(color)
    return p


def add_heading(doc, text, size=11, color='1A1A1A'):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = HEAD_FONT
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = RGBColor.from_string(color)
    return p


# ---------------------------------------------------------------- align v2
def outcome_key(row):
    if row['outcome'] == 'omitted':
        return 'omitted_cut' if row.get('om_kind') == 'cut' else 'omitted_drop'
    if row['outcome'] == 'added':
        return 'added_real' if row.get('added_kind') == 'added_real' \
            else 'added_inventory'
    return row['outcome']


def load_pair_data(pid):
    av = json.load(open(os.path.join(BASE, 'out', 'align_v2',
                                     f'{pid}_align_v2.json')))
    st_ties = {t['id']: t for t in json.load(
        open(f'{BASE}/out/pairs/{pid}/ST_ties.json'))['ties']}
    tt_ties = {t['id']: t for t in json.load(
        open(f'{BASE}/out/pairs/{pid}/TT_ties.json'))['ties']}
    en_row = {}
    vi_rows = {}
    for r in av['alignments']:
        if r.get('st_tie'):
            en_row[r['st_tie']] = r
        if r.get('tt_tie'):
            vi_rows.setdefault(r['tt_tie'], []).append(r)
    return {'av': av, 'st': st_ties, 'tt': tt_ties,
            'en_row': en_row, 'vi_rows': vi_rows}


def en_outcome(d, tid):
    r = d['en_row'].get(tid)
    return outcome_key(r) if r else None


def vi_outcome(d, tid):
    """Tag phía VI: nếu nhiều tie EN cùng đáp về khối này, ưu tiên 'giữ'."""
    rows = d['vi_rows'].get(tid)
    if not rows:
        return None
    outs = {r['outcome'] for r in rows}
    if 'kept' in outs:
        return 'kept'
    if 'shifted' in outs:
        return 'shifted'
    return outcome_key(rows[0])


# ---------------------------------------------------------------- comments
def tie_head(side, tid, tie):
    txt = tie.get('text') or '∅'
    ref = (f' · hướng {tie["ref"]}'
           if tie.get('cat') == 'R' and tie.get('ref') else '')
    lvl = f' · {tie.get("level", "LC")}'
    return (f'{side}·{tid} “{txt}” — {tie["cat"]}/{tie.get("sub", "")}'
            f'{ref}{lvl} · câu {tie.get("sent", "?")}')


def tie_ante_line(tie):
    bits = []
    if tie.get('cat') == 'E' and tie.get('gap_after'):
        bit = f'Vị trí trống sau: {tie["gap_after"]}'
        if tie.get('recovered'):
            bit += f' · hồi phục: {tie["recovered"]}'
        bits.append(bit)
    elif tie.get('ante'):
        bits.append(f'Tiền trạm: {tie["ante"]}')
    if tie.get('conf'):
        bits.append(f'conf={tie["conf"]}')
    return ' · '.join(bits)


def _q(t):
    return f'“{t}”' if t else '∅'


def build_comment_en(d, tid):
    tie = d['st'].get(tid)
    row = d['en_row'].get(tid)
    if not tie:
        return None
    lines = [tie_head('EN', tid, tie)]
    al = tie_ante_line(tie)
    if al:
        lines.append(al)
    if not row:
        lines.append('Bổ sung thủ công từ semantic_analysis (S/E) — '
                     'màu và level theo tie table.')
    note = (row or {}).get('note') or ''
    if tie.get('note'):
        note = (note + ' · ' if note else '') + f'note: {tie["note"]}'
    if note:
        lines.append(note)
    return '\n'.join(lines)


def build_comment_vi(d, tid):
    tie = d['tt'].get(tid)
    rows = d['vi_rows'].get(tid)
    if not tie:
        return None
    lines = [tie_head('VI', tid, tie)]
    al = tie_ante_line(tie)
    if al:
        lines.append(al)
    if not rows:
        lines.append('Bổ sung thủ công từ semantic_analysis (S/E) — '
                     'màu và level theo tie table.')
    note = (rows[0] if rows else {}).get('note') or ''
    if tie.get('note'):
        note = (note + ' · ' if note else '') + f'note: {tie["note"]}'
    if note:
        lines.append(note)
    return '\n'.join(lines)


# ---------------------------------------------------------------- cell fill
def fill_cell_marked(cell, side_ir, cats, d, size=9.5):
    """Ô văn bản: đánh dấu 5 màu + mũ A/C/E + comment."""
    para = cell.paragraphs[0]
    para.paragraph_format.space_after = Pt(0)
    if side_ir['kind'] in ('none', 'dup'):
        return
    if side_ir['kind'] == 'raw':
        run = para.add_run(clean_raw(side_ir['text']))
        run.font.name = BODY_FONT
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor.from_string('444444')
        return
    is_en = None  # xác định phía theo tiền tố id tie
    for seg in side_ir['segs']:
        run = para.add_run(seg['t'])
        run.font.name = BODY_FONT
        run.font.size = Pt(size)
        cat = seg.get('cat')
        if not cat:
            continue
        c = cats[cat]
        shade_run(run, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
        run.font.bold = True
        anchor = [run]
        tid = seg.get('id')
        # chữ mũ 3 hướng quy chiếu của Reference: A / C / E
        if cat == 'R' and seg.get('ref'):
            sup = para.add_run(seg['ref'])
            sup.font.name = BODY_FONT
            sup.font.size = Pt(size)
            sup.font.superscript = True
            shade_run(sup, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
            sup.font.bold = True
            anchor.append(sup)
        # comment Word: note đầy đủ của tie
        if tid:
            ctext = build_comment_en(d, tid) if tid.split('-')[1] == 'EN' \
                else build_comment_vi(d, tid)
            if ctext:
                for ch, repl in (('→', ' sang '), ('»', ''), ('~', ''),
                                 ('×', ''), ('+', '')):
                    ctext = ctext.replace(ch, repl)
                para.part.document.add_comment(
                    runs=anchor, text=ctext,
                    author=COMMENT_AUTHOR, initials=COMMENT_INITIALS)


# ---------------------------------------------------------------- main
def build():
    ir = json.load(open(IR_PATH))
    cats = ir['cats']

    data = {f'P{n:02d}': load_pair_data(f'P{n:02d}') for n in range(1, 21)}

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(1.5)
    sec.top_margin = sec.bottom_margin = Cm(1.6)
    normal = doc.styles['Normal']
    normal.font.name = BODY_FONT
    normal.font.size = Pt(9.5)
    normal.paragraph_format.space_after = Pt(4)

    # ---- title & intro ----
    h = doc.add_paragraph()
    hr = h.add_run(
        'Appendix 1 — 20 cặp bài báo EN–VI '
        '(đánh dấu ngữ nghĩa 5 màu)')
    hr.font.name = HEAD_FONT
    hr.font.size = Pt(15)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor.from_string('1A1A1A')

    intro = doc.add_paragraph()
    irun = intro.add_run(
        'Bản tiếng Anh (EN) đánh dấu theo Halliday & Hasan (1976); bản tiếng '
        'Việt (VI) đánh dấu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh '
        'Tùng 2020), quy về cùng thang 5 màu. Bản này đánh dấu các tie '
        'liên-câu (R/C/L) và BỔ SUNG THỦ CÔNG các vị trí phép thế (S) / phép '
        'tỉnh lược (E) đã phân tích trong download/BDNC/semantic_analysis — '
        'gồm cả [LC] liên câu và [TC] trong câu. Mỗi khối đánh dấu chỉ gồm '
        '(i) nền màu 5 danh mục; (ii) với Reference (R), chữ mũ một trong 3 '
        'hướng quy chiếu A/C/E. Không còn tag kết quả căn cặp. '
        'Comment Word (nếu cần tra cứu) vẫn chứa note của tie.')
    irun.font.size = Pt(9.5)
    irun.font.color.rgb = RGBColor.from_string('333333')

    # ---- legend 5 danh mục ----
    add_heading(doc, 'Chú giải màu — 5 danh mục liên kết (Legend)')
    lt = doc.add_table(rows=len(cats), cols=3)
    lt.style = 'Table Grid'
    lt.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins(lt)
    for i, (k, c) in enumerate(cats.items()):
        row = lt.rows[i]
        row.cells[0].width, row.cells[1].width, row.cells[2].width = \
            Cm(1.4), Cm(1.4), Cm(15.2)
        sw = row.cells[0].paragraphs[0]
        sw.alignment = WD_ALIGN_PARAGRAPH.CENTER
        swrun = sw.add_run(k)
        swrun.font.name = HEAD_FONT
        swrun.font.bold = True
        shade_run(swrun, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
        shade_cell(row.cells[0], c['bg'].lstrip('#'))
        cat_cell = row.cells[1].paragraphs[0]
        crun = cat_cell.add_run(k)
        crun.font.name = HEAD_FONT
        crun.font.bold = True
        desc = row.cells[2].paragraphs[0]
        drun = desc.add_run(f"{c['en']} — {c['vi']}")
        drun.font.name = BODY_FONT
        drun.font.size = Pt(9.5)

    add_note_para(
        doc,
        'Hướng tham chiếu (R): mỗi khối R kèm chữ mũ — A = anaphoric (hồi '
        'quy: tiền trạm nằm trước trong văn bản), C = cataphoric (tiến chỉ: '
        'tiền trạm nằm sau), E = exophoric (ngoại văn bản: tiền trạm trong '
        'bối cảnh phát ngôn — người viết / độc giả). Toàn ngữ liệu không có '
        'trường hợp C liên-câu. (Chữ mũ E này khác ký hiệu danh mục E = '
        'lược bỏ.)')

    # ---- framework correspondence table ----
    add_heading(doc, 'Khung lý thuyết / đối chiếu danh mục '
                     '(EN: Halliday & Hasan 1976 — VI: Trần Ngọc Thêm 2006)')
    fw_map = ir.get('framework_map') or []
    fwt = doc.add_table(rows=len(fw_map), cols=3)
    fwt.style = 'Table Grid'
    fwt.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins(fwt)
    for i, row in enumerate(fw_map):
        cells = fwt.rows[i].cells
        cells[0].width, cells[1].width, cells[2].width = \
            Cm(1.4), Cm(7.6), Cm(9.0)
        kcell = cells[0].paragraphs[0]
        kcell.alignment = WD_ALIGN_PARAGRAPH.CENTER
        krun = kcell.add_run(row['key'])
        krun.font.name = HEAD_FONT
        krun.font.bold = True
        cat = ir['cats'].get(row['key'])
        if cat:
            shade_run(krun, cat['bg'].lstrip('#'), cat['fg'].lstrip('#'))
            shade_cell(cells[0], cat['bg'].lstrip('#'))
        for fname, idx in (('en', 1), ('vi', 2)):
            pcell = cells[idx].paragraphs[0]
            prun = pcell.add_run(row[fname])
            prun.font.name = BODY_FONT
            prun.font.size = Pt(9)

    add_note_para(
        doc,
        'Đối chiếu gần đúng giữa hai khung: phép thế đại từ ≈ reference + '
        'substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ conjunction; '
        'phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng ≈ lexical '
        'cohesion.')

    add_note_para(
        doc,
        'Ký hiệu ∅ (nền xanh) = vị trí trống của phép lược bỏ (E). Mọi khối '
        'đánh dấu đều có comment Word (note đầy đủ: danh mục, hướng quy '
        'chiếu, tiền trạm, độ tin cậy, kết quả căn cặp, đối tác EN/VI, ghi '
        'chú). Số liệu căn cặp tổng hợp 20 cặp: bảng đầu file '
        'Appendix1_Align.docx.')

    # ---- pairs ----
    n_comments = 0
    for pair in ir['pairs']:
        pid = pair['id']
        d = data[pid]

        hp = doc.add_paragraph()
        hp.paragraph_format.page_break_before = True
        hpr = hp.add_run(f"Pair {pair['num']:02d}")
        hpr.font.name = HEAD_FONT
        hpr.font.size = Pt(13)
        hpr.font.bold = True
        hp.paragraph_format.space_after = Pt(2)
        hp.paragraph_format.keep_with_next = True

        if pair.get('title_en') or pair.get('title_vi'):
            tp = doc.add_paragraph()
            tp.paragraph_format.space_after = Pt(4)
            tp.paragraph_format.keep_with_next = True
            tr = tp.add_run(f"EN: {clean_raw(pair.get('title_en', ''))}")
            tr.font.name = BODY_FONT
            tr.font.size = Pt(10)
            tr.font.bold = True
            tp.add_run('\n')
            tr2 = tp.add_run(f"VI: {clean_raw(pair.get('title_vi', ''))}")
            tr2.font.name = BODY_FONT
            tr2.font.size = Pt(10)
            tr2.font.bold = True

        n_rows = len(pair['rows'])
        table = doc.add_table(rows=n_rows + 1, cols=2)
        table.style = 'Table Grid'
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_cell_margins(table)
        table.autofit = False

        hrow = table.rows[0]
        hrow.cells[0].width = hrow.cells[1].width = Cm(9.0)
        set_repeat_header(hrow)
        for j, (label, url) in enumerate(
                (('EN', pair.get('en_url', '')),
                 ('VI', pair.get('vi_url', '')))):
            cell = hrow.cells[j]
            shade_cell(cell, 'EFEFEF')
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if url:
                add_hyperlink(p, url, label, size=10, bold=True)
            else:
                r = p.add_run(label)
                r.font.name = HEAD_FONT
                r.font.size = Pt(10)
                r.font.bold = True

        for i, row_ir in enumerate(pair['rows'], start=1):
            cells = table.rows[i].cells
            cells[0].width = cells[1].width = Cm(9.0)
            fill_cell_marked(cells[0], row_ir['en'], cats, d)
            fill_cell_marked(cells[1], row_ir['vi'], cats, d)

    doc.core_properties.title = (
        'Appendix 1 — 20 cặp bài báo EN–VI (đánh dấu ngữ nghĩa 5 màu)')
    doc.core_properties.author = 'BDNC Group 9'
    doc.core_properties.subject = (
        'Cohesion annotation — Halliday & Hasan (1976) / Trần Ngọc Thêm '
        '(2006); 5-colour marking + A/C/E reference direction')

    doc.save(OUT_DL)
    shutil.copyfile(OUT_DL, OUT_ARTIFACT)

    # ---- QC summary ----
    from docx import Document as D2
    chk = D2(OUT_DL)
    n_shd = {}
    n_sup = 0
    for t in chk.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        rPr = r._element.rPr
                        if rPr is not None:
                            s = rPr.find(qn('w:shd'))
                            if s is not None:
                                fill = s.get(qn('w:fill'))
                                n_shd[fill] = n_shd.get(fill, 0) + 1
                        if r.font.superscript:
                            n_sup += 1
    n_cmt = 0
    for rel in chk.part.rels.values():
        if 'comments' in rel.reltype:
            n_cmt = rel.target_part.blob.decode('utf-8').count('<w:comment ')
    print(f'Output: {OUT_DL} ({os.path.getsize(OUT_DL)} bytes)')
    print(f'Pairs: {len(ir["pairs"])}, tables: {len(chk.tables)} '
          f'(1 legend + 1 framework + 20 pairs)')
    print(f'Shaded runs by fill: {n_shd}')
    print(f'Superscript runs: {n_sup} (A/C/E reference letters only)')
    print(f'Word comments: {n_cmt} (expect 3180)')


if __name__ == '__main__':
    build()
