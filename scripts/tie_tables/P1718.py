# P17/P18 tie tables (P19/P20 follow in P1920.py).

# ---- P17 ----
P17_ST = [
 # S002
 ('S002', 'Prices', 'L', 'repetition', 'S001: falling prices (crisis)', 'high', None, None, 1),
 # S003
 ('S003', 'rubber farmers', 'L', 'repetition', 'S001: falling below production costs (farmers implied)', 'med', None, None, 1),
 ('S003', 'supply', 'L', 'repetition', 'S002: Prices ... production costs', 'low', None, 'supply-demand chain; weak', 1),
 # S004
 ('S004', 'prices', 'L', 'repetition', 'S002: Prices', 'high', None, None, 1),
 ('S004', 'cost of production', 'L', 'repetition', 'S002: production costs', 'high', None, 'reordered', 1),
 ('S004', 'rubber', 'L', 'repetition', 'S001: rubber imports', 'high', None, None, 1),
 # S005
 ('S005', 'Yium', 'L', 'repetition', 'S004: Yium (Tavarolit)', 'high', None, None, 1),
 ('S005', 'that', 'R', 'demonstrative', 'S004: too-low prices', 'high', None, None, 1),
 ('S005', 'rubber farmers', 'L', 'repetition', 'S003: rubber farmers', 'high', None, None, 1),
 # S006
 ('S006', 'They', 'R', 'personal', 'S005: rubber farmers', 'high', None, None, 1),
 ('S006', 'other agricultural activities', 'L', 'repetition', 'S003: rubber farming', 'med', None, None, 1),
 # S007
 ('S007', 'he', 'R', 'personal', 'S005: Yium', 'high', None, None, 1),
 ('S007', 'rubber trees', 'L', 'repetition', 'S005: tapping knives (rubber)', 'med', None, None, 1),
 # S008
 ('S008', 'The consortium', 'L', 'repetition', 'S004: Yium Tavarolit (consortium head)', 'med', None, None, 1),
 ('S008', 'prices', 'L', 'repetition', 'S004: prices', 'high', None, None, 1),
 ('S008', 'supply', 'L', 'repetition', 'S003: supply', 'med', None, None, 1),
 # S009
 ('S009', 'But', 'C', 'adversative', 'S008: speculators skewing prices', 'high', None, None, 1),
 ('S009', 'traders', 'L', 'repetition', 'S008: speculators', 'med', None, None, 1),
 # S010
 ('S010', 'Thailand', 'L', 'repetition', 'S003: Thailand', 'high', None, None, 1),
 ('S010', 'purchasing rubber', 'L', 'repetition', 'S007: rubber trees (rubber chain)', 'med', None, None, 1),
 # S011
 ('S011', 'Tokyo', 'L', 'repetition', 'S009: Tokyo broker', 'high', None, None, 1),
 # S012
 ('S012', 'he', 'R', 'personal', 'S011: a key industry broker', 'high', None, None, 1),
 ('S012', 'rubber trees', 'L', 'repetition', 'S007: rubber trees', 'high', None, None, 1),
 ('S012', 'the supply', 'L', 'repetition', 'S008: supply', 'high', None, None, 1),
 # S013
 ('S013', 'rubber', 'L', 'repetition', 'S012: rubber trees', 'high', None, 'producing rubber', 1),
 ('S013', 'the government', 'L', 'repetition', 'S012: the Thai government', 'high', None, None, 1),
 ('S013', 'the global market', 'L', 'repetition', 'S010: programs (market chain)', 'med', None, None, 1),
 # S014
 ('S014', 'The global supply surplus', 'L', 'repetition', 'S012: control the supply', 'high', None, None, 1),
 # S015
 ('S015', 'But', 'C', 'adversative', 'S014: supply surplus', 'high', None, None, 1),
 ('S015', 'the International Rubber Consortium', 'L', 'repetition', 'S008: The consortium', 'high', None, None, 1),
 ('S015', 'Thailand', 'L', 'repetition', 'S010: Thailand', 'high', None, None, 1),
 ('S015', 'governments', 'L', 'repetition', 'S012: the Thai government', 'high', None, None, 1),
 ('S015', 'rubber', 'L', 'repetition', 'S013: rubber', 'med', None, 'rubber producers', 1),
 # S016
 ('S016', 'he', 'R', 'personal', 'S015: the CEO', 'high', None, None, 1),
 ('S016', 'said', 'L', 'repetition', 'S012: tells VOA', 'low', None, 'weak reporting verb', 1),
 # S017
 ('S017', 'sustainable measures', 'L', 'repetition', 'S016: Immediate assistance', 'med', None, None, 1),
 ('S017', 'farmers', 'L', 'repetition', 'S005: rubber farmers', 'high', None, None, 1),
 # S018
 ('S018', 'But', 'C', 'adversative', 'S017: longer-term measures', 'high', None, None, 1),
 ('S018', 'the Thai government', 'L', 'repetition', 'S013: the government', 'high', None, None, 1),
 ('S018', 'measures', 'L', 'repetition', 'S017: sustainable measures', 'high', None, None, 1),
 ('S018', 'rubber farmers', 'L', 'repetition', 'S017: farmers', 'high', None, None, 1),
 # S019
 ('S019', 'Japan', 'L', 'repetition', 'S011: Tokyo', 'high', None, None, 1),
 ('S019', 'rubber', 'L', 'repetition', 'S015: rubber', 'high', None, None, 1),
 # S020
 ('S020', "The Thai government's support", 'L', 'repetition', 'S010: Thailand is funding', 'high', None, None, 1),
 ('S020', 'prices', 'L', 'repetition', 'S008: prices', 'high', None, None, 1),
 # S021
 ('S021', 'China', 'L', 'repetition', 'S001: imports by China', 'high', None, None, 1),
 ('S021', 'imports', 'L', 'repetition', 'S001: rubber imports', 'high', None, None, 1),
 ('S021', 'Thailand', 'L', 'repetition', 'S015: Thailand', 'high', None, None, 1),
 # S022
 ('S022', 'reduced output', 'L', 'repetition', 'S014: supply surplus', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_17 (§2) ----
 ('S007', None, 'E', 'nominal', 'S007: {farmers} (trong câu)', 'high', None, '[TC] lượng từ + ∅ danh: “Some ∅ are cutting down…”', 1, 'Some ', '{farmers}', 'TC'),
 ('S013', None, 'E', 'clausal', 'S013: {if they don’t cut down / control} (trong câu)', 'high', None, '[TC] “Otherwise ∅ they will keep on producing…” — lược mệnh đề điều kiện', 1, 'Otherwise ', '{if they don’t cut down / control}', 'TC'),
 ('S017', None, 'E', 'nominal', 'S017: {farmers} (trong câu)', 'low', None, '[TC] biên: control “assist farmers ∅ to be more sustainable”', 1, 'to assist farmers ', '{farmers}', 'TC'),
 ('S022', None, 'E', 'clausal', 'S022: {which is still leaving / the situation} (trong câu)', 'low', None, '[TC] biên: vế rút không chủ ngữ “∅ though still leaving a modest surplus”', 1, 'the global appetite for rubber will increase, ', '{which is still leaving / the situation}', 'TC'),

]
P17_TT = [
 # S002
 ('S002', 'Giá', 'L', 'repetition', 'S001: khủng hoảng giá cả', 'high', None, None, 1),
 # S003
 ('S003', 'nông gia trồng cao su', 'L', 'repetition', 'S001: khủng hoảng giá cả (farmers implied)', 'med', None, None, 1),
 ('S003', 'thị trường', 'L', 'repetition', 'S001: thị trường hàng năm', 'high', None, None, 1),
 # S004
 ('S004', 'giá quá thấp', 'L', 'repetition', 'S002: Giá đã sụt xuống dưới giá thành', 'high', None, None, 1),
 ('S004', 'giá thành', 'L', 'repetition', 'S002: giá thành', 'high', None, None, 1),
 ('S004', 'cao su', 'L', 'repetition', 'S001: lượng nhập cao su', 'high', None, None, 1),
 # S005
 ('S005', 'Ông Yium', 'L', 'repetition', 'S004: Ông Yium Tavarolit', 'high', None, None, 1),
 ('S005', 'điều đó', 'R', 'demonstrative', 'S004: giá quá thấp', 'high', None, None, 1),
 ('S005', 'nhà trồng cao su', 'L', 'repetition', 'S003: nông gia trồng cao su', 'high', None, None, 1),
 # S006
 ('S006', 'Ông Yium', 'L', 'repetition', 'S005: Ông Yium', 'high', None, None, 1),
 ('S006', 'Họ', 'R', 'personal', 'S005: nhà trồng cao su', 'high', None, None, 1),
 ('S006', 'hoạt động nông nghiệp', 'L', 'repetition', 'S003: trồng cao su (farming)', 'med', None, None, 1),
 # S007
 ('S007', 'cây cao su', 'L', 'repetition', 'S005: cạo mủ (rubber chain)', 'med', None, None, 1),
 # S008
 ('S008', 'Tổ hợp', 'L', 'repetition', 'S004: Tổ hợp Cao su Quốc tế', 'high', None, None, 1),
 ('S008', 'giá', 'L', 'repetition', 'S004: giá quá thấp', 'high', None, None, 1),
 ('S008', 'cung', 'L', 'repetition', 'S003: thị trường (supply chain)', 'med', None, None, 1),
 # S009
 ('S009', 'Nhưng', 'C', 'adversative', 'S008: ém giá', 'high', None, None, 1),
 ('S009', 'các nhà buôn', 'L', 'repetition', 'S008: những người đầu cơ', 'med', None, None, 1),
 # S010
 ('S010', 'Thái Lan', 'L', 'repetition', 'S003: Thái Lan', 'high', None, None, 1),
 ('S010', 'mua cao su', 'L', 'repetition', 'S007: cây cao su (rubber chain)', 'med', None, None, 1),
 # S011
 # S012
 ('S012', 'Nhân vật này', 'L', 'general word', 'S011: Một nhà trung gian', 'high', None, None, 1),
 ('S012', 'cây cao su', 'L', 'repetition', 'S007: cây cao su', 'high', None, None, 1),
 ('S012', 'mức cung', 'L', 'repetition', 'S008: cung', 'high', None, None, 1),
 ('S012', 'chính phủ Thái', 'L', 'repetition', 'S010: Thái Lan (government implied)', 'med', None, None, 1),
 # S013
 ('S013', 'cao su', 'L', 'repetition', 'S012: cây cao su', 'high', None, 'sản xuất cao su', 1),
 ('S013', 'chính phủ', 'L', 'repetition', 'S012: chính phủ Thái', 'high', None, None, 1),
 ('S013', 'thị trường toàn cầu', 'L', 'repetition', 'S010: các chương trình (market chain)', 'med', None, None, 1),
 # S014
 ('S014', 'Mức cung', 'L', 'repetition', 'S012: mức cung', 'high', None, None, 1),
 # S015
 ('S015', 'Nhưng', 'C', 'adversative', 'S014: cung thặng dư', 'high', None, None, 1),
 ('S015', 'Tổ hợp Cao su Quốc tế', 'L', 'repetition', 'S008: Tổ hợp', 'high', None, None, 1),
 ('S015', 'Thái Lan', 'L', 'repetition', 'S010: Thái Lan', 'high', None, None, 1),
 ('S015', 'các chính phủ khác', 'L', 'repetition', 'S012: chính phủ Thái', 'high', None, None, 1),
 # S016
 ('S016', 'Ông Yium', 'L', 'repetition', 'S015: (CEO = Yium)', 'high', None, None, 1),
 # S017
 ('S017', 'biện pháp', 'L', 'repetition', 'S016: Hỗ trợ cấp thời', 'med', None, None, 1),
 ('S017', 'nông gia', 'L', 'repetition', 'S003: nông gia', 'high', None, None, 1),
 # S018
 ('S018', 'Nhưng', 'C', 'adversative', 'S017: dài hạn', 'high', None, None, 1),
 ('S018', 'chính phủ Thái', 'L', 'repetition', 'S012: chính phủ Thái', 'high', None, None, 1),
 ('S018', 'biện pháp', 'L', 'repetition', 'S017: biện pháp', 'high', None, None, 1),
 ('S018', 'nông gia', 'L', 'repetition', 'S017: nông gia', 'high', None, None, 1),
 # S019
 ('S019', 'Nhật Bản', 'L', 'repetition', 'S011: Tokyo', 'high', None, None, 1),
 # S020
 ('S020', 'chính phủ Thái', 'L', 'repetition', 'S018: chính phủ Thái', 'high', None, None, 1),
 ('S020', 'giá', 'L', 'repetition', 'S019: giá cao su', 'high', None, 'đẩy giá lên', 1),
 # S021
 ('S021', 'Trung Quốc', 'L', 'repetition', 'S001: Trung Quốc', 'high', None, None, 1),
 ('S021', 'lượng nhập', 'L', 'repetition', 'S001: lượng nhập cao su', 'high', None, None, 1),
 ('S021', 'Thái Lan', 'L', 'repetition', 'S015: Thái Lan', 'high', None, None, 1),
 # S022
 ('S022', 'sản lượng giảm sút', 'L', 'repetition', 'S014: cung thặng dư', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_17 (§2) ----
 ('S007', None, 'E', 'nominal', 'S007: {nông dân} (trong câu)', 'high', None, '[TC] “Một số ∅ chặt tất cả các cây cao su” — đối ứng 1–1 E-EN1', 1, 'Một số ', '{nông dân}', 'TC'),
 ('S009', None, 'E', 'clausal', 'S009: {rằng} (trong câu)', 'med', None, '[TC] lược liên từ bổ ngữ “nói ∅ các nhà buôn…”', 1, 'hôm thứ Hai nói ', '{rằng}', 'TC'),
 ('S011', None, 'E', 'clausal', 'S011: {rằng} (trong câu)', 'med', None, '[TC] lược “rằng” trong “nói ∅ một hành động can thiệp…” (VI 12 lại giữ “rằng”)', 1, 'chính phủ Thái, ', '{rằng}', 'TC'),
 ('S013', None, 'E', 'clausal', 'S013: {nếu không chặt / kiểm soát} (trong câu)', 'high', None, '[TC] “Nếu không thì ∅ họ sẽ tiếp tục…” — song song 1–1 E-EN2', 1, 'Nếu không thì ', '{nếu không chặt / kiểm soát}', 'TC'),
 ('S020', None, 'E', 'nominal', 'S020: {sự hỗ trợ} (trong câu)', 'low', None, '[TC] biên: control “giúp ∅ tạm thời đẩy giá lên”', 1, 'của chính phủ Thái giúp ', '{sự hỗ trợ}', 'TC'),
 ('S021', None, 'E', 'nominal', 'S021: {Trung Quốc} (trong câu)', 'high', None, '[TC] control: “Trung Quốc thông báo ∅ sẽ tăng gấp đôi…” — hút đại từ “it” của EN 21', 1, 'Trung Quốc thông báo ', '{Trung Quốc}', 'TC'),
 ('S022', None, 'E', 'clausal', 'S022: {which is still leaving / the situation} (trong câu)', 'low', None, '[TC] biên: vế không chủ ngữ “∅ tuy vẫn còn một mức thặng dư nhỏ”', 1, 'nhu cầu nội địa của Thái Lan sẽ giúp hạ giảm kho dự trữ vào năm tới khi các dự báo gợi ý rằng nhu cần về cao su sẽ gia tăng ', '{which is still leaving / the situation}', 'TC'),

]

# ---- P18 ----
P18_ST = [
 # S002
 ('S002', 'UNICEF', 'L', 'repetition', 'S001: The United Nations Childrens\u2019 Fund', 'high', None, 'abbreviation', 1),
 ('S002', 'Myanmar', 'L', 'repetition', 'S001: several states of Myanmar', 'high', None, None, 1),
 ('S002', 'the U.N. organization\u2019s', 'L', 'repetition', 'S001: The United Nations', 'high', None, None, 1),
 # S003
 ('S003', 'the group', 'L', 'general word', 'S002: the U.N. organization', 'high', None, None, 1),
 # S004
 ('S004', 'Myanmar', 'L', 'repetition', 'S002: Myanmar', 'high', None, None, 1),
 ('S004', 'children', 'L', 'repetition', 'S001: a quarter of a million children', 'high', None, None, 1),
 # S005
 ('S005', 'UNICEF', 'L', 'repetition', 'S002: UNICEF', 'high', None, None, 1),
 ('S005', 'placed', 'L', 'repetition', 'S004: (need implied)', 'low', None, 'weak', 1),
 # S006
 ('S006', 'Rakhine', 'L', 'repetition', 'S005: Rakhine states', 'high', None, None, 1),
 ('S006', 'inter-communal violence', 'L', 'repetition', 'S005: protracted emergencies', 'med', None, None, 1),
 # S007
 ('S007', 'the area', 'L', 'general word', 'S006: Rakhine', 'high', None, None, 1),
 ('S007', 'aid organizations', 'L', 'repetition', 'S002: the U.N. organization\u2019s', 'med', None, None, 1),
 # S008
 ('S008', 'We', 'R', 'personal', 'S007: aid organizations (UNICEF)', 'med', None, None, 1),
 ('S008', 'the communities', 'L', 'repetition', 'S006: inter-communal', 'med', None, None, 1),
 ('S008', 'challenges', 'L', 'repetition', 'S007: posed a challenge', 'high', None, None, 1),
 ('S008', 'access', 'L', 'repetition', 'S007: Getting access', 'high', None, None, 1),
 # S009
 ('S009', 'We', 'R', 'personal', 'S008: We', 'high', None, None, 1),
 ('S009', 'we', 'R', 'personal', 'S008: We', 'high', None, None, 1),
 ('S009', 'life-saving support', 'L', 'repetition', 'S008: (support implied)', 'low', None, 'weak', 1),
 # S010
 ('S010', 'We', 'R', 'personal', 'S009: We', 'high', None, None, 1),
 ('S010', 'van Heese', 'L', 'repetition', 'S008: (speaker implied)', 'low', None, 'first attribution; weak', 1),
 # S011
 ('S011', 'Carmen van Heese', 'L', 'repetition', 'S010: van Heese', 'high', None, None, 1),
 ('S011', "UNICEF's", 'L', 'repetition', 'S005: UNICEF', 'high', None, None, 1),
 ('S011', 'the group', 'L', 'general word', 'S003: the group', 'high', None, None, 1),
 # S012
 ('S012', 'Van Heese', 'L', 'repetition', 'S011: Van Heese', 'high', None, None, 1),
 ('S012', 'North Korea', 'L', 'repetition', 'S003: North Korea', 'high', None, None, 1),
 # S013
 ('S013', 'DPRK (North Korea)', 'L', 'repetition', 'S012: North Korea', 'high', None, None, 1),
 # S014
 ('S014', 'you', 'R', 'personal', 'S013: we (UNICEF, quoted)', 'med', None, None, 1),
 ('S014', 'we', 'R', 'personal', 'S013: we', 'high', None, None, 1),
 ('S014', 'life-savin', 'L', 'repetition', 'S009: life-saving support', 'high', None, None, 1),
 # S015
 ('S015', 'we', 'R', 'personal', 'S014: we', 'high', None, None, 1),
 ('S015', 'agencies', 'L', 'repetition', 'S007: aid organizations', 'high', None, None, 1),
 # S016
 ('S016', 'So', 'C', 'causal', 'S015: other agencies doing the same', 'med', None, None, 1),
 ('S016', 'we', 'R', 'personal', 'S015: we', 'high', None, None, 1),
 ('S016', 'this', 'R', 'demonstrative', 'S015: the same thing', 'high', None, None, 1),
 ('S016', 'van Heese', 'L', 'repetition', 'S012: Van Heese', 'high', None, None, 1),
 # S017
 ('S017', 'UNICEF\u2019s', 'L', 'repetition', 'S011: UNICEF\u2019s', 'high', None, None, 1),
 ('S017', 'life-saving humanitarian assistance', 'L', 'repetition', 'S014: life-savin(g) assistance', 'high', None, None, 1),
 ('S017', 'North Korea', 'L', 'repetition', 'S013: DPRK (North Korea)', 'high', None, None, 1),
 # S018
 ('S018', 'UNICEF', 'L', 'repetition', 'S017: UNICEF\u2019s', 'high', None, None, 1),
 ('S018', 'the Philippines', 'L', 'repetition', 'S003: the Philippines', 'high', None, None, 1),
 # S019
 ('S019', 'The organization', 'L', 'general word', 'S018: UNICEF', 'high', None, None, 1),
 ('S019', 'children', 'L', 'repetition', 'S004: children', 'high', None, None, 1),
 ('S019', 'conflict', 'L', 'repetition', 'S005: protracted emergencies', 'med', None, None, 1),
 ('S019', 'the southern Philippines', 'L', 'repetition', 'S018: the Philippines', 'high', None, None, 1),
 # S020
 ('S020', 'those concerns', 'R', 'demonstrative', 'S018-S019: recovery struggles and conflict', 'high', None, None, 1),
 ('S020', 'UNICEF', 'L', 'repetition', 'S019: The organization', 'high', None, None, 1),
 ('S020', 'the Philippines', 'L', 'repetition', 'S019: the southern Philippines', 'high', None, None, 1),
 # S021
 ('S021', 'This', 'R', 'demonstrative', 'S004-S020: the country appeals', 'high', None, None, 1),
 ('S021', 'a global appeal', 'L', 'repetition', 'S002: (appeal implied)', 'low', None, 'weak', 1),
 ('S021', 'UNICEF', 'L', 'repetition', 'S020: UNICEF', 'high', None, None, 1),
 # S022
 ('S022', 'The organization', 'L', 'general word', 'S021: UNICEF', 'high', None, None, 1),
 ('S022', 'children', 'L', 'repetition', 'S019: children', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_18 (§2–§3) ----
 ('S009', None, 'E', 'clausal', 'S009: {that} (trong câu)', 'med', None, '[TC] lược liên từ bổ ngữ “remind everyone ∅ we are there”', 1, 'remind everyone', '{that}', 'TC'),
 ('S015', 'doing the same thing', 'S', 'verbal', 'S014: the same kind of support work', 'high', None, '[TC] thế vị ngữ do + the same + thing', 1, None, None, 'TC'),
 ('S016', 'do', 'S', 'verbal', 'S015: doing the same thing', 'high', None, '[TC] pro-động từ “do” + chỉ định “this” (this đã là R riêng, không tô trùng)', 1, None, None, 'TC'),
 ('S020', None, 'E', 'clausal', 'S020: {to} (trong câu)', 'high', None, '[TC] tọa hợp to-V: “to prevent…, ∅ allow children…, and to protect…”', 1, 'morbidity and mortality, ', '{to}', 'TC'),

]
P18_TT = [
 # S002
 ('S002', 'UNICEF', 'L', 'repetition', 'S001: (UNICEF)', 'high', None, None, 1),
 ('S002', 'tổ chức này', 'L', 'general word', 'S001: Quĩ Nhi đồng Liên hiệp quốc', 'high', 'R: này', None, 1),
 ('S002', 'Myanmar', 'L', 'repetition', 'S001: Myanmar', 'high', None, None, 1),
 # S004
 ('S004', 'Quỹ Nhi đồng Liên hiệp quốc', 'L', 'repetition', 'S001: Quĩ Nhi đồng Liên hiệp quốc (UNICEF)', 'high', None, None, 1),
 ('S004', 'Myanmar', 'L', 'repetition', 'S002: Myanmar', 'high', None, None, 1),
 # S005
 ('S005', 'Myanmar', 'L', 'repetition', 'S004: Myanmar', 'high', None, 'nơi còn được gọi là Miến Điện', 1),
 ('S005', 'UNICEF', 'L', 'repetition', 'S002: UNICEF', 'high', None, None, 1),
 # S006
 ('S006', 'UNICEF', 'L', 'repetition', 'S005: UNICEF', 'high', None, None, 1),
 ('S006', 'tiểu bang', 'L', 'repetition', 'S001: một số tiểu bang', 'high', None, None, 1),
 # S007
 ('S007', 'Rakhine', 'L', 'repetition', 'S006: Rakhine', 'high', None, None, 1),
 ('S007', 'xung đột', 'L', 'repetition', 'S006: vụ xung đột kéo dài', 'high', None, None, 1),
 # S008
 ('S008', 'Các tổ chức cứu trợ', 'L', 'repetition', 'S002: tổ chức này', 'med', None, None, 1),
 ('S008', 'hoạt động', 'L', 'repetition', 'S005: (working implied)', 'low', None, 'weak', 1),
 # S009
 ('S009', 'UNICEF', 'L', 'repetition', 'S006: UNICEF', 'high', None, None, 1),
 ('S009', 'Philippines', 'L', 'repetition', 'S004: Philippines', 'high', None, None, 1),
 # S010
 ('S010', 'UNICEF', 'L', 'repetition', 'S009: UNICEF', 'high', None, None, 1),
 ('S010', 'Philippines', 'L', 'repetition', 'S009: Philippines', 'high', None, None, 1),
 # S011
 ('S011', 'Bà Carmen van Heese', 'L', 'repetition', 'S008: (speaker implied)', 'low', None, 'first attribution; weak', 1),
 ('S011', 'UNICEF', 'L', 'repetition', 'S009: UNICEF', 'high', None, None, 1),
 # S012
 ('S012', 'Chúng tôi', 'R', 'personal', 'S011: Bà Carmen van Heese (quoted)', 'med', None, None, 1),
 ('S012', 'chúng tôi', 'R', 'personal', 'S011: Bà Carmen van Heese', 'high', None, None, 1),
 ('S012', 'cứu sống', 'L', 'repetition', 'S011: (life-saving implied)', 'low', None, 'weak', 1),
 # S013
 ('S013', 'Chúng tôi', 'R', 'personal', 'S012: Chúng tôi', 'high', None, None, 1),
 # S014
 ('S014', 'Bà van Heese', 'L', 'repetition', 'S011: Bà Carmen van Heese', 'high', None, None, 1),
 ('S014', 'Bắc Triều Tiên', 'L', 'repetition', 'S004: Bắc Triều Tiên', 'high', None, None, 1),
 # S015
 ('S015', 'Bà van Heese', 'L', 'repetition', 'S014: Bà van Heese', 'high', None, None, 1),
 ('S015', 'Bắc Triều Tiên', 'L', 'repetition', 'S014: Bắc Triều Tiên', 'high', None, None, 1),
 # S016
 ('S016', 'chúng tôi', 'R', 'personal', 'S015: (we implied in quote)', 'med', None, None, 1),
 # S017
 ('S017', 'chúng tôi', 'R', 'personal', 'S016: chúng tôi', 'high', None, None, 1),
 # S018
 ('S018', 'Chúng tôi', 'R', 'personal', 'S017: chúng tôi', 'high', None, None, 1),
 # S019
 ('S019', 'Lời kêu gọi quyên góp của UNICEF', 'L', 'repetition', 'S002: lời kêu gọi quyên góp', 'high', None, None, 1),
 ('S019', 'viện trợ nhân đạo', 'L', 'repetition', 'S012: sự trợ giúp', 'med', None, None, 1),
 # S020
 ('S020', 'UNICEF', 'L', 'repetition', 'S019: UNICEF', 'high', None, None, 1),
 ('S020', 'Philippines', 'L', 'repetition', 'S010: Philippines', 'high', None, None, 1),
 # S021
 ('S021', 'Tổ chức này', 'L', 'general word', 'S020: UNICEF', 'high', 'R: này', None, 1),
 ('S021', 'trẻ em', 'L', 'repetition', 'S005: trẻ em', 'high', None, None, 1),
 ('S021', 'xung đột', 'L', 'repetition', 'S007: xung đột', 'high', None, None, 1),
 # S022
 ('S022', 'Những mối quan tâm đó', 'R', 'demonstrative', 'S020-S021: recovery struggles and conflict', 'high', None, None, 1),
 ('S022', 'UNICEF', 'L', 'repetition', 'S021: Tổ chức này', 'high', None, None, 1),
 ('S022', 'Philippines', 'L', 'repetition', 'S020: Philippines', 'high', None, None, 1),
 # S023
 ('S023', 'Những khoản quyên góp', 'L', 'repetition', 'S019: lời kêu gọi quyên góp', 'high', None, None, 1),
 ('S023', 'quyên góp toàn cầu', 'L', 'repetition', 'S002: lời kêu gọi quyên góp lớn nhất', 'high', None, None, 1),
 # S024
 ('S024', 'tổ chức này', 'L', 'general word', 'S022: UNICEF', 'high', 'R: này', None, 1),
 ('S024', 'em bé', 'L', 'repetition', 'S005: trẻ em', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_18 (§2) ----
 ('S016', None, 'E', 'nominal', 'S016: {chính mình} (trong câu)', 'low', None, '[TC] biên: phản thân “đã cam kết ∅ sẽ cung cấp” — EN “commit ourselves”', 1, 'trong tư cách là một tổ chức, đã cam kết', '{chính mình}', 'TC'),

]
