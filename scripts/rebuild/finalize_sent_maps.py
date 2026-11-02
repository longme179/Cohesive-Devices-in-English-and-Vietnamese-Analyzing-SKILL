#!/usr/bin/env python3
"""
Chốt BẢN ĐỒ CÂU cuối cùng = draft (neo số liệu + DP) + HIỆU CHỈNH THỦ CÔNG
từ 20 bản phân tích ngữ nghĩa (download/BDNC/semantic_analysis/Pair_XX/).

Mọi hiệu chỉnh đều truy vết được về một nhận định trong bản phân tích:
- P01: pull-quote dup S031 (§8); split S029→S030+S031, S036→S036+S037;
       merge S046+S047→S046 (đọc trực tiếp); cut={S030,S031,S041,S048,S049}
- P04: merge S008+S009→S006 (khung dẫn Shriane hút vào), S022+S023→S017,
       S025+S026→S019; cut={S001,S005,S011,S018,S027,S030} (lede/AIHW/câu chuyển)
- P08: merge S009+S010→S009; split S016→S015+S016; cut={S021,S022}
- P09: cut={S033,S034,S035} (§9); split S001→S001+S003; lệch +1 từ S005
- P10: cut={S002,S018}; selfgen={S003 (lede trùng), S022 (mở rộng AUD)}
- P17: identity 22↔22 (byline nằm trong VI S002)
- P18: 0 cắt; selfgen={S003 byline}; dup_vi={S009,S010} (Philippines trùng nguồn);
       quote block tái phối S008+S011→S011
- P19: identity lệch +1 sau S003 (selfgen paraphrase)
- P20: cut 4 khối S015-S020/S038-S043/S048-S052/S055-S056 (§1.1);
       selfgen={S001,S002,S003} lede; merge S004+S005→S007; split S024→S020+S021
"""
import json
import os

BASE = '/home/z/my-project'
OUT = os.path.join(BASE, 'out', 'align_v2')

OVERRIDES = {
    'P01': {
        'cut_set': ['S030', 'S031', 'S041', 'S048', 'S049'],
        'selfgen_set': ['S019'],
        'en2vi_patch': {
            'S029': ['S030', 'S031'], 'S036': ['S036', 'S037'],
            'S046': ['S046'], 'S047': ['S046'],
        },
        'cut_notes': {'S031': 'pull-quote trùng nguồn (artifact trích xuất)'},
    },
    'P04': {
        'cut_set': ['S001', 'S005', 'S011', 'S018', 'S027', 'S030'],
        'selfgen_set': [],
        'en2vi_patch': {
            'S008': ['S006'], 'S009': ['S006'], 'S022': ['S017'],
            'S023': ['S017'], 'S025': ['S019'], 'S026': ['S019'],
            'S028': ['S020'],
        },
    },
    'P08': {
        'cut_set': ['S021', 'S022'],
        'selfgen_set': [],
        'en2vi_patch': {
            'S009': ['S009'], 'S010': ['S009'], 'S016': ['S015', 'S016'],
        },
    },
    'P09': {
        'en2vi_full': 'P09',
        'cut_set': ['S033', 'S034', 'S035'],
        'selfgen_set': [],
    },
    'P10': {
        'en2vi_full': 'P10',
        'cut_set': ['S002', 'S018'],
        'selfgen_set': ['S022'],
        'dup_vi': {'S003': 'lede trùng (lặp nội dung S001 — lỗi dồn dòng nguồn)'},
    },
    'P17': {
        'en2vi_full': 'identity',
        'cut_set': [],
        'selfgen_set': [],
    },
    'P18': {
        'en2vi_full': 'P18',
        'cut_set': [],
        'selfgen_set': ['S003'],
        'dup_vi': {
            'S009': 'câu Philippines trùng nguyên văn (lỗi biên tập nguồn VI)',
            'S010': 'câu Philippines trùng nguyên văn (lỗi biên tập nguồn VI)',
        },
    },
    'P19': {
        'en2vi_full': 'P19',
        'cut_set': [],
        'selfgen_set': ['S003'],
    },
    'P20': {
        'en2vi_full': 'P20',
        'cut_set': ['S015', 'S016', 'S017', 'S018', 'S019', 'S020',
                    'S038', 'S039', 'S040', 'S041', 'S042', 'S043',
                    'S048', 'S049', 'S050', 'S051', 'S052',
                    'S055', 'S056'],
        'selfgen_set': ['S001', 'S002', 'S003'],
        'cut_notes': {
            'S015': 'khối A — Trent: brand Korea', 'S016': 'khối A',
            'S017': 'khối A', 'S018': 'khối A', 'S019': 'khối A',
            'S020': 'khối A',
            'S038': 'khối B — Long: chuỗi cung ứng', 'S039': 'khối B',
            'S040': 'khối B', 'S041': 'khối B', 'S042': 'khối B',
            'S043': 'khối B',
            'S048': 'khối C — Ganapathiraju: cạn kiệt', 'S049': 'khối C',
            'S050': 'khối C', 'S051': 'khối C', 'S052': 'khối C',
            'S055': 'khối D — Conniff: 85%', 'S056': 'khối D',
        },
    },
}

# các cặp giữ nguyên draft nhưng kèm cảnh báo (từ phân tích)
CAVEATS = {
    'P02': 'VI tái cấu trúc phần tuyên bố Bộ (dòng 36–39) — bản đồ câu ở vùng này chỉ gần đúng',
    'P03': 'cặp biên tập lại (adaptation) — phân tích khuyến cáo KHÔNG dùng cấp câu',
    'P15': 'có 1 đảo khối (EN S014 → VI S005) — bản đồ đơn điệu chỉ gần đúng vùng này',
}


def build_full(pid, st_ids, vi_ids):
    if pid == 'P09':
        m = {}
        m['S001'] = ['S001', 'S003']
        m['S002'] = ['S002']
        for k in range(3, 33):          # S003..S032 -> S004..S033
            m[f'S{k:03d}'] = [f'S{k + 1:03d}']
        m['S036'] = ['S033']
        return m
    if pid == 'P10':
        m = {}
        m['S001'] = ['S001']
        m['S003'] = ['S002']
        for k in range(4, 18):          # S004..S017 identity
            m[f'S{k:03d}'] = [f'S{k:03d}']
        for k in range(19, 23):         # S019..S022 -> S018..S021
            m[f'S{k:03d}'] = [f'S{k - 1:03d}']
        for k in range(23, 26):         # S023..S025 identity
            m[f'S{k:03d}'] = [f'S{k:03d}']
        return m
    if pid == 'P17':
        return {e: [e] for e in st_ids}
    if pid == 'P18':
        m = {}
        m['S001'] = ['S001']; m['S002'] = ['S002']; m['S003'] = ['S004']
        m['S004'] = ['S005']; m['S005'] = ['S006']; m['S006'] = ['S007']
        m['S007'] = ['S008']; m['S008'] = ['S011']; m['S009'] = ['S012']
        m['S010'] = ['S013']; m['S011'] = ['S011']; m['S012'] = ['S014']
        m['S013'] = ['S015']; m['S014'] = ['S016']; m['S015'] = ['S017']
        m['S016'] = ['S018']; m['S017'] = ['S019']
        m['S018'] = ['S020']            # S009/S010 = bản trùng (dup), S020 bản chính
        m['S019'] = ['S021']; m['S020'] = ['S022']; m['S021'] = ['S023']
        m['S022'] = ['S024']
        return m
    if pid == 'P19':
        m = {'S001': ['S001'], 'S002': ['S002']}
        for k in range(3, 22):          # S003..S021 -> S004..S022
            m[f'S{k:03d}'] = [f'S{k + 1:03d}']
        return m
    if pid == 'P20':
        m = {}
        pairs = [
            ('S001', ['S004']), ('S002', ['S005']), ('S003', ['S006']),
            ('S004', ['S007']), ('S005', ['S007']),            # gộp
            ('S006', ['S008']), ('S007', ['S009']), ('S008', ['S010']),
            ('S009', ['S011']), ('S010', ['S012']), ('S011', ['S013']),
            ('S012', ['S014']), ('S013', ['S015']), ('S014', ['S016']),
            ('S021', ['S017']), ('S022', ['S018']), ('S023', ['S019']),
            ('S024', ['S020', 'S021']),                          # tách
            ('S025', ['S022']), ('S026', ['S023']), ('S027', ['S024']),
            ('S028', ['S025']), ('S029', ['S026']), ('S030', ['S027']),
            ('S031', ['S028']), ('S032', ['S029']),
            ('S033', ['S030']), ('S034', ['S031']), ('S035', ['S032']),
            ('S036', ['S033']), ('S037', ['S034']),
            ('S044', ['S035']), ('S045', ['S036']), ('S046', ['S037']),
            ('S047', ['S038']),
            ('S053', ['S039']), ('S054', ['S040']),
            ('S057', ['S041']), ('S058', ['S042']), ('S059', ['S043']),
            ('S060', ['S044']),
        ]
        for e, v in pairs:
            m[e] = v
        return m
    raise KeyError(pid)


def finalize(pid):
    draft = json.load(open(os.path.join(OUT, f'{pid}_sent_map_draft.json')))
    st_ids = [s['id'] for s in json.load(
        open(f'{BASE}/out/pairs/{pid}/ST_seg.json'))['sentences']]
    vi_ids = [s['id'] for s in json.load(
        open(f'{BASE}/out/pairs/{pid}/TT_seg.json'))['sentences']]
    ov = OVERRIDES.get(pid, {})

    if 'en2vi_full' in ov:
        if ov['en2vi_full'] == 'identity':
            en2vi = {e: [e] for e in st_ids}
        else:
            en2vi = build_full(pid, st_ids, vi_ids)
        # với full override: câu EN không có trong en2vi → cắt
        cut = [e for e in st_ids if e not in en2vi]
    else:
        en2vi = dict(draft['en2vi'])
        cut = list(draft['cut_en'])
        if 'cut_set' in ov:
            cut = list(ov['cut_set'])
        for e, v in ov.get('en2vi_patch', {}).items():
            en2vi[e] = v
            if e in cut:
                cut.remove(e)
        # câu EN nằm trong cut_set thì không được map (loại map còn sót từ draft)
        for e in list(en2vi):
            if e in cut:
                del en2vi[e]

    selfgen = list(ov.get('selfgen_set', draft['selfgen_vi']))
    dup_vi = dict(ov.get('dup_vi', {}))
    if 'en2vi_full' not in ov:
        # loại selfgen còn sót do patch
        for e, v in ov.get('en2vi_patch', {}).items():
            for s in v:
                if s in selfgen:
                    selfgen.remove(s)

    # ---- kiểm tra nhất quán ----
    errs = []
    mapped_en = set(en2vi.keys())
    cut_set = set(cut)
    if mapped_en & cut_set:
        errs.append(f'câu vừa map vừa cut: {sorted(mapped_en & cut_set)}')
    if mapped_en | cut_set != set(st_ids):
        miss = set(st_ids) - mapped_en - cut_set
        errs.append(f'câu EN chưa phân: {sorted(miss)}')
    used_vi = set()
    for v in en2vi.values():
        used_vi.update(v)
    sg_set = set(selfgen)
    dup_set = set(dup_vi)
    if used_vi & sg_set:
        errs.append(f'câu VI vừa map vừa selfgen: {sorted(used_vi & sg_set)}')
    if used_vi & dup_set:
        errs.append(f'câu VI vừa map vừa dup: {sorted(used_vi & dup_set)}')
    if sg_set & dup_set:
        errs.append(f'câu VI vừa sg vừa dup: {sorted(sg_set & dup_set)}')
    if used_vi | sg_set | dup_set != set(vi_ids):
        miss = set(vi_ids) - used_vi - sg_set - dup_set
        extra = used_vi | sg_set | dup_set - set(vi_ids)
        errs.append(f'câu VI chưa phân: {sorted(miss)} / không tồn tại: {sorted(extra)}')
    # đơn điệu (P18: tái phối khung dẫn quote — đảo trật tự CÓ CHỦ Ý, chỉ cảnh báo)
    seq = [(st_ids.index(e), min((vi_ids.index(v) for v in vs), default=-1))
           for e, vs in sorted(en2vi.items(), key=lambda kv: st_ids.index(kv[0]))]
    warns = []
    last = -1
    for a, b in seq:
        if b < last:
            warns.append(f'đảo trật tự tại EN idx {a} (tái phối khung dẫn?)')
            break
        last = b

    out = {
        'pair': pid,
        'en2vi': en2vi,
        'cut_en': cut,
        'selfgen_vi': selfgen,
        'dup_vi': dup_vi,
        'cut_notes': ov.get('cut_notes', {}),
        'caveat': CAVEATS.get(pid),
        'n_en': len(st_ids), 'n_vi': len(vi_ids),
        'source': 'override' if OVERRIDES.get(pid) else 'draft-auto',
        'errors': errs,
        'warnings': warns,
    }
    with open(os.path.join(OUT, f'{pid}_sent_map.json'), 'w',
              encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    status = 'OK' if not errs else 'LỖI: ' + '; '.join(errs)
    if warns:
        status += ' | CẢNH BÁO: ' + '; '.join(warns)
    print(f"{pid}: mapped={len(en2vi)} cut={len(cut)} sg={len(selfgen)} "
          f"dup={len(dup_vi)} [{out['source']}] {status}")


def main():
    for n in range(1, 21):
        finalize(f'P{n:02d}')


if __name__ == '__main__':
    main()
