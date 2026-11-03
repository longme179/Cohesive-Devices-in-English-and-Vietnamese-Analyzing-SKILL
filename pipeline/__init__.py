"""COHESION EN–VI skill pipeline.

Mechanical stages only: ingest -> segment -> annotate (validates a hand-written
tie table) -> render/QC -> build Appendix1 md/html -> export DOCX/PDF.

Run modules with ``python -m pipeline.<stage>``.
"""
__version__ = "1.0.0"
