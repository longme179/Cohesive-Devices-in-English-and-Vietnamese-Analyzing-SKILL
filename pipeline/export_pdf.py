#!/usr/bin/env python3
"""Export Appendix1.html to PDF with WeasyPrint (optional dependency)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Export Appendix 1 PDF")
    ap.add_argument("--out", default="out/appendix1")
    ap.add_argument("--also", default=None)
    args = ap.parse_args(argv)
    try:
        from weasyprint import HTML
    except ImportError:
        print("ERROR: WeasyPrint is required.  Install:\n"
              "  uv venv .venv && uv pip install --python .venv/bin/python "
              "weasyprint", file=sys.stderr)
        return 2
    out = Path(args.out)
    src = out / "Appendix1.html"
    if not src.exists():
        print(f"ERROR: {src} missing; run pipeline.build_appendix first",
              file=sys.stderr)
        return 2
    dst = out / "Appendix1.pdf"
    HTML(filename=str(src)).write_pdf(str(dst))
    if args.also:
        import shutil
        Path(args.also).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(dst, args.also)
    print(f"Wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
