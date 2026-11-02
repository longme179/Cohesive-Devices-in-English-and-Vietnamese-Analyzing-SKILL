# P03 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)

ST = [
 # S003
 ('S003', 'hidden money', 'L', 'synonym', 'S001: "dark" donations', 'med', None, 'concealed-money paraphrase', None),
 ('S003', 'disclosed', 'L', 'repetition', 'S001: disclosure laws', 'high', None, 'morphological reiteration', None),
 # S004
 ('S004', 'donations', 'L', 'repetition', 'S001: donations', 'high', None, None, 1),
 ('S004', 'disclosed', 'L', 'repetition', 'S003: disclosed', 'high', None, None, 1),
 # S005
 ('S005', 'donations', 'L', 'repetition', 'S004: donations', 'high', None, None, 1),
 ('S005', 'Labor', 'L', 'repetition', 'S002: Labor', 'high', None, 'federal Labor', 1),
 # S006
 ('S006', 'Labor', 'L', 'repetition', 'S005: federal Labor', 'high', None, None, 1),
 ('S006', 'donated', 'L', 'repetition', 'S005: donations', 'high', None, 'morphological reiteration', 1),
 # S007
 ('S007', 'donated', 'L', 'repetition', 'S006: donated', 'high', None, None, 1),
 ('S007', 'billionaire', 'L', 'repetition', 'S005: billionaire Anthony Pratt', 'high', None, None, 1),
 # S008
 ('S008', 'also', 'C', 'additive', 'S007: Hancock donation', 'med', None, 'mid-sentence additive across boundary', 1),
 ('S008', 'donated', 'L', 'repetition', 'S007: donated', 'high', None, None, 1),
 ('S008', 'tens of thousands of dollars', 'L', 'repetition', 'S001: Tens of millions of dollars', 'med', None, 'partial phrase echo', 1),
 # S009
 ('S009', 'donated', 'L', 'repetition', 'S008: donated', 'high', None, None, 1),
 ('S009', 'wagering', 'L', 'repetition', 'S008: Wagering companies', 'med', None, 'inside company name and apposition', 1),
 # S010
 ('S010', "Sportbet's", 'L', 'repetition', 'S009: Sportsbet', 'high', None, 'source spelling variant Sportbet/Sportsbet', 1),
 ('S010', 'donation', 'L', 'repetition', 'S009: donated', 'high', None, 'morphological reiteration', 1),
 ('S010', 'Labor', 'L', 'repetition', 'S006: Labor', 'high', None, None, 1),
 ('S010', 'the government', 'L', 'repetition', 'S008: the government', 'high', None, None, 1),
 # S011
 ('S011', 'the government', 'L', 'repetition', 'S010: the government', 'high', None, None, 1),
 ('S011', 'rejected', 'L', 'repetition', 'S010: reject', 'high', None, 'morphological reiteration', 1),
 ('S011', 'recommendation', 'L', 'repetition', 'S010: a recommended blanket advertising ban', 'med', 'R: this', 'head reiterates; demonstrative to alt', 1),
 # S012
 ('S012', 'We', 'R', 'personal', 'S011: Prime Minister Anthony Albanese', 'med', None, 'institutional we of the government', 1),
 # S013
 ('S013', 'We', 'R', 'personal', 'S012: We', 'high', None, None, 1),
 ('S013', 'as well', 'C', 'additive', 'S012: introduced BetStop', 'med', None, None, 1),
 ('S013', 'gambling', 'L', 'repetition', 'S011: problem gambling', 'high', None, 'sport gambling', 1),
 ('S013', 'he', 'R', 'personal', 'S011: Prime Minister Anthony Albanese', 'high', None, None, 1),
 # S014
 ('S014', 'Sportsbet', 'L', 'repetition', 'S010: Sportbet\u2019s', 'high', None, None, 1),
 ('S014', 'also', 'C', 'additive', 'S008: also donated to Labor', 'med', None, None, 1),
 ('S014', 'donated', 'L', 'repetition', 'S009: donated', 'high', None, None, 1),
 ('S014', 'the Liberals', 'L', 'repetition', 'S007: the Liberals South Australia branch', 'high', None, None, 1),
 # S015
 ('S015', 'Tabcorp', 'L', 'repetition', 'S009: Tabcorp', 'high', None, None, 1),
 ('S015', 'donated tens of thousands of dollars', 'L', 'repetition', 'S008: donated tens of thousands of dollars', 'high', None, 'verbatim', 1),
 ('S015', "Labor's state divisions", 'L', 'repetition', 'S002: Labor and its state branches', 'med', None, 'partial NP echo', 1),
 ('S015', 'the Liberals and Nationals', 'L', 'repetition', 'S014: the Liberals and $15,000 to the Nationals', 'high', None, None, 1),
 ('S015', 'state branches', 'L', 'repetition', 'S002: state branches', 'high', None, 'verbatim', 1),
 # S016
 ('S016', 'Coalition', 'L', 'repetition', 'S002: the Coalition', 'high', None, 'a Coalition government', 1),
 ('S016', 'gambling', 'L', 'repetition', 'S013: sport gambling', 'high', None, 'gambling harm', 1),
 # S017
 ('S017', 'the Coalition', 'L', 'repetition', 'S016: a Coalition government', 'high', None, None, 1),
 ('S017', 'gambling', 'L', 'repetition', 'S016: gambling harm', 'high', None, 'gambling ads', 1),
 # S018
 ('S018', 'Labor and the Greens', 'L', 'repetition', 'S002: Labor ... and the Greens', 'high', None, None, 1),
 ('S018', 'the bill', 'L', 'repetition', 'S017: a bill', 'high', 'R: the', None, 1),
 ('S018', 'she', 'R', 'personal', 'S016: Melissa McIntosh', 'high', None, None, 1),
 # S019
 ('S019', 'Opposition Leader', 'L', 'repetition', 'S016: Opposition leader Peter Dutton', 'high', None, None, 1),
 ('S019', 'the prime minister', 'L', 'repetition', 'S011: Prime Minister Anthony Albanese', 'high', None, 'case variant', 1),
 ('S019', 'gambling advertising', 'L', 'repetition', 'S017: gambling ads', 'high', None, None, 1),
 ('S019', 'Labor', 'L', 'repetition', 'S018: Labor', 'high', None, 'Labor-led', 1),
 ('S019', 'it', 'R', 'personal', 'S017: a bill to stop gambling ads', 'med', None, 'calling for it', 2),
 # S020
 ('S020', 'McIntosh', 'L', 'repetition', 'S018: she (S016 McIntosh)', 'high', None, 'subject reintroduction', 1),
 ('S020', 'gambling industry donations', 'L', 'repetition', 'S008: Wagering companies also donated', 'med', None, 'synonym gambling=wagering + donations', 1),
 # S021
 ('S021', 'the Labor party', 'L', 'repetition', 'S019: Labor-led', 'high', None, None, 1),
 ('S021', 'SBS News', 'L', 'repetition', 'S020: SBS News\u2019 inquiry', 'high', None, None, 1),
 ('S021', 'comment', 'L', 'repetition', 'S016: a request for comment', 'high', None, None, 1),
 # S022
 ('S022', 'Greens', 'L', 'repetition', 'S018: the Greens', 'high', None, 'Greens senator', 1),
 ('S022', 'major parties', 'L', 'repetition', 'S001: political parties', 'med', None, 'general word with modifier', 1),
 ('S022', 'disclosures', 'L', 'synonym', 'S002: Australian Electoral Commission data released', 'low', None, 'today\u2019s disclosures ~ the data release; alt: morphological of S001 disclosure laws', 1),
 # S023
 ('S023', 'The Labor government', 'L', 'repetition', 'S011: his government (Albanese)', 'high', None, None, 1),
 ('S023', 'the Liberals', 'L', 'repetition', 'S014: the Liberals', 'high', None, None, 1),
 ('S023', 'donations', 'L', 'repetition', 'S008: donated tens of thousands of dollars', 'med', 'R: these', 'head reiterates via morphology; demonstrative to alt', 1),
 ('S023', 'gambling companies', 'L', 'repetition', 'S008: Wagering companies', 'med', None, 'synonym gambling=wagering', 1),
 ('S023', 'Greens', 'L', 'repetition', 'S022: Greens senator', 'high', None, 'the Greens democracy spokesperson', 1),
 # S024
 ('S024', 'However', 'C', 'adversative', 'S022-S023: criticism of major parties', 'high', None, None, 1),
 ('S024', "the Greens'", 'L', 'repetition', 'S023: the Greens democracy spokesperson', 'high', None, None, 1),
 ('S024', 'gambler', 'L', 'repetition', 'S023: gambling companies', 'med', None, 'morphological reiteration, person vs company', 1),
 ('S024', 'donated', 'L', 'repetition', 'S023: donations', 'high', None, None, 1),
 # S025
 ('S025', 'Turpie', 'L', 'repetition', 'S024: Duncan Turpie', 'high', None, None, 1),
 ('S025', 'donated', 'L', 'repetition', 'S024: donated', 'high', None, None, 1),
 ('S025', 'the party', 'L', 'repetition', 'S024: the party (the Greens)', 'high', None, None, 1),
 # S026
 ('S026', 'SBS News', 'L', 'repetition', 'S021: SBS News', 'high', None, None, 1),
 ('S026', 'donation', 'L', 'repetition', 'S024-S025: donated', 'high', 'R: this', 'head reiterates; demonstrative to alt', 1),
 ('S026', 'Waters', 'L', 'repetition', 'S022: Larissa Waters', 'high', None, None, 1),
 ('S026', 'Donations', 'L', 'repetition', 'S025: donated', 'high', None, 'quote-initial', 1),
 ('S026', 'gambling companies', 'L', 'repetition', 'S023: the gambling companies', 'high', None, None, 1),
 ('S026', "the Greens' position", 'L', 'repetition', 'S024: the Greens', 'high', None, None, 1),
 ('S026', 'gambling', 'L', 'repetition', 'S023: gambling companies', 'high', None, 'on gambling', 2),
 ('S026', 'the major parties', 'L', 'repetition', 'S022: the major parties', 'high', None, None, 1),
 # S027
 ('S027', 'Electoral donations reform', 'L', 'repetition', 'S001: calls for electoral reform', 'med', None, 'expanded compound echo', 1),
 ('S027', 'federal election', 'L', 'repetition', 'S001: electoral reform', 'med', None, 'morphological reiteration (electoral~election)', 1),
 # S028
 ('S028', 'The government', 'L', 'repetition', 'S023: The Labor government', 'high', None, None, 1),
 ('S028', 'Opposition', 'L', 'repetition', 'S019: Opposition Leader', 'high', None, None, 1),
 ('S028', 'donations', 'L', 'repetition', 'S027: Electoral donations reform', 'high', None, 'donations and expenditure caps', 1),
 # S029
 ('S029', 'the proposed changes', 'L', 'general word', 'S027: reform is back on the agenda', 'med', None, 'general word for the reform package', 1),
 ('S029', 'donation disclosure', 'L', 'repetition', 'S004: donations ... need to be disclosed', 'high', None, 'compound of both chain items', 1),
 # S030
 ('S030', 'election campaign', 'L', 'repetition', 'S027: a federal election', 'high', None, 'morphological reiteration', 1),
 ('S030', 'donations', 'L', 'repetition', 'S029: donation disclosure threshold', 'high', None, None, 1),
 # S031
 ('S031', 'also', 'C', 'additive', 'S030: candidate spending caps', 'med', None, None, 1),
 ('S031', 'cap', 'L', 'synonym', 'S030: limited to spending', 'med', None, 'cap = limit', 1),
 ('S031', 'spending', 'L', 'repetition', 'S030: spending', 'high', None, 'federal spending', 1),
 ('S031', 'unions', 'L', 'repetition', 'S006: Unions', 'high', None, None, 1),
 ('S031', 'political parties', 'L', 'repetition', 'S001: political parties', 'high', None, 'registered political parties', 2),
 # S032
 ('S032', 'the proposed legislation', 'L', 'repetition', 'S029: the proposed changes', 'high', None, 'legislation ~ changes', 1),
 ('S032', 'the Senate', 'L', 'repetition', 'S017: the Senate', 'high', None, None, 1),
 ('S032', 'political parties', 'L', 'repetition', 'S031: registered political parties', 'high', None, None, 1),
 ('S032', 'also', 'C', 'additive', 'S031: caps for parties and groups', 'med', None, None, 1),
 ('S032', 'the AEC', 'L', 'repetition', 'S002: Australian Electoral Commission', 'high', None, 'abbreviation', 1),
 # S033
 ('S033', 'But', 'C', 'adversative', 'S032: parties get more cash', 'high', None, None, 1),
 ('S033', 'the proposal', 'L', 'repetition', 'S029: the proposed changes', 'high', None, None, 1),
 ('S033', 'major party', 'L', 'repetition', 'S022: the major parties', 'high', None, 'a major party stitch-up', 1),
 ('S033', 'Labor and Liberal', 'L', 'repetition', 'S018: Labor + S014: the Liberals', 'high', None, None, 1),
 ('S033', 'the electoral commission', 'L', 'repetition', 'S032: the AEC', 'high', None, 'expansion of abbreviation', 1),
 # S034
 ('S034', 'The caps', 'L', 'repetition', 'S031: a cap', 'high', None, None, 1),
 ('S034', 'also', 'C', 'additive', 'S033: stitch-up claim', 'med', None, None, 1),
 ('S034', 'independents', 'L', 'repetition', 'S033: independents', 'high', None, None, 1),
 ('S034', 'major parties', 'L', 'repetition', 'S033: major party', 'high', None, None, 1),
 ('S034', 'tens of millions of dollars', 'L', 'repetition', 'S001: Tens of millions of dollars', 'high', None, 'verbatim', 1),
 ('S034', 'advertising', 'L', 'repetition', 'S019: gambling advertising', 'high', None, None, 1),
 # S035
 ('S035', 'independents', 'L', 'repetition', 'S034: independents', 'high', None, 'teal independents', 1),
 # S036
 ('S036', 'It', 'R', 'personal', 'S035: Climate200', 'high', None, None, 1),
 ('S036', 'donated', 'L', 'repetition', 'S026: Donations', 'high', None, None, 1),
 # S037
 ('S037', 'Daniel', 'L', 'repetition', 'S036: Zoe Daniel', 'high', None, None, 1),
 ('S037', 'donations', 'L', 'repetition', 'S036: donated', 'high', None, None, 1),
 ('S037', 'Spender', 'L', 'repetition', 'S036: Allegra Spender', 'high', None, None, 1),
 ('S037', 'Chaney', 'L', 'repetition', 'S036: Kate Chaney', 'high', None, None, 1),
 ('S037', 'Steggall', 'L', 'repetition', 'S036: Zali Steggall', 'high', None, None, 1),
 ('S037', 'Ryan', 'L', 'repetition', 'S036: Monique Ryan', 'high', None, None, 1),
]

TT = [
 # S002
 ('S002', 'tài trợ', 'L', 'synonym', 'S001: quyên góp', 'med', None, 'thế đồng nghĩa (donate ~ sponsor/fund)', 1),
 ('S002', 'các đảng liên bang', 'L', 'repetition', 'S001: các đảng chính trị lớn', 'med', None, 'đảng chain, different modifier', 1),
 # S003
 ('S003', 'nhà tài trợ', 'L', 'repetition', 'S002: tài trợ', 'high', None, 'morphological reiteration', 1),
 ('S003', 'quyên góp', 'L', 'repetition', 'S001: cải cách quyên góp bầu cử', 'high', None, None, 1),
 ('S003', 'Đảng Lao động Liên bang', 'L', 'repetition', 'S002: Đảng Lao động Liên bang', 'high', None, 'verbatim', 1),
 # S004
 ('S004', 'tập đoàn', 'L', 'repetition', 'S003: tập đoàn', 'high', None, None, 1),
 ('S004', 'tỷ phú', 'L', 'repetition', 'S003: tỷ phú Anthony Pratt', 'high', None, None, 1),
 ('S004', 'tài trợ', 'L', 'repetition', 'S002: tài trợ', 'high', None, None, 1),
 ('S004', 'Đảng Tự do', 'L', 'repetition', 'S002: Đảng Tự do Liên bang', 'high', None, 'partial (party name minus region)', 1),
 ('S004', 'quyên góp', 'L', 'repetition', 'S003: quyên góp', 'high', 'R: này', 'các khoản quyên góp này; demonstrative intra-sentential (points to same-sentence list)', 1),
 ('S004', 'áp lực', 'L', 'repetition', 'S001: áp lực', 'high', None, 'verbatim', 1),
 ('S004', 'cải cách', 'L', 'repetition', 'S001: cải cách', 'high', None, 'cải cách luật tài trợ chính trị', 1),
 # S005
 ('S005', 'quyên góp', 'L', 'repetition', 'S004: quyên góp', 'high', None, None, 1),
 ('S005', 'hàng chục nghìn đô la', 'L', 'repetition', 'S001: hàng chục triệu đô la', 'med', None, 'partial phrase echo (nghìn vs triệu)', 1),
 ('S005', 'Đảng Lao động', 'L', 'repetition', 'S003: Đảng Lao động Liên bang', 'high', None, None, 1),
 ('S005', 'chính phủ', 'L', 'repetition', 'S004: chính phủ', 'high', None, None, 1),
 ('S005', 'cải cách', 'L', 'repetition', 'S004: cải cách', 'high', None, 'cải cách luật cá cược thể thao', 1),
 # S006
 ('S006', 'báo cáo', 'L', 'repetition', 'S002: Theo báo cáo', 'high', None, 'Theo báo cáo tài chính', 1),
 ('S006', 'tài trợ', 'L', 'repetition', 'S004: tài trợ', 'high', None, 'các khoản tài trợ', 1),
 ('S006', 'cá cược', 'L', 'repetition', 'S005: cá cược', 'high', None, 'dịch vụ cá cược', 1),
 ('S006', 'quyên góp', 'L', 'repetition', 'S005: quyên góp', 'high', None, 'khoản quyên góp của Sportsbet', 1),
 ('S006', 'Đảng Lao động', 'L', 'repetition', 'S005: Đảng Lao động', 'high', None, None, 1),
 ('S006', 'chính phủ', 'L', 'repetition', 'S005: chính phủ', 'high', None, None, 1),
 # S007
 ('S007', 'cấm hoàn toàn quảng cáo cá cược', 'L', 'repetition', 'S006: lệnh cấm quảng cáo cá cược toàn diện', 'high', None, 'cấm + quảng cáo + cá cược', 1),
 ('S007', 'chính phủ', 'L', 'repetition', 'S006: chính phủ', 'high', None, 'chính phủ của ông', 1),
 # S008
 ('S008', 'Chúng tôi', 'R', 'personal', 'S007: Thủ tướng Anthony Albanese', 'med', None, 'institutional chúng tôi', 1),
 ('S008', 'cờ bạc', 'L', 'repetition', 'S007: vấn đề cờ bạc', 'high', None, None, 1),
 # S009
 ('S009', 'Chúng tôi', 'R', 'personal', 'S008: Chúng tôi', 'high', None, None, 1),
 ('S009', 'cũng', 'C', 'additive', 'S008: triển khai BetStop', 'med', None, None, 1),
 ('S009', 'cá cược', 'L', 'repetition', 'S006: cá cược', 'high', None, 'các hoạt động cá cược', 1),
 ('S009', 'cờ bạc', 'L', 'repetition', 'S008: cờ bạc', 'high', None, 'cờ bạc thể thao', 1),
 ('S009', 'ông', 'R', 'personal', 'S007: Thủ tướng Anthony Albanese', 'high', None, None, 1),
 # S010
 ('S010', 'chính phủ', 'L', 'repetition', 'S007: chính phủ', 'high', None, 'Dù chính phủ tuyên bố', 1),
 ('S010', 'cờ bạc', 'L', 'repetition', 'S009: cờ bạc', 'high', None, 'tác hại của cờ bạc', 1),
 ('S010', 'lệnh cấm quảng cáo toàn diện', 'L', 'repetition', 'S006: lệnh cấm quảng cáo cá cược toàn diện', 'high', None, 'partial echo', 1),
 ('S010', 'quyên góp', 'L', 'repetition', 'S006: quyên góp', 'high', None, 'các khoản quyên góp đáng kể', 1),
 ('S010', 'công ty cá cược', 'L', 'repetition', 'S005: Các công ty cá cược', 'high', None, None, 1),
 ('S010', 'đảng cầm quyền', 'L', 'synonym', 'S005: Đảng Lao động', 'med', None, 'the governing party', 1),
 # S011
 ('S011', 'Đảng Lao động', 'L', 'repetition', 'S006: Đảng Lao động', 'high', None, None, 1),
 ('S011', 'Bên cạnh', 'C', 'additive', 'S010: donations to Labor', 'med', None, None, 1),
 ('S011', 'cũng', 'C', 'additive', 'S010: các công ty cá cược quyên góp', 'med', None, None, 1),
 ('S011', 'tài trợ', 'L', 'repetition', 'S006: tài trợ', 'high', None, 'Sportsbet đã tài trợ', 2),
 ('S011', 'công ty cá cược', 'L', 'repetition', 'S010: công ty cá cược', 'high', None, None, 1),
 ('S011', 'Sportsbet', 'L', 'repetition', 'S006: Sportsbet', 'high', None, None, 1),
 ('S011', 'Đảng Tự do', 'L', 'repetition', 'S004: Đảng Tự do', 'high', None, None, 1),
 ('S011', 'Đảng Quốc gia', 'L', 'repetition', 'S002: Đảng Quốc gia Liên bang', 'high', None, None, 1),
 # S012
 ('S012', 'Tabcorp', 'L', 'repetition', 'S006: Tabcorp', 'high', None, None, 1),
 ('S012', 'cũng', 'C', 'additive', 'S011: Sportsbet donations', 'med', None, None, 1),
 ('S012', 'đóng góp', 'L', 'synonym', 'S006: tài trợ', 'med', None, 'phép liên tưởng/đồng nghĩa (contribute money)', 1),
 ('S012', 'Đảng Lao động', 'L', 'repetition', 'S011: Đảng Lao động', 'high', None, 'chi nhánh tiểu bang của Đảng Lao động', 1),
 ('S012', 'hàng chục nghìn đô la', 'L', 'repetition', 'S005: hàng chục nghìn đô la', 'high', None, 'verbatim', 1),
 ('S012', 'Đảng Tự do và Đảng Quốc gia', 'L', 'repetition', 'S011: Đảng Tự do ... Đảng Quốc gia', 'high', None, None, 1),
 ('S012', 'chi nhánh', 'L', 'repetition', 'S002: các chi nhánh tiểu bang', 'high', None, 'các chi nhánh liên quan', 1),
 # S013
 ('S013', 'Đảng Xanh', 'L', 'repetition', 'S002: Đảng Xanh Liên bang', 'high', None, None, 1),
 ('S013', 'tài trợ', 'L', 'repetition', 'S011: tài trợ', 'high', None, 'các khoản tài trợ từ', 1),
 ('S013', 'cá cược', 'L', 'repetition', 'S011: công ty cá cược', 'high', None, 'ngành công nghiệp cá cược', 1),
 ('S013', 'đảng lớn', 'L', 'repetition', 'S001: các đảng chính trị lớn', 'high', None, 'hai đảng lớn', 1),
 # S014
 ('S014', 'các công ty cờ bạc', 'L', 'repetition', 'S010: công ty cá cược', 'med', None, 'mixed chain cá cược/cờ bạc', 1),
 ('S014', 'tài trợ', 'L', 'repetition', 'S013: tài trợ', 'high', None, 'tiếp tục tài trợ', 1),
 ('S014', 'Đảng Lao động và Đảng Tự do', 'L', 'repetition', 'S011-S012: Đảng Lao động ... Đảng Tự do', 'high', None, None, 1),
 ('S014', 'quảng cáo cờ bạc', 'L', 'repetition', 'S006: quảng cáo cá cược', 'med', None, 'mixed chain cá cược/cờ bạc', 1),
 ('S014', 'bà', 'R', 'personal', 'S013: Larissa Waters', 'high', None, None, 1),
 # S015
 ('S015', 'Tuy nhiên', 'C', 'adversative', 'S014: Greens attack gambling money', 'high', None, None, 1),
 ('S015', 'các đảng lớn', 'L', 'repetition', 'S013: hai đảng lớn', 'high', None, None, 1),
 ('S015', 'quyên góp', 'L', 'repetition', 'S010: quyên góp', 'high', None, 'các khoản quyên góp liên quan đến cờ bạc', 1),
 ('S015', 'cờ bạc', 'L', 'repetition', 'S014: cờ bạc', 'high', None, None, 1),
 # S016
 ('S016', 'cờ bạc', 'L', 'repetition', 'S015: cờ bạc', 'high', None, 'một tay chơi cờ bạc chuyên nghiệp', 1),
 ('S016', 'tài trợ', 'L', 'repetition', 'S014: tài trợ', 'high', None, 'đã tài trợ khoảng', 1),
 ('S016', 'Đảng Xanh', 'L', 'repetition', 'S013: Đảng Xanh', 'high', None, 'Đảng Xanh Úc', 1),
 ('S016', 'các chi nhánh', 'L', 'repetition', 'S012: chi nhánh', 'high', None, None, 1),
 # S017
 ('S017', 'Turpie', 'L', 'repetition', 'S016: Duncan Turpie', 'high', None, None, 1),
 ('S017', 'đóng góp', 'L', 'repetition', 'S012: đóng góp', 'high', None, 'đã đóng góp tổng cộng', 1),
 ('S017', 'Đảng Xanh', 'L', 'repetition', 'S016: Đảng Xanh', 'high', None, None, 1),
 # S018
 ('S018', 'tài trợ', 'L', 'repetition', 'S016: tài trợ', 'high', None, 'việc nhận tài trợ', 1),
 ('S018', 'tay chơi bài chuyên nghiệp', 'L', 'synonym', 'S016: tay chơi cờ bạc chuyên nghiệp', 'high', None, 'partial verbatim (bài vs cờ bạc)', 1),
 ('S018', 'máy đánh bạc', 'L', 'repetition', 'S014: máy đánh bạc', 'high', None, None, 1),
 # S019
 ('S019', 'Ông', 'R', 'personal', 'S018: Jonathan Sriranganathan', 'high', None, None, 1),
 ('S019', 'Đảng Xanh', 'L', 'repetition', 'S017: Đảng Xanh', 'high', None, 'lập trường của Đảng Xanh', 1),
 ('S019', 'máy đánh bạc', 'L', 'repetition', 'S018: máy đánh bạc', 'high', None, None, 1),
 ('S019', 'quyên góp', 'L', 'repetition', 'S015: quyên góp', 'high', None, 'các khoản quyên góp', 1),
 # S020
 ('S020', 'cải cách quyên góp bầu cử', 'L', 'repetition', 'S001: cải cách quyên góp bầu cử', 'high', None, 'verbatim echo of the lede', 1),
 ('S020', 'tổng tuyển cử liên bang', 'L', 'repetition', 'S001: tổng tuyển cử liên bang', 'high', None, 'verbatim', 1),
 # S021
 ('S021', 'Tuy nhiên', 'C', 'adversative', 'S020: reform back on agenda', 'high', None, None, 1),
 ('S021', 'chính phủ', 'L', 'repetition', 'S010: chính phủ', 'high', None, None, 1),
 ('S021', 'giới hạn', 'L', 'repetition', 'S006: các giới hạn nhất định', 'high', None, 'giới hạn quyên góp', 1),
 ('S021', 'quyên góp', 'L', 'repetition', 'S020: quyên góp', 'high', None, None, 1),
 ('S021', 'bầu cử', 'L', 'repetition', 'S020: tổng tuyển cử', 'high', None, 'morphological reiteration (cử)', 1),
 # S022
 ('S022', 'thay đổi', 'L', 'synonym', 'S020: cải cách', 'med', None, 'change ~ reform', 1),
 ('S022', 'công bố', 'L', 'repetition', 'S004: Việc công bố', 'high', None, 'Hạ ngưỡng công bố', 1),
 ('S022', 'quyên góp', 'L', 'repetition', 'S021: quyên góp', 'high', None, None, 1),
 ('S022', 'tài trợ', 'L', 'repetition', 'S011: tài trợ', 'high', None, 'nguồn tiền tài trợ', 1),
 # S023
 ('S023', 'Giới hạn', 'L', 'repetition', 'S021: giới hạn', 'high', None, 'Giới hạn chi tiêu', 1),
 ('S023', 'chiến dịch tranh cử', 'L', 'repetition', 'S020: tổng tuyển cử', 'med', None, 'morphological reiteration (cử)', 1),
 # S024
 ('S024', 'Giới hạn', 'L', 'repetition', 'S023: Giới hạn', 'high', None, None, 1),
 ('S024', 'quyên góp', 'L', 'repetition', 'S022: quyên góp', 'high', None, 'quyên góp tối đa', 1),
 # S025
 ('S025', 'này', 'R', 'demonstrative', 'S022-S024: Những thay đổi được đề xuất / Giới hạn', 'high', None, 'Những đề xuất này', 1),
 ('S025', 'đề xuất', 'L', 'repetition', 'S022: được đề xuất', 'high', None, None, 1),
 ('S025', 'minh bạch', 'L', 'repetition', 'S022: minh bạch hơn', 'high', None, 'tính minh bạch', 1),
 ('S025', 'các đảng phái', 'L', 'repetition', 'S011: các đảng phái khác', 'high', None, None, 1),
 ('S025', 'bầu cử', 'L', 'repetition', 'S021: bầu cử', 'high', None, 'bầu cử sắp tới', 1),
 # S026
 ('S026', 'Dự luật', 'L', 'repetition', 'S005: bất kỳ dự luật nào', 'med', None, 'indefinite earlier mention, definite now', 1),
 ('S026', 'cải cách quyên góp bầu cử', 'L', 'repetition', 'S020: cải cách quyên góp bầu cử', 'high', None, 'verbatim', 1),
 ('S026', 'cũng', 'C', 'additive', 'S025: proposals debated', 'med', None, None, 1),
 ('S026', 'giới hạn chi tiêu', 'L', 'repetition', 'S023: Giới hạn chi tiêu', 'high', None, 'giới hạn chi tiêu liên bang', 1),
 # S027
 ('S027', 'các đảng chính trị', 'L', 'repetition', 'S001: các đảng chính trị lớn', 'high', None, None, 1),
 ('S027', 'chiến dịch bầu cử', 'L', 'repetition', 'S023: chiến dịch tranh cử', 'high', None, None, 1),
 # S028
 ('S028', 'Ngoài ra', 'C', 'additive', 'S027: spending caps', 'high', None, None, 1),
 ('S028', 'các đảng chính trị', 'L', 'repetition', 'S027: các đảng chính trị', 'high', None, None, 1),
 ('S028', 'Ủy ban Bầu cử Úc', 'L', 'repetition', 'S002: Ủy ban Bầu cử Úc (AEC)', 'high', None, 'verbatim', 1),
 # S029
 ('S029', 'này', 'R', 'demonstrative', 'S026-S028: dự luật / giới hạn chi tiêu', 'high', None, 'đề xuất này', 1),
 ('S029', 'các đảng lớn', 'L', 'repetition', 'S015: các đảng lớn', 'high', None, None, 1),
 ('S029', 'tài trợ', 'L', 'repetition', 'S014: tài trợ', 'high', None, 'để tài trợ cho chiến dịch', 1),
 ('S029', 'chiến dịch tranh cử', 'L', 'repetition', 'S027: chiến dịch bầu cử', 'high', None, None, 1),
 # S030
 ('S030', 'Các đảng lớn', 'L', 'repetition', 'S029: các đảng lớn', 'high', None, None, 1),
 ('S030', 'hưởng lợi', 'L', 'repetition', 'S015: hưởng lợi', 'high', None, None, 1),
 ('S030', 'ngân sách công', 'L', 'synonym', 'S029: ngân sách nhà nước', 'high', None, 'shared ngân sách', 1),
 ('S030', 'AEC', 'L', 'repetition', 'S028: Ủy ban Bầu cử Úc (AEC)', 'high', None, 'abbreviation', 1),
 # S031
 ('S031', 'Các ứng viên độc lập', 'L', 'repetition', 'S029: Các ứng viên độc lập', 'high', None, None, 1),
 ('S031', 'giới hạn chi tiêu', 'L', 'repetition', 'S026: giới hạn chi tiêu', 'high', None, 'bị giới hạn chi tiêu', 1),
 ('S031', 'các đảng lớn', 'L', 'repetition', 'S030: các đảng lớn', 'high', None, None, 1),
 ('S031', 'hàng chục triệu đô la', 'L', 'repetition', 'S001: hàng chục triệu đô la', 'high', None, 'verbatim', 1),
 ('S031', 'quảng cáo', 'L', 'repetition', 'S006: quảng cáo cá cược', 'high', None, None, 1),
 ('S031', 'vận động tranh cử', 'L', 'repetition', 'S029: chiến dịch tranh cử', 'high', None, 'morphological reiteration (tranh cử)', 1),
 # S032
 ('S032', 'Dự luật cải cách tài trợ bầu cử', 'L', 'repetition', 'S026: Dự luật cải cách quyên góp bầu cử', 'high', None, 'near-verbatim', 1),
 # S033
 ('S033', 'Trong khi đó', 'C', 'adversative', 'S032: bill to Senate', 'med', None, 'meanwhile-contrast', 1),
 ('S033', 'Đảng Lao động và Đảng Tự do', 'L', 'repetition', 'S014: Đảng Lao động và Đảng Tự do', 'high', None, None, 1),
]
