# P01 tie table. Row: (sent, text, cat, sub, ante, conf, alt, note, occ)
# cat: R reference, S substitution, E ellipsis, C conjunction, L lexical
# Occ None = auto (first occurrence). Pronouns repeated in one sentence get
# explicit occ 1..n.

ST = [
 # S004
 ('S004', 'city-state', 'L', 'synonym', 'S003: Singapore (small nation)', 'med', 'R: The', 'near-synonym re-description; "the" not marked per rule 3', None),
 ('S004', 'it', 'R', 'personal', 'S003: Singapore', 'high', None, None, 3),
 # S005
 ('S005', 'But', 'C', 'adversative', 'S003-S004: water problem vs leader', 'high', None, None, None),
 ('S005', 'also', 'C', 'additive', 'S004: few resources', 'med', None, 'mid-sentence but adds to previous sentence proposition', None),
 ('S005', 'country', 'L', 'superordinate', 'S003: Singapore / small nation', 'med', 'R: the', 'general-word NP', None),
 ('S005', 'recycled water', 'L', 'repetition', 'S002: recycled wastewater', 'high', None, 'partial repetition of compound', None),
 ('S005', 'sewage water', 'L', 'synonym', 'S002: wastewater', 'med', None, None, None),
 # S006
 ('S006', 'Purified recycled water', 'L', 'repetition', 'S005: purified recycled water', 'high', None, None, None),
 ('S006', 'wastewater', 'L', 'repetition', 'S002: recycled wastewater', 'high', None, None, None),
 ('S006', 'sewage', 'L', 'repetition', 'S005: sewage water', 'med', None, None, None),
 # S007
 ('S007', 'But', 'C', 'adversative', 'S006: discharge to environment', 'high', None, None, None),
 ('S007', 'we', 'R', 'personal', 'S006: Professor Stuart Khan / University of Sydney (institutional we)', 'med', None, 'institutional we of quoted speaker', None),
 ('S007', 'it', 'R', 'personal', 'S006: treated sewage / water', 'high', None, None, 1),
 ('S007', 'environment', 'L', 'repetition', 'S006: the environment', 'high', None, None, None),
 ('S007', 'it', 'R', 'personal', 'S006: treated sewage / water', 'high', None, None, 2),
 ('S007', 'water treatment plant', 'L', 'repetition', 'S006: wastewater treatment plants', 'med', None, 'head repetition + association', None),
 ('S007', 'it', 'R', 'personal', 'S006: treated sewage / water', 'high', None, None, 3),
 ('S007', 'it', 'R', 'personal', 'S006: treated sewage / water', 'high', None, None, 4),
 ('S007', 'drinking water', 'L', 'repetition', 'S005: drinking water', 'high', None, None, None),
 # S008
 ('S008', 'It', 'R', 'personal', 'S005-S007: the purified recycled water practice', 'high', None, 'summary anaphor', None),
 # S009
 ('S009', 'country', 'L', 'superordinate', 'S003: Singapore / small nation', 'med', 'R: the', 'general-word NP', None),
 ('S009', 'treated wastewater', 'L', 'repetition', 'S006: treated sewage / wastewater', 'high', None, None, None),
 # S010
 ('S010', 'Khan', 'L', 'repetition', 'S006: Professor Stuart Khan', 'high', None, 'proper name, subject reintroduction', None),
 ('S010', 'its', 'R', 'personal', 'S009: the country / Singapore', 'high', None, None, None),
 # S011
 ('S011', 'Singapore', 'L', 'repetition', 'S010: its (Singapore)', 'high', None, 'subject reintroduction', None),
 ('S011', 'community education', 'L', 'repetition', 'S010: education campaign', 'med', 'R: that', 'partial repetition; demonstrative "that" not marked because head reiterates', None),
 # S012
 ('S012', 'They', 'R', 'personal', 'S011: Singapore', 'high', None, None, None),
 ('S012', 'their', 'R', 'personal', 'S011: Singapore', 'high', None, None, None),
 ('S012', 'water recycling scheme', 'L', 'repetition', 'S005: purified recycled water', 'med', None, 'reiteration via "recycling"', None),
 ('S012', 'he', 'R', 'personal', 'S010: Khan', 'high', None, None, 4),
 # S013
 ('S013', 'They', 'R', 'personal', 'S012: They (Singapore)', 'high', None, None, None),
 ('S013', 'visitor centre', 'L', 'repetition', 'S012: a visitor centre', 'high', 'R: that', None, None),
 ('S013', 'water recycling', 'L', 'repetition', 'S012: water recycling scheme', 'high', None, None, None),
 # S014
 ('S014', 'Now', 'C', 'temporal', 'S011-S013: Singapore history; shift to Sydney present', 'med', None, 'temporal frame shift', None),
 ('S014', 'educate', 'L', 'repetition', 'S010: education campaign', 'med', None, 'morphological reiteration', None),
 ('S014', 'recycled wastewater', 'L', 'repetition', 'S006: wastewater', 'high', None, None, None),
 # S015
 ('S015', 'pressure', 'L', 'repetition', 'S001: growing pressure', 'high', None, None, None),
 ('S015', 'water supply in cities around the world', 'L', 'repetition', 'S001: the water supply in cities around the world', 'high', None, 'near-verbatim echo of the lede', None),
 # S016
 ('S016', 'Sydney', 'L', 'repetition', 'S014: Sydney', 'high', None, None, None),
 ('S016', 'supply', 'L', 'repetition', 'S015: water supply', 'med', None, None, None),
 # S017
 ('S017', 'Sydney', 'L', 'repetition', 'S016: Sydney', 'med', None, 'embedded in locative PP but continues topic chain', None),
 ('S017', 'dam', 'L', 'collocation', 'S004: reservoirs', 'low', None, 'same water-storage field; association', None),
 # S018
 ('S018', 'water supply', 'L', 'repetition', 'S015: water supply', 'high', None, None, None),
 ('S018', 'dams', 'L', 'repetition', 'S017: dam levels', 'high', None, None, None),
 ('S018', 'drought', 'L', 'repetition', 'S017: drought', 'high', None, None, None),
 # S019
 ('S019', 'Recycled purified water', 'L', 'repetition', 'S005: purified recycled water', 'high', None, 'word-order variant', None),
 ('S019', 'future', 'L', 'repetition', 'S018: the future of our water supply', 'med', None, None, None),
 # S020
 ('S020', 'process', 'L', 'general word', 'S019: recycled purified water solution', 'med', 'R: the', 'general-word NP', None),
 ('S020', 'sewage plant', 'L', 'repetition', 'S006: wastewater treatment plants', 'med', None, None, None),
 ('S020', 'public', 'L', 'repetition', 'S014: the public', 'high', None, None, None),
 # S021
 ('S021', 'Harrington', 'L', 'repetition', 'S018: James Harrington', 'high', None, 'subject reintroduction', None),
 ('S021', 'Purified Recycled Water', 'L', 'repetition', 'S019: recycled purified water', 'med', None, 'embedded in proper name of the centre', None),
 # S022
 ('S022', 'Firstly', 'C', 'additive', 'S021: three main objectives', 'high', None, 'enumerative additive', None),
 ('S022', 'our', 'R', 'personal', 'S018: Sydney Water (speaker institution)', 'med', None, 'institutional our', None),
 ('S022', 'technology', 'L', 'general word', 'S019-S020: recycled purified water process', 'med', 'R: the', 'general-word NP', None),
 # S023
 ('S023', 'Secondly', 'C', 'additive', 'S022: first objective', 'high', None, None, None),
 ('S023', 'technology', 'L', 'repetition', 'S022: the technology', 'high', None, None, None),
 # S024
 ('S024', 'And lastly', 'C', 'additive', 'S023: second objective', 'high', None, None, None),
 ('S024', 'our', 'R', 'personal', 'S018: Sydney Water', 'med', None, 'institutional our', None),
 ('S024', 'testing', 'L', 'repetition', 'S022: test the technology', 'med', None, 'morphological reiteration', None),
 ('S024', 'he', 'R', 'personal', 'S021: Harrington', 'high', None, None, 2),
 # S025
 ('S025', 'We', 'R', 'personal', 'S018: Sydney Water', 'med', None, 'institutional we', None),
 ('S025', 'public', 'L', 'repetition', 'S020: the public', 'high', None, None, None),
 ('S025', 'here', 'R', 'demonstrative', 'S021: Purified Recycled Water Discovery Centre', 'med', None, 'place deixis to centre', None),
 ('S025', 'technology', 'L', 'repetition', 'S023: the technology', 'high', None, None, None),
 ('S025', 'safe and reliable', 'L', 'repetition', 'S007: safely and reliably', 'med', None, 'adverb-adjective reiteration', None),
 # S026
 ('S026', 'Khan', 'L', 'repetition', 'S012: he (Khan)', 'high', None, 'subject reintroduction', None),
 ('S026', 'purified recycled water', 'L', 'repetition', 'S021: Purified Recycled Water', 'high', None, None, None),
 # S027
 ('S027', 'drought-stricken', 'L', 'repetition', 'S017: drought', 'med', None, 'morphological reiteration', None),
 ('S027', 'recycled sewage', 'L', 'repetition', 'S026: purified recycled water', 'high', None, 'reiteration of both parts', None),
 ('S027', 'drinking water', 'L', 'repetition', 'S007: drinking water supplies', 'high', None, None, None),
 # S028
 ('S028', 'Toowoomba', 'L', 'repetition', 'S027: Toowoomba', 'high', None, 'subject reintroduction', None),
 ('S028', 'public', 'L', 'repetition', 'S025: the public', 'med', None, None, None),
 ('S028', 'he', 'R', 'personal', 'S026: Khan', 'high', None, None, 3),
 # S029
 ('S029', 'other', 'R', 'comparative', 'S028: an example of one', 'high', None, 'comparative reference', None),
 ('S029', 'lack of support', 'L', 'repetition', 'S028: lack of public support', 'high', None, None, None),
 ('S029', 'project', 'L', 'repetition', 'S028: the project', 'high', None, None, None),
 # S030
 ('S030', 'projects', 'L', 'repetition', 'S029: a project', 'high', None, None, None),
 ('S030', 'public support', 'L', 'repetition', 'S028: public support', 'high', None, None, None),
 # S031
 ('S031', 'Harrington', 'L', 'repetition', 'S025: he (Harrington)', 'high', None, 'subject reintroduction', None),
 ('S031', 'purified recycled water', 'L', 'repetition', 'S026: purified recycled water', 'high', None, None, None),
 # S032
 ('S032', 'Harrington', 'L', 'repetition', 'S031: Harrington', 'high', None, 'source PDF repeats this sentence (pull quote duplicated in table)', None),
 ('S032', 'purified recycled water', 'L', 'repetition', 'S031: purified recycled water', 'high', None, None, None),
 # S033
 ('S033', 'purified recycled water', 'L', 'repetition', 'S032: purified recycled water', 'high', None, None, None),
 # S034
 ('S034', 'technology', 'L', 'repetition', 'S025: the technology', 'high', 'R: this', 'head reiterates; demonstrative to alt', None),
 # S035
 ('S035', 'cities', 'L', 'repetition', 'S034: 35 cities ... 60 more cities', 'high', None, None, None),
 ('S035', 'process', 'L', 'repetition', 'S020: the process', 'med', None, None, None),
 # S036
 ('S036', 'Sydney', 'L', 'repetition', 'S016: Sydney', 'med', None, 'contrastive comparison', None),
 ('S036', 'Western Australian capital', 'L', 'synonym', 'S035: Perth', 'high', None, 'appositive re-description', None),
 ('S036', 'dams', 'L', 'repetition', 'S018: our dams', 'med', None, None, None),
 ('S036', 'Khan', 'L', 'repetition', 'S026: Khan', 'high', None, 'reintroduces source', None),
 ('S036', 'depleting', 'L', 'repetition', 'S018: depleting', 'med', None, None, None),
 # S037
 ('S037', 'WA', 'L', 'repetition', 'S036: the Western Australian capital', 'high', None, 'abbreviation of prior NP', None),
 # S038
 ('S038', 'So', 'C', 'causal', 'S037: WA leading out of necessity', 'med', None, None, None),
 ('S038', 'Perth', 'L', 'repetition', 'S035: Perth', 'high', None, None, None),
 ('S038', 'climate change', 'L', 'repetition', 'S015: climate change', 'high', None, None, None),
 ('S038', 'he', 'R', 'personal', 'S036: Khan', 'high', None, None, 2),
 # S039
 ('S039', 'Perth', 'L', 'repetition', 'S038: Perth', 'high', None, None, None),
 ('S039', 'groundwater', 'L', 'repetition', 'S036: groundwater', 'high', None, None, None),
 # S040
 ('S040', 'It', 'R', 'personal', 'S039: a scheme', 'high', None, None, None),
 ('S040', 'wastewater treatment plant', 'L', 'repetition', 'S006: wastewater treatment plants', 'high', None, None, None),
 ('S040', 'advanced water treatment', 'L', 'repetition', 'S007: advanced water treatment plant', 'high', None, None, None),
 # S041
 ('S041', 'And', 'C', 'additive', 'S040: water put into aquifers', 'med', None, 'sentence-initial additive', None),
 ('S041', 'aquifers', 'L', 'repetition', 'S040: the important aquifers', 'high', 'R: those', 'head reiterates; demonstrative to alt', None),
 ('S041', 'purified recycled water', 'L', 'repetition', 'S033: purified recycled water schemes', 'high', None, None, None),
 ('S041', 'their', 'R', 'personal', 'S038: people in Perth', 'med', None, None, None),
 ('S041', 'drinking water', 'L', 'repetition', 'S027: drinking water', 'high', None, None, None),
 # S042
 ('S042', 'WA', 'L', 'repetition', 'S037: WA', 'high', None, None, None),
 ('S042', 'treated wastewater', 'L', 'repetition', 'S009: treated wastewater', 'high', None, None, None),
 # S043
 ('S043', 'Queensland', 'L', 'repetition', 'S027: the regional Queensland city', 'high', None, None, None),
 ('S043', 'Recycled Water', 'L', 'repetition', 'S033: purified recycled water', 'med', None, 'embedded in proper name', None),
 ('S043', 'drought', 'L', 'repetition', 'S027: drought-stricken', 'high', None, None, None),
 # S044
 ('S044', 'It', 'R', 'personal', 'S043: the Western Corridor Recycled Water Scheme', 'high', None, None, None),
 ('S044', 'Khan', 'L', 'repetition', 'S036: Khan', 'high', None, None, None),
 # S045
 ('S045', 'So', 'C', 'causal', 'S044: floods stopped the scheme', 'high', None, None, None),
 ('S045', 'it', 'R', 'personal', 'S044: It (the scheme)', 'high', None, None, 1),
 ('S045', 'it', 'R', 'personal', 'S044: It (the scheme)', 'high', None, None, 2),
 ('S045', 'Brisbane', 'L', 'repetition', 'S044: the Brisbane area', 'med', None, None, None),
 ('S045', 'Queensland', 'L', 'repetition', 'S043: Queensland', 'med', None, None, None),
 ('S045', 'future', 'L', 'repetition', 'S018: the future of our water supply', 'med', None, None, None),
 ('S045', 'water supply', 'L', 'repetition', 'S018: water supply', 'med', None, None, None),
 # S046
 ('S046', 'Khan', 'L', 'repetition', 'S044: Khan', 'high', None, None, None),
 ('S046', 'it', 'R', 'personal', 'S045: it (the scheme)', 'high', None, None, 1),
 ('S046', 'drinking water', 'L', 'repetition', 'S041: drinking water supply', 'high', None, None, None),
 ('S046', 'it', 'R', 'personal', 'S045: it (the scheme)', 'high', None, None, 2),
 # S047
 ('S047', 'That', 'R', 'demonstrative', 'S046: 80 gigalitres a year', 'high', None, 'pronominal demonstrative', None),
 ('S047', 'Queensland', 'L', 'repetition', 'S045: south-east Queensland', 'med', None, None, None),
 # S048
 ('S048', 'their', 'R', 'personal', 'S047: south-east Queensland 3.8 million residents', 'med', None, None, 1),
 ('S048', 'water supply strategy', 'L', 'repetition', 'S045: future water supply strategy', 'high', None, None, None),
 ('S048', 'their', 'R', 'personal', 'S047: south-east Queensland residents', 'med', None, None, 2),
 ('S048', 'dams', 'L', 'repetition', 'S018: our dams', 'med', None, None, None),
 # S049
 ('S049', 'purified recycled water scheme', 'L', 'repetition', 'S043: Western Corridor Recycled Water Scheme', 'med', 'R: that', 'head reiterates; demonstrative to alt', None),
 ('S049', 'Brisbane', 'L', 'repetition', 'S048: Brisbane', 'med', None, None, 1),
 ('S049', 'storage', 'L', 'repetition', 'S048: storages', 'med', None, None, None),
 ('S049', 'drinking water', 'L', 'repetition', 'S046: drinking water', 'high', None, None, 1),
]

TT = [
 # S004
 ('S004', 'đảo quốc', 'L', 'synonym', 'S003: Singapore', 'high', 'R: này', 'thế đồng nghĩa; "này" not marked because head reiterates (per rule 3 analog)', None),
 ('S004', 'thiếu nước', 'L', 'repetition', 'S003: vấn đề thiếu nước', 'high', None, None, None),
 # S005
 ('S005', 'Tuy nhiên', 'C', 'adversative', 'S003-S004: thiếu nước vs đi đầu', 'high', None, None, None),
 ('S005', 'Singapore', 'L', 'repetition', 'S004: đảo quốc này', 'high', None, 'subject reintroduction', None),
 ('S005', 'cũng', 'C', 'additive', 'S003: vấn đề thiếu nước', 'med', None, 'mid-sentence additive across boundary', None),
 ('S005', 'tái chế nước thải', 'L', 'repetition', 'S002: tái chế nước thải', 'high', None, None, None),
 ('S005', 'nước uống', 'L', 'repetition', 'S002: nước uống', 'high', None, None, None),
 # S006
 ('S006', 'Tái chế nước thải', 'L', 'repetition', 'S005: tái chế nước thải', 'high', None, None, None),
 ('S006', 'xử lý', 'L', 'repetition', 'S005: công nghệ xử lý', 'high', None, None, 1),
 # S007
 ('S007', 'Nhưng', 'C', 'adversative', 'S006: thải ra môi trường', 'high', None, None, None),
 ('S007', 'chúng tôi', 'R', 'personal', 'S006: Giáo sư Stuart Khan (institutional chúng tôi)', 'med', None, 'institutional chúng tôi of quoted speaker', None),
 ('S007', 'môi trường', 'L', 'repetition', 'S006: môi trường', 'high', None, None, None),
 ('S007', 'nhà máy xử lý nước', 'L', 'repetition', 'S006: nhà máy xử lý nước thải', 'med', None, 'partial repetition of compound', None),
 ('S007', 'nước uống', 'L', 'repetition', 'S005: nước uống', 'high', None, None, None),
 # S008
 ('S008', 'Singapore', 'L', 'repetition', 'S005: Singapore', 'high', None, None, None),
 ('S008', 'này', 'R', 'demonstrative', 'S005-S007: quá trình tái chế nước', 'high', None, 'hệ thống = general word for the process; demonstrative marked', None),
 # S009
 ('S009', 'Họ', 'R', 'personal', 'S008: Người dân Singapore', 'high', None, None, None),
 ('S009', 'nước thải đã qua xử lý', 'L', 'repetition', 'S006: nước thải ... đã qua xử lý', 'high', None, 'near-verbatim reiteration', None),
 # S010
 ('S010', 'Khan', 'L', 'repetition', 'S006: Giáo sư Stuart Khan', 'high', None, None, None),
 ('S010', 'Singapore', 'L', 'repetition', 'S008: Singapore', 'high', None, None, None),
 # S011
 ('S011', 'Singapore', 'L', 'repetition', 'S010: Singapore', 'high', None, None, None),
 ('S011', 'giáo dục cộng đồng', 'L', 'repetition', 'S010: chiến dịch giáo dục cộng đồng', 'high', None, None, None),
 # S012
 ('S012', 'Họ', 'R', 'personal', 'S011: Singapore', 'high', None, None, None),
 ('S012', 'ông', 'R', 'personal', 'S010: Giáo sư Khan', 'high', None, 'kinship term as pronoun', None),
 # S013
 ('S013', 'Họ', 'R', 'personal', 'S012: Họ', 'high', None, None, None),
 ('S013', 'này', 'R', 'demonstrative', 'S012: một trung tâm giới thiệu', 'high', None, 'nơi = general word (place)', None),
 ('S013', 'tái chế nước', 'L', 'repetition', 'S005: tái chế nước thải', 'high', None, None, None),
 # S014
 ('S014', 'cũng', 'C', 'additive', 'S010-S013: Singapore education efforts', 'med', None, 'Sydney cũng = additive across boundary', None),
 ('S014', 'nước thải tái chế', 'L', 'repetition', 'S013: tái chế nước', 'high', None, None, None),
 # S015
 ('S015', 'nguồn cung cấp nước', 'L', 'repetition', 'S001: Nguồn nước', 'med', None, None, None),
 ('S015', 'thành phố trên thế giới, bao gồm cả Úc', 'L', 'repetition', 'S001: thành phố trên thế giới, bao gồm cả Úc', 'high', None, 'near-verbatim echo of the lede', None),
 ('S015', 'áp lực', 'L', 'repetition', 'S001: áp lực', 'high', None, None, None),
 # S016
 ('S016', 'Sydney', 'L', 'repetition', 'S014: Sydney', 'high', None, None, None),
 ('S016', 'nhà máy', 'L', 'collocation', 'S007: nhà máy xử lý nước tiên tiến', 'low', None, 'phép liên tưởng: same water-infrastructure field, different referent', None),
 # S017
 ('S017', 'Sydney', 'L', 'repetition', 'S016: Sydney', 'high', None, None, None),
 ('S017', 'hồ chứa', 'L', 'repetition', 'S004: xây hồ chứa', 'high', None, None, None),
 # S018
 ('S018', 'nguồn nước', 'L', 'repetition', 'S015: nguồn cung cấp nước', 'high', None, None, None),
 ('S018', 'hồ chứa', 'L', 'repetition', 'S017: hồ chứa', 'high', None, None, None),
 ('S018', 'hạn hán', 'L', 'repetition', 'S017: hạn hán', 'high', None, None, None),
 # S019
 ('S019', 'Chúng ta', 'R', 'personal', 'S018: Chúng ta', 'med', None, 'referent exophoric (generic) but chain continues textually; no ST counterpart (EN pull quote excluded as display element)', None),
 ('S019', 'nguồn cung cấp nước', 'L', 'repetition', 'S018: nguồn nước', 'high', None, None, None),
 ('S019', 'lượng mưa', 'L', 'repetition', 'S016: nước mưa', 'med', None, 'morphological reiteration of mưa', None),
 ('S019', 'nhà máy khử muối', 'L', 'repetition', 'S016: nhà máy khử muối', 'high', None, None, None),
 # S020
 ('S020', 'Nước thải tái chế', 'L', 'repetition', 'S014: nước thải tái chế', 'high', None, None, None),
 # S021
 ('S021', 'này', 'R', 'demonstrative', 'S020: Nước thải tái chế', 'high', None, 'công nghệ = general word for the process', None),
 ('S021', 'nhà máy xử lý nước thải', 'L', 'repetition', 'S007: nhà máy xử lý nước', 'high', None, None, None),
 # S022
 ('S022', 'Harrington', 'L', 'repetition', 'S018: ông James Harrington', 'high', None, None, None),
 ('S022', 'Tái chế', 'L', 'repetition', 'S020: Nước thải tái chế', 'med', None, 'embedded in proper name', None),
 # S023
 ('S023', 'Thứ nhất', 'C', 'additive', 'S022: ba mục tiêu chính', 'high', None, 'enumerative additive', None),
 ('S023', 'công nghệ', 'L', 'repetition', 'S021: Công nghệ này', 'high', None, None, 1),
 # S024
 ('S024', 'Thứ hai', 'C', 'additive', 'S023: mục tiêu thứ nhất', 'high', None, None, None),
 ('S024', 'công nghệ', 'L', 'repetition', 'S023: công nghệ', 'high', None, None, None),
 # S025
 ('S025', 'Và cuối cùng', 'C', 'additive', 'S024: mục tiêu thứ hai', 'high', None, None, None),
 ('S025', 'chúng tôi', 'R', 'personal', 'S022: ông Harrington / Sydney Water', 'med', None, 'institutional chúng tôi', None),
 ('S025', 'thử nghiệm', 'L', 'repetition', 'S023: thử nghiệm công nghệ', 'high', None, None, None),
 ('S025', 'ông', 'R', 'personal', 'S022: ông Harrington', 'high', None, None, None),
 # S026
 ('S026', 'Chúng tôi', 'R', 'personal', 'S025: chúng tôi', 'high', None, None, 1),
 ('S026', 'người dân', 'L', 'repetition', 'S008: Người dân Singapore', 'med', None, 'same lexical item, different referent', None),
 ('S026', 'tham quan', 'L', 'repetition', 'S021: được mời đến tham quan', 'high', None, None, None),
 ('S026', 'chúng tôi', 'R', 'personal', 'S025: chúng tôi', 'high', None, None, 1),
 ('S026', 'công nghệ', 'L', 'repetition', 'S024: công nghệ', 'high', 'R: này', None, None),
 ('S026', 'an toàn và đáng tin cậy', 'L', 'repetition', 'S007: an toàn và đáng tin cậy', 'high', None, 'verbatim reiteration', None),
 # S027
 ('S027', 'Khan', 'L', 'repetition', 'S012: ông (Khan)', 'high', None, None, None),
 ('S027', 'nước tái chế', 'L', 'repetition', 'S026: công nghệ này / S020 nước thải tái chế', 'high', None, None, None),
 # S028
 ('S028', 'hạn hán', 'L', 'repetition', 'S018: hạn hán', 'high', None, None, None),
 ('S028', 'nước thải tái chế', 'L', 'repetition', 'S027: nước tái chế', 'high', None, None, None),
 ('S028', 'nước uống', 'L', 'repetition', 'S005: nước uống', 'med', None, None, None),
 # S029
 ('S029', 'Toowoomba', 'L', 'repetition', 'S028: Toowoomba', 'high', None, 'subject reintroduction', None),
 ('S029', 'công chúng', 'L', 'repetition', 'S021: công chúng', 'high', None, None, None),
 ('S029', 'ông', 'R', 'personal', 'S027: Giáo sư Khan', 'high', None, None, 3),
 # S030
 ('S030', 'ví dụ', 'L', 'repetition', 'S029: một ví dụ', 'high', 'R: khác', 'khác = other (comparative in EN terms); Trần Ngọc Thêm has no comparative-reference class', None),
 # S031
 ('S031', 'người dân', 'L', 'repetition', 'S029: công chúng', 'med', None, None, None),
 ('S031', 'ủng hộ', 'L', 'repetition', 'S029: sự ủng hộ', 'high', None, None, None),
 ('S031', 'dự án', 'L', 'repetition', 'S029: một dự án', 'high', None, None, None),
 # S032
 ('S032', 'Harrington', 'L', 'repetition', 'S025: ông (Harrington)', 'high', None, None, None),
 ('S032', 'tái chế nước thải', 'L', 'repetition', 'S028: nước thải tái chế', 'high', None, None, None),
 ('S032', 'công nghệ', 'L', 'repetition', 'S024: công nghệ', 'high', 'R: này', None, None),
 # S033
 ('S033', 'dự án tái chế nước thải', 'L', 'repetition', 'S032: tái chế nước thải + S031 dự án', 'high', None, None, None),
 # S034
 ('S034', 'công nghệ', 'L', 'repetition', 'S032: công nghệ', 'high', 'R: này', None, None),
 ('S034', 'áp dụng', 'L', 'repetition', 'S027: áp dụng', 'med', None, None, None),
 ('S034', 'ông', 'R', 'personal', 'S032: ông Harrington', 'high', None, None, 2),
 # S035
 ('S035', 'nơi', 'L', 'general word', 'S034: 35 thành phố', 'med', None, 'general word for the cities', None),
 ('S035', 'thành công', 'L', 'repetition', 'S010: sự thành công', 'med', None, None, None),
 # S036
 ('S036', 'Sydney', 'L', 'repetition', 'S032: Sydney', 'high', None, 'contrastive comparison', None),
 ('S036', 'hồ chứa', 'L', 'repetition', 'S018: hồ chứa', 'high', None, None, None),
 # S037
 ('S037', 'này', 'R', 'demonstrative', 'S036: Perth', 'high', None, 'Thành phố = general word for Perth', None),
 ('S037', 'nguồn nước', 'L', 'repetition', 'S019: nguồn cung cấp nước', 'med', None, None, 1),
 ('S037', 'suy giảm', 'L', 'repetition', 'S017: giảm xuống', 'med', None, 'morphological reiteration of giảm', None),
 # S038
 ('S038', 'này', 'R', 'demonstrative', 'S033-S034: tái chế nước thải (lĩnh vực = general word)', 'med', None, None, None),
 # S039
 ('S039', 'Perth', 'L', 'repetition', 'S036: Perth', 'high', None, None, None),
 ('S039', 'biến đổi khí hậu', 'L', 'repetition', 'S015: biến đổi khí hậu', 'high', None, None, None),
 ('S039', 'nguồn nước', 'L', 'repetition', 'S037: nguồn nước ngầm', 'med', None, None, None),
 ('S039', 'Khan', 'L', 'repetition', 'S027: Giáo sư Khan', 'high', None, None, None),
 # S040
 ('S040', 'Perth', 'L', 'repetition', 'S039: Perth', 'high', None, None, None),
 ('S040', 'họ', 'R', 'personal', 'S039: Người dân Perth', 'high', None, None, None),
 ('S040', 'nước ngầm', 'L', 'repetition', 'S037: nguồn nước ngầm', 'high', None, None, None),
 # S041
 ('S041', 'Kế hoạch', 'L', 'repetition', 'S040: một kế hoạch', 'high', None, None, None),
 ('S041', 'nhà máy xử lý nước thải', 'L', 'repetition', 'S021: nhà máy xử lý nước thải', 'high', None, None, None),
 ('S041', 'xử lý', 'L', 'repetition', 'S007/S021: xử lý (tiên tiến)', 'med', None, None, 2),
 # S042
 ('S042', 'Tây Úc', 'L', 'repetition', 'S038: Tây Úc', 'high', None, None, None),
 ('S042', 'tái chế', 'L', 'repetition', 'S033: tái chế nước thải', 'high', None, None, None),
 ('S042', 'nước thải đã qua xử lý', 'L', 'repetition', 'S009: nước thải đã qua xử lý', 'high', None, None, None),
 # S043
 ('S043', 'Queensland', 'L', 'repetition', 'S028: Toowoomba, Queensland', 'high', None, None, None),
 ('S043', 'cũng', 'C', 'additive', 'S042: Perth/WA goal', 'med', None, 'Queensland cũng = additive across boundary', None),
 ('S043', 'dự án tái chế nước', 'L', 'repetition', 'S033: dự án tái chế nước thải', 'high', None, None, None),
 ('S043', 'hạn hán', 'L', 'repetition', 'S028: hạn hán', 'high', None, None, None),
 # S044
 ('S044', 'Tuy nhiên', 'C', 'adversative', 'S043: dự án được xây dựng', 'high', None, None, None),
 ('S044', 'dự án', 'L', 'repetition', 'S043: dự án tái chế nước', 'high', None, None, None),
 # S045
 ('S045', 'nó', 'R', 'personal', 'S044: dự án', 'high', None, None, None),
 ('S045', 'cung cấp nước', 'L', 'repetition', 'S019: nguồn cung cấp nước', 'med', None, None, None),
 ('S045', 'Brisbane', 'L', 'repetition', 'S044: khu vực Brisbane', 'med', None, None, None),
 ('S045', 'Queensland', 'L', 'repetition', 'S043: Queensland', 'med', None, None, None),
 ('S045', 'tương lai', 'L', 'repetition', 'S018: tương lai nguồn nước', 'med', None, None, None),
 ('S045', 'Khan', 'L', 'repetition', 'S039: Giáo sư Khan', 'high', None, None, None),
 # S046
 ('S046', 'nước uống', 'L', 'repetition', 'S028: nước uống', 'med', None, None, None),
 ('S046', 'này', 'R', 'demonstrative', 'S044: dự án', 'high', None, 'hệ thống = general word for the scheme', None),
 ('S046', 'Queensland', 'L', 'repetition', 'S045: Queensland', 'med', None, None, None),
 ('S046', 'sử dụng', 'L', 'repetition', 'S034: đang sử dụng', 'med', None, None, None),
 ('S046', 'cư dân', 'L', 'repetition', 'S028: cư dân thành phố Toowoomba', 'med', None, 'same lexical item, different referent', None),
]
