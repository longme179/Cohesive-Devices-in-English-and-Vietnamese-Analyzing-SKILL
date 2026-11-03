# Sample prompt — attach a two-column EN|VI markdown

> Open a chat with the agent, attach the `.md` file, copy the block below,
> replace `[ATTACHED_FILE]`, and send.

```text
You are in the COHESION EN–VI skill repository (the cloned folder containing SKILL.md).

Attached file: [ATTACHED_FILE] — a two-column EN | VI markdown table.

Follow SKILL.md end to end and deliver a complete Appendix 1 (DOCX + PDF).
Do not ask questions if the file is readable; ask only if it cannot be opened
or contains no two-column table.

MANDATORY STEPS

1. Read SKILL.md, templates/analysis_template.md,
   templates/tie_table_template.md and README.md first.
2. Never edit the input file. If it is a PDF, convert it with
   `python -m pipeline.pdf_to_md`, read the draft and repair extraction
   damage (merged cells, wrapped lines, missing spaces) before analysis.
3. Run:
   python -m pipeline.ingest --input <file> --work work
   python -m pipeline.segment --work work
4. For EACH pair, in this order:
   a. Read EN + VI + the sentence map; understand content, genre and antecedents.
   b. Write work/analysis/PXX_semantic.md with all 9 sections; mark [LC] vs [TC].
   c. Hand-write work/tie_tables/PXX.py (13 fields): exact text/gap_after,
      sentence id in ante, level LC/TC, and an explicit A/C/E ref for every R.
   d. Run:
      python -m pipeline.annotate --work work --pair PXX
      python -m pipeline.render   --work work --pair PXX
      until both EN and VI PASS.
5. Build and export:
   python -m pipeline.build_appendix --work work --out out/appendix1
   .venv/bin/python -m pipeline.export_docx --out out/appendix1
   .venv/bin/python -m pipeline.export_pdf  --out out/appendix1
   python -m pipeline.validate --work work --out out/appendix1
   If python-docx/WeasyPrint are missing, create .venv and install requirements.txt.
6. Visually check the PDF/DOCX: 5 colours, blue ∅, A/C/E superscripts,
   no → » ~ × + tags, no overflow.

NON-NEGOTIABLE RULES

- The research target is COHESION BEYOND THE SENTENCE LEVEL (Halliday & Hasan
  1976 vs Trần Ngọc Thêm 2006). [LC] is the main unit; [TC] is a supplementary
  S/E layer only.
- NEVER generate ties with regex, pronoun/connector lists, word counts,
  string matching or loops. Every tie row must be written after reading.
- NEVER default ref="A"; every R needs an explicit A/C/E decision.
- Do NOT invent ∅ when the translation filled the slot; use S for a pro-form.
- Do NOT add ties that are not in the analysis; do not copy another pair.
- Quality over speed. For multiple pairs, work pair by pair; if parallel,
  one agent per pair with the same conventions.

FINAL REPLY

- Table: pair, EN/VI tie counts, coverage, QC.
- Paths: out/appendix1/Appendix1.docx, .pdf, .md, .html.
- [TD]/unrendered items and any source-data caveats.
```
