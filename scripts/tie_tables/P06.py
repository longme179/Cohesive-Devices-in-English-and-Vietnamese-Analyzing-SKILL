# P06 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S003
 ('S003', 'The program', 'L', 'repetition', 'S002: the US Global Entry program', 'high', None, None, 1),
 ('S003', 'Australians', 'L', 'repetition', 'S002: Australia', 'med', None, 'morphological reiteration', 1),
 ('S003', 'travel', 'L', 'synonym', 'S001: planning a trip', 'med', None, None, 1),
 ('S003', 'the US', 'L', 'repetition', 'S001: the United States', 'high', None, 'abbreviation', 1),
 # S004
 ('S004', 'Global Entry program', 'L', 'repetition', 'S002: the US Global Entry program', 'high', None, None, 1),
 # S005
 ('S005', 'Australians', 'L', 'repetition', 'S003: Australians', 'med', None, None, 1),
 # S006
 ('S006', 'Australian', 'L', 'repetition', 'S005: Australians', 'med', None, 'Australian passport holders', 1),
 ('S006', 'ETA', 'L', 'repetition', 'S005: (ETA)', 'high', None, 'abbreviation', 1),
 # S007
 ('S007', 'Australians', 'L', 'repetition', 'S006: Australian passport holders', 'med', None, None, 1),
 ('S007', 'travelling', 'L', 'repetition', 'S005: travelling', 'med', None, None, 1),
 # S008
 ('S008', 'ETIAS', 'L', 'repetition', 'S007: an ETIAS', 'high', None, None, 1),
 ('S008', 'travellers', 'L', 'repetition', 'S007: Australians travelling', 'med', None, 'morphological reiteration', 1),
 # S009
 ('S009', 'It', 'R', 'personal', 'S008: The ETIAS process', 'high', None, None, 1),
 ('S009', 'the new process', 'L', 'repetition', 'S008: The ETIAS process', 'high', None, None, 1),
 ('S009', 'travelling', 'L', 'repetition', 'S007: travelling', 'med', None, None, 1),
 ('S009', 'European', 'L', 'repetition', 'S007: Europe\u2019s Schengen Area', 'med', None, 'morphological reiteration', 1),
 # S011
 ('S011', 'The airline', 'L', 'general word', 'S010: Qantas', 'high', None, None, 1),
 # S012
 ('S012', 'Meanwhile', 'C', 'additive', 'S011: Qantas route changes', 'high', None, None, 1),
 # S013
 ('S013', 'also', 'C', 'additive', 'S011-S012: route cuts', 'med', None, None, 1),
 ('S013', 'daily', 'L', 'repetition', 'S011: daily', 'med', None, None, 1),
 # S014
 ('S014', 'The airline', 'L', 'general word', 'S013: Virgin Australia', 'high', None, None, 1),
 ('S014', 'the route', 'L', 'general word', 'S013: Cairns to Tokyo service', 'med', None, None, 1),
 # S015
 ('S015', 'travelling', 'L', 'repetition', 'S007: travelling', 'med', None, None, 1),
 ('S015', 'Australia', 'L', 'repetition', 'S002: Australia', 'med', None, None, 1),
 # S016
 ('S016', 'Australia', 'L', 'repetition', 'S015: Australia', 'med', None, None, 1),
 # S017
 ('S017', 'The report', 'L', 'repetition', 'S016: Amex Air Monitor report', 'high', None, None, 1),
 ('S017', 'airfares', 'L', 'repetition', 'S016: airfares', 'high', None, None, 1),
 ('S017', 'ticket prices', 'L', 'synonym', 'S016: airfares', 'med', None, None, 1),
 # S018
 ('S018', 'domestic airfares', 'L', 'repetition', 'S017: domestic economy airfares', 'high', None, None, 1),
 ('S018', 'increased', 'L', 'synonym', 'S017: jump', 'med', None, 'jump / surge ~ increase', 1),
 # S019
 ('S019', 'airline', 'L', 'repetition', 'S011: The airline', 'med', None, 'domestic airline industry', 1),
 ('S019', 'airfares', 'L', 'repetition', 'S018: domestic airfares', 'high', None, None, 1),
 # S020
 ('S020', 'However', 'C', 'adversative', 'S019: difficult to speculate', 'high', None, None, 1),
 ('S020', 'ACCC', 'L', 'repetition', 'S018: (ACCC)', 'high', None, 'abbreviation', 1),
 ('S020', 'airfares', 'L', 'repetition', 'S019: airfares', 'high', None, None, 1),
 ('S020', 'competition', 'L', 'repetition', 'S018: reduction in competition', 'high', None, None, 1),
 # S021
 ('S021', 'airline', 'L', 'repetition', 'S019: airline', 'med', None, 'an additional airline', 1),
 ('S021', 'route', 'L', 'repetition', 'S014: the route', 'med', None, None, 1),
 ('S021', 'airfares', 'L', 'repetition', 'S020: airfares', 'high', None, None, 1),
 # S022
 ('S022', "airline's", 'L', 'repetition', 'S021: airline', 'med', None, 'morphological reiteration', 1),
 # S023
 ('S023', 'However', 'C', 'adversative', 'S022: jet fuel as major cost', 'high', None, None, 1),
 ('S023', 'our', 'R', 'personal', 'S019: an ACCC spokesperson', 'med', None, 'institutional our', 1),
 ('S023', 'report', 'L', 'repetition', 'S017: The report', 'med', None, 'genre echo', 1),
 ('S023', 'the price of jet fuel', 'L', 'repetition', 'S022: the price of jet fuel', 'high', None, 'verbatim', 1),
 # S024
 ('S024', 'travel', 'L', 'repetition', 'S003: travel', 'med', None, 'the world of travel', 1),
 # S025
 ('S025', 'Travel', 'L', 'repetition', 'S024: travel', 'med', None, None, 1),
 ('S025', 'Trends', 'L', 'repetition', 'S024: trends', 'high', None, None, 1),
 ('S025', 'report', 'L', 'repetition', 'S023: report', 'med', None, 'genre echo', 1),
 ('S025', 'destinations', 'L', 'repetition', 'S024: the actual destinations', 'high', None, None, 1),
 # S026
 ('S026', 'the world', 'L', 'repetition', 'S024: the world of travel', 'med', None, None, 1),
 # S027
 ('S027', 'search traffic', 'L', 'repetition', 'S025: online search traffic', 'high', None, None, 1),
 ('S027', 'surged', 'L', 'repetition', 'S016: surge', 'med', None, 'morphological reiteration', 1),
 ('S027', 'tourist hot spot', 'L', 'general word', 'S026: Siem Reap in Cambodia', 'high', None, None, 1),
 # S028
 ('S028', 'travel', 'L', 'repetition', 'S025: Travel', 'med', None, 'travel club', 1),
 # S029
 ('S029', 'Richards', 'L', 'repetition', 'S028: Vanessa Richards', 'high', None, None, 1),
 ('S029', 'content creators', 'L', 'repetition', 'S028: content creators', 'high', None, None, 1),
 ('S029', 'travel industry', 'L', 'repetition', 'S028: travel club', 'med', None, None, 1),
 ('S029', 'trends', 'L', 'repetition', 'S025: Trends', 'med', None, None, 1),
 # S030
 ('S030', 'Content creators', 'L', 'repetition', 'S029: content creators', 'high', None, None, 1),
 ('S030', 'travel', 'L', 'repetition', 'S029: travel industry', 'med', None, None, 1),
 # S031
 ('S031', 'It', 'R', 'personal', 'S030: the driving force', 'med', None, 'It\u2019s the ability', 1),
 ('S031', 'their', 'R', 'personal', 'S030: Content creators', 'high', None, None, 1),
 # S032
 ('S032', 'travel', 'L', 'repetition', 'S030: travel', 'med', None, 'Community-driven travel', 1),
 ('S032', 'travellers', 'L', 'repetition', 'S008: travellers', 'low', None, 'distant chain', 1),
 ('S032', 'recommendations', 'L', 'repetition', 'S031: recommendations', 'high', None, None, 1),
 ('S032', 'the change', 'L', 'general word', 'S005: one of the most significant changes', 'med', None, None, 1),
 # S033
 ('S033', 'That', 'R', 'demonstrative', 'S032: community-driven travel and human connection', 'high', None, None, 1),
 # S034
 ('S034', 'Travellers', 'L', 'repetition', 'S032: travellers', 'high', None, None, 1),
 ('S034', 'eco-conscious', 'L', 'repetition', 'S029: eco-conscious travel', 'high', None, None, 1),
 # S035
 ('S035', 'Destinations', 'L', 'repetition', 'S025: destinations', 'high', None, None, 1),
 ('S035', 'that', 'R', 'demonstrative', 'S034: demanding eco-conscious options', 'high', None, None, 1),
 ('S035', 'tourism', 'L', 'synonym', 'S024: travel', 'med', None, 'regenerative tourism', 1),
 # S036
 ('S036', 'Skyscanner', 'L', 'repetition', 'S025: Skyscanner\u2019s', 'high', None, None, 1),
 ('S036', 'travellers', 'L', 'repetition', 'S034: Travellers', 'high', None, None, 1),
 # S037
 ('S037', 'airlines', 'L', 'repetition', 'S022: airline\u2019s', 'med', None, 'morphological reiteration', 1),
 ('S037', 'travellers', 'L', 'repetition', 'S036: travellers', 'high', None, None, 1),
 ('S037', 'respond', 'L', 'repetition', 'S035: respond', 'high', None, None, 1),
 ('S037', 'demand', 'L', 'repetition', 'S015: the demand', 'med', None, 'market demand', 1),
 # S038
 ('S038', 'At the same time', 'C', 'additive', 'S037: AI adoption', 'med', None, None, 1),
 ('S038', 'airlines', 'L', 'repetition', 'S037: airlines', 'high', None, None, 1),
 ('S038', 'routes', 'L', 'repetition', 'S021: route', 'med', None, None, 1),
]

TT = [
 # S002
 ('S002', 'Hoa Kỳ', 'L', 'repetition', 'S001: Hoa Kỳ', 'high', None, None, 1),
 # S003
 ('S003', 'Chương trình', 'L', 'repetition', 'S002: chương trình Nhập cảnh Toàn cầu', 'high', None, None, 1),
 ('S003', 'người Úc', 'L', 'repetition', 'S002: Úc', 'med', None, 'morphological reiteration', 1),
 ('S003', 'Hoa Kỳ', 'L', 'repetition', 'S002: Hoa Kỳ', 'high', None, None, 1),
 # S004
 ('S004', 'Tuy nhiên', 'C', 'adversative', 'S003: limited availability', 'high', None, None, 1),
 ('S004', 'chương trình', 'L', 'repetition', 'S003: Chương trình', 'high', 'R: này', 'chương trình này', 1),
 # S005
 ('S005', 'chương trình Global Entry', 'L', 'repetition', 'S004: chương trình này', 'high', None, None, 1),
 ('S005', 'người Úc', 'L', 'repetition', 'S003: người Úc', 'med', None, None, 1),
 ('S005', 'Hoa Kỳ', 'L', 'repetition', 'S003: Hoa Kỳ', 'high', None, None, 1),
 # S006
 ('S006', 'người Úc', 'L', 'repetition', 'S005: người Úc', 'med', None, None, 1),
 # S007
 ('S007', 'hộ chiếu Úc', 'L', 'repetition', 'S006: người Úc', 'med', None, 'Úc morphological chain', 1),
 ('S007', 'ETA', 'L', 'repetition', 'S006: (Electronic Travel Authorisation - ETA)', 'high', None, 'abbreviation', 1),
 # S008
 ('S008', 'người Úc', 'L', 'repetition', 'S007: người mang hộ chiếu Úc', 'med', None, None, 1),
 ('S008', 'đơn xin', 'L', 'repetition', 'S007: đơn xin ETA', 'high', None, 'nộp đơn xin miễn thị thực', 1),
 # S009
 ('S009', 'ETIAS', 'L', 'repetition', 'S008: ETIAS', 'high', None, 'Quy trình ETIAS', 1),
 ('S009', 'du khách', 'L', 'repetition', 'S008: người Úc đi du lịch', 'med', None, 'morphological reiteration (du)', 1),
 # S010
 ('S010', 'Đây', 'R', 'demonstrative', 'S009: Quy trình ETIAS', 'high', None, None, 1),
 ('S010', 'quy trình', 'L', 'repetition', 'S009: Quy trình ETIAS', 'high', None, None, 1),
 ('S010', 'châu Âu', 'L', 'repetition', 'S008: châu Âu', 'high', None, None, 1),
 ('S010', 'khách du lịch', 'L', 'repetition', 'S009: du khách', 'med', None, 'word-order variant', 1),
 # S012
 ('S012', 'Hãng hàng không', 'L', 'general word', 'S011: Qantas', 'high', None, None, 1),
 # S013
 ('S013', 'Trong khi đó', 'C', 'additive', 'S012: Qantas route changes', 'high', None, None, 1),
 ('S013', 'cắt giảm', 'L', 'synonym', 'S012: ngừng bay', 'med', None, None, 1),
 # S014
 ('S014', 'cũng', 'C', 'additive', 'S012-S013: route cuts', 'med', None, None, 1),
 ('S014', 'cắt giảm', 'L', 'repetition', 'S013: cắt giảm', 'high', None, None, 1),
 # S015
 ('S015', 'Hãng hàng không', 'L', 'repetition', 'S012: Hãng hàng không', 'high', 'R: này', 'Hãng hàng không này', 1),
 ('S015', 'dịch vụ', 'L', 'repetition', 'S014: dịch vụ hàng ngày', 'high', None, None, 1),
 ('S015', 'từ Cairns đến Tokyo', 'L', 'repetition', 'S014: từ Cairns đến Tokyo', 'high', None, 'verbatim', 1),
 # S016
 ('S016', 'du khách', 'L', 'repetition', 'S009: du khách', 'med', None, None, 1),
 ('S016', 'Úc', 'L', 'repetition', 'S006: người Úc', 'med', None, 'morphological chain', 1),
 # S017
 ('S017', 'Úc', 'L', 'repetition', 'S016: Úc', 'med', None, None, 1),
 ('S017', 'năm 2025', 'L', 'repetition', 'S002: năm 2025', 'med', None, 'date echo', 1),
 # S018
 ('S018', 'Báo cáo', 'L', 'repetition', 'S017: báo cáo thường niên', 'high', None, None, 1),
 ('S018', 'giá vé máy bay', 'L', 'repetition', 'S017: giá vé máy bay', 'high', None, None, 1),
 ('S018', 'Úc', 'L', 'repetition', 'S017: Úc', 'med', None, None, 1),
 # S019
 ('S019', 'giá vé máy bay nội địa', 'L', 'repetition', 'S018: giá vé máy bay ... trong nước', 'high', None, 'nội địa ~ trong nước', 1),
 ('S019', 'tăng', 'L', 'repetition', 'S018: tăng 13,7%', 'high', None, None, 1),
 # S020
 ('S020', 'nội địa', 'L', 'repetition', 'S019: nội địa', 'high', None, 'Ngành hàng không nội địa', 1),
 ('S020', 'hàng không', 'L', 'repetition', 'S012: Hãng hàng không', 'med', None, 'partial reiteration', 1),
 ('S020', 'giá vé máy bay', 'L', 'repetition', 'S019: giá vé máy bay nội địa', 'high', None, None, 1),
 # S021
 ('S021', 'Tuy nhiên', 'C', 'adversative', 'S020: khó suy đoán', 'high', None, None, 1),
 ('S021', 'ACCC', 'L', 'repetition', 'S019: (ACCC)', 'high', None, 'abbreviation', 1),
 ('S021', 'giá vé máy bay', 'L', 'repetition', 'S020: giá vé máy bay', 'high', None, None, 1),
 ('S021', 'cạnh tranh', 'L', 'repetition', 'S019: sự cạnh tranh', 'high', None, 'đối thủ cạnh tranh', 1),
 # S022
 ('S022', 'hãng hàng không', 'L', 'repetition', 'S020: Ngành hàng không', 'med', None, None, 1),
 ('S022', 'giá vé', 'L', 'repetition', 'S021: giá vé máy bay', 'high', None, None, 1),
 ('S022', 'giảm', 'L', 'repetition', 'S019: cạnh tranh giảm', 'med', None, None, 1),
 # S023
 ('S023', 'yếu tố', 'L', 'repetition', 'S020: các yếu tố', 'high', None, None, 1),
 ('S023', 'hãng hàng không', 'L', 'repetition', 'S022: hãng hàng không', 'med', None, 'của hãng hàng không', 1),
 # S024
 ('S024', 'Tuy nhiên', 'C', 'adversative', 'S023: fuel as major cost', 'high', None, None, 1),
 ('S024', 'báo cáo', 'L', 'repetition', 'S018: Báo cáo', 'med', None, 'genre echo', 1),
 ('S024', 'chúng tôi', 'R', 'personal', 'S020: một phát ngôn viên của ACCC', 'med', None, 'institutional chúng tôi', 1),
 ('S024', 'giá nhiên liệu máy bay', 'L', 'repetition', 'S023: giá nhiên liệu máy bay', 'high', None, 'verbatim', 1),
]
