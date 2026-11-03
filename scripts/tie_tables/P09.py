# P09 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S002
 ('S002', 'A new report', 'L', 'repetition', 'S001: according to a new report', 'high', None, 'verbatim', 1),
 ('S002', 'GP clinics', 'L', 'repetition', 'S001: bulk billing GP clinics', 'high', None, None, 1),
 ('S002', 'bulk billing', 'L', 'repetition', 'S001: bulk billing', 'high', None, None, 1),
 ('S002', 'patients', 'L', 'repetition', 'S001: patients', 'high', None, None, 1),
 ('S002', 'out-of-pocket', 'L', 'repetition', 'S001: out-of-pocket', 'high', None, None, 1),
 ('S002', 'general practitioner', 'L', 'repetition', 'S001: GP', 'high', None, 'expansion of abbreviation', 1),
 # S003
 ('S003', 'However', 'C', 'adversative', 'S001-S002: report findings', 'high', None, None, 1),
 ('S003', 'the government', 'L', 'repetition', 'S001-S002: report context', 'low', None, 'first government mention; weak frame', 1),
 ('S003', "the report's findings", 'L', 'repetition', 'S002: A new report has found', 'high', None, None, 1),
 ('S003', 'bulk billing', 'L', 'repetition', 'S002: bulk billing', 'high', None, None, 1),
 ('S003', 'concession card holders and under-16s', 'L', 'repetition', 'S002: non-concession card holders', 'med', None, 'contrastive echo (negated counterpart)', 1),
 # S004
 ('S004', 'The national Blue Report', 'L', 'repetition', 'S002: A new report', 'high', None, None, 1),
 ('S004', 'GP clinics', 'L', 'repetition', 'S002: GP clinics', 'high', None, None, 1),
 ('S004', 'the country', 'L', 'repetition', 'S002: in Australia', 'med', None, None, 1),
 # S005
 ('S005', 'bulk billing clinics', 'L', 'repetition', 'S004: clinics that bulk bill', 'high', None, None, 1),
 ('S005', 'nationally', 'L', 'repetition', 'S004: across the country', 'med', None, None, 1),
 # S006
 ('S006', 'The report', 'L', 'repetition', 'S004: The national Blue Report', 'high', None, None, 1),
 ('S006', 'the bulk billing rate', 'L', 'repetition', 'S005: proportion of such bulk billing clinics', 'high', None, None, 1),
 ('S006', 'clinics', 'L', 'repetition', 'S005: bulk billing clinics', 'high', None, None, 1),
 ('S006', 'bulk bill', 'L', 'repetition', 'S005: bulk billing', 'high', None, None, 2),
 ('S006', 'a new adult patient without concessions', 'L', 'repetition', 'S002: non-concession card holders', 'med', None, 'contrastive echo', 1),
 # S007
 ('S007', 'Cleanbill', 'L', 'repetition', 'S004: healthcare directory Cleanbill', 'high', None, None, 1),
 ('S007', 'this data', 'L', 'repetition', 'S006: the bulk billing rate definition', 'high', 'R: this', None, 1),
 ('S007', 'clinics', 'L', 'repetition', 'S006: clinics', 'high', None, None, 1),
 ('S007', 'bulk billing', 'L', 'repetition', 'S006: bulk bill', 'high', None, None, 1),
 ('S007', 'such patients', 'R', 'demonstrative', 'S006: a new adult patient without concessions', 'high', None, None, 1),
 # S008
 ('S008', 'It', 'R', 'personal', 'S007: Cleanbill', 'high', None, None, 1),
 ('S008', 'its data', 'R', 'personal', 'S007: this data', 'high', None, None, 1),
 ('S008', 'GP clinic', 'L', 'repetition', 'S007: clinics', 'high', None, None, 1),
 ('S008', 'without concessions', 'L', 'repetition', 'S006: without concessions', 'high', None, None, 1),
 # S009
 ('S009', 'the states and territories', 'L', 'repetition', 'S004: across the country', 'med', None, None, 1),
 ('S009', 'GP clinics', 'L', 'repetition', 'S008: GP clinic', 'high', None, None, 1),
 ('S009', 'bulk billing', 'L', 'repetition', 'S007: bulk billing', 'high', None, None, 1),
 # S010
 ('S010', 'The Cleanbill report', 'L', 'repetition', 'S004: The national Blue Report ... Cleanbill', 'high', None, None, 1),
 ('S010', 'the findings', 'L', 'repetition', 'S003: the report\u2019s findings', 'high', None, None, 1),
 ('S010', 'healthcare accessibility in Australia', 'L', 'repetition', 'S002: healthcare accessibility in Australia', 'high', None, 'verbatim', 1),
 # S011
 ('S011', 'the government', 'L', 'repetition', 'S003: the government', 'high', None, None, 1),
 ('S011', 'bulk billing data', 'L', 'repetition', 'S007-S008: this data / its data', 'high', None, None, 1),
 ('S011', 'concession card holders and under-16s', 'L', 'repetition', 'S003: concession card holders and under-16s', 'high', None, 'verbatim', 1),
 ('S011', "Cleanbill's", 'L', 'repetition', 'S010: The Cleanbill report', 'high', None, None, 1),
 # S012
 ('S012', "The government's data", 'L', 'repetition', 'S011: bulk billing data', 'high', None, None, 1),
 ('S012', 'GP visits', 'L', 'repetition', 'S011: visits from concession card holders', 'med', None, None, 1),
 ('S012', 'bulk billed', 'L', 'repetition', 'S011: bulk billing data', 'high', None, None, 1),
 # S013
 ('S013', 'The government', 'L', 'repetition', 'S012: The government\u2019s data', 'high', None, None, 1),
 ('S013', 'the increase', 'L', 'repetition', 'S012: increased from 75.6 per cent to 77.3', 'high', 'R: the', None, 1),
 ('S013', 'Medicare bulk billing incentive payments', 'L', 'repetition', 'S002-S003: bulk billing', 'high', None, None, 1),
 # S014
 ('S014', 'Medicare incentive payments', 'L', 'repetition', 'S013: Medicare bulk billing incentive payments', 'high', None, None, 1),
 ('S014', 'patient rebates', 'L', 'repetition', 'S001: out-of-pocket', 'med', None, 'payment-side association', 1),
 ('S014', 'bulk billed', 'L', 'repetition', 'S012: bulk billed', 'high', None, None, 1),
 ('S014', 'under-16s and Commonwealth concession card holders', 'L', 'repetition', 'S011: concession card holders and under-16s', 'high', None, 'reordered echo', 1),
 # S015
 ('S015', 'the Cleanbill report', 'L', 'repetition', 'S010: The Cleanbill report', 'high', None, None, 1),
 ('S015', 'the bulk billing incentive', 'L', 'repetition', 'S013-S014: incentive payments', 'high', None, None, 1),
 ('S015', 'bulk billing', 'L', 'repetition', 'S014: bulk billed', 'high', None, None, 2),
 ('S015', 'every state and territory', 'L', 'repetition', 'S009: the states and territories', 'high', None, None, 1),
 # S016
 ('S016', 'Every state and territory', 'L', 'repetition', 'S015: every state and territory', 'high', None, 'verbatim', 1),
 ('S016', 'bulk billing', 'L', 'repetition', 'S015: bulk billing', 'high', None, None, 1),
 ('S016', 'the largest rise', 'L', 'repetition', 'S012: increased', 'med', None, None, 1),
 # S017
 ('S017', 'The Cleanbill report', 'L', 'repetition', 'S015: the Cleanbill report', 'high', None, None, 1),
 ('S017', 'also', 'C', 'additive', 'S005: bulk billing decline', 'med', None, None, 1),
 ('S017', 'patients', 'L', 'repetition', 'S008: adult ... patients', 'high', None, None, 1),
 ('S017', 'bulk billed', 'L', 'repetition', 'S016: bulk billing', 'high', None, None, 1),
 ('S017', 'out-of-pocket', 'L', 'repetition', 'S002: out-of-pocket', 'high', None, None, 1),
 # S018
 ('S018', 'The national average cost', 'L', 'repetition', 'S017: paying more out-of-pocket', 'med', None, None, 1),
 ('S018', 'visiting a doctor', 'L', 'repetition', 'S001: to see doctors', 'high', None, None, 1),
 # S019
 ('S019', 'The rising cost of GP visits', 'L', 'repetition', 'S018: The national average cost of visiting a doctor', 'high', None, None, 1),
 ('S019', 'more Australians', 'L', 'repetition', 'S002: in Australia', 'med', None, None, 1),
 ('S019', 'appointments', 'L', 'repetition', 'S002: general practitioner appointments', 'high', None, None, 1),
 # S020
 ('S020', 'Analysis', 'L', 'repetition', 'S004: looked at nearly 7,000 GP clinics', 'med', None, None, 1),
 ('S020', 'the GP', 'L', 'repetition', 'S019: GP visits', 'high', None, None, 1),
 # S021
 ('S021', 'a GP', 'L', 'repetition', 'S020: the GP', 'high', None, None, 1),
 ('S021', 'the cost', 'L', 'repetition', 'S020: due to cost', 'high', None, None, 1),
 # S022
 ('S022', 'SBS News', 'L', 'repetition', 'S015: told SBS News', 'high', None, None, 1),
 ('S022', "patients' avoidance of GPs", 'L', 'repetition', 'S020-S021: not visiting / put off seeing the GP', 'high', None, None, 1),
 ('S022', 'cost', 'L', 'repetition', 'S021: the cost', 'high', None, None, 1),
 ('S022', 'the healthcare system', 'L', 'repetition', 'S002: healthcare accessibility', 'high', None, None, 1),
 # S023
 ('S023', "anyone's health", 'L', 'repetition', 'S022: hospital emergency rooms', 'med', None, 'health domain echo', 1),
 ('S023', 'patients', 'L', 'repetition', 'S022: patients', 'high', None, None, 1),
 # S024
 ('S024', 'Wright', 'L', 'repetition', 'S022: Dr Michael Wright', 'high', None, None, 1),
 ('S024', 'the incentives', 'L', 'repetition', 'S013-S014: incentive payments', 'high', 'R: the', None, 1),
 ('S024', 'funding', 'L', 'repetition', 'S022: far more costly', 'med', None, None, 1),
 # S025
 ('S025', 'Data', 'L', 'repetition', 'S007-S008: data (Cleanbill)', 'high', None, None, 1),
 ('S025', 'bulk billing', 'L', 'repetition', 'S024: bulk bill context', 'high', None, None, 1),
 ('S025', 'a person lives', 'L', 'repetition', 'S009: the states and territories', 'med', None, 'place chain', 1),
 ('S025', 'bulk billed', 'L', 'repetition', 'S017: bulk billed', 'high', None, None, 1),
 ('S025', 'GP visits', 'L', 'repetition', 'S019: GP visits', 'high', None, None, 1),
 # S026
 ('S026', 'patients', 'L', 'repetition', 'S023: patients', 'high', None, None, 1),
 ('S026', "weren't bulk billed", 'L', 'repetition', 'S025: when they are not bulk billed', 'high', None, None, 1),
 ('S026', 'out-of-pocket costs', 'L', 'repetition', 'S017: out-of-pocket', 'high', None, None, 1),
 # S027
 ('S027', 'told SBS News', 'L', 'repetition', 'S022: told SBS News', 'high', None, None, 1),
 ('S027', 'bulk billing', 'L', 'repetition', 'S026: bulk billed', 'high', None, None, 1),
 # S028
 ('S028', 'Breadon', 'L', 'repetition', 'S027: Peter Breadon', 'high', None, None, 1),
 ('S028', 'the decrease in bulk billing', 'L', 'repetition', 'S027: low rates of bulk billing', 'high', None, None, 1),
 ('S028', 'increase in prices', 'L', 'repetition', 'S018: increased by 4.1 per cent', 'high', None, None, 1),
 # S029
 ('S029', 'This cost of living crisis', 'L', 'repetition', 'S028: increase in the expense', 'med', None, None, 1),
 ('S029', 'GPs', 'L', 'repetition', 'S025: GP visits', 'high', None, None, 1),
 ('S029', 'he', 'R', 'personal', 'S028: Breadon', 'high', None, None, 1),
 # S030
 ('S030', 'RACGP', 'L', 'repetition', 'S022: (RACGP)', 'high', None, 'abbreviation', 1),
 ('S030', 'the federal government', 'L', 'repetition', 'S003: the government', 'high', None, None, 1),
 ('S030', 'the patient rebate', 'L', 'repetition', 'S014: general patient rebates', 'high', None, None, 1),
 # S031
 ('S031', 'patient rebates', 'L', 'repetition', 'S030: the patient rebate', 'high', None, None, 1),
 # S032
 ('S032', 'rising costs', 'L', 'repetition', 'S029: cost of living crisis', 'high', None, None, 1),
 ('S032', 'the RACGP', 'L', 'repetition', 'S030: RACGP', 'high', None, None, 1),
 ('S032', 'Medicare rebates', 'L', 'repetition', 'S013: Medicare + S030: rebate', 'high', None, None, 1),
 ('S032', 'GP consultations', 'L', 'repetition', 'S025: GP visits', 'high', None, None, 1),
 ('S032', 'GP mental health items', 'L', 'repetition', 'S022: healthcare system', 'med', None, 'health domain echo', 1),
 # S033
 ('S033', 'Wright', 'L', 'repetition', 'S024: Wright', 'high', None, None, 1),
 ('S033', 'Medicare rebates', 'L', 'repetition', 'S032: Medicare rebates', 'high', None, 'verbatim', 1),
 ('S033', 'patients', 'L', 'repetition', 'S026: patients', 'high', None, None, 1),
 ('S033', 'consultations', 'L', 'repetition', 'S032: GP consultations', 'high', None, None, 1),
 ('S033', 'bulk bill', 'L', 'repetition', 'S027: bulk billing', 'high', None, None, 1),
 ('S033', 'out-of-pocket costs', 'L', 'repetition', 'S026: out-of-pocket costs', 'high', None, 'verbatim', 1),
 # S034
 ('S034', 'Breadon', 'L', 'repetition', 'S029: he (Breadon)', 'high', None, None, 1),
 ('S034', 'the cost of visiting a doctor', 'L', 'repetition', 'S018: cost of visiting a doctor', 'high', None, 'verbatim', 1),
 # S035
 ('S035', 'Breadon', 'L', 'repetition', 'S034: Breadon', 'high', None, None, 1),
 ('S035', 'GP clinics', 'L', 'repetition', 'S009: GP clinics', 'high', None, None, 1),
 ('S035', 'bulk billing', 'L', 'repetition', 'S033: bulk bill', 'high', None, None, 1),
 ('S035', 'patients', 'L', 'repetition', 'S033: patients', 'high', None, None, 1),
 # S036
 ('S036', 'the NSW government', 'L', 'repetition', 'S030: the federal government', 'high', None, None, 1),
 ('S036', 'a new incentive', 'L', 'repetition', 'S024: the incentives', 'high', None, None, 1),
 ('S036', 'rebate', 'L', 'repetition', 'S031: patient rebates', 'high', None, None, 1),
 ('S036', 'GPs', 'L', 'repetition', 'S029: GPs', 'high', None, None, 1),
 ('S036', 'bulk billing threshold', 'L', 'repetition', 'S035: bulk billing', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_09 (§2–§3) ----
 ('S009', None, 'E', 'verbal', 'S009: NSW GP clinics had the highest rate of bulk billing (within sentence)', 'high', None, '[TC] E-EN1 gapping: “… and Tasmania ∅ the lowest (0 per cent)” — lược vị ngữ {had} + {rate of bulk billing} sau “Tasmania”; gap 2 sau “the lowest” lược {rate of bulk billing}', 1, 'and Tasmania ', '{had}', 'TC'),
 ('S021', None, 'E', 'verbal', 'S021: did not see a GP when they needed to (within sentence)', 'high', None, '[TC] E-EN2 lược động từ sau “to”: “when they needed to ∅ {see a GP}”; EN to-ellipsis', 1, 'when they needed to', '{see a GP}', 'TC'),
 ('S011', None, 'E', 'nominal', "S011: paints a different picture than Cleanbill's (within sentence)", 'high', None, "[TC] E-EN3 lược sở hữu cách: “than Cleanbill's ∅” — lược {picture/data} sau “Cleanbill's”", 1, "than Cleanbill's", '{picture}', 'TC'),
 ('S036', None, 'E', 'nominal', 'S036: 80 per cent of services in Sydney and 70 per cent in the rest of NSW (within sentence)', 'high', None, '[TC] E-EN4 gapping: “… and 70 per cent ∅ in the rest of NSW” — lược {of services} sau “70 per cent”', 1, 'and 70 per cent', '{of services}', 'TC'),
 ('S016', None, 'E', 'clausal', 'S015: Health Minister Mark Butler told SBS News (khung dẫn ở khối 17)', 'low', None, '[LC] biên: E-EN5 trích dẫn Butler kéo dài — S016 là đoạn 2 của cùng trích dẫn, lược khung dẫn lặp {Butler told SBS News}; khung chỉ có ở S015; vị trí: đầu câu, ngay trước dấu ngoặc kép mở', 1, '', '{Butler told SBS News}', 'LC'),
 ('S026', 'those', 'S', 'nominal', 'S026: patients living in very remote areas (within sentence)', 'high', None, '[TC] S-EN1 thế danh từ “those” ← {bệnh nhân} (patients…); VI hiện thực hóa “những bệnh nhân” nên không có S tương ứng', 1, None, None, 'TC'),
]

TT = [
 # S002
 ('S002', 'Một báo cáo mới', 'L', 'repetition', 'S001: Theo một báo cáo mới', 'high', None, 'verbatim', 1),
 ('S002', 'bác sĩ gia đình', 'L', 'repetition', 'S001: bác sĩ gia đình', 'high', None, None, 1),
 ('S002', 'bulk-billing', 'L', 'repetition', 'S001: bulk-billing', 'high', None, None, 1),
 # S003
 ('S003', 'bác sĩ gia đình', 'L', 'repetition', 'S002: bác sĩ gia đình', 'high', None, None, 1),
 # S004
 ('S004', 'Tuy nhiên', 'C', 'adversative', 'S001-S003: report findings', 'high', None, None, 1),
 ('S004', 'báo cáo', 'L', 'repetition', 'S002: Một báo cáo mới', 'high', None, None, 1),
 ('S004', 'thanh toán toàn bộ', 'L', 'repetition', 'S002: thanh toán', 'high', None, None, 1),
 # S005
 ('S005', 'Báo cáo', 'L', 'repetition', 'S004: báo cáo', 'high', None, None, 1),
 ('S005', 'phòng khám', 'L', 'repetition', 'S002: phòng khám', 'high', None, None, 1),
 # S006
 ('S006', 'phòng khám', 'L', 'repetition', 'S005: phòng khám', 'high', None, None, 1),
 ('S006', 'thanh toán', 'L', 'repetition', 'S004: thanh toán toàn bộ', 'high', None, None, 1),
 ('S006', 'toàn quốc', 'L', 'repetition', 'S005: trên toàn quốc', 'high', None, None, 1),
 # S007
 ('S007', 'Báo cáo', 'L', 'repetition', 'S005: Báo cáo', 'high', None, None, 1),
 ('S007', 'thanh toán', 'L', 'repetition', 'S006: thanh toán', 'high', None, None, 1),
 ('S007', 'phòng khám', 'L', 'repetition', 'S006: phòng khám', 'high', None, None, 1),
 ('S007', 'bệnh nhân', 'L', 'repetition', 'S002: bệnh nhân', 'high', None, None, 1),
 # S008
 ('S008', 'Cleanbill', 'L', 'repetition', 'S005: Cleanbill', 'high', None, None, 1),
 ('S008', 'dữ liệu này', 'L', 'repetition', 'S007: (dữ liệu implied in definition)', 'high', 'R: này', 'dữ liệu first overt use with demonstrative', 1),
 ('S008', 'phòng khám', 'L', 'repetition', 'S007: phòng khám', 'high', None, None, 1),
 ('S008', 'thanh toán', 'L', 'repetition', 'S007: thanh toán', 'high', None, None, 1),
 ('S008', 'bệnh nhân', 'L', 'repetition', 'S007: bệnh nhân', 'high', None, None, 1),
 # S009
 ('S009', 'Báo cáo', 'L', 'repetition', 'S007: Báo cáo', 'high', None, None, 1),
 ('S009', 'dữ liệu', 'L', 'repetition', 'S008: dữ liệu này', 'high', None, None, 1),
 ('S009', 'phòng khám', 'L', 'repetition', 'S008: phòng khám', 'high', None, None, 1),
 ('S009', 'bạn', 'R', 'personal', 'ngoài văn bản: người đọc (bối cảnh phát ngôn)', 'high', None, 'địa chỉ hoá người đọc (exophoric); EN counterpart "you" không đánh dấu theo quy ước gộp của phép liên kết', 1),
 # S010
 ('S010', 'NSW GP', 'L', 'repetition', 'S009: phòng khám gia đình', 'med', None, 'GP chain', 1),
 ('S010', 'thanh toán bulk-billing', 'L', 'repetition', 'S008: thanh toán', 'high', None, None, 1),
 # S011
 ('S011', 'báo cáo Cleanbill', 'L', 'repetition', 'S009: Báo cáo (Cleanbill)', 'high', None, None, 1),
 ('S011', 'những phát hiện này', 'L', 'repetition', 'S004: những phát hiện của báo cáo', 'high', 'R: này', None, 1),
 ('S011', 'chăm sóc sức khỏe', 'L', 'repetition', 'S002: chăm sóc sức khỏe', 'high', None, None, 1),
 # S012
 ('S012', 'chính phủ', 'L', 'repetition', 'S004: chính phủ', 'high', None, None, 1),
 ('S012', 'dữ liệu', 'L', 'repetition', 'S009: dữ liệu', 'high', None, None, 1),
 ('S012', 'thanh toán hoàn toàn bulk-billing', 'L', 'repetition', 'S010: thanh toán bulk-billing', 'high', None, None, 1),
 ('S012', 'thẻ ưu đãi', 'L', 'repetition', 'S007: bệnh nhân ... không tính phí thêm', 'med', None, 'concession concept echo', 1),
 # S013
 ('S013', 'Dữ liệu của chính phủ', 'L', 'repetition', 'S012: dữ liệu + chính phủ', 'high', None, None, 1),
 ('S013', 'bác sĩ gia đình', 'L', 'repetition', 'S003: bác sĩ gia đình', 'high', None, None, 1),
 # S014
 ('S014', 'Chính phủ', 'L', 'repetition', 'S013: chính phủ', 'high', None, None, 1),
 ('S014', 'sự gia tăng này', 'L', 'repetition', 'S013: tăng từ 75,6% lên 77,3%', 'high', 'R: này', None, 1),
 ('S014', 'thanh toán khuyến khích của Medicare', 'L', 'repetition', 'S012: thanh toán hoàn toàn', 'high', None, None, 1),
 # S015
 ('S015', 'thanh toán khuyến khích Medicare', 'L', 'repetition', 'S014: thanh toán khuyến khích của Medicare', 'high', None, None, 1),
 ('S015', 'bệnh nhân', 'L', 'repetition', 'S008: bệnh nhân', 'high', None, None, 1),
 # S016
 ('S016', 'báo cáo Cleanbill', 'L', 'repetition', 'S011: báo cáo Cleanbill', 'high', None, None, 1),
 ('S018', 'cũng', 'C', 'additive', 'S006: tỷ lệ giảm', 'med', None, None, 1),
 ('S016', 'bệnh nhân', 'L', 'repetition', 'S015: bệnh nhân', 'high', None, None, 1),
 ('S016', 'thanh toán bulk-billing', 'L', 'repetition', 'S012: thanh toán hoàn toàn bulk-billing', 'high', None, None, 1),
 # S017
 ('S016', 'SBS News', 'L', 'repetition', 'S001: SBS News (implied source)', 'low', None, 'first overt SBS News mention in TT', 1),
 ('S017', 'tiểu bang và lãnh thổ', 'L', 'repetition', 'S016: mọi tiểu bang và lãnh thổ', 'high', None, None, 1),
 ('S017', 'bulk-billing', 'L', 'repetition', 'S016: thanh toán bulk-billing', 'high', None, None, 1),
 ('S017', 'tăng', 'L', 'repetition', 'S016: bắt đầu tăng trở lại', 'high', None, None, 1),
 # S018
 ('S018', 'Báo cáo Cleanbill', 'L', 'repetition', 'S016: báo cáo Cleanbill', 'high', None, None, 1),

 ('S018', 'bệnh nhân', 'L', 'repetition', 'S016: bệnh nhân', 'high', None, None, 1),
 ('S018', 'bulk-bill', 'L', 'repetition', 'S017: bulk-billing', 'high', None, None, 1),
 # S019
 ('S019', 'Chi phí đi khám bác sĩ', 'L', 'repetition', 'S018: trả nhiều tiền hơn', 'med', None, None, 1),
 ('S019', 'toàn quốc', 'L', 'repetition', 'S006: toàn quốc', 'high', None, None, 1),
 # S020
 ('S020', 'Chi phí', 'L', 'repetition', 'S019: Chi phí', 'high', None, None, 1),
 ('S020', 'bác sĩ', 'L', 'repetition', 'S018: bác sĩ gia đình', 'high', None, None, 2),
 ('S020', 'người Úc', 'L', 'repetition', 'S002: Úc', 'med', None, None, 1),
 # S021
 ('S021', 'Phân tích', 'L', 'repetition', 'S005: xem xét gần 7.000 phòng khám', 'med', None, None, 1),
 ('S021', 'bác sĩ gia đình', 'L', 'repetition', 'S020: bác sĩ gia đình', 'high', None, None, 1),
 ('S021', 'chi phí', 'L', 'repetition', 'S020: Chi phí', 'high', None, None, 1),
 # S022
 ('S022', 'bác sĩ gia đình', 'L', 'repetition', 'S021: bác sĩ gia đình', 'high', None, None, 1),
 ('S022', 'chi phí', 'L', 'repetition', 'S021: chi phí', 'high', None, None, 1),
 # S023
 ('S023', 'bác sĩ gia đình', 'L', 'repetition', 'S022: bác sĩ gia đình', 'high', None, None, 1),
 ('S023', 'SBS News', 'L', 'repetition', 'S017: SBS News', 'high', None, None, 1),
 ('S023', 'bệnh nhân', 'L', 'repetition', 'S018: bệnh nhân', 'high', None, None, 1),
 # S024
 ('S024', 'Ông', 'R', 'personal', 'S023: bác sĩ Michael Wright', 'high', None, None, 1),
 ('S024', 'sức khỏe', 'L', 'repetition', 'S011: chăm sóc sức khỏe', 'high', None, None, 1),
 ('S024', 'bệnh nhân', 'L', 'repetition', 'S023: bệnh nhân', 'high', None, None, 1),
 ('S024', 'bác sĩ gia đình', 'L', 'repetition', 'S023: bác sĩ gia đình', 'high', None, None, 1),
 # S025
 ('S025', 'Ông Wright', 'L', 'repetition', 'S024: Ông (Wright)', 'high', None, None, 1),
 ('S025', 'ưu đãi', 'L', 'repetition', 'S016: tăng gấp ba lần ưu đãi', 'high', None, None, 1),
 ('S025', 'nước Úc', 'L', 'repetition', 'S020: người Úc', 'high', None, None, 1),
 # S026
 ('S026', 'thanh toán bulk-billing', 'L', 'repetition', 'S017: bulk-billing', 'high', None, None, 1),
 ('S026', 'người', 'L', 'repetition', 'S020: người Úc', 'med', None, 'person chain', 1),
 # S027
 ('S027', 'bệnh nhân', 'L', 'repetition', 'S024: bệnh nhân', 'high', None, None, 1),
 ('S027', 'thanh toán toàn bộ', 'L', 'repetition', 'S012: thanh toán hoàn toàn', 'high', None, None, 1),
 # S028
 ('S028', 'SBS News', 'L', 'repetition', 'S023: SBS News', 'high', None, None, 1),
 ('S028', 'thanh toán bulk-billing', 'L', 'repetition', 'S026: thanh toán bulk-billing', 'high', None, None, 1),
 ('S028', 'tăng giá', 'L', 'repetition', 'S019: Chi phí ... tăng', 'high', None, None, 1),
 # S029
 ('S029', 'chi phí sinh hoạt', 'L', 'repetition', 'S028: chi phí hoạt động', 'med', None, None, 1),
 ('S029', 'người Úc', 'L', 'repetition', 'S025: nước Úc', 'high', None, None, 1),
 ('S029', 'bác sĩ', 'L', 'repetition', 'S024: bác sĩ gia đình', 'high', None, None, 1),
 # S030
 ('S030', 'RACGP', 'L', 'repetition', 'S023: (RACGP)', 'high', None, 'abbreviation', 1),
 ('S030', 'chính phủ liên bang', 'L', 'repetition', 'S012: chính phủ', 'high', None, None, 1),
 ('S030', 'giảm giá cho bệnh nhân', 'L', 'repetition', 'S015: chiết khấu chung cho bệnh nhân', 'high', None, None, 1),
 ('S030', 'bác sĩ', 'L', 'repetition', 'S029: bác sĩ', 'high', None, None, 1),
 # S031
 ('S031', 'giảm giá cho bệnh nhân', 'L', 'repetition', 'S030: giảm giá cho bệnh nhân', 'high', None, None, 1),
 ('S031', 'bác sĩ gia đình', 'L', 'repetition', 'S030: bác sĩ gia đình', 'high', None, None, 1),
 ('S031', 'cô', 'R', 'personal', 'S030: bác sĩ Rebekah Hoffman', 'high', None, None, 1),
 # S032
 ('S032', 'chi phí gia tăng', 'L', 'repetition', 'S029: chi phí sinh hoạt', 'high', None, None, 1),
 ('S032', 'RACGP', 'L', 'repetition', 'S030: RACGP', 'high', None, None, 1),
 ('S032', 'chiết khấu Medicare', 'L', 'repetition', 'S014: Medicare + S030: giảm giá', 'high', None, None, 1),
 ('S032', 'bác sĩ gia đình', 'L', 'repetition', 'S031: bác sĩ gia đình', 'high', None, None, 1),
 # S033
 ('S033', 'chính phủ NSW', 'L', 'repetition', 'S030: chính phủ liên bang', 'high', None, None, 1),
 ('S033', 'ưu đãi mới', 'L', 'repetition', 'S025: ưu đãi', 'high', None, None, 1),
 ('S033', 'giảm giá', 'L', 'repetition', 'S031: giảm giá cho bệnh nhân', 'high', None, None, 1),
 ('S033', 'bác sĩ gia đình', 'L', 'repetition', 'S032: bác sĩ gia đình', 'high', None, None, 1),
 ('S033', 'thanh toán', 'L', 'repetition', 'S028: thanh toán bulk-billing', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_09 (§2–§3) ----
 ('S010', None, 'E', 'verbal', 'S010: các phòng khám NSW GP có tỷ lệ thanh toán bulk-billing cao nhất (trong câu)', 'high', None, '[TC] E-VI1 song song E-EN1 (gapping): “và Tasmania ∅ thấp nhất (0%)” — lược {có tỷ lệ thanh toán} sau “Tasmania”', 1, 'và Tasmania ', '{có tỷ lệ thanh toán}', 'TC'),
 ('S022', None, 'E', 'verbal', 'S022: không gặp bác sĩ gia đình khi họ cần (trong câu)', 'high', None, '[TC] E-VI2 song song E-EN2: “khi họ cần ∅” — lược {gặp bác sĩ gia đình} sau “cần”', 1, 'khi họ cần', '{gặp bác sĩ gia đình}', 'TC'),
 ('S033', None, 'E', 'nominal', 'S033: 80% dịch vụ ở Sydney và 70% ở phần còn lại của NSW (trong câu)', 'high', None, '[TC] E-VI3 song song E-EN4: “80% dịch vụ ở Sydney và 70% ∅ ở phần còn lại của NSW” — lược {dịch vụ} sau “70%”', 1, 'và 70%', '{dịch vụ}', 'TC'),
 ('S028', None, 'E', 'clausal', 'S028: Peter Breadon nói với SBS News rằng (khung dẫn ở đầu câu)', 'high', None, '[TC] E-VI4 VI tự sinh: lược khung dẫn lặp “Breadon said” của EN S028 (EN lặp chủ ngữ + khung; VI gộp vào khung đầu câu)', 1, 'nói với SBS News rằng ', '{Breadon said}', 'TC'),
 ('S012', None, 'E', 'nominal', 'S012: một bức tranh khác với Cleanbill (trong câu)', 'high', None, '[TC] E-VI5 song song E-EN3: “khác với ∅ Cleanbill” — lược sở hữu {của} trước “Cleanbill” (EN: than Cleanbill’s)', 1, 'khác với ', '{của}', 'TC'),
 ('S017', None, 'E', 'clausal', 'S016: Bộ trưởng Y tế Mark Butler nói với SBS News (khung dẫn ở khối 17)', 'low', None, '[LC] biên: E-VI6 trích dẫn Butler kéo dài — S017 là đoạn 2 của cùng trích dẫn, lược khung dẫn lặp {Bộ trưởng Y tế Mark Butler nói với SBS News rằng}; khung chỉ có ở S016; vị trí: đầu câu, ngay trước dấu ngoặc kép mở', 1, '', '{Bộ trưởng Y tế Mark Butler nói với SBS News rằng}', 'LC'),
]
