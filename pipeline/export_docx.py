#!/usr/bin/env python3
"""Export Appendix 1 to DOCX from appendix1_segments.json.

Format: A4, 2-column EN|VI tables, one table per pair.  Every marked segment
gets the exact 5-colour fill; Reference keeps its A/C/E superscript.  No
outcome tags and no extra legend table beyond the 5 categories.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:  # pragma: no cover
    Document = None

from .common import CATS, FRAMEWORK_MAP, load_json

BODY = "Times New Roman"
HEAD = "Calibri"


def shade_run(run, fill, fg):
    rPr = run._element.get_or_add_rPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill.lstrip("#"))
    rPr.append(shd)
    run.font.color.rgb = RGBColor.from_string(fg.lstrip("#"))


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill.lstrip("#"))
    tcPr.append(shd)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def cell_margins(table, top=40, bottom=40, left=80, right=80):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for tag, val in (("top", top), ("left", left),
                     ("bottom", bottom), ("right", right)):
        el = OxmlElement(f"w:{tag}")
        el.set(qn("w:w"), str(val))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)


def hyperlink(paragraph, url, text, size=8.5, bold=False):
    part = paragraph.part
    r_id = part.relate_to(
        url, "http://schemas.openxmlformats.org/officeDocument/2006/"
             "relationships/hyperlink", is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), HEAD)
    rFonts.set(qn("w:hAnsi"), HEAD)
    rPr.append(rFonts)
    c = OxmlElement("w:color")
    c.set(qn("w:val"), "0B57D0")
    rPr.append(c)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), str(int(size * 2)))
    rPr.append(sz)
    if bold:
        rPr.append(OxmlElement("w:b"))
    run.append(rPr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = text
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def fill_cell(cell, side, size=9.5):
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    if side["kind"] == "none":
        return
    for seg in side["segs"]:
        run = p.add_run(seg["t"])
        run.font.name = BODY
        run.font.size = Pt(size)
        cat = seg.get("cat")
        if not cat:
            continue
        c = CATS[cat]
        shade_run(run, c["bg"], c["fg"])
        run.font.bold = True
        if cat == "R" and seg.get("ref"):
            sup = p.add_run(seg["ref"])
            sup.font.name = BODY
            sup.font.size = Pt(size)
            sup.font.superscript = True
            sup.font.bold = True
            shade_run(sup, c["bg"], c["fg"])


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Export Appendix 1 DOCX")
    ap.add_argument("--out", default="out/appendix1")
    ap.add_argument("--also", default=None, help="optional second output path")
    args = ap.parse_args(argv)
    if Document is None:
        print("ERROR: python-docx is required.  Install:\n"
              "  uv venv .venv && uv pip install --python .venv/bin/python "
              "python-docx", file=sys.stderr)
        return 2

    out = Path(args.out)
    ir = load_json(out / "appendix1_segments.json")
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(1.4)
    sec.top_margin = sec.bottom_margin = Cm(1.5)
    normal = doc.styles["Normal"]
    normal.font.name = BODY
    normal.font.size = Pt(9.5)
    normal.paragraph_format.space_after = Pt(4)

    h = doc.add_paragraph()
    r = h.add_run(ir["title"])
    r.font.name = HEAD
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = RGBColor.from_string("1A1A1A")

    intro = doc.add_paragraph()
    irun = intro.add_run(ir["intro"].replace("&amp;", "&"))
    irun.font.size = Pt(9.5)
    irun.font.color.rgb = RGBColor.from_string("333333")

    # legend 5 colours
    p = doc.add_paragraph()
    rr = p.add_run("Chú giải màu — 5 danh mục liên kết (Legend)")
    rr.font.name = HEAD
    rr.font.bold = True
    rr.font.size = Pt(11)
    lt = doc.add_table(rows=5, cols=3)
    lt.style = "Table Grid"
    lt.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_margins(lt)
    for i, (k, c) in enumerate(CATS.items()):
        row = lt.rows[i]
        row.cells[0].width = Cm(1.5)
        row.cells[1].width = Cm(1.5)
        row.cells[2].width = Cm(15.0)
        p0 = row.cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(k)
        r0.font.name = HEAD
        r0.font.bold = True
        shade_run(r0, c["bg"], c["fg"])
        shade_cell(row.cells[0], c["bg"])
        p1 = row.cells[1].paragraphs[0]
        r1 = p1.add_run(f'{c["emoji"]} {k}')
        r1.font.name = BODY
        r1.font.size = Pt(9)
        p2 = row.cells[2].paragraphs[0]
        r2 = p2.add_run(f'{c["en"]} — {c["vi"]}  ({c["bg"]})')
        r2.font.name = BODY
        r2.font.size = Pt(9)

    note = doc.add_paragraph()
    nr = note.add_run(
        "Hướng tham chiếu (R): A = anaphoric (hồi quy), C = cataphoric "
        "(tiến chỉ), E = exophoric (ngoại văn bản). ∅ (nền xanh) = vị trí "
        "trống của phép tỉnh lược. S/E có level [LC] liên câu hoặc [TC] trong "
        "câu theo quyết định thủ công của người phân tích.")
    nr.font.size = Pt(8.5)
    nr.font.italic = True
    nr.font.color.rgb = RGBColor.from_string("555555")

    p = doc.add_paragraph()
    fr = p.add_run("Khung lý thuyết / đối chiếu danh mục")
    fr.font.name = HEAD
    fr.font.bold = True
    fr.font.size = Pt(11)
    ft = doc.add_table(rows=5, cols=3)
    ft.style = "Table Grid"
    ft.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_margins(ft)
    for i, (k, en, vi) in enumerate(FRAMEWORK_MAP):
        row = ft.rows[i]
        row.cells[0].width, row.cells[1].width, row.cells[2].width = (
            Cm(1.5), Cm(8.0), Cm(8.5))
        p0 = row.cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r0 = p0.add_run(k)
        r0.font.name = HEAD
        r0.font.bold = True
        c = CATS[k]
        shade_run(r0, c["bg"], c["fg"])
        shade_cell(row.cells[0], c["bg"])
        for col, txt in ((1, en), (2, vi)):
            rr = row.cells[col].paragraphs[0].add_run(txt)
            rr.font.name = BODY
            rr.font.size = Pt(8.5)

    for pair in ir["pairs"]:
        h = doc.add_paragraph()
        hr = h.add_run(f'Pair {pair["num"]:02d}')
        hr.font.name = HEAD
        hr.font.size = Pt(12.5)
        hr.font.bold = True
        hr.font.color.rgb = RGBColor.from_string("1A1A1A")
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.keep_with_next = True

        t = doc.add_table(rows=2, cols=2)
        t.style = "Table Grid"
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell_margins(t)
        head = t.rows[0]
        for j, (url, label) in enumerate(((pair.get("en_url"), "EN"),
                                          (pair.get("vi_url"), "VI"))):
            cell = head.cells[j]
            cell.width = Cm(9.0)
            p0 = cell.paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if url:
                hyperlink(p0, url, label, size=8.5, bold=True)
            else:
                rr = p0.add_run(label)
                rr.font.name = HEAD
                rr.font.bold = True
                rr.font.size = Pt(8.5)
        repeat_header(head)
        tr = t.rows[1]
        tr.cells[0].width = Cm(9.0)
        tr.cells[1].width = Cm(9.0)
        for j, txt in enumerate((pair.get("title_en", ""),
                                 pair.get("title_vi", ""))):
            p0 = tr.cells[j].paragraphs[0]
            rr = p0.add_run(txt)
            rr.font.name = BODY
            rr.font.size = Pt(9.5)
            rr.font.bold = True

        for row in pair["rows"]:
            tr = t.add_row()
            tr.cells[0].width = Cm(9.0)
            tr.cells[1].width = Cm(9.0)
            fill_cell(tr.cells[0], row["en"])
            fill_cell(tr.cells[1], row["vi"])

    target = out / "Appendix1.docx"
    doc.save(target)
    if args.also:
        import shutil
        Path(args.also).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(target, args.also)

    # QC
    chk = Document(target)
    shd, sup = Counter(), 0
    for table in chk.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        rPr = r._element.rPr
                        if rPr is not None:
                            s = rPr.find(qn("w:shd"))
                            if s is not None:
                                shd[s.get(qn("w:fill"))] += 1
                        if r.font.superscript:
                            sup += 1
    print(f"Wrote {target} ({target.stat().st_size} bytes)")
    print(f"tables: {len(chk.tables)} | shaded runs: {dict(shd)} | "
          f"A/C/E superscripts: {sup}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
