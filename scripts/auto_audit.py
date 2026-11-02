#!/usr/bin/env python3
"""Automated content audit over all tie tables.

Checks:
  1. R ties: sub taxonomy + ref direction present; E-ref ties must not have
     an in-text (Sxxx) antecedent; A-ref ties must have one.
  2. C ties (conjunction): item checked against H&H-style connective lexicons
     (EN + VI). Unknown items are flagged for human review.
  3. L ties: sub taxonomy membership.
  4. Ellipsis ties: text=None, gap_after & recovered present.
  5. Confidence distribution; all low-confidence ties listed.
Outputs: out/audit/auto_checks.txt + out/audit/audit_stats.json
"""
import json
import glob
import re
from collections import Counter, defaultdict

AUD = '/home/z/my-project/out/audit'

R_SUBS = {'personal', 'demonstrative', 'comparative', 'quantified'}
L_SUBS = {'repetition', 'synonym', 'antonym', 'collocation', 'superordinate',
          'hyponym', 'general word', 'near-synonym', 'meronym', 'derived',
          'phrase-level repetition'}

# H&H conjunction word classes (abridged to what occurs in news prose)
EN_CONJ = {
    # adversative
    'but', 'however', 'yet', 'still', 'though', 'although', 'while',
    'whereas', 'instead', 'rather', 'nevertheless', 'nonetheless',
    'on the other hand', 'in contrast', 'by contrast', 'conversely',
    # additive
    'and', 'also', 'too', 'as well', 'in addition', 'moreover', 'furthermore',
    'besides', 'similarly', 'likewise', 'firstly', 'secondly', 'thirdly',
    'lastly', 'finally', 'even', 'equally',
    # temporal
    'when', 'after', 'before', 'since', 'until', 'once', 'then', 'next',
    'later', 'soon', 'meanwhile', 'at the same time', 'afterwards',
    'eventually', 'previously', 'earlier', 'today', 'now', 'so far',
    # causal
    'so', 'therefore', 'thus', 'hence', 'consequently', 'as a result',
    'because', 'accordingly', 'in turn', 'that is why', "that's why",
    'overall', 'altogether', 'in short', 'in conclusion',
}
VI_CONJ = {
    'nhưng', 'tuy nhiên', 'song', 'mà', 'thay vào đó', 'ngược lại',
    'trong khi', 'trong khi đó', 'mặc dù', 'dù', 'dù vậy', 'mặc dầu',
    'tuy vậy', 'đối lại', 'khác với', 'khác với điều đó',
    'và', 'cũng', 'ngoài ra', 'thêm vào đó', 'hơn nữa', 'ngoái lại',
    'đồng thời', 'tương tự', 'tương tự như vậy', 'cả', 'kể cả',
    'trước tiên', 'thứ hai', 'thứ ba', 'cuối cùng', 'sau cùng', 'rồi',
    'khi', 'sau khi', 'trước khi', 'trước đó', 'kể từ khi', 'đến khi',
    'một khi', 'sau đó', 'tiếp theo', 'về sau', 'cuối cùng',
    'trong lúc đó', 'meanwhile', 'vừa... vừa',
    'vì', 'vì vậy', 'do đó', 'do vậy', 'bởi vì', 'bởi vậy', 'cho nên',
    'vì thế', 'hậu quả là', 'kết quả là', 'do đó,', 'như vậy', 'như vậy là',
    'vì thế nên', 'tóm lại', 'nói chung', 'điều đó có nghĩa là',
    'theo đó', 'hơn thế nữa', 'và như vậy', 'nên', 'bởi',
}

SENT_ID = re.compile(r'S\d{3}')

flagged = []
stats = defaultdict(lambda: defaultdict(Counter))
low_conf = []
conj_unknown = Counter()
conj_items = Counter()

for path in sorted(glob.glob('/home/z/my-project/out/pairs/P*/ST_ties.json')) + \
             sorted(glob.glob('/home/z/my-project/out/pairs/P*/TT_ties.json')):
    d = json.load(open(path))
    pid, lang = d['pair'], d['lang']
    for t in d['ties']:
        cat = t['cat']
        stats[pid][lang][cat] += 1
        if t.get('conf') == 'low':
            low_conf.append(f"{t['id']} [{cat}/{t.get('sub')}] "
                            f"item={t['text']!r} ante={t.get('ante')!r}")
        if cat == 'R':
            if t.get('sub') not in R_SUBS:
                flagged.append(f"{t['id']}: R sub={t.get('sub')!r} outside taxonomy")
            ref = t.get('ref')
            if ref not in ('A', 'C', 'E'):
                flagged.append(f"{t['id']}: missing/invalid ref={ref!r}")
            has_sent_ante = bool(SENT_ID.search(t.get('ante') or ''))
            if ref == 'E' and has_sent_ante:
                flagged.append(f"{t['id']}: E-ref but ante cites in-text sentence: "
                               f"{t.get('ante')!r}")
            if ref == 'A' and not has_sent_ante:
                flagged.append(f"{t['id']}: A-ref but no in-text antecedent: "
                               f"{t.get('ante')!r}")
            if pid == 'P09' and t['id'] == 'P09-VI-025':
                pass  # known, fixed
        elif cat == 'C':
            item = (t['text'] or '').strip()
            key = item.lower().rstrip(',;:')
            conj_items[(lang, key)] += 1
            lex = EN_CONJ if lang == 'EN' else VI_CONJ
            if key not in lex and not any(k in key for k in lex):
                conj_unknown[(lang, key)] += 1
        elif cat == 'L':
            if t.get('sub') not in L_SUBS:
                flagged.append(f"{t['id']}: L sub={t.get('sub')!r} outside taxonomy")
        elif cat == 'E':
            if t['text'] is not None or not t.get('gap_after') \
                    or not t.get('recovered'):
                flagged.append(f"{t['id']}: ellipsis shape invalid: "
                               f"text={t['text']!r} gap={t.get('gap_after')!r} "
                               f"rec={t.get('recovered')!r}")
        elif cat == 'S':
            if t.get('sub') not in ('nominal', 'verbal', 'clausal'):
                flagged.append(f"{t['id']}: S sub={t.get('sub')!r} "
                               f"(H&H: nominal/verbal/clausal)")

with open(f'{AUD}/auto_checks.txt', 'w', encoding='utf-8') as f:
    f.write('=== STRUCTURAL FLAGS ===\n')
    f.write('\n'.join(flagged) if flagged else 'none\n')
    f.write('\n\n=== CONJUNCTION ITEMS NOT IN LEXICON (review) ===\n')
    for (lang, item), n in sorted(conj_unknown.items()):
        f.write(f'{lang} {item!r} x{n}\n')
    f.write('\n\n=== LOW CONFIDENCE TIES ===\n')
    f.write('\n'.join(low_conf) if low_conf else 'none\n')

json_stats = {}
for pid in sorted(stats):
    json_stats[pid] = {
        'EN': dict(stats[pid]['EN']),
        'VI': dict(stats[pid]['VI']),
    }
grand = {'EN': Counter(), 'VI': Counter()}
for pid in stats:
    for lang in ('EN', 'VI'):
        grand[lang] += stats[pid][lang]
json_stats['grand'] = {'EN': dict(grand['EN']), 'VI': dict(grand['VI'])}

# R direction stats
ref_stats = {}
tot = Counter()
for path in sorted(glob.glob('/home/z/my-project/out/pairs/P*/ST_ties.json')) + \
             sorted(glob.glob('/home/z/my-project/out/pairs/P*/TT_ties.json')):
    d = json.load(open(path))
    pid, lang = d['pair'], d['lang']
    for t in d['ties']:
        if t['cat'] == 'R':
            ref_stats.setdefault(pid, {}).setdefault(lang, Counter())
            ref_stats[pid][lang][t.get('ref')] += 1
            tot[(lang, t.get('ref'))] += 1
json_stats['R_direction'] = {
    pid: {lang: dict(c) for lang, c in langs.items()}
    for pid, langs in ref_stats.items()
}
json_stats['R_direction']['grand'] = {
    f'{lang}_ref_{r}': n for (lang, r), n in sorted(tot.items())
}

with open(f'{AUD}/audit_stats.json', 'w', encoding='utf-8') as f:
    json.dump(json_stats, f, ensure_ascii=False, indent=1)

print(f'structural flags: {len(flagged)}')
for x in flagged[:20]:
    print('  ', x)
print(f'unknown conjunction items: {len(conj_unknown)}')
print(f'low-confidence ties: {len(low_conf)}')
print('R direction grand:', dict(tot))
