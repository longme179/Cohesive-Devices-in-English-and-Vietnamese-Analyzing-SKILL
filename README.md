# COHESION EN–VI — a skill for manual contrastive cohesion annotation

This repository is a **reproducible skill** for the study of

> **COHESION BEYOND THE SENTENCE LEVEL — A Comparison of Cohesive Devices in
> English and Vietnamese.**

It takes a two-column EN|VI markdown (or a PDF converted to that shape), guides
an AI agent through a **manual semantic analysis of every pair**, and renders a
five-colour **Appendix 1** in Markdown, HTML, DOCX and PDF.  The scripts are
mechanical only; the linguistic decisions are written by hand in per-pair
analysis files and tie tables.

Start with **[SKILL.md](SKILL.md)**.  It is the operating contract for the agent.

## What the agent does

1. **Read** each English–Vietnamese pair, not a list of pronouns.
2. **Write a 9-section semantic analysis** (`work/analysis/PXX_semantic.md`)
   covering ellipsis, substitution, reference (A/C/E), conjunction, lexical
   cohesion, translation shifts and source defects.
3. **Write the tie table by hand** (`work/tie_tables/PXX.py`), one row per
   decision, with exact source strings, antecedent, category, level
   (`[LC]`/`[TC]`) and — for Reference — a manually chosen direction.
4. Run the mechanical pipeline: ingest → segment → annotate → render/QC →
   build Appendix 1 → DOCX/PDF.
5. Inspect the rendered colours and the 100% marker-coverage gate.

## Quick start

```bash
git clone <this-repo> cohesion-en-vi
cd cohesion-en-vi

# 1. input: a 2-column markdown table (see templates/input_template.md)
python -m pipeline.ingest --input input.md --work work
python -m pipeline.segment --work work

# 2. MANUAL WORK for each pair:
#    - copy templates/analysis_template.md to work/analysis/P01_semantic.md
#    - write work/tie_tables/P01.py from templates/tie_table_template.py
python -m pipeline.annotate --work work --pair P01
python -m pipeline.render   --work work --pair P01

# 3. build the appendix
python -m pipeline.build_appendix --work work --out out/appendix1

# 4. DOCX/PDF (install the two optional dependencies once)
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python -m pipeline.export_docx --out out/appendix1
.venv/bin/python -m pipeline.export_pdf  --out out/appendix1
```

For a PDF input:

```bash
python -m pipeline.pdf_to_md --pdf input.pdf --out input.md
# READ input.md, repair merged cells / row order / missing spaces, then ingest
```

## The five colours

| Category | Colour | HEX |
|---|---|---|
| R Reference | 🟨 vàng | `#FFFF00` |
| S Substitution | 🟩 xanh lá | `#00FF00` |
| E Ellipsis | 🟦 xanh dương | `#0000FF` |
| C Conjunction | 🟧 cam | `#FF9900` |
| L Lexical cohesion | 🟪 tím | `#9900FF` |

Reference spans also carry a superscript **A** (anaphoric), **C** (cataphoric)
or **E** (exophoric).  Ellipsis slots are shown as `∅` on blue.  There are no
outcome tags (`→ » ~ × +`) and no seven-outcome legend.

## Repository map

```
SKILL.md                  operating contract for the agent (read first)
AGENTS.md                 short pointer for agent runtimes
templates/                input, analysis and tie-table templates
pipeline/                 mechanical stages:
  ingest.py               markdown 2-column parser
  segment.py              row-preserving sentence segmentation
  annotate.py             validates a hand-written tie table (analysis gate)
  render.py               marked text + QC gates
  build_appendix.py       Appendix1.md / .html / segment IR
  export_docx.py          DOCX (python-docx)
  export_pdf.py           PDF (WeasyPrint)
  pdf_to_md.py            best-effort PDF -> markdown helper
  locate.py               literal offset locator (no tie decisions)
  validate.py             end-to-end readiness check
examples/mini/            tiny worked example, already runnable
download/BDNC/            the 20-pair reference corpus and deliverables
download/BDNC/semantic_analysis/   20 hand-written analyses (B1–B28 ledger)
out/appendix1/            the 20-pair Appendix 1 (v7, 5 colours, no tags)
```

## The example first

A four-sentence worked pair lives in `examples/mini/`:

```bash
python -m pipeline.ingest --input examples/mini/input.md --work examples/mini/work
python -m pipeline.segment --work examples/mini/work
```

The `work/` tree already contains the manual analysis and tie table, so you can
run annotate → render → build → export and see the complete product before
writing your own pair.  The generated `output/Appendix1.{md,html,docx,pdf}` is
the target format.

## What is included as a benchmark

- `download/BDNC/semantic_analysis/` — 20 full manual analyses (one folder per
  pair) plus `INDEX.md` with the cross-pair findings ledger.
- `out/appendix1/` — the 20-pair Appendix 1 (3.180 marked ties, five colours,
  100% marker coverage, 40/40 side-level QC passes).
- `REPLICATION_GUIDE.md` — the long-form 22-step protocol and the catalogue of
  traps encountered while building the benchmark.

Those files are for **calibration**, not for copying.  A new pair must be read
and annotated from scratch.

## Design principle

> Linking is a relation of meaning between sentences, not a repeated character
> string.  The decision “is this a tie, what type, where is the antecedent?”
> must be made by reading.  Scripts only parse, locate, validate, render, count
> and package.

If a script ever defaults a label (for example `ref="A"`), replace that default
with the analyst's explicit decision in the tie table.  This repository's
`pipeline.annotate` deliberately refuses R rows without an explicit `ref`.
