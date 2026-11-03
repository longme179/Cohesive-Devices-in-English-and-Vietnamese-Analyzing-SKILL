# EN–VI mapping and decision tests

This file is the single place where a surface form is turned into one of the five
Appendix codes. Read it immediately before writing a tie row. When two readings
are possible, the analysis file must name both and the table must keep **one**
code.

## 1. The five codes (this project)

| Code | Name | Relation | Typical English | Typical Vietnamese |
|---|---|---|---|---|
| **R** | Reference | identity of a referent | *he, she, it, they, this, that, the, such, other* | *nó, họ, ông ấy, này, ấy, đó, kia* (repeated nouns are L, not R — §3.9) |
| **S** | Substitution | replacement of **wording** | *one, ones, do, so, not, the same* | *như vậy, làm vậy, thế, vậy* |
| **E** | Ellipsis | omission recoverable from co-text | *Yes, ∅; John can ∅; two ∅* | zero subject/verb/object recoverable from the co-text |
| **C** | Conjunction | semantic relation between clauses | *and, but, so, then, however, because* | *và, nhưng, nên, vì, rồi, tuy…nhưng* |
| **L** | Lexical cohesion | lexical relation between items | repetition, synonym, antonym, superordinate, collocation | *phép lặp, phép thế đẳng nghĩa, phép liên tưởng, phép đối* |

**Notation warning.** Category `E` (ellipsis) and direction `ref=E`
(exophoric) are different fields. A row with `cat="E"` has `ref=None`; a row with
`ref="E"` is an R tie whose referent is outside the text. Never write both.

## 2. Mapping table

| H&H category | Closest Trần Ngọc Thêm device | What it is *not* | Decision test |
|---|---|---|---|
| Reference (personal, demonstrative, comparative, `the`) | *phép thế đại từ* (hồi quy / dự báo), *phép lặp từ vựng* when VI repeats a noun | not substitution; not ellipsis | Is the **same referent** retrieved? → R |
| Substitution (*one/do/so*) | *phép thế đại từ* when the pro-form stands for wording; *phép thế đẳng nghĩa* is lexical, not this | not reference | Does the form replace **wording** that could be spelled out? → S |
| Ellipsis (nominal/verbal/clausal) | *phép tỉnh lược* (yếu/liên kết/mạnh) | not zero anaphora (*thế đại từ khiếm diện*), which tracks a referent | Is the missing piece **recoverable wording**? → E |
| Conjunction (additive/adversative/causal/temporal) | *phép nối* (lỏng/liên kết/chặt) | not a word-class test; not lexical cohesion | Is there a **semantic relation** between clauses? → C |
| Lexical cohesion (reiteration, collocation) | *phép lặp từ vựng*, *phép thế đẳng nghĩa*, *phép liên tưởng*, *phép đối* | not reference; not topic continuity | Is there a **lexical relation** between two items? → L |

## 3. Decision tests, in order

1. **Identify the two items.** Write both (the presupposing form and the
   presupposed item/antecedent) before choosing a category. If you cannot name the
   second item, there is no tie yet.
2. **Identity or wording?** Same referent → R. Replaces wording → S. Missing
   wording → E. Semantic relation between clauses → C. Lexical relation between
   content words → L.
3. **Does the English form have an antecedent in the text?** No → exophoric
   (`ref=E`), still R, and say in the note that the referent is outside the text.
   An antecedent that is merely far away is still anaphoric (`ref=A`).
4. **Cataphoric?** The antecedent comes later (rare in news; common in
   introductions and headings) → `ref=C`. Do not default to A.
5. **Zero form.** Code E. If the zero tracks a **participant** rather than
   omitting wording, the Vietnamese analysis is *thế đại từ khiếm diện*; record
   that reading in §2/§4 of the analysis, but keep the single E row. Do not add an
   R row for the same zero.
6. **`the`.** It is a reference item (R), even when Vietnamese realizes
   definiteness by *ấy/đó*, by repetition, or by zero. Do not treat it as L.
7. **`one / do / so / not`.** These are S when they stand for wording (*the red
   one*, *he did*, *I think so*). A pronoun in the same position is R.
8. **A connector is not automatically C.** If the relation is not recoverable
   (e.g. a filler *and* that only continues the sentence), do not invent a C tie.
   If the relation is clear but the connector is zero in one language, code the
   side that has the relation and note the shift.
9. **A repeated noun is L, not R.** This is the most frequent EN→VI shift:
   English pronoun → Vietnamese repetition. Code the Vietnamese repetition as L
   and note “R→L realization” in the analysis; do not code the Vietnamese noun as
   R just because the English side was R.
10. **Synonym, antonym, superordinate, collocation → L.** *Phép thế đẳng nghĩa*
    and *phép liên tưởng* are lexical: L, never S.
11. **Parallelism / order alone (*phép đối*, *phép tuyến tính*) is not a tie.**
    Record the lexical pair if there is one (L); otherwise no row.
12. **Function, not form, across languages.** The same function may be realized
    by a different device on the other side. That is a shift to describe, not an
    error to flag and not a reason to duplicate a row.
13. **One form, one row.** Do not code the same item as both R and S, or both R
    and L. If the analysis needs both perspectives, the table gets the dominant
    relation and the analysis explains the other.
14. **Level.** A relation inside one sentence is `[TC]`; across sentences is
    `[LC]`; a title is `[TD]`. Only `[LC]` supports a claim about cohesion beyond
    the sentence.

## 4. Vietnamese forms that need a decision

| Form | Default | Watch out for |
|---|---|---|
| zero subject | E | may be *khiếm diện* (participant tracking) or *tỉnh lược* (wording omission); record which |
| *nó, họ, ông ấy, bà ấy* | R | kinship/status pronoun; register and distance are part of the meaning |
| repeated proper name / noun | L | normal Vietnamese cohesion; not an error and not R |
| *này, ấy, đó, kia* | R | proximal/distal meaning; `ấy/đó` often realizes English *the* |
| *như vậy, thế, vậy, làm vậy* | S | if it replaces wording; if it points to a fact, it may be R (text reference) |
| *và, nhưng, nên, vì, rồi* | C | check the relation type; *rồi* can be temporal or aspectual |
| *cái, việc, điều, con, chiếc* | — | classifier alone is not a tie; *việc/điều* can be a general noun (L or R) |
| final particle (*nhé, ạ, chứ*) | — | not a cohesive device; do not create a row |
| *phép đối* pair | L | only if the two lexical items are identifiable; parallelism alone is not a tie |

## 5. Expected cross-language shifts (from the 2020 study)

| Direction | Typical shift | Annotation consequence |
|---|---|---|
| EN→VI | pronoun → zero | R (EN) vs E (VI); do not invent a VI pronoun |
| EN→VI | pronoun → repeated noun | R (EN) vs L (VI); note the shift |
| EN→VI | *the* → demonstrative / zero / repetition | R (EN) vs R/L/E (VI) depending on the realization |
| EN→VI | clausal ellipsis → filled clause | E (EN) only; the VI side has no E row |
| VI→EN | zero subject → pronoun | E (VI) vs R (EN) |
| VI→EN | repeated noun → pronoun | L (VI) vs R (EN) |
| VI→EN | zero connector → explicit connector | C on the side where the relation is marked; note the shift |
| VI→EN | weak ellipsis → explicit verb/NP | E (VI); the EN side may have no counterpart |

## 6. Common misclassifications and the fix

| Wrong | Why it happens | Fix |
|---|---|---|
| coding a repeated noun as R | the English side had a pronoun | R belongs to the English form; the Vietnamese repetition is L |
| coding a zero as R | “it refers to the same person” | the category is about the form: zero = E; the referent analysis goes in §4 |
| coding *the* as L | it looks like a determiner | `the` is R (definiteness); L needs a lexical relation |
| coding *phép thế đẳng nghĩa* as S | the names look alike | it is lexical synonymy → L |
| creating C from a connector word | the word is present | C needs a recoverable semantic relation |
| creating L from topic continuity | both sentences are “about” the same thing | L needs two identifiable lexical items in a relation |
| double-coding R + E for one zero | wanting to show both analyses | one code per form; the analysis explains the other reading |

## 7. When the decision is genuinely unclear

Write the row with `conf: "low"` and a note naming both candidates, e.g.
`"R vs L: EN 'it' → VI 'công ty' (repetition); coded L per §3.9"`. A documented
low-confidence decision is acceptable; an undocumented guess is not.
