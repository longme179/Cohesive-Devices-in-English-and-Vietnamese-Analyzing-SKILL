# P08 — Pair summary

**ST (English):** Revealed: Australian suburbs with the biggest home price falls
**TT (Vietnamese):** Những khu vực có giá nhà giảm mạnh nhất tại Úc trong năm 2024

## Counts

| | sentences | R | S | E | C | L | total | med/low conf |
|---|---|---|---|---|---|---|---|---|
| ST | 39 | 13 | 0 | 0 | 7 | 66 | 86 | 14 |
| TT | 37 | 7 | 0 | 0 | 8 | 62 | 77 | 16 |

Alignment: kept 74, shifted 1,
omitted 11, added 8.

## Most informative examples

- **shifted / L>R**: ST S005 “the data” (L/general word) → TT S005 “người mua nhà” (L/repetition) — the data shows -> dữ liệu phản ảnh; TT marks người mua nhà NP instead
- **kept**: ST S003 “Australia's housing market” (L/repetition) → TT S003 “Thị trường nhà ở Úc” (L/repetition) — Australia's housing market -> Thị trường nhà ở Úc

## Notes

- No substitution (S) or ellipsis (E) ties in this pair: the only substitute
  items (ST "do the same" / TT "làm như vậy") are intra-sentential, outside the
  intersentential scope.
- Source-document defects kept as-is (see exclusions_log.json): duplicated
  sentence ST S031–S032; missing spaces TT S004, S012; EN S033 pull-quote block
  excluded as display element while its TT translation (TT S019) is body text.
- TT abridges the ending (EN S047–S049 partly unrendered).
