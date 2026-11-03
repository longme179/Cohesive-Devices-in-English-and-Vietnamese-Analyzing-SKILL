#!/usr/bin/env python3
"""Render one pair and run mechanical QC.

Outputs under work/pairs/PXX/:
  ST_highlighted.md / TT_highlighted.md   emoji + ⟦...⟧ notation
  PXX.html                                colour + tooltip preview
  ST_qc.txt / TT_qc.txt                   QC report

QC gates
  (a) each tie's text occurs at its stated occurrence in its sentence
  (b) no overlapping markers / no point inside a text span
  (c) removing all markers reproduces the flow text exactly
  (d) intersentential antecedent direction is valid
  (e) every R tie has a manual A/C/E direction
"""
from __future__ import annotations

import argparse
import html as H
import json
import re
import sys
from collections import Counter
from pathlib import Path

from .common import CATS, load_json, pair_dir

SENT_RE = re.compile(r"S(\d{3})")


def markers_for(seg: dict, ties: list[dict]) -> list[tuple[int, int, dict]]:
    flow = seg.get("flow") or "\n".join(seg["paras"])
    sents = {s["id"]: s for s in seg["sentences"]}
    markers = []
    for t in ties:
        s = sents.get(t["sent"])
        if not s:
            raise ValueError(f'{t["id"]}: sentence {t["sent"]} missing')
        if t["text"] is None:
            gap = t["gap_after"]
            occ = t.get("occ") or 1
            pos, found, p = -1, 0, -1
            while True:
                p = s["text"].find(gap, p + 1)
                if p < 0:
                    break
                found += 1
                if found == occ:
                    pos = p + len(gap)
                    break
            if pos < 0:
                raise ValueError(
                    f'{t["id"]}: gap_after {gap!r} occ {occ} not in {t["sent"]}')
            a = b = s["fa"] + pos
        else:
            text = t["text"]
            occ = t.get("occ") or 1
            pos, found, p = -1, 0, -1
            while True:
                p = s["text"].find(text, p + 1)
                if p < 0:
                    break
                found += 1
                if found == occ:
                    pos = p
                    break
            if pos < 0:
                raise ValueError(
                    f'{t["id"]}: text {text!r} occ {occ} not in {t["sent"]}')
            a, b = s["fa"] + pos, s["fa"] + pos + len(text)
            if flow[a:b] != text:
                raise ValueError(f'{t["id"]}: flow span mismatch for {text!r}')
        markers.append((a, b, t))
    markers.sort(key=lambda m: (m[0], m[1]))
    return markers


def check(seg: dict, ties: list[dict], markers: list[tuple[int, int, dict]]):
    qc, fail = [], False
    flow = seg.get("flow") or "\n".join(seg["paras"])
    for i in range(len(markers) - 1):
        a1, b1, t1 = markers[i]
        a2, b2, t2 = markers[i + 1]
        if a2 < b1:
            qc.append(f'FAIL (b): overlap {t1["id"]} [{a1},{b1}) vs '
                      f'{t2["id"]} [{a2},{b2})')
            fail = True
    text_ms = [m for m in markers if m[0] < m[1]]
    for pa, _, pt in [m for m in markers if m[0] == m[1]]:
        for ta, tb, tt in text_ms:
            if ta < pa < tb:
                qc.append(f'FAIL (b): ellipsis {pt["id"]} inside {tt["id"]}')
                fail = True
    for t in ties:
        if t.get("level") in ("TC", "TD"):
            if not (t.get("ante") or "").strip():
                qc.append(f'FAIL (d): {t["id"]}: level {t["level"]} without ante')
                fail = True
            continue
        if t["cat"] == "R" and t.get("ref") == "E":
            continue
        nums = [int(n) for n in SENT_RE.findall(t.get("ante") or "")]
        if not nums:
            qc.append(f'FAIL (d): {t["id"]}: ante has no sentence id: '
                      f'{t.get("ante")!r}')
            fail = True
            continue
        tnum = int(SENT_RE.match(t["sent"]).group(1))
        if t.get("dir", "ana") == "ana" and max(nums) >= tnum:
            qc.append(f'FAIL (d): {t["id"]}: anaphoric ante {t["ante"]!r} '
                      f'not before {t["sent"]}')
            fail = True
        if t.get("dir") == "cata" and min(nums) <= tnum:
            qc.append(f'FAIL (d): {t["id"]}: cataphoric ante {t["ante"]!r} '
                      f'not after {t["sent"]}')
            fail = True
    for t in ties:
        if t["cat"] == "R" and t.get("ref") not in ("A", "C", "E"):
            qc.append(f'FAIL (e): {t["id"]}: R without valid ref')
            fail = True
    # strip test
    out = flow
    for a, b, t in sorted(markers, key=lambda m: (-m[0], -m[1])):
        if a == b:
            out = out[:a] + "🟦⟦∅⟧" + out[a:]
        else:
            out = out[:b] + "⟧" + out[b:]
            out = out[:a] + CATS[t["cat"]]["emoji"] + "⟦" + out[a:]
    stripped = out.replace("🟦⟦∅⟧", "")
    for c in CATS.values():
        stripped = stripped.replace(c["emoji"] + "⟦", "")
    stripped = stripped.replace("⟧", "")
    if stripped != flow:
        i = 0
        while i < min(len(stripped), len(flow)) and stripped[i] == flow[i]:
            i += 1
        qc.append(f'FAIL (c): stripping changes text at {i}: '
                  f'{stripped[max(0, i-25):i+25]!r} vs '
                  f'{flow[max(0, i-25):i+25]!r}')
        fail = True
    return out, qc, fail


def marked_to_html(flow: str, markers, title: str):
    parts, last = [], 0
    for a, b, t in markers:
        parts.append(H.escape(flow[last:a]))
        tip = f'{CATS[t["cat"]]["en"]} ({t["cat"]}/{t.get("sub", "")})'
        tip += f' | level: {t.get("level", "LC")}'
        if t["cat"] == "R":
            tip += f' | dir: {t.get("ref")}'
        tip += f' | ante: {t.get("ante", "")} | conf={t.get("conf", "")}'
        if t.get("note"):
            tip += f' | note: {t["note"]}'
        if a == b:
            parts.append(
                f'<span class="tie" style="background-color:{CATS["E"]["bg"]};'
                f'color:{CATS["E"]["fg"]}" title="{H.escape(tip)}">∅</span>')
            last = a
        else:
            sup = (f'<sup>{t["ref"]}</sup>'
                   if t["cat"] == "R" and t.get("ref") else "")
            parts.append(
                f'<span class="tie" style="background-color:'
                f'{CATS[t["cat"]]["bg"]};color:{CATS[t["cat"]]["fg"]}" '
                f'title="{H.escape(tip)}">{H.escape(flow[a:b])}{sup}</span>')
            last = b
    parts.append(H.escape(flow[last:]))
    body = "".join(parts).replace("\n", "<br>\n")
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{H.escape(title)}</title><style>
body{{font-family:Georgia,serif;max-width:900px;margin:2em auto;padding:0 1em;line-height:1.7}}
.tie{{padding:0 2px;border-radius:3px;cursor:help}}
</style></head><body><h1>{H.escape(title)}</h1><p>{body}</p></body></html>"""


def render_side(work: Path, pid: str, side: str, pref: str) -> bool:
    d = pair_dir(work, pid)
    seg = load_json(d / f"{pref}_seg.json")
    ties = load_json(d / f"{pref}_ties.json")["ties"]
    meta = load_json(d / "meta.json")
    markers = markers_for(seg, ties)
    out, qc, fail = check(seg, ties, markers)
    counts = Counter(t["cat"] for t in ties)
    (d / f"{pref}_highlighted.md").write_text(
        f"# {pid} — {'ST (English)' if side == 'EN' else 'TT (Vietnamese)'}\n\n"
        f"**Title:** {meta.get('title_en' if side == 'EN' else 'title_vi', '')}\n\n"
        f"**Legend:** 🟨 R | 🟩 S | 🟦 E (∅ = gap) | 🟧 C | 🟪 L\n\n---\n\n"
        + out + "\n", encoding="utf-8")
    title = f"{pid} — {'Source text' if side == 'EN' else 'Target text'}"
    (d / f"{pid}.html").write_text(marked_to_html(seg.get("flow") or "\n".join(seg["paras"]), markers, title),
                                   encoding="utf-8")
    status = "PASS" if not fail else "FAIL"
    qc.insert(0, f"QC {pid} {side}: {status}")
    qc.append(f"counts: {dict(sorted(counts.items()))}")
    qc.append(f"ties: {len(ties)}")
    (d / f"{pref}_qc.txt").write_text("\n".join(qc) + "\n", encoding="utf-8")
    print(f"{pid} {side}: {status} — {len(ties)} ties | {dict(sorted(counts.items()))}")
    for line in qc[:8]:
        if line.startswith("FAIL"):
            print("   " + line)
    return not fail


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Render and QC one pair")
    ap.add_argument("--work", default="work")
    ap.add_argument("--pair", required=True)
    args = ap.parse_args(argv)
    ok1 = render_side(Path(args.work), args.pair, "EN", "ST")
    ok2 = render_side(Path(args.work), args.pair, "VI", "TT")
    return 0 if (ok1 and ok2) else 1


if __name__ == "__main__":
    sys.exit(main())
