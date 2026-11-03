# P01 mini example — hand-written tie table (13-field format).
ST = [
    ("S002", "It", "R", "personal", "S001: a new shelter", "high", None,
     "đại từ hồi quy", 1, None, None, "LC", "A"),
    ("S003", "But", "C", "adversative", "S002: forty beds", "high", None,
     "nối tương phản liên câu", 1, None, None, "LC", None),
    ("S004", None, "E", "nominal", "S002: forty beds", "high", None,
     "[LC] lược {beds} sau “add more”", 1, "add more", "{beds}", "LC", None),
    ("S004", "they", "R", "personal", "S004: Officials (trong câu)", "high",
     None, "[TC] they ← Officials trong cùng câu", 1, None, None, "TC", "A"),
    ("S005", "One", "S", "nominal", "S001: a new shelter", "high", None,
     "[LC] One ← a new shelter", 1, None, None, "LC", None),
]
TT = [
    ("S002", "Nơi này", "R", "demonstrative", "S001: nơi trú ẩn", "high", None,
     "danh ngữ demonstrative hồi quy", 1, None, None, "LC", "A"),
    ("S003", "Nhưng", "C", "adversative", "S002: bốn mươi giường", "high", None,
     "nối tương phản liên câu", 1, None, None, "LC", None),
    ("S004", None, "E", "nominal", "S002: bốn mươi giường", "high", None,
     "[LC] lược {giường} sau “bổ sung thêm”", 1, "bổ sung thêm", "{giường}",
     "LC", None),
    ("S004", "họ", "R", "personal", "S004: Các quan chức (trong câu)", "high",
     None, "[TC] họ ← Các quan chức trong cùng câu", 1, None, None, "TC", "A"),
    ("S005", "nơi", "L", "repetition", "S001: nơi trú ẩn", "med", None,
     "lặp danh từ chung", 1, None, None, "LC", None),
]
