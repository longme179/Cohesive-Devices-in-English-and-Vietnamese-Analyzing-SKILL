---
name: cohesion-en-vi
description: Manually annotate English–Vietnamese parallel texts for cohesion beyond the sentence level (Halliday & Hasan vs Trần Ngọc Thêm) and render a five-colour Appendix 1 DOCX/PDF. Use when the user supplies a two-column EN|VI markdown/PDF and asks for a semantics-first cohesive-device analysis and highlighted appendix.
---

# COHESION EN–VI — manual annotation → Appendix 1

This repository is a **skill**, not a one-shot script.  The scientific value is
the **manual semantic analysis of each EN–VI pair**; the scripts only parse
tables, segment sentences, validate offsets, render colours, count and package.
The target research question is:

> **COHESION BEYOND THE SENTENCE LEVEL — A Comparison of Cohesive Devices in
> English and Vietnamese.**

The finished artefact is an Appendix 1 like `out/appendix1/`: two-column EN|VI
tables, five background colours, Reference superscripts A/C/E, no outcome tags.

## 1. Non-negotiable manual-first protocol

1. **Read the pair before writing any tie.**  Deciding “is this a tie, which
   category, where is the antecedent?” is an act of reading comprehension.
2. **Never generate ties from regex, pronoun/connector lists, dictionaries,
   repeated strings, word counts or loops.**  A script may only locate a literal
   you have already chosen (`pipeline.locate`) or validate a row you wrote.
3. **One pair = one analysis file + one hand-written tie table.**  If several
   agents work in parallel, give each agent exactly one pair; all agents use the
   same conventions and the same row format.
4. **The analysis gate is enforced.**  `pipeline.annotate` refuses to run unless
   `work/analysis/PXX*.md` exists with the 9-section template.  Do not bypass it
   with `--allow-missing-analysis` except for a dummy smoke test.
5. **Never default a reference direction.**  Every R tie must carry an explicit
   `ref` decision (`A`/`C`/`E`) in the tie table.
6. **Do not fabricate a zero.**  If the analysis says the target language filled
   the slot with a noun/auxiliary, do not add an E marker there.  If it replaced
   the slot with a pro-form, record **S**, not E.

## 2. Theoretical framing

Read the digests in `references/` before annotating; they are the authority for
category decisions and record the exact chapters/sections they summarize.

- **English — Halliday & Hasan (1976)**, *Cohesion in English*. Five resources:
  **reference** (personal, demonstrative, comparative, and the definite article
  `the`), **substitution** (nominal, verbal, clausal), **ellipsis** (substitution
  by zero), **conjunction** (additive, adversative, causal, temporal, plus
  continuatives), and **lexical cohesion** (reiteration — repetition, synonym,
  superordinate, general word — and collocation). Reference is *identity of a
  referent*; substitution and ellipsis are *wording* relations. See
  `references/halliday-hasan-1976.md`.
- **Vietnamese — Trần Ngọc Thêm**, *Hệ thống liên kết văn bản tiếng Việt*
  (1st ed. 1985; 3rd ed. 2006). The system is built on the **phát ngôn**
  (utterance), not the sentence, and separates **liên kết hình thức** (formal)
  from **liên kết nội dung** (topic + logic); both are required for a text. Three
  utterance types — *câu tự nghĩa*, *câu hợp nghĩa*, *ngữ trực thuộc* — condition
  which devices are normal. Devices: *phép lặp*, *phép đối*, *phép thế đẳng
  nghĩa*, *phép liên tưởng*, *phép tuyến tính* (all utterance types);
  *phép thế đại từ* (khiếm diện / dự báo / hồi quy), *phép tỉnh lược yếu*,
  *phép nối lỏng* (câu hợp nghĩa); *phép tỉnh lược mạnh*, *phép nối chặt*
  (ngữ trực thuộc). See `references/tran-ngoc-them-2006.md`.
- **No one-to-one mapping.** *Phép thế đại từ* covers both H&H reference and
  pro-form substitution; *phép thế đẳng nghĩa* and *phép liên tưởng* are lexical
  (L), not S; *phép tuyến tính* and *phép đối* are not ties by themselves. Use
  the decision tests in `references/en-vi-mapping.md` §3 before writing a row.
- **Translation evidence.** Nguyễn Thanh Tùng (2020) documents the systematic
  EN↔VI shifts (pronoun ↔ repetition, *the* ↔ demonstrative/zero, ellipsis
  difficulty) that make form-by-form comparison wrong; see
  `references/translation-en-vi-2020.md`.
- **Unit of analysis:** the tie that crosses a sentence boundary (`[LC]`).  The
  Appendix also carries a **supplementary S/E layer** (`[TC]`) because Vietnamese
  ellipsis and substitution are often intra-sentential and would otherwise be
  invisible; label every such row `[TC]` and do not use it as evidence for an
  intersentential claim.
- **Reference direction:** `A` anaphoric (antecedent before), `C` cataphoric
  (antecedent after; rare in news), `E` exophoric (writer/reader/context).
  `ref=E` is a **direction**, not the E (ellipsis) category: a row with `cat="E"`
  has `ref=None`, and a row with `ref="E"` is an R tie. Never mix the two.

### 2.1 Four rules that prevent most coding errors

1. **Identity vs wording.** Same referent → R. Pro-form replacing wording → S.
   Missing wording → E. A connector word alone does not make a C tie; a repeated
   topic does not make an L tie.
2. **One form, one row.** Never code the same zero as both E and R. A Vietnamese
   zero that tracks a participant is *thế đại từ khiếm diện* in the analysis
   (§2/§4) and E in the table; the note carries the other reading.
3. **Repetition is L, not R.** When English uses a pronoun and Vietnamese repeats
   the noun, code the Vietnamese noun as L and record the R→L shift; do not mark
   the Vietnamese side as a missing R.
4. **Judge translation by target norms.** A legitimate Vietnamese repetition or
   zero is not an error; see `references/translation-en-vi-2020.md` §3.

## 3. Input contract

Accepted input is a markdown file with two-column tables:

```markdown
## Pair 01

| https://en-source | https://vi-source |
| :--- | :--- |
| **English title** | **Tiêu đề tiếng Việt** |
| English body row. | Vietnamese body row. |
| Another row; use an empty cell if that side was cut. | ... |
```

The parser also accepts `| Tiếng Anh | Tiếng Việt |` header rows, blank lines
inside a pair, `none` cells, markdown links and bold/italic markup.  See
`templates/input_template.md`.

If the user sends a **PDF**, first convert it to this markdown shape:

```bash
python -m pipeline.pdf_to_md --pdf input.pdf --out input.md
```

The helper uses `pdftotext -layout` (Poppler) when available, because layout
text preserves the two visual columns better than generic table detectors.  It
falls back to word positions via PyMuPDF.  PDF extraction is still lossy.
**Read the markdown and repair merged cells, wrapping, row order and missing
spaces before analysis.**  If the PDF is a scan or has multi-column body text,
transcribe the pair manually; do not analyse corrupt text.

## 4. Commands (run from the repository root)

```bash
# 1. parse the input into work/pairs/PXX/{rows.json,meta.json,ST.txt,TT.txt}
python -m pipeline.ingest --input input.md --work work

# 2. sentence segmentation, preserving original rows
python -m pipeline.segment --work work

# 3. for each pair: write work/analysis/PXX*.md and work/tie_tables/PXX.py
#    (manual work — see §5–§6), then:
python -m pipeline.annotate --work work --pair P01
python -m pipeline.render   --work work --pair P01

# 4. when every pair renders PASS:
python -m pipeline.build_appendix --work work --out out/appendix1
python -m pipeline.export_docx    --out out/appendix1
python -m pipeline.export_pdf     --out out/appendix1
python -m pipeline.validate       --work work --out out/appendix1
```

Dependencies for DOCX/PDF:

```bash
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
# then run export with .venv/bin/python -m pipeline.export_docx ...
```

The ingest/segment/annotate/render/build stages need only the Python standard
library.

## 4b. User-facing prompt templates

A user who only attaches a two-column markdown can paste one of:

- `prompts/annotate-input.vi.md` (Vietnamese)
- `prompts/annotate-input.en.md` (English)

Both prompts tell the agent to read this SKILL.md, run ingest/segment, do the
manual analysis + tie table for each pair, render/QC, build Appendix 1 and
export DOCX/PDF.

## 5. Per-pair manual analysis — the scientific core

Create `work/analysis/PXX_semantic.md` from
`templates/analysis_template.md`.  It must contain these 9 sections:

1. content, genre, source, **sentence map ST ↔ TT** (translated / cut /
   VI-only);
2. **ellipsis** — every zero slot, with `[LC]`/`[TC]` and `{recovered}`;
3. **substitution** — nominal/verbal/clausal pro-forms, realization vs kept
   pro-form;
4. **reference** — table of forms, antecedent, `A/C/E`; then the
   `[±human]` / honorific / general-noun behaviour;
5. **conjunction** — adversative/additive/temporal/causal; kept, dropped,
   self-generated, type change;
6. **lexical cohesion** — chains that converge or split under translation;
7. **notable shifts** — a compact count table;
8. **source data defects** — duplicated sentences, missing spaces, wrong
   numbers, cut blocks; say what must not be used as sentence-level evidence;
9. **count reconciliation** — manual counts vs tie table, with a short
   conclusion.

Write the analysis **in your own words**, quoting exact source strings.  Do not
copy another pair's notes.  The analysis is the audit trail for every colour in
the Appendix.

## 6. Tie table — hand-written, 13 fields

Create `work/tie_tables/PXX.py` (see `templates/tie_table_template.py`):

```python
ST = [
    ("S002", "It", "R", "personal", "S001: a new shelter",
     "high", None, "pronoun refers to the shelter", 1,
     None, None, "LC", "A"),

    ("S004", None, "E", "nominal", "S002: forty beds",
     "high", None, "[LC] zero after 'add more'; recover {beds}", 1,
     "add more", "{beds}", "LC", None),
]
TT = [...]
```

Field order:

| # | field | meaning |
|---|---|---|
| 1 | `sent` | sentence id from `*_seg.json` |
| 2 | `text` | exact substring, or `None` for E |
| 3 | `cat` | `R` / `S` / `E` / `C` / `L` |
| 4 | `sub` | e.g. `personal`, `demonstrative`, `nominal`, `verbal`, `clausal`, `adversative`, `repetition`, `synonym` |
| 5 | `ante` | antecedent / gap description **with sentence id** |
| 6 | `conf` | `high` / `med` / `low` |
| 7 | `alt` | optional alternative form (e.g. the article absorbed into an L tie) |
| 8 | `note` | short justification; prefix `[LC]` or `[TC]` |
| 9 | `occ` | explicit occurrence when the string/gap repeats; else `1` |
| 10 | `gap_after` | E only: exact substring ending immediately before ∅; `""` at sentence start |
| 11 | `recovered` | E only: meaning in `{...}` |
| 12 | `level` | `LC` intersentential / `TC` intra-sentential / `TD` title |
| 13 | `ref` | R only: `A`/`C`/`E`; `None` otherwise |

Rules:

- `text` and `gap_after` must be **verbatim** in the sentence; use
  `python -m pipeline.locate` to check offsets.
- If the same literal occurs more than once, `annotate` refuses an implicit
  `occ=None`; write `1`, `2`, … explicitly.
- For `[LC]`, `ante` must cite an earlier sentence (or a later one for `C`).
  For `[TC]`, cite the same sentence and say “(trong câu)”.
- Do not add a row that is not in the analysis.  Do not add a row for a
  first-mention noun that has no antecedent.
- Vietnamese pro-drop: a zero slot is **E**; when it tracks a participant, record
  *thế đại từ khiếm diện* in the analysis and keep the single E row. A pro-form
  such as `như vậy` / `làm vậy` is **S**; a repeated noun is **L**.
- Before writing a row, run the decision tests in
  `references/en-vi-mapping.md` §3; §6 there lists the recurring
  misclassifications and the fix.
- English `one/those` realized as a full NP in Vietnamese is not an S tie in
  Vietnamese; record the English S and note the realization.

## 7. Rendering specification

Final colours (single source of truth: `pipeline/common.py:CATS`):

| Category | Colour | HEX | Text |
|---|---|---|---|
| R Reference | 🟨 vàng | `#FFFF00` | black |
| S Substitution | 🟩 xanh lá | `#00FF00` | black |
| E Ellipsis | 🟦 xanh dương | `#0000FF` | white |
| C Conjunction | 🟧 cam | `#FF9900` | black |
| L Lexical cohesion | 🟪 tím | `#9900FF` | white |

- Reference spans keep a superscript `A`/`C`/`E`.
- Ellipsis slots are `∅` on the E colour.
- **No outcome tags** (`→`, `»`, `~`, `×`, `+`) and no 7-outcome legend.
- `Appendix1.md` / `.html` are the working outputs; `.docx` and `.pdf` are the
  deliverables.  The DOCX has one 2-column table per pair, a title row and the
  5-category legend.

## 8. Quality gates

For every pair:

- `pipeline.annotate` has no errors and prints counts.
- `pipeline.render` prints `PASS` for EN and VI.
- 0 overlapping markers; 0 point inside a text span; stripping markers
  reproduces the flow exactly.
- every R has `ref ∈ {A,C,E}`.
- `pipeline.build_appendix` reports **100% marker coverage** and 0
  straddle/orphan.
- `pipeline.validate` reports `N/N pairs OK`.

Inspect the final PDF/DOCX visually: legend colours, `∅` background, A/C/E
superscript, no tag glyphs, no overflow.

## 9. Parallelisation

When several agents work at once:

1. One agent per pair; never two agents editing the same `PXX.py`.
2. Every agent reads this SKILL.md, `templates/analysis_template.md` and
   `templates/tie_table_template.py` first.
3. Use the same row format and the same `[LC]/[TC]` convention.
4. A coordinator runs `annotate`, `render`, `build_appendix` and
   `validate` after all pairs are written.  Each agent may run annotate/render
   for its own pair.
5. If a pair fails QC, fix that pair's table only; never “fix” the renderer to
   accept a wrong span.

## 10. Common traps

- **Copy-paste notes** from another pair (very common in the legacy corpus).
- **Positional zip alignment**: pairing EN and VI ties by row number instead of
  reading the referent.
- **Sentence ID vs tie ID** confusion in `ante`/`notes`.
- **Missing spaces** in PDF-extracted text; repair before segmenting.
- **Cut blocks**: a tie in an untranslated EN sentence has no VI counterpart;
  mark it on the EN side and leave the VI cell empty; do not invent a VI tie.
- **VI-only sentences**: they have no EN counterpart; do not force a tie back
  to EN.
- **Title-level** `[TD]` ellipsis: the current Appendix does not mark title
  rows; record it in the analysis and note it in the report rather than
  fabricating a body marker.
- **Source defects** (duplicated sentence, wrong number, missing verb): record
  them in §8; do not use them as evidence of a translation shift.

## 11. Deliverables

```
work/
  pairs/PXX/{meta.json,rows.json,ST.txt,TT.txt,ST_seg.json,TT_seg.json,
             ST_ties.json,TT_ties.json,ST_highlighted.md,TT_highlighted.md,
             PXX.html,ST_qc.txt,TT_qc.txt}
  analysis/PXX_semantic.md
  tie_tables/PXX.py
out/appendix1/
  Appendix1.md
  Appendix1.html
  Appendix1.docx
  Appendix1.pdf
  appendix1_segments.json
  match_stats.json
```

The repository also ships a complete 20-pair reference corpus
(`download/BDNC/`, `out/appendix1/`, `download/BDNC/semantic_analysis/`) and a
tiny worked example (`examples/mini/`) you can run end-to-end before touching a
real pair.

## 12. Reference corpus (optional reading)

The 20-pair corpus is a worked benchmark, not a template to copy.  Read a few
files to calibrate the level of detail:

- `download/BDNC/semantic_analysis/Pair_01/P01_phan-tich-ngu-nghia.md`
- `download/BDNC/semantic_analysis/Pair_07/P07_phan-tich-ngu-nghia.md`
- `download/BDNC/semantic_analysis/INDEX.md` (cross-pair ledger B1–B28)
- `REPLICATION_GUIDE.md` (long-form 22-step replication protocol)

Never copy a tie table wholesale into a new pair.  Re-read the new text.
