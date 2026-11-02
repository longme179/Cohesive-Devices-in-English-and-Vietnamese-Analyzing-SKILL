#!/usr/bin/env python3
"""
Giai đoạn D (bước tiền xử lý) — dựng BẢN ĐỒ CÂU EN<->VI cho 20 cặp. v2

Nguyên tắc (REPLICATION_GUIDE §4):
- Link align chỉ tin cậy khi biết câu EN nào dịch sang câu VI nào (bước 4 + 12).

Phương pháp 2 lớp:
  LỚP 1 (xương tự tin): DP đơn điệu chỉ dùng tín hiệu mạnh —
    neo số liệu/tên riêng (3đ) + phiếu bầu align cũ (1đ, cap 3).
    Cắt/tự sinh miễn phí (0đ) → khối không tín hiệu mặc định rơi vào khoảng trống.
  LỚP 2 (hòa giải khoảng trống): giữa 2 khối xương, dư EN↔VI bao nhiêu câu
    thì ghép 1-1 theo thứ tự với tương đồng độ dài; dư EN = cắt (chọn cặp
    khớp tệ nhất), dư VI = tự sinh. Mọi khối hòa giải đánh dấu inferred=true
    để soát tay.

Output: out/align_v2/PXX_sent_map_draft.json
"""
import json
import os
import re
import sys

BASE = '/home/z/my-project'

CAP_STOP = {
    'The', 'And', 'But', 'He', 'She', 'It', 'They', 'We', 'In', 'On', 'At',
    'For', 'From', 'With', 'This', 'That', 'These', 'Those', 'His', 'Her',
    'Their', 'Our', 'Your', 'My', 'A', 'An', 'As', 'By', 'If', 'Not', 'So',
    'There', 'When', 'While', 'What', 'Who', 'Which', 'How', 'Why', 'All',
    'Some', 'Many', 'Few', 'Both', 'Each', 'Other', 'Another', 'One', 'Two',
    'Three', 'Four', 'Five', 'Now', 'Then', 'After', 'Before', 'During',
    'According', 'Or', 'Nor', 'Yet', 'Than', 'Because', 'Since', 'However',
    'Meanwhile', 'Instead', 'Rather', 'Even', 'Only', 'Most', 'More', 'Less',
    'Under', 'Over', 'Between', 'Among', 'About', 'Into', 'Through',
    'Against', 'Without', 'Within', 'Across', 'Along', 'Behind', 'Beyond',
    'Toward', 'Towards', 'Up', 'Down', 'Out', 'Off', 'Again', 'Further',
    'Once', 'Here', 'Where', 'Whose', 'Whom', 'Us', 'Them', 'Him', 'Me',
    'You', 'Am', 'Is', 'Are', 'Was', 'Were', 'Be', 'Been', 'Being', 'Has',
    'Have', 'Had', 'Do', 'Does', 'Did', 'Will', 'Would', 'Can', 'Could',
    'Should', 'May', 'Might', 'Must', 'Shall', 'Said', 'Says', 'Say', 'Told',
    'Tell', 'New', 'First', 'Last', 'Next', 'No', 'Yes', 'Mr', 'Mrs', 'Ms',
    'Dr', 'St',
}
NUM_RE = re.compile(r'\d+(?:[.,]\d+)*%?')
LATIN_RE = re.compile(r'[A-Za-zÀ-ỹ]{2,}')


def anchors(text):
    toks = set()
    for m in NUM_RE.finditer(text):
        s = m.group(0).rstrip('%').rstrip('.')
        if s and s.replace('.', '').strip('0') not in ('',):
            toks.add('#' + s.replace(',', '.'))
    words = LATIN_RE.findall(text)
    i = 0
    while i < len(words):
        if words[i][0].isupper():
            j = i
            while j < len(words) and words[j][0].isupper():
                j += 1
            phrase = ' '.join(words[i:j]).lower()
            if (j - i) >= 2 or words[i] not in CAP_STOP:
                toks.add('@' + phrase)
            i = j
        else:
            i += 1
    return toks


def load_pairs():
    for n in range(1, 21):
        pid = f'P{n:02d}'
        d = os.path.join(BASE, 'out', 'pairs', pid)
        if os.path.isdir(d):
            yield pid, d


def build_map(pid, dirp, verbose=False):
    st = json.load(open(os.path.join(dirp, 'ST_seg.json')))
    tt = json.load(open(os.path.join(dirp, 'TT_seg.json')))
    en, vi = st['sentences'], tt['sentences']
    E, V = len(en), len(vi)
    en_anch = [anchors(s['text']) for s in en]
    vi_anch = [anchors(s['text']) for s in vi]
    en_len = [len(s['text'].split()) for s in en]
    vi_len = [len(s['text'].split()) for s in vi]

    votes = {}
    apath = os.path.join(dirp, 'align.json')
    if os.path.exists(apath):
        st_ties = {t['id']: t for t in json.load(
            open(os.path.join(dirp, 'ST_ties.json')))['ties']}
        tt_ties = {t['id']: t for t in json.load(
            open(os.path.join(dirp, 'TT_ties.json')))['ties']}
        for row in json.load(open(apath))['alignments']:
            if row.get('outcome') not in ('kept', 'shifted'):
                continue
            stie = st_ties.get(row.get('st_tie'))
            ttie = tt_ties.get(row.get('tt_tie'))
            if stie and ttie:
                key = (stie['sent'], ttie['sent'])
                votes[key] = votes.get(key, 0) + 1

    def sig(i, j):
        shared = len(en_anch[i] & vi_anch[j])
        v = votes.get((en[i]['id'], vi[j]['id']), 0)
        return 3.0 * shared + 1.0 * min(v, 3)

    # ---------- LỚP 1: DP xương ----------
    NEG = -1e9
    f = [[NEG] * (V + 1) for _ in range(E + 1)]
    back = [[None] * (V + 1) for _ in range(E + 1)]
    f[0][0] = 0.0
    for i in range(E + 1):
        for j in range(V + 1):
            cur = f[i][j]
            if cur == NEG:
                continue
            if i < E and j < V:
                s = cur + sig(i, j)
                if s > f[i + 1][j + 1]:
                    f[i + 1][j + 1], back[i + 1][j + 1] = s, ('m', i, j)
            if i < E:  # cắt miễn phí
                if f[i + 1][j] < cur:
                    f[i + 1][j], back[i + 1][j] = cur, ('cut', i, j)
            if j < V:  # tự sinh miễn phí
                if f[i][j + 1] < cur:
                    f[i][j + 1], back[i][j + 1] = cur, ('sg', i, j)
    # truy vết xương
    skel = []
    i, j = E, V
    while (i, j) != (0, 0):
        op = back[i][j]
        kind, pi, pj = op
        if kind == 'm':
            skel.append((pi, pj))
        i, j = pi, pj
    skel.reverse()  # danh sách cặp (en_idx, vi_idx) khớp chắc

    # ---------- LỚP 2: hòa giải khoảng trống ----------
    def len_sim(a, b):
        return 1 - min(1.0, abs(a - b) / (a + b + 1.0) * 2)

    def reconcile(en_lo, en_hi, vi_lo, vi_hi):
        """Ghép khoảng EN [lo,hi) với VI [lo,hi): trả list khối."""
        ne, nv = en_hi - en_lo, vi_hi - vi_lo
        blocks = []
        if ne == 0 and nv == 0:
            return blocks
        if nv == 0:
            return [('cut', list(range(en_lo, en_hi)), [], True)]
        if ne == 0:
            return [('sg', [], list(range(vi_lo, vi_hi)), True)]
        if ne == nv:
            return [('map', [k], [w], True)
                    for k, w in zip(range(en_lo, en_hi), range(vi_lo, vi_hi))]
        # ne != nv: ghép 1-1 cặp khớp tốt nhất theo độ dài, phần dư → cut/sg
        sims = {}
        for k in range(en_lo, en_hi):
            for w in range(vi_lo, vi_hi):
                sims[(k, w)] = len_sim(en_len[k], vi_len[w]) \
                    + 0.5 * len(en_anch[k] & vi_anch[w])
        # tham: ghép theo thứ tự mỗi câu EN với VI gần vị trí tương đối
        pairs = []
        used_vi = set()
        order = sorted(sims.items(), key=lambda kv: -kv[1])
        assigned = {}
        for (k, w), s in order:
            if k in assigned or w in used_vi:
                continue
            assigned[k] = w
            used_vi.add(w)
        for k in range(en_lo, en_hi):
            if k in assigned:
                pairs.append(('map', [k], [assigned[k]], True))
            else:
                pairs.append(('cut', [k], [], True))
        for w in range(vi_lo, vi_hi):
            if w not in used_vi:
                pairs.append(('sg', [], [w], True))
        pairs.sort(key=lambda b: (b[1][0] if b[1] else 1e9,
                                  b[2][0] if b[2] else 1e9))
        return pairs

    allblocks = []
    prev_i = prev_j = 0
    for (a, b) in skel:
        gap = reconcile(prev_i, a, prev_j, b)
        allblocks.extend(gap)
        allblocks.append(('map', [a], [b], False))  # xương: tự tin
        prev_i, prev_j = a + 1, b + 1
    allblocks.extend(reconcile(prev_i, E, prev_j, V))

    # ---------- đóng gói ----------
    en2vi, cut_en, selfgen_vi = {}, [], []
    inferred = []
    for kind, eidx, vidx, inf in allblocks:
        eids = [en[k]['id'] for k in eidx]
        vids = [vi[w]['id'] for w in vidx]
        if kind == 'map':
            for e in eids:
                en2vi[e] = vids
            if inf:
                inferred.append({'en': eids, 'vi': vids})
        elif kind == 'cut':
            cut_en.extend(eids)
        else:
            selfgen_vi.extend(vids)

    out = {
        'pair': pid,
        'en2vi': en2vi,
        'cut_en': cut_en,
        'selfgen_vi': selfgen_vi,
        'n_en': E, 'n_vi': V,
        'n_skeleton': len(skel),
        'inferred_gap_blocks': inferred,
    }
    if verbose:
        print(f"{pid}: E={E} V={V} mapped={len(en2vi)} cut={len(cut_en)} "
              f"selfgen={len(selfgen_vi)} skeleton={len(skel)} "
              f"inferred={len(inferred)}")
    return out


def main():
    os.makedirs(os.path.join(BASE, 'out', 'align_v2'), exist_ok=True)
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for pid, dirp in load_pairs():
        if only and pid not in only:
            continue
        out = build_map(pid, dirp, verbose=True)
        path = os.path.join(BASE, 'out', 'align_v2', f'{pid}_sent_map_draft.json')
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump(out, fh, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
