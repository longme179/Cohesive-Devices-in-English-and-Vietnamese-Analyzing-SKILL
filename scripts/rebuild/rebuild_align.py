#!/usr/bin/env python3
"""
GIAI ĐOẠN D — DỰNG LẠI BẢNG ALIGN 20 CẶP THEO GIAO THỨC MỚI
(REPLICATION_GUIDE §4 bước 12–13, schema §5)

Quy tắc (mỗi link phải giải thích được bằng ngữ nghĩa):
1. Tie EN nằm trong câu KHÔNG có bản dịch (bản đồ câu) → outcome=omitted,
   om_kind=cut. KHÔNG bao giờ gắn omitted theo mã câu (bẫy 10).
2. Link st_tie→tt_tie chỉ nhận khi tt_tie nằm trong câu VI tương ứng theo
   bản đồ câu (chống zip vị trí — bẫy 9) VÀ hợp loại/tham chiếu.
   Nguồn ứng viên: (a) link cũ đã qua kiểm bản đồ câu; (b) tìm đối tác trong
   cùng cặp câu theo điểm (loại + loại phụ + trùng tiền trạm + vị trí).
3. Tie EN ở câu CÓ dịch nhưng không tìm được tie VI đối ứng:
   - align cũ ghi omitted (item không được render — vi-lược) → omitted,
     om_kind=drop;
   - còn lại → kept_unmarked (hiện thực hóa bằng cụm không đánh dấu).
4. Tie EN ở câu có dịch, link được nhưng khác danh mục → shifted (R>L...).
5. Tie VI không tie EN nào nhắc → added:
   - added_real: câu VI tự sinh (lede/byline/paraphrase) hoặc câu trùng nguồn;
   - added_inventory: bất đối xứng kiểm kê (đối ứng EN là first-mention
     không đánh dấu — bẫy 12).

Cổng kiểm 13 (in ra + gate):
- kept + shifted + kept_unmarked + omitted = tổng ST tie;
- mọi omitted-cut nằm trong câu bỏ; mọi om-drop nằm trong câu CÓ dịch;
- mọi link kept/shifted: câu tt_tie ∈ en2vi[câu st_tie];
- added + (tt tie được link) = tổng TT tie;
- dump link đáng ngờ (khác loại + không trùng tiền trạm) để soát tay.
"""
import json
import os
import re
import sys
import unicodedata

BASE = '/home/z/my-project'
OUT = os.path.join(BASE, 'out', 'align_v2')

# Sửa link tay sau soát cổng 13 (mỗi mục truy vết về đọc ngữ nghĩa)
LINK_FIXES = {
    'P01': {
        'P01-EN-032': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "visitor centre — VI S013 'Trung tâm Khám phá Nước Tái "
                    "chế' không đánh dấu; 'tái chế nước' là đối ứng của "
                    "'water recycling' (EN-033)",
        },
        'P01-EN-114': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "khung dẫn dịch chỗ: 'Khan says' ở EN S044 → 'Giáo sư "
                    "Khan cho biết' cuối VI S045; S044 không còn mention",
        },
    },
    'P04': {
        'P04-EN-054': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "gộp S022+S023 → VI S017; khung dẫn 'Shriane said' bị "
                    "lược trong bản gộp",
        },
    },
    'P05': {
        'P05-EN-004': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "fines — VI S003 'tiền phạt' không đánh dấu "
                    "(first-mention theo quy ước VI)",
        },
        'P05-EN-066': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "'1 January' — VI S024 'Từ ngày 1 tháng 1' không đánh "
                    "dấu (công thức lặp của listicle không tie hóa phía VI)",
        },
        'P05-EN-089': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "'Aged Care Award workers' — VI S035 'Những người chăm "
                    "sóc' không đánh dấu; 'người cao tuổi' thuộc chuỗi aged-"
                    "care, không phải đối số của workers",
        },
    },
    'P07': {
        'P07-EN-032': {
            'outcome': 'kept', 'tt_tie': 'P07-VI-031', 'shift': None,
            'note': "British → người Anh (S023)",
        },
        'P07-EN-092': {
            'outcome': 'kept', 'tt_tie': 'P07-VI-090', 'shift': None,
            'note': "idioms → 'Những thành ngữ hài hước này' (gộp marker "
                    "với EN-091 'These')",
        },
    },
    'P20': {
        'P20-EN-003': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "'Continuing violations' — VI S006 'tiếp tục vi phạm' "
                    "không đánh dấu (bỏ sót tie TT — phân tích P20 §9)",
        },
        'P20-EN-004': {
            'outcome': 'kept', 'tt_tie': 'P20-VI-009', 'shift': None,
            'note': "South Korean-flagged ships → 'Nam Triều Tiên' trong "
                    "cụm 'tàu thuyền treo cờ Nam Triều Tiên' (S006)",
        },
    },
    'P08': {
        'P08-EN-073': {
            'outcome': 'kept_unmarked', 'tt_tie': None, 'shift': None,
            'note': "Will it be a buyer's market in 2025? → Liệu năm 2025 "
                    "có phải là thị trường của người mua nhà? — VI không có "
                    "đại từ đối ứng; 'người mua nhà' là đối ứng của buyer's "
                    "market",
        },
    },
}

# Sửa trạng thái tie VI theo phân tích tay (added tự sinh trong câu đã dịch)
TT_FIXES = {
    'P16': {
        'P16-VI-022': {
            'outcome': 'added', 'added_kind': 'added_real',
            'note': "quy chiếu TỰ SINH trong câu đã dịch: 'thuộc hiệp hội "
                    "này' — EN S011 không nhắc hiệp hội nào (phân tích P16 "
                    "§8: nguy cơ gán nhầm hội của Suladda)",
        },
    },
}

SENT_ID_RE = re.compile(r'S\d{3}[:\s]*')
WORD_RE = re.compile(r'[A-Za-zÀ-ỹ]{3,}')


def ante_tokens(s):
    """token hóa chuỗi tiền trạm để so tham chiếu chung."""
    if not s:
        return set()
    s = SENT_ID_RE.sub(' ', s)
    return {w.lower() for w in WORD_RE.findall(s)}


def norm_text(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFC', s)
    return re.sub(r'\s+', ' ', s.lower().strip())


ARROW_RE = re.compile(r'^\s*([^→\n]{1,60}?)\s*(?:->|→)\s*([^\n]{1,80}?)\s*(?:[,;(.]|$)')


def build_phrase_table(old_rows):
    """Bảng cụm đối dịch EN->VI trích từ note cũ dạng 'X -> Y ...'."""
    table = {}
    for r in old_rows:
        note = r.get('note')
        if not note:
            continue
        m = ARROW_RE.match(note)
        if m:
            en, vi = norm_text(m.group(1)), norm_text(m.group(2))
            if en and vi:
                table.setdefault(en, set()).add(vi)
    return table


SENT_REF_RE = re.compile(r'EN\s*(S\d{3})')


REALIZED_KW = ('merged', 'covers', 'rendered as', 'renders', 'reformulat',
               'absorbed', 'instead', 'no demonstrative', 'as a full',
               'uses', 'reworded', 'paraphras', 're-express', 'full question',
               'unmarked', 'first mention', 'no prior')
DROP_KW = ('drop', 'unrendered', 'not rendered', 'lost', 'omit', 'no longer')


def classify_omitted_note(note, own_sent, cut_set):
    """Phân loại note omitted cũ: false_flag | realized | drop | unknown."""
    if not note:
        return 'unknown', None
    # note nhắc câu EN khác (thường là khối cắt) -> cờ gắn nhầm tie (bẫy 10)
    mentioned = SENT_REF_RE.findall(note)
    if mentioned and own_sent not in mentioned:
        if any(s in cut_set for s in mentioned):
            return 'false_flag', note
    low = note.lower()
    if any(k in low for k in REALIZED_KW):
        return 'realized', note
    if any(k in low for k in DROP_KW):
        return 'drop', note
    return 'unknown', note


def load_pair(pid):
    d = os.path.join(BASE, 'out', 'pairs', pid)
    st_ties = json.load(open(os.path.join(d, 'ST_ties.json')))['ties']
    tt_ties = json.load(open(os.path.join(d, 'TT_ties.json')))['ties']
    old = json.load(open(os.path.join(d, 'align.json')))['alignments']
    smap = json.load(open(os.path.join(OUT, f'{pid}_sent_map.json')))
    return st_ties, tt_ties, old, smap


def rebuild(pid, verbose=False):
    st_ties, tt_ties, old_rows, smap = load_pair(pid)
    en2vi = smap['en2vi']
    cut_set = set(smap['cut_en'])
    sg_set = set(smap['selfgen_vi'])
    dup_map = smap.get('dup_vi', {})

    tt_by_id = {t['id']: t for t in tt_ties}
    st_by_id = {t['id']: t for t in st_ties}
    old_by_st = {}
    for r in old_rows:
        if r.get('st_tie'):
            old_by_st.setdefault(r['st_tie'], []).append(r)
    phrases = build_phrase_table(old_rows)

    # hạng vị trí của tie trong nhóm cùng loại cùng câu (để ghép cặp câu)
    st_rank = {}
    for t in st_ties:
        k = (t['sent'], t['cat'])
        st_rank[t['id']] = sum(1 for x in st_ties
                               if (x['sent'], x['cat']) == k
                               and x['id'] < t['id'])
    tt_rank = {}
    for u in tt_ties:
        k = (u['sent'], u['cat'])
        tt_rank[u['id']] = sum(1 for x in tt_ties
                               if (x['sent'], x['cat']) == k
                               and x['id'] < u['id'])

    # ứng viên theo câu: st sent -> list tt tie
    cands_cache = {}

    def candidates(sent):
        if sent not in cands_cache:
            vis = en2vi.get(sent, [])
            cands_cache[sent] = [t for t in tt_ties if t['sent'] in vis]
        return cands_cache[sent]

    taken_tt = set()   # tt id đã bị chiếm bởi tìm đối tác (link cũ được giữ)
    rows = []
    suspicious = []

    for t in st_ties:
        sent = t['sent']
        rid = t['id']
        if sent in cut_set:
            note = smap.get('cut_notes', {}).get(
                sent, 'câu EN không có bản dịch (khối cắt)')
            rows.append({
                'st_tie': rid, 'tt_tie': None, 'outcome': 'omitted',
                'om_kind': 'cut', 'shift': None,
                'note': note + f' — {t["text"]}' if t['text'] else note,
            })
            continue

        cands = candidates(sent)
        cand_ids = {c['id'] for c in cands}
        olds = old_by_st.get(rid, [])
        linked = None
        ntt_t = norm_text(t['text'])
        t_ante = ante_tokens(t.get('ante'))

        def trusted(u):
            """link chéo loại chỉ tin khi có bằng chứng tham chiếu."""
            if u['cat'] == t['cat']:
                return True
            if t_ante & ante_tokens(u.get('ante')):
                return True
            nu = norm_text(u['text'])
            if nu and any(nu in vs for vs in phrases.get(ntt_t, ())):
                return True
            return False

        # (a) link cũ hợp bản đồ câu VÀ hợp loại/tham chiếu (chống zip)
        for r in olds:
            if r.get('outcome') not in ('kept', 'shifted'):
                continue
            ttid = r.get('tt_tie')
            if ttid in cand_ids and trusted(tt_by_id[ttid]):
                linked = (tt_by_id[ttid], r)
                break
        # (b) note omitted cũ = BẰNG CHỨNG item không/khác render —
        #     phân loại TRƯỚC khi tìm đối tác (tránh relink nhầm)
        om_old = [r for r in olds if r.get('outcome') == 'omitted']
        if linked is None and om_old:
            om_kind_cls, om_note = classify_omitted_note(
                om_old[0].get('note'), sent, cut_set)
            if om_kind_cls == 'realized':
                rows.append({
                    'st_tie': rid, 'tt_tie': None,
                    'outcome': 'kept_unmarked', 'shift': None,
                    'note': f'hiện thực hóa khác/gộp marker: {om_note}',
                })
                continue
            if om_kind_cls in ('drop', 'unknown'):
                rows.append({
                    'st_tie': rid, 'tt_tie': None, 'outcome': 'omitted',
                    'om_kind': 'drop', 'shift': None,
                    'note': om_note or 'item không được render trong câu đã dịch',
                })
                continue
            # false_flag: cờ gắn nhầm — cứ tiếp tục tìm đối tác

        # (c) tìm đối tác trong cặp câu: loại + loại phụ + trùng tiền trạm
        #     + hạng vị trí + bảng cụm đối dịch trích từ note cũ
        if linked is None:
            best, best_sc = None, 0.0
            for c in cands:
                if c['id'] in taken_tt:
                    continue
                sc = 0.0
                if c['cat'] == t['cat']:
                    sc += 2.0
                    if c.get('sub') == t.get('sub'):
                        sc += 1.0
                shared = ante_tokens(t.get('ante')) & ante_tokens(c.get('ante'))
                sc += min(1.5 * len(shared), 4.5)
                if c['cat'] == t['cat'] and st_rank[t['id']] == tt_rank[c['id']]:
                    sc += 1.5
                ntt = norm_text(c['text'])
                if ntt:
                    for vi_side in phrases.get(norm_text(t['text']), ()):
                        if ntt in vi_side:
                            sc += 2.5
                            break
                if sc > best_sc:
                    best, best_sc = c, sc
            if best is not None and best_sc >= 4.0 and trusted(best):
                linked = (best, None)
                taken_tt.add(best['id'])

        if linked is not None:
            u, oldr = linked
            if u['cat'] != t['cat']:
                outcome = 'shifted'
                shift = f"{t['cat']}>{u['cat']}"
            else:
                outcome = 'kept'
                shift = oldr.get('shift') if oldr else None
                if shift:
                    outcome = 'shifted'
            note = oldr.get('note') if oldr else None
            if not note:
                note = f"{t['text']} → {u['text']} (relink theo bản đồ câu)"
            # dấu hiệu zip: khác loại + không trùng token tiền trạm
            if u['cat'] != t['cat'] and not (
                    ante_tokens(t.get('ante')) & ante_tokens(u.get('ante'))):
                suspicious.append((rid, u['id'], t['text'], u['text']))
            rows.append({
                'st_tie': rid, 'tt_tie': u['id'], 'outcome': outcome,
                'shift': shift, 'note': note,
            })
            continue

        # (d) không đối tác và không bằng chứng omitted cũ
        if linked is None:
            rows.append({
                'st_tie': rid, 'tt_tie': None, 'outcome': 'kept_unmarked',
                'shift': None,
                'note': 'câu VI có dịch; không có tie VI đối ứng '
                        '(hiện thực hóa bằng cụm không đánh dấu / hấp thụ)',
            })
            continue

    # (6) áp sửa link tay
    for rid, fix in LINK_FIXES.get(pid, {}).items():
        for i, r in enumerate(rows):
            if r.get('st_tie') == rid:
                old_tt = r.get('tt_tie')
                rows[i] = dict(fix)
                rows[i]['st_tie'] = rid
                if old_tt and not rows[i].get('tt_tie'):
                    # giải phóng đối tác nếu bị chiếm bởi tìm đối tác
                    taken_tt.discard(old_tt)
                break
    # (5) added
    linked_tt = {r['tt_tie'] for r in rows if r['tt_tie']}
    for u in tt_ties:
        if u['id'] in linked_tt:
            continue
        if u['sent'] in sg_set:
            kind, note = 'added_real', 'câu VI tự sinh (lede/byline/paraphrase)'
        elif u['sent'] in dup_map:
            kind = 'added_real'
            note = dup_map[u['sent']]
        else:
            kind = 'added_inventory'
            note = ('bất đối xứng kiểm kê: đối ứng EN tồn tại nhưng không '
                    'được đánh dấu (first-mention / quy ước từng ngôn ngữ)')
        rows.append({
            'st_tie': None, 'tt_tie': u['id'], 'outcome': 'added',
            'added_kind': kind, 'shift': None, 'note': note,
        })

    # (5b) sửa trạng thái tie VI theo phân tích tay
    for ttid, fix in TT_FIXES.get(pid, {}).items():
        for i, r in enumerate(rows):
            if r.get('tt_tie') == ttid and r.get('outcome') == 'added':
                rows[i] = {'st_tie': None, 'tt_tie': ttid, 'shift': None}
                rows[i].update(fix)
                break

    n_st, n_tt = len(st_ties), len(tt_ties)
    cnt = {}
    for r in rows:
        cnt[r['outcome']] = cnt.get(r['outcome'], 0) + 1
    errs = []
    if sum(cnt.get(k, 0) for k in
           ('kept', 'shifted', 'kept_unmarked', 'omitted')) != n_st:
        errs.append('tổng outcome ST ≠ số ST tie')
    if cnt.get('added', 0) + len(linked_tt) != n_tt:
        errs.append('added + linked ≠ số TT tie')
    for r in rows:
        if r['outcome'] == 'omitted' and r.get('om_kind') == 'cut':
            if st_by_id[r['st_tie']]['sent'] not in cut_set:
                errs.append(f"om-cut sai câu: {r['st_tie']}")
        if r['outcome'] == 'omitted' and r.get('om_kind') == 'drop':
            if st_by_id[r['st_tie']]['sent'] in cut_set:
                errs.append(f"om-drop nằm trong câu bỏ: {r['st_tie']}")
        if r['st_tie'] and r['tt_tie']:
            s = st_by_id[r['st_tie']]['sent']
            v = tt_by_id[r['tt_tie']]['sent']
            if v not in en2vi.get(s, []):
                errs.append(f'link ngoài bản đồ câu: {r["st_tie"]}->{r["tt_tie"]}')

    out = {
        'pair': pid,
        'protocol': 'v2 — semantic align per sent_map (gate 13)',
        'counts': {
            'st_ties': n_st, 'tt_ties': n_tt,
            'kept': cnt.get('kept', 0),
            'shifted': cnt.get('shifted', 0),
            'kept_unmarked': cnt.get('kept_unmarked', 0),
            'omitted_cut': sum(1 for r in rows if r.get('om_kind') == 'cut'),
            'omitted_drop': sum(1 for r in rows if r.get('om_kind') == 'drop'),
            'added_real': sum(1 for r in rows
                              if r.get('added_kind') == 'added_real'),
            'added_inventory': sum(1 for r in rows
                                   if r.get('added_kind') == 'added_inventory'),
        },
        'alignments': rows,
        'suspicious_links': [
            {'st': a, 'tt': b, 'st_text': c, 'tt_text': d}
            for a, b, c, d in suspicious],
        'gate13_errors': errs,
        'caveat': smap.get('caveat'),
    }
    with open(os.path.join(OUT, f'{pid}_align_v2.json'), 'w',
              encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

    c = out['counts']
    om = c['omitted_cut'] + c['omitted_drop']
    print(f"{pid}: ST={n_st} TT={n_tt} | kept={c['kept']} shifted="
          f"{c['shifted']} keptUnm={c['kept_unmarked']} omitted={om} "
          f"(cut={c['omitted_cut']} drop={c['omitted_drop']}) | added="
          f"{c['added_real']}real+{c['added_inventory']}inv | "
          f"susp={len(suspicious)} errs={len(errs)}")
    if errs:
        for e in errs[:5]:
            print('   !', e)
    return out


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for n in range(1, 21):
        pid = f'P{n:02d}'
        if only and pid not in only:
            continue
        rebuild(pid)


if __name__ == '__main__':
    main()
