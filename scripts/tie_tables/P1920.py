# P19/P20 tie tables.

# ---- P19 ----
P19_ST = [
 # S002
 ('S002', 'A lawsuit', 'L', 'repetition', 'S001: (lawsuit implied in settlement)', 'med', None, None, 1),
 ('S002', 'air carriers', 'L', 'repetition', 'S001: eight airlines', 'med', None, 'carrier chain; “five more” is the ellipsis site, marked E', 1),
 # S003
 ('S003', 'The case', 'L', 'general word', 'S001-S002: the lawsuit', 'high', None, None, 1),
 ('S003', 'tickets', 'L', 'repetition', 'S001: (tickets implied)', 'low', None, 'weak', 1),
 ('S003', 'airlines', 'L', 'repetition', 'S001: eight airlines', 'high', None, None, 1),
 # S004
 ('S004', 'Settlements', 'L', 'repetition', 'S001: eligible for a share of settlements', 'high', None, None, 1),
 ('S004', 'a lawsuit', 'L', 'repetition', 'S002: A lawsuit', 'high', None, None, 1),
 ('S004', 'airlines', 'L', 'repetition', 'S003: airlines', 'high', None, None, 1),
 # S005
 ('S005', 'The carriers which have settled', 'L', 'repetition', 'S004: eight airlines', 'high', None, None, 1),
 # S006
 ('S006', 'the case', 'L', 'repetition', 'S003: The case', 'high', None, None, 1),
 ('S006', 'U.S. government', 'L', 'repetition', 'S001: (none)', 'low', None, 'first overt mention; weak', 1),
 # S007
 ('S007', 'the air passenger industry', 'L', 'repetition', 'S001: Travelers who flew', 'med', None, None, 1),
 ('S007', 'air cargo carriers', 'L', 'repetition', 'S006: (cargo implied in investigations)', 'low', None, 'weak', 1),
 # S008
 ('S008', 'the cargo', 'L', 'repetition', 'S007: air cargo carriers', 'high', None, None, 1),
 ('S008', 'the world', 'L', 'repetition', 'S001: across the Pacific (world)', 'low', None, 'weak', 1),
 # S009
 ('S009', 'a very large class action [lawsuit]', 'L', 'repetition', 'S002-S004: the lawsuit', 'high', None, None, 1),
 # S010
 ('S010', 'many of the defendants', 'L', 'repetition', 'S009: class action [lawsuit] (defendants)', 'med', None, None, 1),
 ('S010', 'that case', 'R', 'demonstrative', 'S009: a very large class action', 'high', None, None, 1),
 ('S010', 'our case', 'R', 'personal', 'S006: the case (Zapala\u2019s)', 'high', None, None, 1),
 ('S010', 'Zapala', 'L', 'repetition', 'S006: Attorney Adam Zapala', 'high', None, None, 1),
 # S011
 ('S011', 'Zapala', 'L', 'repetition', 'S010: Zapala', 'high', None, None, 1),
 ('S011', 'passengers', 'L', 'repetition', 'S007: the air passenger industry', 'high', None, None, 1),
 ('S011', 'applications', 'L', 'repetition', 'S001: (claims implied)', 'low', None, 'weak', 1),
 # S012
 ('S012', 'People', 'L', 'repetition', 'S011: passengers', 'high', None, None, 1),
 ('S012', 'the number of flights', 'L', 'repetition', 'S001: flew ... between 2000 and this year', 'med', None, None, 1),
 # S013
 ('S013', 'the class', 'L', 'repetition', 'S009: a very large class action', 'high', None, None, 1),
 ('S013', 'claims', 'L', 'repetition', 'S011: applications for claims', 'high', None, None, 1),
 # S014
 ('S014', 'The attorney', 'L', 'general word', 'S011: Zapala', 'high', None, None, 1),
 ('S014', 'price-fixing', 'L', 'repetition', 'S006: price-fixing investigations', 'high', None, None, 1),
 ('S014', 'such legal actions', 'L', 'repetition', 'S009-S010: the class action lawsuits', 'high', None, None, 1),
 # S015
 ('S015', 'The class action suit', 'L', 'repetition', 'S009: a very large class action [lawsuit]', 'high', None, None, 1),
 ('S015', 'airlines', 'L', 'repetition', 'S004: airlines', 'high', None, None, 1),
 ('S015', 'fix prices', 'L', 'repetition', 'S014: price-fixing', 'high', None, None, 1),
 ('S015', 'trans-Pacific travel', 'L', 'repetition', 'S001: across the Pacific', 'high', None, None, 1),
 ('S015', 'passengers', 'L', 'repetition', 'S011: passengers', 'high', None, None, 1),
 # S016
 ('S016', 'The routes', 'L', 'repetition', 'S001: across the Pacific (routes)', 'med', None, None, 1),
 ('S016', 'the United States', 'L', 'repetition', 'S006: U.S. government', 'high', None, 'expansion of abbreviation', 1),
 # S017
 ('S017', 'The eight airlines which settled', 'L', 'repetition', 'S005: The carriers which have settled', 'high', None, None, 1),
 ('S017', 'the allegation', 'L', 'repetition', 'S015: claims airlines colluded', 'high', None, None, 1),
 # S018
 ('S018', 'Those still being sued', 'L', 'repetition', 'S002-S004: five more air carriers', 'high', None, None, 1),
 # S019
 ('S019', 'However', 'C', 'adversative', 'S018: those still being sued', 'high', None, None, 1),
 ('S019', 'ANA', 'L', 'repetition', 'S018: All Nippon Airways (ANA)', 'high', None, None, 1),
 ('S019', 'fixing the prices', 'L', 'repetition', 'S015: fix prices', 'high', None, None, 1),
 # S020
 ('S020', 'Those', 'R', 'demonstrative', 'S001: Travelers who flew', 'high', None, None, 1),
 ('S020', 'a claim form', 'L', 'repetition', 'S013: claims', 'high', None, None, 1),
 # S021
 ('S021', 'Information', 'L', 'repetition', 'S020: a claim form (info implied)', 'low', None, 'weak', 1),
 ('S021', 'the website', 'L', 'repetition', 'S020: online', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_19 (§2–§3) ----
 ('S002', None, 'E', 'nominal', 'S002: {air carriers} (trong câu)', 'high', None, '[TC] lượng từ + ∅ danh: “five more ∅ air carriers”; vị trí 2 ở S004', 1, 'against five more', '{air carriers}', 'TC'),
 ('S002', 'the same thing', 'S', 'nominal', 'S001-S002: price-fixing', 'high', None, '[TC] the same + ∅ {price-fixing}; VI “một hành vi tương tự” (hạ đồng nhất → tương tự)', 1, None, None, 'TC'),
 ('S007', 'the same players', 'S', 'nominal', 'S006: the airlines', 'high', None, '[TC] the same + ∅ {players}; VI “Nhiều dịch vụ hàng không” (mất đồng nhất + khử tác nhân)', 1, None, None, 'TC'),
 ('S018', None, 'E', 'nominal', 'S018: {airlines who are} (trong câu)', 'high', None, '[TC] headless relative “Those ∅ still being sued”', 1, '', '{Airlines who are} (Those ∅ still being sued)', 'TC'),
 ('S020', None, 'E', 'nominal', 'S020: {people} (trong câu)', 'high', None, '[TC] headless relative “Those ∅ who believe they may be eligible”', 1, '', '{people} (Those ∅ who believe…)', 'TC'),

 ('S004', None, 'E', 'nominal', 'S004: {air carriers} (trong câu)', 'high', None, '[TC] lượng từ + ∅ danh lần 2: “continues against five more ∅”', 1, 'a lawsuit continues against five more', '{air carriers}', 'TC'),
]
P19_TT = [
 # S002
 ('S002', 'vụ kiện', 'L', 'repetition', 'S001: (lawsuit implied)', 'med', None, None, 1),
 ('S002', '5 hãng máy bay', 'L', 'repetition', 'S001: 8 hãng hàng không', 'med', None, 'carrier chain', 1),
 # S003
 ('S003', 'Hành khách', 'L', 'repetition', 'S001: Hành khách', 'high', None, None, 1),
 ('S003', 'xuyên Thái Bình Dương', 'L', 'repetition', 'S001: xuyên Thái Bình Dương', 'high', None, 'verbatim', 1),
 # S004
 ('S004', 'Vụ kiện', 'L', 'repetition', 'S002: vụ kiện', 'high', None, None, 1),
 ('S004', 'vé máy bay', 'L', 'repetition', 'S003: (tickets implied)', 'low', None, 'weak', 1),
 ('S004', 'hãng hàng không', 'L', 'repetition', 'S001: 8 hãng hàng không', 'high', None, None, 1),
 # S005
 ('S005', '8 hãng hàng không', 'L', 'repetition', 'S004: hãng hàng không', 'high', None, None, 1),
 ('S005', 'vụ kiện', 'L', 'repetition', 'S004: Vụ kiện', 'high', None, None, 1),
 ('S005', '5 hãng máy bay', 'L', 'repetition', 'S002: 5 hãng máy bay', 'high', None, None, 1),
 # S006
 ('S006', 'Các hãng', 'L', 'repetition', 'S005: 8 hãng hàng không', 'high', None, None, 1),
 # S007
 ('S007', 'vụ kiện này', 'L', 'repetition', 'S005: vụ kiện', 'high', 'R: này', None, 1),
 ('S007', 'chính phủ Mỹ', 'L', 'repetition', 'S001: (none)', 'low', None, 'first overt mention; weak', 1),
 ('S007', 'Luật sư Adam Zapala', 'L', 'repetition', 'S006: (none)', 'low', None, 'first overt mention; chain anchor', 1),
 # S008
 ('S008', 'Ông Zapala', 'L', 'repetition', 'S007: Luật sư Adam Zapala', 'high', None, None, 1),
 ('S008', 'ngành vận tải hành khách', 'L', 'repetition', 'S003: Hành khách', 'med', None, None, 1),
 ('S008', 'vận tải hàng hóa', 'L', 'repetition', 'S007: (cargo implied)', 'low', None, 'weak', 1),
 # S009
 ('S009', 'hàng hóa', 'L', 'repetition', 'S008: vận tải hàng hóa', 'high', None, None, 1),
 ('S009', 'thế giới', 'L', 'repetition', 'S001: (world implied)', 'low', None, 'weak', 1),
 # S010
 ('S010', 'một vụ kiện tập thể', 'L', 'repetition', 'S005: vụ kiện', 'high', None, None, 1),
 # S011
 ('S011', 'nhiều bị cáo', 'L', 'repetition', 'S010: vụ kiện tập thể (defendants)', 'med', None, None, 1),
 ('S011', 'vụ này', 'R', 'demonstrative', 'S010: một vụ kiện tập thể', 'high', None, None, 1),
 ('S011', 'vụ kiện của chúng tôi', 'R', 'personal', 'S007: vụ kiện này (Zapala\u2019s)', 'high', None, None, 1),
 # S012
 ('S012', 'Luật sư Zapala', 'L', 'repetition', 'S008: Ông Zapala', 'high', None, None, 1),
 ('S012', 'hành khách', 'L', 'repetition', 'S008: hành khách', 'high', None, None, 1),
 # S013
 ('S013', 'Ông Zapala', 'L', 'repetition', 'S012: Luật sư Zapala', 'high', None, None, 1),
 ('S013', 'hành khách', 'L', 'repetition', 'S012: hành khách', 'high', None, None, 1),
 # S014
 ('S014', 'hành khách', 'L', 'repetition', 'S013: hành khách', 'high', None, 'vụ kiện tập thể ... hành khách', 1),
 ('S014', 'vụ kiện tập thể', 'L', 'repetition', 'S010: một vụ kiện tập thể', 'high', None, None, 1),
 # S015
 ('S015', 'Luật sư Zapala', 'L', 'repetition', 'S013: Ông Zapala', 'high', None, None, 1),
 ('S015', 'lũng đoạn giá vé', 'L', 'repetition', 'S007: điều tra (price-fixing implied)', 'low', None, 'weak', 1),
 # S016
 ('S016', 'Các hãng hàng không', 'L', 'repetition', 'S006: Các hãng', 'high', None, None, 1),
 ('S016', 'định giá vé', 'L', 'repetition', 'S015: lũng đoạn giá vé', 'high', None, None, 1),
 ('S016', 'xuyên Thái Bình Dương', 'L', 'repetition', 'S003: xuyên Thái Bình Dương', 'high', None, None, 1),
 ('S016', 'hành khách', 'L', 'repetition', 'S013: hành khách', 'high', None, None, 1),
 # S017
 ('S017', 'Các tuyến bay', 'L', 'repetition', 'S001: xuyên Thái Bình Dương (routes)', 'med', None, None, 1),
 ('S017', 'vụ kiện này', 'L', 'repetition', 'S011: vụ kiện', 'high', 'R: này', None, 1),
 ('S017', 'Hoa Kỳ', 'L', 'repetition', 'S007: chính phủ Mỹ', 'high', None, None, 1),
 # S018
 ('S018', 'Các hãng hàng không', 'L', 'repetition', 'S016: Các hãng hàng không', 'high', None, None, 1),
 ('S018', 'cáo buộc', 'L', 'repetition', 'S016: thông đồng', 'med', None, None, 1),
 # S019
 ('S019', 'Những hãng vẫn đang bị kiện', 'L', 'repetition', 'S005: 5 hãng máy bay', 'high', None, None, 1),
 # S020
 ('S020', 'Riêng', 'C', 'adversative', 'S019: những hãng vẫn đang bị kiện', 'med', None, None, 1),
 ('S020', 'ANA', 'L', 'repetition', 'S019: All Nippon Airways (ANA)', 'high', None, None, 1),
 ('S020', 'lũng đoạn giá cả', 'L', 'repetition', 'S016: định giá vé', 'med', None, None, 1),
 # S021
 ('S021', 'Những hành khách', 'R', 'demonstrative', 'S003: Hành khách', 'high', None, None, 1),
 ('S021', 'hồ sơ đòi bồi thường', 'L', 'repetition', 'S014: hồ sơ đòi đền bù', 'high', None, None, 1),
 # S022
 ('S022', 'Các thông tin', 'L', 'repetition', 'S021: (info implied)', 'low', None, 'weak', 1),
 ('S022', 'trang web', 'L', 'repetition', 'S021: trên mạng', 'med', None, None, 1),
]

# ---- P20 ----
P20_ST = [
 # S002
 ('S002', 'South Korea', 'L', 'repetition', 'S001: South Korea', 'high', None, None, 1),
 ('S002', 'a "yellow card" warning', 'L', 'repetition', 'S001: "red card"', 'med', None, 'card metaphor chain', 1),
 # S003
 ('S003', 'Continuing violations', 'L', 'repetition', 'S002: (violations implied by warning)', 'med', None, None, 1),
 ('S003', 'South Korean-flagged ships', 'L', 'repetition', 'S002: South Korea', 'high', None, None, 1),
 # S004
 ('S004', 'EU red cards', 'L', 'repetition', 'S001: "red card"', 'high', None, None, 1),
 # S005
 ('S005', 'The red card', 'L', 'repetition', 'S004: EU red cards', 'high', None, None, 1),
 ('S005', 'those countries', 'R', 'demonstrative', 'S004: Belize, Cambodia and Guinea', 'high', None, None, 1),
 ('S005', 'EU countries', 'L', 'repetition', 'S001: the European Union', 'high', None, None, 1),
 # S006
 ('S006', 'illegally caught fish', 'L', 'repetition', 'S001: illegal fishing', 'high', None, None, 1),
 ('S006', 'EU markets', 'L', 'repetition', 'S005: EU countries', 'high', None, None, 1),
 # S007
 ('S007', "It's", 'R', 'personal', 'S005: The red card (the system)', 'med', None, None, 1),
 # S008
 ('S008', 'that', 'R', 'demonstrative', 'S007: showing its teeth', 'high', None, None, 1),
 ('S008', '[South] Korea', 'L', 'repetition', 'S003: South Korean-flagged ships', 'high', None, None, 1),
 # S009
 ('S009', 'We', 'R', 'personal', 'S006: the EJF (quoted speaker)', 'med', None, None, 1),
 ('S009', 'the European Commission', 'L', 'repetition', 'S001: the European Union', 'high', None, None, 1),
 # S010
 ('S010', 'What you have done', 'R', 'personal', 'S009: you haven\u2019t done enough', 'high', None, None, 1),
 # S011
 ('S011', 'you', 'R', 'personal', 'S010: you', 'high', None, None, 1),
 ('S011', 'penalties', 'L', 'repetition', 'S004: were penalized', 'high', None, None, 1),
 # S012
 ('S012', 'the EJF', 'L', 'repetition', 'S006: the Environmental Justice Foundation', 'high', None, 'abbreviation', 1),
 ('S012', 'South Korean ships', 'L', 'repetition', 'S003: South Korean-flagged ships', 'high', None, None, 1),
 # S013
 ('S013', 'The organization', 'L', 'general word', 'S012: the EJF', 'high', None, None, 1),
 ('S013', 'South Korean pirates', 'L', 'repetition', 'S012: South Korean ships', 'high', None, None, 1),
 ('S013', 'fish', 'L', 'repetition', 'S006: illegally caught fish', 'high', None, None, 1),
 # S014
 ('S014', 'It', 'R', 'personal', 'S013: The organization', 'high', None, None, 1),
 ('S014', 'the vessels', 'L', 'repetition', 'S013: South Korean ships', 'high', None, None, 1),
 # S015
 ('S015', 'South Korea', 'L', 'repetition', 'S008: [South] Korea', 'high', None, None, 1),
 ('S015', 'a red card', 'L', 'repetition', 'S005: The red card', 'high', None, None, 1),
 ('S015', 'the EJF', 'L', 'repetition', 'S012: the EJF', 'high', None, None, 1),
 # S016
 ('S016', 'that', 'R', 'demonstrative', 'S015: repercussions beyond maritime commerce', 'med', None, None, 1),
 ('S016', 'brand Korea', 'L', 'repetition', 'S015: South Korea', 'high', None, None, 1),
 # S017
 ('S017', 'This', 'R', 'demonstrative', 'S016: brand Korea gets some damage', 'high', None, None, 1),
 # S018
 ('S018', 'It', 'R', 'personal', 'S017: This (a red card)', 'high', None, None, 1),
 ('S018', 'the country', 'L', 'general word', 'S016: brand Korea', 'high', None, None, 1),
 ('S018', 'he', 'R', 'personal', 'S006: Steve Trent', 'high', None, None, 2),
 # S019
 ('S019', "It's", 'R', 'personal', 'S018: It (the red card)', 'high', None, None, 1),
 # S020
 ('S020', 'that', 'R', 'demonstrative', 'S019: can\u2019t look after their own responsibilities', 'high', None, None, 1),
 ('S020', 'the country', 'L', 'repetition', 'S018: the country', 'high', None, None, 1),
 # S021
 ('S021', 'illegal, unreported and unregulated (IIU) fishing', 'L', 'repetition', 'S001: illegal fishing', 'high', None, None, 1),
 # S022
 ('S022', 'It', 'R', 'personal', 'S021: A new study', 'high', None, None, 1),
 ('S022', 'the tuna', 'L', 'repetition', 'S013: high-value fish (species chain)', 'med', None, None, 1),
 ('S022', 'illegal', 'L', 'repetition', 'S021: illegal, unreported and unregulated', 'high', None, None, 1),
 # S023
 ('S023', 'That', 'R', 'demonstrative', 'S022: 40 percent of the tuna ... illegal', 'high', None, None, 1),
 ('S023', 'salmon imports', 'L', 'repetition', 'S022: the tuna ... imports implied', 'med', None, None, 1),
 # S024
 ('S024', 'The lead author of the report', 'L', 'repetition', 'S021: A new study ... published', 'high', None, None, 1),
 ('S024', 'the Fisheries Center', 'L', 'repetition', 'S001: fisheries (fishing chain)', 'med', None, None, 1),
 # S025
 # S026
 ('S026', 'the amount of manpower', 'L', 'repetition', 'S025: The volumes (quantity chain)', 'med', None, None, 1),
 ('S026', 'illegal catches', 'L', 'repetition', 'S022: illegal', 'high', None, None, 1),
 # S027
 ('S027', 'they', 'R', 'personal', 'S024: (importing countries implied)', 'med', None, None, 1),
 ('S027', 'the manpower', 'L', 'repetition', 'S026: the amount of manpower', 'high', None, None, 1),
 ('S027', 'monitoring, control and surveillance', 'L', 'repetition', 'S013: fisheries patrols', 'med', None, None, 1),
 # S028
 ('S028', 'A 2009 government report', 'L', 'repetition', 'S024: the report', 'high', None, None, 1),
 ('S028', 'seafood imports', 'L', 'repetition', 'S005: their seafood', 'high', None, None, 1),
 # S029
 ('S029', 'public data', 'L', 'repetition', 'S028: government report (data)', 'med', None, None, 1),
 ('S029', 'other major import markets', 'L', 'repetition', 'S028: seafood imports', 'high', None, None, 1),
 # S030
  ('S030', "the 2009 U.N. Food and Agriculture Organization's Port State Measures agreement", 'L', 'repetition', 'S028: A 2009 government report', 'med', None, 'agreement chain', 1),
 # S031
 ('S031', 'It', 'R', 'personal', 'S030: the Port States Measures Agreement', 'high', None, None, 1),
 ('S031', 'foreign vessels', 'L', 'repetition', 'S014: the vessels', 'high', None, None, 1),
 ('S031', 'illegal fishing', 'L', 'repetition', 'S021: illegal ... fishing', 'high', None, None, 1),
 ('S031', 'the ports of nations', 'L', 'repetition', 'S027: their ports', 'high', None, None, 1),
 # S032
 ('S032', 'Ten coastal countries and the EU', 'L', 'repetition', 'S005: EU countries', 'high', None, None, 1),
 ('S032', 'it', 'R', 'personal', 'S031: It (the agreement)', 'high', None, None, 1),
 ('S032', 'similar approval', 'L', 'repetition', 'S030: gave its approval', 'high', None, None, 1),
 # S033
 ('S033', 'The agreement', 'L', 'repetition', 'S030: Port States Measures Agreement', 'high', None, None, 1),
 ('S033', 'illegal fish', 'L', 'repetition', 'S031: illegal fishing', 'high', None, None, 1),
 ('S033', 'the global market', 'L', 'repetition', 'S006: EU markets', 'high', None, None, 1),
 # S034
 ('S034', 'The fisherman', 'L', 'repetition', 'S013: pirates ... fish', 'med', None, None, 1),
 ('S034', 'it', 'R', 'personal', 'S033: illegal fish', 'high', None, None, 1),
 # S035
 ('S035', 'that', 'R', 'demonstrative', 'S034: bring it to port', 'high', None, None, 1),
 ('S035', 'the expensive resources', 'L', 'repetition', 'S027: the manpower (resources)', 'med', None, None, 1),
 # S036
 ('S036', "It's", 'R', 'personal', 'S033: The agreement', 'high', None, None, 1),
 # S037
 ('S037', 'the Port States Measures agreement', 'L', 'repetition', 'S033: The agreement', 'high', None, None, 1),
 ('S037', 'the developing countries', 'L', 'repetition', 'S032: 14 others (countries)', 'med', None, None, 1),
 # S038
 ('S038', 'Long', 'L', 'repetition', 'S033: Long', 'high', None, None, 1),
 ('S038', 'the seafood supply chain', 'L', 'repetition', 'S028: seafood imports', 'high', None, None, 1),
 # S039
 ('S039', 'the system', 'L', 'general word', 'S031-S032: the agreement system', 'med', None, None, 1),
 ('S040', "The U.S., the European Union, Japan, all big markets", 'L', 'repetition', 'S028: the United States + S005: EU countries', 'high', None, None, 1),
 ('S040', 'fishing', 'L', 'repetition', 'S031: illegal fishing', 'high', None, None, 1),
 # S041
 ('S041', 'Long', 'L', 'repetition', 'S038: Long', 'high', None, None, 1),
 ('S041', 'seafood suppliers', 'L', 'repetition', 'S038: the seafood supply chain', 'high', None, None, 1),
 # S042
 ('S042', 'suppliers', 'L', 'repetition', 'S041: seafood suppliers', 'high', None, None, 1),
 ('S042', 'the supply chain', 'L', 'repetition', 'S038: the seafood supply chain', 'high', None, None, 1),
 ('S042', 'that evidence', 'R', 'demonstrative', 'S041: conscientious (evidence implied)', 'med', None, None, 1),
 # S043
 ('S043', "We're", 'R', 'personal', 'S041: Long (quoted speaker)', 'med', None, None, 1),
 ('S043', 'suppliers', 'L', 'repetition', 'S042: suppliers', 'high', None, None, 1),
 ('S043', 'a system', 'L', 'general word', 'S039: the system', 'med', None, None, 1),
 # S044
 ('S044', 'the author of Species Seekers', 'L', 'repetition', 'S024: The lead author of the report', 'med', None, 'author chain', 1),
 # S045
 ('S045', 'The distributors', 'L', 'repetition', 'S042: suppliers (supply chain)', 'high', None, None, 1),
 ('S045', 'Conniff', 'L', 'repetition', 'S044: Richard Conniff', 'high', None, None, 1),
 # S046
 ('S046', "That's", 'R', 'demonstrative', 'S045: The distributors are the bottleneck', 'high', None, None, 1),
 ('S046', 'most of the (sea)food', 'L', 'repetition', 'S045: distributors (seafood chain)', 'med', None, None, 1),
 ('S046', 'this country', 'R', 'demonstrative', 'S028: the United States', 'high', None, None, 1),

]

P20_ST = P20_ST + [
 # S047
 ('S047', 'they', 'R', 'personal', 'S040: the U.S., the European Union, Japan', 'med', None, None, 1),
 ('S047', 'it', 'R', 'personal', 'S040: the shape of fishing', 'med', None, None, 1),
 # S048
 ('S048', 'Ganapathiraju', 'L', 'repetition', 'S024: Pramod Ganapathiraju', 'high', None, None, 1),
 ('S048', 'his research', 'R', 'personal', 'S024: a researcher', 'med', None, None, 1),
 ('S048', 'distributors', 'L', 'repetition', 'S045: The distributors', 'high', None, None, 1),
 # S049
 ('S049', 'The catches', 'L', 'repetition', 'S026: illegal catches', 'high', None, None, 1),
 # S051
 ('S051', 'the demand', 'L', 'repetition', 'S050: the demand', 'high', None, None, 1),
 ('S051', 'over-fishing', 'L', 'repetition', 'S049: catches are being depleted', 'med', None, None, 1),
 ('S051', 'illegal', 'L', 'repetition', 'S021: illegal, unreported and unregulated', 'high', None, None, 1),
 # S052
 ('S052', "That's", 'R', 'demonstrative', 'S049-S051: depletion and rising demand', 'high', None, None, 1),
 ('S052', "they're", 'R', 'personal', 'S051: they\u2019re', 'med', None, None, 1),
 # S053
 ('S053', "the EJF's Steve Trent", 'L', 'repetition', 'S006: Steve Trent', 'high', None, None, 1),
 ('S053', 'China', 'L', 'repetition', 'S023: China', 'high', None, None, 1),
 ('S053', 'seafood', 'L', 'repetition', 'S005: their seafood', 'high', None, None, 1),
 # S054
 ('S054', 'the Chinese government', 'L', 'repetition', 'S053: China', 'high', None, None, 1),
 ('S054', 'fisheries', 'L', 'repetition', 'S024: the Fisheries Center', 'med', None, None, 1),
 ('S054', 'global platform', 'L', 'repetition', 'S033: the global market', 'med', None, None, 1),
 # S055
 ('S055', 'Conniff', 'L', 'repetition', 'S045: Conniff', 'high', None, None, 1),
 ('S055', 'China and other nations', 'L', 'repetition', 'S053-S054: China', 'high', None, None, 1),
 ('S055', 'changes', 'L', 'repetition', 'S029: (regulatory changes implied)', 'med', None, None, 1),
 # S056
 ('S056', 'China', 'L', 'repetition', 'S055: China', 'high', None, None, 1),
 ('S056', 'all these other countries', 'R', 'demonstrative', 'S055: other nations', 'high', None, None, 1),
 ('S056', 'change', 'L', 'repetition', 'S055: changes', 'high', None, None, 1),
 # S057
 ('S057', 'regulatory changes', 'L', 'repetition', 'S055: changes', 'med', None, None, 1),
 # S058
 ('S058', 'vessels', 'L', 'repetition', 'S031: foreign vessels', 'high', None, 'Fishing vessels', 1),
 # S059
 ('S059', 'vessel', 'L', 'repetition', 'S058: vessels', 'high', None, None, 1),
 ('S059', 'monitoring', 'L', 'repetition', 'S027: monitoring, control and surveillance', 'high', None, None, 1),
 # S060
 ('S060', 'It', 'R', 'personal', 'S059: a global satellite vessel monitoring system', 'high', None, None, 1),
 ('S060', 'vessels', 'L', 'repetition', 'S059: vessel', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_20 (§2) ----
 ('S005', None, 'E', 'verbal', 'S005: {can they sell} (trong câu)', 'high', None, '[TC] nor + ∅ trợ động từ: “nor ∅ fish in member countries’ waters”', 1, 'in EU countries nor ', '{can they sell}', 'TC'),
 ('S035', None, 'E', 'nominal', 'S035: {we need} (trong câu)', 'med', None, '[TC] chủ ngữ rỗng trong quote: “Therefore ∅ to focus on that…”', 1, 'Therefore ', '{we need}', 'TC'),
 ('S056', None, 'E', 'verbal', 'S056: {they need} (trong câu)', 'med', None, '[TC] lặp to + ∅: “to change and ∅ to change fast” (khối EN bị VI cắt)', 1, 'to change and ', '{they need}', 'TC'),
]

P20_TT = [
 # S002
 ('S002', 'Điều này', 'R', 'demonstrative', 'S001: bị cấm bán hải sản', 'high', None, None, 1),
 ('S002', 'Liên hiệp Châu Âu', 'L', 'repetition', 'S001: Châu Âu', 'high', None, None, 1),
 # S003
 ('S003', 'Vấn đề này', 'R', 'demonstrative', 'S001-S002: the EU crackdown', 'high', None, None, 1),
 ('S003', 'Hoa Kỳ', 'L', 'repetition', 'S001: (none)', 'low', None, 'first overt mention; weak', 1),
 # S004
 ('S004', 'Liên hiệp Châu Âu', 'L', 'repetition', 'S002: Liên hiệp Châu Âu', 'high', None, None, 1),
 ('S004', 'Nam Triều Tiên', 'L', 'repetition', 'S001: Nam Triều Tiên', 'high', None, None, 1),
 # S005
 ('S005', 'Nam Triều Tiên', 'L', 'repetition', 'S004: Nam Triều Tiên', 'high', None, None, 1),
 ('S005', '\u201cthẻ vàng\u201d', 'L', 'repetition', 'S004: \u201cthẻ đỏ\u201d', 'med', None, 'card metaphor chain', 1),
 # S006
 ('S006', 'Nam Triều Tiên', 'L', 'repetition', 'S005: Nam Triều Tiên', 'high', None, None, 1),
 # S007
 ('S007', 'thẻ đỏ', 'L', 'repetition', 'S004: \u201cthẻ đỏ\u201d', 'high', None, None, 1),
 # S008
 ('S008', 'đánh bắt bất hợp pháp', 'L', 'repetition', 'S007: đánh cá trộm', 'high', None, 'synonym', 1),
 # S009
 ('S009', 'EU', 'L', 'repetition', 'S004: Liên hiệp Châu Âu', 'high', None, 'abbreviation', 1),
 # S010
 ('S010', 'đó', 'R', 'demonstrative', 'S009: đưa ra những lời đe dọa', 'high', None, None, 1),
 ('S010', 'Nam Triều Tiên', 'L', 'repetition', 'S006: Nam Triều Tiên', 'high', None, None, 1),
 # S011
 ('S011', 'Chúng ta', 'R', 'personal', 'S008: Ông Steve Trent (quoted speaker)', 'med', None, None, 1),
 ('S011', 'Ủy hội Âu châu', 'L', 'repetition', 'S009: EU', 'high', None, None, 1),
 # S012
 ('S012', 'chúng tôi', 'R', 'personal', 'S011: Chúng ta', 'med', None, 'speaker chain', 1),
 # S013
 ('S013', 'trừng phạt', 'L', 'repetition', 'S002: truy dẹp', 'med', None, None, 1),
 # S014
 ('S014', 'Tổ chức Tư pháp Môi trường', 'L', 'repetition', 'S008: Tổ chức Tư pháp Môi trường', 'high', None, None, 1),
 ('S014', 'tàu thuyền Nam Triều Tiên', 'L', 'repetition', 'S006: tàu thuyền treo cờ Nam Triều Tiên', 'high', None, None, 1),
 ('S014', 'đánh bắt', 'L', 'repetition', 'S008: đánh bắt bất hợp pháp', 'high', None, None, 1),
 # S015
 ('S015', 'Tổ chức này', 'L', 'repetition', 'S014: Tổ chức Tư pháp Môi trường', 'high', 'R: này', None, 1),
 ('S015', 'Nam Triều Tiên', 'L', 'repetition', 'S014: Nam Triều Tiên', 'high', None, None, 1),
 ('S015', 'đánh trộm cá', 'L', 'repetition', 'S007: đánh cá trộm', 'high', None, None, 1),
 # S016
 ('S016', 'Tổ chức này', 'L', 'repetition', 'S015: Tổ chức này', 'high', 'R: này', None, 1),
 ('S016', 'tàu thuyền', 'L', 'repetition', 'S014: tàu thuyền', 'high', None, None, 1),
 # S017
 ('S017', 'Một cuộc nghiên cứu mới', 'L', 'repetition', 'S003: một cuộc nghiên cứu mới', 'high', None, 'echo of the lede', 1),
 ('S017', 'đánh bắt bất hợp pháp', 'L', 'repetition', 'S014: đánh bắt', 'high', None, None, 1),
 # S018
 ('S018', 'Cuộc nghiên cứu này', 'L', 'repetition', 'S017: một cuộc nghiên cứu mới', 'high', 'R: này', None, 1),
 ('S018', 'bất hợp pháp', 'L', 'repetition', 'S017: bất hợp pháp', 'high', None, None, 1),
 # S019
 ('S019', 'Đây', 'R', 'demonstrative', 'S018: 40% cá ngừ bất hợp pháp', 'high', None, None, 1),
 ('S019', 'nhập khẩu', 'L', 'repetition', 'S003: nhập khẩu', 'high', None, None, 1),
 # S020
 ('S020', 'bản phúc trình', 'L', 'repetition', 'S017: nghiên cứu', 'med', None, 'report ~ study', 1),
 # S021
 ('S021', 'Ông', 'R', 'personal', 'S020: ông Pramod Ganapathiraju', 'high', None, None, 1),
 ('S021', 'Hoa Kỳ', 'L', 'repetition', 'S003: Hoa Kỳ', 'high', None, None, 1),
 ('S021', 'thị trường nhập khẩu hải sản', 'L', 'repetition', 'S003: hải sản nhập khẩu', 'high', None, None, 1),
 ('S021', 'Liên hiệp Châu Âu', 'L', 'repetition', 'S011: Ủy hội Âu châu', 'high', None, None, 1),
 ('S021', 'Trung Quốc', 'L', 'repetition', 'S019: Trung Quốc', 'high', None, None, 1),
 # S023
 ('S023', 'hải sản đánh bắt bất hợp pháp', 'L', 'repetition', 'S017: đánh bắt bất hợp pháp', 'high', None, None, 1),
 ('S023', 'thị trường', 'L', 'repetition', 'S021: thị trường nhập khẩu', 'high', None, None, 1),
 # S024
 ('S024', 'những quốc gia này', 'R', 'demonstrative', 'S021: thị trường nhập khẩu (countries)', 'high', None, None, 1),
 ('S024', 'nhân lực', 'L', 'repetition', 'S023: nhân lực', 'high', None, None, 1),
 # S025
 ('S025', 'phúc trình', 'L', 'repetition', 'S020: bản phúc trình', 'high', None, None, 1),
 ('S025', 'hải sản', 'L', 'repetition', 'S023: hải sản', 'high', None, None, 1),
 ('S025', 'Hoa Kỳ', 'L', 'repetition', 'S021: Hoa Kỳ', 'high', None, None, 1),
 # S026
 ('S026', 'thị trường nhập khẩu', 'L', 'repetition', 'S021: thị trường nhập khẩu hải sản', 'high', None, None, 1),
 # S027
 ('S027', 'Thượng viện Hoa Kỳ', 'L', 'repetition', 'S025: Hoa Kỳ', 'high', None, None, 1),
 # S028
 ('S028', 'Thỏa thuận này', 'L', 'repetition', 'S027: thỏa thuận', 'high', 'R: này', None, 1),
 ('S028', 'tàu thuyền nước ngoài', 'L', 'repetition', 'S016: tàu thuyền', 'high', None, None, 1),
 ('S028', 'đánh bắt bất hợp pháp', 'L', 'repetition', 'S023: hải sản đánh bắt bất hợp pháp', 'high', None, None, 1),
 ('S028', 'cảng', 'L', 'repetition', 'S024: cảng', 'high', None, None, 1),
 # S029
 ('S029', 'EU', 'L', 'repetition', 'S011: Ủy hội Âu châu', 'high', None, None, 1),
 ('S029', 'phê chuẩn', 'L', 'synonym', 'S027: chấp thuận', 'high', None, None, 1),
 ('S029', 'hiệp ước', 'L', 'repetition', 'S027: thỏa thuận', 'med', None, None, 1),
 # S030
 ('S030', 'thỏa thuận', 'L', 'repetition', 'S028: Thỏa thuận này', 'high', None, None, 1),
 ('S030', 'Đánh bắt bất hợp pháp', 'L', 'repetition', 'S028: đánh bắt bất hợp pháp', 'high', None, None, 1),
 # S031
 ('S031', 'Ngư dân', 'L', 'repetition', 'S016: ngư dân', 'high', None, None, 1),
 ('S031', 'cá', 'L', 'repetition', 'S015: đánh trộm cá', 'high', None, None, 1),
 ('S031', 'cảng', 'L', 'repetition', 'S028: cảng', 'high', None, None, 1),
 # S032
 ('S032', 'việc này', 'R', 'demonstrative', 'S031: đưa cá vào cảng', 'high', None, None, 1),
 ('S032', 'tuần tra', 'L', 'repetition', 'S015: tàu tuần', 'high', None, 'morphological reiteration', 1),
 # S033
 ('S033', 'Việc này', 'R', 'demonstrative', 'S032: nguồn lực tốn kém', 'med', None, None, 1),
 # S034
 ('S034', 'thỏa thuận', 'L', 'repetition', 'S030: thỏa thuận', 'high', None, None, 1),
 ('S034', 'Biện pháp tại Cảng các Quốc gia', 'L', 'repetition', 'S027: thỏa thuận các Biện pháp tại Cảng', 'high', None, None, 1),
 # S035
 ('S035', 'người Mỹ', 'L', 'repetition', 'S003: Hoa Kỳ', 'med', None, None, 1),
 # S037
 ('S037', 'Đó', 'R', 'demonstrative', 'S036: nơi gây tắc nghẽn', 'high', None, None, 1),
 ('S037', 'hải sản', 'L', 'repetition', 'S025: hải sản', 'high', None, None, 1),
 ('S037', 'nước này', 'R', 'demonstrative', 'S021: Hoa Kỳ', 'high', None, None, 1),
 # S038
 ('S038', 'họ', 'R', 'personal', 'S036: Các nhà phân phối', 'high', None, None, 1),
 ('S038', 'ấy', 'R', 'demonstrative', 'S036: tắc nghẽn (the bottleneck)', 'med', None, None, 1),
 # S039
 ('S039', 'Tổ chức Tư pháp Môi trường', 'L', 'repetition', 'S014: Tổ chức Tư pháp Môi trường', 'high', None, None, 1),
 ('S039', 'Trung Quốc', 'L', 'repetition', 'S021: Trung Quốc', 'high', None, None, 1),
 ('S039', 'hải sản', 'L', 'repetition', 'S037: hải sản', 'high', None, None, 1),
 # S040
 ('S040', 'chính phủ Trung Quốc', 'L', 'repetition', 'S039: Trung Quốc', 'high', None, None, 1),
 ('S040', 'đánh cá', 'L', 'repetition', 'S031: cá', 'high', None, 'morphological reiteration', 1),
 # S041
 ('S041', 'đánh bắt bất hợp pháp', 'L', 'repetition', 'S030: Đánh bắt bất hợp pháp', 'high', None, None, 1),
 # S042
 ('S042', 'đánh cá', 'L', 'repetition', 'S040: đánh cá', 'high', None, None, 1),
 # S043
 ('S043', 'theo dõi', 'L', 'repetition', 'S024: theo dõi, kiểm soát và giám sát', 'high', None, None, 1),
 ('S043', 'tàu thuyền', 'L', 'repetition', 'S028: tàu thuyền', 'high', None, None, 1),
 # S044
 ('S044', 'Hệ thống này', 'L', 'repetition', 'S043: hệ thống theo dõi', 'high', 'R: này', None, 1),
 ('S044', 'theo dõi', 'L', 'repetition', 'S043: theo dõi', 'high', None, None, 1),
 ('S044', 'tàu', 'L', 'repetition', 'S043: tàu thuyền', 'high', None, None, 1),
 ('S044', 'nhận diện', 'L', 'repetition', 'S042: số hiệu nhận diện', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_20 (§2) ----
 ('S032', None, 'E', 'nominal', 'S032: {chúng ta} (trong câu)', 'med', None, '[TC] chủ ngữ rỗng trong quote: “Do đó ∅ cần chú trọng…” — copy 1–1 E-EN2', 1, 'Do đó ', '{chúng ta}', 'TC'),

]
