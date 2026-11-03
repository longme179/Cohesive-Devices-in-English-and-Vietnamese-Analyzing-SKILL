# P11 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'election', 'L', 'repetition', 'S001: parliamentary elections', 'med', None, None, 1),
 # S004
 ('S004', 'party', 'L', 'repetition', 'S001: his party', 'high', None, 'opposition party', 1),
 # S005
 ('S005', 'The United States', 'L', 'repetition', 'S002: the November 5 U.S. election', 'high', None, 'expansion of abbreviation', 1),
 ('S005', 'such', 'R', 'comparative', 'S004: shadow government system', 'high', None, 'no such system', 1),
 # S006
 ('S006', 'America\u2019s', 'L', 'synonym', 'S005: The United States', 'high', None, None, 1),
 # S007
 ('S007', 'govern', 'L', 'repetition', 'S006: government bureaucracy', 'med', None, 'morphological reiteration', 1),
 ('S007', 'Presidential Transition', 'L', 'repetition', 'S006: president-to-be', 'med', None, 'embedded in proper name', 1),
 # S008
 ('S008', 'The presidential transition', 'L', 'repetition', 'S007: Center for Presidential Transition', 'high', None, None, 1),
 ('S008', 'Election Day in November', 'L', 'repetition', 'S002: the November 5 U.S. election', 'med', None, None, 1),
 ('S008', 'American', 'L', 'repetition', 'S006: America\u2019s', 'high', None, 'morphological reiteration', 1),
 # S009
 ('S009', 'The period', 'L', 'general word', 'S008: those critical 11 weeks', 'high', None, None, 1),
 ('S009', 'administration', 'L', 'repetition', 'S006: government bureaucracy', 'med', None, None, 1),
 # S010
 # S011
 ('S011', 'The transition period', 'L', 'repetition', 'S008: The presidential transition', 'high', None, None, 1),
 ('S011', 'America\u2019s history', 'L', 'repetition', 'S008: American democracy', 'high', None, 'morphological reiteration', 1),
 # S012
 ('S012', 'the phrase \u201cpresidential transition\u201d', 'L', 'repetition', 'S011: The transition period', 'high', None, None, 1),
 ('S012', 'Riley', 'L', 'repetition', 'S011: historian Russel Riley', 'high', None, None, 1),
 # S013
 ('S013', 'the transition', 'L', 'repetition', 'S012: the phrase \u201cpresidential transition\u201d', 'high', None, None, 1),
 ('S013', 'tradition', 'L', 'repetition', 'S004: (shadow government tradition implied)', 'low', None, 'first overt tradition mention; weak', 1),
 # S014
 ('S014', 'the customs and habits', 'L', 'repetition', 'S013: tradition and custom', 'high', None, None, 1),
 # S015
 ('S015', 'traditions', 'L', 'repetition', 'S013: tradition', 'high', None, None, 1),
 # S016
 ('S016', 'the post-election White House meeting', 'L', 'repetition', 'S015: Some of the traditions', 'med', None, 'instance of the traditions', 1),
 ('S016', 'a sitting president', 'L', 'repetition', 'S002: become president again', 'med', None, None, 1),
 # S017
 ('S017', 'President Harry Truman', 'L', 'repetition', 'S016: a sitting president', 'high', None, None, 1),
 ('S017', 'this tradition', 'L', 'repetition', 'S015: traditions', 'high', 'R: this', None, 1),
 # S018
 ('S018', 'The example', 'L', 'repetition', 'S017: this tradition', 'high', None, None, 1),
 ('S018', 'every president', 'L', 'repetition', 'S017: President Harry Truman', 'high', None, None, 1),
 ('S018', 'Trump', 'L', 'repetition', 'S002: Donald Trump', 'high', None, None, 1),
 # S019
 ('S019', 'Other', 'R', 'comparative', 'S015-S018: symbolic traditions', 'high', None, None, 1),
 ('S019', 'practices', 'L', 'repetition', 'S016: the post-election White House meeting', 'med', None, None, 1),
 # S020
 ('S020', 'a tradition', 'L', 'repetition', 'S017: this tradition', 'high', None, None, 1),
 ('S020', 'the president', 'L', 'repetition', 'S018: every president', 'high', None, None, 1),
 ('S020', 'the incoming commander-in-chief', 'L', 'repetition', 'S016: a president-elect', 'high', None, None, 1),
 # S021
 ('S021', 'Neither', 'R', 'comparative', 'S016-S020: the two traditions', 'high', None, None, 1),
 ('S021', 'practice', 'L', 'repetition', 'S019: practices', 'high', None, None, 1),
 ('S021', 'the transition', 'L', 'repetition', 'S013: the transition', 'high', None, None, 1),
 # S022
 ('S022', 'The Presidential Transition Act', 'L', 'repetition', 'S012: the phrase \u201cpresidential transition\u201d', 'high', None, None, 1),
 ('S022', 'updated over the years', 'L', 'repetition', 'S011: used to be even longer', 'low', None, 'temporal echo; weak', 1),
 # S023
 ('S023', 'the election', 'L', 'repetition', 'S008: Election Day in November', 'high', None, None, 1),
 ('S023', 'the president', 'L', 'repetition', 'S020: the president', 'high', None, None, 1),
 ('S023', 'a transition coordinating council', 'L', 'repetition', 'S022: The Presidential Transition Act', 'med', None, 'transition chain', 1),
 # S024
 ('S024', 'succession plans', 'L', 'repetition', 'S023: designates a transition director', 'med', None, None, 1),
 # S025
 ('S025', 'the General Services Administration', 'L', 'repetition', 'S022: The Presidential Transition Act', 'med', None, 'agency chain', 1),
 ('S025', 'the federal government\u2019s', 'L', 'repetition', 'S023: each federal agency', 'high', None, None, 1),
 ('S025', 'transition', 'L', 'repetition', 'S023: a transition director', 'high', None, 'transition teams', 1),
 # S026
 ('S026', 'these', 'R', 'demonstrative', 'S022-S025: legal provisions', 'high', None, None, 1),
 ('S026', 'presidential succession', 'L', 'repetition', 'S024: succession plans', 'high', None, None, 1),
 ('S026', 'American history', 'L', 'repetition', 'S011: America\u2019s history', 'high', None, 'verbatim', 1),
 # S027
 ('S027', 'Then', 'C', 'temporal', 'S026: the norm through most of history', 'high', None, None, 1),
 ('S027', 'Trump', 'L', 'repetition', 'S018: Trump', 'high', None, None, 1),
 ('S027', 'claimed voter fraud', 'L', 'repetition', 'S002: won the election', 'med', None, 'election chain', 1),
 # S028
 ('S028', 'President Joe Biden', 'L', 'repetition', 'S016: a sitting president', 'high', None, None, 1),
 ('S028', 'the daily intelligence briefing', 'L', 'repetition', 'S020: his daily intelligence briefing document', 'high', None, None, 1),
 ('S028', 'the GSA', 'L', 'repetition', 'S025: the General Services Administration', 'high', None, 'abbreviation', 1),
 # S029
 ('S029', 'Breaking with tradition', 'L', 'repetition', 'S015-S020: the traditions', 'high', None, None, 1),
 ('S029', 'Trump', 'L', 'repetition', 'S027: Trump', 'high', None, None, 1),
 ('S029', 'Biden', 'L', 'repetition', 'S028: President Joe Biden', 'high', None, None, 1),
 ('S029', 'the White House', 'L', 'repetition', 'S016: White House meeting', 'high', None, None, 1),
 # S030
 ('S030', 'Trump', 'L', 'repetition', 'S029: Trump', 'high', None, None, 1),
 ('S030', "this year\u2019s election", 'R', 'demonstrative', 'S002: the November 5 U.S. election', 'high', None, None, 1),
 ('S030', 'established protocol', 'L', 'repetition', 'S013: formalized process', 'med', None, None, 1),
 # S031
 ('S031', 'Biden', 'L', 'repetition', 'S029: Biden', 'high', None, None, 1),
 ('S031', 'Trump', 'L', 'repetition', 'S030: Trump', 'high', None, None, 1),
 ('S031', 'the White House', 'L', 'repetition', 'S029: the White House', 'high', None, None, 1),
 ('S031', 'a smooth transition', 'L', 'repetition', 'S009: seamless and peaceful transfer of power', 'high', None, None, 1),
 # S032
 ('S032', 'The White House', 'L', 'repetition', 'S031: the White House', 'high', None, None, 1),
 ('S032', 'their', 'R', 'personal', 'S031: Biden and Trump', 'high', None, None, 1),
 ('S032', 'meeting', 'L', 'repetition', 'S016: White House meeting', 'high', None, None, 1),
 # S033
 ('S033', 'A White House meet-and-greet', 'L', 'repetition', 'S032: their two-hour meeting', 'high', None, None, 1),
 ('S033', 'the president-elect', 'L', 'repetition', 'S016: a president-elect', 'high', None, None, 1),
 # S034
 ('S034', 'staffing', 'L', 'repetition', 'S006: filling posts', 'med', None, None, 1),
 ('S034', 'a new administration', 'L', 'repetition', 'S009: one administration to another', 'high', None, None, 1),
 # S035
 ('S035', 'The incoming administration', 'L', 'repetition', 'S034: a new administration', 'high', None, None, 1),
 ('S035', 'the Center for Presidential Transition', 'L', 'repetition', 'S007: Center for Presidential Transition', 'high', None, 'verbatim', 1),
 # S036
 ('S036', 'the incoming president', 'L', 'repetition', 'S020: the incoming commander-in-chief', 'high', None, None, 1),
 ('S036', 'inaugurated', 'L', 'repetition', 'S008: Inauguration Day', 'high', None, 'morphological reiteration', 1),
 # S037
 ('S037', 'This', 'R', 'demonstrative', 'S035: fill more than 4,000 positions', 'high', None, None, 1),
 ('S037', 'recruitment', 'L', 'repetition', 'S034: staffing', 'med', None, None, 1),
 # S038
 ('S038', 'Candidates for political positions', 'L', 'repetition', 'S035: 4,000 positions', 'high', None, None, 1),
 ('S038', 'vetted', 'L', 'repetition', 'S023-S025: succession plans and agreements', 'low', None, 'process chain; weak', 1),
 # S039
 ('S039', 'presidents-elect', 'L', 'repetition', 'S033: the president-elect', 'high', None, None, 1),
 ('S039', 'Inauguration Day', 'L', 'repetition', 'S008: Inauguration Day', 'high', None, 'verbatim', 1),
 ('S039', 'appointments', 'L', 'repetition', 'S036: political appointees', 'high', None, 'morphological reiteration', 1),
 # S040
 ('S040', 'Trump', 'L', 'repetition', 'S031: Trump', 'high', None, None, 1),
 ('S040', 'administration officials', 'L', 'repetition', 'S035: The incoming administration', 'high', None, None, 1),
 # S041
 ('S041', 'top-level personnel announcements', 'L', 'repetition', 'S040: picked key administration officials', 'high', None, None, 1),
 # S042
 ('S042', 'these announcements', 'R', 'demonstrative', 'S041: personnel announcements', 'high', None, None, 1),
 ('S042', 'presidential succession', 'L', 'repetition', 'S026: presidential succession', 'high', None, 'verbatim', 1),
 # S043
 ('S043', 'both administrations', 'L', 'repetition', 'S035: The incoming administration', 'high', None, None, 1),
 ('S043', 'share information', 'L', 'repetition', 'S020: shares a copy of his daily intelligence briefing', 'low', None, 'sharing chain; weak', 1),
 # S044
 ('S044', 'Shurkin', 'L', 'repetition', 'S010: Michael Shurkin', 'high', None, None, 1),
 ('S044', 'time and time again', 'L', 'repetition', 'S026: the norm through most of history', 'med', None, None, 1),
 ('S044', 'the Republican exception of 2020-2021', 'L', 'repetition', 'S027: the rupture of 2020', 'high', None, None, 1),
 # S045
 ('S045', 'the government', 'L', 'repetition', 'S025: the federal government\u2019s', 'high', None, None, 1),
 # S046
 ('S046', 'your job', 'R', 'personal', 'S045: people in the vital elements of the government', 'med', None, 'quoted question', 1),
 # S048
 ('S048', 'the Trump and Biden teams', 'L', 'repetition', 'S043: Agency-level teams', 'high', None, None, 1),
 # S049
 ('S049', 'Biden', 'L', 'repetition', 'S048: Biden teams', 'high', None, None, 1),
 ('S049', 'a smooth handover', 'L', 'repetition', 'S031: a smooth transition', 'high', None, None, 1),
 ('S049', "Trump's team", 'L', 'repetition', 'S048: The Trump and Biden teams', 'high', None, None, 1),
 ('S049', 'the White House', 'L', 'repetition', 'S032: The White House', 'high', None, None, 1),
 ('S049', 'GSA', 'L', 'repetition', 'S028: the GSA', 'high', None, None, 1),
 ('S049', 'federal agencies', 'L', 'repetition', 'S023: each federal agency', 'high', None, None, 1),
 # S050
 ('S050', 'Muller', 'L', 'repetition', 'S014: Derek Muller', 'high', None, None, 1),
 ('S050', "Trump's team", 'L', 'repetition', 'S049: Trump\u2019s team', 'high', None, 'verbatim', 1),
 # S051
 ('S051', 'you', 'R', 'personal', 'S050: Muller (addressing the transition team)', 'med', None, 'generic you in quote', 1),
 ('S051', 'federal agencies', 'L', 'repetition', 'S049: federal agencies', 'high', None, 'verbatim', 1),
 # S052
 ('S052', 'The presidential transition', 'L', 'repetition', 'S022: The Presidential Transition Act', 'high', None, None, 1),
 ('S052', 'the outgoing president', 'L', 'repetition', 'S036: the incoming president (counterpart)', 'high', None, None, 1),
 ('S052', 'the incoming president', 'L', 'repetition', 'S036: the incoming president', 'high', None, None, 1),
 # S053
 ('S053', 'the sitting president', 'L', 'repetition', 'S052: the outgoing president', 'high', None, None, 1),
 ('S053', 'January 20', 'L', 'repetition', 'S008: Inauguration Day in January', 'med', None, None, 1),
 # S054
 ('S054', 'This', 'R', 'demonstrative', 'S052-S053: lame duck limits', 'high', None, None, 1),
 ('S054', 'domestic and global affairs', 'L', 'repetition', 'S008: American democracy', 'low', None, 'affairs chain; weak', 1),
 # S055
 ('S055', 'Allies and rivals', 'L', 'repetition', 'S052-S054: the two administrations', 'med', None, None, 1),
 ('S055', 'current and future administrations', 'L', 'repetition', 'S048: The Trump and Biden teams', 'high', None, None, 1),
 # S056
 ('S056', 'Foreign governments', 'L', 'repetition', 'S055: Allies and rivals', 'med', None, None, 1),
 ('S056', 'the U.S.', 'L', 'repetition', 'S005: The United States', 'high', None, 'abbreviation', 1),
 # S057
 ('S057', 'The diplomatic dance', 'L', 'repetition', 'S056: walk a diplomatic tightrope', 'high', None, None, 1),
 # S058
 ('S058', 'foreign governments', 'L', 'repetition', 'S056: Foreign governments', 'high', None, 'verbatim', 1),
 ('S058', 'U.S. embassies', 'L', 'repetition', 'S056: the U.S.', 'high', None, None, 1),
 ('S058', 'Muller', 'L', 'repetition', 'S050: Muller', 'high', None, None, 1),
 ('S058', 'foreign leaders', 'L', 'repetition', 'S056: those with critical ties', 'high', None, None, 1),
 ('S058', 'Trump', 'L', 'repetition', 'S050: Trump\u2019s team', 'high', None, None, 1),
 ('S058', 'a new administration', 'L', 'repetition', 'S055: future administrations', 'high', None, None, 1),
 # S059
 ('S059', 'Earlier this week', 'C', 'temporal', 'S057: The diplomatic dance has already begun', 'high', None, None, 1),
 ('S059', 'Trump', 'L', 'repetition', 'S058: Trump', 'high', None, None, 1),
 # S060
 ('S060', 'the United States', 'L', 'repetition', 'S058: U.S. embassies', 'high', None, 'expansion of abbreviation', 1),
 ('S060', 'foreign government leaders', 'L', 'repetition', 'S058: foreign leaders', 'high', None, None, 1),
 ('S060', 'Muller', 'L', 'repetition', 'S058: Muller', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_11 (§2–§3) ----
 ('S023', None, 'E', 'clausal', 'S023: {the priorities are} (trong câu)', 'low', None, '[TC] biên: khung danh sách không vị ngữ “Among other things:”', 1, 'Among other things:', '{the priorities are}', 'TC'),
 ('S034', None, 'E', 'clausal', 'S034: {is} (trong câu)', 'low', None, '[TC] biên: câu không hệ từ sau dấu hai chấm “Topping the list of priorities: staffing…”', 1, 'Topping the list of priorities: ', '{is}', 'TC'),
 ('S045', None, 'E', 'clausal', 'S044: Shurkin said in an interview with VOA', 'low', None, '[LC] biên: phần 2 trích dẫn Shurkin lược khung dẫn (attribution continuation)', 1, '', '{Shurkin said in an interview with VOA}', 'LC'),
 ('S056', 'those', 'S', 'nominal', 'S055: foreign governments (within sentence)', 'high', None, '[TC] those ← foreign governments; EN 56 “especially those with critical ties”', 1, None, None, 'TC'),
 ('S059', 'the two', 'S', 'nominal', 'S058: Trump and Prabowo Subianto', 'high', None, '[TC] the two ← hai người; định lượng từ trần', 1, None, None, 'TC'),

]

TT = [
 # S002
 ('S002', 'bầu cử', 'L', 'repetition', 'S001: cuộc bầu cử quốc hội', 'high', None, None, 1),
 ('S002', 'tổng thống', 'L', 'repetition', 'S001: thủ tướng', 'med', None, 'head-of-government chain (phép đối)', 1),
 # S003
 ('S003', 'Đảng đối lập', 'L', 'repetition', 'S001: đảng của ông', 'high', None, None, 1),
 # S004
 ('S004', 'Hoa Kỳ', 'L', 'repetition', 'S002: cuộc bầu cử Hoa Kỳ', 'high', None, None, 1),
 ('S004', 'hệ thống như vậy', 'R', 'comparative', 'S003: chính phủ lập sẵn', 'high', None, None, 1),
 # S005
 ('S005', 'Tổng thống tương lai của Hoa Kỳ', 'L', 'repetition', 'S002: trở thành tổng thống', 'high', None, None, 1),
 # S006
 ('S006', 'cai quản', 'L', 'repetition', 'S005: bộ máy của tân chính phủ', 'med', None, None, 1),
 ('S006', 'Chuyển giao Tổng thống', 'L', 'repetition', 'S005: Tổng thống tương lai', 'med', None, 'embedded in proper name', 1),
 # S007
 ('S007', 'Chuyển giao tổng thống', 'L', 'repetition', 'S006: Trung tâm Chuyển giao Tổng thống', 'high', None, None, 1),
 ('S007', 'Ngày bầu cử', 'L', 'repetition', 'S002: cuộc bầu cử Hoa Kỳ', 'med', None, None, 1),
 ('S007', 'năm sau', 'L', 'repetition', 'S001: Vào tháng 7 năm nay', 'low', None, 'temporal echo; weak', 1),
 # S008
 ('S008', 'Khoảng thời gian này', 'L', 'general word', 'S007: 11 tuần quan trọng', 'high', 'R: này', None, 1),
 ('S008', 'chuyển giao quyền lực', 'L', 'repetition', 'S007: Chuyển giao tổng thống', 'high', None, None, 1),
 ('S008', 'chính quyền', 'L', 'repetition', 'S005: tân chính phủ', 'high', None, None, 1),
 # S009
 ('S009', 'họ', 'R', 'personal', 'S008: chính quyền (the incoming teams)', 'med', None, None, 1),
 # S010
 ('S010', 'thời kỳ chuyển tiếp', 'L', 'repetition', 'S008: Khoảng thời gian này', 'high', None, None, 1),
 ('S010', 'lịch sử', 'L', 'repetition', 'S007: nền tảng của nền dân chủ', 'low', None, 'history-democracy chain; weak', 1),
 # S011
 ('S011', 'Ông Riley', 'L', 'repetition', 'S010: Riley', 'high', None, None, 1),
 ('S011', 'chuyển giao quyền lực tổng thống', 'L', 'repetition', 'S007: Chuyển giao tổng thống', 'high', None, None, 1),
 # S012
 ('S012', 'quá trình chuyển tiếp', 'L', 'repetition', 'S010: thời kỳ chuyển tiếp', 'high', None, None, 1),
 ('S012', 'truyền thống', 'L', 'repetition', 'S003: (shadow government implied)', 'low', None, 'first overt tradition mention; weak', 1),
 # S013
 ('S013', 'phong tục', 'L', 'repetition', 'S012: truyền thống', 'med', None, 'custom ~ tradition', 1),
 # S014
 ('S014', 'truyền thống', 'L', 'repetition', 'S012: truyền thống', 'high', None, None, 1),
 # S015
 ('S015', 'cuộc họp tại Tòa Bạch Ốc', 'L', 'repetition', 'S014: truyền thống', 'med', None, 'instance of the traditions', 1),
 ('S015', 'tổng thống đương nhiệm', 'L', 'repetition', 'S002: tổng thống', 'med', None, None, 1),
 # S016
 ('S016', 'Tổng thống Harry Truman', 'L', 'repetition', 'S015: tổng thống đương nhiệm', 'high', None, None, 1),
 ('S016', 'truyền thống này', 'L', 'repetition', 'S014: truyền thống', 'high', 'R: này', None, 1),
 # S017
 ('S017', 'tấm gương này', 'L', 'repetition', 'S016: truyền thống này', 'high', 'R: này', None, 1),
 ('S017', 'Mọi tổng thống', 'L', 'repetition', 'S016: Tổng thống Harry Truman', 'high', None, None, 1),
 ('S017', 'ông Trump', 'L', 'repetition', 'S002: ông Donald Trump', 'high', None, None, 1),
 # S018
 ('S018', 'một truyền thống', 'L', 'repetition', 'S016: truyền thống này', 'high', None, None, 1),
 ('S018', 'tổng thống', 'L', 'repetition', 'S017: Mọi tổng thống', 'high', None, None, 1),
 # S019
 ('S019', 'quá trình chuyển tiếp', 'L', 'repetition', 'S012: quá trình chuyển tiếp', 'high', None, None, 1),
 ('S019', 'pháp luật', 'L', 'repetition', 'S012: luật', 'high', None, None, 1),
 # S020
 ('S020', 'Đạo luật Chuyển tiếp Tổng thống', 'L', 'repetition', 'S011: chuyển giao quyền lực tổng thống', 'high', None, None, 1),
 ('S020', 'chuyển', 'L', 'repetition', 'S011: chuyển giao', 'med', None, 'morphological reiteration', 1),
 # S021
 ('S021', 'cuộc bầu cử', 'L', 'repetition', 'S007: Ngày bầu cử', 'high', None, None, 1),
 ('S021', 'tổng thống', 'L', 'repetition', 'S018: tổng thống', 'high', None, None, 1),
 ('S021', 'chuyển giao', 'L', 'repetition', 'S020: chuyển', 'high', None, 'hội đồng điều phối quá trình chuyển giao', 1),
 # S022
 ('S022', 'kế hoạch kế nhiệm', 'L', 'repetition', 'S021: chuyển giao', 'med', None, None, 1),
 # S023
 ('S023', 'Tổng cục Dịch vụ GSA', 'L', 'repetition', 'S020: Đạo luật (agency chain)', 'med', None, None, 1),
 ('S023', 'các nhóm chuyển giao', 'L', 'repetition', 'S021: quá trình chuyển giao', 'high', None, None, 1),
 # S024
 ('S024', 'những bổ sung', 'L', 'repetition', 'S020: được cập nhật qua nhiều năm', 'med', None, None, 1),
 ('S024', 'kế nhiệm tổng thống', 'L', 'repetition', 'S022: kế hoạch kế nhiệm', 'high', None, None, 1),
 ('S024', 'lịch sử', 'L', 'repetition', 'S010: lịch sử', 'high', None, None, 1),
 # S025
 ('S025', 'Rồi', 'C', 'temporal', 'S024: chuẩn mực trong lịch sử', 'high', None, None, 1),
 ('S025', 'ông Trump', 'L', 'repetition', 'S017: ông Trump', 'high', None, None, 1),
 ('S025', 'bầu cử', 'L', 'repetition', 'S021: cuộc bầu cử', 'high', None, 'tuyên bố gian lận bầu cử', 1),
 # S026
 ('S026', 'Tổng thống Joe Biden', 'L', 'repetition', 'S018: tổng thống', 'high', None, None, 1),
 ('S026', 'báo cáo tình báo hàng ngày', 'L', 'repetition', 'S018: tóm tắt tình báo hàng ngày', 'high', None, None, 1),
 ('S026', 'GSA', 'L', 'repetition', 'S023: Tổng cục Dịch vụ GSA', 'high', None, 'abbreviation', 1),
 # S027
 ('S027', 'truyền thống', 'L', 'repetition', 'S016: truyền thống này', 'high', None, 'Phá vỡ truyền thống', 1),
 ('S027', 'ông Trump', 'L', 'repetition', 'S025: ông Trump', 'high', None, None, 1),
 ('S027', 'ông Biden', 'L', 'repetition', 'S026: Tổng thống Joe Biden', 'high', None, None, 1),
 ('S027', 'Tòa Bạch Ốc', 'L', 'repetition', 'S015: Tòa Bạch Ốc', 'high', None, None, 1),
 # S028
 ('S028', 'ông Trump', 'L', 'repetition', 'S027: ông Trump', 'high', None, None, 1),
 ('S028', 'cuộc bầu cử năm nay', 'L', 'repetition', 'S002: cuộc bầu cử Hoa Kỳ', 'high', 'R: năm nay', None, 1),
 # S029
 ('S029', 'ông Biden', 'L', 'repetition', 'S027: ông Biden', 'high', None, None, 1),
 ('S029', 'ông Trump', 'L', 'repetition', 'S028: ông Trump', 'high', None, None, 1),
 ('S029', 'Tòa Bạch Ốc', 'L', 'repetition', 'S027: Tòa Bạch Ốc', 'high', None, None, 1),
 ('S029', 'chuyển giao', 'L', 'repetition', 'S023: chuyển giao', 'high', None, 'cuộc chuyển giao suôn sẻ', 1),
 # S030
 ('S030', 'Tòa Bạch Ốc', 'L', 'repetition', 'S029: Tòa Bạch Ốc', 'high', None, None, 1),
 ('S030', 'cuộc họp', 'L', 'repetition', 'S015: cuộc họp tại Tòa Bạch Ốc', 'high', None, None, 1),
 # S031
 ('S031', 'Tòa Bạch Ốc', 'L', 'repetition', 'S030: Tòa Bạch Ốc', 'high', None, None, 1),
 ('S031', 'tổng thống đắc cử', 'L', 'repetition', 'S015: một tổng thống đắc cử', 'high', None, None, 1),
 # S032
 ('S032', 'chính quyền mới', 'L', 'repetition', 'S008: chính quyền', 'high', None, None, 1),
 ('S032', 'nhân sự', 'L', 'repetition', 'S005: lấp đầy các vị trí', 'med', None, None, 1),
 # S033
 ('S033', 'chính quyền mới', 'L', 'repetition', 'S032: chính quyền mới', 'high', None, 'verbatim', 1),
 ('S033', 'Trung tâm Chuyển giao Tổng thống', 'L', 'repetition', 'S006: Trung tâm Chuyển giao Tổng thống', 'high', None, 'verbatim', 1),
 ('S033', 'lấp đầy', 'L', 'repetition', 'S005: lấp đầy các vị trí', 'high', None, 'verbatim', 1),
 # S034
 ('S034', 'tân tổng thống', 'L', 'repetition', 'S005: Tổng thống tương lai', 'high', None, None, 1),
 # S035
 ('S035', 'Nỗ lực tuyển dụng', 'L', 'repetition', 'S032: tuyển dụng nhân sự', 'high', None, None, 1),
 # S036
 ('S036', 'Các ứng viên', 'L', 'repetition', 'S033: 4.000 vị trí (positions)', 'med', None, None, 1),
 ('S036', 'các vị trí chính trị', 'L', 'repetition', 'S033: 1.200 vị trí', 'high', None, None, 1),
 # S037
 ('S037', 'các tổng thống đắc cử', 'L', 'repetition', 'S031: tổng thống đắc cử', 'high', None, None, 1),
 ('S037', 'Ngày nhậm chức', 'L', 'repetition', 'S007: Ngày nhậm chức', 'high', None, 'verbatim', 1),
 # S038
 ('S038', 'Ông Trump', 'L', 'repetition', 'S029: ông Trump', 'high', None, None, 1),
 ('S038', 'quan chức chính quyền', 'L', 'repetition', 'S033: chính quyền mới', 'high', None, None, 1),
 # S039
 ('S039', 'thông báo', 'L', 'repetition', 'S038: chọn các quan chức', 'med', None, 'announcement chain', 1),
 # S040
 ('S040', 'những thông báo', 'L', 'repetition', 'S039: thông báo', 'high', None, None, 1),
 ('S040', 'kế nhiệm tổng thống', 'L', 'repetition', 'S024: kế nhiệm tổng thống', 'high', None, 'verbatim', 1),
 # S041
 ('S041', 'cả hai chính quyền', 'L', 'repetition', 'S033: chính quyền mới', 'high', None, None, 1),
 ('S041', 'chia sẻ thông tin', 'L', 'repetition', 'S018: chia sẻ (tóm tắt tình báo)', 'med', None, None, 1),
 ('S041', 'chuyển giao', 'L', 'repetition', 'S029: chuyển giao', 'high', None, None, 1),
 # S042
 ('S042', 'Ông Shurkin', 'L', 'repetition', 'S009: ông Michael Shurkin', 'high', None, None, 1),
 ('S042', 'ngoại trừ đảng Cộng hòa', 'L', 'repetition', 'S025: đứt gãy năm 2020', 'high', None, None, 1),
 # S043
 ('S043', 'chính phủ', 'L', 'repetition', 'S005: bộ máy của tân chính phủ', 'high', None, None, 1),
 # S044
 ('S044', 'Công việc của bạn', 'R', 'personal', 'S043: những người trong cuộc', 'med', None, 'quoted question', 1),
 # S046
 ('S046', 'nhóm của ông Trump và ông Biden', 'L', 'repetition', 'S041: cả hai chính quyền', 'high', None, None, 1),
 # S047
 ('S047', 'Ông Biden', 'L', 'repetition', 'S046: ông Biden', 'high', None, None, 1),
 ('S047', 'chuyển giao suôn sẻ', 'L', 'repetition', 'S029: cuộc chuyển giao suôn sẻ', 'high', None, None, 1),
 ('S047', 'nhóm của ông Trump', 'L', 'repetition', 'S046: nhóm của ông Trump', 'high', None, None, 1),
 ('S047', 'Tòa Bạch Ốc', 'L', 'repetition', 'S031: Tòa Bạch Ốc', 'high', None, None, 1),
 ('S047', 'các cơ quan liên bang', 'L', 'repetition', 'S021: mỗi cơ quan liên bang', 'high', None, None, 1),
 # S048
 ('S048', 'Ông Muller', 'L', 'repetition', 'S013: ông Derek Muller', 'high', None, None, 1),
 ('S048', 'nhóm của ông Trump', 'L', 'repetition', 'S047: nhóm của ông Trump', 'high', None, 'verbatim', 1),
 # S049
 ('S049', 'bạn', 'R', 'personal', 'S048: Ông Muller (addressing the team)', 'med', None, 'generic bạn in quote', 1),
 ('S049', 'các cơ quan liên bang', 'L', 'repetition', 'S047: các cơ quan liên bang', 'high', None, 'verbatim', 1),
 # S050
 ('S050', 'Thời kỳ chuyển giao tổng thống', 'L', 'repetition', 'S020: Đạo luật Chuyển tiếp Tổng thống', 'high', None, None, 1),
 ('S050', 'tổng thống sắp mãn nhiệm', 'L', 'repetition', 'S034: tân tổng thống (counterpart)', 'high', None, None, 1),
 # S051
 ('S051', 'tổng thống đương nhiệm', 'L', 'repetition', 'S050: tổng thống sắp mãn nhiệm', 'high', None, None, 1),
 ('S051', 'ngày 20 tháng 1', 'L', 'repetition', 'S007: Ngày nhậm chức vào tháng 1', 'med', None, None, 1),
 # S052
 ('S052', 'Điều này', 'R', 'demonstrative', 'S050-S051: vịt què limits', 'high', None, None, 1),
 # S053
 ('S053', 'Các đồng minh và đối thủ', 'L', 'repetition', 'S046: nhóm của ông Trump và ông Biden', 'med', None, None, 1),
 ('S053', 'chính quyền hiện tại và tương lai', 'L', 'repetition', 'S046: hai nhóm', 'high', None, None, 1),
 # S054
 ('S054', 'Các chính phủ nước ngoài', 'L', 'repetition', 'S053: các đồng minh và đối thủ', 'med', None, None, 1),
 ('S054', 'Hoa Kỳ', 'L', 'repetition', 'S004: Hoa Kỳ', 'high', None, None, 1),
 # S055
 ('S055', 'Vũ điệu ngoại giao', 'L', 'repetition', 'S054: sợi dây ngoại giao', 'high', None, None, 1),
 # S056
 ('S056', 'các chính phủ nước ngoài', 'L', 'repetition', 'S054: Các chính phủ nước ngoài', 'high', None, 'verbatim', 1),
 ('S056', 'toà đại sứ Hoa Kỳ', 'L', 'repetition', 'S054: Hoa Kỳ', 'high', None, None, 1),
 ('S056', 'ông Muller', 'L', 'repetition', 'S048: Ông Muller', 'high', None, None, 1),
 ('S056', 'các nhà lãnh đạo', 'L', 'repetition', 'S054: những chính phủ (leaders)', 'med', None, None, 1),
 ('S056', 'ông Trump', 'L', 'repetition', 'S048: nhóm của ông Trump', 'high', None, None, 1),
 ('S056', 'chính quyền mới', 'L', 'repetition', 'S053: chính quyền tương lai', 'high', None, None, 1),
 # S057
 ('S057', 'Đầu tuần này', 'C', 'temporal', 'S055: Vũ điệu ngoại giao đã bắt đầu', 'high', None, None, 1),
 ('S057', 'ông Trump', 'L', 'repetition', 'S056: ông Trump', 'high', None, None, 1),
 # S058
 ('S058', 'Hoa Kỳ', 'L', 'repetition', 'S056: Hoa Kỳ', 'high', None, None, 1),
 ('S058', 'các nhà lãnh đạo', 'L', 'repetition', 'S056: các nhà lãnh đạo', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_11 (§2–§3) ----
 ('S032', None, 'E', 'clausal', 'S032: {is} (trong câu)', 'low', None, '[TC] biên: song song E-EN2 “Ưu tiên hàng đầu trong danh sách: tuyển dụng…”', 1, 'Ưu tiên hàng đầu trong danh sách: ', '{là}', 'TC'),
 ('S043', None, 'E', 'clausal', 'S042: Ông Shurkin nói trong một cuộc phỏng vấn với VOA', 'low', None, '[LC] biên: phần 2 trích dẫn Shurkin lược khung dẫn', 1, '', '{Ông Shurkin nói trong một cuộc phỏng vấn với VOA rằng}', 'LC'),

]
