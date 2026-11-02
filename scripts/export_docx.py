#!/usr/bin/env python3
"""
Appendix 1 — DOCX exporter.

Consumes out/appendix1/appendix1_segments.json (built by build_appendix_md.py)
and produces out/appendix1/Appendix1.docx: two-column EN|VI tables per pair,
tie runs shaded with the 5 category colours (w:shd run shading + font colour).

The HTML version carries the per-tie tooltips (danh mục, tiền trạm, độ tin
cậy); the DOCX keeps the same colours for print/offline review in Word.
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
OUT_PATH = os.path.join(BASE, 'out', 'appendix1', 'Appendix1.docx')

BODY_FONT = 'Times New Roman'
HEAD_FONT = 'Calibri'


# ---------------------------------------------------------------- helpers

def shade_run(run, fill, color=None):
    """Apply run-level shading (w:shd) + optional font colour."""
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
    """Markdown cell -> plain text for raw-fallback cells."""
    text = MD_LINK.sub(r'\1', text)
    text = text.replace('\\|', '|').replace('**', '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# ---------------------------------------------------------------- cell fill

def fill_cell(cell, side, cats, size=9.5):
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
        if cat:
            c = cats[cat]
            shade_run(run, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
            run.font.bold = True
            if cat == 'R' and seg.get('ref'):
                sup = para.add_run(seg['ref'])
                sup.font.name = BODY_FONT
                sup.font.size = Pt(size)
                sup.font.superscript = True
                shade_run(sup, c['bg'].lstrip('#'), c['fg'].lstrip('#'))
                sup.font.bold = True


# ---------------------------------------------------------------- document

def build():
    with open(IR_PATH, 'r', encoding='utf-8') as f:
        ir = json.load(f)
    cats = ir['cats']

    doc = Document()

    # page + base style
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
    hr = h.add_run(ir['title'])
    hr.font.name = HEAD_FONT
    hr.font.size = Pt(16)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor.from_string('1A1A1A')

    intro = doc.add_paragraph()
    irun = intro.add_run(ir['intro'])
    irun.font.size = Pt(9.5)
    irun.font.color.rgb = RGBColor.from_string('333333')

    # ---- legend table ----
    leg = doc.add_paragraph()
    lr = leg.add_run('Chú giải màu (Legend)')
    lr.font.name = HEAD_FONT
    lr.font.size = Pt(11)
    lr.font.bold = True

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

    # ---- R direction note ----
    refn = doc.add_paragraph()
    rr = refn.add_run(
        'Hướng tham chiếu (R): mỗi khối R kèm chữ mũ — A = anaphoric '
        '(hồi quy: tiền trạm nằm trước trong văn bản), C = cataphoric '
        '(tiến chỉ: tiền trạm nằm sau), E = exophoric (ngoại văn bản: tiền '
        'trạm trong bối cảnh phát ngôn — người viết / độc giả). Toàn ngữ '
        'liệu không có trường hợp C liên-câu. (Chữ mũ E này khác ký hiệu '
        'danh mục E = lược bỏ.)')
    rr.font.size = Pt(8.5)
    rr.font.italic = True
    rr.font.color.rgb = RGBColor.from_string('555555')

    # ---- framework correspondence table ----
    fw_head = doc.add_paragraph()
    fwr = fw_head.add_run('Khung lý thuyết / đối chiếu danh mục '
                          '(EN: Halliday & Hasan 1976 — VI: Trần Ngọc Thêm 2006)')
    fwr.font.name = HEAD_FONT
    fwr.font.size = Pt(11)
    fwr.font.bold = True

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

    fw_note = doc.add_paragraph()
    fnr = fw_note.add_run(
        'Đối chiếu gần đúng giữa hai khung: phép thế đại từ ≈ reference + '
        'substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ conjunction; '
        'phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng ≈ lexical '
        'cohesion.')
    fnr.font.size = Pt(8.5)
    fnr.font.italic = True
    fnr.font.color.rgb = RGBColor.from_string('555555')

    note = doc.add_paragraph()
    nrun = note.add_run(
        'Ký hiệu ∅ (nền xanh) = vị trí trống của phép lược bỏ (E). '
        'Bản đầy đủ có chú thích chi tiết từng liên kết (danh mục, tiền trạm, '
        'độ tin cậy) khi rê chuột: xem file Appendix1.html.')
    nrun.font.size = Pt(8.5)
    nrun.font.italic = True
    nrun.font.color.rgb = RGBColor.from_string('555555')

    # ---- pairs ----
    for pair in ir['pairs']:
        hp = doc.add_paragraph()
        hp.paragraph_format.page_break_before = True
        hpr = hp.add_run(f"Pair {pair['num']:02d}")
        hpr.font.name = HEAD_FONT
        hpr.font.size = Pt(13)
        hpr.font.bold = True
        hp.paragraph_format.space_after = Pt(2)
        hp.paragraph_format.keep_with_next = True

        # title row (bold, both languages)
        if pair.get('title_en') or pair.get('title_vi'):
            tp = doc.add_paragraph()
            tp.paragraph_format.space_after = Pt(4)
            tp.paragraph_format.keep_with_next = True
            tr = tp.add_run(
                f"EN: {clean_raw(pair.get('title_en', ''))}")
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

        # header row: EN | VI hyperlinks
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
            fill_cell(cells[0], row_ir['en'], cats)
            fill_cell(cells[1], row_ir['vi'], cats)

    # core properties
    doc.core_properties.title = ir['title']
    doc.core_properties.author = 'BDNC Group 9'
    doc.core_properties.subject = (
        'Cohesion annotation — Halliday & Hasan (1976) / Trần Ngọc Thêm (2006)')

    doc.save(OUT_PATH)
    print(f'Output: {OUT_PATH} ({os.path.getsize(OUT_PATH)} bytes)')
    print(f'Pairs: {len(ir["pairs"])}, '
          f'tables: {len(doc.tables)} (1 legend + {len(ir["pairs"])} pairs)')


if __name__ == '__main__':
    build()
