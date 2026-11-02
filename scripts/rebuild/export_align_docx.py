#!/usr/bin/env python3
"""
Xuất DOCX: APPENDIX 1 — bản dựng lại theo giao thức mới.

Nội dung mỗi cặp:
  (1) tóm tắt bản đồ câu + số liệu align (đã qua cổng kiểm 13);
  (2) bảng văn bản song song EN|VI với marking chuẩn:
      - nền màu 5 danh mục R/S/E/C/L (đúng màu như Appendix 1);
      - chữ mũ A/C/E trên khối R (3 hướng quy chiếu — 'đúng label 3 subset
        đối với Reference');
      - annotation kết quả căn cặp ngay sau mỗi khối đánh dấu (mũ nhỏ):
        → giữ · » dịch chuyển · ~ giữ-không-đánh-dấu · × bỏ · + thêm;
  (3) bảng align chi tiết từng tie (EN tie | kết quả | VI tie | ghi chú),
      phân biệt omitted-cut vs omitted-drop, added-real vs added-inventory.

Đầu vào:
  out/appendix1/appendix1_segments.json  (IR đánh dấu — tầng tin cậy)
  out/align_v2/PXX_align_v2.json         (bảng align v2 — cổng 13 PASS)
  out/align_v2/PXX_sent_map.json         (bản đồ câu)
  out/pairs/PXX/{ST,TT}_ties.json        (tiền trạm, loại phụ)
"""
import json
import os
import re

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = '/home/z/my-project'
IR_PATH = os.path.join(BASE, 'out', 'appendix1', 'appendix1_segments.json')
OUT_DIR = os.path.join(BASE, 'download', 'BDNC')
OUT_PATH = os.path.join(OUT_DIR, 'Appendix1_Align.docx')

BODY_FONT = 'Times New Roman'
HEAD_FONT = 'Calibri'

# ---------------------------------------------------------------- hệ màu
OUT_STYLE = {
    'kept':           {'bg': 'DCFCE7', 'fg': '14532D', 'vi': 'giữ',
                       'tag': '→', 'tag_fg': '15803D'},
    'shifted':        {'bg': 'FEF3C7', 'fg': '92400E', 'vi': 'dịch chuyển',
                       'tag': '»', 'tag_fg': 'B45309'},
    'kept_unmarked':  {'bg': 'F3F4F6', 'fg': '4B5563', 'vi': 'giữ, không đánh dấu',
                       'tag': '~', 'tag_fg': '6B7280'},
    'omitted_cut':    {'bg': 'FEE2E2', 'fg': '991B1B', 'vi': 'bỏ — khối cắt',
                       'tag': '×', 'tag_fg': 'DC2626'},
    'omitted_drop':   {'bg': 'FFE4E6', 'fg': '9F1239', 'vi': 'bỏ — vi-lược',
                       'tag': '×', 'tag_fg': 'DC2626'},
    'added_real':     {'bg': 'EDE9FE', 'fg': '5B21B6', 'vi': 'thêm — tự sinh',
                       'tag': '+', 'tag_fg': '7C3AED'},
    'added_inventory': {'bg': 'F5F3FF', 'fg': '6D28D9',
                         'vi': 'thêm — bất đối xứng kiểm kê',
                         'tag': '+', 'tag_fg': 'A78BFA'},
}


def outcome_key(row):
    if row['outcome'] == 'omitted':
        return 'omitted_cut' if row.get('om_kind') == 'cut' else 'omitted_drop'
    if row['outcome'] == 'added':
        return 'added_real' if row.get('added_kind') == 'added_real' \
            else 'added_inventory'
    return row['outcome']


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


def set_cell_margins(table, top=30, bottom=30, left=70, right=70):
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


def add_heading(doc, text, size=13, space_before=0, color='1A1A1A'):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = HEAD_FONT
    r.font.size = Pt(size)
    r.font.bold = True
    r.font.color.rgb = RGBColor.from_string(color)
    return p


def ranges_of(ids):
    """['S001','S002','S005'] -> 'S001–S002, S005'"""
    nums = sorted(int(x[1:]) for x in ids)
    out, start, prev = [], None, None
    for n in nums:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append(f'S{start:03d}' if start == prev
                       else f'S{start:03d}–S{prev:03d}')
            start = prev = n
    if start is not None:
        out.append(f'S{start:03d}' if start == prev else f'S{start:03d}–S{prev:03d}')
    return ', '.join(out)


# ---------------------------------------------------------------- marking
def fill_cell_marked(cell, side, cats, outcome_by_tie, size=9.5):
    """Ô văn bản có đánh dấu + mũ A/C/E + annotation kết quả align."""
    para = cell.paragraphs[0]
    para.paragraph_format.space_after = Pt(0)
    if side['kind'] in ('none', 'dup'):
        return
    if side['kind'] == 'raw':
        run = para.add_run(clean_raw(side['text']))
        run.font.name = BODY_FONT
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor.from_string('444444')
        return
    for seg in side['segs']:
        run = para.add_run(seg['t'])
        run.font.name = BODY_FONT
        run.font.size = Pt(size)
        cat = seg.get('cat')
        if not cat:
            continue
        c = cats[cat]
        shade_run(run, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
        run.font.bold = True
        # chữ mũ 3 hướng quy chiếu của Reference: A / C / E
        if cat == 'R' and seg.get('ref'):
            sup = para.add_run(seg['ref'])
            sup.font.name = BODY_FONT
            sup.font.size = Pt(size)
            sup.font.superscript = True
            shade_run(sup, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
            sup.font.bold = True
        # annotation kết quả căn cặp
        oc = outcome_by_tie.get(seg.get('id'))
        if oc:
            st = OUT_STYLE[oc]
            tag = para.add_run(st['tag'])
            tag.font.name = BODY_FONT
            tag.font.size = Pt(max(size - 2.0, 7.0))
            tag.font.superscript = True
            tag.font.bold = True
            tag.font.color.rgb = RGBColor.from_string(st['tag_fg'])


# ---------------------------------------------------------------- align tbl
def tie_desc(t, side):
    if not t:
        return '—'
    ref = f" ({t['ref']})" if t.get('cat') == 'R' and t.get('ref') else ''
    first = f"“{t['text']}” · {t['sent']} · {t['cat']}/{t.get('sub', '')}{ref}"
    second = ''
    if t.get('ante'):
        second = f"tiền trạm: {t['ante']}"
    return first, second


def fill_two_line(cell, line1, line2, size=8, l2size=7.5,
                  fg='1F2937', l2fg='6B7280', bg=None, bold1=False):
    para = cell.paragraphs[0]
    para.paragraph_format.space_after = Pt(0)
    r1 = para.add_run(line1)
    r1.font.name = BODY_FONT
    r1.font.size = Pt(size)
    r1.font.color.rgb = RGBColor.from_string(fg)
    r1.font.bold = bold1
    if bg:
        shade_cell(cell, bg)
    if line2:
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(line2)
        r2.font.name = BODY_FONT
        r2.font.size = Pt(l2size)
        r2.font.color.rgb = RGBColor.from_string(l2fg)


# ---------------------------------------------------------------- main
def build():
    ir = json.load(open(IR_PATH))
    cats = ir['cats']

    # nạp align v2 + bản đồ câu + ties
    data = {}
    for n in range(1, 21):
        pid = f'P{n:02d}'
        av = json.load(open(os.path.join(BASE, 'out', 'align_v2',
                                         f'{pid}_align_v2.json')))
        sm = json.load(open(os.path.join(BASE, 'out', 'align_v2',
                                         f'{pid}_sent_map.json')))
        st_ties = {t['id']: t for t in json.load(
            open(f'{BASE}/out/pairs/{pid}/ST_ties.json'))['ties']}
        tt_ties = {t['id']: t for t in json.load(
            open(f'{BASE}/out/pairs/{pid}/TT_ties.json'))['ties']}
        outcome_by_tie = {}
        for r in av['alignments']:
            k = outcome_key(r)
            if r.get('st_tie'):
                outcome_by_tie[r['st_tie']] = k
            if r.get('tt_tie') and r['outcome'] in ('kept', 'shifted'):
                outcome_by_tie[r['tt_tie']] = k
            elif r.get('tt_tie'):
                outcome_by_tie[r['tt_tie']] = k
        data[pid] = {'av': av, 'sm': sm, 'st': st_ties, 'tt': tt_ties,
                     'outcome_by_tie': outcome_by_tie}

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(1.5)
    sec.top_margin = sec.bottom_margin = Cm(1.5)
    normal = doc.styles['Normal']
    normal.font.name = BODY_FONT
    normal.font.size = Pt(9.5)
    normal.paragraph_format.space_after = Pt(4)

    # ---- título ----
    h = doc.add_paragraph()
    hr = h.add_run(
        'APPENDIX 1 — GÁN NHÃN LIÊN KẾT NGỮ PHÁP & BẢNG CĂN CẶP EN–VI '
        '(bản dựng lại theo giao thức mới)')
    hr.font.name = HEAD_FONT
    hr.font.size = Pt(15)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor.from_string('1A1A1A')

    intro = doc.add_paragraph()
    irun = intro.add_run(
        'Bản dựng lại theo giao thức mới của REPLICATION_GUIDE (Giai đoạn D, '
        'bước 12–13): bảng căn cặp (align) được viết lại từ BẢN ĐỒ CÂU của '
        'từng cặp — kết quả của việc phân tích thủ công 20 cặp trước khi '
        'marking thành phẩm — chứ không phải ghép theo thứ tự xuất hiện. '
        'Mỗi khối đánh dấu mang: (i) nền màu theo 5 danh mục liên kết '
        '(R/S/E/C/L); (ii) với Reference (R), chữ mũ một trong 3 hướng quy '
        'chiếu A = anaphoric, C = cataphoric, E = exophoric; (iii) annotation '
        'kết quả căn cặp ở dạng mũ nhỏ ngay sau khối. Mọi link đã qua cổng '
        'kiểm 13: tổng các kết quả khớp số tie hai đầu; cờ bỏ gắn đúng '
        'từng tie trong câu không dịch; link chỉ nhận khi câu VI nằm trong '
        'bản đồ câu của câu EN.')
    irun.font.size = Pt(9.5)
    irun.font.color.rgb = RGBColor.from_string('333333')

    # ---- legend 1: 5 danh mục ----
    add_heading(doc, 'Chú giải màu — 5 danh mục liên kết (Legend)', 11)
    lt = doc.add_table(rows=len(cats), cols=3)
    lt.style = 'Table Grid'
    lt.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins(lt)
    for i, (k, c) in enumerate(cats.items()):
        row = lt.rows[i]
        row.cells[0].width, row.cells[1].width, row.cells[2].width = \
            Cm(1.3), Cm(1.3), Cm(15.4)
        sw = row.cells[0].paragraphs[0]
        sw.alignment = WD_ALIGN_PARAGRAPH.CENTER
        swrun = sw.add_run(k)
        swrun.font.name = HEAD_FONT
        swrun.font.bold = True
        shade_run(swrun, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
        shade_cell(row.cells[0], c['bg'].lstrip('#'))
        cc = row.cells[1].paragraphs[0]
        crun = cc.add_run(k)
        crun.font.name = HEAD_FONT
        crun.font.bold = True
        dc = row.cells[2].paragraphs[0]
        drun = dc.add_run(f"{c['en']} — {c['vi']}")
        drun.font.name = BODY_FONT
        drun.font.size = Pt(9)

    add_note_para(
        doc,
        'Hướng tham chiếu của R — 3 nhãn con (chữ mũ trên khối R): '
        'A = anaphoric (hồi quy: tiền trạm trước), C = cataphoric (tiến chỉ: '
        'tiền trạm sau), E = exophoric (ngoại văn bản: người viết/độc giả). '
        'Toàn ngữ liệu không có C liên-câu. Chữ mũ E của quy chiếu khác ký '
        'hiệu danh mục E = lược bỏ (∅, nền xanh).')

    # ---- legend 2: outcome ----
    add_heading(doc, 'Chú giải annotation kết quả căn cặp (trên mỗi khối '
                    'đánh dấu, dạng mũ nhỏ)', 11)
    ot = doc.add_table(rows=len(OUT_STYLE) + 1, cols=3)
    ot.style = 'Table Grid'
    ot.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins(ot)
    hdr = ot.rows[0]
    for j, (w, txt) in enumerate(((Cm(1.2), 'Ký hiệu'),
                                  (Cm(4.2), 'Kết quả'),
                                  (Cm(12.6), 'Ý nghĩa'))):
        hdr.cells[j].width = w
        shade_cell(hdr.cells[j], 'EFEFEF')
        p = hdr.cells[j].paragraphs[0]
        r = p.add_run(txt)
        r.font.name = HEAD_FONT
        r.font.bold = True
        r.font.size = Pt(9)
    meanings = {
        'kept': 'Tie EN có tie VI đối dịch cùng referent (đọc lên thành cặp '
                'ngữ nghĩa hợp lý).',
        'shifted': 'Có đối dịch nhưng đổi danh mục (vd R>L: đại từ EN → '
                   'danh từ láy VI; L>zero: không còn hiện diện).',
        'kept_unmarked': 'Câu VI có dịch nhưng item hiện thực hóa bằng cụm '
                         'không được đánh dấu (first-mention, quy ước từng '
                         'ngôn ngữ) hoặc bị hấp thụ/gộp.',
        'omitted_cut': 'Tie nằm trong câu EN KHÔNG có bản dịch (khối cắt) — '
                       'cờ gắn theo tie, không theo mã câu.',
        'omitted_drop': 'Câu có dịch nhưng item không được render '
                        '(vi-lược trong dịch).',
        'added_real': 'Tie VI tự sinh: câu VI tự sinh (lede/byline/'
                      'paraphrase), câu trùng nguồn, hoặc quy chiếu tự sinh '
                      'trong câu đã dịch.',
        'added_inventory': 'Bất đối xứng kiểm kê: đối ứng EN tồn tại nhưng '
                           'không được đánh dấu (EN first-mention không tô '
                           'theo quy ước).',
    }
    for i, (k, st) in enumerate(OUT_STYLE.items(), start=1):
        row = ot.rows[i]
        row.cells[0].width, row.cells[1].width, row.cells[2].width = \
            Cm(1.2), Cm(4.2), Cm(12.6)
        shade_cell(row.cells[0], st['bg'])
        p0 = row.cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(st['tag'])
        r0.font.name = BODY_FONT
        r0.font.bold = True
        r0.font.size = Pt(11)
        r0.font.color.rgb = RGBColor.from_string(st['tag_fg'])
        fill_two_line(row.cells[1], st['vi'], None, size=8.5, bold1=True)
        fill_two_line(row.cells[2], meanings[k], None, size=8.5)

    add_note_para(
        doc,
        'Ví dụ cách đọc: "itᴬ→" = Reference hồi quy, có tie VI đối dịch; '
        '"Weᴱ+" (phía VI) = quy chiếu ngoại văn bản, tie VI tự sinh; '
        '"thoseᴬ×" = đại từ hồi quy rơi vào khối cắt.')

    # ---- bảng tổng 20 cặp ----
    add_heading(doc, 'Bảng tổng hợp 20 cặp — kết quả căn cặp theo giao thức '
                    'mới (đã qua cổng kiểm 13)', 11)
    cols = ['Cặp', 'ST\ntie', 'TT\ntie', 'giữ', 'dịch\nchuyển',
            'giữ\nkhông đd', 'bỏ\nkhối cắt', 'bỏ\nvi-lược',
            'thêm\nthật', 'thêm\nkiểm kê']
    stt = doc.add_table(rows=22, cols=len(cols))
    stt.style = 'Table Grid'
    stt.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins(stt, top=20, bottom=20, left=50, right=50)
    for j, cname in enumerate(cols):
        cell = stt.rows[0].cells[j]
        cell.width = Cm(1.83 if j else 1.4)
        shade_cell(cell, 'EFEFEF')
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(cname)
        r.font.name = HEAD_FONT
        r.font.bold = True
        r.font.size = Pt(8)
    set_repeat_header(stt.rows[0])
    tot = {k: 0 for k in ('st_ties', 'tt_ties', 'kept', 'shifted',
                          'kept_unmarked', 'omitted_cut', 'omitted_drop',
                          'added_real', 'added_inventory')}
    for i, n in enumerate(range(1, 21), start=1):
        pid = f'P{n:02d}'
        c = data[pid]['av']['counts']
        for k in tot:
            tot[k] += c[k]
        row = stt.rows[i]
        vals = [pid, c['st_ties'], c['tt_ties'], c['kept'], c['shifted'],
                c['kept_unmarked'], c['omitted_cut'], c['omitted_drop'],
                c['added_real'], c['added_inventory']]
        for j, v in enumerate(vals):
            cell = row.cells[j]
            cell.width = Cm(1.83 if j else 1.4)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j == 0 \
                else WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(str(v))
            r.font.name = BODY_FONT
            r.font.size = Pt(8.5)
            if j == 0:
                r.font.bold = True
            elif j >= 3:
                key = ['kept', 'shifted', 'kept_unmarked', 'omitted_cut',
                       'omitted_drop', 'added_real',
                       'added_inventory'][j - 3]
                shade_cell(cell, OUT_STYLE[key]['bg'])
                r.font.color.rgb = RGBColor.from_string(OUT_STYLE[key]['fg'])
    # hàng tổng
    row = stt.rows[21]
    vals = ['TỔNG', tot['st_ties'], tot['tt_ties'], tot['kept'],
            tot['shifted'], tot['kept_unmarked'], tot['omitted_cut'],
            tot['omitted_drop'], tot['added_real'], tot['added_inventory']]
    for j, v in enumerate(vals):
        cell = row.cells[j]
        cell.width = Cm(1.83 if j else 1.4)
        shade_cell(cell, 'F8FAFC')
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT if j == 0 \
            else WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(str(v))
        r.font.name = HEAD_FONT
        r.font.bold = True
        r.font.size = Pt(8.5)
    add_note_para(
        doc,
        f"Kiểm tra cổng 13 toàn bộ: giữ + dịch chuyển + giữ-không-đd + bỏ = "
        f"{tot['kept'] + tot['shifted'] + tot['kept_unmarked'] + tot['omitted_cut'] + tot['omitted_drop']}"
        f" = tổng ST tie ({tot['st_ties']}) ✓. Số giữ ở tầng tie gồm cả "
        f"giữ-không-đánh-dấu (đối ứng tồn tại nhưng không được tô theo quy "
        f"ước); số bỏ tách hai tầng: khối cắt (câu không dịch) và vi-lược "
        f"(item mất trong câu đã dịch). Cặp P03 (biên tập lại) và P15 (đảo "
        f"khối) dùng kèm cảnh báo trong phân tích cặp.")

    # ---- từng cặp ----
    for pair in ir['pairs']:
        pid = pair['id']
        d = data[pid]
        av, sm = d['av'], d['sm']
        c = av['counts']

        hp = doc.add_paragraph()
        hp.paragraph_format.page_break_before = True
        hp.paragraph_format.space_after = Pt(2)
        hp.paragraph_format.keep_with_next = True
        hpr = hp.add_run(f"Pair {pair['num']:02d}")
        hpr.font.name = HEAD_FONT
        hpr.font.size = Pt(13)
        hpr.font.bold = True

        if pair.get('title_en') or pair.get('title_vi'):
            tp = doc.add_paragraph()
            tp.paragraph_format.space_after = Pt(3)
            tp.paragraph_format.keep_with_next = True
            tr = tp.add_run(f"EN: {clean_raw(pair.get('title_en', ''))}")
            tr.font.name = BODY_FONT
            tr.font.size = Pt(9.5)
            tr.font.bold = True
            tp.add_run('\n')
            tr2 = tp.add_run(f"VI: {clean_raw(pair.get('title_vi', ''))}")
            tr2.font.name = BODY_FONT
            tr2.font.size = Pt(9.5)
            tr2.font.bold = True

        # bản đồ câu
        cut_r = ranges_of(sm['cut_en']) or 'không có'
        sg_r = ranges_of(sm['selfgen_vi']) or 'không có'
        dup_r = ranges_of(list(sm.get('dup_vi', {}))) or 'không có'
        mp = doc.add_paragraph()
        mp.paragraph_format.space_after = Pt(3)
        mr = mp.add_run(
            f"Bản đồ câu: {len(sm['en2vi'])}/{sm['n_en']} câu EN được dịch · "
            f"{len(sm['cut_en'])} câu bỏ ({cut_r}) · "
            f"{len(sm['selfgen_vi'])} câu VI tự sinh ({sg_r})"
            + (f" · câu VI trùng nguồn ({dup_r})"
               if sm.get('dup_vi') else ''))
        mr.font.size = Pt(8.5)
        mr.font.color.rgb = RGBColor.from_string('444444')
        if sm.get('caveat'):
            mr2 = mp.add_run(f"  ⚠ {sm['caveat']}")
            mr2.font.size = Pt(8.5)
            mr2.font.italic = True
            mr2.font.color.rgb = RGBColor.from_string('B45309')

        # dòng số liệu align
        ap = doc.add_paragraph()
        ap.paragraph_format.space_after = Pt(6)
        ar = ap.add_run(
            f"Align v2: giữ {c['kept']} · dịch chuyển {c['shifted']} · "
            f"giữ-không-đd {c['kept_unmarked']} · bỏ-khối {c['omitted_cut']} · "
            f"bỏ-vi-lược {c['omitted_drop']} · thêm-thật {c['added_real']} · "
            f"thêm-kiểm kê {c['added_inventory']}")
        ar.font.size = Pt(8.5)
        ar.font.color.rgb = RGBColor.from_string('444444')

        # ---- bảng văn bản đánh dấu ----
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
            fill_cell_marked(cells[0], row_ir['en'], cats,
                             d['outcome_by_tie'])
            fill_cell_marked(cells[1], row_ir['vi'], cats,
                             d['outcome_by_tie'])

        # ---- bảng align chi tiết ----
        add_heading(doc, f'Bảng căn cặp chi tiết — {pid} '
                        f'(mỗi dòng = 1 tie; ghi chú truy vết tiền trạm)',
                    10.5, space_before=8)
        rows = av['alignments']
        at = doc.add_table(rows=len(rows) + 1, cols=5)
        at.style = 'Table Grid'
        at.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_cell_margins(at, top=16, bottom=16, left=50, right=50)
        at.autofit = False
        widths = (Cm(0.9), Cm(5.4), Cm(2.7), Cm(5.0), Cm(5.0))
        hdrs = ('#', 'Tie EN (đơn vị · câu · loại)', 'Kết quả',
                'Tie VI (đơn vị · câu · loại)', 'Ghi chú')
        hrow = at.rows[0]
        for j, w in enumerate(widths):
            hrow.cells[j].width = w
            shade_cell(hrow.cells[j], 'EFEFEF')
            p = hrow.cells[j].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(hdrs[j])
            r.font.name = HEAD_FONT
            r.font.bold = True
            r.font.size = Pt(8)
        set_repeat_header(hrow)
        for i, rr in enumerate(rows, start=1):
            cells = at.rows[i].cells
            for j, w in enumerate(widths):
                cells[j].width = w
            k = outcome_key(rr)
            st_style = OUT_STYLE[k]
            # cột 0: số thứ tự
            p0 = cells[0].paragraphs[0]
            p0.paragraph_format.space_after = Pt(0)
            r0 = p0.add_run(str(i))
            r0.font.name = BODY_FONT
            r0.font.size = Pt(7.5)
            r0.font.color.rgb = RGBColor.from_string('6B7280')
            # cột 1: EN
            st_t = d['st'].get(rr.get('st_tie'))
            if st_t:
                l1, l2 = tie_desc(st_t, 'EN')
                fill_two_line(cells[1], l1, l2, size=8, l2size=7)
            else:
                fill_two_line(cells[1], '—', None, size=8,
                              l2fg='9CA3AF')
            # cột 2: kết quả
            fill_two_line(cells[2], st_style['vi'],
                          (rr.get('shift') or None), size=8,
                          bg=st_style['bg'], fg=st_style['fg'], bold1=True)
            # cột 3: VI
            tt_t = d['tt'].get(rr.get('tt_tie'))
            if tt_t:
                l1, l2 = tie_desc(tt_t, 'VI')
                fill_two_line(cells[3], l1, l2, size=8, l2size=7)
            else:
                fill_two_line(cells[3], '—', None, size=8, l2fg='9CA3AF')
            # cột 4: ghi chú
            note = rr.get('note') or ''
            if rr['outcome'] == 'shifted' and rr.get('shift'):
                note = f"[{rr['shift']}] " + note
            if len(note) > 220:
                note = note[:217] + '…'
            fill_two_line(cells[4], note, None, size=7.5, l2fg='6B7280')

    doc.core_properties.title = (
        'Appendix 1 — cohesion marking + alignment v2 (giao thức mới)')
    doc.core_properties.author = 'BDNC Group 9'
    doc.core_properties.subject = (
        'Cohesion annotation — Halliday & Hasan (1976) / Trần Ngọc Thêm '
        '(2006); alignment rebuilt per sent_map (gate 13)')

    os.makedirs(OUT_DIR, exist_ok=True)
    doc.save(OUT_PATH)
    print(f'Output: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)')
    print(f'Pairs: {len(ir["pairs"])}, tables: {len(doc.tables)}')


if __name__ == '__main__':
    build()
