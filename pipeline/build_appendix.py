#!/usr/bin/env python3
"""Build Appendix 1 markdown / HTML / segment IR from rendered pairs.

Outputs
-------
out/appendix1/Appendix1.md
out/appendix1/Appendix1.html
out/appendix1/appendix1_segments.json
out/appendix1/match_stats.json

The two-column layout follows the original table rows, so empty VI cells (a
cut sentence) stay empty.  Every marked span keeps its 5-colour category, and
Reference spans keep their manual A/C/E superscript.  Outcome tags (→ » ~ × +)
are deliberately NOT emitted in this skill version.
"""
from __future__ import annotations

import argparse
import html as H
import json
import sys
from collections import Counter
from pathlib import Path

from .common import (CATS, FRAMEWORK_MAP, REF_NAMES, dump_json, load_json,
                     pair_ids)
from .render import markers_for

PAD = "padding:1px 4px;border-radius:3px"
INTRO = (
    "Bản tiếng Anh (EN) đánh dấu theo Halliday & Hasan (1976); bản tiếng "
    "Việt (VI) đánh dấu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh Tùng "
    "2020), quy về cùng thang 5 màu. Trọng tâm là COHESION BEYOND THE SENTENCE "
    "LEVEL: các tie liên-câu (R/C/L) được phân tích thủ công từng cặp; lớp S/E "
    "bổ sung các vị trí phép thế / tỉnh lược đã đọc và quyết định bằng tay, gồm "
    "cả [LC] liên câu và [TC] trong câu. Mỗi khối chỉ gồm nền màu 5 danh mục "
    "và — với Reference — chữ mũ hướng A/C/E. Không có tag kết quả căn cặp."
)


def row_starts(paras: list[str]) -> list[int]:
    out, pos = [], 0
    for p in paras:
        out.append(pos)
        pos += len(p) + 1
    return out


def side_ir(flow: str, text: str, markers, start: int, end: int):
    if not text:
        return {"kind": "none", "segs": []}
    rel = [m for m in markers if start <= m[0] and m[1] <= end]
    segs, last = [], start
    for a, b, t in rel:
        if a > last:
            segs.append({"t": flow[last:a]})
        if a == b:
            segs.append({"t": "∅", "cat": "E", "id": t["id"],
                         "level": t.get("level", "LC"), "point": True})
        else:
            segs.append({"t": flow[a:b], "cat": t["cat"], "id": t["id"],
                         "ref": t.get("ref"), "level": t.get("level", "LC")})
        last = b
    if last < end:
        segs.append({"t": flow[last:end]})
    return {"kind": "segs", "segs": segs}


def md_escape(s: str) -> str:
    return H.escape(s, quote=False).replace("|", "\\|")


def md_side(side: dict) -> str:
    if side["kind"] == "none":
        return ""
    bits = []
    for seg in side["segs"]:
        t = md_escape(seg["t"])
        cat = seg.get("cat")
        if not cat:
            bits.append(t)
            continue
        c = CATS[cat]
        sup = (f'<sup>{seg["ref"]}</sup>'
               if cat == "R" and seg.get("ref") else "")
        title = (f'{c["en"]} ({cat})' +
                 (f' · {seg["level"]}' if seg.get("level") else ""))
        bits.append(f'<span style="background-color:{c["bg"]};color:{c["fg"]};'
                    f'{PAD}" title="{H.escape(title)}">{t}{sup}</span>')
    return "".join(bits)


def html_side(side: dict) -> str:
    if side["kind"] == "none":
        return ""
    bits = []
    for seg in side["segs"]:
        t = H.escape(seg["t"])
        cat = seg.get("cat")
        if not cat:
            bits.append(t)
            continue
        c = CATS[cat]
        sup = (f'<sup>{seg["ref"]}</sup>'
               if cat == "R" and seg.get("ref") else "")
        tip = f'{c["en"]} ({cat}) · {seg.get("level", "LC")}'
        bits.append(f'<span class="tie" style="background-color:{c["bg"]};'
                    f'color:{c["fg"]}" title="{H.escape(tip)}">{t}{sup}</span>')
    return "".join(bits)


def build(work: Path, out: Path):
    pids = pair_ids(work)
    pairs_ir, md_parts, html_parts = [], [], []
    grand = Counter()
    stats = {}

    for pid in pids:
        d = work / "pairs" / pid
        for pref in ("ST", "TT"):
            qc = d / f"{pref}_qc.txt"
            if not qc.exists() or not qc.read_text(encoding="utf-8").startswith("QC") or "PASS" not in qc.read_text(encoding="utf-8").splitlines()[0]:
                raise SystemExit(f"QC gate failed: {qc} missing or not PASS")
        meta = load_json(d / "meta.json")
        rows = load_json(d / "rows.json")
        st_seg = load_json(d / "ST_seg.json")
        tt_seg = load_json(d / "TT_seg.json")
        st_m = markers_for(st_seg, load_json(d / "ST_ties.json")["ties"])
        tt_m = markers_for(tt_seg, load_json(d / "TT_ties.json")["ties"])
        st_flow = st_seg.get("flow") or "\n".join(st_seg["paras"])
        tt_flow = tt_seg.get("flow") or "\n".join(tt_seg["paras"])
        st_starts = row_starts(st_seg["paras"])
        tt_starts = row_starts(tt_seg["paras"])
        n = max(len(st_seg["paras"]), len(tt_seg["paras"]))

        rows_ir = []
        md_rows, html_rows = [], []
        for i in range(n):
            en_text = st_seg["paras"][i] if i < len(st_seg["paras"]) else ""
            vi_text = tt_seg["paras"][i] if i < len(tt_seg["paras"]) else ""
            en_start = st_starts[i] if i < len(st_starts) else 0
            vi_start = tt_starts[i] if i < len(tt_starts) else 0
            en = side_ir(st_flow, en_text, st_m, en_start,
                         en_start + len(en_text))
            vi = side_ir(tt_flow, vi_text, tt_m, vi_start,
                         vi_start + len(vi_text))
            rows_ir.append({"en": en, "vi": vi})
            md_rows.append(f"| {md_side(en)} | {md_side(vi)} |")
            html_rows.append(f"<tr><td>{html_side(en)}</td>"
                             f"<td>{html_side(vi)}</td></tr>")

        used = Counter()
        for row in rows_ir:
            for side_key in ("en", "vi"):
                for seg in row[side_key].get("segs", []):
                    if seg.get("id"):
                        used[seg["id"]] += 1
        all_ids = {t["id"] for _, _, t in st_m} | {t["id"] for _, _, t in tt_m}
        lost = sorted(all_ids - set(used))
        if lost:
            raise SystemExit(f"{pid}: {len(lost)} tie(s) fell outside every "
                             f"row: {lost[:5]}")
        for side, markers in (("en", st_m), ("vi", tt_m)):
            c = Counter(t["cat"] for _, _, t in markers)
            grand.update({side: len(markers)})
            stats.setdefault(pid, {})[side] = {
                "markers": len(markers), "by_cat": dict(sorted(c.items()))
            }

        en_url, vi_url = meta.get("en_url", ""), meta.get("vi_url", "")
        en_head = f"[EN]({en_url})" if en_url else "EN"
        vi_head = f"[VI]({vi_url})" if vi_url else "VI"
        md_parts += [f"## Pair {meta['num']:02d}", "",
                     f"| {en_head} | {vi_head} |", "| :--- | :--- |",
                     f"| **{md_escape(meta.get('title_en',''))}** | "
                     f"**{md_escape(meta.get('title_vi',''))}** |",
                     *md_rows, ""]
        h_en = f'<a href="{H.escape(en_url, quote=True)}">EN</a>' if en_url else "EN"
        h_vi = f'<a href="{H.escape(vi_url, quote=True)}">VI</a>' if vi_url else "VI"
        html_parts.append(
            f'<h2 id="{pid}">Pair {meta["num"]:02d}</h2><table>'
            f"<tr><th>{h_en}</th><th>{h_vi}</th></tr>"
            f'<tr class="titles"><td><b>{H.escape(meta.get("title_en",""))}</b></td>'
            f'<td><b>{H.escape(meta.get("title_vi",""))}</b></td></tr>'
            + "".join(html_rows) + "</table>")
        pairs_ir.append({
            "id": pid, "num": meta["num"],
            "en_url": en_url, "vi_url": vi_url,
            "title_en": meta.get("title_en", ""),
            "title_vi": meta.get("title_vi", ""),
            "rows": rows_ir,
        })

    legend_md = ["**Chú giải màu (Legend):**", "",
                 "| Màu | Ký hiệu | Danh mục | HEX |", "| :--- | :--- | :--- | :--- |"]
    for k, c in CATS.items():
        legend_md.append(
            f'| <span style="background-color:{c["bg"]};color:{c["fg"]};'
            f'{PAD}">&nbsp;{k}&nbsp;</span> | {c["emoji"]} {k} | '
            f'{c["en"]} — {c["vi"]} | `{c["bg"]}` |')
    legend_md += ["", "> ∅ (nền xanh) = vị trí trống của phép tỉnh lược (E). "
                  "S/E có level `[LC]` (liên câu) hoặc `[TC]` (trong câu) trong "
                  "tooltip/comment. Chữ mũ trên R: A = anaphoric, "
                  "C = cataphoric, E = exophoric."]

    title = f"Appendix 1 — {len(pids)} cặp bài báo EN–VI (đánh dấu ngữ nghĩa)"
    md = (f"# {title}\n\n"
          + INTRO + "\n\n" + "\n".join(legend_md) + "\n\n"
          + "\n".join(md_parts) + "\n")
    out.mkdir(parents=True, exist_ok=True)
    (out / "Appendix1.md").write_text(md, encoding="utf-8")

    legend_html = " ".join(
        f'<span class="tie" style="background-color:{c["bg"]};color:{c["fg"]}">'
        f'{c["emoji"]} {c["en"]}</span>' for c in CATS.values())
    html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">
<title>{H.escape(title)}</title><style>
@page {{ size: A4; margin: 1.6cm 1.4cm; }}
body {{ font-family: "Times New Roman", Georgia, serif; font-size: 10pt; line-height: 1.45; }}
h1 {{ font-size: 16pt; }} h2 {{ font-size: 12.5pt; margin-top: 18px; }}
table {{ width: 100%; border-collapse: collapse; table-layout: fixed; margin: 6px 0 14px; }}
th, td {{ border: 1px solid #bbb; padding: 3px 5px; vertical-align: top; }}
th {{ background: #eee; text-align: center; }}
tr {{ break-inside: avoid; page-break-inside: avoid; }}
.tie {{ padding: 0 2px; border-radius: 2px; }}
.titles td {{ font-weight: bold; }}
.legend .tie {{ margin-right: 8px; padding: 1px 5px; }}
</style></head><body>
<h1>{H.escape(title)}</h1>
<p>{H.escape(INTRO)}</p>
<p class="legend">{legend_html}</p>
<p>Chữ mũ trên Reference: <b>A</b> = anaphoric, <b>C</b> = cataphoric,
<b>E</b> = exophoric. ∅ = vị trí trống của phép tỉnh lược.</p>
{''.join(html_parts)}
</body></html>"""
    (out / "Appendix1.html").write_text(html, encoding="utf-8")

    ir = {
        "title": title,
        "intro": INTRO, "cats": CATS, "ref_names": REF_NAMES,
        "framework_map": [{"key": k, "en": en, "vi": vi}
                          for k, en, vi in FRAMEWORK_MAP],
        "totals": {
            "en_markers": grand.get("en", 0),
            "vi_markers": grand.get("vi", 0),
        },
        "pairs": pairs_ir,
    }
    dump_json(out / "appendix1_segments.json", ir)
    dump_json(out / "match_stats.json", {"grand": ir["totals"], "pairs": stats})
    print(f"Wrote {out}/Appendix1.md ({len(md)} chars)")
    print(f"Wrote {out}/Appendix1.html ({len(html)} chars)")
    print(f"Wrote {out}/appendix1_segments.json")
    total = grand.get("en", 0) + grand.get("vi", 0)
    print(f"Markers: EN {grand.get('en',0)} / VI {grand.get('vi',0)} = {total}")
    print("Marker coverage: 100% (every tie mapped back to a source row)")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build Appendix 1 outputs")
    ap.add_argument("--work", default="work")
    ap.add_argument("--out", default="out/appendix1")
    args = ap.parse_args(argv)
    return build(Path(args.work), Path(args.out))


if __name__ == "__main__":
    sys.exit(main())
