# P08 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S003
 ('S003', "Australia's housing market", 'L', 'repetition', 'S001: Australia\u2019s property market', 'high', None, 'near-verbatim', 1),
 ('S003', 'property values', 'L', 'repetition', 'S001: property market', 'high', None, None, 1),
 # S004
 ('S004', 'home prices', 'L', 'repetition', 'S003: property values', 'high', None, None, 1),
 # S005
 ('S005', 'Domain', 'L', 'repetition', 'S004: Domain\u2019s house price report', 'high', None, None, 1),
 ('S005', 'the data', 'L', 'general word', 'S004: house price report findings', 'high', 'R: the', None, 1),
 ('S005', 'buyer', 'L', 'repetition', 'S002: buyers', 'high', None, 'buyer behaviour', 1),
 ('S005', 'demand', 'L', 'repetition', 'S003: shifting demand', 'high', None, None, 1),
 # S006
 ('S006', 'we', 'R', 'personal', 'S005: Nicola Powell (quoted speaker)', 'med', None, None, 1),
 ('S006', 'buyer demand', 'L', 'repetition', 'S005: demand', 'high', None, None, 1),
 # S007
 ('S007', 'That', 'R', 'demonstrative', 'S006: a pullback in buyer demand', 'high', None, None, 1),
 ('S007', 'demand', 'L', 'repetition', 'S006: buyer demand', 'high', None, None, 1),
 ('S007', 'Powell said', 'L', 'repetition', 'S005: Nicola Powell', 'high', None, None, 1),
 # S008
 ('S008', 'This delay', 'L', 'repetition', 'S007: people delay their decisions', 'high', 'R: this', None, 1),
 ('S008', 'affordability pressures', 'L', 'repetition', 'S003: affordability pressures', 'high', None, 'verbatim', 1),
 ('S008', 'prices', 'L', 'repetition', 'S004: home prices', 'high', None, 'rising prices', 1),
 ('S008', 'buyers', 'L', 'repetition', 'S005: buyer', 'high', None, None, 1),
 # S009
 ('S009', 'But', 'C', 'adversative', 'S006-S008: demand delayed not gone', 'high', None, None, 1),
 ('S009', 'house prices', 'L', 'repetition', 'S008: prices', 'high', None, None, 1),
 ('S009', 'the quarter', 'L', 'repetition', 'S004: the December quarter', 'high', None, None, 1),
 # S010
 ('S010', 'Sydney', 'L', 'repetition', 'S009: the only city (Sydney)', 'med', None, 'S009 says the only city to record a decline', 1),
 ('S010', "Australia's", 'L', 'repetition', 'S003: Australia\u2019s housing market', 'high', None, None, 1),
 ('S010', 'housing market', 'L', 'repetition', 'S003: housing market', 'high', None, None, 1),
 # S011
 ('S011', "It's", 'R', 'personal', 'S010: Sydney', 'high', None, None, 1),
 ('S011', 'Sydney', 'L', 'repetition', 'S010: Sydney', 'high', None, None, 1),
 ('S011', 'quarterly decline', 'L', 'repetition', 'S009: the second consecutive decline', 'high', None, None, 1),
 # S012
 ('S012', 'Data', 'L', 'repetition', 'S005: the data', 'high', None, None, 1),
 ('S012', "Domain's recent report", 'L', 'repetition', 'S004: Domain\u2019s house price report', 'high', None, None, 1),
 ('S012', "the city's", 'R', 'personal', 'S010-S011: Sydney', 'high', None, None, 1),
 ('S012', 'median', 'L', 'repetition', 'S009: a median of $1,645,444', 'high', None, None, 1),
 # S013
 ('S013', 'property price', 'L', 'repetition', 'S003: property values', 'high', None, None, 1),
 # S014
 ('S014', 'houses prices', 'L', 'repetition', 'S013: property price changes', 'high', None, 'source typo houses prices', 1),
 # S015
 ('S015', 'Similarly', 'C', 'additive', 'S014: Biggera Waters price fall', 'high', None, None, 1),
 ('S015', 'house prices', 'L', 'repetition', 'S014: houses prices', 'high', None, None, 1),
 # S016
 ('S016', 'unit prices', 'L', 'repetition', 'S012: median prices for units', 'high', None, None, 1),
 ('S016', 'the December quarter', 'L', 'repetition', 'S004: the December quarter', 'high', None, 'verbatim', 1),
 # S017
 ('S017', 'Powell', 'L', 'repetition', 'S007: Powell said', 'high', None, None, 1),
 ('S017', 'unit price', 'L', 'repetition', 'S016: unit prices', 'high', None, None, 1),
 # S018
 ('S018', 'Melbourne', 'L', 'repetition', 'S016: Melbourne unit prices', 'high', None, None, 1),
 # S019
 ('S019', "It's", 'R', 'personal', 'S018: Melbourne', 'high', None, None, 1),
 ('S019', 'a market', 'L', 'general word', 'S003: housing market', 'high', None, None, 1),
 ('S019', 'we', 'R', 'personal', 'S017: Powell', 'med', None, None, 1),
 ('S019', 'Powell said', 'L', 'repetition', 'S017: Powell', 'high', None, None, 1),
 # S020
 ('S020', 'This', 'R', 'demonstrative', 'S019: growth in the final quarter of 2024', 'high', None, None, 1),
 ('S020', 'buyers', 'L', 'repetition', 'S008: buyers', 'high', None, 'activating buyers', 1),
 ('S020', 'first-home buyers', 'L', 'repetition', 'S017: first-home buyer activity', 'high', None, None, 1),
 # S021
 ('S021', 'Sydney and Melbourne', 'L', 'repetition', 'S010: Sydney + S016: Melbourne', 'high', None, None, 1),
 ('S021', 'price cycles', 'L', 'repetition', 'S019: underperformed as a market', 'med', None, None, 1),
 # S022
 ('S022', 'those two movements in price', 'R', 'demonstrative', 'S021: Sydney and Melbourne price cycles', 'high', None, None, 1),
 ('S022', 'this', 'R', 'demonstrative', 'S021: strong relationship between the cycles', 'high', None, None, 1),
 ('S022', 'Melbourne', 'L', 'repetition', 'S021: Melbourne', 'high', None, None, 1),
 # S023
 ('S023', 'housing affordability', 'L', 'repetition', 'S003: affordability pressures', 'high', None, None, 1),
 ('S023', 'unit prices', 'L', 'repetition', 'S016: unit prices', 'high', None, None, 1),
 # S024
 ('S024', 'also', 'C', 'additive', 'S023: Chadstone improvement', 'med', None, None, 1),
 ('S024', 'a fall', 'L', 'repetition', 'S023: unit prices dropping', 'high', None, None, 1),
 ('S024', 'unit price', 'L', 'repetition', 'S023: unit prices', 'high', None, None, 1),
 ('S024', 'over the same period', 'L', 'repetition', 'S023: year-on-year', 'med', None, None, 1),
 # S025
 ('S025', 'Meanwhile', 'C', 'additive', 'S023-S024: Melbourne unit falls', 'high', None, None, 1),
 ('S025', 'house prices', 'L', 'repetition', 'S014: house prices', 'high', None, None, 1),
 # S026
 ('S026', 'Regional and smaller markets', 'L', 'repetition', 'S010: Australia\u2019s most expensive housing market', 'med', None, 'market chain generalisation', 1),
 ('S026', 'these changes', 'R', 'demonstrative', 'S023-S025: price falls', 'high', None, None, 1),
 # S027
 ('S027', 'the median house price', 'L', 'repetition', 'S012: median + S014: house prices', 'high', None, None, 1),
 # S028
 ('S028', 'unit prices', 'L', 'repetition', 'S024: unit price', 'high', None, None, 1),
 ('S028', 'capital cities', 'L', 'repetition', 'S010: Australia\u2019s most expensive housing market', 'med', None, 'capital-level market chain', 1),
 # S029
 ('S029', 'In contrast', 'C', 'adversative', 'S028: sharpest unit decline', 'high', None, None, 1),
 ('S029', 'house prices', 'L', 'repetition', 'S025: house prices', 'high', None, None, 1),
 ('S029', 'the quarter', 'L', 'repetition', 'S009: the quarter', 'high', None, None, 1),
 # S030
 ('S030', "Canberra's housing market", 'L', 'repetition', 'S003: Australia\u2019s housing market', 'high', None, None, 1),
 ('S030', 'the same period', 'L', 'repetition', 'S024: over the same period', 'high', None, None, 1),
 ('S030', 'house or unit prices', 'L', 'repetition', 'S028-S029: house prices / unit prices', 'high', None, None, 1),
 # S031
 ('S031', 'But', 'C', 'adversative', 'S030: stagnant market', 'high', None, None, 1),
 ('S031', 'house prices', 'L', 'repetition', 'S030: house or unit prices', 'high', None, None, 1),
 ('S031', 'the median', 'L', 'repetition', 'S027: the median house price', 'high', None, None, 1),
 # S032
 ('S032', 'it', 'R', 'personal', 'S026-S031: the market changes', 'med', None, 'a buyer\u2019s market', 1),
 # S033
 ('S033', 'the market', 'L', 'repetition', 'S030: Canberra\u2019s housing market', 'high', None, None, 1),
 ('S033', 'affordability', 'L', 'repetition', 'S023: housing affordability', 'high', None, None, 1),
 # S034
 ('S034', 'Increased supply', 'L', 'repetition', 'S033: annual growth slow', 'med', None, 'supply-side echo', 1),
 ('S034', 'price', 'L', 'repetition', 'S031: house prices', 'high', None, 'negotiate on price', 1),
 # S035
 ('S035', 'But', 'C', 'adversative', 'S034: more opportunities', 'high', None, None, 1),
 ('S035', 'this trend', 'L', 'repetition', 'S033-S034: slowed growth and supply', 'high', 'R: this', None, 1),
 # S036
 ('S036', 'Powell', 'L', 'repetition', 'S019: Powell said', 'high', None, None, 1),
 # S037
 ('S037', 'interesting', 'L', 'repetition', 'S001: an "interesting" one', 'high', None, 'echo of the lede', 1),
 ('S037', 'she', 'R', 'personal', 'S036: Powell', 'high', None, None, 1),
 # S038
 ('S038', 'Weak conditions', 'L', 'repetition', 'S033: growth slow to its lowest', 'med', None, None, 1),
 ('S038', '2025', 'L', 'repetition', 'S037: 2025 is going to be an interesting year', 'med', None, None, 1),
 # S039
 ('S039', 'the change', 'L', 'repetition', 'S035: will this trend hold', 'med', None, None, 1),
 ('S039', 'we', 'R', 'personal', 'S019: we (Powell)', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_08 (§2–§3, §9) ----
 # [LC] = liên câu; [TC] = trong câu. Các dòng này KHÔNG do script sinh:
 # người đọc bản phân tích ngữ nghĩa rồi chọn đúng vị trí/tiền trạm.
 # E-EN1: bổ ngữ “with” + vị ngữ trần, lược hệ từ.
 ('S014', None, 'E', 'clausal', 'S014: {being} (trong câu)', 'high', None,
  '[TC] E-EN1: vị ngữ trần trong bổ ngữ “with” — “with houses prices {being} at $660,000”, lược hệ từ', 1,
  'affordable, with houses prices ', '{being}', 'TC'),
 # E-EN2: cùng khuôn with + ∅ hệ từ.
 ('S030', None, 'E', 'clausal', 'S030: {there being} (trong câu)', 'high', None,
  '[TC] E-EN2: cùng khuôn “with” + ∅ hệ từ — “with {there being} no change in house or unit prices”', 1,
  'the same period, with ', '{there being}', 'TC'),
 # E-EN3: vị ngữ rút sau gạch ngang (biên).
 ('S016', None, 'E', 'clausal', 'S016: {it was} (trong câu)', 'low', None,
  '[TC] biên E-EN3: vị ngữ rút sau gạch ngang — “— {it was} up 2.1 per cent over the December quarter”', 1,
  'increase in 1.5 years — ', '{it was}', 'TC'),
 # E-EN4: trích dẫn kéo dài không khung dẫn (biên, liên câu). EN 7 = S008;
 # các vị trí còn lại: EN 17 = S020, EN 30 = S038 (cùng hiện tượng).
 ('S008', None, 'E', 'clausal', 'S007: Powell said (khung dẫn khối mở đầu)', 'low', None,
  '[LC] biên E-EN4: trích dẫn kéo dài không khung dẫn — lược {she said} ở cuối khối; cùng hiện tượng ở EN 17 (S020) và EN 30 (S038)', 1,
  'keep up."', '{she said}', 'LC'),
 # S-EN1: thế “one” trong standfirst (VI hiện thực hóa “một năm”, không thêm S cho VI).
 ('S001', 'one', 'S', 'nominal', 'S001: a year (within sentence)', 'high', None,
  '[TC] S-EN1: one thế danh từ ← year trong standfirst; VI hiện thực hóa “một năm”', 1,
  None, None, 'TC'),
]

TT = [
 # S003
 ('S003', 'Thị trường nhà ở Úc', 'L', 'repetition', 'S001: thị trường địa ốc Úc', 'high', None, None, 1),
 ('S003', 'giá nhà', 'L', 'repetition', 'S002: người mua nhà', 'med', None, 'nhà morphological chain', 1),
 # S004
 ('S004', 'giá nhà', 'L', 'repetition', 'S003: giá nhà', 'high', None, None, 1),
 # S005
 ('S005', 'Domain', 'L', 'repetition', 'S004: Domain', 'high', None, None, 1),
 ('S005', 'người mua nhà', 'L', 'repetition', 'S002: người mua nhà', 'high', None, None, 1),
 # S006
 ('S006', 'chúng tôi', 'R', 'personal', 'S005: bà Nicola Powell (quoted speaker)', 'med', None, None, 1),
 ('S006', 'người mua', 'L', 'repetition', 'S005: người mua nhà', 'high', None, 'nhu cầu của người mua', 1),
 # S007
 ('S007', 'Điều đó', 'R', 'demonstrative', 'S006: nhu cầu của người mua giảm', 'high', None, None, 1),
 ('S007', 'nhu cầu', 'L', 'repetition', 'S006: nhu cầu', 'high', None, None, 1),
 ('S007', 'họ', 'R', 'personal', 'S006: người mua', 'high', None, None, 1),
 ('S007', 'bà', 'R', 'personal', 'S005: bà Nicola Powell', 'high', None, None, 1),
 # S008
 ('S008', 'Sự trì hoãn này', 'L', 'repetition', 'S007: trì hoãn việc ra quyết định', 'high', 'R: này', None, 1),
 ('S008', 'giá nhà', 'L', 'repetition', 'S004: giá nhà', 'high', None, 'áp lực giá nhà', 1),
 ('S008', 'người mua', 'L', 'repetition', 'S006: người mua', 'high', None, None, 1),
 # S009
 ('S009', 'thị trường nhà ở', 'L', 'repetition', 'S003: Thị trường nhà ở Úc', 'high', None, None, 1),
 ('S009', 'Úc', 'L', 'repetition', 'S003: Úc', 'high', None, None, 1),
 ('S009', 'giá nhà', 'L', 'repetition', 'S008: giá nhà', 'high', None, None, 1),
 ('S009', 'trong quý', 'L', 'repetition', 'S004: quý 4/2024', 'med', None, None, 1),
 # S010
 ('S010', 'Sydney', 'L', 'repetition', 'S009: Sydney', 'high', None, None, 1),
 ('S010', 'giá nhà', 'L', 'repetition', 'S009: giá nhà', 'high', None, None, 1),
 ('S010', 'hai quý', 'L', 'repetition', 'S009: trong quý', 'med', None, None, 1),
 # S011
 ('S011', 'Dữ liệu', 'L', 'repetition', 'S005: dữ liệu', 'high', None, None, 1),
 ('S011', 'Domain', 'L', 'repetition', 'S005: Domain', 'high', None, None, 1),
 ('S011', 'giá căn hộ', 'L', 'repetition', 'S009: giá nhà', 'med', None, 'căn hộ ~ nhà (unit vs house)', 1),
 ('S011', 'Sydney', 'L', 'repetition', 'S010: Sydney', 'high', None, 'phía bắc Sydney', 1),
 # S012
 ('S012', 'giá bất động sản', 'L', 'repetition', 'S011: giá căn hộ', 'high', None, None, 1),
 # S013
 ('S013', 'giá nhà', 'L', 'repetition', 'S012: giá nhà', 'high', None, None, 1),
 # S014
 ('S014', 'Tương tự', 'C', 'additive', 'S013: Biggera Waters price fall', 'high', None, None, 1),
 ('S014', 'giá nhà', 'L', 'repetition', 'S013: giá nhà', 'high', None, None, 1),
 # S015
 ('S015', 'căn hộ', 'L', 'repetition', 'S011: giá căn hộ', 'high', None, None, 1),
 ('S015', 'quý 4', 'L', 'repetition', 'S004: quý 4/2024', 'high', None, None, 1),
 # S016
 ('S016', 'Giá nhà', 'L', 'repetition', 'S014: giá nhà', 'high', None, None, 1),
 ('S016', 'trong cùng giai đoạn', 'L', 'repetition', 'S015: trong quý 4', 'med', None, None, 1),
 # S017
 ('S017', 'Bà Powell', 'L', 'repetition', 'S007: bà', 'high', None, None, 1),
 ('S017', 'sự gia tăng này', 'L', 'repetition', 'S015-S016: giá tăng', 'high', 'R: này', None, 1),
 # S018
 ('S018', 'Melbourne', 'L', 'repetition', 'S015: Melbourne', 'high', None, None, 1),
 # S019
 ('S019', 'Thị trường', 'L', 'general word', 'S009: thị trường nhà ở', 'high', None, None, 1),
 ('S019', 'chúng tôi', 'R', 'personal', 'S017: Bà Powell', 'med', None, None, 1),
 ('S019', 'bà Powell', 'L', 'repetition', 'S017: Bà Powell', 'high', None, None, 1),
 # S020
 ('S020', 'Sự tăng trưởng này', 'L', 'repetition', 'S019: sự tăng trưởng', 'high', 'R: này', None, 1),
 ('S020', 'người mua', 'L', 'repetition', 'S008: người mua', 'high', None, 'thu hút người mua', 1),
 ('S020', 'người mua nhà lần đầu', 'L', 'repetition', 'S017: người mua nhà lần đầu', 'high', None, None, 1),
 # S021
 ('S021', 'khả năng chi trả nhà ở', 'L', 'repetition', 'S008: áp lực giá nhà (affordability)', 'med', None, None, 1),
 ('S021', 'giá căn hộ', 'L', 'repetition', 'S011: giá căn hộ', 'high', None, None, 1),
 # S022
 ('S022', 'cũng', 'C', 'additive', 'S021: Chadstone improvement', 'med', None, None, 1),
 ('S022', 'giá căn hộ', 'L', 'repetition', 'S021: giá căn hộ', 'high', None, None, 1),
 ('S022', 'trong cùng giai đoạn', 'L', 'repetition', 'S016: trong cùng giai đoạn', 'high', None, None, 1),
 # S023
 ('S023', 'Trong khi đó', 'C', 'additive', 'S021-S022: unit price falls', 'high', None, None, 1),
 ('S023', 'giá nhà', 'L', 'repetition', 'S016: Giá nhà', 'high', None, None, 1),
 # S024
 ('S024', 'những thay đổi này', 'L', 'repetition', 'S012: sự thay đổi lớn về giá', 'high', 'R: này', None, 1),
 ('S024', 'thị trường', 'L', 'repetition', 'S019: Thị trường', 'med', None, 'Các thị trường nhỏ hơn', 1),
 # S025
 ('S025', 'giá nhà', 'L', 'repetition', 'S023: giá nhà', 'high', None, 'giá nhà trung bình', 1),
 # S026
 ('S026', 'giá căn hộ', 'L', 'repetition', 'S022: giá căn hộ', 'high', None, None, 1),
 # S027
 ('S027', 'Tuy nhiên', 'C', 'adversative', 'S026: sharpest unit decline', 'high', None, None, 1),
 ('S027', 'giá nhà', 'L', 'repetition', 'S025: giá nhà', 'high', None, None, 1),
 ('S027', 'trong quý 4', 'L', 'repetition', 'S015: quý 4', 'high', None, None, 1),
 # S028
 ('S028', 'Trong khi đó', 'C', 'additive', 'S027: Hobart contrast', 'med', None, None, 1),
 ('S028', 'thị trường', 'L', 'repetition', 'S024: thị trường', 'med', None, 'thị trường Canberra', 1),
 ('S028', 'giá nhà và căn hộ', 'L', 'repetition', 'S026-S027: giá căn hộ / giá nhà', 'high', None, None, 1),
 ('S028', 'trong cùng giai đoạn', 'L', 'repetition', 'S022: trong cùng giai đoạn', 'high', None, None, 1),
 # S029
 ('S029', 'Tuy nhiên', 'C', 'adversative', 'S028: stagnant market', 'high', None, None, 1),
 ('S029', 'giá nhà', 'L', 'repetition', 'S028: giá nhà', 'high', None, None, 1),
 # S030
 ('S030', 'người mua nhà', 'L', 'repetition', 'S005: người mua nhà', 'high', None, None, 1),
 ('S030', 'năm 2025', 'L', 'repetition', 'S001: năm 2025', 'high', None, None, 1),
 # S031
 ('S031', 'thị trường địa ốc', 'L', 'repetition', 'S001: thị trường địa ốc Úc', 'high', None, None, 1),
 ('S031', 'khả năng chi trả', 'L', 'repetition', 'S021: khả năng chi trả nhà ở', 'high', None, None, 1),
 # S032
 ('S032', 'Nguồn cung gia tăng', 'L', 'repetition', 'S031: tăng trưởng hàng năm', 'med', None, 'supply-side echo', 1),
 ('S032', 'giá', 'L', 'repetition', 'S029: giá nhà', 'high', None, 'thương lượng về giá', 1),
 # S033
 ('S033', 'Nhưng', 'C', 'adversative', 'S032: more opportunities', 'high', None, None, 1),
 ('S033', 'xu hướng này', 'L', 'repetition', 'S031-S032: slowed growth and supply', 'high', 'R: này', None, 1),
 # S034
 ('S034', 'bà Powell', 'L', 'repetition', 'S019: bà Powell', 'high', None, None, 1),
 # S035
 ('S035', 'một năm thú vị', 'L', 'repetition', 'S001: một năm thú vị', 'high', None, 'echo of the lede', 1),
 ('S035', 'bà', 'R', 'personal', 'S034: Bà Powell', 'high', None, None, 1),
 # S036
 ('S036', 'điều kiện yếu', 'L', 'repetition', 'S031: chậm lại', 'med', None, None, 1),
 ('S036', 'năm 2025', 'L', 'repetition', 'S030: năm 2025', 'med', None, None, 1),
 # S037
 ('S037', 'Tuy nhiên', 'C', 'adversative', 'S036: weak conditions flowing into 2025', 'high', None, None, 1),
 ('S037', 'chúng ta', 'R', 'personal', 'S019: chúng tôi (Powell)', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_08 (§2–§3, §9) ----
 # [LC] = liên câu; [TC] = trong câu. Các dòng này KHÔNG do script sinh:
 # người đọc bản phân tích ngữ nghĩa rồi chọn đúng vị trí/tiền trạm.
 # E-VI1: VI cắt cả cụm “it means” của EN, chuyển thẳng sang chủ ngữ mới.
 ('S007', None, 'E', 'clausal', 'S007: “it means” (EN 6) (trong câu)', 'high', None,
  '[TC] E-VI1: lược cả cụm {nó có nghĩa là} — EN giữ “it means”, VI cắt bỏ rồi sang chủ ngữ mới “họ”', 1,
  'biến mất – ', '{nó có nghĩa là}', 'TC'),
 # E-VI2: lược liên từ “và” khi nối vế.
 ('S020', None, 'E', 'clausal', 'S020: {và} (trong câu)', 'high', None,
  '[TC] E-VI2: lược liên từ {và} — “theo thời gian, ∅ thu hút người mua”; EN: and activating buyers', 1,
  'theo thời gian, ', '{và}', 'TC'),
 # E-VI3: VI lược chủ ngữ “that/đó”, chia sẻ chủ ngữ cho hai vế.
 ('S036', None, 'E', 'nominal', 'S036: {đó} (trong câu)', 'high', None,
  '[TC] E-VI3: lược chủ ngữ {đó} — EN “that is going to flow”, VI chia sẻ chủ ngữ “Các điều kiện yếu”', 1,
  '2024 và ', '{đó}', 'TC'),
 # E-VI4: vị ngữ trần “còn $660.000”, song song E-EN1.
 ('S013', None, 'E', 'nominal', 'S013: {giá} (trong câu)', 'med', None,
  '[TC] E-VI4: vị ngữ trần “còn $660.000”, lược chủ ngữ {giá}; song song E-EN1', 1,
  'so với năm trước, ', '{giá}', 'TC'),
 # E-VI5: cụm “với” không vị ngữ (biên), song song E-EN3.
 ('S015', None, 'E', 'verbal', 'S015: {là} (trong câu)', 'low', None,
  '[TC] biên E-VI5: cụm “với” không vị ngữ — “với mức tăng {là} 2,1% trong quý 4”, song song E-EN3', 1,
  'với mức tăng ', '{là}', 'TC'),
 # E-VI6: trích dẫn kéo dài không khung dẫn (biên, liên câu). VI 7 = S008;
 # các vị trí còn lại: VI 17 = S020, VI 30 = S036 (cùng hiện tượng).
 ('S008', None, 'E', 'clausal', 'S007: bà nói (khung dẫn khối mở đầu)', 'low', None,
  '[LC] biên E-VI6: trích dẫn kéo dài không khung dẫn — lược {bà nói} ở cuối khối; cùng hiện tượng ở VI 17 (S020) và VI 30 (S036)', 1,
  'trong việc chi trả.”', '{bà nói}', 'LC'),
]
