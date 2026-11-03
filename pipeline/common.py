"""Shared constants and helpers for the COHESION EN–VI skill pipeline.

This package is deliberately dependency-free for ingest/segment/annotate/render/
build.  Only DOCX/PDF export needs python-docx / WeasyPrint.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

# Final Appendix 1 palette (v7).  Keep this table as the single source of truth:
# build_appendix, export_docx and render all read it.
CATS = {
    "R": {
        "bg": "#FFFF00", "fg": "#000000", "emoji": "🟨",
        "en": "Reference", "vi": "tham chiếu (đại từ, chỉ từ)",
    },
    "S": {
        "bg": "#00FF00", "fg": "#000000", "emoji": "🟩",
        "en": "Substitution", "vi": "thay thế",
    },
    "E": {
        "bg": "#0000FF", "fg": "#FFFFFF", "emoji": "🟦",
        "en": "Ellipsis", "vi": "lược bỏ (∅ = vị trí trống)",
    },
    "C": {
        "bg": "#FF9900", "fg": "#000000", "emoji": "🟧",
        "en": "Conjunction", "vi": "liên kết",
    },
    "L": {
        "bg": "#9900FF", "fg": "#FFFFFF", "emoji": "🟪",
        "en": "Lexical cohesion", "vi": "liên kết từ vựng",
    },
}

FRAMEWORK_MAP = [
    ("R", "reference (personal, demonstrative, comparative, quantified)",
     "phép thế đại từ (đại từ / chỉ từ) — cùng nhóm với S"),
    ("S", "substitution (nominal, verbal, clausal)",
     "phép thế đại từ (phần thế danh từ / động từ / mệnh đề)"),
    ("E", "ellipsis", "phép tỉnh lược"),
    ("C", "conjunction (adversative, additive, temporal, causal)",
     "phép nối"),
    ("L", "lexical cohesion (repetition, synonymy, antonymy, collocation)",
     "phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng"),
]

REF_NAMES = {"A": "anaphoric", "C": "cataphoric", "E": "exophoric"}


def pair_dir(work: str | Path, pid: str) -> Path:
    return Path(work) / "pairs" / pid


def load_json(path: str | Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_json(path: str | Path, obj) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def pair_ids(work: str | Path) -> list[str]:
    root = Path(work) / "pairs"
    if not root.is_dir():
        return []
    return sorted(p.name for p in root.iterdir() if p.is_dir())


def clean_cell(text: str) -> str:
    """Turn a markdown table cell into the plain text used for annotation."""
    text = text.strip()
    # [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"\\([\[\]|*_])", r"\1", text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\s*\n\s*", " ", text).strip()
    if text.lower() in {"none", "(?)", "?"}:
        return ""
    return text


def split_table_row(line: str) -> list[str]:
    """Split a markdown table row on unescaped pipes."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", body)]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells)


def is_url(cell: str) -> bool:
    c = cell.strip()
    return bool(re.match(r"https?://", c)) or bool(
        re.fullmatch(r"\[[^\]]*\]\(https?://[^)]+\)", c)
    )


def is_header(cells: list[str]) -> bool:
    if len(cells) < 2:
        return False
    a, b = cells[0].strip().lower(), cells[1].strip().lower()
    return (a in {"tiếng anh", "english", "en", "eng"} and
            b in {"tiếng việt", "vietnamese", "vi", "vie"})


def is_title_row(cells: list[str]) -> bool:
    if len(cells) < 2 or not all(cells[:2]):
        return False
    a, b = cells[0], cells[1]
    return ("](" in a and "](" in b) or (
        a.startswith("**") and b.startswith("**"))
