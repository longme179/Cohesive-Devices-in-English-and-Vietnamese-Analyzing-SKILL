# HƯỚNG DẪN TÁI LẬP (REPLICATION GUIDE) — GÁN NHÃN LIÊN KẾT NGỮ PHÁP EN–VI

Tài liệu này giúp một AI agent (hoặc người) **tái lập toàn bộ quy trình** của repo này với **20 cặp bài báo khác** để ra sản phẩm tương đương **Appendix 1** (phụ lục highlight 5 màu + chữ mũ A/C/E, 20 bảng 2 cột EN|VI).

> **Phạm vi vòng này: APPENDIX 1.** Phần Appendix 2 (báo cáo phát hiện + `stats.csv` / `shifts.csv` / `spot_check.csv`) **chưa được tái lập trong vòng này** vì tầng alignment của pipeline cũ có lỗi hệ thống (xem §6, bẫy 9–11); sẽ làm lại sau khi xây lại bảng align theo ngữ nghĩa. Mọi số liệu cấp alignment của vòng cũ **không dùng được cho đến khi xây lại**.

## 0. Nguyên tắc nền tảng — PHÂN TÍCH THỦ CÔNG TỪNG CẶP TRƯỚC, MARKING THÀNH PHẨM SAU

Đây là bài học lớn nhất của vòng 20 cặp (2.996 tie, coverage render 100%, QC 40/40 PASS):

1. **Ba tầng dữ liệu, ba mức tin cậy khác nhau:**
   - **Tầng 1 — văn bản chuẩn + tách câu** (`ST.txt`/`TT.txt`/`*_seg.json`): tin cậy (có QC ký tự).
   - **Tầng 2 — bảng tie hai đầu** (`ST_ties.json`/`TT_ties.json`): tin cậy **vì được viết bằng đọc hiểu từng cặp** (mỗi tie có tiền trạm + độ tin cậy; render + QC gates bắt lỗi vị trí/ chồng lấn). Đây là nền của Appendix 1.
   - **Tầng 3 — alignment + thống kê tổng hợp** (`align.json` → shifts/stats): **không tin cậy ở cấp link** — bảng align cũ được ghép theo *thứ tự xuất hiện* (zip vị trí), không theo ngữ nghĩa (bẫy 9). Chỉ dùng sau khi đối chiếu lại tay.
2. **Không bao giờ dùng đối khớp chuỗi (string matching) hoặc ghép thứ tự để quyết định liên kết.** Quyết định gán nhãn phải giải thích được bằng ngữ nghĩa: tiền trạm là gì, vì sao item này là R/L/C..., vì sao câu VI này là bản dịch của câu EN kia.
3. **Mỗi cặp phải có một bản phân tích thủ công riêng trước khi chốt marking** (quy trình chi tiết ở §4, Giai đoạn B). Bộ 20 bản phân tích này nằm ở `download/BDNC/semantic_analysis/Pair_01…Pair_20/` (mỗi bản ~200 dòng: bản đồ câu, chuỗi từ vựng, nhân vật, sai lệch dịch, đánh giá pipeline). Nó không phải "báo cáo đẹp" — nó là **lớp kiểm chứng**: chính việc đọc tay P20 đã phát hiện bảng align zip vị trí và cờ omitted gắn nhầm tầng ID, điều mà mọi QC tự động đều bỏ qua.
4. **Notes tự sinh phải được kiểm tra nguyên văn trước khi ghi.** Vòng cũ copy-paste Notes cho ~19/20 cặp, viện dẫn đơn vị không tồn tại ("do the same", "S031–S032 trùng", "pull-quote S033"…) — lần nào trùng thực tế cũng là ngẫu nhiên (bẫy 8).

## 1. Tổng quan nhiệm vụ

Gán nhãn **quan hệ liên kết ngôn bản (cohesion)** trên cặp bài báo song song Anh–Việt:

- **Phía EN** theo Halliday & Hasan (1976), 5 phương tiện: reference, substitution, ellipsis, conjunction, lexical cohesion.
- **Phía VI** đối chiếu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh Tùng 2020): **phép thế đại từ ≈ reference + substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ conjunction; phép lặp + phép đối + phép thế đồng nghĩa + phép liên tưởng ≈ lexical cohesion.**
- Ký hiệu thống nhất 5 danh mục: `R S E C L` (R🟨 S🟩 E🟦 C🟧 L🟪).
- **Reference (R) tách hướng quy chiếu**: `A` = anaphoric, `C` = cataphoric, `E` = exophoric (hiển thị bằng chữ mũ trên khối đánh dấu).

### Quy ước gán nhãn (quan trọng — quyết định tính tái lập)

1. **Chỉ liên-câu (intersentential)**: item nằm ở câu N, tiền trạm ở câu M ≠ N (thường M < N). Liên kết nội câu không đánh dấu.
2. **Chỉ tô chính item** (từ mang chức năng liên kết), không tô cả danh ngữ chứa nó. "The" không tô khi đầu ngữ lặp lại từ khóa.
3. **Điều kiện tiên quyết (prerequisite)** — thực thể nêu lần đầu, deictic chưa neo trong văn bản — **không tô**, ghi vào `exclusions_log.json`.
4. **Một chuỗi nhiều từ trong cùng một câu chỉ tô một lần** (vd `my/me/us` cùng câu → 1 mark).
5. **Đại từ ngôi 1/2 trong trích dẫn**: nếu attribution (tên người nói) nằm ở **câu trước** → được phép gán nhãn (tiền trạm = attribution). Attribution cùng câu hoặc sau câu → không đủ điều kiện liên-câu.
6. **Hướng quy chiếu A/C/E**:
   - `A`: tiền trạm truy xuất được từ văn bản trước (thực thể/mệnh đề/attribution).
   - `C`: tiền trạm ở câu sau (trong ngữ liệu tin tức này = 0 trường hợp liên-câu).
   - `E`: tiền trạm ngoài văn bản (authorial/generic we-ta, bạn/you hướng độc giả). Với tie E, trường `ante` chỉ mang tính thông tin, không bắt buộc mã câu.
7. `conf` ∈ {high, med, low}; bridging (đề cập lần đầu hàm ý) gán `low` và vẫn giữ trong inventory.
8. **Bất đối xứng inventory là bình thường, không "sửa cho cân"**: hai đầu đánh dấu độc lập theo quy ước từng ngôn ngữ (EN có "the U.S." lần 2 không đánh dấu — VI "Hoa Kỳ" lần 2 đánh dấu…); chênh lệch ghi nhận trong phân tích cặp, **không** sửa inventory khi đã chốt số liệu.

## 2. Môi trường

```bash
python3 (≥3.12 — f-string lồng cùng loại dấu nháy)
pip install pymupdf python-docx pyvi   # trích PDF, xuất DOCX, tokenize VI
pandoc, soffice (libreoffice)          # chuyển đổi báo cáo
```

## 3. Đầu vào kỳ vọng

- **PDF song ngữ 2 cột EN|VI** (`upload/Appendix 1 - 20 pairs of articles.pdf`): mỗi cặp = tiêu đề + link + bảng 2 cột song đoạn (mỗi hàng = một đoạn EN đối chiếu VI).
- Hoặc **markdown tham chiếu** (`upload/Appendix 1 - 20 pairs.md`): bảng `| EN | VI |` từng dòng, có link bài gốc — script `build_appendix_md.py` dùng file này làm khung bố cục của phụ lục cuối (PAIR_BOUNDARIES + URL_LINES là số dòng, **phải chỉnh lại cho ngữ liệu mới**).

## 4. Quy trình 6 giai đoạn (22 bước) — MARKING CHỈ SAU KHI PHÂN TÍCH

### GIAI ĐOẠN A — Trích xuất & dựng văn bản chuẩn (tự động + kiểm tay)

**Bước 1 — Trích PDF → raw pairs.** `extract_pdf.py` → `extract_pairs.py`: tách 2 cột theo tọa độ x (VI cell edge = min(vi_x0); EN edge = max(en_x1) trước vi_left+10), nối mảnh dấu tiếng Việt (gap ≤ 1,5pt), bỏ đoạn URL rời. Output `out/raw_pairs/PXX.json {en:[para...], vi:[para...]}`. Chạy `flag_candidates.py` rà tiêu đề phụ/chú ảnh (SHORT-NOEND, Photo/Credit…).

**Bước 2 — Dựng văn bản chuẩn.** `build_texts.py`: áp `CFG` từng pair (exclude/strip_prefix/replace) → `ST.txt`, `TT.txt`; mọi thứ bị loại ghi `exclusions_log.json` kèm lý do (title row, subhead, pull-quote, byline…). `meta.json` chứa title_en/title_vi.

**Bước 3 — Tách câu.** `segment.py`: đánh số S001…, bảo vệ từ viết tắt/số (U.S., Mr., 1.5, TP.HCM…), "…" không tách; câu ghi span (fa, fb); sửa thủ công qua `PXX_seg_fixes.json`. Output `ST_seg.json`, `TT_seg.json`.
⚠ Lỗi thiếu space của nguồn (vd "hợp lệ.Thông") khiến hai câu dính thành MỘT đơn vị — kiểm tra ranh giới câu quanh mọi dấu chấm không khoảng trắng (bẫy 7).

### GIAI ĐOẠN B — PHÂN TÍCH THỦ CÔNG TỪNG CẶP (bước người/AI — BẮT BUỘC trước khi viết tie table)

Đây là giai đoạn quyết định chất lượng Appendix 1. Với **mỗi cặp**, đọc cả hai văn bản chuẩn và lập 6 sản phẩm:

**Bước 4 — Bản đồ tương ứng câu (sentence map).** Đọc lần lượt EN→VI, với mỗi câu EN ghi một trong: `giữ` (có đúng một câu VI dịch, giữ thứ tự) / `gộp` (n câu EN → 1 câu VI) / `tách` (1 câu EN → n câu VI) / `bỏ` (không có bản dịch — đánh dấu ranh giới khối cắt) / và danh sách câu VI **tự sinh** (lede, byline, paraphrase — không có đối ứng EN; markdown gốc ghi ô EN = "none" là bằng chứng tốt). Ví dụ P20: 41/60 câu giữ (gồm 1 gộp S004+S005, 1 tách S024), 19 câu bỏ gom thành 4 khối (mỗi khối = lượt phát biểu thứ hai của một nhân vật), 3 câu lede tự sinh + byline. Bản đồ này là **điều kiện tiên quyết** của Giai đoạn D (align) và là bằng chứng cho mọi phát biểu "độ phủ".

**Bước 5 — Kiểm kê nhân vật & tầng hiển thị.** Danh sách người nói + số khối quote + vị trí khung dẫn (mở/đóng, dịch chỗ); subhead EN ↔ VI (bỏ/giữ); byline (thêm/cắt/dính); dateline; xử lý tít (khử tên, hấp thụ vào lede…). Tầng này là "vùng can thiệp tự do" của desk VI — can thiệp ở đây KHÔNG làm hỏng độ phủ tầng câu, nhưng là nơi lỗi nguồn hay trú ẩn.

**Bước 6 — Kiểm kê chuỗi từ vựng + số liệu.** Mỗi chuỗi then chốt (tên quốc gia/tổ chức, thuật ngữ chủ đề, chuỗi "vụ kiện/nghiên cứu/thỏa thuận"…): liệt kê các dạng EN ↔ các dạng VI, nhận xét hội tụ/phân rã; mọi con số hai bên đối chiếu từng vị trí (kể cả số tự sinh, số mất đích, số hedge hóa).

**Bước 7 — Rà lỗi nguồn hai đầu.** Typo, cú pháp hỏng, câu trùng, thiếu space, sai đơn vị… và ghi **chiến lược VI** với từng lỗi: chuẩn hóa im lặng hay truyền bê (cùng một bài có thể có cả hai).

**Bước 8 — Đối chiếu danh mục R/S/E/C/L hai đầu (đếm tay).** Cho mỗi danh mục: vị trí liên-câu có đối ứng (định danh cặp EN↔VI), vị trí trong khối cắt, vị trí VI tự sinh; quy chiếu [+người]/[−người]; đích distal/proximal; thay/lược/hiện thực hóa. Bảng này chính là "đối chiếu số đếm: phân tích ngữ nghĩa ↔ pipeline" cuối mỗi bản phân tích.

**Bước 9 — Viết bản phân tích cặp.** Lưu `download/BDNC/semantic_analysis/Pair_XX/PXX_phan-tich-ngu-nghia.md` theo khuôn 9 mục: (1) tổng quan cấu trúc + bản đồ câu; (2) tỉnh lược; (3) thế; (4) quy chiếu (bảng + [±người] + chuỗi danh xưng); (5) nối; (6) liên kết từ vựng; (7) bảng dịch chuyển nổi bật; (8) bất thường dữ liệu nguồn (kể cả đánh giá alignment pipeline); (9) đối chiếu số đếm + tổng kết. Cập nhật `INDEX.md` (tiến độ + phát hiện xuyên cặp) **ngay sau mỗi cặp** — sổ cái xuyên cặp (chuỗi B1–B28) chỉ có giá trị nếu cập nhật liên tục.

**Cổng kiểm tra của Giai đoạn B (không đạt thì không sang C):**
- [ ] Mỗi câu EN đã có trạng thái trên bản đồ; tổng giữ+bỏ+tự sinh khớp số câu hai đầu;
- [ ] Mỗi khối cắt đã định danh nội dung + số tie EN rơi vào;
- [ ] Mỗi con số đã đối chiếu; mỗi lỗi nguồn đã ghi chiến lược xử lý;
- [ ] Không kết luận dịch chuyển nào thiếu ví dụ nguyên văn hai đầu.

### GIAI ĐOẠN C — Gán nhãn (dựa trực tiếp trên phân tích B)

**Bước 10 — Viết bảng tie.** `scripts/tie_tables/PXX.py` rồi chạy `annotate.py PXX`:
```python
# (sent, text, cat, sub, ante, conf, alt, note, occ)
('S004', 'it', 'R', 'personal', 'S003: Singapore', 'high', None, None, 3)
# tie R bắt buộc thêm: ref='A'|'C'|'E' (annotate.py tự điền 'A' nếu thiếu)
```
`annotate.py` **từ chối ghi** nếu occurrence của text không tồn tại trong câu. Sau đó `fix_tie_occ.py`/`fix_tie_occ_v2.py` sửa lỗi occ rơi giữa từ.
Mọi tie phải truy vết được về một nhận định trong bản phân tích B (tiền trạm, loại, hướng, độ tin cậy).

**Bước 11 — Render + QC từng pair.** `render.py PXX` sinh `ST/TT_highlighted.md`, `PXX.html` (tooltip), `*_qc.txt`. **QC gates:** (a) text nằm đúng occurrence trong câu; (b) marker không chồng lấn; (c) bỏ marker → ra đúng .txt từng ký tự; (d) tiền trạm `ana` nằm trước (tie ref='E' miễn); (e) in phân bố danh mục; (f) mọi R phải có ref ∈ {A,C,E}.

### GIAI ĐOẠN D — Căn cặp theo NGỮ NGHĨA (chỉ sau khi có bản đồ câu)

**Bước 12 — Viết bảng align thủ công.** `scripts/align_tables/PXX.py` với quy tắc:
- Link `st_tie → tt_tie` chỉ được ghi khi **hai tie cùng tham chiếu một tiền thể** (dịch đúng referent), kiểm tra bằng việc đọc hai câu chứa chúng;
- Outcome `omitted` gắn cho **từng tie** nằm trong câu EN không có bản dịch (lấy từ bản đồ câu bước 4), KHÔNG gắn theo mã câu (bẫy 10: tie-ID ≠ sentence-ID);
- Outcome `kept` khi tie EN có đối dịch là một tie VI (hoặc cụm dịch không được đánh dấu — khi đó ghi `kept_unmarked` kèm note);
- TT tie không được tie EN nào nhắc → `added`, phân biệt added-thật (câu VI tự sinh) vs added-do-bất-đối-xứng-inventory (đối ứng EN là first-mention không đánh dấu).

**Bước 13 — Cổng kiểm tra align (mới, bắt buộc):**
- [ ] Mỗi link kept: đọc thành cặp "EN text → VI text" — nếu đọc lên thấy vô nghĩa (vd "South Korea → Hoa Kỳ", "pirates → trừng phạt") là zip vị trí, làm lại;
- [ ] Tổng kept + omitted = tổng ST tie; tổng câu bỏ theo align khớp bản đồ câu;
- [ ] Mỗi cờ omitted: câu chứa tie thực sự không có bản dịch trong TT;
- [ ] Sample ngẫu nhiên 10 link: người độc lập đọc 2 câu phải xác nhận cùng referent.

### GIAI ĐOẠN E — Lắp Appendix 1

**Bước 14 — Lắp phụ lục.** `build_appendix_md.py`: đối chiếu từng hàng bảng gốc ↔ văn bản đã đánh dấu (fuzzy match + repair), sinh `Appendix1.md` (span 5 màu inline CSS), `Appendix1.html` (2 cột + tooltip), `appendix1_segments.json` (IR), `match_stats.json`. Gate: **marker coverage phải = 100%** (rendered/markers), straddle/orphan = 0. Nếu thiếu: `diagnose_missing.py PXX`.

**Bước 15 — Xuất DOCX.** `export_docx.py` → `Appendix1.docx` (bảng 2 cột, tô màu run-level `w:shd`, chữ mũ A/C/E superscript). Xuất PDF qua `soffice` nếu cần bản in.

### GIAI ĐOẠN F — Tổng hợp & giao

**Bước 16 — Thống kê.** `stats.py` → `stats.csv`, `shifts.csv`, `spot_check.csv`; `summarize.py PXX` → `summary.md` + `progress.json`. ⚠ Chỉ chạy sau khi align qua cổng bước 13 (vòng cũ chạy với align zip → thống kê cấp alignment lỗi).
**Bước 17 — Kiểm cuối (mở lại file thật):** mở `Appendix1.docx/html/pdf`, soát 3 cặp ngẫu nhiên: đủ 20 bảng, màu đúng danh mục, chữ mũ A/C/E đúng, tooltip hiện tiền trạm; tìm ký tự lạ/placeholder.
**Bước 18 — Giao.** Copy vào `download/BDNC/` (docx/html/md/pdf) + README mô tả.

*(Giai đoạn G — Appendix 2: báo cáo phát hiện + thống kê alignment. Ngoài phạm vi vòng này — dựng lại từ dữ liệu align đã qua cổng bước 13.)*

## 5. Schema dữ liệu lõi

```jsonc
// ST_ties.json / TT_ties.json
{ "pair": "P01", "lang": "EN", "ties": [
  { "id": "P01-EN-002", "sent": "S004", "text": "it", "occ": 3,
    "cat": "R",              // R|S|E|C|L
    "sub": "personal",       // R: personal|demonstrative|comparative|quantified
                             // C: adversative|additive|temporal|causal
                             // L: repetition|synonym|antonym|collocation|general word|superordinate...
    "dir": "ana",            // hướng của tiền trạm (ana|cata) — ref='E' miễn kiểm
    "ref": "A",              // CHỈ dành cho cat='R': A|C|E
    "ref_reason": "…",       // tùy chọn, lý do khi E
    "ante": "S003: Singapore", // bắt buộc có mã câu trừ khi ref='E'
    "conf": "high", "alt": null, "note": null } ] }
// Ellipsis: text=null, thêm gap_after + recovered; marker là điểm ⟦∅⟧.

// align.json
{ "pair": "P20", "alignments": [
  { "st_tie": "P20-EN-001", "tt_tie": "P20-VI-007",   // cùng referent!
    "outcome": "kept",        // kept|kept_unmarked|shifted|omitted
    "shift": null,            // "R>L" | "L>zero" | ...
    "note": "South Korea → Nam Triều Tiên (TT S005)" } ] }
// TT tie không được nhắc → outcome=added (phân biệt added-thật vs added-inventory trong note).
```

## 6. Bẫy đã gặp (và cách xử lý) — cập nhật sau 20 cặp + phân tích thủ công

| # | Bẫy | Hiện tượng | Xử lý |
| :--- | :--- | :--- | :--- |
| 1 | Pull-quote trùng lặp | đoạn quote hiển thị lặp lại trong PDF | exclude 1 bản, ghi log; chú ý bất đối xứng EN/VI |
| 2 | Hàng tiêu đề dính ô | span ngang qua 2 cột | exclude/strip_prefix trong CFG |
| 3 | Mảnh dấu tiếng Việt | "n ướ c" tách rời | nối span gap ≤ 1,5pt (trong extract_pairs) |
| 4 | Mất ký tự PDF | chữ biến mất → fuzzy match | `_fuzzy_find` trong build_appendix_md |
| 5 | occ rơi giữa từ | "he" khớp vào "the" | fix_tie_occ (word-boundary) |
| 6 | Đoạn con/headline | không có liên kết | không gán nhãn, vẫn hiện raw |
| 7 | Thiếu space nguồn | "hợp lệ.Thông" → 2 câu dính thành 1 đơn vị (P20: byline bị hút vào lede) | rà mọi dấu chấm không space trước khi chốt seg; ghi vào phân tích cặp |
| 8 | Notes copy-paste | summary.md viện dẫn đơn vị không tồn tại (20/20 lần kiểm chỉ ~1 lần trùng thật, và trùng cũng sai vị trí) | mọi ghi chú phủ định phải kiểm tra nguyên văn (rg) trước khi dùng; Notes phải viết từ phân tích cặp |
| 9 | **Align zip vị trí** | link kept ghép theo thứ tự xuất hiện: "South Korea → Hoa Kỳ", "pirates → trừng phạt" (P19, P20) | align chỉ từ bản đồ câu + referent; cổng bước 13 (đọc cặp link phải hợp nghĩa) |
| 10 | **Cờ omitted nhầm tầng ID** | ghi "EN S038–S043 unrendered" rồi đánh omitted vào tie EN-038/039 (nằm ở S022–S023 **có dịch**) | omitted gắn cho TIE nằm trong câu bỏ (dùng bản đồ câu), không gắn theo mã câu |
| 11 | **Số trùng ngẫu nhiên tạo ảo giác** | P20: align kept 41/omitted 19 trùng đúng số câu 41/19 dù link sai hoàn toàn | không tin số trùng khi link chưa qua cổng ngữ nghĩa; báo cáo luôn cả 2 tầng (câu và tie) |
| 12 | Bất đối xứng inventory | EN "the U.S." lần 2 không đánh dấu, VI "Hoa Kỳ" lần 2 đánh dấu → "added" giả | phân biệt added-thật vs added-inventory trong align; không sửa inventory đã chốt |
| 13 | Đối xứng EN–VI về đại từ | VI thêm/bớt đại từ trích dẫn so EN | ghi nhận trong phân tích + audit, không sửa inventory khi đã chốt số liệu |
| 14 | ADDED_NOTES copy-paste | note align nhắc chuỗi "công nghệ" ở cặp không có công nghệ | note align viết riêng cho từng cặp từ phân tích B |

## 7. Audit checklist (làm lại mỗi vòng)

1. Dump toàn bộ R tie kèm ngữ cảnh → soát tay A/C/E (script mẫu: `audit_dump_r.py`).
2. Audit tự động: taxonomy `sub`, từ điển liên từ EN/VI, hình thái ellipsis, phân bố conf (script mẫu: `auto_audit.py`; output `out/audit/`).
3. Soát mọi tie conf=low (bridging) — liệt kê, không xoá.
4. Quét bất đối xứng EN–VI: đại từ ngôi 1/2 + deictic (we/you/us/our/chúng ta/bạn/here/này…) đối chiếu trạng thái đánh dấu hai bên.
5. **Cổng align ngữ nghĩa (bước 13)** với từng cặp — mới, cho toàn bộ 20 cặp.
6. Render lại + kiểm coverage 100% + QC PASS + soát ngẫu nhiên tooltip/chữ mũ ở cả 3 định dạng.
7. **Đối chiếu số đếm pipeline ↔ phân tích tay** từng cặp (bảng §9 của mỗi bản phân tích): chênh lệch >20% ở danh mục nào thì danh mục đó phải rà lại.

## 8. Cấu trúc thư mục

```
upload/            PDF + md gốc (input, không sửa)
scripts/           toàn bộ pipeline (thứ tự ở §4)
  align_tables/    căn cặp thủ công từng pair (bước 12 — phải qua cổng 13)
  tie_tables/      bảng tie thủ công từng pair (bước 10)
out/raw_pairs/     trích thô
out/pairs/PXX/     ST/TT.txt, seg, ties, align, highlighted.md, PXX.html, qc.txt, summary.md
out/appendix1/     Appendix1.{md,html,docx}, IR, match_stats
out/appendix2/     báo cáo phát hiện + stats/shifts/spot_check CSV (cần dựng lại từ align đã sửa)
out/audit/         AUDIT.md, auto_checks, thống kê A/C/E
download/BDNC/     bản giao người dùng
download/BDNC/semantic_analysis/   ★ 20 bản phân tích thủ công từng cặp (Giai đoạn B) + INDEX.md
```

## 9. Số liệu tham chiếu (vòng này, để so khi tái lập)

- **Tầng tie (tin cậy):** tổng tie EN 1.605 / VI 1.391. R: 246/149 (A: 234/135, E: 12/14, C: 0/0). S: 0/0. Ellipsis: 1/0. C: 65/67. L: 1.293/1.175. L-sub chủ đạo: repetition (EN 1.240, VI 1.146). Marker coverage render: 100/100%. Tie conf=low: 76 (bridging).
- **Tầng câu (tin cậy khi có bản đồ):** vd P20 = 41 giữ / 19 bỏ / 3+byline tự sinh; P19 = 21↔21 1–1 + 1 câu VI tự sinh.
- **Tầng alignment (CHƯA tin cậy):** số liệu kept/omitted/added của vòng cũ mang tính tham khảo — phải dựng lại qua Giai đoạn D + cổng bước 13 trước khi dùng.

## 10. Hồ sơ 20 cặp (địa hình — kết quả của việc phân tích thủ công từng cặp)

| Cặp | Cấu hình | Độ phủ câu | Cảnh báo chính khi dùng |
|---|---|---|---|
| P01 | SBS | có lặp pull-quote; VI +1/−3 câu | ST lặp câu (pull-quote) |
| P02 | SBS | VI thêm thông tin Wiradjuri | tái cấu trúc tuyên bố |
| P03 | SBS | lệch nặng | số liệu đảng không khớp; câu gán sai người nói — không dùng cấp câu |
| P04 | SBS | gộp số liệu, bỏ khung dẫn ×2 | mất "Shriane said" |
| P05 | SBS | ~60% (14/24 khối) | số liệu khớp 100% — dùng được sau chuẩn hóa |
| P06 | SBS | cắt mạch "xu hướng" ~40% | số liệu khớp 100% |
| P07 | SBS | 100% (benchmark) | 2 cặp ngoặc rỗng "( )" hai đầu |
| P08 | SBS | ~85% | mâu thuẫn lãi suất (rate-lifting ↔ giảm) — kèm cảnh báo |
| P09 | SBS | cắt 3 khối | sai lệch ngữ nghĩa đậm nhất — không dùng cấp câu |
| P10 | SBS | lệch cấu trúc nặng nhất (EN lặp đoạn, VI mô-đun trùng P05) | không dùng so mật độ tuyệt đối |
| P11 | VOA→VOA (lần 1) | ~95% | ẩn dụ giữ 9/12 — hiệu ứng nhà xuất bản |
| P12 | VOA dek (micro 2 câu) | 50% | câu mở tự sinh có hedge — cờ micro-pair |
| P13 | Reuters→VOA | ~68% | mất hedge qua cắt khối 2018 |
| P14 | Reuters→VOA | ~100% | tít "tự ĐỘNG trục xuất" sai nghĩa |
| P15 | AP→VOA | ~70% | nghi version-mismatch — kiểm version trước kết luận nội dung |
| P16 | VOA→VOA (lần 2) | ~100% (benchmark) | quy chiếu tự sinh "thuộc hiệp hội này" |
| P17 | VOA→VOA (lần 3) | ~100% 22↔22 | đảo chiều "blamed for → quy cho" ở câu mở |
| P18 | VOA→VOA (lần 4) | ~100% | 3 lỗi biên tập nguồn VI (trùng ×2; 240.000 ngàn; S024 hỏng) |
| P19 | VOA→VOA (lần 5) | 100% 21↔21 | URL VI sai (thừa "s"); mất khung cáo buộc; thuật ngữ pháp lý |
| P20 | VOA→VOA (lần 6) | ~68% — thấp nhất nhánh VOA | 2 lỗi đọc thuật ngữ (IUU; switch off→thay đổi); truyền bê IIU; align pipeline hỏng nặng nhất |

Chi tiết từng cặp: `download/BDNC/semantic_analysis/Pair_XX/PXX_phan-tich-ngu-nghia.md` + `INDEX.md` (sổ cái quy luật B1–B28).

---

**Tóm lại luồng tái lập:** trích xuất (A) → **phân tích thủ công từng cặp (B: bản đồ câu, nhân vật, chuỗi, số liệu, lỗi nguồn, đếm tay)** → gán nhãn tie (C) → **căn cặp theo ngữ nghĩa + cổng kiểm link (D)** → lắp Appendix 1 (E) → thống kê + kiểm cuối (F). Không giai đoạn nào được bỏ qua; chất lượng marking thành phẩm bằng chất lượng phân tích thủ công đứng trước nó.
