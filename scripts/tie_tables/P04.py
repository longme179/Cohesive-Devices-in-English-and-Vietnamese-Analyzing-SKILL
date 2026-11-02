# P04 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S003
 ('S003', 'That', 'R', 'demonstrative', 'S002: Almost 3 in 4 (71 per cent) Australians', 'high', None, None, 1),
 ('S003', 'struggling', 'L', 'repetition', 'S002: struggle to get a good night\u2019s sleep', 'high', None, 'morphological reiteration', 1),
 ('S003', 'sleep', 'L', 'repetition', 'S002: a good night\u2019s sleep', 'high', None, 'their sleep', 1),
 # S004
 ('S004', 'surveyed', 'L', 'repetition', 'S002: a new survey ... responses from 1,010 participants', 'med', 'R: those', 'head reiterates; demonstrative to alt', 1),
 ('S004', 'struggled', 'L', 'repetition', 'S003: struggling', 'high', None, None, 1),
 ('S004', 'night', 'L', 'repetition', 'S002: a good night\u2019s sleep', 'med', None, 'during the night', 1),
 # S005
 ('S005', 'snoring', 'L', 'repetition', 'S004: their partner snoring', 'high', None, 'their own snoring', 1),
 ('S005', 'sleep', 'L', 'repetition', 'S003: sleep', 'med', None, 'inside compound sleep apnea', 1),
 # S006
 ('S006', 'sleep', 'L', 'repetition', 'S005: sleep apnea', 'high', None, 'sleep issues', 1),
 ('S006', 'night', 'L', 'repetition', 'S004: during the night', 'med', None, None, 1),
 # S007
 ('S007', 'To top it off', 'C', 'additive', 'S004-S006: sleep issues', 'high', None, None, 1),
 ('S007', 'the survey', 'L', 'repetition', 'S002: a new survey', 'high', None, None, 1),
 ('S007', 'Australian', 'L', 'repetition', 'S002: Australians', 'high', None, 'the average Australian', 1),
 ('S007', 'sleep', 'L', 'repetition', 'S006: sleep issues', 'high', None, '6.9 hours of sleep', 1),
 # S008
 ('S008', 'sleep', 'L', 'repetition', 'S007: sleep', 'high', None, 'sleep researcher', 1),
 ('S008', 'Australian', 'L', 'repetition', 'S007: the average Australian', 'high', None, 'Australian adults', 1),
 # S009
 ('S009', 'Finder', 'L', 'repetition', 'S002: site Finder', 'high', None, 'the Finder study', 1),
 ('S009', 'study', 'L', 'synonym', 'S002: a new survey', 'med', None, 'survey ~ study', 1),
 ('S009', 'sleep-deprived', 'L', 'repetition', 'S008: enough quality sleep', 'med', None, 'negated reiteration of the sleep chain', 1),
 ('S009', 'Shriane', 'L', 'repetition', 'S008: Alexandra Shriane', 'high', None, None, 1),
 ('S009', 'suffering', 'L', 'repetition', 'S005: suffered from sleep apnea', 'med', None, 'morphological reiteration', 1),
 # S010
 ('S010', 'sleep', 'L', 'repetition', 'S009: sleep-deprived', 'high', None, 'amount of sleep', 1),
 ('S010', 'asleep', 'L', 'repetition', 'S009: sleep-deprived', 'med', None, 'morphological reiteration', 1),
 ('S010', 'she', 'R', 'personal', 'S009: Shriane', 'high', None, None, 1),
 # S011
 ('S011', 'Other', 'R', 'comparative', 'S009: the Finder study', 'high', None, 'other than the Finder study', 1),
 ('S011', 'sleep problem', 'L', 'repetition', 'S006: sleep issues', 'med', None, 'problem ~ issue', 1),
 # S012
 ('S012', 'adults', 'L', 'repetition', 'S008: Australian adults', 'high', None, 'healthy adults', 1),
 ('S012', 'quality sleep', 'L', 'repetition', 'S008: enough quality sleep', 'high', None, 'verbatim', 1),
 ('S012', 'Shriane', 'L', 'repetition', 'S010: she', 'high', None, None, 1),
 ('S012', 'each night', 'L', 'repetition', 'S007: each night', 'med', None, 'verbatim', 1),
 # S013
 ('S013', 'This', 'R', 'demonstrative', 'S012: seven to nine hours of quality sleep', 'high', None, 'This figure', 1),
 ('S013', 'studies', 'L', 'repetition', 'S009: the Finder study', 'med', None, 'thousands of studies', 1),
 ('S013', 'sleep', 'L', 'repetition', 'S012: quality sleep', 'high', None, 'less than seven hours of sleep', 1),
 ('S013', 'seven hours', 'L', 'repetition', 'S012: seven to nine hours', 'med', None, None, 1),
 ('S013', 'health', 'L', 'repetition', 'S007: our health', 'med', None, 'poor health', 1),
 # S014
 ('S014', 'On the contrary', 'C', 'adversative', 'S013: less than seven hours harms', 'high', None, None, 1),
 ('S014', 'sleeping', 'L', 'repetition', 'S013: sleep', 'high', None, 'those sleeping more than nine hours', 1),
 ('S014', 'nine hours', 'L', 'repetition', 'S012: seven to nine hours', 'med', None, None, 1),
 ('S014', 'she', 'R', 'personal', 'S012: Shriane', 'high', None, None, 1),
 # S015
 ('S015', 'She', 'R', 'personal', 'S014: she', 'high', None, None, 1),
 ('S015', 'also', 'C', 'additive', 'S008: Shriane\u2019s first claim', 'med', None, None, 1),
 # S016
 ('S016', 'sleep deprivation', 'L', 'repetition', 'S009: sleep-deprived', 'high', None, None, 1),
 ('S016', 'she', 'R', 'personal', 'S015: She', 'high', None, None, 1),
 # S017
 ('S017', 'seven to nine-hour recommendation', 'L', 'repetition', 'S012: seven to nine hours ... recommendation', 'high', None, 'combined echo', 1),
 ('S017', 'people', 'L', 'repetition', 'S016: people say', 'high', 'R: these', 'head reiterates; demonstrative to alt', 1),
 ('S017', 'sleep deprivation', 'L', 'repetition', 'S016: sleep deprivation', 'high', None, 'chronic sleep deprivation', 1),
 # S018
 ('S018', 'seven to nine-hour recommendation', 'L', 'repetition', 'S017: the seven to nine-hour recommendation', 'high', None, 'verbatim', 1),
 ('S018', 'healthy adults', 'L', 'repetition', 'S012: healthy adults', 'high', None, 'verbatim', 1),
 # S019
 ('S019', 'adults', 'L', 'repetition', 'S018: healthy adults', 'high', None, None, 1),
 ('S019', 'sleep', 'L', 'repetition', 'S014: sleeping', 'high', None, 'more sleep', 1),
 ('S019', 'Shriane', 'L', 'repetition', 'S016: she', 'high', None, None, 1),
 # S021
 ('S021', 'AIHW', 'L', 'repetition', 'S011: (AIHW)', 'high', None, 'abbreviation', 1),
 ('S021', 'sleep', 'L', 'repetition', 'S019: sleep', 'high', None, 'hours of sleep', 1),
 # S022
 ('S022', 'Shriane', 'L', 'repetition', 'S019: Shriane', 'high', None, None, 1),
 ('S022', 'snooze', 'L', 'repetition', 'S001: hit the snooze alarm ... more snoozes', 'med', None, 'echo of the lede', 1),
 # S023
 ('S023', 'They', 'R', 'personal', 'S022: women', 'high', None, None, 1),
 ('S023', 'recommendation', 'L', 'repetition', 'S018: seven to nine-hour recommendation', 'high', None, 'the recommendation range', 1),
 ('S023', 'nine hours', 'L', 'repetition', 'S014: nine hours', 'med', None, None, 1),
 ('S023', 'men', 'L', 'repetition', 'S022: men', 'high', None, None, 2),
 ('S023', 'seven hours', 'L', 'repetition', 'S013: seven hours', 'med', None, None, 1),
 # S024
 ('S024', 'Those', 'R', 'demonstrative', 'S018: other groups', 'med', None, None, 1),
 ('S024', 'health', 'L', 'repetition', 'S013: poor health', 'med', None, 'health conditions', 1),
 # S025
 ('S025', 'sleep quality', 'L', 'repetition', 'S012: quality sleep', 'high', None, 'word-order variant', 1),
 # S026
 ('S026', 'adults', 'L', 'repetition', 'S019: adults', 'high', None, 'most adults', 1),
 ('S026', 'sleep', 'L', 'repetition', 'S025: sleep quality', 'high', None, 'enough sleep', 1),
 ('S026', 'quality sleep', 'L', 'repetition', 'S012: quality sleep', 'high', None, None, 1),
 ('S026', 'Shriane', 'L', 'repetition', 'S022: Shriane', 'high', None, None, 1),
 # S027
 ('S027', 'quality of sleep', 'L', 'repetition', 'S025: sleep quality', 'high', None, None, 1),
 ('S027', 'Shriane', 'L', 'repetition', 'S026: Shriane', 'high', None, None, 1),
 # S028
 ('S028', 'struggle', 'L', 'repetition', 'S002: struggle', 'med', None, None, 1),
 ('S028', 'quality sleep', 'L', 'repetition', 'S026: quality sleep', 'high', None, None, 1),
 ('S028', 'she', 'R', 'personal', 'S027: Shriane', 'high', None, None, 1),
 # S029
 ('S029', 'indicators', 'L', 'repetition', 'S027: some indicators', 'high', None, None, 1),
 ('S029', 'sleep', 'L', 'repetition', 'S028: quality sleep', 'high', None, 'sleep needs', 1),
 # S030
 ('S030', 'sleep', 'L', 'repetition', 'S029: sleep needs', 'med', None, 'brush off sleep', 1),
 ('S030', 'sleep deprivation', 'L', 'repetition', 'S017: chronic sleep deprivation', 'high', None, None, 1),
 # S031
 ('S031', 'sleep deprivation', 'L', 'repetition', 'S030: sleep deprivation', 'high', None, 'Short-term sleep deprivation', 1),
 ('S031', 'intense food cravings', 'L', 'repetition', 'S029: really intense food cravings', 'high', None, 'verbatim', 1),
 # S032
 ('S032', 'chronically deprived', 'L', 'repetition', 'S017: chronic sleep deprivation', 'med', None, 'morphological reiteration', 1),
 ('S032', 'these', 'R', 'demonstrative', 'S031: effects on immune system, brain, mood', 'med', None, 'these impacts; impacts ~ effects synonym', 1),
 # S033
 ('S033', 'quality sleep', 'L', 'repetition', 'S028: quality sleep', 'high', None, None, 1),
 ('S033', 'struggle', 'L', 'repetition', 'S028: struggle', 'med', None, None, 1),
 ('S033', 'Shriane', 'L', 'repetition', 'S027: Shriane', 'high', None, None, 1),
 # S034
 ('S034', 'Sleep', 'L', 'repetition', 'S033: quality sleep', 'high', None, 'sentence-initial topic', 1),
 ('S034', 'health', 'L', 'repetition', 'S013: poor health', 'med', None, 'pillar of health', 1),
 ('S034', 'major flow-on effects', 'L', 'repetition', 'S007: "major flow-on effects"', 'high', None, 'verbatim echo', 1),
 # S035
 ('S035', 'sleep', 'L', 'repetition', 'S034: Sleep', 'high', None, 'improve your sleep', 1),
 ('S035', 'Shriane', 'L', 'repetition', 'S033: Shriane', 'high', None, None, 1),
 # S036
 ('S036', 'Instead', 'C', 'adversative', 'S035: gadgets not backed by science', 'high', None, None, 1),
 ('S036', 'she', 'R', 'personal', 'S035: Shriane', 'high', None, None, 1),
 # S038
 ('S038', 'sleep', 'L', 'repetition', 'S035: sleep', 'high', None, 'before sleep', 1),
 # S039
 ('S039', 'sleep', 'L', 'repetition', 'S038: sleep', 'high', None, 'before sleep', 1),
 # S040
 ('S040', 'sleep', 'L', 'repetition', 'S039: sleep', 'high', None, 'before sleep', 1),
 # S041
 ('S041', 'bed', 'L', 'repetition', 'S010: the time you spend in bed', 'med', None, None, 1),
 # S044
 ('S044', 'struggling with sleep', 'L', 'repetition', 'S003: struggling with their sleep', 'high', None, 'verbatim echo', 1),
]

TT = [
 # S002
 ('S002', 'Nói cách khác', 'C', 'additive', 'S001: 71% người Úc khó có giấc ngủ ngon', 'high', None, 'reformulation additive', 1),
 ('S002', 'người Úc', 'L', 'repetition', 'S001: người Úc', 'high', None, None, 1),
 ('S002', 'giấc ngủ', 'L', 'repetition', 'S001: giấc ngủ ngon', 'high', None, None, 1),
 # S003
 ('S003', 'khảo sát', 'L', 'repetition', 'S001: theo khảo sát', 'high', None, None, 1),
 ('S003', 'khó ngủ', 'L', 'repetition', 'S002: chật vật với giấc ngủ', 'med', None, 'morphological reiteration (ngủ)', 1),
 # S004
 ('S004', 'giấc ngủ', 'L', 'repetition', 'S003: khó ngủ', 'high', None, None, 1),
 # S005
 ('S005', 'Cũng', 'C', 'additive', 'S003-S004: survey details', 'med', None, None, 1),
 ('S005', 'khảo sát', 'L', 'repetition', 'S003: khảo sát', 'high', None, None, 1),
 ('S005', 'người Úc', 'L', 'repetition', 'S002: người Úc', 'high', None, None, 1),
 ('S005', 'ngủ', 'L', 'repetition', 'S004: giấc ngủ', 'high', None, 'ngủ 6,9 tiếng', 1),
 # S006
 ('S006', 'khảo sát', 'L', 'repetition', 'S005: khảo sát', 'high', None, 'khảo sát của Finder', 1),
 ('S006', 'Finder', 'L', 'repetition', 'S001: trang Finder', 'high', None, None, 1),
 ('S006', 'người Úc', 'L', 'repetition', 'S005: người Úc', 'high', None, None, 1),
 ('S006', 'thiếu ngủ', 'L', 'repetition', 'S005: ngủ', 'high', None, 'negated reiteration of the sleep chain', 1),
 ('S006', 'giấc ngủ', 'L', 'repetition', 'S004: giấc ngủ', 'high', None, 'nhà nghiên cứu giấc ngủ', 1),
 ('S006', 'con số', 'L', 'repetition', 'S005: con số này', 'med', None, None, 1),
 # S007
 ('S007', 'ngủ', 'L', 'repetition', 'S006: thiếu ngủ', 'high', None, 'thời gian ngủ', 1),
 ('S007', 'bà', 'R', 'personal', 'S006: bà Alexandra Shriane', 'high', None, None, 1),
 # S008
 ('S008', 'ngủ', 'L', 'repetition', 'S007: ngủ', 'high', None, 'ngủ từ 7 đến 9 tiếng', 1),
 # S009
 ('S009', 'này', 'R', 'demonstrative', 'S008: 7 đến 9 tiếng', 'high', None, 'Con số này', 1),
 ('S009', 'ngủ', 'L', 'repetition', 'S008: ngủ', 'high', None, 'ngủ dưới 7 tiếng', 1),
 # S010
 ('S010', 'Ngược lại', 'C', 'adversative', 'S009: dưới 7 tiếng harmful', 'high', None, None, 1),
 ('S010', 'ngủ', 'L', 'repetition', 'S009: ngủ', 'high', None, 'ngủ hơn 9 tiếng', 1),
 ('S010', 'giấc ngủ', 'L', 'repetition', 'S006: giấc ngủ', 'high', None, 'rối loạn giấc ngủ', 1),
 # S011
 ('S011', 'Bà Shriane', 'L', 'repetition', 'S006: bà Alexandra Shriane', 'high', None, 'surname reiteration', 1),
 ('S011', 'cũng', 'C', 'additive', 'S006: Shriane\u2019s first claim', 'med', None, None, 1),
 ('S011', 'ngủ', 'L', 'repetition', 'S010: ngủ', 'high', None, 'ngủ 5 tiếng', 1),
 # S012
 ('S012', 'ngủ', 'L', 'repetition', 'S011: ngủ', 'high', None, 'ngủ năm tiếng', 1),
 ('S012', 'bà', 'R', 'personal', 'S011: Bà Shriane', 'high', None, None, 1),
 # S013
 ('S013', 'họ', 'R', 'personal', 'S012: Một số người', 'high', None, None, 1),
 ('S013', 'thiếu ngủ', 'L', 'repetition', 'S006: thiếu ngủ', 'high', None, 'thiếu ngủ mãn tính', 1),
 # S014
 ('S014', 'ngủ', 'L', 'repetition', 'S013: thiếu ngủ', 'high', None, 'cần ngủ nhiều hơn', 1),
 ('S014', 'bà Shriane', 'L', 'repetition', 'S011: Bà Shriane', 'high', None, None, 1),
 # S015
 ('S015', 'Trẻ nhỏ', 'L', 'repetition', 'S014: Trẻ em', 'med', None, 'partial reiteration (Trẻ)', 1),
 ('S015', 'ngủ', 'L', 'repetition', 'S014: ngủ', 'high', None, 'cần ngủ 11-14 tiếng', 1),
 # S017
 ('S017', 'Ngoài ra', 'C', 'additive', 'S016: người cao niên', 'high', None, None, 1),
 ('S017', 'ngủ', 'L', 'repetition', 'S015: ngủ', 'high', None, 'cần ngủ nhiều hơn', 1),
 # S018
 ('S018', 'cũng', 'C', 'additive', 'S017: phụ nữ cần ngủ nhiều', 'med', None, None, 1),
 ('S018', 'ngủ', 'L', 'repetition', 'S017: ngủ', 'high', None, 'cần ngủ nhiều giờ hơn', 1),
 # S019
 ('S019', 'ngủ', 'L', 'repetition', 'S018: ngủ', 'med', None, 'số giờ ngủ', 1),
 ('S019', 'giấc ngủ', 'L', 'repetition', 'S010: rối loạn giấc ngủ', 'high', None, 'chất lượng giấc ngủ', 1),
 # S020
 ('S020', 'buồn ngủ', 'L', 'repetition', 'S019: giờ ngủ', 'med', None, 'morphological reiteration (ngủ)', 1),
 ('S020', 'giấc ngủ', 'L', 'repetition', 'S019: chất lượng giấc ngủ', 'high', None, None, 1),
 ('S020', 'bà Shriane', 'L', 'repetition', 'S014: bà Shriane', 'high', None, None, 1),
 # S021
 ('S021', 'ngủ', 'L', 'repetition', 'S020: giấc ngủ', 'med', None, 'ngủ chưa đủ giấc', 1),
 # S022
 ('S022', 'Thiếu ngủ', 'L', 'repetition', 'S013: thiếu ngủ mãn tính', 'high', None, None, 1),
 # S023
 ('S023', 'tình trạng', 'L', 'general word', 'S013: tình trạng thiếu ngủ mãn tính', 'high', None, None, 1),
 # S024
 ('S024', 'thiếu ngủ', 'L', 'repetition', 'S022: Thiếu ngủ', 'high', None, None, 1),
 ('S024', 'bà Shriane', 'L', 'repetition', 'S020: bà Shriane', 'high', None, None, 1),
 # S025
 ('S025', 'Giấc ngủ', 'L', 'repetition', 'S020: giấc ngủ', 'high', None, 'sentence-initial topic', 1),
 ('S025', 'sức khỏe', 'L', 'repetition', 'S009: các vấn đề sức khỏe', 'high', None, None, 1),
 # S026
 ('S026', 'giấc ngủ', 'L', 'repetition', 'S025: Giấc ngủ', 'high', None, None, 1),
 ('S026', 'bà Shriane', 'L', 'repetition', 'S024: bà Shriane', 'high', None, None, 1),
 # S027
 ('S027', 'Thay vào đó', 'C', 'adversative', 'S026: đa số không hiệu quả', 'high', None, None, 1),
 ('S027', 'bà', 'R', 'personal', 'S026: bà Shriane', 'high', None, None, 1),
 ('S027', 'Đi ngủ', 'L', 'repetition', 'S026: giấc ngủ', 'med', None, 'morphological reiteration', 1),
 # S028
 ('S028', 'ngủ trưa', 'L', 'repetition', 'S027: Đi ngủ', 'med', None, 'morphological reiteration', 1),
 # S029
 ('S029', 'ngủ', 'L', 'repetition', 'S028: ngủ trưa', 'high', None, 'trước khi ngủ', 1),
 # S030
 ('S030', 'ngủ', 'L', 'repetition', 'S029: ngủ', 'high', None, 'trước khi ngủ', 1),
 # S031
 ('S031', 'ngủ', 'L', 'repetition', 'S030: ngủ', 'high', None, 'trước giờ ngủ', 1),
 # S032
 ('S032', 'giường', 'L', 'repetition', 'S007: nằm trên giường', 'high', None, None, 1),
 ('S032', 'ngủ', 'L', 'repetition', 'S031: ngủ', 'med', None, 'để ngủ', 1),
 # S033
 ('S033', 'phòng ngủ', 'L', 'repetition', 'S032: ngủ', 'med', None, 'morphological reiteration', 1),
 # S034
 ('S034', 'giường', 'L', 'repetition', 'S032: giường', 'high', None, 'ra khỏi giường', 1),
 # S035
 ('S035', 'khó ngủ', 'L', 'repetition', 'S003: khó ngủ', 'high', None, 'verbatim echo of the earlier survey sentence', 1),
]
