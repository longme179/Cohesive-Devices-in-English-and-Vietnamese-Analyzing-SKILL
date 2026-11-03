# P05 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'changes', 'L', 'repetition', 'S001: a wave of changes', 'high', None, None, 1),
 # S003
 ('S003', 'the new wage-theft laws', 'L', 'repetition', 'S002: laws that come into effect', 'med', 'R: the', 'general word wages/theft + repetition of laws', 1),
 ('S003', 'underpayment', 'L', 'repetition', 'S002: underpay their employees', 'high', None, 'morphological reiteration', 1),
 # S004
 ('S004', 'fines', 'L', 'repetition', 'S003: could be fined', 'high', None, 'morphological reiteration', 1),
 # S005
 ('S005', 'the new', 'L', 'repetition', 'S003: the new wage-theft laws', 'low', None, 'formulaic new in the list genre; weak', 1),
 ('S005', 'underpayment', 'L', 'repetition', 'S003: underpayment', 'high', None, 'unintentional underpayment', 1),
 ('S005', 'penalties', 'L', 'synonym', 'S004: fines', 'med', None, None, 1),
 # S006
 ('S006', 'Australian', 'L', 'repetition', 'S001: Australians', 'med', None, 'Australian citizenship', 1),
 # S007
 ('S007', 'Applicants', 'L', 'repetition', 'S006: Residents ... will be able to', 'high', None, None, 1),
 # S008
 ('S008', 'The change', 'L', 'general word', 'S006: fast-track citizenship policy', 'high', 'R: the', None, 1),
 ('S008', 'applications', 'L', 'repetition', 'S007: applying', 'high', None, 'morphological reiteration', 1),
 ('S008', 'ADF', 'L', 'repetition', 'S006: (ADF)', 'high', None, 'abbreviation', 1),
 # S009
 ('S009', 'applicants', 'L', 'repetition', 'S007: Applicants', 'high', None, None, 1),
 ('S009', 'apply', 'L', 'repetition', 'S008: applications', 'high', None, 'morphological reiteration', 1),
 ('S009', 'citizenship', 'L', 'repetition', 'S006: Australian citizenship', 'high', None, None, 1),
 # S010
 ('S010', 'ADF', 'L', 'repetition', 'S008: ADF', 'high', None, None, 1),
 # S011
 ('S011', 'Australians', 'L', 'repetition', 'S006: Australian', 'med', None, None, 1),
 ('S011', '1 January', 'L', 'repetition', 'S002: taking effect on 1 January', 'med', None, 'section date echo', 1),
 # S012
 ('S012', 'Youth Allowance and Austudy', 'L', 'repetition', 'S011: Youth Allowance, Austudy', 'high', None, None, 1),
 ('S012', 'payments', 'L', 'repetition', 'S011: Centrelink payment increase', 'high', None, None, 1),
 # S013
 ('S013', 'Australians', 'L', 'repetition', 'S011: Australians', 'med', None, None, 1),
 ('S013', 'ABSTUDY', 'L', 'repetition', 'S011: ABSTUDY', 'high', None, None, 1),
 ('S013', 'a fortnight', 'L', 'repetition', 'S012: a fortnight', 'med', None, None, 1),
 # S014
 ('S014', 'Those', 'S', 'nominal', 'S011-S013: người hưởng Youth Allowance/Austudy/ABSTUDY (câu trước)', 'high', None, '[LC] those ← người hưởng các khoản trợ cấp ở S011–S013; đánh dấu lại thành S (nhãn R cũ bị thay theo §3)', 1, None, None, 'LC'),
 ('S014', 'a fortnight', 'L', 'repetition', 'S013: a fortnight', 'med', None, None, 1),
 # S015
 ('S015', 'also', 'C', 'additive', 'S012-S014: payment rises', 'med', None, None, 1),
 ('S015', 'payments', 'L', 'repetition', 'S012: payments', 'high', None, None, 1),
 # S016
 ('S016', 'More', 'R', 'comparative', 'S011-S015: details of the changes', 'low', None, 'More details; quantity reference', 1),
 # S017
 ('S017', 'Australian', 'L', 'repetition', 'S011: Australians', 'med', None, 'Australian passport', 1),
 ('S017', 'increase', 'L', 'repetition', 'S011: payment increase', 'med', None, 'same verb across sections (list genre)', 1),
 # S018
 ('S018', '1 January', 'L', 'repetition', 'S011: 1 January', 'med', None, None, 1),
 ('S018', 'Australian passport', 'L', 'repetition', 'S017: Australian passport prices', 'high', None, None, 1),
 ('S018', '2024', 'L', 'repetition', 'S017: 2025 due to annual indexation', 'low', None, 'year pair', 1),
 # S019
 ('S019', 'This', 'R', 'demonstrative', 'S018: $412 passport cost', 'high', None, None, 1),
 ('S019', "Australia's", 'L', 'repetition', 'S017: Australian passport', 'med', None, None, 1),
 # S020
 ('S020', '1 January', 'L', 'repetition', 'S018: 1 January', 'med', None, None, 1),
 ('S020', 'Australians', 'L', 'repetition', 'S017: Australian', 'med', None, None, 1),
 # S021
 ('S021', 'surcharges', 'L', 'repetition', 'S020: debit card surcharges', 'high', None, None, 1),
 # S022
 ('S022', 'gaming areas', 'L', 'repetition', 'S021: gaming areas', 'high', None, None, 1),
 # S023
 ('S023', 'also', 'C', 'additive', 'S022: ATMs not allowed within 5m', 'med', None, None, 1),
 ('S023', 'gaming rooms', 'L', 'repetition', 'S022: gaming areas', 'high', None, None, 1),
 # S024
 ('S024', 'Additionally', 'C', 'additive', 'S022-S023: ATM placement bans', 'high', None, None, 1),
 ('S024', 'gaming areas', 'L', 'repetition', 'S023: gaming rooms', 'high', None, None, 1),
 ('S024', 'ATMs', 'L', 'repetition', 'S022: ATMs', 'high', None, None, 1),
 # S025
 ('S025', '1 January', 'L', 'repetition', 'S020: 1 January', 'med', None, None, 1),
 ('S025', 'Australian', 'L', 'repetition', 'S020: Australians', 'med', None, 'large Australian businesses', 1),
 # S027
 ('S027', '1 January', 'L', 'repetition', 'S025: 1 January', 'med', None, None, 1),
 ('S027', 'classifications', 'L', 'repetition', 'S026: entry-level work classifications', 'high', None, None, 1),
 # S028
 ('S028', 'classifications', 'L', 'repetition', 'S027: introductory classifications', 'high', None, None, 1),
 ('S028', 'this period', 'R', 'demonstrative', 'S027: six months', 'high', None, None, 1),
 # S029
 ('S029', 'This', 'R', 'demonstrative', 'S028: progression to higher classifications', 'high', None, None, 1),
 ('S029', 'employees', 'L', 'repetition', 'S028: Employees', 'high', None, None, 1),
 ('S029', 'minimum wage', 'L', 'repetition', 'S026: minimum wage requirements', 'high', None, None, 1),
 # S030
 ('S030', 'A ban', 'L', 'repetition', 'S025: new regulations', 'low', None, 'ban fresh in this section; weak cross-section link', 1),
 # S031
 ('S031', 'It', 'R', 'personal', 'S030: A ban on the importation', 'high', None, None, 1),
 ('S031', 'ban', 'L', 'repetition', 'S030: A ban', 'high', None, None, 1),
 ('S031', 'engineered stone bench tops, panels and slabs', 'L', 'repetition', 'S030: engineered stone bench tops, panels and slabs', 'high', None, 'verbatim', 1),
 ('S031', 'came into effect', 'L', 'repetition', 'S002: laws that come into effect', 'med', None, 'cross-section echo (list genre)', 1),
 # S032
 ('S032', 'The material', 'L', 'general word', 'S030-S031: engineered stone', 'high', None, None, 1),
 ('S032', 'kitchen bench tops', 'L', 'repetition', 'S030: kitchen benches', 'high', None, 'near-verbatim', 1),
 # S033
 ('S033', 'Australian', 'L', 'repetition', 'S025: Australian', 'med', None, 'Australian resident', 1),
 # S034
 ('S034', 'But', 'C', 'adversative', 'S033: current clearance certificate rule', 'high', None, None, 1),
 ('S034', '1 January', 'L', 'repetition', 'S027: 1 January', 'med', None, None, 1),
 ('S034', 'withholding', 'L', 'repetition', 'S033: having 12.5 per cent withheld', 'high', None, 'morphological reiteration', 1),
 ('S034', 'property', 'L', 'repetition', 'S033: property sale', 'high', None, 'property threshold', 1),
 # S035
 ('S035', '1 January', 'L', 'repetition', 'S034: 1 January', 'med', None, None, 1),
 ('S035', 'Centrelink', 'L', 'repetition', 'S011: Centrelink payment increase', 'high', None, 'cross-section echo', 1),
 # S036
 ('S036', 'The change', 'L', 'general word', 'S035: Centrelink medical exemption extension', 'high', 'R: the', None, 1),
 ('S036', 'welfare', 'L', 'repetition', 'S002: welfare payment hikes', 'high', None, 'cross-section echo', 1),
 ('S036', 'those', 'S', 'nominal', 'S036: in select welfare recipient groups (trong câu)', 'high', None, '[TC] those ← nhóm người hưởng phúc lợi trong cùng câu; đánh dấu lại thành S (nhãn R cũ bị thay theo §3)', 1, None, None, 'TC'),
 # S037
 ('S037', 'applicants', 'L', 'repetition', 'S006-S009: Applicants ... applicants', 'med', None, 'cross-section echo (visa section)', 1),
 # S038
 ('S038', 'This change', 'L', 'general word', 'S037: new student visa rules', 'high', 'R: this', None, 1),
 ('S038', 'study', 'L', 'repetition', 'S037: student visa', 'high', None, 'morphological reiteration', 1),
 # S039
 ('S039', 'applications', 'L', 'repetition', 'S037: time of application', 'high', None, 'morphological reiteration', 1),
 ('S039', 'CoE', 'L', 'repetition', 'S037: (CoE)', 'high', None, 'abbreviation', 1),
 # S040
 # S041
 ('S041', 'This expansion', 'L', 'general word', 'S040: will expand to include', 'high', 'R: this', None, 1),
 ('S041', 'medications', 'L', 'repetition', 'S040: PBS medicines', 'high', None, None, 1),
 # S042
 ('S042', '1 January', 'L', 'repetition', 'S035: 1 January', 'med', None, None, 1),
 ('S042', 'medical', 'L', 'repetition', 'S035: medical exemptions', 'med', None, 'cross-section echo', 1),
 # S043
 ('S043', 'Safety Net threshold', 'L', 'repetition', 'S042: qualifying for a higher rebate', 'med', None, 'threshold concept link', 1),
 ('S043', 'Medicare', 'L', 'repetition', 'S042: out-of-hospital medical expenses', 'high', None, None, 1),
 # S044
 ('S044', 'PBS co-payment', 'L', 'repetition', 'S040: PBS Co-payment Program', 'high', None, None, 1),
 # S045
 ('S045', 'The co-payments', 'L', 'repetition', 'S044: PBS co-payment', 'high', None, None, 1),
 # S046
 ('S046', 'Wage changes', 'L', 'repetition', 'S002-S003: wage-theft laws', 'med', None, 'cross-section echo', 1),
 ('S046', '1 January', 'L', 'repetition', 'S042: 1 January', 'med', None, None, 1),
 ('S046', 'awards', 'L', 'repetition', 'S027: introductory classifications in awards', 'med', None, 'cross-section echo', 1),
 # S047
 ('S047', 'Minimum pay rates', 'L', 'repetition', 'S046: Wage changes', 'high', None, None, 1),
 ('S047', 'Aged Care Award', 'L', 'repetition', 'S046: those working in aged care', 'high', None, None, 1),
 # S048
 ('S048', 'Aged Care Award workers', 'L', 'repetition', 'S047: Aged Care Award', 'high', None, None, 1),
 ('S048', 'minimum pay rate', 'L', 'repetition', 'S047: Minimum pay rates', 'high', None, 'singular variant', 1),
 # S049
 ('S049', '1 January', 'L', 'repetition', 'S046: 1 January', 'med', None, None, 1),
 # S050
 ('S050', 'your health fund', 'L', 'repetition', 'S049: health insurance companies', 'high', None, None, 1),
 # S051
 ('S051', 'Australia', 'L', 'repetition', 'S019: Australia\u2019s', 'med', None, None, 1),
 # S052
 ('S052', 'new cars', 'L', 'repetition', 'S051: Any new cars sold in Australia', 'high', None, None, 1),
 # S053
 ('S053', '1 January', 'L', 'repetition', 'S049: 1 January', 'med', None, None, 1),
 # S054
 ('S054', 'The levy', 'L', 'repetition', 'S053: pay a levy', 'high', None, None, 1),
 # S055
 ('S055', 'Those', 'S', 'nominal', 'S055: chủ sở hữu bất động sản cho thuê (trong câu; nối về EN 48)', 'high', None, '[TC] those ← chủ bất động sản; đánh dấu lại thành S (nhãn R cũ bị thay theo §3)', 1, None, None, 'TC'),
 # S056
 ('S056', "Victoria's", 'L', 'repetition', 'S053: Victorian property owners', 'high', None, None, 1),
 # S057
 ('S057', 'The tax', 'L', 'repetition', 'S056: vacant residential land tax', 'high', None, None, 1),
 ('S057', 'property', 'L', 'repetition', 'S053-S054: property owners / booking fee context', 'med', None, None, 1),
 # S058
 ('S058', 'holiday houses', 'L', 'repetition', 'S056: vacant residential land', 'med', None, 'associated term (phép liên tưởng)', 1),
 # S059
 ('S059', 'cost of living relief', 'L', 'repetition', 'S002: welfare payment hikes', 'low', None, 'cross-section echo; weak', 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_05 (§2–§3) ----
 # [LC] = liên câu; [TC] = trong câu. Người đọc bản phân tích chọn vị trí;
 # không dùng regex/đếm chuỗi để sinh tie. S-EN1/2/5 đã đánh dấu lại tại chỗ
 # (S014, S036, S055) nên khối này chỉ thêm S-EN3/4 cùng 7 dòng E.
 ('S046', 'those', 'S', 'nominal', 'S046: several awards (trong câu)', 'high', None, '[TC] those ← người lao động theo các award; tiền ngữ lỏng lẻo “awards… those working” (nguồn §8.7)', 1, None, None, 'TC'),
 ('S047', 'those', 'S', 'nominal', 'S047: Aged Care Award, Nurses Award… (trong câu)', 'high', None, '[TC] those ← người lao động trong các ngành/award', 1, None, None, 'TC'),
 ('S003', None, 'E', 'clausal', 'S003: vế “or … $7.82 million” (trong câu)', 'high', None, '[TC] gapping vế hoặc: “or {companies could be fined up to} $7.82 million”; EN 4', 1, 'amount, or ', '{companies could be fined up to}', 'TC'),
 ("S036", None, 'E', 'nominal', 'S036: vế “and unable to work” (trong câu)', 'high', None, "[TC] lược chủ ngữ + hệ từ vế tọa hợp: “and {you're} unable to work”; EN 34", 1, 'sick or injured and ', "{you're}", 'TC'),
 ('S050', None, 'E', 'nominal', 'S050: mệnh lệnh “Check with your health fund” (trong câu)', 'high', None, '[TC] mệnh lệnh lược chủ ngữ {you}: “∅ Check with your health fund”; EN 45 (khối bị VI lược)', 1, '', '{you}', 'TC'),
 ('S058', None, 'E', 'nominal', 'S058: vế “if used for at least four weeks” (trong câu)', 'high', None, '[TC] lược chủ ngữ + trợ động từ bị động vế if: “if {they are} used”; EN 52', 1, 'exempt if ', '{they are}', 'TC'),
 ('S018', None, 'E', 'clausal', 'S018: vế “up $14 from 2024” (trong câu)', 'low', None, '[TC] biên: vế bổ trợ rút gọn “{which is} up $14 from 2024”; EN 18', 1, 'hit $412, ', '{which is}', 'TC'),
 ('S030', None, 'E', 'clausal', 'S030: vế “commonly used for kitchen benches” (trong câu)', 'low', None, '[TC] biên: quan hệ từ rút gọn “{which are} commonly used…”; EN 29 (khối bị VI lược)', 1, 'panels and slabs — ', '{which are}', 'TC'),
 ('S028', None, 'E', 'clausal', 'S028: vế “based on demonstrated competencies” (trong câu)', 'low', None, '[TC] biên: vế bổ trợ phi hữu hạn “{which is} based on…”; EN 27 (khối bị VI lược)', 1, 'once this period ends, ', '{which is}', 'TC'),
]

TT = [
 # S002
 ('S002', 'luật trộm cắp tiền lương mới', 'L', 'repetition', 'S001: theo luật có hiệu lực', 'med', 'R: the', None, 1),
 # S003
 ('S003', 'Cá nhân', 'L', 'repetition', 'S002: các công ty', 'low', None, 'person-chain contrast (companies vs individuals)', 1),
 # S004
 ('S004', 'trả thiếu tiền lương', 'L', 'repetition', 'S001: trả lương thấp hơn', 'high', None, None, 1),
 ('S004', 'Bộ luật', 'L', 'repetition', 'S002: theo luật', 'med', None, None, 1),
 ('S004', 'mới', 'R', 'demonstrative', 'S002: luật trộm cắp tiền lương mới', 'med', None, 'new code referring back to the laws', 1),
 # S005
 ('S005', 'Cư dân', 'L', 'repetition', 'S003: Cá nhân', 'low', None, 'person chain across sections', 1),
 # S006
 ('S006', 'Người nộp đơn', 'L', 'repetition', 'S005: Cư dân ... sẽ có thể', 'high', None, None, 1),
 # S007
 ('S007', 'Sự thay đổi này', 'L', 'general word', 'S005: fast-track citizenship policy', 'high', 'R: này', None, 1),
 ('S007', 'đơn đăng ký', 'L', 'repetition', 'S006: nộp đơn', 'high', None, 'morphological reiteration', 1),
 ('S007', 'ADF', 'L', 'repetition', 'S005: (ADF)', 'high', None, 'abbreviation', 1),
 # S008
 ('S008', 'người nộp đơn', 'L', 'repetition', 'S006: Người nộp đơn', 'high', None, None, 1),
 ('S008', 'quốc tịch', 'L', 'repetition', 'S005: nhập quốc tịch Úc', 'high', None, None, 1),
 # S009
 ('S009', 'ADF', 'L', 'repetition', 'S007: ADF', 'high', None, None, 1),
 # S010
 ('S010', 'người Úc', 'L', 'repetition', 'S005: quốc tịch Úc', 'med', None, 'Úc morphological chain', 1),
 ('S010', 'ngày 1 tháng 1', 'L', 'repetition', 'S007: ngày 1 tháng 1', 'med', None, 'section date echo', 1),
 # S011
 ('S011', 'Trợ cấp thanh thiếu niên', 'L', 'repetition', 'S010: Youth Allowance', 'high', None, 'translated back-formation of the allowance names', 1),
 ('S011', 'thanh toán', 'L', 'repetition', 'S010: khoản tăng thanh toán', 'high', None, None, 1),
 # S012
 ('S012', 'Người Úc', 'L', 'repetition', 'S010: người Úc', 'med', None, None, 1),
 ('S012', 'ABSTUDY', 'L', 'repetition', 'S010: ABSTUDY', 'high', None, None, 1),
 ('S012', 'mỗi hai tuần', 'L', 'repetition', 'S011: mỗi hai tuần', 'med', None, None, 1),
 # S013
 ('S013', 'Những người hưởng', 'L', 'repetition', 'S012: Người Úc nhận ABSTUDY', 'high', None, None, 1),
 ('S013', 'mỗi hai tuần', 'L', 'repetition', 'S012: mỗi hai tuần', 'med', None, None, 1),
 # S014
 ('S014', 'cũng', 'C', 'additive', 'S011-S013: payment rises', 'med', None, None, 1),
 ('S014', 'thanh toán', 'L', 'repetition', 'S011: thanh toán', 'high', None, None, 1),
 # S015
 ('S015', 'thêm', 'R', 'comparative', 'S010-S014: payment change details', 'low', None, 'thêm thông tin; quantity reference', 1),
 # S016
 ('S016', 'hộ chiếu Úc', 'L', 'repetition', 'S010: người Úc', 'med', None, 'Úc morphological chain', 1),
 # S017
 ('S017', 'ngày 1 tháng 1', 'L', 'repetition', 'S010: ngày 1 tháng 1', 'med', None, None, 1),
 ('S017', 'hộ chiếu Úc', 'L', 'repetition', 'S016: hộ chiếu Úc', 'high', None, None, 1),
 ('S017', '2024', 'L', 'repetition', 'S016: năm 2025', 'low', None, 'year pair', 1),
 # S018
 ('S018', 'Điều này', 'R', 'demonstrative', 'S017: 412 đô la hộ chiếu', 'high', None, None, 1),
 ('S018', 'nước Úc', 'L', 'repetition', 'S016: hộ chiếu Úc', 'med', None, None, 1),
 # S019
 ('S019', 'ngày 1 tháng 1', 'L', 'repetition', 'S017: ngày 1 tháng 1', 'med', None, None, 1),
 ('S019', 'người Úc', 'L', 'repetition', 'S016: hộ chiếu Úc', 'med', None, 'Úc chain', 1),
 # S020
 ('S020', 'phụ phí', 'L', 'repetition', 'S019: phụ phí thẻ ghi nợ', 'high', None, None, 1),
 # S021
 # S022
 ('S022', 'cũng', 'C', 'additive', 'S021: ATM placement ban', 'med', None, None, 1),
 ('S022', 'chơi game', 'L', 'repetition', 'S021: khu vực chơi game', 'high', None, 'phòng chơi game', 1),
 # S023
 ('S023', 'Ngoài ra', 'C', 'additive', 'S021-S022: ATM placement bans', 'high', None, None, 1),
 ('S023', 'chơi game', 'L', 'repetition', 'S022: phòng chơi game', 'high', None, 'khu vực chơi game', 1),
 ('S023', 'ATM', 'L', 'repetition', 'S021: các máy ATM', 'high', None, None, 1),
 # S024
 ('S024', 'Centrelink', 'L', 'repetition', 'S010: Centrelink', 'high', None, 'cross-section echo', 1),
 # S025
 ('S025', 'Thay đổi này', 'L', 'general word', 'S024: Centrelink medical exemption extension', 'high', 'R: này', None, 1),
 ('S025', 'những người', 'L', 'repetition', 'S013: Những người hưởng', 'med', None, 'person chain across sections', 1),
 # S026
 ('S026', 'người nộp đơn', 'L', 'repetition', 'S006: Người nộp đơn', 'med', None, 'cross-section echo (visa section)', 1),
 # S027
 ('S027', 'Thay đổi này', 'L', 'general word', 'S026: quy định mới về thị thực', 'high', 'R: này', None, 1),
 ('S027', 'học', 'L', 'repetition', 'S026: thị thực du học', 'high', None, 'morphological reiteration', 1),
 # S028
 ('S028', 'đơn', 'L', 'repetition', 'S026: nộp đơn', 'high', None, None, 1),
 ('S028', 'CoE', 'L', 'repetition', 'S026: (CoE)', 'high', None, 'abbreviation', 1),
 # S029
 ('S029', 'ngày 1 tháng 1', 'L', 'repetition', 'S019: ngày 1 tháng 1', 'med', None, None, 1),
 # S030
 # S031
 # S032
 ('S032', 'Đồng thanh toán', 'L', 'repetition', 'S031: Đồng thanh toán PBS', 'high', None, None, 1),
 # S033
 ('S033', 'tiền lương', 'L', 'repetition', 'S001: trả lương thấp hơn', 'med', None, 'cross-section echo', 1),
 ('S033', 'ngày 1 tháng 1', 'L', 'repetition', 'S029: ngày 1 tháng 1', 'med', None, None, 1),
 # S034
 ('S034', 'Mức lương tối thiểu', 'L', 'repetition', 'S033: Thay đổi tiền lương', 'high', None, None, 1),
 ('S034', 'người cao niên', 'L', 'repetition', 'S033: chăm sóc người cao tuổi', 'high', None, 'synonym variation within chain', 1),
 # S035
 ('S035', 'người cao tuổi', 'L', 'repetition', 'S034: người cao niên', 'high', None, 'synonym variation within chain', 1),
 ('S035', 'mức lương tối thiểu', 'L', 'repetition', 'S034: Mức lương tối thiểu', 'high', None, None, 1),
 # S036
 ('S036', 'ngày 1 tháng 1', 'L', 'repetition', 'S033: ngày 1 tháng 1', 'med', None, None, 1),
 # S037
 ('S037', 'Khoản thuế này', 'L', 'repetition', 'S036: một khoản thuế', 'high', 'R: này', None, 1),
 # S038
 ('S038', 'Những người', 'R', 'demonstrative', 'S036: chủ sở hữu bất động sản', 'med', None, None, 1),
 ('S038', 'thuế', 'L', 'repetition', 'S037: Khoản thuế này', 'high', None, None, 1),
 # S039
 ('S039', 'Victoria', 'L', 'repetition', 'S036: Victoria', 'high', None, None, 1),
 ('S039', 'Thuế', 'L', 'repetition', 'S038: thuế', 'high', None, 'Thuế đất ... verbatim head', 1),
 # S040
 ('S040', 'Thuế này', 'L', 'repetition', 'S039: Thuế đất', 'high', 'R: này', None, 1),
 ('S040', 'bất động sản', 'L', 'repetition', 'S036: chủ sở hữu bất động sản', 'high', None, None, 1),
 # S041
 ('S041', 'nhà nghỉ', 'L', 'repetition', 'S039: đất ở bỏ trống', 'med', None, 'associated term (phép liên tưởng)', 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_05 (§2–§3) ----
 # [TC] = trong câu. Chỉ E: VI không có S (5 vị trí “those” đều được hiện thực
 # hóa bằng “những người + VP”, §3 S-VI) nên không thêm dòng S nào.
 ('S002', None, 'E', 'verbal', 'S002: vế “hoặc … 7,82 triệu đô la” (trong câu)', 'high', None, '[TC] lược vị ngữ vế hoặc “hoặc {bị phạt tới} 7,82 triệu đô la”; VI 2; song song E-EN1', 1, 'hoặc ', '{bị phạt tới}', 'TC'),
 ('S025', None, 'E', 'nominal', 'S025: vế “và không thể làm việc” (trong câu)', 'high', None, '[TC] lược chủ ngữ vế tọa hợp “và {bạn} không thể làm việc”; VI 22; song song E-EN2', 1, 'bị thương và ', '{bạn}', 'TC'),
 ('S041', None, 'E', 'nominal', 'S041: vế “nếu được sử dụng” (trong câu)', 'high', None, '[TC] lược chủ ngữ + dấu bị động “nếu {chúng} được sử dụng”; VI 35; song song E-EN4', 1, 'miễn nếu ', '{chúng}', 'TC'),
 ('S017', None, 'E', 'clausal', 'S017: vế “tăng 14 đô la so với năm 2024” (trong câu)', 'low', None, '[TC] biên: vế bổ trợ rút gọn “{và} tăng 14 đô la so với năm 2024”; VI 16; song song E-EN5', 1, '412 đô la, ', '{và}', 'TC'),
 ('S007', None, 'E', 'verbal', 'S007: cụm “nơi … đang tìm cách” (trong câu)', 'high', None, '[TC] VI tự sinh: “nơi ∅ đang tìm cách” ← EN “which is looking”; lược hệ từ {là}; VI 7', 1, 'ADF, nơi ', '{là}', 'TC'),
 ('S006', None, 'E', 'nominal', 'S006: vế “trước khi nộp đơn” (trong câu)', 'low', None, '[TC] biên: chủ ngữ vế “trước khi” được điều khiển, lược {họ}; VI 6', 1, 'trước khi ', '{họ}', 'TC'),
 ('S026', None, 'E', 'nominal', 'S026: cụm “tại thời điểm nộp đơn” (trong câu)', 'low', None, '[TC] biên: bất đối xứng hình thái EN “at the time of application” ↔ VI “tại thời điểm ∅ nộp đơn”; VI 23', 1, 'tại thời điểm ', '{người nộp đơn}', 'TC'),
]
