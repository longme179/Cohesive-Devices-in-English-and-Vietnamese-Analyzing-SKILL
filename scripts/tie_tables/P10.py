# P10 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'The Australian dollar', 'L', 'repetition', 'S001: a weaker Aussie dollar', 'high', None, 'Aussie -> Australian expansion', 1),
 # S003
 ('S003', 'Its', 'R', 'personal', 'S002: The Australian dollar', 'high', None, None, 1),
 ('S003', 'the United States dollar', 'L', 'collocation', 'S002: The Australian dollar', 'low', None, 'currency association (phép liên tưởng)', 1),
 ('S003', "it's", 'R', 'personal', 'S002: The Australian dollar', 'high', None, None, 1),
 # S004
 ('S004', 'a weaker dollar', 'L', 'repetition', 'S001: a weaker Aussie dollar', 'high', None, None, 1),
 ('S004', 'Australian', 'L', 'repetition', 'S001: the Australian economy', 'high', None, 'Australian exporters', 1),
 # S005
 ('S005', 'the weakening of the Australian dollar', 'L', 'repetition', 'S002-S004: The Australian dollar / weaker dollar', 'high', None, None, 1),
 # S006
 ('S006', "the dollar's value", 'L', 'repetition', 'S003: Its value', 'high', None, None, 1),
 ('S006', 'factors', 'L', 'repetition', 'S005: A number of elements', 'high', None, 'elements ~ factors', 1),
 # S007
 ('S007', 'the US', 'L', 'repetition', 'S003: the United States dollar', 'high', None, 'abbreviation', 1),
 # S008
 ('S008', 'This', 'R', 'demonstrative', 'S007: fewer interest rate cuts in the US', 'high', None, None, 1),
 ('S008', 'the US dollar', 'L', 'repetition', 'S003: the United States dollar', 'high', None, 'abbreviation', 1),
 ('S008', 'the Australian dollar', 'L', 'repetition', 'S005: the Australian dollar', 'high', None, None, 1),
 ('S008', 'he', 'R', 'personal', 'S006: Graeme Hughes', 'high', None, None, 2),
 # S009
 ('S009', 'the Chinese yuan', 'L', 'collocation', 'S008: other currencies', 'low', None, 'currency association', 1),
 # S010
 ('S010', 'declining prices', 'L', 'repetition', 'S009: weakening', 'med', None, None, 1),
 # S011
 ('S011', 'agreed', 'L', 'repetition', 'S006: said several factors', 'low', None, 'stance echo; weak', 1),
 # S012
 ('S012', 'the US', 'L', 'repetition', 'S008: the US dollar', 'high', None, None, 1),
 # S013
 ('S013', 'That', 'R', 'demonstrative', 'S012: tariffs raising prices', 'high', None, None, 1),
 ('S013', 'the value of the Australian dollar', 'L', 'repetition', 'S006: the dollar\u2019s value', 'high', None, None, 1),
 ('S013', 'he', 'R', 'personal', 'S011: Greg Jericho', 'high', None, None, 3),
 # S014
 ('S014', 'The Australian dollar', 'L', 'repetition', 'S013: the value of the Australian dollar', 'high', None, None, 1),
 ('S014', 'the Chinese economy', 'L', 'repetition', 'S009: China\u2019s economic stimulus', 'high', None, None, 1),
 ('S014', 'our', 'R', 'personal', 'S011: Greg Jericho (authorial our)', 'med', None, None, 1),
 # S015
 ('S015', 'A weak Australian dollar', 'L', 'repetition', 'S014: The Australian dollar', 'high', None, None, 1),
 ('S015', 'imports', 'L', 'repetition', 'S001: dependent on imports', 'high', None, None, 1),
 # S016
 ('S016', 'Jericho', 'L', 'repetition', 'S013: he (Jericho)', 'high', None, None, 1),
 ('S016', 'this', 'R', 'demonstrative', 'S015: imports more expensive', 'high', None, None, 1),
 # S017
 ('S017', 'However', 'C', 'adversative', 'S016: petrol prices most affected', 'high', None, None, 1),
 ('S017', 'also', 'C', 'additive', 'S016: petrol prices', 'med', None, None, 1),
 ('S017', 'he', 'R', 'personal', 'S016: Jericho', 'high', None, None, 2),
 # S018
 ('S018', 'the dollar', 'L', 'repetition', 'S015: A weak Australian dollar', 'high', None, None, 1),
 # S019
 ('S019', 'a falling dollar', 'L', 'repetition', 'S018: the dollar falls', 'high', None, None, 1),
 ('S019', 'the cost of living', 'L', 'repetition', 'S015: tough for household budgets', 'med', None, None, 1),
 ('S019', 'households', 'L', 'repetition', 'S015: household budgets', 'high', None, None, 1),
 ('S019', 'imports', 'L', 'repetition', 'S015: imports', 'high', None, None, 1),
 # S021
 ('S020', 'a falling dollar', 'L', 'repetition', 'S019: a falling dollar', 'high', None, 'verbatim', 1),
 # S022
 ('S021', 'Hughes', 'L', 'repetition', 'S008: he (Hughes)', 'high', None, None, 1),
 # S023
 ('S022', 'However', 'C', 'adversative', 'S021: exchange now advice', 'high', None, None, 1),
 ('S022', 'the dollar', 'L', 'repetition', 'S020: a falling dollar', 'high', None, None, 1),
 # S025
 ('S023', 'Hughes', 'L', 'repetition', 'S021: Hughes', 'high', None, None, 1),
 ('S023', 'currency', 'L', 'repetition', 'S021: exchanging some currency', 'high', None, 'predicting currency movements', 1),
 # S026
 ('S024', 'the US dollar', 'L', 'repetition', 'S008: the US dollar', 'high', None, None, 1),
 # S027
 ('S025', 'the dollar', 'L', 'repetition', 'S022: the dollar', 'high', None, None, 1),
 ('S025', 'the situation', 'L', 'general word', 'S023-S024: indicators and conditions', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_10 (§2–§3) ----
 # [LC] biên = khung dẫn bị lược (attribution continuation); [TC] = trong câu.
 ('S009', None, 'E', 'clausal', 'S008: “This has led to an appreciation…,” he said', 'low', None, '[LC] biên: EN 11, 12 — trích dẫn Hughes kéo dài, khung dẫn chỉ ở EN 10 (“he said”); lược khung dẫn (attribution continuation), ∅ ở đầu khối trích tiếp theo', 1, '', '{he said}', 'LC'),
 ('S022', None, 'E', 'clausal', 'S021: “It might be worth considering…,” Hughes said', 'low', None, '[LC] biên: EN 36 — khối trích Hughes tiếp sau khung “Hughes said” ở EN 35; lược khung dẫn (attribution continuation)', 1, '', '{Hughes said}', 'LC'),
 ('S025', None, 'E', 'clausal', 'S024: “The Reserve Bank…,” he said', 'low', None, '[LC] biên: EN 41 — khối trích cuối tiếp sau khung “he said” ở EN 40; lược khung dẫn (attribution continuation)', 1, '', '{he said}', 'LC'),
]

TT = [
 # S002
 ('S002', 'đồng đô la Úc', 'L', 'repetition', 'S001: đồng đô la Úc', 'high', None, None, 1),
 ('S002', 'đồng đô la Mỹ', 'L', 'collocation', 'S001: đồng đô la Úc', 'low', None, 'currency association (phép liên tưởng)', 1),
 # S003
 ('S003', 'đồng đô la Úc', 'L', 'repetition', 'S002: đồng đô la Úc', 'high', None, None, 1),
 # S004
 ('S004', 'đồng đô la', 'L', 'repetition', 'S003: đồng đô la Úc', 'high', None, 'đồng đô la giảm giá', 1),
 ('S004', 'Úc', 'L', 'repetition', 'S003: đồng đô la Úc', 'high', None, 'các nhà xuất khẩu Úc', 1),
 # S005
 ('S005', 'đồng đô la Úc', 'L', 'repetition', 'S004: đồng đô la', 'high', None, None, 1),
 # S006
 ('S006', 'yếu tố', 'L', 'repetition', 'S005: Một số yếu tố', 'high', None, None, 1),
 ('S006', 'đồng đô la', 'L', 'repetition', 'S005: đồng đô la Úc', 'high', None, 'giá trị của đồng đô la', 1),
 # S007
 ('S007', 'Hoa Kỳ', 'L', 'repetition', 'S002: đồng đô la Mỹ', 'high', None, None, 1),
 # S008
 ('S008', 'Điều này', 'R', 'demonstrative', 'S007: ít cắt giảm lãi suất hơn', 'high', None, None, 1),
 ('S008', 'đồng đô la Mỹ', 'L', 'repetition', 'S002: đồng đô la Mỹ', 'high', None, None, 1),
 ('S008', 'đồng đô la Úc', 'L', 'repetition', 'S005: đồng đô la Úc', 'high', None, None, 1),
 ('S008', 'ông', 'R', 'personal', 'S006: Graeme Hughes', 'high', None, None, 1),
 # S009
 ('S009', 'đồng nhân dân tệ', 'L', 'collocation', 'S008: các loại tiền tệ khác', 'low', None, 'currency association', 1),
 # S010
 ('S010', 'giá cả giảm', 'L', 'repetition', 'S009: suy yếu', 'med', None, None, 1),
 # S011
 ('S011', 'đồng ý', 'L', 'repetition', 'S006: cho biết', 'low', None, 'stance echo; weak', 1),
 # S012
 ('S012', 'Hoa Kỳ', 'L', 'repetition', 'S007: Hoa Kỳ', 'high', None, None, 1),
 # S013
 ('S013', 'Điều đó', 'R', 'demonstrative', 'S012: thuế đẩy giá lên', 'high', None, None, 1),
 ('S013', 'giá trị của đồng đô la Úc', 'L', 'repetition', 'S006: giá trị của đồng đô la', 'high', None, None, 1),
 ('S013', 'ông', 'R', 'personal', 'S011: Greg Jericho', 'high', None, None, 1),
 # S014
 ('S014', 'Đồng đô la Úc', 'L', 'repetition', 'S013: đồng đô la Úc', 'high', None, None, 1),
 ('S014', 'nền kinh tế Trung Quốc', 'L', 'repetition', 'S009: kích thích kinh tế của Trung Quốc', 'high', None, None, 1),
 ('S014', 'chúng ta', 'R', 'personal', 'S011: Greg Jericho (authorial chúng ta)', 'med', None, None, 1),
 # S015
 ('S015', 'Đồng đô la Úc', 'L', 'repetition', 'S014: Đồng đô la Úc', 'high', None, None, 1),
 ('S015', 'hàng nhập khẩu', 'L', 'repetition', 'S001: phụ thuộc vào hàng nhập khẩu', 'high', None, None, 1),
 # S016
 ('S016', 'Ông Jericho', 'L', 'repetition', 'S013: ông (Jericho)', 'high', None, None, 1),
 ('S016', 'điều này', 'R', 'demonstrative', 'S015: hàng nhập khẩu đắt hơn', 'high', None, None, 1),
 # S017
 ('S017', 'Tuy nhiên', 'C', 'adversative', 'S016: giá xăng affected most', 'high', None, None, 1),
 ('S017', 'ông', 'R', 'personal', 'S016: Ông Jericho', 'high', None, None, 1),
 ('S017', 'cũng', 'C', 'additive', 'S016: giá xăng', 'med', None, None, 1),
 # S018
 ('S018', 'Đồng đô la giảm giá', 'L', 'repetition', 'S015: Đồng đô la Úc yếu', 'high', None, None, 1),
 ('S018', 'chi phí sinh hoạt', 'L', 'repetition', 'S015: ngân sách hộ gia đình', 'med', None, None, 1),
 ('S018', 'hộ gia đình', 'L', 'repetition', 'S015: ngân sách hộ gia đình', 'high', None, None, 1),
 ('S018', 'hàng nhập khẩu', 'L', 'repetition', 'S015: hàng nhập khẩu', 'high', None, None, 1),
 # S019
 ('S019', 'đồng đô la giảm giá', 'L', 'repetition', 'S018: Đồng đô la giảm giá', 'high', None, None, 1),
 # S020
 ('S020', 'ông Hughes', 'L', 'repetition', 'S008: ông (Hughes)', 'high', None, None, 1),
 # S021
 ('S021', 'Tuy nhiên', 'C', 'adversative', 'S020: exchange now advice', 'high', None, None, 1),
 ('S021', 'đồng đô la', 'L', 'repetition', 'S019: đồng đô la giảm giá', 'high', None, None, 1),
 # S022
 ('S022', 'Tuy nhiên', 'C', 'adversative', 'S021: wait advice', 'med', None, 'TT adds contrast EN lacks here', 1),
 ('S022', 'đồng AUD', 'L', 'repetition', 'S021: đồng đô la', 'high', None, 'AUD abbreviation variant', 1),
 # S023
 ('S023', 'Ông Hughes', 'L', 'repetition', 'S020: ông Hughes', 'high', None, None, 1),
 ('S023', 'tiền tệ', 'L', 'repetition', 'S020: đổi một số loại tiền tệ', 'high', None, 'biến động tiền tệ', 1),
 # S024
 ('S024', 'đồng đô la Mỹ', 'L', 'repetition', 'S008: đồng đô la Mỹ', 'high', None, None, 1),
 # S025
 ('S025', 'đồng đô la', 'L', 'repetition', 'S022: đồng AUD', 'high', None, None, 1),
 ('S025', 'tình hình', 'L', 'general word', 'S023-S024: các chỉ số', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_10 (§2–§3) ----
 # [TC] = trong câu; [LC] biên = khung dẫn bị lược (attribution continuation).
 ('S018', None, 'E', 'nominal', 'S018: {nó/đồng đô la} chủ ngữ vế “nhưng ∅ sẽ không ảnh hưởng” (trong câu)', 'high', None, '[TC] lược chủ ngữ {nó/đồng đô la} của “sẽ không ảnh hưởng”; EN 22 dùng đại từ it', 1, 'nhưng ', '{nó}', 'TC'),
 ('S021', None, 'E', 'nominal', 'S021: {nó} chủ ngữ “∅ có thể nên chờ” (trong câu)', 'high', None, '[TC] lược it-chủ từ hình thức + khung “be wise”: “∅ có thể nên chờ”; EN 36 “it might be wise to wait”', 1, 'sớm, ', '{nó}', 'TC'),
 ('S020', None, 'E', 'nominal', 'S020: {nó} chủ ngữ “∅ có thể cân nhắc” (trong câu)', 'high', None, '[TC] lược it-chủ từ + “be worth”: “∅ có thể cân nhắc đổi…”; EN 35 “It might be worth considering”', 1, '"', '{nó}', 'TC'),
 ('S004', None, 'E', 'nominal', 'S004: {điều này} (trong câu)', 'med', None, '[TC] lược this tình huống — vế “vì” mượn chủ ngữ từ ngữ cảnh; EN 6 “as this can make prices more competitive”', 1, 'giảm giá ', '{điều này}', 'TC'),
 ('S009', None, 'E', 'clausal', 'S008: “Điều này đã dẫn đến…”, ông cho biết', 'low', None, '[LC] biên: VI 11, 12 (sau khung “ông cho biết” ở VI 10), VI 36 (sau khung “ông Hughes nói” ở VI 35), VI 41 (sau khung “ông nói” ở VI 40) — lược khung dẫn (attribution continuation), ∅ ở đầu khối trích tiếp theo', 1, '', '{ông cho biết}', 'LC'),
]
