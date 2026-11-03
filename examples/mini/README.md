# Mini worked example

A 5-row synthetic EN–VI pair used only to smoke-test the skill pipeline.  It is
not research data.

## Run it

From the repository root:

```bash
python -m pipeline.ingest --input examples/mini/input.md --work examples/mini/work
python -m pipeline.segment --work examples/mini/work
python -m pipeline.annotate --work examples/mini/work --pair P01
python -m pipeline.render   --work examples/mini/work --pair P01
python -m pipeline.build_appendix --work examples/mini/work --out examples/mini/output
.venv/bin/python -m pipeline.export_docx --out examples/mini/output
.venv/bin/python -m pipeline.export_pdf  --out examples/mini/output
python -m pipeline.validate --work examples/mini/work --out examples/mini/output
```

The `work/` tree already contains the manual analysis and tie table.  Look at:

- `work/analysis/P01-manual.md` — 9-section analysis;
- `work/tie_tables/P01.py` — 13-field hand-written tie table;
- `output/Appendix1.{md,html,docx,pdf}` — the rendered Appendix 1.

The output has 5 EN ties and 5 VI ties, all five categories represented across
the pair, and 4 Reference superscripts.
