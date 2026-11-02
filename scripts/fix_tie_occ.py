#!/usr/bin/env python3
"""
Auto-fix mid-word occurrence bugs in tie tables.
For each tie where the marked text lands mid-word at the given occurrence,
find the correct word-boundary occurrence and update the tie table.
"""
import re
import json
import os
import sys

BASE = '/home/z/my-project'
TIE_DIR = os.path.join(BASE, 'scripts', 'tie_tables')
PAIRS_DIR = os.path.join(BASE, 'out', 'pairs')


def find_word_boundary_occurrences(text, sub):
    """Find all occurrences of sub in text where sub is a whole word."""
    occurrences = []
    idx = 0
    while True:
        idx = text.find(sub, idx)
        if idx == -1:
            break
        start_ok = idx == 0 or not (text[idx-1].isalnum() and sub[0].isalnum())
        end = idx + len(sub)
        end_ok = end >= len(text) or not (text[end].isalnum() and sub[-1].isalnum())
        if start_ok and end_ok:
            occurrences.append(idx + 1)  # 1-indexed position
        idx += 1
    return occurrences


def find_substring_occurrences(text, sub):
    """Find all substring occurrences (1-indexed)."""
    occurrences = []
    idx = 0
    while True:
        idx = text.find(sub, idx)
        if idx == -1:
            break
        occurrences.append(idx + 1)
        idx += 1
    return occurrences


def analyze_pair(pair_id):
    """Analyze a pair for mid-word marking issues and propose fixes."""
    issues = []
    for lang, prefix in [('EN', 'ST'), ('VI', 'TT')]:
        seg_path = os.path.join(PAIRS_DIR, pair_id, f'{prefix}_seg.json')
        ties_path = os.path.join(PAIRS_DIR, pair_id, f'{prefix}_ties.json')
        with open(seg_path) as f:
            seg = json.load(f)
        with open(ties_path) as f:
            ties = json.load(f)['ties']
        sents = {s['id']: s['text'] for s in seg['sentences']}

        for t in ties:
            if t.get('recovered') or not t.get('text'):
                continue
            text = t['text']
            sent_id = t['sent']
            if sent_id not in sents:
                continue
            stext = sents[sent_id]
            occ = t.get('occ', 1)

            # Find the occ-th substring occurrence
            sub_occs = find_substring_occurrences(stext, text)
            if occ > len(sub_occs):
                continue
            pos = sub_occs[occ - 1] - 1  # 0-indexed

            # Check word boundaries
            start_ok = pos == 0 or not (stext[pos-1].isalnum() and text[0].isalnum())
            end = pos + len(text)
            end_ok = end >= len(stext) or not (stext[end].isalnum() and text[-1].isalnum())

            if not start_ok or not end_ok:
                # Bug! Find correct word-boundary occurrence
                word_occs = find_word_boundary_occurrences(stext, text)
                sub_count = len(sub_occs)
                # The correct occ (in substring numbering) that is also word-boundary
                correct_occ = None
                for wo in word_occs:
                    # wo is 1-indexed position; find which substring-occ index this is
                    wo_idx0 = wo - 1
                    for si, so in enumerate(sub_occs):
                        if so == wo:
                            correct_occ = si + 1
                            break
                    if correct_occ:
                        break

                context = stext[max(0, pos-25):pos+len(text)+25]
                issues.append({
                    'pair': pair_id, 'lang': lang, 'id': t['id'],
                    'text': text, 'current_occ': occ,
                    'correct_occ': correct_occ,
                    'word_occs_count': len(word_occs),
                    'context': context,
                })
    return issues


def fix_tie_table(pair_id, fixes):
    """Apply occ fixes to the tie table Python file."""
    lang_prefixes = {'EN': 'ST', 'VI': 'TT'}
    for lang, fix_list in fixes.items():
        table_path = os.path.join(TIE_DIR, f'{pair_id}.py')
        with open(table_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for fix in fix_list:
            tie_id = fix['id']
            old_occ = fix['current_occ']
            new_occ = fix['correct_occ']
            text = fix['text']

            if new_occ is None:
                print(f"  WARNING: no word-boundary occurrence for {tie_id} '{text}' - cannot auto-fix")
                continue

            # Find the line with this tie text and occ
            # Tie table format: rows like (sent, text, cat, sub, ante, conf, alt, note, occ)
            # We need to find the specific row and update occ
            # Look for pattern: 'text', ... , old_occ)
            # Escape special regex chars in text
            esc_text = re.escape(text)
            # Pattern: find the row containing this text
            # Rows are tuples like ('S017', 'he', 'R', ..., 1)
            pattern = rf"('{fix.get('sent', '')}'\s*,\s*'{esc_text}'\s*,.*?)\b{old_occ}\b\s*\)"

            # Simpler: search line by line
            lines = content.split('\n')
            fixed = False
            for li, line in enumerate(lines):
                # Match: contains 'text' and ends with old_occ)
                if f"'{text}'" in line and line.rstrip().endswith(f'{old_occ})'):
                    # Check if this is the right row (by sent if available)
                    if fix.get('sent') and fix['sent'] not in line:
                        continue
                    # Update occ
                    new_line = re.sub(rf'\b{old_occ}\s*\)$', f'{new_occ})', line.rstrip())
                    lines[li] = new_line
                    fixed = True
                    print(f"  Fixed {tie_id}: '{text}' occ {old_occ} -> {new_occ}")
                    break

            if not fixed:
                print(f"  WARNING: could not find line for {tie_id} '{text}' occ={old_occ}")

        with open(table_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))


def main():
    all_issues = []
    for i in range(1, 21):
        pair_id = f'P{i:02d}'
        issues = analyze_pair(pair_id)
        if issues:
            all_issues.extend(issues)

    print(f"Total issues: {len(all_issues)}\n")

    # Group by pair
    by_pair = {}
    for iss in all_issues:
        by_pair.setdefault(iss['pair'], []).append(iss)

    for pair_id, issues in sorted(by_pair.items()):
        print(f"\n{pair_id}:")
        for iss in issues:
            print(f"  {iss['id']} [{iss['lang']}]: '{iss['text']}' occ={iss['current_occ']} -> {iss['correct_occ']}")
            print(f"    Context: ...{iss['context']}...")

    # Save issues for reference
    with open(os.path.join(BASE, 'out', 'appendix1', 'tie_fixes_needed.json'), 'w', encoding='utf-8') as f:
        json.dump(all_issues, f, ensure_ascii=False, indent=2)

    # Ask for confirmation or auto-fix
    if '--fix' in sys.argv:
        print("\n\nApplying fixes...")
        for pair_id, issues in sorted(by_pair.items()):
            fixes_by_lang = {}
            for iss in issues:
                fixes_by_lang.setdefault(iss['lang'], []).append(iss)
            # Add sent info
            for lang, fl in fixes_by_lang.items():
                for f_ in fl:
                    # Get sent from tie id or look up
                    pass
            print(f"\n{pair_id}:")
            # Re-read tie data to get sent
            for lang, fl in fixes_by_lang.items():
                prefix = 'ST' if lang == 'EN' else 'TT'
                ties_path = os.path.join(PAIRS_DIR, pair_id, f'{prefix}_ties.json')
                with open(ties_path) as f:
                    ties = json.load(f)['ties']
                tie_map = {t['id']: t for t in ties}
                for f_ in fl:
                    if f_['id'] in tie_map:
                        f_['sent'] = tie_map[f_['id']]['sent']
            fix_tie_table(pair_id, fixes_by_lang)


if __name__ == '__main__':
    main()
