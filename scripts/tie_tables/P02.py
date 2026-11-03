# P02 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'homeless', 'L', 'repetition', 'S001: homelessness', 'high', None, 'morphological reiteration', None),
 # S003
 ('S003', 'She', 'R', 'personal', 'S002: Tyrah Chan-Hampton', 'high', None, None, None),
 ('S003', 'she', 'R', 'personal', 'S002: Tyrah Chan-Hampton', 'high', None, None, None),
 ('S003', 'her', 'R', 'personal', 'S002: Tyrah Chan-Hampton', 'high', None, None, 1),
 # S004
 ('S004', 'They', 'R', 'personal', 'S003: she ... her aunt', 'high', None, 'plural: Tyrah and her aunt', None),
 ('S004', 'homelessness', 'L', 'repetition', 'S001: homelessness', 'high', None, None, None),
 ('S004', 'she', 'R', 'personal', 'S003: She (Tyrah)', 'high', None, None, None),
 ('S004', 'her', 'R', 'personal', 'S002: Tyrah Chan-Hampton', 'high', None, None, 2),
 # S005
 ('S005', 'She', 'R', 'personal', 'S004: she (Tyrah)', 'high', None, None, None),
 ('S005', 'she', 'R', 'personal', 'S004: she (Tyrah)', 'high', None, None, None),
 ('S005', 'homelessness', 'L', 'repetition', 'S004: homelessness', 'high', None, None, None),
 ('S005', 'housing insecurity', 'L', 'repetition', 'S002: housing insecurity', 'high', None, None, None),
 # S006
 ('S006', 'it', 'R', 'personal', 'S005: felt embarrassed (the feeling)', 'low', None, 'vague it', 2),
 ('S006', 'it', 'R', 'personal', 'S002: the word homeless', 'med', None, None, 3),
 ('S006', 'I', 'R', 'personal', 'S005: She said (Tyrah, quoted speaker)', 'med', None, 'first person in quote', None),
 ('S006', 'she', 'R', 'personal', 'S005: She (Tyrah)', 'high', None, None, None),
 # S007
 ('S007', 'family', 'L', 'repetition', 'S004: extended family', 'med', None, None, None),
 ('S007', 'cousins', 'L', 'repetition', 'S004: sister and cousin', 'med', None, None, None),
 ('S007', 'she', 'R', 'personal', 'S006: she (Tyrah)', 'high', None, None, None),
 # S008
 ('S008', 'we', 'R', 'personal', 'S002: Tyrah Chan-Hampton (quoted speaker)', 'med', None, 'first person in quote; my/me/us same chain, one mark', None),
 ('S008', 'homelessness', 'L', 'repetition', 'S005: homelessness', 'high', None, None, 1),
 ('S008', 'stigma', 'L', 'repetition', 'S005: the stigma', 'high', None, None, 1),
 ('S008', 'shame', 'L', 'repetition', 'S006: shame', 'high', None, None, 1),
 # S009
 ('S009', 'homelessness', 'L', 'repetition', 'S008: homelessness', 'high', None, None, None),
 # S010
 ('S010', 'And', 'C', 'additive', 'S009: ABS statistic', 'med', None, 'sentence-initial additive', None),
 ('S010', 'homelessness', 'L', 'repetition', 'S009: homelessness', 'high', None, None, 1),
 ('S010', 'people', 'L', 'repetition', 'S009: 122,000 people', 'med', None, None, 1),
 # S011
 ('S011', 'New analysis', 'L', 'repetition', 'S001: New analysis', 'high', None, None, None),
 ('S011', 'people', 'L', 'repetition', 'S010: 38,600 people', 'med', None, None, 1),
 ('S011', 'homelessness', 'L', 'repetition', 'S010: homelessness services', 'high', None, None, 1),
 ('S011', 'identified the 20 hotspots across the country', 'L', 'repetition', 'S001: identified the top 20 hotspots across the country', 'high', None, 'near-verbatim self-echo', None),
 ('S011', 'struggling to find a place to live', 'L', 'repetition', 'S001: struggling to find a place to live', 'high', None, 'verbatim', None),
 # S012
 ('S012', 'list', 'L', 'general word', 'S011: the 20 hotspots', 'med', 'R: the', 'general word for the ranking', None),
 ('S012', 'young people', 'L', 'repetition', 'S001: young people', 'high', None, None, None),
 ('S012', 'homelessness', 'L', 'repetition', 'S011: homelessness', 'high', None, None, None),
 # S013
 ('S013', 'top five', 'L', 'repetition', 'S012: topped the list / S001: top 20', 'med', None, 'reiteration of top', None),
 # S014
 ('S014', 'Areas', 'L', 'general word', 'S012-S013: the listed regions', 'med', None, None, None),
 ('S014', 'the top 20', 'L', 'repetition', 'S001: the top 20 / S011: the 20 hotspots', 'high', None, None, None),
 # S015
 ('S015', 'Foyer Foundation', 'L', 'repetition', 'S011: the Foyer Foundation', 'high', None, None, None),
 ('S015', 'analysis', 'L', 'repetition', 'S011: New analysis', 'high', None, None, None),
 ('S015', 'young people', 'L', 'repetition', 'S012: young people', 'high', None, None, None),
 ('S015', 'homelessness', 'L', 'repetition', 'S012: homelessness', 'high', None, None, None),
 # S016
 ('S016', 'we', 'R', 'personal', 'S015: Corin Moffatt (quoted speaker)', 'med', None, 'institutional we', 1),
 ('S016', 'we', 'R', 'personal', 'S015: Corin Moffatt', 'med', None, None, 2),
 ('S016', 'list', 'L', 'repetition', 'S012: the list', 'high', 'R: that', None, None),
 ('S016', 'areas', 'L', 'repetition', 'S014: Areas', 'high', None, None, None),
 ('S016', 'that', 'R', 'demonstrative', 'S015: unemployment and school-completion rates', 'med', None, 'that combination of challenges', 3),
 ('S016', 'young people', 'L', 'repetition', 'S015: young people', 'high', None, None, None),
 ('S016', 'she', 'R', 'personal', 'S015: Corin Moffatt', 'high', None, None, None),
 # S017
 ('S017', 'We', 'R', 'personal', 'S016: we (Moffat)', 'med', None, None, None),
 ('S017', 'areas', 'L', 'repetition', 'S016: areas', 'high', None, None, None),
 ('S017', 'it', 'R', 'personal', 'S016: that list', 'med', None, 'what it shows', 3),
 ('S017', 'problem', 'L', 'general word', 'S016: challenges for young people', 'med', None, 'the problem', None),
 ('S017', 'young people', 'L', 'repetition', 'S016: young people', 'high', None, None, None),
 ('S017', 'challenges', 'L', 'repetition', 'S016: challenges', 'high', 'R: these', None, None),
 # S018
 ('S018', 'Moffat', 'L', 'repetition', 'S016: she (Moffat)', 'high', None, 'subject reintroduction', None),
 ('S018', 'youth homelessness', 'L', 'repetition', 'S015: youth ... homelessness', 'high', None, None, None),
 ('S018', 'domestic violence', 'L', 'repetition', 'S008: domestic violence', 'high', None, None, None),
 ('S018', 'housing', 'L', 'repetition', 'S005: housing insecurity', 'med', None, 'affordable housing', None),
 # S019
 ('S019', 'housing', 'L', 'repetition', 'S018: affordable housing', 'med', None, None, None),
 ('S019', 'young people', 'L', 'repetition', 'S018: youth homelessness', 'high', None, None, None),
 ('S019', 'struggle', 'L', 'repetition', 'S011: struggling to find a place to live', 'med', None, None, None),
 ('S019', 'she', 'R', 'personal', 'S018: Moffat', 'high', None, None, None),
 # S020
 ('S020', 'young people', 'L', 'repetition', 'S019: young people', 'high', None, None, 1),
 ('S020', 'school', 'L', 'repetition', 'S015: finishing high school', 'med', None, None, None),
 ('S020', 'factors', 'L', 'repetition', 'S018: several factors', 'high', 'R: those', None, None),
 ('S020', 'young people', 'L', 'repetition', 'S019: young people', 'high', None, None, 2),
 # S021
 ('S021', 'Now', 'C', 'temporal', 'S020: current situation; shift to call for action', 'med', None, None, None),
 ('S021', 'Foyer', 'L', 'repetition', 'S015: Foyer Foundation', 'high', None, None, None),
 ('S021', 'youth foyers', 'L', 'repetition', 'S015: Foyer Foundation', 'med', None, 'foyer reiteration from org name', None),
 ('S021', 'housing', 'L', 'repetition', 'S019: housing', 'med', None, 'medium-term housing', None),
 ('S021', 'young people', 'L', 'repetition', 'S020: young people', 'high', None, None, None),
 ('S021', 'homelessness', 'L', 'repetition', 'S018: youth homelessness', 'high', None, None, None),
 # S022
 ('S022', 'Youth foyers', 'L', 'repetition', 'S021: youth foyers', 'high', None, None, None),
 ('S022', 'housing', 'L', 'repetition', 'S021: medium-term housing', 'med', None, 'transitional housing', None),
 ('S022', 'people', 'L', 'repetition', 'S021: young people', 'med', None, 'people aged 16 to 25', None),
 ('S022', 'accommodation', 'L', 'repetition', 'S020: safe and secure accommodation', 'med', None, 'stable accommodation', None),
 # S023
 ('S023', 'Moffat', 'L', 'repetition', 'S019: she (Moffat)', 'high', None, None, None),
 ('S023', 'young people', 'L', 'repetition', 'S022: people aged 16 to 25', 'high', None, None, None),
 ('S023', 'support', 'L', 'repetition', 'S022: support pursuing education', 'med', None, None, 1),
 # S024
 ('S024', 'crisis services', 'L', 'repetition', 'S023: crisis centres ... support services', 'high', None, None, None),
 ('S024', 'young people', 'L', 'repetition', 'S023: young people', 'high', None, None, None),
 ('S024', 'also', 'C', 'additive', 'S023: not enough ongoing support', 'med', None, None, None),
 ('S024', 'medium and longer-term housing', 'L', 'repetition', 'S021: medium-term housing', 'high', None, None, None),
 ('S024', 'she', 'R', 'personal', 'S023: Moffat', 'high', None, None, None),
 # S025
 ('S025', 'And so', 'C', 'causal', 'S024: not enough services', 'med', None, None, None),
 ('S025', 'we', 'R', 'personal', 'S024: she (Moffat)', 'med', None, None, None),
 ('S025', 'young people', 'L', 'repetition', 'S024: young people', 'high', None, None, None),
 ('S025', 'crisis services', 'L', 'repetition', 'S024: crisis services', 'high', None, None, None),
 ('S025', 'pathway', 'L', 'repetition', 'S021: a pathway out of homelessness', 'high', None, None, None),
 ('S025', 'system', 'L', 'general word', 'S023-S024: crisis and support services', 'med', None, 'the system', None),
 # S026
 ('S026', 'youth homelessness', 'L', 'repetition', 'S018: youth homelessness', 'high', None, None, None),
 # S027
 ('S027', 'He', 'R', 'personal', 'S026: David MacKenzie', 'high', None, None, None),
 ('S027', 'also', 'C', 'additive', 'S021-S025: foyers and support', 'med', None, None, None),
 ('S027', 'housing', 'L', 'repetition', 'S024: housing options', 'med', None, 'housing assistance', None),
 ('S027', 'support', 'L', 'repetition', 'S023: support', 'med', None, None, 1),
 ('S027', 'schools', 'L', 'repetition', 'S020: finish school', 'med', None, None, None),
 # S028
 ('S028', 'prevention', 'L', 'repetition', 'S027: prevention', 'high', None, None, None),
 ('S028', 'he', 'R', 'personal', 'S027: He (MacKenzie)', 'high', None, None, 3),
 # S029
 ('S029', 'we', 'R', 'personal', 'S028: he (MacKenzie, quoted speaker)', 'med', None, None, None),
 ('S029', 'prevent', 'L', 'repetition', 'S027: prevention', 'high', None, None, None),
 ('S029', 'it', 'R', 'personal', 'S026: youth homelessness', 'med', None, None, None),
 ('S029', 'people', 'L', 'repetition', 'S022: people', 'med', None, None, 1),
 ('S029', 'young people', 'L', 'repetition', 'S027: young people', 'high', None, None, None),
 ('S029', 'homelessness', 'L', 'repetition', 'S026: youth homelessness', 'high', None, None, None),
 ('S029', 'problem', 'L', 'repetition', 'S017: the problem', 'med', None, None, None),
 # S030
 ('S030', 'MacKenzie', 'L', 'repetition', 'S029: we (MacKenzie)', 'high', None, None, None),
 ('S030', 'homelessness', 'L', 'repetition', 'S029: homelessness', 'high', None, None, None),
 # S031
 ('S031', 'support', 'L', 'repetition', 'S027: support', 'med', None, None, None),
 ('S031', 'he', 'R', 'personal', 'S030: MacKenzie', 'high', None, None, 6),
 # S032
 ('S032', 'Chan-Hampton', 'L', 'repetition', 'S002: Tyrah Chan-Hampton', 'high', None, 'reintroduction after absence', None),
 # S033
 ('S033', 'She', 'R', 'personal', 'S032: Chan-Hampton', 'high', None, None, 1),
 ('S033', 'her', 'R', 'personal', 'S032: Chan-Hampton', 'high', None, None, 1),
 ('S033', 'youth foyer', 'L', 'repetition', 'S022: Youth foyers', 'high', None, None, None),
 ('S033', 'two years', 'L', 'repetition', 'S022: up to two years', 'med', None, None, None),
 ('S033', 'her', 'R', 'personal', 'S032: Chan-Hampton', 'high', None, None, 2),
 # S034
 ('S034', 'support services', 'L', 'repetition', 'S023: emergency support services', 'high', None, None, None),
 ('S034', 'she', 'R', 'personal', 'S033: She (Tyrah)', 'high', None, None, None),
 ('S034', 'young people', 'L', 'repetition', 'S029: young people', 'high', None, None, None),
 ('S034', 'housing', 'L', 'repetition', 'S027: housing', 'med', None, 'secure housing', None),
 # S035
 ('S035', 'People', 'L', 'repetition', 'S034: young people', 'med', None, None, None),
 ('S035', 'unsafe environments', 'L', 'repetition', 'S034: unstable or unsafe environments', 'high', None, None, None),
 ('S035', 'she', 'R', 'personal', 'S034: she (Tyrah)', 'high', None, None, None),
 # S036
 ('S036', 'young people', 'L', 'repetition', 'S035: People', 'high', None, None, None),
 ('S036', 'crisis accommodation', 'L', 'repetition', 'S022: accommodation / S024: crisis services', 'med', None, None, None),
 # S037
 ('S037', 'homelessness', 'L', 'repetition', 'S034: homelessness', 'high', None, None, 1),
 ('S037', 'housing', 'L', 'repetition', 'S034: housing', 'med', None, None, None),
 ('S037', 'long-term', 'L', 'repetition', 'S024: longer-term / S031: long-term', 'med', None, None, None),
 # S038
 ('S038', 'government', 'L', 'repetition', 'S021: the government', 'high', None, None, None),
 ('S038', 'housing and homelessness', 'L', 'repetition', 'S037: housing and homelessness', 'high', None, None, None),
 ('S038', 'spokesperson', 'L', 'repetition', 'S037: a Department of Social Services spokesperson', 'high', None, None, None),
 # S039
 ('S039', 'this', 'R', 'demonstrative', 'S038: reform agenda', 'high', None, 'As part of this', None),
 ('S039', 'government', 'L', 'repetition', 'S038: The government', 'high', None, None, None),
 ('S039', 'homeless', 'L', 'repetition', 'S037: homelessness', 'high', None, None, None),
 ('S039', 'people', 'L', 'repetition', 'S035: People', 'med', None, None, None),
 ('S039', 'support', 'L', 'repetition', 'S034: support services', 'med', None, None, None),
 # S040
 ('S040', 'This', 'R', 'demonstrative', 'S039: significant investments', 'high', None, None, None),
 ('S040', 'young people', 'L', 'repetition', 'S036: young people', 'high', None, None, None),
 ('S040', 'homelessness', 'L', 'repetition', 'S039: homelessness', 'high', None, None, None),
 # S041
 ('S041', 'The spokesperson', 'L', 'repetition', 'S038: the spokesperson', 'high', None, None, None),
 ('S041', 'government', 'L', 'repetition', 'S039: the government', 'high', None, None, None),
 ('S041', 'Housing and Homelessness', 'L', 'repetition', 'S038: housing and homelessness', 'high', None, 'embedded in proper name', None),
 ('S041', 'people', 'L', 'repetition', 'S039: people', 'med', None, None, None),
 ('S041', 'homelessness', 'L', 'repetition', 'S040: homelessness', 'high', None, None, 1),
 # S042
 ('S042', 'They', 'R', 'personal', 'S041: The spokesperson', 'high', None, 'plural for singular (source usage)', None),
 ('S042', 'government', 'L', 'repetition', 'S041: the government', 'high', None, None, None),
 ('S042', 'also', 'C', 'additive', 'S041: $9.3 billion provision', 'med', None, None, None),
 ('S042', 'youth homelessness', 'L', 'repetition', 'S041: Homelessness', 'high', None, None, None),
 ('S042', 'prevention', 'L', 'repetition', 'S028: prevention', 'high', None, None, 1),
 # S043
 ('S043', 'They', 'R', 'personal', 'S042: They (the spokesperson)', 'high', None, None, None),
 ('S043', 'Housing', 'L', 'repetition', 'S041: Housing', 'med', None, 'embedded in proper name', None),
 ('S043', 'also', 'C', 'additive', 'S042: also investing', 'med', None, None, None),
 ('S043', 'support', 'L', 'repetition', 'S039: support', 'med', None, None, None),
 ('S043', 'crisis and transitional accommodation', 'L', 'repetition', 'S036: crisis accommodation / S022: transitional housing', 'med', None, None, None),
 ('S043', 'domestic violence', 'L', 'repetition', 'S018: domestic violence', 'high', None, None, None),
 ('S043', 'youth', 'L', 'repetition', 'S042: youth homelessness', 'med', None, None, None),
 ('S043', 'homelessness', 'L', 'repetition', 'S042: youth homelessness', 'high', None, None, None),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_02 (§2–§3) ----
 # [LC] = liên câu; [TC] = trong câu. Các dòng này KHÔNG do script sinh:
 # người đọc bản phân tích ngữ nghĩa rồi chọn đúng vị trí/tiền trạm.
 ('S003', None, 'E', 'nominal', 'S003: {she} (trong câu)', 'high', None, '[TC] lược chủ ngữ vế tọa hợp thứ hai: “she was 11 and ∅ was placed…”; EN verb coordination', 1, 'when she was 11 and ', '{she}', 'TC'),
 ('S019', None, 'E', 'clausal', 'S019: {are struggling to afford housing} (trong câu)', 'high', None, '[TC] “let alone” stripping: lược vị ngữ {are struggling to afford housing}, chỉ giữ NP đối chiếu', 1, 'let alone young people', '{are struggling to afford housing}', 'TC'),
 ('S031', None, 'E', 'verbal', 'S031: {there’s} (trong câu)', 'high', None, '[TC] lược “there’s” ở vế 2 của chuỗi điệp “no one…”; gap còn lại trước “no one to help you get…”', 1, 'there to help you, ', '{there’s}', 'TC'),
 ('S032', None, 'E', 'nominal', 'S002: Tyrah Chan-Hampton (người được nhắc lại ở đầu câu)', 'high', None, '[LC] đồng vị ngữ rút gọn: {She is} now 23; chỗ trống ở đầu câu nên gap_after rỗng', 1, '', '{She is}', 'LC'),
 ('S036', None, 'E', 'nominal', 'S036: {a place} (trong câu)', 'low', None, '[TC] biên tỉnh lược/quy chiếu: lược bổ ngữ địa điểm của “to go to ∅”; EN: nothing available … to go to', 1, 'to go to', '{a place}', 'TC'),
]

TT = [
 # S002
 ('S002', 'vô gia cư', 'L', 'repetition', 'S001: tình trạng vô gia cư', 'high', None, None, 1),
 # S003
 ('S003', 'Cô', 'R', 'personal', 'S002: Tyrah Chan-Hampton', 'high', None, None, None),
 # S004
 ('S004', 'Cả hai', 'R', 'personal', 'S003: cô ... dì', 'med', None, 'quantified reference (both = she and her aunt)', None),
 ('S004', 'vô gia cư', 'L', 'repetition', 'S002: vô gia cư', 'high', None, None, 1),
 ('S004', 'cô', 'R', 'personal', 'S003: Cô (Tyrah)', 'high', None, None, None),
 # S005
 ('S005', 'Tyrah', 'L', 'repetition', 'S002: Tyrah Chan-Hampton', 'high', None, None, None),
 ('S005', 'cô', 'R', 'personal', 'S004: cô (Tyrah)', 'high', None, None, None),
 ('S005', 'tình trạng vô gia cư', 'L', 'repetition', 'S004: cảnh vô gia cư', 'high', None, None, None),
 ('S005', 'bất ổn về nhà ở', 'L', 'repetition', 'S002: bất ổn về nhà ở', 'high', None, None, None),
 # S006
 ('S006', 'Tôi', 'R', 'personal', 'S002: Tyrah Chan-Hampton (quoted speaker)', 'med', None, 'first person in quote', 1),
 ('S006', 'xấu hổ', 'L', 'repetition', 'S005: cảm thấy xấu hổ', 'high', None, None, None),
 ('S006', 'cô', 'R', 'personal', 'S005: cô (Tyrah)', 'high', None, None, None),
 # S007
 ('S007', 'Chan-Hampton', 'L', 'repetition', 'S005: Tyrah', 'high', None, None, None),
 ('S007', 'cô', 'R', 'personal', 'S006: cô (Tyrah)', 'high', None, None, 1),
 ('S007', 'tình trạng vô gia cư', 'L', 'repetition', 'S005: tình trạng vô gia cư', 'high', None, None, None),
 # S008
 ('S008', 'anh chị em họ', 'L', 'repetition', 'S004: em họ', 'med', None, None, None),
 ('S008', 'người thân', 'L', 'repetition', 'S004: nhà người thân', 'med', None, None, None),
 ('S008', 'sống cùng', 'L', 'repetition', 'S003: sống cùng dì', 'med', None, None, None),
 ('S008', 'cô', 'R', 'personal', 'S007: cô (Tyrah)', 'high', None, None, None),
 # S009
 ('S009', 'tình trạng vô gia cư', 'L', 'repetition', 'S007: tình trạng vô gia cư', 'high', None, None, 1),
 ('S009', 'định kiến', 'L', 'repetition', 'S005: định kiến xã hội', 'high', None, None, None),
 ('S009', 'xấu hổ', 'L', 'repetition', 'S006: xấu hổ', 'high', None, None, None),
 # S010
 ('S010', 'cảnh vô gia cư', 'L', 'repetition', 'S009: tình trạng vô gia cư', 'high', None, None, None),
 # S011
 ('S011', 'vô gia cư', 'L', 'repetition', 'S010: cảnh vô gia cư', 'high', None, None, 1),
 ('S011', 'cũng', 'C', 'additive', 'S010: ABS statistic', 'med', None, None, None),
 ('S011', 'người', 'L', 'repetition', 'S010: 122.000 người', 'low', None, 'very general word', None),
 ('S011', 'thanh niên', 'L', 'repetition', 'S001: thanh niên', 'high', None, None, 1),
 # S012
 ('S012', 'Phân tích mới', 'L', 'repetition', 'S001: Phân tích mới đây', 'high', None, None, None),
 ('S012', 'hỗ trợ', 'L', 'repetition', 'S011: dịch vụ hỗ trợ', 'med', None, None, None),
 ('S012', 'vô gia cư', 'L', 'repetition', 'S011: vô gia cư', 'high', None, None, 1),
 ('S012', 'nhà ở', 'L', 'repetition', 'S002: bất ổn về nhà ở', 'med', None, 'nguy cơ mất nhà ở', None),
 ('S012', '20 “điểm nóng” trên khắp cả nước', 'L', 'repetition', 'S001: 20 “điểm nóng” trên khắp cả nước', 'high', None, 'verbatim echo', None),
 ('S012', 'thanh niên', 'L', 'repetition', 'S011: thanh niên', 'high', None, None, None),
 ('S012', 'chật vật tìm kiếm', 'L', 'repetition', 'S001: chật vật tìm kiếm một nơi ở', 'high', None, None, None),
 # S013
 ('S013', 'danh sách', 'L', 'general word', 'S012: 20 "điểm nóng"', 'med', None, 'general word for the ranking', None),
 ('S013', 'thanh niên', 'L', 'repetition', 'S012: thanh niên', 'high', None, None, None),
 ('S013', 'tình trạng vô gia cư', 'L', 'repetition', 'S012: vô gia cư', 'high', None, None, None),
 # S014
 ('S014', 'Vùng', 'L', 'repetition', 'S013: Vùng Latrobe-Gippsland', 'med', None, 'semi-generic region word', 1),
 # S015
 ('S015', 'Danh sách', 'L', 'repetition', 'S013: danh sách', 'high', None, None, None),
 ('S015', 'điểm nóng', 'L', 'repetition', 'S012: "điểm nóng"', 'high', None, None, None),
 ('S015', 'vô gia cư thanh niên', 'L', 'repetition', 'S013: thanh niên ... vô gia cư', 'high', None, None, None),
 # S016
 ('S016', 'Foyer Foundation', 'L', 'repetition', 'S012: Foyer Foundation', 'high', None, None, None),
 ('S016', 'phân tích', 'L', 'repetition', 'S012: Phân tích mới', 'high', 'R: này', None, None),
 ('S016', 'thanh niên vô gia cư', 'L', 'repetition', 'S015: vô gia cư thanh niên', 'high', None, None, None),
 ('S016', 'giới trẻ', 'L', 'synonym', 'S012: thanh niên', 'med', None, 'thế đồng nghĩa (youth)', None),
 # S017
 ('S017', 'danh sách', 'L', 'repetition', 'S015: Danh sách', 'high', 'R: này', None, None),
 ('S017', 'khu vực', 'L', 'repetition', 'S015: các khu vực', 'high', None, None, None),
 ('S017', 'này', 'R', 'demonstrative', 'S016: thất nghiệp ... hoàn thành trung học (các thách thức)', 'med', None, 'những thách thức này; head is new lexis', 2),
 ('S017', 'thanh niên', 'L', 'repetition', 'S016: thanh niên', 'high', None, None, None),
 ('S017', 'bà', 'R', 'personal', 'S016: Corin Moffatt', 'high', None, 'kinship term as pronoun', None),
 # S018
 ('S018', 'khu vực', 'L', 'repetition', 'S017: khu vực', 'high', None, None, 2),
 ('S018', 'vô gia cư', 'L', 'repetition', 'S016: thanh niên vô gia cư', 'high', None, None, None),
 ('S018', 'thanh niên', 'L', 'repetition', 'S017: thanh niên', 'high', None, None, None),
 ('S018', 'giới trẻ', 'L', 'repetition', 'S016: giới trẻ', 'med', None, None, None),
 ('S018', 'trên khắp cả nước', 'L', 'repetition', 'S012: trên khắp cả nước', 'high', None, None, None),
 # S019
 ('S019', 'Corin Moffatt', 'L', 'repetition', 'S017: bà (Moffatt)', 'high', None, None, None),
 ('S019', 'thanh niên', 'L', 'repetition', 'S018: thanh niên', 'high', None, None, None),
 ('S019', 'tình trạng vô gia cư', 'L', 'repetition', 'S018: vô gia cư', 'high', None, None, None),
 ('S019', 'nhà ở', 'L', 'repetition', 'S012: mất nhà ở', 'med', None, 'nhà ở giá rẻ', None),
 ('S019', 'bạo lực gia đình', 'L', 'repetition', 'S009: bạo lực gia đình', 'high', None, None, None),
 # S020
 ('S020', 'chật vật', 'L', 'repetition', 'S012: chật vật tìm kiếm', 'med', None, None, None),
 ('S020', 'nhà ở', 'L', 'repetition', 'S019: nhà ở giá rẻ', 'med', None, 'chi phí nhà ở', None),
 ('S020', 'thanh niên', 'L', 'repetition', 'S019: thanh niên', 'high', None, None, None),
 ('S020', 'bà', 'R', 'personal', 'S019: Corin Moffatt', 'high', None, None, None),
 # S021
 ('S021', 'thanh niên', 'L', 'repetition', 'S020: thanh niên', 'high', None, None, None),
 # S022
 ('S022', 'điều đó', 'R', 'demonstrative', 'S021: chỗ ở an toàn và ổn định', 'high', None, 'TT splits the EN sentence, making this cross-sentential', None),
 ('S022', 'họ', 'R', 'personal', 'S021: thanh niên', 'high', None, None, None),
 ('S022', 'yếu tố', 'L', 'repetition', 'S019: nhiều yếu tố', 'high', 'R: này', None, None),
 ('S022', 'thanh niên', 'L', 'repetition', 'S021: thanh niên', 'high', None, None, None),
 # S023
 ('S023', 'Hiện tại', 'C', 'temporal', 'S022: current impasse; shift to call for action', 'med', None, None, None),
 ('S023', 'Foyer Foundation', 'L', 'repetition', 'S016: Foyer Foundation', 'high', None, None, None),
 ('S023', 'thanh niên', 'L', 'repetition', 'S022: thanh niên', 'high', None, None, 1),
 ('S023', 'nhà ở', 'L', 'repetition', 'S020: chi phí nhà ở', 'med', None, 'nhà ở trung hạn', None),
 ('S023', 'cảnh vô gia cư', 'L', 'repetition', 'S019: tình trạng vô gia cư', 'high', None, None, None),
 # S024
 ('S024', 'Youth foyers', 'L', 'repetition', 'S023: youth foyers', 'high', None, None, None),
 ('S024', 'nhà ở', 'L', 'repetition', 'S023: nhà ở trung hạn', 'med', None, 'nhà ở chuyển tiếp', None),
 ('S024', 'thanh niên', 'L', 'repetition', 'S023: thanh niên', 'high', None, None, None),
 # S025
 ('S025', 'trung tâm', 'L', 'repetition', 'S024: các trung tâm', 'high', 'R: này', None, None),
 ('S025', 'chỗ ở', 'L', 'repetition', 'S021: chỗ ở an toàn và ổn định', 'high', None, None, None),
 ('S025', 'thanh niên', 'L', 'repetition', 'S024: thanh niên', 'high', None, None, None),
 ('S025', 'học', 'L', 'repetition', 'S022: việc học', 'med', None, 'tiếp tục học tập', None),
 # S026
 ('S026', 'Corin Moffatt', 'L', 'repetition', 'S020: bà (Moffatt)', 'high', None, None, None),
 ('S026', 'thanh niên', 'L', 'repetition', 'S025: thanh niên', 'high', None, None, None),
 ('S026', 'trung tâm', 'L', 'repetition', 'S025: trung tâm', 'med', None, 'trung tâm khủng hoảng', None),
 ('S026', 'hỗ trợ', 'L', 'repetition', 'S025: nhân viên hỗ trợ', 'med', None, None, 1),
 # S027
 ('S027', 'dịch vụ khẩn cấp', 'L', 'repetition', 'S026: dịch vụ hỗ trợ khẩn cấp', 'high', None, None, None),
 ('S027', 'thanh niên', 'L', 'repetition', 'S026: thanh niên', 'high', None, None, None),
 ('S027', 'cũng', 'C', 'additive', 'S026: hỗ trợ dài hạn chưa đủ', 'med', None, None, None),
 ('S027', 'nhà ở trung hạn và dài hạn', 'L', 'repetition', 'S023: nhà ở trung hạn', 'high', None, None, None),
 ('S027', 'bà', 'R', 'personal', 'S026: Corin Moffatt', 'high', None, None, None),
 # S028
 ('S028', 'Vì vậy', 'C', 'causal', 'S027: không có đủ dịch vụ', 'high', None, None, None),
 ('S028', 'thanh niên', 'L', 'repetition', 'S027: thanh niên', 'high', None, None, None),
 ('S028', 'hỗ trợ khẩn cấp', 'L', 'repetition', 'S027: dịch vụ khẩn cấp', 'high', None, None, None),
 # S029
 ('S029', 'vô gia cư', 'L', 'repetition', 'S023: cảnh vô gia cư', 'high', None, None, None),
 ('S029', 'thanh niên', 'L', 'repetition', 'S028: thanh niên', 'high', None, None, None),
 # S030
 ('S030', 'Ông', 'R', 'personal', 'S029: David MacKenzie', 'high', None, 'kinship term as pronoun', None),
 ('S030', 'hỗ trợ', 'L', 'repetition', 'S028: hỗ trợ khẩn cấp', 'med', None, None, None),
 ('S030', 'nhà ở', 'L', 'repetition', 'S027: nhà ở trung hạn', 'med', None, 'hỗ trợ nhà ở', None),
 ('S030', 'này', 'R', 'demonstrative', 'S029: vô gia cư ở thanh niên', 'med', None, 'tình trạng này; head is a frame word', None),
 # S031
 ('S031', 'phòng ngừa', 'L', 'repetition', 'S029: công tác phòng ngừa', 'high', None, None, None),
 ('S031', 'ông', 'R', 'personal', 'S030: Ông (MacKenzie)', 'high', None, None, 2),
 # S032
 ('S032', 'ngăn chặn', 'L', 'repetition', 'S030: ngăn chặn tình trạng này', 'high', None, None, None),
 ('S032', 'thanh niên', 'L', 'repetition', 'S029: thanh niên', 'high', None, None, None),
 ('S032', 'cảnh vô gia cư', 'L', 'repetition', 'S029: vô gia cư', 'high', None, None, None),
 ('S032', 'này', 'R', 'demonstrative', 'S029: vấn đề vô gia cư ở thanh niên', 'med', None, 'vấn đề này', None),
 # S033
 ('S033', 'MacKenzie', 'L', 'repetition', 'S029: David MacKenzie', 'high', None, None, None),
 ('S033', 'tình trạng vô gia cư', 'L', 'repetition', 'S032: cảnh vô gia cư', 'high', None, None, None),
 # S034
 ('S034', 'thiếu niên', 'L', 'repetition', 'S033: tuổi thiếu niên', 'med', None, None, None),
 ('S034', 'giúp đỡ', 'L', 'repetition', 'S030: giúp đỡ học sinh', 'med', None, None, None),
 ('S034', 'hỗ trợ', 'L', 'repetition', 'S030: hỗ trợ nhà ở', 'med', None, None, None),
 ('S034', 'bế tắc', 'L', 'repetition', 'S022: tình cảnh bế tắc', 'med', None, None, None),
 ('S034', 'ông', 'R', 'personal', 'S033: MacKenzie', 'high', None, None, 3),
 # S035
 ('S035', 'Tyrah Chan-Hampton', 'L', 'repetition', 'S007: Chan-Hampton', 'high', None, 'reintroduction after absence', None),
 # S036
 ('S036', 'Cô', 'R', 'personal', 'S035: Tyrah Chan-Hampton', 'high', None, None, None),
 ('S036', 'sự hỗ trợ', 'L', 'repetition', 'S034: hỗ trợ', 'med', None, None, None),
 ('S036', 'youth foyer', 'L', 'repetition', 'S024: Youth foyers', 'high', None, None, None),
 ('S036', 'hai năm', 'L', 'repetition', 'S024: hai năm', 'med', None, None, None),
 ('S036', 'cô', 'R', 'personal', 'S035: Tyrah Chan-Hampton', 'high', None, None, None),
 # S037
 ('S037', 'Tyrah Chan-Hampton', 'L', 'repetition', 'S036: Cô (Tyrah)', 'high', None, None, None),
 ('S037', 'dịch vụ hỗ trợ', 'L', 'repetition', 'S036: sự hỗ trợ', 'med', None, None, None),
 ('S037', 'thanh niên', 'L', 'repetition', 'S032: thanh niên', 'high', None, None, None),
 ('S037', 'bất ổn', 'L', 'repetition', 'S005: bất ổn về nhà ở', 'med', None, 'môi trường bất ổn', None),
 ('S037', 'chỗ ở', 'L', 'repetition', 'S025: chỗ ở ổn định', 'high', None, None, None),
 # S038
 ('S038', 'người', 'L', 'repetition', 'S037: thanh niên', 'low', None, 'very general word', None),
 ('S038', 'môi trường', 'L', 'repetition', 'S037: môi trường bất ổn hoặc nguy hiểm', 'high', None, None, None),
 ('S038', 'cô', 'R', 'personal', 'S037: Tyrah Chan-Hampton', 'high', None, None, None),
 # S039
 ('S039', 'thanh niên', 'L', 'repetition', 'S037: thanh niên', 'high', None, None, None),
 ('S039', 'trung tâm tạm trú', 'L', 'repetition', 'S026: trung tâm khủng hoảng / S004: nhà tạm trú', 'med', None, None, None),
 ('S039', 'sự hỗ trợ', 'L', 'repetition', 'S037: dịch vụ hỗ trợ', 'med', None, None, None),
 ('S039', 'nơi ở ổn định', 'L', 'repetition', 'S023: nơi ở ổn định', 'med', None, None, None),
 # S040
 ('S040', 'tình trạng vô gia cư', 'L', 'repetition', 'S033: tình trạng vô gia cư', 'high', None, None, None),
 ('S040', 'nhà ở', 'L', 'repetition', 'S030: hỗ trợ nhà ở', 'med', None, 'tổ chức hỗ trợ nhà ở', None),
 # S041
 ('S041', 'Chính phủ', 'L', 'repetition', 'S023: chính phủ', 'high', None, None, None),
 ('S041', 'nhà ở', 'L', 'repetition', 'S040: nhà ở', 'med', None, None, None),
 ('S041', 'tình trạng vô gia cư', 'L', 'repetition', 'S040: tình trạng vô gia cư', 'high', None, None, None),
 ('S041', 'người phát ngôn', 'L', 'repetition', 'S040: một phát ngôn viên', 'high', None, None, None),
 # S042
 ('S042', 'chính phủ', 'L', 'repetition', 'S023: chính phủ', 'high', None, None, None),
 ('S042', 'thanh niên', 'L', 'repetition', 'S039: thanh niên', 'high', None, None, None),
 ('S042', 'vô gia cư', 'L', 'repetition', 'S041: tình trạng vô gia cư', 'high', None, None, None),
 ('S042', 'nhà ở', 'L', 'repetition', 'S041: nhà ở', 'med', None, 'lựa chọn nhà ở bền vững', None),
 # S043
 ('S043', 'Vô gia cư', 'L', 'repetition', 'S042: vô gia cư', 'med', None, 'embedded in proper name', 1),
 ('S043', 'vô gia cư', 'L', 'repetition', 'S042: vô gia cư', 'high', None, None, 2),
 ('S043', 'nhà ở', 'L', 'repetition', 'S042: nhà ở', 'med', None, 'hệ thống nhà ở xã hội', None),
 # S044
 ('S044', 'đầu tư', 'L', 'repetition', 'S042: khoản đầu tư', 'high', None, None, None),
 ('S044', 'phòng ngừa', 'L', 'repetition', 'S031: phòng ngừa', 'high', None, None, None),
 ('S044', 'tình trạng vô gia cư', 'L', 'repetition', 'S043: vô gia cư', 'high', None, None, None),
 ('S044', 'thanh niên', 'L', 'repetition', 'S043: thanh niên', 'high', None, None, None),
 ('S044', 'hỗ trợ', 'L', 'repetition', 'S043: hỗ trợ', 'med', None, None, None),
 # S045
 ('S045', 'nhà ở chuyển tiếp', 'L', 'repetition', 'S024: nhà ở chuyển tiếp', 'high', None, None, None),
 ('S045', 'hỗ trợ', 'L', 'repetition', 'S044: hỗ trợ', 'med', None, None, None),
 ('S045', 'khẩn cấp', 'L', 'repetition', 'S028: hỗ trợ khẩn cấp', 'med', None, 'chỗ ở khẩn cấp', None),
 ('S045', 'bạo lực gia đình', 'L', 'repetition', 'S019: bạo lực gia đình', 'high', None, None, None),
 ('S045', 'thanh niên vô gia cư', 'L', 'repetition', 'S044: tình trạng vô gia cư ở thanh niên', 'high', None, None, None),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_02 (§2–§3) ----
 # [LC] = liên câu; [TC] = trong câu. Các dòng này KHÔNG do script sinh:
 # người đọc bản phân tích ngữ nghĩa rồi chọn đúng vị trí/tiền trạm.
 ('S003', None, 'E', 'nominal', 'S003: {cô} (trong câu)', 'high', None, '[TC] lược chủ ngữ trong vế thời gian “khi ∅ mới 11 tuổi”; hệ từ [là] trước “11 tuổi” cũng lược', 1, 'khi ', '{cô}', 'TC'),
 ('S003', None, 'E', 'nominal', 'S003: {cô} (trong câu)', 'high', None, '[TC] lược chủ ngữ {cô} trước “được đưa đến” ở vế tọa hợp; EN: and was placed', 1, 'và ', '{cô}', 'TC'),
 ('S004', None, 'E', 'nominal', 'S004: {cả hai} (trong câu)', 'high', None, '[TC] chủ ngữ dùng chung cho chuỗi 3 mệnh đề; gap còn lại trước “ở nhờ nhà người thân”', 1, 'cảnh vô gia cư, ', '{cả hai}', 'TC'),
 ('S006', None, 'E', 'nominal', 'S002: từ “vô gia cư” (tân ngữ bị lược)', 'high', None, '[LC] lược tân ngữ {từ “vô gia cư”} sau “nói ra”; EN dùng đại từ it (“say it”) — cặp đối lập quy chiếu ↔ tỉnh lược', 1, 'chỉ cần nói ra', '{từ “vô gia cư”}', 'LC'),
 ('S022', None, 'E', 'nominal', 'S022: {họ} (trong câu)', 'high', None, '[TC] lược chủ ngữ vế 2, 3 của chuỗi liệt kê; gap còn lại trước “cũng không thể giữ…”', 1, 'hoàn thành việc học, ', '{họ}', 'TC'),
 ('S028', None, 'E', 'nominal', 'S028: {thanh niên} (trong câu)', 'high', None, '[TC] lược chủ ngữ {thanh niên} sau liên từ “mà”: “mà ∅ không có lối thoát…”', 1, 'hệ thống hỗ trợ khẩn cấp ', '{thanh niên}', 'TC'),
 ('S039', None, 'E', 'nominal', 'S039: {những thanh niên} (trong câu)', 'high', None, '[TC] chủ ngữ dùng chung cho chuỗi 3 vị ngữ; gap còn lại trước “nỗ lực hết sức…”', 1, 'phải ngủ trong xe hơi, ', '{những thanh niên}', 'TC'),
 ('S043', None, 'E', 'verbal', 'S043: {được} (trong câu)', 'high', None, '[TC] danh sách không vị từ do bản dịch tự tạo: lược “được” trước “dành cho”; các gap sau: S044 “đầu tư vào”, S045 “bổ sung vào”', 1, '9,3 tỷ AUD ', '{được}', 'TC'),
 ('S035', None, 'E', 'nominal', 'S002: Tyrah Chan-Hampton (người được nhắc lại ở đầu câu)', 'high', None, '[LC] đồng vị ngữ rút gọn “Hiện 23 tuổi” = {cô} 23 tuổi, giữ nguyên tỉnh lược của E-EN4; gap_after rỗng vì chỗ trống ở đầu câu', 1, '', '{cô}', 'LC'),
]
