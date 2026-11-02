#!/usr/bin/env python3
"""Build ST.txt / TT.txt per pair from raw_pairs + pair_config.

pair_config entries (indices refer to raw_pairs/PXX.json paragraph lists):
  exclude: [idx...]            - drop paragraph (title row / subheading / credit)
  strip_prefix: {idx: "text"}  - remove merged subheading / stray fragment prefix
  replace: {idx: "new text"}   - repair source defect (P11 VI leak)
Everything removed is logged with a reason in exclusions_log.json.
"""
import json, os, re

OUT = '/home/z/my-project/out'

CFG = {
 'P01': {
   'EN': {'exclude': {17: 'pull-quote attribution (caption)'},
          'strip_suffix': {27: ' - James Harrington, Sydney Water project manager'}},
   'VI': {},
 },
 'P02': {
   'EN': {'exclude': {0: 'title row', 15: 'subheading', 34: 'subheading'},
          'strip_prefix': {29: "'Absolutely nowhere to go'"},
          'strip_suffix': {7: 'Youth homelessness across Australia'}},
   'VI': {'exclude': {0: 'title row', 16: 'subheading', 35: 'subheading'},
          'strip_prefix': {12: 'Khu vực Latrobe-Gippsland đứng đầu danh sách',
                            13: 'Các khu vực',
                            30: '‘Không còn nơi nào để đi’'},
          'strip_suffix': {8: 'Tình trạng vô gia cư ở thanh niên trên khắp nước Úc',
                            20: 'Youth Foyers – Mô hình hỗ trợ nhà ở chuyển tiếp cho thanh niên'}},
 },
 'P03': {'EN': {}, 'VI': {}},
 'P04': {'EN': {}, 'VI': {}},
 'P05': {
   'EN': {},
   'VI': {'exclude': {0: 'subheading', 5: 'subheading', 19: 'subheading',
                       25: 'subheading', 30: 'subheading', 34: 'subheading'},
          'strip_prefix': {38: 'Thuế đất được gia hạn tại Victoria'}},
 },
 'P06': {'EN': {}, 'VI': {}},
 'P07': {
   'EN': {'exclude': {0: 'title row', 3: 'subheading', 6: 'subheading',
                       29: 'series credit note', 30: 'author bio (byline)'},
          'strip_prefix': {13: 'Embracing and creating Australia’s English stories',
                            22: 'The future of Australian English'}},
   'VI': {'exclude': {0: 'title row', 3: 'subheading', 6: 'subheading',
                       29: 'series credit note', 30: 'author bio (byline)'},
          'strip_prefix': {13: 'Nắm bắt và tạo ra những câu chuyện tiếng Anh của Úc',
                            22: 'Tương lai của tiếng Anh Úc'}},
 },
 'P08': {'EN': {'exclude': {0: 'title row'}}, 'VI': {'exclude': {0: 'title row'}}},
 'P09': {
   'EN': {'exclude': {0: 'title row', 10: 'subheading', 16: 'subheading',
                       24: 'subheading', 27: 'subheading'}},
   'VI': {'exclude': {0: 'title row', 10: 'subheading', 16: 'subheading',
                       24: 'subheading', 27: 'subheading'}},
 },
 'P10': {
   'EN': {'exclude': {0: 'title row', 7: 'subheading', 15: 'subheading'}},
   'VI': {'exclude': {0: 'title row', 6: 'subheading', 15: 'subheading',
                       29: 'subheading', 33: 'subheading'},
          'strip_prefix': {20: 'Một số biện pháp hỗ trợ chi phí sinh hoạt của chính phủ Úc'}},
 },
 'P11': {
   'EN': {'exclude': {0: 'title row', 10: 'subheading', 25: 'subheading',
                       33: 'subheading'},
          'strip_suffix': {13: 'Một số truyền thống phần lớn mang tính biểu'}},
   'VI': {'exclude': {0: 'title row', 9: 'subheading', 22: 'subheading',
                       30: 'subheading'},
          'replace': {12: 'Một số truyền thống phần lớn mang tính biểu tượng.'}},
 },
 'P12': {'EN': {'exclude': {0: 'title row'}}, 'VI': {'exclude': {0: 'title row'}}},
 'P13': {'EN': {}, 'VI': {}},
 'P14': {'EN': {}, 'VI': {}},
 'P15': {'EN': {'exclude': {7: 'footnote marker (1)'}},
          'VI': {'exclude': {10: 'footnote marker (1)'}}},
 'P16': {'EN': {'exclude': {0: 'title row (merged EN+VI title)'}},
          'VI': {'exclude': {0: 'title row (VI title continuation)'}}},
 'P17': {'EN': {'exclude': {0: 'title row', 6: 'subheading', 13: 'subheading'}},
          'VI': {'exclude': {0: 'title row'}}},
 'P18': {'EN': {'exclude': {0: 'title row'}}, 'VI': {'exclude': {0: 'title row'}}},
 'P19': {'EN': {'exclude': {0: 'title row'}}, 'VI': {'exclude': {0: 'title row'}}},
 'P20': {'EN': {'exclude': {0: 'title row', 6: 'subheading', 10: 'subheading',
                            16: 'subheading', 24: 'subheading'}},
          'VI': {'exclude': {0: 'title row'}}},
}

TITLES = {
 'P01': ('Beer made from recycled wastewater? Some want to see it on Australian bottle-o shelves',
         'Bia làm từ nước thải tái chế: Bạn có dám thử?'),
 'P02': ("Australia is in a youth homelessness 'crisis'. These are the most affected areas",
         'Úc đang đối mặt với một "cuộc khủng hoảng" vô gia cư ở giới trẻ'),
 'P03': ("Who are the biggest donors to Australia's political parties?",
         'Từ tỷ phú đến các công ty cá cược: Danh sách những nhà tài trợ lớn nhất cho các đảng chính trị được tiết lộ'),
 'P04': ("'Major flow-on effects': Australia's sleep struggle — and how much you need",
         'Ngủ bao nhiêu tiếng là đủ, và hậu quả của việc thiếu ngủ là gì?'),
 'P05': ("Fast-tracked citizenship to anti-wage theft laws: What's changing in Australia from 1 January",
         'Những thay đổi tại Úc từ ngày 1 tháng 1'),
 'P06': ('Visa rules, airfares and hot trends: How travel is changing in 2025',
         'Những thay đổi về du lịch trong năm 2025'),
 'P07': ('Is Australian English different from English?',
         'Tiếng Anh Úc có khác với tiếng Anh không?'),
 'P08': ('Revealed: Australian suburbs with the biggest home price falls',
         'Những khu vực có giá nhà giảm mạnh nhất tại Úc trong năm 2024'),
 'P09': ("Bulk billing rates across Australia — and where you're most likely to find a fee-free GP",
         'Nơi nào ở Úc có chi phí khám bác sĩ gia đình thấp, được Medicare thanh toán nhiều hơn?'),
 'P10': ("How the falling Aussie dollar could impact you",
         'Đồng đô la Úc giảm giá có thể ảnh hưởng đến túi tiền của bạn'),
 'P11': ('How America hands power from one president to the next',
         'Nước Mỹ trao quyền lực từ tổng thống này sang tổng thống kia ra sao?'),
 'P12': ('RFK Jr. endorses Donald Trump',
         'Ứng cử viên tổng thống độc lập ủng hộ Donald Trump'),
 'P13': ('Seoul working for pope visit to N.Korea, Vatican agency says',
         'Hàn Quốc tìm cách thu xếp cho chuyến thăm của Giáo hoàng'),
 'P14': ("Trump administration launches new 'self-deportation' app",
         'Chính quyền Trump ra mắt ứng dụng ‘tự động trục xuất’'),
 'P15': ('ICE arrests Palestinian activist Mahmoud Khalil',
         'Mỹ bắt giữ nhà hoạt động Palestine ủng hộ biểu tình phản chiến'),
 'P16': ('Tanking Ruble Hits Russian Tourists, Thai Hotels',
         'Đồng rúp tuột giá tác động đến du khách Nga và khách sạn Thái Lan'),
 'P17': ("Southeast Asia's Rubber Farmers Hope for Rebound",
         'Nông gia trồng cao su hy vọng phục hồi trở lại'),
 'P18': ('Myanmar, North Korea and Philippines are Focus of UNICEF 2015 Appeal',
         'UNICEF kêu gọi quyên góp giúp trẻ em Miến Điện, Triều Tiên, Philippines'),
 'P19': ('Trans-Pacific Air Passengers to Divy Up $40M in Price-fixing Settlement',
         'Hành khách sẽ chia tiền thắng kiện vụ ‘lũng đoạn giá vé’ máy bay'),
 'P20': ('EU Rolls Out Trade Bans in Global Crackdown on Illegal Fishing',
         'EU xúc tiến việc cấm buôn bán hải sản đánh bắt bất hợp pháp'),
}

for i in range(1, 21):
    pid = f'P{i:02d}'
    d = json.load(open(f'{OUT}/raw_pairs/{pid}.json'))
    os.makedirs(f'{OUT}/pairs/{pid}', exist_ok=True)
    log = {'pair': pid, 'titles': TITLES[pid],
           'extractor_dropped': d['dropped'], 'manual': []}
    for lang, fname in (('EN', 'ST.txt'), ('VI', 'TT.txt')):
        cfg = CFG[pid][lang]
        paras = list(d['en'] if lang == 'EN' else d['vi'])
        out = []
        for idx, p in enumerate(paras):
            if idx in cfg.get('exclude', {}):
                log['manual'].append({'lang': lang, 'idx': idx, 'action': 'exclude',
                                      'reason': cfg['exclude'][idx], 'text': p[:120]})
                continue
            if idx in cfg.get('strip_prefix', {}):
                pre = cfg['strip_prefix'][idx]
                assert p.startswith(pre), f'{pid} {lang}[{idx}] does not start with {pre!r}: {p[:80]!r}'
                p = p[len(pre):].strip()
                log['manual'].append({'lang': lang, 'idx': idx, 'action': 'strip_prefix',
                                      'reason': 'merged subheading/stray fragment', 'text': pre})
            if idx in cfg.get('strip_suffix', {}):
                suf = cfg['strip_suffix'][idx]
                assert p.endswith(suf), f'{pid} {lang}[{idx}] does not end with {suf!r}: {p[-80:]!r}'
                p = p[:-len(suf)].strip()
                log['manual'].append({'lang': lang, 'idx': idx, 'action': 'strip_suffix',
                                      'reason': 'source defect: VI text inside EN cell',
                                      'text': suf})
            if idx in cfg.get('replace', {}):
                log['manual'].append({'lang': lang, 'idx': idx, 'action': 'replace',
                                      'reason': 'source defect: repair fragmented sentence',
                                      'text': p, 'with': cfg['replace'][idx]})
                p = cfg['replace'][idx]
            out.append(p)
        with open(f'{OUT}/pairs/{pid}/{fname}', 'w') as f:
            f.write('\n'.join(out) + '\n')
        print(f'{pid} {lang}: {len(paras)} -> {len(out)} paras, '
              f'{sum(len(p) for p in out)} chars')
    json.dump(log, open(f'{OUT}/pairs/{pid}/exclusions_log.json', 'w'),
              ensure_ascii=False, indent=1)
print('done')
