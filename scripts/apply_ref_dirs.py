#!/usr/bin/env python3
"""Audit pass: add reference direction (A/C/E) to every R tie.

Operational rules (documented in out/audit/AUDIT.md):
  A (anaphoric)  - the referent is recoverable from the preceding co-text
                   (named entity, prior mention/proposition, or a quote
                   attribution that precedes the quoted pronoun).
  C (cataphoric)  - the referent is supplied by a later sentence. None exist
                   in this corpus (news register; cf. H&H 1976 on the rarity
                   of intersentential cataphora).
  E (exophoric)   - the referent lies outside the text: authorial/generic
                   1st person (author + readership), reader-addressing 2nd
                   person, with no in-text NP denoting them.

Also fixes two ante fields found incorrect during the audit:
  P09-VI-025 (bạn)  - ante pointed to a non-existent S008 "bạn"; the
                      referent is the reader (extra-textual) -> E.
  P20-VI-017 (chúng tôi) - inner quote spoken by the European Commission
                      (VI S011), not by Trent's organisation.
"""
import json
import glob
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- ties to label E (exophoric), with documented reasons -------------
E_SET = {
    # P07 EN — authorial/generic we-chain of the feature article
    'P07-EN-010': 'authorial we (author + readers), no in-text NP',
    'P07-EN-012': 'authorial we chain',
    'P07-EN-013': 'authorial we chain',
    'P07-EN-018': 'authorial us (English speakers incl. reader)',
    'P07-EN-020': 'authorial us chain',
    'P07-EN-030': 'authorial our',
    'P07-EN-061': 'authorial we chain',
    'P07-EN-101': 'authorial us - new Australians and old',
    'P07-EN-103': 'authorial my (author unnamed in text)',
    'P07-EN-107': 'authorial I (anecdote, author unnamed)',
    'P07-EN-114': "family/authorial our inside the author's own anecdote",
    'P07-EN-117': 'authorial I chain',
    # P07 VI — same authorial/generic chúng ta / ta / tôi chain
    'P07-VI-009': 'authorial chúng ta (author + readers)',
    'P07-VI-011': 'authorial chúng ta chain',
    'P07-VI-012': 'authorial chúng ta chain',
    'P07-VI-018': 'authorial chúng ta chain',
    'P07-VI-020': 'authorial chúng ta chain',
    'P07-VI-046': 'generic ta (Aussie speakers incl. reader)',
    'P07-VI-060': 'authorial chúng ta chain',
    'P07-VI-080': 'authorial chúng ta chain',
    'P07-VI-099': 'authorial chúng ta - người Úc mới và cũ',
    'P07-VI-101': 'authorial của tôi (author unnamed in text)',
    'P07-VI-105': 'authorial tôi (anecdote, author unnamed)',
    'P07-VI-112': "family/authorial của chúng ta inside the author's anecdote",
    'P07-VI-115': 'authorial tôi chain',
    # P09 VI — reader-addressing bạn (VI translator's explicit addressee)
    'P09-VI-025': 'reader-addressing bạn (bối cảnh phát ngôn)',
}

ANTE_FIXES = {
    'P09-VI-025': {
        'ante': 'ngoài văn bản: người đọc (bối cảnh phát ngôn)',
        'note': ('địa chỉ hoá người đọc (exophoric); EN counterpart "you" '
                 'không đánh dấu theo quy ước gộp của phép liên kết'),
    },
    'P20-VI-017': {
        'ante': 'S011: Ủy hội Âu châu (lời trích dẫn gián tiếp trong câu Trent)',
        'note': 'trích dẫn gián tiếp: chúng tôi = Ủy hội Âu châu',
    },
}

changed = {'E': 0, 'A': 0}
for path in sorted(glob.glob(os.path.join(BASE, 'out/pairs/P*/ST_ties.json'))) + \
             sorted(glob.glob(os.path.join(BASE, 'out/pairs/P*/TT_ties.json'))):
    d = json.load(open(path))
    ids_seen = set()
    for t in d['ties']:
        if t['cat'] != 'R':
            continue
        if t['id'] in E_SET:
            t['ref'] = 'E'
            t['ref_reason'] = E_SET[t['id']]
            changed['E'] += 1
        else:
            t['ref'] = 'A'
            changed['A'] += 1
        if t['id'] in ANTE_FIXES:
            for k, v in ANTE_FIXES[t['id']].items():
                t[k] = v
        ids_seen.add(t['id'])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')

missing = set(E_SET) - ids_seen
print(f"R ties labelled: A={changed['A']}, E={changed['E']}, C=0")
print('E ids not found:', missing if missing else 'none')
