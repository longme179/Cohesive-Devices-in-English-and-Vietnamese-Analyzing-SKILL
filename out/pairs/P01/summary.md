# P01 — Pair summary

**ST (English):** Beer made from recycled wastewater? Some want to see it on Australian bottle-o shelves
**TT (Vietnamese):** Bia làm từ nước thải tái chế: Bạn có dám thử?

## Counts

| | sentences | R | S | E | C | L | total | med/low conf |
|---|---|---|---|---|---|---|---|---|
| ST | 49 | 30 | 0 | 0 | 10 | 95 | 135 | 47 |
| TT | 46 | 20 | 0 | 0 | 9 | 90 | 119 | 30 |

Alignment: kept 90, shifted 10,
omitted 35, added 27.

## Most informative examples

- **shifted / R>L**: ST S004 “it” (R/personal) → TT S004 “đảo quốc” (L/synonym) — EN pronoun it rendered as lexical NP đảo quốc này; merged with EN-001 counterpart
- **shifted / L>R**: ST S009 “country” (L/superordinate) → TT S009 “Họ” (R/personal) — the country -> Họ (pronoun)
- **shifted / R>L**: ST S010 “its” (R/personal) → TT S010 “Singapore” (L/repetition) — its -> của Singapore (repeated proper name)
- **shifted / L>R**: ST S013 “visitor centre” (L/repetition) → TT S013 “này” (R/demonstrative) — repeated noun visitor centre -> general word + demonstrative nơi này
- **shifted / L>R**: ST S020 “process” (L/general word) → TT S021 “này” (R/demonstrative) — the process -> Công nghệ này (demonstrative NP)
- **kept**: ST S004 “city-state” (L/synonym) → TT S004 “đảo quốc” (L/synonym) — city-state -> đảo quốc, synonym re-description in both

## Notes

- No substitution (S) or ellipsis (E) ties in this pair: the only substitute
  items (ST "do the same" / TT "làm như vậy") are intra-sentential, outside the
  intersentential scope.
- Source-document defects kept as-is (see exclusions_log.json): duplicated
  sentence ST S031–S032; missing spaces TT S004, S012; EN S033 pull-quote block
  excluded as display element while its TT translation (TT S019) is body text.
- TT abridges the ending (EN S047–S049 partly unrendered).
