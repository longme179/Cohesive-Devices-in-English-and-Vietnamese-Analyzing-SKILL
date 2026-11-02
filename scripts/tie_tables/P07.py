# P07 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'this', 'R', 'demonstrative', 'S001: This article', 'high', None, 'this is the tale', 1),
 # S004
 ('S004', 'Australians', 'L', 'repetition', 'S002: Australians', 'high', None, None, 1),
 ('S004', 'this question', 'R', 'demonstrative', 'S003: Is Australian English really English?', 'high', None, None, 1),
 # S005
 ('S005', None, 'E', 'nominal', 'S004: asking this question', 'high', None, 'fragment answering S003/S004; no omitted NP recoverable — see note', 1, 'Who’s a “mate”?', 'a mate (the addressee)'),
 # S008
 ('S008', 'This', 'R', 'demonstrative', 'S005-S007: mate / Crikey examples', 'high', None, 'This is confusing', 1),
 # S009
 ('S009', 'But', 'C', 'adversative', 'S008: This is confusing', 'high', None, None, 1),
 ('S009', 'it', 'R', 'personal', 'S008: This (the way Australians communicate)', 'high', None, None, 1),
 ('S009', 'English', 'L', 'repetition', 'S003: English', 'med', None, None, 1),
 # S010
 ('S010', 'English', 'L', 'repetition', 'S009: English', 'high', None, 'sentence-initial topic', 1),
 # S011
 ('S011', 'we', 'R', 'personal', 'S001: This article (authorial we)', 'med', None, 'authorial we', 1),
 ('S011', 'English', 'L', 'repetition', 'S010: English', 'high', None, 'to English', 1),
 # S012
 ('S012', 'We', 'R', 'personal', 'S011: We', 'high', None, None, 1),
 # S013
 ('S013', 'We', 'R', 'personal', 'S012: We', 'high', None, None, 1),
 # S014
 ('S014', 'The people who meet English', 'L', 'repetition', 'S011-S013: Vikings, French, cowboys', 'med', None, 'summary NP', 1),
 # S015
 ('S015', 'Vikings', 'L', 'repetition', 'S011: Viking axes and swords', 'high', None, None, 1),
 ('S015', 'English', 'L', 'repetition', 'S014: English', 'high', None, 'English speakers', 1),
 # S016
 ('S016', 'French', 'L', 'repetition', 'S012: fancy French feasts', 'high', None, None, 1),
 ('S016', 'us', 'R', 'personal', 'S011: we (English speakers)', 'med', None, None, 1),
 # S017
 ('S017', 'American cowboys', 'L', 'repetition', 'S013: American cowboy', 'high', None, None, 1),
 ('S017', 'us', 'R', 'personal', 'S016: us', 'med', None, None, 1),
 # S018
 ('S018', 'tall tales', 'L', 'repetition', 'S017: tall tales', 'high', None, None, 1),
 ('S018', 'English words', 'L', 'repetition', 'S014: its words', 'med', None, None, 1),
 ('S018', 'true', 'L', 'repetition', 'S017: too outlandish to be true', 'high', None, None, 1),
 # S019
 ('S019', 'Australia', 'L', 'repetition', 'S004: Australians', 'med', None, None, 1),
 ('S019', 'words', 'L', 'repetition', 'S018: English words', 'high', None, None, 1),
 ('S019', 'English', 'L', 'repetition', 'S018: English words', 'high', None, 'credibility of English', 1),
 # S020
 ('S020', 'Australian', 'L', 'repetition', 'S019: Australia', 'med', None, 'Australian history', 1),
 # S021
 ('S021', 'Aussie words', 'L', 'repetition', 'S019: its words', 'high', None, None, 1),
 # S022
 ('S022', 'Aussie', 'L', 'repetition', 'S021: Aussie words', 'high', None, 'Aussie ways of speaking', 1),
 ('S022', 'our', 'R', 'personal', 'S001: This article (authorial we)', 'med', None, 'authorial our', 1),
 # S023
 ('S023', 'Australian', 'L', 'repetition', 'S020: Australian history', 'med', None, 'the Australian experience', 1),
 ('S023', 'British', 'L', 'repetition', 'S022: our history', 'low', None, 'first overt British mention; weak', 1),
 # S024
 ('S024', 'the British', 'L', 'repetition', 'S023: British formality', 'high', None, None, 1),
 ('S024', 'Australian', 'L', 'repetition', 'S023: the Australian experience', 'med', None, 'the Australian colony', 1),
 # S025
 ('S025', 'The British', 'L', 'repetition', 'S024: the British', 'high', None, None, 1),
 ('S025', 'called', 'L', 'repetition', 'S024: mocked', 'med', None, None, 1),
 ('S025', 'them', 'R', 'personal', 'S024: those born in the Australian colony', 'high', None, None, 1),
 # S026
 ('S026', 'The British', 'L', 'repetition', 'S025: The British', 'high', None, None, 1),
 ('S026', 'called', 'L', 'repetition', 'S025: called', 'high', None, None, 1),
 ('S026', 'a unit of money', 'L', 'repetition', 'S025: a unit of money', 'high', None, 'parallel construction', 1),
 # S027
 ('S027', 'But', 'C', 'adversative', 'S024-S026: British mockery', 'high', None, None, 1),
 ('S027', 'Aussies', 'L', 'repetition', 'S022: Aussie ways of speaking', 'high', None, None, 1),
 ('S027', 'currency', 'L', 'repetition', 'S025: currency', 'high', None, 'currency lads', 1),
 # S028
 ('S028', 'this', 'R', 'demonstrative', 'S027: pride in being currency lads', 'high', None, 'this obsession', 1),
 ('S028', 'Australia', 'L', 'repetition', 'S024: the Australian colony', 'med', None, None, 1),
 # S030
 ('S030', 'Australians', 'L', 'repetition', 'S027: Aussies', 'med', None, None, 1),
 # S032
 ('S032', 'it’s', 'R', 'personal', 'S031: The word Australian', 'high', None, None, 1),
 # S033
 ('S033', 'British', 'L', 'repetition', 'S026: the British', 'high', None, 'Many British words', 1),
 ('S033', 'Aussie', 'L', 'repetition', 'S027: Aussies', 'high', None, 'the Aussie experience', 1),
 # S034
 ('S034', 'Britain', 'L', 'repetition', 'S033: British', 'high', None, None, 1),
 ('S034', 'Australia', 'L', 'repetition', 'S028: Australia', 'med', None, 'used in Australia', 1),
 # S035
 ('S035', 'Britain', 'L', 'repetition', 'S034: Britain', 'high', None, 'In Britain', 1),
 ('S035', 'larrikin', 'L', 'repetition', 'S002: larrikin', 'high', None, 'echo of the lede', 1),
 # S036
 ('S036', 'Australia', 'L', 'repetition', 'S034: Australia', 'med', None, 'In Australia', 1),
 ('S036', 'larrikin', 'L', 'repetition', 'S035: larrikin', 'high', None, None, 1),
 # S037
 ('S037', 'the “larrikin”', 'L', 'repetition', 'S036: the larrikin', 'high', None, None, 1),
 ('S037', 'Aussies', 'L', 'repetition', 'S033: the Aussie experience', 'high', None, None, 1),
 # S038
 ('S038', 'These stories', 'R', 'demonstrative', 'S037: an underdog story', 'high', None, None, 1),
 ('S038', 'Aussie', 'L', 'repetition', 'S037: Aussies', 'high', None, 'the Aussie experience', 1),
 # S039
 ('S039', 'yarns', 'L', 'repetition', 'S038: yarns', 'high', None, None, 1),
 ('S039', 'We', 'R', 'personal', 'S022: our history (authorial we)', 'med', None, None, 1),
 ('S039', 'English words', 'L', 'repetition', 'S018: English words', 'high', None, None, 1),
 ('S039', 'Aussie', 'L', 'repetition', 'S038: Aussie', 'high', None, 'a more Aussie feel', 1),
 # S040
 ('S040', 'British', 'L', 'repetition', 'S035: Britain', 'high', None, 'a British word', 1),
 # S041
 ('S041', 'Aussies', 'L', 'repetition', 'S039: we', 'high', None, None, 1),
 ('S041', 'British', 'L', 'repetition', 'S040: British word', 'high', None, 'these British origins', 1),
 ('S041', 'yarns', 'L', 'repetition', 'S039: yarns', 'high', None, None, 1),
 ('S041', 'dinkum', 'L', 'repetition', 'S040: Dinkum', 'high', None, None, 1),
 # S042
 ('S042', 'story', 'L', 'repetition', 'S041: a few yarns', 'high', None, 'One story', 1),
 ('S042', 'it', 'R', 'personal', 'S041: dinkum', 'high', None, 'links it to', 1),
 ('S042', 'goldminers', 'L', 'repetition', 'S041: the goldfields', 'med', None, 'phép liên tưởng (association)', 1),
 # S043
 ('S043', 'story', 'L', 'repetition', 'S042: One story', 'high', None, 'Another story', 1),
 ('S043', 'it', 'R', 'personal', 'S042: it (dinkum)', 'high', None, 'attributes it to', 1),
 ('S043', 'goldfields', 'L', 'repetition', 'S041: the goldfields', 'high', None, 'goldfields gamblers', 1),
 ('S043', 'dinkum', 'L', 'repetition', 'S041: dinkum', 'high', None, 'fair dinkum', 1),
 # S044
 ('S044', 'goldfields', 'L', 'repetition', 'S043: goldfields gamblers', 'high', None, 'goldfields stories', 1),
 ('S044', 'stories', 'L', 'repetition', 'S043: Another story', 'high', None, None, 1),
 ('S044', 'Aussie', 'L', 'repetition', 'S041: Aussies', 'high', None, 'Aussie slang', 1),
 ('S044', 'dinkum', 'L', 'repetition', 'S043: fair dinkum', 'high', None, None, 1),
 # S045
 ('S045', 'However', 'C', 'adversative', 'S044: stories almost certainly not true', 'high', None, None, 1),
 ('S045', 'we’ve', 'R', 'personal', 'S039: we', 'med', None, None, 1),
 ('S045', 'story', 'L', 'repetition', 'S044: stories', 'high', None, 'a story', 1),
 # S046
 ('S046', 'stories', 'L', 'repetition', 'S045: a story', 'high', None, 'the more stories', 1),
 # S047
 ('S047', 'And', 'C', 'additive', 'S045-S046: story survival', 'med', None, None, 1),
 ('S047', 'Aussie', 'L', 'repetition', 'S044: Aussie slang', 'high', None, 'Aussie words and stories', 1),
 ('S047', 'stories', 'L', 'repetition', 'S046: stories', 'high', None, None, 1),
 # S048
 ('S048', 'Aussie', 'L', 'repetition', 'S047: Aussie words', 'high', None, 'Aussie relationships', 1),
 ('S048', 'idioms', 'L', 'repetition', 'S001: slang and idioms', 'high', None, 'colourful idioms', 1),
 # S049
 ('S049', 'Aussies', 'L', 'repetition', 'S048: Aussie relationships', 'high', None, None, 1),
 ('S049', 'fair', 'L', 'repetition', 'S048: fairness', 'high', None, 'fair go / fair crack (chain of 4)', 1),
 # S050
 ('S050', 'These', 'R', 'demonstrative', 'S049: fair go idioms', 'high', None, None, 1),
 ('S050', 'idioms', 'L', 'repetition', 'S048: colourful idioms', 'high', None, 'humorous idioms', 1),
 ('S050', 'Aussies', 'L', 'repetition', 'S049: Aussies', 'high', None, None, 1),
 # S051
 ('S051', 'Aussies', 'L', 'repetition', 'S050: Aussies', 'high', None, None, 1),
 # S052
 ('S052', 'Is Australian English really English', 'L', 'repetition', 'S003: Is Australian English really English?', 'high', None, 'verbatim echo of the section opener', 1),
 # S053
 ('S053', 'Almost certainly', 'L', 'repetition', 'S044: almost certainly not true', 'low', None, 'echoed stance adverbial', 1),
 # S054
 ('S054', 'Australian English', 'L', 'repetition', 'S052: Australian English', 'high', None, None, 1),
 ('S054', 'stories', 'L', 'repetition', 'S047: stories', 'high', None, None, 1),
 ('S054', 'British', 'L', 'repetition', 'S041: British origins', 'high', None, 'not British', 1),
 # S055
 ('S055', 'Australian English', 'L', 'repetition', 'S054: Australian English', 'high', None, None, 1),
 ('S055', 'us', 'R', 'personal', 'S039: we', 'med', None, None, 2),
 ('S055', 'Australians', 'L', 'repetition', 'S030: Australians', 'high', None, 'new Australians and old', 1),
 # S056
 ('S056', 'my', 'R', 'personal', 'S022: our history (authorial voice)', 'med', None, 'authorial my', 1),
 # S057
 ('S057', 'He', 'R', 'personal', 'S056: my young son', 'high', None, None, 1),
 ('S057', 'galah', 'L', 'repetition', 'S056: a galah', 'high', None, None, 1),
 ('S057', 'stupid', 'L', 'repetition', 'S051: silly or stupid', 'high', None, None, 1),
 # S058
 ('S058', 'I', 'R', 'personal', 'S056: my (the author)', 'high', None, None, 1),
 # S059
 ('S059', 'He', 'R', 'personal', 'S057: He (my son)', 'high', None, None, 1),
 ('S059', 'that', 'R', 'demonstrative', 'S057: galah means stupid', 'high', None, None, 1),
 # S060
 ('S060', 'Most of them', 'R', 'personal', 'S059: Americans', 'high', None, 'them', 1),
 # S061
 ('S061', 'My', 'R', 'personal', 'S056: my young son', 'high', None, None, 1),
 ('S061', 'Australian', 'L', 'repetition', 'S055: Australian English', 'med', None, 'Australian words', 1),
 # S062
 ('S062', 'They’re', 'R', 'personal', 'S061: Australian words', 'high', None, None, 1),
 ('S062', 'our', 'R', 'personal', 'S061: my ... (the family/authorial voice)', 'med', None, None, 1),
 # S063
 ('S063', 'he', 'R', 'personal', 'S059: He (my son)', 'high', None, None, 1),
 ('S063', 'bird', 'L', 'repetition', 'S056: a galah (the bird)', 'med', None, 'general word', 1),
 # S065
 ('S065', 'I', 'R', 'personal', 'S058: I', 'high', None, None, 1),
 ('S065', 'pink-atoo', 'L', 'repetition', 'S063: pink-atoo', 'high', None, None, 1),
 # S066
 ('S066', 'But', 'C', 'adversative', 'S065: pink-atoo may not catch on', 'high', None, None, 1),
 ('S066', 'Australia English', 'L', 'repetition', 'S055: Australian English', 'high', None, None, 1),
 ('S066', 'stories', 'L', 'repetition', 'S054: past stories', 'high', None, 'collection of stories', 1),
]

TT = [
 # S002
 ('S002', 'đây', 'R', 'demonstrative', 'S001: Bài viết này', 'high', None, 'đây là câu chuyện', 1),
 # S004
 ('S004', 'người Úc', 'L', 'repetition', 'S002: người Úc', 'high', None, None, 1),
 ('S004', 'câu hỏi này', 'R', 'demonstrative', 'S003: Tiếng Anh Úc có thực sự là tiếng Anh không?', 'high', None, None, 1),
 # S008
 ('S008', 'Đúng', 'L', 'repetition', 'S005-S007: mate / Crikey examples', 'med', None, 'Đúng là khó hiểu thật summarises the examples', 1),
 # S009
 ('S009', 'Nhưng', 'C', 'adversative', 'S008: Đúng là khó hiểu', 'high', None, None, 1),
 ('S009', 'đó', 'R', 'demonstrative', 'S008: cách người Úc dùng từ (the examples)', 'med', None, 'chắc chắn đó là tiếng Anh', 1),
 ('S009', 'tiếng Anh', 'L', 'repetition', 'S003: tiếng Anh', 'med', None, None, 1),
 # S010
 ('S010', 'Tiếng Anh', 'L', 'repetition', 'S009: tiếng Anh', 'high', None, 'sentence-initial topic', 1),
 # S011
 ('S011', 'chúng ta', 'R', 'personal', 'S001: Bài viết này (authorial chúng ta)', 'med', None, 'authorial chúng ta', 1),
 ('S011', 'tiếng Anh', 'L', 'repetition', 'S010: Tiếng Anh', 'high', None, 'lắng nghe tiếng Anh', 1),
 # S012
 ('S012', 'Chúng ta', 'R', 'personal', 'S011: chúng ta', 'high', None, None, 1),
 # S013
 ('S013', 'Chúng ta', 'R', 'personal', 'S012: Chúng ta', 'high', None, None, 1),
 # S014
 ('S014', 'Những người từng nói tiếng Anh', 'L', 'repetition', 'S011-S013: Viking, Pháp, cao bồi Mỹ', 'med', None, 'summary NP', 1),
 ('S014', 'ngôn ngữ này', 'L', 'repetition', 'S010: Tiếng Anh', 'high', 'R: này', 'general word + demonstrative', 1),
 # S015
 ('S015', 'Viking', 'L', 'repetition', 'S011: rìu và kiếm Viking', 'high', None, None, 1),
 ('S015', 'người nói tiếng Anh', 'L', 'repetition', 'S014: Những người từng nói tiếng Anh', 'high', None, None, 1),
 # S016
 ('S016', 'Pháp', 'L', 'repetition', 'S012: kiểu Pháp', 'high', None, None, 1),
 ('S016', 'chúng ta', 'R', 'personal', 'S011: chúng ta', 'med', None, None, 1),
 # S017
 ('S017', 'cao bồi Mỹ', 'L', 'repetition', 'S013: chàng cao bồi Mỹ', 'high', None, None, 1),
 ('S017', 'chúng ta', 'R', 'personal', 'S016: chúng ta', 'med', None, None, 1),
 # S018
 ('S018', 'những câu chuyện cổ tích', 'L', 'repetition', 'S017: những câu chuyện cổ tích', 'high', None, None, 1),
 ('S018', 'từ tiếng Anh mới', 'L', 'repetition', 'S014: trong ngôn ngữ này (its words)', 'med', None, None, 1),
 ('S018', 'sự thật', 'L', 'repetition', 'S017: khó có thể là sự thật', 'high', None, None, 1),
 # S019
 ('S019', 'Nước Úc', 'L', 'repetition', 'S004: người Úc', 'med', None, 'Úc morphological chain', 1),
 ('S019', 'tiếng Anh Úc', 'L', 'repetition', 'S003: Tiếng Anh Úc', 'high', None, None, 1),
 # S020
 ('S020', 'Úc', 'L', 'repetition', 'S019: Nước Úc', 'med', None, 'Lịch sử Úc', 1),
 # S021
 ('S021', 'từ ngữ Úc', 'L', 'repetition', 'S018: từ tiếng Anh mới', 'high', None, None, 1),
 ('S021', 'những câu chuyện', 'L', 'repetition', 'S018: những câu chuyện cổ tích', 'high', None, None, 1),
 # S022
 ('S022', 'người Úc', 'L', 'repetition', 'S019: Nước Úc', 'med', None, 'Cách nói chuyện của người Úc', 1),
 # S023
 ('S023', 'người Úc', 'L', 'repetition', 'S022: người Úc', 'high', None, 'trải nghiệm của người Úc', 1),
 ('S023', 'người Anh', 'L', 'repetition', 'S022: (first overt mention)', 'low', None, 'first overt British mention; weak', 1),
 # S024
 ('S024', 'người Anh', 'L', 'repetition', 'S023: người Anh', 'high', None, None, 1),
 ('S024', 'thuộc địa Úc', 'L', 'repetition', 'S023: trải nghiệm của người Úc', 'med', None, 'Úc chain', 1),
 # S025
 ('S025', 'Người Anh', 'L', 'repetition', 'S024: người Anh', 'high', None, None, 1),
 ('S025', 'gọi', 'L', 'repetition', 'S024: chế giễu', 'med', None, None, 1),
 ('S025', 'họ', 'R', 'personal', 'S024: những người sinh ra ở thuộc địa Úc', 'high', None, None, 1),
 # S026
 ('S026', 'Người Anh', 'L', 'repetition', 'S025: Người Anh', 'high', None, None, 1),
 ('S026', 'gọi', 'L', 'repetition', 'S025: gọi', 'high', None, None, 1),
 ('S026', 'đơn vị tiền tệ', 'L', 'repetition', 'S025: đơn vị tiền tệ', 'high', None, 'parallel construction', 1),
 # S027
 ('S027', 'Thế nhưng', 'C', 'adversative', 'S024-S026: British mockery', 'high', None, None, 1),
 ('S027', 'người Úc', 'L', 'repetition', 'S024: thuộc địa Úc', 'high', None, None, 1),
 ('S027', 'tiền tệ', 'L', 'repetition', 'S025: tiền tệ', 'high', None, 'những chàng trai tiền tệ', 1),
 # S028
 ('S028', 'này', 'R', 'demonstrative', 'S027: tự hào về địa vị currency lads', 'high', None, 'nỗi ám ảnh ... này', 1),
 ('S028', 'nước Úc', 'L', 'repetition', 'S019: Nước Úc', 'med', None, None, 1),
 # S030
 ('S030', 'người Úc', 'L', 'repetition', 'S027: người Úc', 'med', None, None, 1),
 # S032
 ('S032', 'Ta', 'R', 'personal', 'S029-S031: implicit speakers of Australian English', 'med', None, 'generic ta; weak chain to authorial voice', 1),
 # S033
 ('S033', 'từ tiếng Anh', 'L', 'repetition', 'S018: từ tiếng Anh mới', 'high', None, 'Nhiều từ tiếng Anh', 1),
 ('S033', 'người Úc', 'L', 'repetition', 'S030: người Úc', 'high', None, 'trải nghiệm của người Úc', 1),
 # S034
 ('S034', 'Anh', 'L', 'repetition', 'S033: tiếng Anh (British side)', 'high', None, 'ở Anh', 1),
 ('S034', 'Úc', 'L', 'repetition', 'S033: người Úc', 'med', None, 'ở Úc', 1),
 # S035
 ('S035', 'Anh', 'L', 'repetition', 'S034: Anh', 'high', None, 'Ở Anh', 1),
 ('S035', 'larrikin', 'L', 'repetition', 'S002: larrikin', 'high', None, 'echo of the lede', 1),
 # S036
 ('S036', 'Úc', 'L', 'repetition', 'S034: Úc', 'med', None, 'Ở Úc', 1),
 ('S036', 'larrikin', 'L', 'repetition', 'S035: larrikin', 'high', None, None, 1),
 # S037
 ('S037', 'larrikin', 'L', 'repetition', 'S036: larrikin', 'high', None, None, 1),
 ('S037', 'người Úc', 'L', 'repetition', 'S033: người Úc', 'high', None, None, 1),
 # S038
 ('S038', 'Những câu chuyện này', 'R', 'demonstrative', 'S037: các câu chuyện về những kẻ yếu', 'high', None, None, 1),
 ('S038', 'người Úc', 'L', 'repetition', 'S037: người Úc', 'high', None, None, 1),
 # S039
 ('S039', 'câu chuyện', 'L', 'repetition', 'S038: Những câu chuyện này', 'high', None, None, 1),
 ('S039', 'Chúng ta', 'R', 'personal', 'S011: chúng ta (authorial)', 'med', None, None, 1),
 ('S039', 'từ ngữ tiếng Anh', 'L', 'repetition', 'S033: từ tiếng Anh', 'high', None, None, 1),
 ('S039', 'Úc', 'L', 'repetition', 'S038: người Úc', 'high', None, 'cảm giác kiểu Úc', 1),
 # S040
 ('S040', 'tiếng Anh', 'L', 'repetition', 'S035: Anh', 'high', None, 'một từ tiếng Anh (British)', 1),
 # S041
 ('S041', 'người Úc', 'L', 'repetition', 'S039: chúng ta', 'high', None, None, 1),
 ('S041', 'Anh', 'L', 'repetition', 'S040: tiếng Anh', 'high', None, 'nguồn gốc Anh', 1),
 ('S041', 'câu chuyện', 'L', 'repetition', 'S039: câu chuyện', 'high', None, None, 1),
 ('S041', 'dinkum', 'L', 'repetition', 'S040: Dinkum', 'high', None, None, 1),
 # S042
 ('S042', 'câu chuyện', 'L', 'repetition', 'S041: một vài câu chuyện', 'high', None, None, 1),
 ('S042', 'từ này', 'L', 'repetition', 'S041: dinkum', 'high', 'R: này', None, 1),
 ('S042', 'thợ đào vàng', 'L', 'repetition', 'S041: các mỏ vàng', 'med', None, 'phép liên tưởng (association)', 1),
 # S043
 ('S043', 'câu chuyện', 'L', 'repetition', 'S042: Một câu chuyện', 'high', None, None, 1),
 ('S043', 'từ này', 'L', 'repetition', 'S042: từ này', 'high', 'R: này', None, 1),
 ('S043', 'đào vàng', 'L', 'repetition', 'S042: thợ đào vàng', 'high', None, 'những kẻ đào vàng', 1),
 ('S043', 'dinkum', 'L', 'repetition', 'S041: dinkum', 'high', None, 'fair dinkum', 1),
 # S044
 ('S044', 'mỏ vàng', 'L', 'repetition', 'S043: đào vàng', 'high', None, 'Những câu chuyện về mỏ vàng', 1),
 ('S044', 'câu chuyện', 'L', 'repetition', 'S043: Một câu chuyện khác', 'high', None, None, 1),
 ('S044', 'người Úc', 'L', 'repetition', 'S041: người Úc', 'high', None, 'tiếng lóng ... của người Úc', 1),
 ('S044', 'dinkum', 'L', 'repetition', 'S043: fair dinkum', 'high', None, None, 1),
 # S045
 ('S045', 'Tuy nhiên', 'C', 'adversative', 'S044: gần như chắc chắn không có thật', 'high', None, None, 1),
 ('S045', 'chúng ta', 'R', 'personal', 'S039: chúng ta', 'med', None, None, 1),
 ('S045', 'câu chuyện', 'L', 'repetition', 'S044: câu chuyện', 'high', None, None, 1),
 # S046
 ('S046', 'câu chuyện', 'L', 'repetition', 'S045: câu chuyện', 'high', None, None, 1),
 # S047
 ('S047', 'Và', 'C', 'additive', 'S045-S046: story survival', 'med', None, None, 1),
 ('S047', 'người Úc', 'L', 'repetition', 'S044: người Úc', 'high', None, 'từ ngữ và câu chuyện của người Úc', 1),
 ('S047', 'câu chuyện', 'L', 'repetition', 'S046: câu chuyện', 'high', None, None, 1),
 # S048
 ('S048', 'người Úc', 'L', 'repetition', 'S047: người Úc', 'high', None, 'Các mối quan hệ của người Úc', 1),
 ('S048', 'thành ngữ', 'L', 'repetition', 'S001: thành ngữ', 'high', None, 'thành ngữ đầy màu sắc', 1),
 # S049
 ('S049', 'Người Úc', 'L', 'repetition', 'S048: người Úc', 'high', None, None, 1),
 ('S049', 'fair', 'L', 'repetition', 'S048: công bằng', 'med', None, 'fair go / fair crack (chain of 4)', 1),
 # S050
 ('S050', 'Những thành ngữ hài hước này', 'R', 'demonstrative', 'S049: các thành ngữ fair', 'high', None, None, 1),
 ('S050', 'người Úc', 'L', 'repetition', 'S049: Người Úc', 'high', None, None, 1),
 # S051
 ('S051', 'người Úc', 'L', 'repetition', 'S050: người Úc', 'high', None, None, 1),
 # S052
 ('S052', 'Tiếng Anh Úc có thực sự là tiếng Anh không', 'L', 'repetition', 'S003: Tiếng Anh Úc có thực sự là tiếng Anh không?', 'high', None, 'verbatim echo of the section opener', 1),
 # S053
 ('S053', 'Gần như chắc chắn', 'L', 'repetition', 'S044: gần như chắc chắn', 'low', None, 'echoed stance adverbial', 1),
 # S054
 ('S054', 'Tiếng Anh Úc', 'L', 'repetition', 'S052: Tiếng Anh Úc', 'high', None, None, 1),
 ('S054', 'câu chuyện', 'L', 'repetition', 'S047: câu chuyện', 'high', None, None, 1),
 # S055
 ('S055', 'Tuy nhiên', 'C', 'adversative', 'S054: defined by past stories', 'high', None, None, 1),
 ('S055', 'tiếng Anh Úc', 'L', 'repetition', 'S054: Tiếng Anh Úc', 'high', None, None, 1),
 ('S055', 'chúng ta', 'R', 'personal', 'S045: chúng ta', 'med', None, None, 1),
 ('S055', 'người Úc', 'L', 'repetition', 'S030: người Úc', 'high', None, 'người Úc mới và cũ', 1),
 # S056
 ('S056', 'của tôi', 'R', 'personal', 'S022: (authorial voice)', 'med', None, 'authorial của tôi', 1),
 # S057
 ('S057', 'Nó', 'R', 'personal', 'S056: con trai nhỏ của tôi', 'high', None, None, 1),
 ('S057', 'galah', 'L', 'repetition', 'S056: một con galah', 'high', None, None, 1),
 ('S057', 'ngớ ngẩn', 'L', 'repetition', 'S051: ngớ ngẩn (silly)', 'high', None, None, 1),
 # S058
 ('S058', 'Tôi', 'R', 'personal', 'S056: của tôi (the author)', 'high', None, None, 1),
 # S059
 ('S059', 'Nó', 'R', 'personal', 'S057: Nó (my son)', 'high', None, None, 1),
 ('S059', 'điều này', 'R', 'demonstrative', 'S057: galah có nghĩa là ngớ ngẩn', 'high', None, None, 1),
 # S060
 ('S060', 'Hầu hết họ', 'R', 'personal', 'S059: Người Mỹ', 'high', None, None, 1),
 # S061
 ('S061', 'của tôi', 'R', 'personal', 'S056: con trai nhỏ của tôi', 'high', None, None, 1),
 ('S061', 'Úc', 'L', 'repetition', 'S055: Tiếng Anh Úc', 'med', None, 'các từ ngữ Úc', 1),
 # S062
 ('S062', 'Chúng', 'R', 'personal', 'S061: các từ ngữ Úc', 'high', None, None, 1),
 ('S062', 'của chúng ta', 'R', 'personal', 'S061: của tôi (family/authorial voice)', 'med', None, None, 1),
 # S063
 ('S063', 'nó', 'R', 'personal', 'S059: Nó (my son)', 'high', None, None, 1),
 ('S063', 'con chim đó', 'L', 'general word', 'S056: một con galah (the bird)', 'med', 'R: đó', None, 1),
 # S065
 ('S065', 'Tôi', 'R', 'personal', 'S058: Tôi', 'high', None, None, 1),
 ('S065', 'pink-atoo', 'L', 'repetition', 'S063: pink-atoo', 'high', None, None, 1),
 # S066
 ('S066', 'Nhưng', 'C', 'adversative', 'S065: không chắc được ưa chuộng', 'high', None, None, 1),
 ('S066', 'tiếng Anh Úc', 'L', 'repetition', 'S055: Tiếng Anh Úc', 'high', None, None, 1),
 ('S066', 'câu chuyện', 'L', 'repetition', 'S054: câu chuyện', 'high', None, 'bộ sưu tập các câu chuyện', 1),
]
