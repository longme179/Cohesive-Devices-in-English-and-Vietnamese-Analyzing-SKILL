# Appendix 2 — Findings

## A2.1 Corpus and method

**Corpus.** 20 English–Vietnamese pairs of news texts (40 texts) taken from the group's
parallel PDF: 10 SBS pairs (P01–P10) and 10 wire-style pairs (VOA/Reuters/AP, P11–P20).
After removing headlines, subheadings, bylines, captions, pull-quote attributions and
source-display artefacts, the analysed body comprises **697 English sentences (14,982
words)** and **621 Vietnamese sentences (15,939 segmented words, pyvi)**. The Vietnamese
counts are machine-segmented words (syllable-based tokens merged by pyvi); per-word
rates are therefore not compared across languages.

**Settings.** Scope = intersentential: only ties crossing a sentence boundary were
marked; the antecedent was logged, not highlighted. One token, one colour, no overlaps.
English was annotated with Halliday & Hasan (1976) categories; Vietnamese with Trần Ngọc
Thêm's categories (as summarised in Nguyễn Thanh Tùng 2020), mapped onto the same five
colours; phép tuyến tính was not marked (no formal marker).

**Conventions applied** (logged per pair in `exclusions_log.json`): display pull-quotes
repeated inside the source table were excluded (P01, P10); subheadings merged into body
paragraphs were stripped (P02, P07, P08, P10); misplaced content belonging to another
article was excluded from P10 TT (PBS/Centrelink paragraphs) and duplicate paragraphs
were removed (P10, P18); datelines (BANGKOK —, WASHINGTON —) were kept in the text but
never marked. Where the source PDF repeats or abridges sentences, this was preserved and
noted. Pronoun chains were marked once per sentence per chain node; demonstrative +
repeated-noun combinations were marked on the head (e.g. *chương trình này* → mark
*chương trình*), with the demonstrative recorded as `alt` — except when the head was new
lexis, in which case the demonstrative itself was marked.

**Quality control.** Every pair passed an automated QC before release: each tie's text
was verified at its stated occurrence; marker spans were checked for overlap; removing
all markers had to reproduce ST.txt/TT.txt character for character; every antecedent had
to precede its tie (anaphora) or follow it (cataphora). All 20 pairs pass; the QC logs
are in `pairs/PXX/*_qc.txt`.

**Uncertainty.** Low- and medium-confidence ties: EN 423/1605 = **26.4%** (37 low, 386
medium); VI 315/1391 = **22.6%** (39 low, 276 medium). All low-confidence ties plus a
random sample of 6 ties per language × category (113 rows) are listed in
`spot_check.csv` for human verification.

## A2.2 Overall distribution of cohesive devices, ST vs TT

| Category | ST n | ST % | TT n | TT % | median per pair ST / TT |
|---|---|---|---|---|---|
| Reference (R) | 246 | 15.3% | 149 | 10.7% | 11.5 / 6.5 |
| Substitution (S) | 0 | 0.0% | 0 | 0.0% | 0 / 0 |
| Ellipsis (E) | 1 | 0.1% | 0 | 0.0% | 0 / 0 |
| Conjunction (C) | 65 | 4.1% | 67 | 4.8% | 3 / 3 |
| Lexical cohesion (L) | 1293 | 80.6% | 1175 | 84.5% | 62.5 / 55 |
| **Total** | **1605** | 100% | **1391** | 100% | 80 / 69.5 |

Ties per sentence: ST 1605/697 = **2.30**; TT 1391/621 = **2.24**. The two languages
pattern alike in this corpus: lexical cohesion dominates (over 80% of ties in both),
followed by reference; conjunction is a small, stable class; substitution and ellipsis
are marginal at sentence level. The TT has 89 reference ties fewer than the ST (149 vs
246) while keeping the conjunction count almost identical (67 vs 65).

## A2.3 Findings by category

**Reference.** Typical ST forms: personal pronouns (*it, they, she, he, we, their*) and
demonstratives (*this, that, those, It's*, quantified *the two politicians*, P12 S002).
Typical TT forms: *ông, bà, cô, họ, nó, chúng tôi, này, đó, Điều đó*. From ST to TT the
category shrinks by 39% in this corpus (246 → 149): 142 EN reference ties are kept
(63.7% of the 223 with TT counterparts), 72 become zero (pronoun dropped) and 9 become
lexical items. Examples: P01 S013 *They* → P01 TT S012 *Họ* (kept); P01 S038 *he* → TT
S039 *Giáo sư Khan* (R>L, repeated name); P09 S027 *It says* → TT S009 *Báo cáo cho
biết* (pronoun becomes repeated noun). The TT also *adds* 34 reference ties, chiefly
demonstrative NPs (*người mua nhà lần đầu*, P05; *hiệp hội này*, P16 S011) where the EN
used a bare repeated noun — the mirror image of the EN→TT direction.

**Substitution.** No intersentential substitution ties occurred in either language in
this corpus. The candidate items (*do the same* / *làm như vậy*, P01 S002; *did too*)
are all intra-sentential and therefore out of scope. This is a corpus finding, not a
claim about the languages: 20 news texts offer few sentence-level substitutes.

**Ellipsis.** Exactly one tie: P07 ST S005 *Who's a "mate"?* — a fragment answering the
question posed in S003–S004, marked 🟦⟦∅⟧. Its TT counterpart renders the fragment as a
full question (*"Mate" là ai?*), so the tie is omitted in translation (E>zero). No
intersentential ellipsis tie arose in the Vietnamese texts: pro-dropped subjects in the
TT never had their antecedent in a *preceding* sentence with an incomplete clause of the
type the report's Section 3 examples describe; they were either intra-sentential or the
clause was complete without the subject.

**Conjunction.** ST forms: *But, However, However(, the Greens...), And, So, Meanwhile,
Similarly, In contrast, Additionally, To top it off, Now, Then, Instead, On the
contrary*. TT forms: *Tuy nhiên, Nhưng, Và, Vì vậy, Ngoài ra, Bên cạnh, Trong khi đó,
Tương tự, Ngược lại, Thay vào đó, Cũng (mid-sentence), Kể từ đó, Rồi*. Of 63 EN
conjunction ties with counterparts, 52 are kept (82.5%) and 11 dropped (17.5%). The TT
adds 17 conjunction ties (e.g. P06 TT S004 *Tuy nhiên* with no EN counterpart; P15 TT
S007 *cũng*). Position moves are frequent: EN sentence-initial *And*/*also* typically
becomes mid-sentence *cũng* (P02 S010 → TT S011; P02 S024 → TT S027). Examples: P17
S009 *But* → *Nhưng* (kept); P09 S020 *However* → TT S021 *Tuy nhiên* (kept); P04 S036
*Instead* → TT S027 *Thay vào đó* (kept).

**Lexical cohesion.** The dominant device in both languages (ST 1293, TT 1175).
Repetition is the most frequent subtype by far (e.g. *bulk billing* chain, P09, 24 ST
repetitions; *đồng đô la / giá nhà* chains, P08/P10), then synonymy/superordinates
(*homeless → vô gia cư*; *the reclusive state → North Korea*, P13 S002), general words
(*the system, tình trạng, The agreement*), and 4 collocation ties per language (all
currency associations: *đồng rúp – đồng đôla*, P16; *U.S. dollar – Australian dollar*,
P10 — all kept). 932 of 1202 EN L ties are kept (77.5%); 264 are lost where the TT
abridges whole passages; 6 shift category. The TT adds 269 L ties — more than any other
category — typically where the translator repeats a Vietnamese head noun where EN varies
the wording (*ngủ / giấc ngủ / thiếu ngủ*, P04; *hỗ trợ* chains, P02). Examples: P07
S052 *Is Australian English really English?* → TT S052 verbatim echo (kept); P05 S058
*holiday houses* → TT S041 *nhà nghỉ* (association, kept); P01 S015 *water supply in
cities around the world* → TT S031 near-verbatim echo (kept).

## A2.4 Translation shifts

Outcome totals over 1809 alignment rows: **kept 1126 (62.3%), shifted 15 (0.8%),
omitted 348 (19.2%), added 320 (17.7%)**.

| ST category | kept | shifted | omitted | TT added |
|---|---|---|---|---|
| R | 142 | 9 | 72 | 34 |
| S | 0 | 0 | 0 | 0 |
| E | 0 | 0 | 1 | 0 |
| C | 52 | 0 | 11 | 17 |
| L | 932 | 6 | 264 | 269 |

Most frequent shift paths:

1. **L > zero (264).** Almost all whole-passage abridgements rather than local losses:
   P20 TT omits EN S015–S020 and S038–S056 (34 L ties lost); P03 TT omits EN S016–S021
   (the McIntosh block); P06 TT omits EN S024–S038 (the travel-trends section). Where
   the TT translates the sentence, lexical chains are usually kept.
2. **R > zero (72).** Pronoun drop: P01 S007 four *it* ties → pro-dropped TT; P02 S003
   *her* → TT (được đưa đến sống cùng dì); P09 S015 *we* → TT drops. These cluster in
   quoted speech with clear referents — exactly the "recoverable referent" case.
3. **C > zero (11).** P01 S034 *Now* dropped (TT uses progressive *đang*); P04 S026
   *And* dropped; P20 EN S017 *However* family dropped in abridged passages.
4. **R > L (9).** Pronoun → repeated name or lexical NP: *he → Giáo sư Khan* (P01
   S038); *it → đảo quốc này* (P01 S004); *it → từ này* (P07 S042–S043).
5. **L > R (6).** Repeated/general NP → demonstrative NP: *the country → Họ* (P01
   S009); *visitor centre → nơi này* (P01 S013); *the problem → vấn đề này* (P02 S029);
   *the data → người mua nhà* (P08 S005, opposite direction of the general trend).

Counter-examples run both ways: P01 TT S009 turns EN *the country* into the pronoun
*Họ*, and TT texts freely introduce pronouns (*ông, bà, họ*) that the EN does not have
(34 added R ties), so the "Vietnamese always drops" simplification does not hold.

## A2.5 Test of the report's Section 4 claims

**(1) "Vietnamese can omit a recoverable subject or referent more freely." —
supported (in this corpus).** 72 of 223 EN reference ties with counterparts become zero
(32.3%), and a further 9 become repeated names; together 36.3% of EN reference ties
lose their pronominal form in the TT, while the reverse direction (added pronouns, 34)
is smaller and mostly involves kinship pronouns after full names. Example: P01 S007
(*it* ×4) → TT S007 (pro-drop); P02 S003 *her* → TT S003 (dropped).

**(2) "English grammatical substitutes (one, do, so) are rarely matched by grammatical
substitutes in Vietnamese." — insufficient evidence.** No intersentential substitution
tie occurred in either language in these 20 pairs (S = 0 in both). The only candidate
items (*do the same / làm như vậy*, P01 S002) are intra-sentential. The claim could not
be tested at sentence level in this corpus.

**(3) "A connector may be changed, moved or omitted in Vietnamese when the relation is
already clear." — partly supported.** Omission is real but limited: 11 of 63 EN
conjunction ties are dropped (17.5%). Change of position is common (EN sentence-initial
*And/also* → mid-sentence *cũng*: P02 S010→TT S011; P02 S024→TT S027; P05 S015→TT
S014). But the dominant pattern is keeping (82.5%), and the TT also *adds* 17
connectors (P06 TT S004 *Tuy nhiên*; P15 TT S007 *cũng*) — so connectors are adjusted
rather than simply reduced.

**(4) "Lexical repetition is often kept or increased in Vietnamese." — supported, with
one caveat.** Where the TT translates the passage, lexical chains are kept at 77.5% and
the TT adds 269 new L ties — repetition is demonstrably maintained or increased
locally (e.g. P04's *ngủ/giấc ngủ/thiếu ngủ* chain of 21 ties against EN's 15-item
*sleep* chain; P02's *thanh niên* chain of 18 against EN *young people* ×13). The
caveat: raw TT L counts (1175) are lower than ST (1293) solely because six TTs abridge
whole sections (P03, P06, P08, P11, P15, P20); ties per sentence are nearly identical
(2.24 vs 2.30).

**(5) "Related lexical expressions and collocations are kept as a lexical field." —
insufficient evidence (weakly supported).** Only 4 collocation ties per language met
the marking threshold (clear field association, conf=low by rule), and all 4 were kept
(currency chains: P10 *the U.S. dollar → đồng đôla*; P16 *the ruble → đồng rúp*). The
broader lexical-field effect is visible but was captured under repetition/synonymy, so
the collocation-specific claim rests on 4 data points.

## A2.6 Conclusions and recommendations for translators

1. **Do not translate pronouns mechanically** (A2.3, A2.5-1): a third of EN reference
   ties are dropped or lexicalised in natural Vietnamese. First fix the referent, then
   choose between pronoun, repeated noun and omission — the safe default in news TT is
   a repeated name/NP when the referent is a person (P01 S038 *he → Giáo sư Khan*).
2. **Preserve demonstrative NPs as a cohesive resource** (A2.4): Vietnamese *này/đó*
   NPs routinely replace EN repeated nouns (*vấn đề này, Thỏa thuận này*); using them
   keeps the text compact where EN would repeat (P02 S029, P20 TT S028).
3. **Keep the connective relation, adjust the form** (A2.5-3): connectors survive at
   82.5%; the adjustments are positional (*also → cũng* mid-sentence) and lexical
   (*However → Tuy nhiên/Nhưng*). Drop a connector only when the TT clause order and
   aspect already signal the relation (P01 S034 *Now* → *đang*).
4. **Treat repetition as a cohesive feature, not redundancy** (A2.5-4): TTs that
   repeated key items (*thanh niên, giá nhà, đồng đô la*) scored high cohesion; the 269
   added L ties show translators actively maintaining chains that EN carries with
   pronouns and variation.
5. **Watch abridgement damage** (A2.4): 264 L ties were lost to omitted passages —
   most "lost cohesion" in this corpus is lost content. Translators editing down a
   story should check that the first and last mentions of each key chain survive.
6. **Sentence-level substitution/ellipsis is a non-issue in this genre** (A2.3, A2.5-2):
   neither language used *one/do/so* or recoverable omissions across sentence
   boundaries in 1318 sentences; effort is better spent on reference and lexical chains.
7. **Verify quoted-speech chains first** (A2.3): pronoun drops concentrate in quotes
   where the speaker is clear (P01 S007, P09 S015); outside quotes, TTs prefer explicit
   NPs — mirror that distribution.

## A2.7 Limitations

1. **Single AI annotator.** All ties were produced by one annotator (an AI assistant)
   following the written rules; no inter-annotator agreement was computed. 26.4% (EN)
   and 22.6% (VI) of ties carry medium or low confidence and are flagged in
   `spot_check.csv` for human verification.
2. **Boundary cases.** The intersentential-only scope forced many judgement calls
   (intra-sentential chains, same-sentence appositions, chain anchors) that were
   resolved by explicit conventions (A2.1) but could be resolved differently.
3. **Corpus size and genre.** 20 pairs of news texts (SBS feature/wire style). Findings
   hold "in this corpus"; academic, literary or technical texts may behave differently.
4. **Source-document defects.** The parallel PDF contains duplicated sentences,
   misplaced paragraphs and missing spaces; these were logged and (where unambiguous)
   excluded, but some noise remains in the sentence counts.
5. **No inter-annotator check.** The lecturer's spot-check of `spot_check.csv` (113
   rows) is the intended quality control; its results are not part of this report.
6. **Word counts are not comparable across languages** (EN words vs pyvi-segmented VN
   words); only raw counts, shares and per-sentence rates were used, as instructed.
