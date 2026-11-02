# P07 alignment table. Row: (st_id, tt_id_or_None, outcome, shift, note)
# P07 is nearly sentence-parallel; pairs are listed explicitly.

def _mk():
    pairs = [
        (1, 1), (2, 2), (3, 3), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9),
        (11, 10), (12, 11), (13, 12), (14, 13), (15, 15), (16, 16), (17, 17),
        (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24),
        (25, 25), (27, 26), (28, 27), (29, 28), (31, 29), (32, 30), (33, 31),
        (34, 32), (34, 33), (35, 34), (36, 35), (37, 36), (38, 37), (39, 38),
        (40, 39), (41, 40), (42, 41), (43, 42), (44, 43), (45, 44), (46, 45),
        (47, 46), (48, 47), (49, 48), (50, 49), (51, 50), (52, 51), (53, 52),
        (54, 53), (55, 54), (56, 55), (57, 56), (58, 57), (59, 58), (60, 59),
        (61, 60), (62, 61), (63, 62), (64, 63), (65, 64), (66, 65), (67, 66),
        (68, 67), (69, 68), (71, 70), (72, 71), (74, 73), (75, 74), (76, 75),
        (77, 76), (78, 77), (79, 78), (80, 79), (81, 80), (82, 81), (83, 82),
        (84, 83), (85, 84), (86, 85), (87, 86), (88, 87), (89, 88), (90, 89),
        (92, 90), (93, 91), (94, 92), (95, 93), (96, 94), (97, 95), (98, 96),
        (100, 98), (101, 99), (102, 100), (103, 101), (104, 102), (105, 103),
        (106, 104), (107, 105), (108, 106), (109, 107), (110, 108), (111, 109),
        (112, 110), (113, 111), (114, 112), (115, 113), (116, 114), (117, 115),
        (118, 116), (119, 117), (120, 118), (121, 119),
    ]
    # special cases: (st_num, tt_num, outcome, shift, note)
    specials = {
        4: (None, 'omitted', 'E>zero', 'TT renders the fragment as a full question (Mate là ai?), no ellipsis'),
        5: (None, 'omitted', 'R>zero', 'This is confusing -> Đúng là khó hiểu thật (no demonstrative in TT)'),
        26: (None, 'omitted', 'L>zero', 'merged in TT marking (tiếng Anh Úc covers words + English)'),
        30: (None, 'omitted', 'R>zero', 'TT drops possessive (Cách nói chuyện của người Úc gắn liền với lịch sử)'),
        70: (69, 'shifted', 'R>L', 'it -> từ này (pronoun becomes demonstrative NP)'),
        73: (72, 'shifted', 'R>L', 'it -> từ này (pronoun becomes demonstrative NP)'),
        91: (None, 'omitted', 'R>zero', 'merged in TT marking (Những thành ngữ hài hước này covers These + idioms)'),
        99: (None, 'omitted', 'L>zero', 'merged in TT marking (kiểu cách Anh overlapped, removed)'),
    }
    A = []
    for st_n, tt_n in pairs:
        st_id = f'P07-EN-{st_n:03d}'
        if st_n in specials:
            spec = specials[st_n]
            if spec[0] is None:
                A.append((st_id, None, spec[1], spec[2], spec[3]))
                continue
            A.append((st_id, f'P07-VI-{spec[0]:03d}', spec[1], spec[2], spec[3]))
            continue
        A.append((st_id, f'P07-VI-{tt_n:03d}', 'kept', None, None))
    # specials not covered by the pairs loop -> append their rows directly
    in_pairs = {p[0] for p in pairs}
    for st_n, spec in specials.items():
        if st_n in in_pairs:
            continue
        st_id = f'P07-EN-{st_n:03d}'
        if spec[0] is None:
            A.append((st_id, None, spec[1], spec[2], spec[3]))
        else:
            A.append((st_id, f'P07-VI-{spec[0]:03d}', spec[1], spec[2], spec[3]))
    A.sort(key=lambda r: r[0])
    return A

A = _mk()

ADDED_NOTES = {
 'P07-VI-004': 'TT Đúng affirms the examples; EN This is confusing has no demonstrative counterpart',
 'P07-VI-014': 'TT ngôn ngữ này (general word + demonstrative) where EN its words is unmarked',
 'P07-VI-097': 'TT adds adversative Tuy nhiên for EN And, yet (unmarked in EN)',
}
