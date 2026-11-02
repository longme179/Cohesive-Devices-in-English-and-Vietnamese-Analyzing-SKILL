# HƯỚNG DẪN TÁI LẬP (REPLICATION GUIDE) — GÁN NHÃN LIÊN KẾT NGỮ PHÁP EN–VI

Tài liệu này giúp một AI agent (hoặc người) **tái lập toàn bộ quy trình** của repo này với **20 cặp bài báo khác**. Quy trình đã chạy end-to-end trên 20 cặp (2.996 tie, coverage render 100%, QC 40/40 PASS).

## 0. Tổng quan nhiệm vụ

Gán nhãn **quan hệ liên kết ngôn bản (cohesion)** trên cặp bài báo song song Anh–Việt:

- **Phía EN** theo Halliday & Hasan (1976), 5 phương tiện: reference, substitution, ellipsis, conjunction, lexical cohesion.
- **Phía VI** đối chiếu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh Tùng 2020): **phép thế đại từ ≈ reference + substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ conjunction; phép lặp + phép đối + phép thế đồng nghĩa + phép liên tưởng ≈ lexical cohesion.**
- Ký hiệu thống nhất 5 danh mục: `R S E C L` (R🟨 S🟩 E🟦 C🟧 L🟪).
- **Reference (R) tách hướng quy chiếu**: `A` = anaphoric, `C` = cataphoric, `E` = exophoric (hiển thị bằng chữ mũ trên khối đánh dấu).

### Quy ước gán nhãn (quan trọng — quyết định tính tái lập)

1. **Chỉ liên-câu (intersentential)**: item nằm ở câu N, tiền trạm ở câu M ≠ N (thường M < N). Liên kết nội câu không đánh dấu.
2. **Chỉ tô chính item** (từ/create mang chức năng liên kết), không tô cả danh ngữ chứa nó. "The" không tô khi đầu ngữ lặp lại từ khoá (rule 3 của pilot).
3. **Điều kiện tiên quyết (prerequisite)** — thực thể nêu lần đầu, deictic chưa neo trong văn bản — **không tô**, ghi vào `exclusions_log.json`.
4. **Một chuỗi nhiều từ trong cùng một câu chỉ tô một lần** (vd `my/me/us` cùng câu → 1 mark).
5. **Đại từ ngôi 1/2 trong trích dẫn**: nếu attribution (tên người nói) nằm ở **câu trước** → được phép gán nhãn (tiền trạm = attribution). Attribution cùng câu hoặc sau câu → không đủ điều kiện liên-câu.
6. **Hướng quy chiếu A/C/E**:
   - `A`: tiền trạm truy xuất được từ văn bản trước (thực thể/mệnh đề/attribution).
   - `C`: tiền trạm ở câu sau (trong ngữ liệu tin tức này = 0 trường hợp liên-câu).
   - `E`: tiền trạm ngoài văn bản (authorial/generic we-ta, bạn/you hướng độc giả). Với tie E, trường `ante` chỉ mang tính thông tin (mỏi chuỗi/mô tả bối cảnh), không bắt buộc mã câu.
7. `conf` ∈ {high, med, low}; bridging (đề cập lần đầu hàm ý) gán `low` và vẫn giữ trong inventory.

## 1. Môi trường

```bash
python3 (≥3.12 — f-string lồng cùng loại dấu nháy)
pip install pymupdf python-docx pyvi   # trích PDF, xuất DOCX, tokenize VI
pandoc, soffice (libreoffice)          # chuyển đổi báo cáo
```

## 2. Đầu vào kỳ vọng

- **PDF song ngữ 2 cột EN|VI** (`upload/Appendix 1 - 20 pairs of articles.pdf`): mỗi cặp = tiêu đề + link + bảng 2 cột song đoạn (mỗi hàng = một đoạn EN đối chiếu VI).
- Hoặc **markdown tham chiếu** (`upload/Appendix 1 - 20 pairs.md`): bảng `| EN | VI |` từng dòng, có link bài gốc — script `build_appendix_md.py` dùng file này làm khung bố cục của phụ lục cuối (PAIR_BOUNDARIES + URL_LINES là số dòng, **phải chỉnh lại cho ngữ liệu mới**).

## 3. Quy trình 8 bước

### Bước 1 — Trích PDF → raw pairs
`extract_pdf.py` → `extract_pairs.py` (v7): tách 2 cột theo toạ độ x (VI cell edge = min(vi_x0); EN edge = max(en_x1) trước vi_left+10), nối mảnh dấu tiếng Việt (gap ≤ 1.5pt), bỏ đoạn URL rời.
Output: `out/raw_pairs/PXX.json {en:[para...], vi:[para...]}`.
Chạy `flag_candidates.py` để rà tiêu đề phụ/chú ảnh (SHORT-NOEND, Photo/Credit…).

### Bước 2 — Dựng văn bản chuẩn
`build_texts.py`: áp `CFG` từng pair (exclude/strip_prefix/replace) → `ST.txt`, `TT.txt` (EN/VI), mọi thứ bị loại ghi vào `exclusions_log.json` kèm lý do. `meta.json` chứa title_en/title_vi.

### Bước 3 — Tách câu
`segment.py`: đánh số S001…, bảo vệ từ viết tắt/số (U.S., Mr., 1.5, TP.HCM…), "…" không tách. Câu ghi span (fa, fb) trong văn bản chuẩn. Sửa thủ công qua `PXX_seg_fixes.json`.
Output: `ST_seg.json`, `TT_seg.json`.

### Bước 4 — Gán nhãn (bước con người/AI)
Viết bảng tie tại `scripts/tie_tables/PXX.py` rồi chạy `annotate.py PXX`:
```python
# (sent, text, cat, sub, ante, conf, alt, note, occ)
('S004', 'it', 'R', 'personal', 'S003: Singapore', 'high', None, None, 3)
# tie R bắt buộc thêm: ref='A'|'C'|'E' (annotate.py sẽ tự điền 'A' nếu thiếu — cập nhật hàm nếu tái lập)
```
`annotate.py` **từ chối ghi** nếu occurrence của text không tồn tại trong câu. Sau đó `fix_tie_occ.py`/`fix_tie_occ_v2.py` sửa lỗi occ rơi giữa từ.

### Bước 5 — Căn cặp
`align.py PXX` → `align.json`: outcome mỗi ST tie = kept/shifted/omitted; TT tie không được nhắc → auto outcome=added.

### Bước 6 — Render + QC từng pair
`render.py PXX` sinh `ST/TT_highlighted.md` (ký hiệu trung gian emoji+⟦⟧), `PXX.html` (tooltip), `*_qc.txt`. **QC gates:**
- (a) text nằm đúng occurrence trong câu; (b) marker không chồng lấn; (c) bỏ marker → ra đúng .txt từng ký tự; (d) tiền trạm `ana` nằm trước (tie ref='E' được miễn); (e) in phân bố danh mục; (f) mọi R phải có ref ∈ {A,C,E}.

### Bước 7 — Lắp phụ lục
`build_appendix_md.py`: đối chiếu từng hàng bảng gốc ↔ văn bản đã đánh dấu (fuzzy match + repair), sinh `Appendix1.md` (span 5 màu inline CSS), `Appendix1.html` (2 cột + tooltip), `appendix1_segments.json` (IR), `match_stats.json`. Gate: **marker coverage phải = 100%** (rendered/markers), straddle/orphan = 0. Nếu thiếu: dùng `diagnose_missing.py PXX` để tìm hàng gán nhầm.

### Bước 8 — Xuất DOCX + thống kê
`export_docx.py` → `Appendix1.docx` (bảng 2 cột, tô màu run-level `w:shd`, chữ mũ A/C/E superscript). `stats.py` → `stats.csv`, `shifts.csv`, `spot_check.csv`. `summarize.py PXX` → `summary.md` + `progress.json`.

## 4. Schema dữ liệu lõi

```jsonc
// ST_ties.json / TT_ties.json
{ "pair": "P01", "lang": "EN", "ties": [
  { "id": "P01-EN-002", "sent": "S004", "text": "it", "occ": 3,
    "cat": "R",              // R|S|E|C|L
    "sub": "personal",       // R: personal|demonstrative|comparative|quantified
                             // C: adversative|additive|temporal|causal
                             // L: repetition|synonym|antonym|collocation|general word|superordinate...
    "dir": "ana",            // hướng của tiền trạm (ana|cata) — ref='E' thì miễn kiểm
    "ref": "A",              // CHỈ dành cho cat='R': A|C|E
    "ref_reason": "…",       // tùy chọn, lý do khi E
    "ante": "S003: Singapore", // bắt buộc có mã câu trừ khi ref='E'
    "conf": "high", "alt": null, "note": null } ] }
// Ellipsis: text=null, thêm gap_after + recovered; marker là điểm ⟦∅⟧.
```

## 5. Bẫy đã gặp (và cách xử lý)

| Bẫy | Hiện tượng | Xử lý |
| :--- | :--- | :--- |
| Pull-quote trùng lặp | đoạn quote hiển thị lặp lại trong PDF | exclude 1 bản, ghi log; chú ý bất đối xứng EN/VI |
| Hàng tiêu đề dính ô | span ngang qua 2 cột | exclude/strip_prefix trong CFG |
| Mảnh dấu tiếng Việt | "n ướ c" tách rời | nối span gap ≤ 1.5pt (đã trong extract_pairs) |
| Mất ký tự PDF | chữ biến mất → fuzzy match | `_fuzzy_find` trong build_appendix_md |
| occ rơi giữa từ | "he" khớp vào "the" | fix_tie_occ (word-boundary) |
| Đoạn con/headline | không có liên kết | không gán nhãn, vẫn hiện raw |
| Đối xứng EN–VI | VI thêm/bớt đại từ trích dẫn | ghi nhận trong audit, **không** sửa inventory khi đã chốt số liệu |

## 6. Audit checklist (làm lại mỗi vòng)

1. Dump toàn bộ R tie kèm ngữ cảnh → soát tay A/C/E (script mẫu: `audit_dump_r.py`).
2. Audit tự động: taxonomy `sub`, từ điển liên từ EN/VI, hình thái ellipsis, phân bố conf (script mẫu: `auto_audit.py`; output `out/audit/`).
3. Soát mọi tie conf=low (bridging) — liệt kê, không xoá.
4. Quét bất đối xứng EN–VI: đại từ ngôi 1/2 + deictic (we/you/us/our/chúng ta/bạn/here/này…) đối chiếu trạng thái đánh dấu hai bên.
5. Render lại + kiểm coverage 100% + QC PASS + soát ngẫu nhiên tooltip/chữ mũ ở cả 3 định dạng.

## 7. Cấu trúc thư mục

```
upload/            PDF + md gốc (input, không sửa)
scripts/           toàn bộ pipeline (thứ tự ở §3)
  align_tables/    căn cặp thủ công từng pair
  tie_tables/      bảng tie thủ công từng pair
out/raw_pairs/     trích thô
out/pairs/PXX/     ST/TT.txt, seg, ties, align, highlighted.md, PXX.html, qc.txt, summary.md
out/appendix1/     Appendix1.{md,html,docx}, IR, match_stats
out/appendix2/     báo cáo phát hiện + stats/shifts/spot_check CSV
out/audit/         AUDIT.md, auto_checks, thống kê A/C/E
download/BDNC/     bản giao người dùng
```

## 8. Số liệu tham chiếu (vòng này, để so khi tái lập)

- Tổng tie: EN 1.605, VI 1.391. R: 246/149 (A: 234/135, E: 12/14, C: 0/0). S: 0/0. Ellipsis: 1/0. C: 65/67. L: 1.293/1.175.
- L-sub chủ đạo: repetition (EN 1.240, VI 1.146) — nhất quán với *phép lặp* của TNT.
- Marker coverage render: 100/100%. Tie conf=low: 76 (bridging).
