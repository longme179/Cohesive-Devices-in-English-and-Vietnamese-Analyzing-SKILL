# PXX tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# - text tie: gap_after=None, recovered=None
# - ellipsis: text=None, gap_after="exact substring ending before ∅",
#             recovered="{meaning}", gap_after="" only for sentence-initial ∅
# - level: "LC" intersentential / "TC" intra-sentential / "TD" title
# - ref:  R only, one of "A"/"C"/"E"; must be a manual decision, never defaulted
# - occ:  explicit when the same text/gap_after repeats in the sentence
#
# Categories: R reference | S substitution | E ellipsis | C conjunction | L lexical
# Do not add a row that is not in the analysis.  Do not use regex/word lists.

ST = [
    # R: anaphoric pronoun with a clear antecedent before the sentence
    ("S003", "it", "R", "personal", "S002: the new app", "high", None,
     "pronoun refers to the app", 1, None, None, "LC", "A"),

    # C: conjunction across a sentence boundary
    ("S004", "But", "C", "adversative", "S003: the app was announced",
     "high", None, None, 1, None, None, "LC", None),

    # L: repetition / synonym / collocation chain
    ("S005", "the application", "L", "synonym", "S002: the new app", "med",
     None, "synonym re-description", 1, None, None, "LC", None),

    # E: zero subject in a coordinated clause (LC if it points to S003)
    ("S006", None, "E", "nominal", "S003: the government", "high", None,
     "[LC] zero subject after 'and'; recover {the government}",
     1, "and ", "{the government}", "LC", None),

    # S: pro-form substitution inside the sentence
    ("S007", "one", "S", "nominal", "S006: a visa", "high", None,
     "[TC] one ← a visa", 1, None, None, "TC", None),
]

TT = [
    ("S002", "nó", "R", "personal", "S001: ứng dụng mới", "high", None,
     "đại từ hồi quy", 1, None, None, "LC", "A"),
    ("S003", "Nhưng", "C", "adversative", "S002: ứng dụng đã được công bố",
     "high", None, None, 1, None, None, "LC", None),
    ("S004", "ứng dụng", "L", "repetition", "S002: ứng dụng mới", "med",
     None, "lặp từ vựng", 1, None, None, "LC", None),
    ("S005", None, "E", "nominal", "S002: chính phủ", "high", None,
     "[LC] lược chủ ngữ vế tọa hợp; hồi phục {chính phủ}",
     1, "và ", "{chính phủ}", "LC", None),
    ("S006", "một", "S", "nominal", "S005: thị thực", "high", None,
     "[TC] một ← thị thực", 1, None, None, "TC", None),
]
