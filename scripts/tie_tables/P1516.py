# P15/P16 tie tables.

# ---- P15 ----
P15_ST = [
 # S002
 ('S002', 'his', 'R', 'personal', 'S001: a Palestinian activist (Mahmoud Khalil)', 'high', None, None, 1),
 # S003
 ('S003', 'Greer', 'L', 'repetition', 'S002: attorney Amy Greer (implied)', 'med', None, 'first overt Greer mention', 1),
 ('S003', 'the arrest', 'L', 'repetition', 'S001: arrested a Palestinian activist', 'high', None, None, 1),
 # S004
 ('S004', 'the attorney', 'L', 'repetition', 'S003: Greer (the attorney)', 'high', None, None, 1),
 ('S004', 'Khalil', 'L', 'repetition', 'S002: Mahmoud Khalil', 'high', None, None, 1),
 ('S004', 'the United States', 'L', 'repetition', 'S001: (U.S. implied)', 'low', None, 'first overt US mention; weak', 1),
 # S005
 ('S005', 'Khalil\u2019s arrest', 'L', 'repetition', 'S003: the arrest', 'high', None, None, 1),
 # S006
 ('S006', 'Khalil\u2019s arrest', 'L', 'repetition', 'S005: Khalil\u2019s arrest', 'high', None, 'verbatim', 1),
 ('S006', 'Trump\u2019s', 'L', 'repetition', 'S005: Trump (Homeland Security context)', 'med', None, None, 1),
 # S007
 ('S007', 'The administration', 'L', 'repetition', 'S006: Trump\u2019s promised crackdown', 'high', None, None, 1),
 ('S007', 'participants', 'L', 'repetition', 'S001: played a prominent role (in protests)', 'med', None, None, 1),
 ('S007', 'the country', 'L', 'repetition', 'S004: the United States', 'high', None, None, 1),
 # S008
 ('S008', 'McLaughlin', 'L', 'repetition', 'S005: Tricia McLaughlin', 'high', None, None, 1),
 ('S008', 'the arrest', 'L', 'repetition', 'S006: Khalil\u2019s arrest', 'high', None, None, 1),
 ('S008', 'Khalil\u2019s role', 'R', 'personal', 'S002: Mahmoud Khalil', 'high', None, None, 1),
 ('S008', 'the protests', 'L', 'repetition', 'S001: played a prominent role (in protests)', 'med', None, None, 1),
 # S009
 ('S009', 'ICE agents', 'L', 'repetition', 'S003: ICE agents', 'high', None, None, 1),
 ('S009', 'Khalil\u2019s', 'R', 'personal', 'S008: Khalil', 'high', None, None, 1),
 # S010
 ('S010', 'Khalil\u2019s attorney', 'L', 'repetition', 'S004: the attorney', 'high', None, None, 1),
  ('S010', 'he', 'R', 'personal', 'S009: Khalil', 'high', None, None, 1),
 # S011
 ('S011', 'his wife', 'R', 'personal', 'S010: he (Khalil)', 'high', None, None, 1),
 ('S011', 'he', 'R', 'personal', 'S010: he (Khalil)', 'high', None, None, 1),
 # S012
 ('S012', 'Greer', 'L', 'repetition', 'S010: Khalil\u2019s attorney', 'high', None, None, 1),
 ('S012', 'Khalil\u2019s whereabouts', 'R', 'personal', 'S011: he was not there', 'high', None, None, 1),
 # S013
 ('S013', 'We', 'R', 'personal', 'S012: she (Greer, quoted)', 'med', None, None, 1),
 ('S013', 'he', 'R', 'personal', 'S012: Khalil', 'high', None, None, 1),
 ('S013', 'Greer', 'L', 'repetition', 'S012: Greer', 'high', None, None, 1),
 # S015
 ('S015', 'The administration', 'L', 'repetition', 'S007: The administration', 'high', None, None, 1),
 # S016
 ('S016', 'A Columbia University spokesperson', 'L', 'repetition', 'S005: A spokesperson for the Department of Homeland Security', 'med', None, 'spokesperson chain across institutions', 1),
 ('S016', 'law enforcement agents', 'L', 'repetition', 'S009: ICE agents', 'high', None, None, 1),
 # S017
 ('S017', 'The spokesperson', 'L', 'repetition', 'S016: A Columbia University spokesperson', 'high', None, None, 1),
 ('S017', 'Khalil\u2019s detention', 'R', 'personal', 'S010: he was being held', 'high', None, None, 1),
 # S018
 ('S018', 'the administration', 'L', 'repetition', 'S015: The administration', 'high', None, None, 1),
 # S019
 ('S019', 'The Department of Homeland Security', 'L', 'repetition', 'S005: the Department of Homeland Security', 'high', None, None, 1),
 ('S019', 'green card holders', 'L', 'repetition', 'S004: a green card', 'high', None, None, 1),
 # S020
 ('S020', 'But', 'C', 'adversative', 'S019: can initiate deportation proceedings', 'high', None, None, 1),
 ('S020', 'the detention', 'L', 'repetition', 'S017: Khalil\u2019s detention', 'high', None, None, 1),
 ('S020', 'a legal permanent resident', 'L', 'repetition', 'S004: permanent resident with a green card', 'high', None, None, 1),
 # S021
 ('S021', 'This', 'R', 'demonstrative', 'S020: the detention of a legal permanent resident', 'high', None, None, 1),
 ('S021', 'the Trump', 'L', 'repetition', 'S006: Trump\u2019s', 'high', None, None, 1),
 # S022
 ('S022', 'Khalil', 'L', 'repetition', 'S021: someone (Khalil)', 'high', None, None, 1),
 ('S022', 'Columbia\u2019s', 'L', 'repetition', 'S002: Columbia', 'high', None, None, 1),
 # S023
 ('S023', 'The role', 'L', 'repetition', 'S022: his role as negotiator', 'high', None, None, 1),
 ('S023', 'him', 'R', 'personal', 'S022: Khalil', 'high', None, None, 1),
 ('S023', 'the movement', 'L', 'repetition', 'S001: a prominent role (in the movement)', 'med', None, None, 1),
 # S024
 ('S024', 'Khalil', 'L', 'repetition', 'S023: him', 'high', None, None, 1),
 ('S024', 'a new Columbia University office', 'L', 'repetition', 'S016: A Columbia University spokesperson', 'high', None, None, 1),
 # S025
 ('S025', 'The investigations', 'L', 'repetition', 'S024: under investigation', 'high', None, None, 1),
 ('S025', 'the Trump administration', 'L', 'repetition', 'S018: the administration', 'high', None, None, 1),
 # S026
 ('S026', 'The university\u2019s', 'R', 'personal', 'S024: a new Columbia University office', 'high', None, None, 1),
 ('S026', 'Khalil', 'L', 'repetition', 'S024: Khalil', 'high', None, None, 1),
 ('S026', 'the Columbia University', 'L', 'repetition', 'S024: a new Columbia University office', 'high', None, None, 1),
 # S027
 ('S027', 'He', 'R', 'personal', 'S026: Khalil', 'high', None, None, 1),
 # S029
 # S030
 ('S030', 'They', 'R', 'personal', 'S024: a new Columbia University office (investigators)', 'med', None, None, 1),
 # S031
 ('S031', 'It\u2019s', 'R', 'personal', 'S024: a new Columbia University office', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_15 (§2–§3) ----
 ('S002', None, 'E', 'nominal', 'S002: {who was} (trong câu)', 'med', None, '[TC] đồng vị rút gọn “Mahmoud Khalil, ∅ a graduate student…”; EN 15 nửa sau bị cắt', 1, 'Mahmoud Khalil, ', '{who was}', 'TC'),
 ('S004', None, 'E', 'clausal', 'S004: {Having been} (trong câu)', 'med', None, '[TC] rút gọn bị động “∅ Informed by the attorney…”', 1, '', '{Having been}', 'TC'),
 ('S016', 'one', 'S', 'nominal', 'S015: a warrant', 'high', None, '[TC] one ← a warrant; “if the school had received one”', 1, None, None, 'TC'),
 ('S024', 'those', 'S', 'nominal', 'S023: students / activists', 'high', None, '[TC] those ← students; “among those under investigation”', 1, None, None, 'TC'),
 ('S028', None, 'E', 'clausal', 'S027: He faced sanctions for', 'high', None, '[TC] tọa hợp lược khung: “∅ and playing a substantial role…”', 1, 'attack ', '{He faced sanctions for}', 'TC'),

]
P15_TT = [
 # S002
 ('S002', 'Luật sư', 'L', 'repetition', 'S001: (attorney implied in arrest report)', 'low', None, 'first overt mention; weak', 1),
 ('S002', 'Mahmoud Khalil', 'L', 'repetition', 'S001: một sinh viên sau đại học người Palestine', 'high', None, 'name specification', 1),
 # S003
 ('S003', 'Luật sư Greer', 'L', 'repetition', 'S002: Luật sư Amy Greer', 'high', None, None, 1),
 ('S003', 'ICE', 'L', 'repetition', 'S002: ICE', 'high', None, None, 1),
 ('S003', 'vụ bắt giữ', 'L', 'repetition', 'S001: bắt giữ', 'high', None, None, 1),
 # S004
 ('S004', 'bà Greer', 'R', 'personal', 'S003: bà', 'high', None, None, 1),
 ('S004', 'luật sư', 'L', 'repetition', 'S003: Luật sư Greer', 'high', None, None, 1),
 ('S004', 'Khalil', 'L', 'repetition', 'S002: Mahmoud Khalil', 'high', None, None, 1),
 ('S004', 'Hoa Kỳ', 'L', 'repetition', 'S001: liên bang Mỹ', 'high', None, None, 1),
 # S005
 ('S005', 'Vụ bắt giữ này', 'L', 'repetition', 'S003: vụ bắt giữ', 'high', 'R: này', None, 1),
 ('S005', 'Trump', 'L', 'repetition', 'S004: (none)', 'low', None, 'first overt Trump mention in TT', 1),
 # S006
 ('S006', 'Chính quyền của ông Trump', 'L', 'repetition', 'S005: Trump', 'high', None, None, 1),
 ('S006', 'những người tham gia', 'L', 'repetition', 'S001: đóng vai trò nổi bật (in protests)', 'med', None, None, 1),
 ('S006', 'đất nước này', 'R', 'demonstrative', 'S004: Hoa Kỳ', 'high', None, None, 1),
 # S007
 ('S007', 'Khalil', 'L', 'repetition', 'S004: Khalil', 'high', None, None, 1),
 ('S007', 'sinh viên', 'L', 'repetition', 'S001: sinh viên sau đại học', 'high', None, None, 1),
 ('S007', 'các giới chức trường đại học', 'L', 'repetition', 'S002: trường gần khuôn viên Đại học Columbia', 'high', None, None, 1),
 # S008
 ('S008', 'Luật sư Greer', 'L', 'repetition', 'S004: bà Greer', 'high', None, None, 1),
 ('S008', 'chính quyền', 'L', 'repetition', 'S006: Chính quyền của ông Trump', 'high', None, None, 1),
 # S009
 ('S009', 'Khalil', 'L', 'repetition', 'S008: Khalil', 'high', None, None, 1),
 ('S009', 'Kể từ đó', 'C', 'temporal', 'S008: the transfer event', 'high', None, None, 1),
 ('S009', 'giam giữ người nhập cư', 'L', 'repetition', 'S001: di trú', 'med', None, None, 1),
 # S010
 ('S010', 'Chúng tôi', 'R', 'personal', 'S008: Luật sư Greer (quoted)', 'med', None, None, 1),
 ('S010', 'anh ấy', 'R', 'personal', 'S009: Khalil', 'high', None, None, 1),
 ('S010', 'luật sư Greer', 'L', 'repetition', 'S008: Luật sư Greer', 'high', None, None, 1),
 # S011
 ('S011', 'sự leo thang', 'L', 'repetition', 'S010: (escalation implied in detention details)', 'low', None, 'weak', 1),
 # S012
 ('S012', 'Chính quyền', 'L', 'repetition', 'S008: chính quyền', 'high', None, None, 1),
 # S013
 ('S013', 'Một người phát ngôn của Đại học Columbia', 'L', 'repetition', 'S002: Đại học Columbia', 'high', None, None, 1),
 ('S013', 'các nhân viên thực thi pháp luật', 'L', 'repetition', 'S003: nhân viên của ICE', 'high', None, None, 1),
 # S014
 ('S014', 'Người phát ngôn này', 'L', 'repetition', 'S013: Một người phát ngôn', 'high', 'R: này', None, 1),
 ('S014', 'Khalil', 'L', 'repetition', 'S010: anh ấy (Khalil)', 'high', None, None, 1),
 # S015
 ('S015', 'bình luận', 'L', 'repetition', 'S014: bình luận', 'high', None, None, 1),
 ('S015', 'Bộ An ninh Nội địa', 'L', 'repetition', 'S001: (Homeland Security implied)', 'low', None, 'first overt mention; weak', 1),
 # S016
 ('S016', 'Bộ An ninh Nội địa Mỹ', 'L', 'repetition', 'S015: Bộ An ninh Nội địa', 'high', None, None, 1),
 ('S016', 'thẻ xanh', 'L', 'repetition', 'S004: thẻ xanh', 'high', None, None, 1),
 # S017
 ('S017', 'liên minh', 'L', 'repetition', 'S016: (coalition implied)', 'low', None, 'weak', 1),
 # S018
 ('S018', 'hành động trả đũa', 'L', 'repetition', 'S012: các mối đe dọa', 'low', None, 'weak', 1),
 ('S018', 'chính quyền Trump', 'L', 'repetition', 'S012: Chính quyền', 'high', None, None, 1),
 # S019
 ('S019', 'Khalil', 'L', 'repetition', 'S014: Khalil', 'high', None, None, 1),
 ('S019', 'Đại học Columbia', 'L', 'repetition', 'S013: Đại học Columbia', 'high', None, None, 1),
 # S020
 ('S020', 'cáo buộc', 'L', 'repetition', 'S019: điều tra', 'med', None, None, 1),
 # S021
 ('S021', 'Những cuộc điều tra đó', 'R', 'demonstrative', 'S020: cáo buộc kỷ luật', 'high', None, None, 1),
 ('S021', 'chính quyền Trump', 'L', 'repetition', 'S018: chính quyền Trump', 'high', None, None, 1),
 ('S021', 'Đại học Columbia', 'L', 'repetition', 'S019: Đại học Columbia', 'high', None, None, 1),
 # S022
 # S023
 ('S023', 'Khalil', 'L', 'repetition', 'S019: Khalil', 'high', None, None, 1),
 # S024
 # S025
 ('S025', 'Họ', 'R', 'personal', 'S019: văn phòng mới (investigators)', 'med', None, None, 1),
 # S026
 ('S026', 'công việc', 'L', 'repetition', 'S019: văn phòng (office work)', 'low', None, 'weak', 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_15 (§2) ----
 ('S001', None, 'E', 'nominal', 'S001: {người} (trong câu)', 'med', None, '[TC] lược quan hệ từ: “sinh viên…, ∅ vốn đóng vai trò…”', 1, 'sinh viên sau đại học người Palestine, ', '{người}', 'TC'),
 ('S004', None, 'E', 'clausal', 'S004: {bà ấy được} (trong câu)', 'med', None, '[TC] rút gọn bị động “khi ∅ được luật sư thông báo…”', 1, 'Theo bà Greer, ', '{bà ấy được}', 'TC'),
 ('S007', None, 'E', 'nominal', 'S007: {người} (trong câu)', 'med', None, '[TC] control: “nhà hoạt động sinh viên ∅ sẵn sàng chia sẻ…”', 1, 'nhà hoạt động sinh viên ', '{người}', 'TC'),
 ('S023', None, 'E', 'clausal', 'S022: {anh ta đã giúp tổ chức} (trong câu)', 'high', None, '[TC] tọa hợp song song “∅ và đóng vai trò đáng kể”; đối ứng 1–1 E-EN1', 1, 'vào ngày 7/10/2023 ', '{anh ta đã giúp tổ chức}', 'TC'),

]

# ---- P16 ----
P16_ST = [
 # S002
 ('S002', 'the ruble', 'L', 'repetition', 'S001: Russia\u2019s plunging currency', 'high', None, None, 1),
 ('S002', 'the U.S. dollar', 'L', 'collocation', 'S001: currency', 'low', None, 'currency association', 1),
 ('S002', 'Russians', 'L', 'repetition', 'S001: Russia\u2019s', 'high', None, None, 1),
 # S003
 ('S003', 'That cutback', 'L', 'repetition', 'S002: cutting back on spending', 'high', 'R: that', None, 1),
 ('S003', 'the beach resort city of Pattaya', 'L', 'repetition', 'S001: tourism industry', 'med', None, None, 1),
 # S004
 ('S004', 'the Russians', 'L', 'repetition', 'S002: Russians', 'high', None, None, 1),
 ('S004', 'Thai', 'L', 'repetition', 'S001: Thailand\u2019s', 'high', None, None, 1),
 # S005
 ('S005', 'the Pattaya office', 'L', 'repetition', 'S003: Pattaya', 'high', None, None, 1),
 ('S005', 'the Tourism Association of Thailand', 'L', 'repetition', 'S004: the Thai Hotel Association', 'med', None, 'association chain', 1),
 ('S005', 'VOA', 'L', 'repetition', 'S001: (VOA dateline excluded)', 'low', None, 'dateline excluded; weak', 1),
 # S006
 ('S006', 'it\u2019s', 'R', 'personal', 'S005: the Russian market', 'med', None, None, 1),
 ('S006', 'Pattaya', 'L', 'repetition', 'S005: the Pattaya office', 'high', None, None, 1),
 # S007
 ('S007', 'Russian tourists', 'L', 'repetition', 'S004: the Russians ... big spenders', 'high', None, None, 1),
 # S008
 ('S008', 'Russian tourists', 'L', 'repetition', 'S007: Russian tourists', 'high', None, 'verbatim', 1),
 ('S008', 'Suladda', 'L', 'repetition', 'S005: Suladda Sarutilavan', 'high', None, None, 1),
 # S009
 ('S009', 'Russian visitors', 'L', 'repetition', 'S008: Russian tourists', 'high', None, None, 1),
 ('S009', 'Thailand', 'L', 'repetition', 'S004: Thailand\u2019s', 'high', None, None, 1),
 # S010
 ('S010', 'But', 'C', 'adversative', 'S009: 1.4 million visitors', 'high', None, None, 1),
 ('S010', "the national hotel operators' association", 'L', 'repetition', 'S004: the Thai Hotel Association', 'high', None, None, 1),
 # S011
 ('S011', 'Suladda', 'L', 'repetition', 'S008: Suladda', 'high', None, None, 1),
 ('S011', 'Pattaya', 'L', 'repetition', 'S006: Pattaya', 'high', None, None, 1),
 ('S011', 'visitors', 'L', 'repetition', 'S009: Russian visitors', 'high', None, None, 1),
 # S013
 ('S013', 'the Russian market', 'L', 'repetition', 'S006: a major or main market', 'high', None, None, 1),
 # S014
 ('S014', 'But', 'C', 'adversative', 'S013: quite worried about it', 'high', None, None, 1),
 ('S014', 'they', 'R', 'personal', 'S013: they (operators and hoteliers)', 'high', None, None, 1),
 ('S014', 'other markets', 'L', 'repetition', 'S013: the Russian market', 'high', None, None, 1),
 ('S014', 'the decreasing number of Russian', 'L', 'repetition', 'S009: Russian visitors', 'high', None, None, 1),
 # S015
 ('S015', 'The Thai resort cities', 'L', 'repetition', 'S003: the beach resort city of Pattaya', 'high', None, None, 1),
 ('S015', 'the Russians', 'L', 'repetition', 'S014: Russian', 'high', None, None, 1),
 ('S015', 'marketing', 'L', 'repetition', 'S011: (marketing implied in destinations)', 'low', None, 'weak', 1),
 # S016
 ('S016', 'the Russian market', 'L', 'repetition', 'S014: other markets / the Russian market', 'high', None, None, 1),
 ('S016', 'tourists', 'L', 'repetition', 'S008: Russian tourists', 'high', None, None, 1),
 ('S016', 'Thailand', 'L', 'repetition', 'S009: Thailand', 'high', None, None, 1),
 # S017
 ('S017', 'Russian', 'L', 'repetition', 'S016: the Russian market', 'high', None, 'Russian winter', 1),
 # S018
 ('S018', 'Russian President Vladimir Putin', 'L', 'repetition', 'S017: Russian', 'high', None, None, 1),
 ('S018', 'the "unfavorable situation"', 'L', 'repetition', 'S001: plunging currency creating serious concerns', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_16 (§2–§3) ----
 ('S001', None, 'E', 'nominal', 'S001: {which is} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “industry, ∅ already suffering…”', 1, 'tourism industry, ', '{which is}', 'TC'),
 ('S011', None, 'E', 'nominal', 'S011: {which are} (trong câu)', 'med', None, '[TC] đồng vị rút gọn “Samui - ∅ all heavily reliant…”', 1, 'Phuket and Samui - ', '{which are}', 'TC'),
 ('S011', None, 'E', 'nominal', 'S011: {who are} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “visitors ∅ converting Russian rubles…”', 1, 'reliant on visitors ', '{who are}', 'TC'),
 ('S015', None, 'E', 'nominal', 'S015: {which are} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “islands ∅ dependent on the Russians”', 1, 'cities and islands ', '{which are}', 'TC'),
 ('S017', 'those', 'S', 'nominal', 'S016: an affordable warm escape', 'high', None, '[TC] those + VP “still yearning”', 1, None, None, 'TC'),
 ('S017', None, 'E', 'nominal', 'S017: {who are} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “those ∅ still yearning…”', 1, 'As for those ', '{who are}', 'TC'),
 ('S018', None, 'E', 'nominal', 'S018: {which is} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “situation ∅ depreciating the ruble”', 1, 'unfavorable situation" ', '{which is}', 'TC'),

]
P16_TT = [
 # S002
 ('S002', 'đồng rúp', 'L', 'repetition', 'S001: Chỉ tệ Nga', 'high', None, None, 1),
 ('S002', 'đồng đôla', 'L', 'collocation', 'S001: đôla (currency chain)', 'low', None, 'currency association', 1),
 ('S002', 'người Nga', 'L', 'repetition', 'S001: Nga', 'high', None, None, 1),
 # S003
 ('S003', 'Sự cắt giảm đó', 'L', 'repetition', 'S002: cắt giảm chi tiêu', 'high', 'R: đó', None, 1),
 ('S003', 'Pattaya', 'L', 'repetition', 'S001: (Pattaya implied in tourism industry)', 'low', None, 'first overt mention; weak', 1),
 # S004
 ('S004', 'du khách Nga', 'L', 'repetition', 'S002: người Nga', 'high', None, None, 1),
 ('S004', 'Thái', 'L', 'repetition', 'S001: Thái Lan', 'high', None, None, 1),
 # S005
 ('S005', 'Pattaya', 'L', 'repetition', 'S003: Pattaya', 'high', None, None, 1),
 ('S005', 'Hiệp hội Du lịch Thái Lan', 'L', 'repetition', 'S004: Hiệp hội Khách sạn Thái', 'med', None, 'association chain', 1),
 ('S005', 'VOA', 'L', 'repetition', 'S002: (VOA dateline excluded)', 'low', None, 'dateline excluded; weak', 1),
 # S006
 ('S006', 'đó', 'R', 'demonstrative', 'S005: thị trường Nga (implied)', 'med', None, None, 1),
 ('S006', 'Pattaya', 'L', 'repetition', 'S005: Pattaya', 'high', None, None, 1),
 # S007
 ('S007', 'Du khách Nga', 'L', 'repetition', 'S004: du khách Nga', 'high', None, None, 1),
 # S008
 ('S008', 'du khách Nga', 'L', 'repetition', 'S007: Du khách Nga', 'high', None, 'verbatim', 1),
 ('S008', 'chúng tôi', 'R', 'personal', 'S005: Bà Suladda (quoted speaker)', 'med', None, None, 1),
 ('S008', 'Pattaya', 'L', 'repetition', 'S006: Pattaya', 'high', None, None, 1),
 # S009
 ('S009', 'du khách Nga', 'L', 'repetition', 'S008: du khách Nga', 'high', None, None, 1),
 ('S009', 'Thái Lan', 'L', 'repetition', 'S005: Hiệp hội Du lịch Thái Lan', 'high', None, None, 1),
 # S010
 ('S010', 'Nhưng', 'C', 'adversative', 'S009: 1,4 triệu du khách', 'high', None, None, 1),
 ('S010', 'hiệp hội điều hành khách sạn quốc gia', 'L', 'repetition', 'S004: Hiệp hội Khách sạn Thái', 'high', None, None, 1),
 # S011
 ('S011', 'Bà Suladda', 'L', 'repetition', 'S005: Bà Suladda Sarutilavan', 'high', None, None, 1),
 ('S011', 'hiệp hội này', 'L', 'repetition', 'S010: hiệp hội điều hành khách sạn quốc gia', 'high', 'R: này', None, 1),
 ('S011', 'Pattaya', 'L', 'repetition', 'S008: Pattaya', 'high', None, None, 1),
 ('S011', 'du khách', 'L', 'repetition', 'S009: du khách Nga', 'high', None, None, 1),
 # S012
 ('S012', 'tình trạng này', 'L', 'repetition', 'S002: đồng rúp sụt xuống', 'high', 'R: này', None, 1),
 # S013
 ('S013', 'thị trường Nga', 'L', 'repetition', 'S006: thị trường lớn', 'high', None, None, 1),
 # S014
 ('S014', 'Nhưng', 'C', 'adversative', 'S013: lấy làm lo ngại', 'high', None, None, 1),
 ('S014', 'họ', 'R', 'personal', 'S013: họ', 'high', None, None, 1),
 ('S014', 'các thị trường khác', 'L', 'repetition', 'S013: thị trường Nga', 'high', None, None, 1),
 ('S014', 'du khách Nga', 'L', 'repetition', 'S011: du khách', 'high', None, None, 1),
 # S015
 ('S015', 'Các thành phố nghỉ mát', 'L', 'repetition', 'S003: thành phố biển nghỉ mát Pattaya', 'high', None, None, 1),
 ('S015', 'Thái Lan', 'L', 'repetition', 'S009: Thái Lan', 'high', None, None, 1),
 ('S015', 'người Nga', 'L', 'repetition', 'S014: du khách Nga', 'high', None, None, 1),
 # S016
 ('S016', 'thị trường Nga', 'L', 'repetition', 'S014: các thị trường khác', 'high', None, None, 1),
 ('S016', 'du khách', 'L', 'repetition', 'S014: du khách Nga', 'high', None, None, 1),
 ('S016', 'Thái Lan', 'L', 'repetition', 'S015: Thái Lan', 'high', None, None, 1),
 # S017
 ('S017', 'Nga', 'L', 'repetition', 'S016: thị trường Nga', 'high', None, 'mùa đông ... của Nga', 1),
 # S018
 ('S018', 'Tổng thống Nga', 'L', 'repetition', 'S017: Nga', 'high', None, None, 1),
 ('S018', 'tình hình', 'L', 'repetition', 'S012: tình trạng này', 'med', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_16 (§2) ----
 ('S004', None, 'E', 'nominal', 'S004: {được} (trong câu)', 'med', None, '[TC] rút gọn “du khách Nga, ∅ nổi tiếng là chịu chi”', 1, 'mất đi du khách Nga, ', '{được}', 'TC'),
 ('S004', None, 'E', 'nominal', 'S004: {diễn ra} (trong câu)', 'med', None, '[TC] quan hệ vị ngữ đầy đủ EN “which runs” → VI còn PP thời gian “mùa cao điểm ∅ sắp tới…”', 1, 'trong mùa cao điểm', '{diễn ra}', 'TC'),
 ('S008', None, 'E', 'clausal', 'S007: said Suladda (khung dẫn mở)', 'low', None, '[LC] biên: lược khung dẫn đóng “said Suladda” lần 1 (P09 tái hiện)', 1, 'đến Pattaya.”', '{said Suladda}', 'LC'),
 ('S014', None, 'E', 'clausal', 'S013: said Suladda (khung dẫn mở)', 'low', None, '[LC] biên: lược khung dẫn đóng “said Suladda” lần 2', 1, 'sụt giảm đến Pattaya.”', '{said Suladda}', 'LC'),
 ('S017', None, 'E', 'nominal', 'S017: {người ta} (trong câu)', 'low', None, '[TC] biên: “∅ nghe nói họ đang chuyển kế hoạch…” — evidential ngữ pháp hóa', 1, 'của Nga, ', '{người ta}', 'TC'),

]
