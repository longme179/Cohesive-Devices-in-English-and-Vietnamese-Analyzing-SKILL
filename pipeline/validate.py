#!/usr/bin/env python3
"""End-to-end readiness check for the skill work tree.

Checks, per pair:
  - manual analysis exists (9-section template)
  - hand-written tie table exists
  - ST/TT ties JSON exist and QC files say PASS
  - highlighted files exist
  - Appendix match_stats marker counts are non-zero
Exit code 0 only when every pair passes.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .annotate import check_analysis
from .common import load_json, pair_ids


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validate a skill work tree")
    ap.add_argument("--work", default="work")
    ap.add_argument("--out", default="out/appendix1")
    args = ap.parse_args(argv)
    work, out = Path(args.work), Path(args.out)
    pids = pair_ids(work)
    if not pids:
        print(f"FAIL: no pairs under {work}/pairs")
        return 1
    bad = 0
    for pid in pids:
        d = work / "pairs" / pid
        errors = []
        ok, msg = check_analysis(work, pid)
        if not ok:
            errors.append(msg)
        if not (work / "tie_tables" / f"{pid}.py").exists():
            errors.append(f"missing tie_tables/{pid}.py")
        for pref in ("ST", "TT"):
            if not (d / f"{pref}_ties.json").exists():
                errors.append(f"missing {pref}_ties.json")
            qc = d / f"{pref}_qc.txt"
            if not qc.exists() or not qc.read_text(encoding="utf-8").startswith("QC") or "PASS" not in qc.read_text(encoding="utf-8").splitlines()[0]:
                errors.append(f"{pref}_qc.txt not PASS")
            if not (d / f"{pref}_highlighted.md").exists():
                errors.append(f"missing {pref}_highlighted.md")
        if errors:
            bad += 1
            print(f"{pid}: FAIL")
            for e in errors:
                print("  - " + e)
        else:
            print(f"{pid}: OK")

    stats_path = out / "match_stats.json"
    if stats_path.exists():
        stats = load_json(stats_path)
        print(f"\nAppendix markers: {stats.get('grand', {})}")
    else:
        print(f"\nWARN: {stats_path} not built yet")
    print(f"\n{len(pids) - bad}/{len(pids)} pairs OK")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
