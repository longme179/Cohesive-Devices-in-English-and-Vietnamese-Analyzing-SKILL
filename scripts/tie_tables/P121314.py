# P12/P13/P14 tie tables.

# ---- P12 ----
P12_ST = [
 ('S002', 'the two politicians', 'R', 'quantified', 'S001: Robert F. Kennedy Jr. and Donald Trump', 'med', None, 'general word + numeral; quantified reference', 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_12 (§2) ----
 # EN không có E/S (2 câu bão hòa); "the two politicians" là R, không phải S.

]
P12_TT = [
 ('S002', 'Trump', 'L', 'repetition', 'S001: Donald Trump', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_12 (§2) ----
 ('S001', None, 'E', 'nominal', 'S001: {người} (trong câu)', 'med', None, '[TC] lược quan hệ từ chủ ngữ “một nhóm cử tri {người} ủng hộ…”; ∅ tự sinh trong câu VI-only', 1, 'một nhóm cử tri ', '{người}', 'TC'),
 ('S002', None, 'E', 'nominal', 'S002: {Robert F. Kennedy Jr.} (trong câu)', 'med', None, '[TC] control: “tuyên bố ủng hộ ∅ Trump” — chủ ngữ của “ủng hộ” bị lược, hồi phục từ chủ ngữ “tuyên bố”; EN dùng “his endorsement”', 1, 'tuyên bố ủng hộ ', '{Robert F. Kennedy Jr.}', 'TC'),

]

# ---- P13 ----
P13_ST = [
 # S002
 ('S002', 'Any visit', 'L', 'repetition', 'S001: a possible visit', 'high', None, None, 1),
 ('S002', 'a pope', 'L', 'repetition', 'S001: Pope Francis', 'med', None, None, 1),
 ('S002', 'the reclusive state', 'L', 'synonym', 'S001: North Korea', 'high', None, None, 1),
 # S003
 ('S003', 'its', 'R', 'personal', 'S002: the reclusive state', 'high', None, None, 1),
 ('S003', 'Catholic', 'L', 'repetition', 'S001: a Catholic news agency', 'high', None, None, 1),
 # S004
 ('S004', 'the announcement', 'L', 'repetition', 'S001: has said', 'low', None, 'announcement ~ said; weak', 1),
 ('S004', 'South Korea', 'L', 'repetition', 'S001: South Korea\u2019s intelligence chief', 'high', None, None, 1),
 # S005
 ('S005', 'Fides', 'L', 'repetition', 'S004: Fides', 'high', None, None, 1),
 ('S005', 'Park', 'L', 'repetition', 'S004: Park Jie-won', 'high', None, None, 1),
 ('S005', 'the Mass', 'L', 'repetition', 'S004: a Mass in Mokpo', 'high', None, None, 1),
 ('S005', "the Vatican's", 'L', 'repetition', 'S001: associated with the Vatican', 'high', None, None, 1),
 ('S005', 'South Korea', 'L', 'repetition', 'S004: South Korea', 'high', None, None, 1),
 ('S005', 'a possible papal visit', 'L', 'repetition', 'S001: a possible visit by Pope Francis', 'high', None, None, 1),
 # S006
 ('S006', 'Park', 'L', 'repetition', 'S005: Park', 'high', None, None, 1),
 ('S006', 'the National Intelligence Service', 'L', 'repetition', 'S001: South Korea\u2019s intelligence chief', 'high', None, 'intelligence chain', 1),
 # S007
 ('S007', 'Park', 'L', 'repetition', 'S006: Park', 'high', None, None, 1),
 ('S007', 'his attendance', 'R', 'personal', 'S006: Park (director of the NIS)', 'med', None, 'his = Park (person who answered disambiguated)', 1),
 # S008
 ('S008', 'The intelligence agency', 'L', 'repetition', 'S006: the National Intelligence Service', 'high', None, None, 1),
 ('S008', "Park's comments", 'L', 'repetition', 'S007: his comments', 'high', None, None, 1),
 # S009
 ('S009', 'North Korean', 'L', 'repetition', 'S002: the reclusive state (North Korea)', 'med', None, None, 1),
 ('S009', 'the pope', 'L', 'repetition', 'S002: a pope', 'high', None, None, 1),
 # S010
 ('S010', 'Kim and Moon', 'L', 'repetition', 'S009: Kim Jong Un + Moon Jae-in', 'high', None, None, 1),
 # S011
 ('S011', 'Vatican officials', 'L', 'repetition', 'S005: the Vatican\u2019s ambassador', 'high', None, None, 1),
 ('S011', 'invitation', 'L', 'repetition', 'S009: an invitation from North Korean leader', 'high', None, None, 1),
 # S012
 ('S012', 'It', 'R', 'personal', 'S011: an official written invitation', 'high', None, None, 1),
 ('S012', 'invitation', 'L', 'repetition', 'S011: invitation', 'high', None, None, 1),
 # S013
 ('S013', 'They', 'R', 'personal', 'S011: Vatican officials', 'high', None, None, 1),
 ('S013', 'the pope', 'L', 'repetition', 'S009: the pope', 'high', None, None, 1),
 ('S013', 'the two Koreas', 'L', 'repetition', 'S001: North Korea + S009: South Korean President', 'high', None, None, 1),
 ('S013', 'such a trip', 'R', 'comparative', 'S001-S002: the possible visit', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_13 (§2) ----
 ('S007', None, 'E', 'nominal', 'S007: {a person} (trong câu)', 'med', None, '[TC] chủ ngữ “a person” chia sẻ qua chuỗi vị ngữ “confirmed … but would not confirm”; ∅ đặt ở vế tọa hợp thứ hai', 1, 'confirmed his attendance but ', '{a person}', 'TC'),

]
P13_TT = [
 # S002
 ('S002', 'chuyến thăm', 'L', 'repetition', 'S001: chuyến thăm', 'high', None, None, 1),
 ('S002', 'một vị giáo hoàng', 'L', 'repetition', 'S001: Giáo hoàng Francis', 'med', None, None, 1),
 ('S002', 'Triều Tiên', 'L', 'repetition', 'S001: Triều Tiên', 'high', None, None, 1),
 # S003
 ('S003', 'Triều Tiên', 'L', 'repetition', 'S002: Triều Tiên', 'high', None, 'công dân Triều Tiên', 1),
 ('S003', 'Công giáo', 'L', 'repetition', 'S001: (Catholic implied in Vatican agency)', 'low', None, 'first overt Công giáo mention; weak', 1),
 # S004
 ('S004', 'thông báo này', 'L', 'repetition', 'S001: cho biết', 'low', None, None, 1),
 ('S004', 'Hàn Quốc', 'L', 'repetition', 'S001: Hàn Quốc', 'high', None, None, 1),
 # S005
 ('S005', 'Fides', 'L', 'repetition', 'S004: Fides', 'high', None, None, 1),
 ('S005', 'ông Park', 'L', 'repetition', 'S004: ông Park Jie-won', 'high', None, None, 1),
 ('S005', 'Thánh lễ', 'L', 'repetition', 'S004: một thánh lễ', 'high', None, None, 1),
 ('S005', 'Vatican', 'L', 'repetition', 'S004: Hiệp hội Truyền giáo Giáo hoàng', 'med', None, 'Vatican chain', 1),
 ('S005', 'Hàn Quốc', 'L', 'repetition', 'S004: Hàn Quốc', 'high', None, None, 1),
 ('S005', 'Giáo hoàng Francis', 'L', 'repetition', 'S001: Giáo hoàng Francis', 'high', None, None, 1),
 # S006
 ('S006', 'Ông Park', 'L', 'repetition', 'S005: ông Park', 'high', None, None, 1),
 ('S006', 'Cơ quan Tình báo Quốc gia', 'L', 'repetition', 'S001: cơ quan tình báo Hàn Quốc', 'high', None, None, 1),
 # S007
 ('S007', 'ông Park', 'L', 'repetition', 'S006: Ông Park', 'high', None, None, 1),
 ('S007', 'của ông', 'R', 'personal', 'S006: Ông Park', 'high', None, 'sự tham dự của ông', 1),
 # S008
 ('S008', 'Cơ quan tình báo', 'L', 'repetition', 'S006: Cơ quan Tình báo Quốc gia', 'high', None, None, 1),
 ('S008', 'ông Park', 'L', 'repetition', 'S007: ông Park', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_13 (§2) ----
 ('S007', None, 'E', 'nominal', 'S007: {một người} (trong câu)', 'med', None, '[TC] chủ ngữ “một người” chia sẻ qua 3 vị ngữ tọa hợp; ∅ đặt ở vế “nhưng không xác nhận…”', 1, 'sự tham dự của ông nhưng ', '{một người}', 'TC'),

]

# ---- P14 ----
P14_ST = [
 # S002
 ('S002', 'The U.S. Customs and Border Protection app', 'L', 'repetition', 'S001: a new app', 'high', None, None, 1),
 # S003
 ('S003', 'The CBP Home app', 'L', 'repetition', 'S002: called CBP Home', 'high', None, None, 1),
 ('S003', 'aliens', 'L', 'synonym', 'S001-S002: immigrants ... illegally', 'med', None, 'aliens ~ immigrants', 1),
 # S004
 ('S004', 'they', 'R', 'personal', 'S003: aliens', 'high', None, None, 1),
 ('S004', 'we', 'R', 'personal', 'S003: (the administration speaker)', 'med', None, 'institutional we', 1),
 ('S004', 'them', 'R', 'personal', 'S003: aliens', 'high', None, None, 1),
 ('S004', 'they', 'R', 'personal', 'S003: aliens', 'high', None, None, 2),
 # S005
 ('S005', 'Trump', 'L', 'repetition', 'S001: The Trump administration', 'high', None, None, 1),
 ('S005', 'deport', 'L', 'repetition', 'S002: signal their intent to depart (deport chain)', 'med', None, None, 1),
 ('S005', 'migrants in the U.S. illegally', 'L', 'repetition', 'S001: immigrants in the United States illegally', 'high', None, 'migrants ~ immigrants', 1),
 # S006
 ('S006', "Trump's", 'L', 'repetition', 'S005: Trump', 'high', None, None, 1),
 ('S006', 'deportation', 'L', 'repetition', 'S005: deport', 'high', None, 'morphological reiteration', 1),
 # S007
 ('S007', 'The Trump administration', 'L', 'repetition', 'S006: Trump\u2019s', 'high', None, None, 1),
 ('S007', 'immigrants in the United States illegally', 'L', 'repetition', 'S005: migrants in the U.S. illegally', 'high', None, 'verbatim', 1),
 # S008
 ('S008', 'A Trump administration regulation', 'L', 'repetition', 'S007: The Trump administration', 'high', None, None, 1),
 ('S008', 'legal status', 'L', 'repetition', 'S001: illegally (status chain)', 'med', None, None, 1),
 # S009
 ('S009', 'CBP Home', 'L', 'repetition', 'S003: The CBP Home app', 'high', None, None, 1),
 ('S009', 'an app', 'L', 'repetition', 'S002: The U.S. Customs and Border Protection app', 'high', None, None, 1),
 ('S009', 'Biden', 'L', 'repetition', 'S006: Joe Biden', 'high', None, None, 1),
 # S010
 ('S010', 'The Biden-era app', 'L', 'repetition', 'S009: an app known as CBP One ... under Biden', 'high', None, None, 1),
 ('S010', 'migrants', 'L', 'repetition', 'S005: migrants', 'high', None, None, 1),
 # S011
 ('S011', 'Republicans', 'L', 'repetition', 'S005: a Republican', 'high', None, None, 1),
 ('S011', 'the Biden program', 'L', 'repetition', 'S010: The Biden-era app ... feature', 'high', None, None, 1),
 ('S011', 'the United States', 'L', 'repetition', 'S007: the United States', 'high', None, None, 1),
 # S012
 ('S012', 'Trump', 'L', 'repetition', 'S008: A Trump administration regulation', 'high', None, None, 1),
 ('S012', 'CBP One', 'L', 'repetition', 'S009: CBP One', 'high', None, None, 1),
 ('S012', 'migrants', 'L', 'repetition', 'S010: migrants', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_14 (§2) ----
 ('S002', None, 'E', 'nominal', 'S002: {which is} (trong câu)', 'med', None, '[TC] quan hệ rút gọn “app, ∅ called CBP Home”; 3 vị trí còn lại: known as CBP One, set to take effect, after taking office', 1, 'Border Protection app, ', '{which is}', 'TC'),
 ('S004', None, 'E', 'verbal', 'S004: {self-deport / leave} (trong câu)', 'high', None, '[TC] do-ellipsis “If they don’t ∅, we will find them”', 1, 'If they don’t', '{self-deport / leave}', 'TC'),

]
P14_TT = [
 # S002
 ('S002', 'Ứng dụng', 'L', 'repetition', 'S001: một ứng dụng mới', 'high', None, None, 1),
 # S003
 ('S003', 'Ứng dụng CBP Home', 'L', 'repetition', 'S002: CBP Home', 'high', None, None, 1),
 ('S003', 'người nhập cư', 'L', 'repetition', 'S002: người nhập cư', 'high', None, None, 1),
 # S004
 ('S004', 'họ', 'R', 'personal', 'S003: người nhập cư', 'high', None, None, 1),
 ('S004', 'chúng tôi', 'R', 'personal', 'S003: (the administration speaker)', 'med', None, 'institutional chúng tôi', 1),
 ('S004', 'họ', 'R', 'personal', 'S003: người nhập cư', 'high', None, None, 2),
 ('S004', 'họ', 'R', 'personal', 'S003: người nhập cư', 'high', None, None, 3),
 # S005
 ('S005', 'Tổng thống Trump', 'L', 'repetition', 'S001: Chính quyền Trump', 'high', None, None, 1),
 ('S005', 'trục xuất', 'L', 'repetition', 'S001: tự trục xuất', 'high', None, None, 1),
 ('S005', 'di dân', 'L', 'repetition', 'S002: người nhập cư', 'med', None, 'di dân ~ người nhập cư', 1),
 # S006
 ('S006', 'Số liệu trục xuất', 'L', 'repetition', 'S005: trục xuất', 'high', None, None, 1),
 ('S006', 'ông Trump', 'L', 'repetition', 'S005: Tổng thống Trump', 'high', None, None, 1),
 # S007
 ('S007', 'Chính quyền Trump', 'L', 'repetition', 'S006: ông Trump', 'high', None, None, 1),
 ('S007', 'cũng', 'C', 'additive', 'S006: deportation numbers', 'med', None, None, 1),
 ('S007', 'người nhập cư trái phép', 'L', 'repetition', 'S005: di dân vào Mỹ trái phép', 'high', None, None, 1),
 # S008
 ('S008', 'chính quyền Trump', 'L', 'repetition', 'S007: Chính quyền Trump', 'high', None, None, 1),
 # S009
 ('S009', 'CBP Home', 'L', 'repetition', 'S003: Ứng dụng CBP Home', 'high', None, None, 1),
 ('S009', 'Biden', 'L', 'repetition', 'S006: Biden', 'high', None, None, 1),
 # S010
 ('S010', 'Ứng dụng CBP One', 'L', 'repetition', 'S009: CBP One', 'high', None, None, 1),
 ('S010', 'thời Biden', 'L', 'repetition', 'S009: dưới thời Biden', 'high', None, None, 1),
 ('S010', 'di dân', 'L', 'repetition', 'S005: di dân', 'high', None, None, 1),
 # S011
 ('S011', 'Các đảng viên Cộng hòa', 'L', 'repetition', 'S005: một đảng viên Cộng hòa', 'high', None, None, 1),
 ('S011', 'chương trình của thời Biden', 'L', 'repetition', 'S010: thời Biden', 'high', None, None, 1),
 ('S011', 'di cư', 'L', 'repetition', 'S010: di dân', 'med', None, 'morphological reiteration (di)', 1),
 # S012
 ('S012', 'Ông Trump', 'L', 'repetition', 'S008: chính quyền Trump', 'high', None, None, 1),
 ('S012', 'CBP One', 'L', 'repetition', 'S010: Ứng dụng CBP One', 'high', None, None, 1),
 ('S012', 'di dân', 'L', 'repetition', 'S010: di dân', 'high', None, None, 1),
 # ---- S/E bổ sung thủ công từ semantic_analysis/Pair_14 (§2–§3) ----
 ('S002', None, 'E', 'nominal', 'S002: {tự} (trong câu)', 'med', None, '[TC] control “để người dùng ∅ thông báo ý định rời đi”; 2 vị trí còn lại: ∅ phải đăng ký, buộc ∅ phải rời', 1, 'để người dùng ', '{tự}', 'TC'),
 ('S004', None, 'E', 'nominal', 'S004: {họ} (trong câu)', 'high', None, '[TC] bổ ngữ “truy tìm ∅” bị lược; đối lập “trục xuất họ” giữ tân ngữ', 1, 'chúng tôi sẽ truy tìm', '{họ}', 'TC'),
 ('S004', 'không làm vậy', 'S', 'verbal', 'S004: EN do-ellipsis “don’t”', 'high', None, '[TC] E→S chéo loại: pro-động từ “làm vậy” hiện thực hóa chỗ trống “don’t” của EN', 1, None, None, 'TC'),

]
