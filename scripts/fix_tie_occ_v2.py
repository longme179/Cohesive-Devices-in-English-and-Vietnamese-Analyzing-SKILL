#!/usr/bin/env python3
"""
Fix mid-word occurrence bugs in tie tables (v2 - precise line matching).
"""
import re
import os

BASE = '/home/z/my-project'
TIE_DIR = os.path.join(BASE, 'scripts', 'tie_tables')

# All fixes: (pair, lang, sent, text, old_occ, new_occ) or text fixes: (pair, lang, sent, old_text, new_text)
OCC_FIXES = [
    # (pair, lang, sent, text, old_occ, new_occ)
    ('P03', 'ST', 'S013', 'he', 1, 2),
    ('P03', 'ST', 'S019', 'it', 2, 3),
    ('P10', 'ST', 'S006', 'he', 2, 4),
    ('P10', 'ST', 'S017', 'he', 1, 2),
    ('P15', 'ST', 'S002', 'his', 1, 2),
    ('P15', 'ST', 'S014', 'he', 1, 2),
    ('P15', 'ST', 'S016', 'he', 1, 3),
    ('P17', 'ST', 'S014', 'he', 1, 2),
]

TEXT_FIXES = [
    # (pair, lang, sent, old_text, new_text)  — occ stays the same (1)
    ('P09', 'TT', None, 'thanh toán bulk-bill', 'thanh toán bulk-billing'),
    ('P18', 'ST', None, 'life-savin', 'life-saving'),
]


def fix_file(pair, fixes_for_file, text_fixes_for_file):
    """Apply fixes to one tie table file."""
    path = os.path.join(TIE_DIR, f'{pair}.py')
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    changed = 0
    current_section = None  # 'ST' or 'TT'

    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('ST = [') or stripped.startswith('ST='):
            current_section = 'ST'
        elif stripped.startswith('TT = [') or stripped.startswith('TT='):
            current_section = 'TT'
        elif stripped.startswith(']'):
            current_section = None

        if current_section is None:
            continue

        # Apply occ fixes
        for (pair_, lang, sent, text, old_occ, new_occ) in fixes_for_file:
            if lang != current_section:
                continue
            if f"'{sent}'" in line and f"'{text}'" in line and line.rstrip().endswith(f'{old_occ}),'):
                new_line = re.sub(rf'(\s){old_occ}\),$', rf'\g<1>{new_occ}),', line.rstrip() + '\n')
                lines[i] = new_line
                changed += 1
                print(f"  {pair} {lang}: '{text}' in {sent}: occ {old_occ} -> {new_occ}")

        # Apply text fixes
        for (pair_, lang, sent, old_text, new_text) in text_fixes_for_file:
            if lang != current_section:
                continue
            if f"'{old_text}'" in line:
                new_line = line.replace(f"'{old_text}'", f"'{new_text}'")
                lines[i] = new_line
                changed += 1
                print(f"  {pair} {lang}: text '{old_text}' -> '{new_text}'")

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return changed


def main():
    total = 0
    # Group fixes by pair
    pairs = set(f[0] for f in OCC_FIXES) | set(f[0] for f in TEXT_FIXES)
    for pair in sorted(pairs):
        occ_fixes = [f for f in OCC_FIXES if f[0] == pair]
        text_fixes = [f for f in TEXT_FIXES if f[0] == pair]
        print(f"\n{pair}:")
        total += fix_file(pair, occ_fixes, text_fixes)

    print(f"\nTotal changes: {total}")


if __name__ == '__main__':
    main()
