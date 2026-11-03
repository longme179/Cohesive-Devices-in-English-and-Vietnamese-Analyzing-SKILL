# AGENTS.md — entry point

This repository is a skill.  Read **[SKILL.md](SKILL.md)** before doing anything.

Short version:

1. The user supplies a 2-column EN|VI markdown/PDF.  For PDF, convert with
   `python -m pipeline.pdf_to_md` and repair the markdown by hand.
   Theory digests for the category decisions: `references/` (read before
   annotating; `references/en-vi-mapping.md` has the decision tests).
2. Run `python -m pipeline.ingest --input input.md --work work` and
   `python -m pipeline.segment --work work`.
3. For **each pair**, read the text and write:
   - `work/analysis/PXX_semantic.md` (9 sections, from
     `templates/analysis_template.md`);
   - `work/tie_tables/PXX.py` (13-field rows, from
     `templates/tie_table_template.py`).
   Do not generate ties with regex, pronoun lists, word counts or loops.
4. Run `python -m pipeline.annotate --work work --pair PXX` and
   `python -m pipeline.render --work work --pair PXX` until both sides PASS.
5. Build and export:
   `python -m pipeline.build_appendix --work work --out out/appendix1`,
   `.venv/bin/python -m pipeline.export_docx --out out/appendix1`,
   `.venv/bin/python -m pipeline.export_pdf --out out/appendix1`.
6. Run `python -m pipeline.validate --work work --out out/appendix1`.

The target is **cohesion beyond the sentence level** (Halliday & Hasan 1976 vs
Trần Ngọc Thêm 2006), not a string-matching exercise.  The final Appendix uses
five colours (R `#FFFF00`, S `#00FF00`, E `#0000FF`, C `#FF9900`, L `#9900FF`),
Reference superscripts A/C/E, and no outcome tags.

A runnable tiny example is in `examples/mini/`; run it first to see the expected
output.
