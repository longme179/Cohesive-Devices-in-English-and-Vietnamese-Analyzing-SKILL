# BDNC Group 9 — Corpus linguistics deliverables

Cohesion annotation of 20 EN–VI parallel news pairs.
EN: Halliday & Hasan (1976) · VI: Trần Ngọc Thêm (2006) · 5 colour-coded categories:

| Màu | Ký hiệu | Danh mục |
| :--- | :--- | :--- |
| 🟨 vàng `#FFFF00` | R | Reference (tham chiếu) |
| 🟩 xanh lá `#00FF00` | S | Substitution (thay thế) |
| 🟦 xanh dương `#0000FF` | E | Ellipsis (lược bỏ, ∅ = vị trí trống) |
| 🟧 cam `#FF9900` | C | Conjunction (liên kết) |
| 🟪 tím `#9900FF` | L | Lexical cohesion (liên kết từ vựng) |

## Appendix 1 — bản v6 (2026-11): bổ sung thủ công toàn bộ S/E từ semantic_analysis

- **Thay đổi cốt lõi so với v5:** 20 bảng `tie_tables/PXX.py` được đọc lại cùng
  20 bản `BDNC/semantic_analysis/Pair_XX/PXX_phan-tich-ngu-nghia.md`; toàn bộ
  vị trí **phép thế (S)** và **phép tỉnh lược (E)** mà bản phân tích thủ công
  đã xác định được thêm tay vào bảng (không sinh bằng regex/script), gồm cả
  `[LC]` liên câu và `[TC]` trong câu. Kết quả: **184 tie mới** (EN 92 / VI 92),
  nâng tổng từ 2.996 lên **3.180** tie; 5 màu hiện đủ trên toàn bộ 20 cặp
  (trước đây S = 0, E = 1 ở EN và 0 ở VI).
- **Số mới:** EN 1.697 (R 243 · S 21 · E 75 · C 65 · L 1.293) / VI 1.483
  (R 149 · S 3 · E 89 · C 67 · L 1.175). Marker coverage **3.180/3.180 (100%)**,
  0 straddle / 0 orphan / 0 deferred; `render.py` PASS 40/40.
- **Định dạng:** 2 cột EN|VI, marker 5 màu + mũ A/C/E trên Reference; **đã bỏ
  toàn bộ tag kết quả căn cặp (→ » ~ × +) và bảng chú giải 7 kết quả**. Mỗi
  khối S/E mới có comment Word ghi id, danh mục, `[LC]/[TC]`, tiền trạm,
  phần bù `{…}` và ghi chú.
- **File:** `BDNC/Appendix1.{md,html,docx,pdf}` (bản chuẩn hiện hành);
  `out/appendix1/Appendix1.*` là bản artifact tương ứng. PDF 112 trang,
  xuất từ HTML bằng WeasyPrint; DOCX 3.180 comment.

## Appendix 1 — highlighted parallel texts (v3.1, đa màu + hướng tham chiếu A/C/E)

- `BDNC/Appendix1.html` — bản tương tác vòng v3.1: 20 bảng 2 cột EN|VI,
  highlight 5 màu, rê chuột lên mỗi đoạn đánh dấu để xem chi tiết (danh mục,
  hướng quy chiếu, tiền trạm, độ tin cậy).
- `BDNC/Appendix1.md` — bản Markdown tham chiếu vòng v3.1 (GitHub lọc `style`
  inline nên màu có thể không hiển thị trên GitHub; mở bằng editor hỗ trợ
  HTML inline).

**Mới v3.1:** mỗi khối R kèm chữ mũ hướng quy chiếu — <sup>A</sup> = anaphoric
(234 EN + 135 VI), <sup>C</sup> = cataphoric (0), <sup>E</sup> = exophoric
(12 EN + 14 VI: chuỗi authorial “we/chúng ta” ở P07 và “bạn” hướng độc giả ở
P09-VI). Trang đầu mỗi định dạng có bảng đối chiếu khung lý thuyết
Halliday & Hasan (1976) ↔ Trần Ngọc Thêm (2006).

Độ phủ bản v6: **3180/3180 tie đã render (EN 1697 + VI 1483, 100%)**,
0 straddle / 0 orphan / 0 deferred (xem `out/appendix1/match_stats.json`).
Số 2.996 của v3.1/v5 là tầng R/C/L liên-câu trước khi bổ sung S/E thủ công.

## Appendix 1 — bản TÔ LẠI theo align v2 (v5, LỊCH SỬ — v7 đã bỏ tag kết quả)

- `BDNC/Appendix1.docx` / `.pdf` — **bản v5 lịch sử** (v7 hiện hành đã bỏ tag), dựng lại từ bảng
  align v2 (đã qua cổng kiểm 13): giữ nguyên định dạng 2 cột E–V mỗi cặp như
  vòng trước (20 bảng, header EN|VI kèm link nguồn, lặp header khi sang trang)
  và toàn bộ marking 5 màu + chữ mũ A/C/E (đối chiếu ký tự với bản cũ: 606/606
  hàng bảng pair giống hệt sau khi bỏ các run mũ), CỘNG THÊM:
  - **annotation kết quả căn cặp** dạng mũ nhỏ màu ngay sau mỗi khối đánh dấu
    (→ giữ · » dịch chuyển · ~ giữ-không-đánh-dấu · × bỏ—khối cắt/vi-lược ·
    + thêm—tự sinh/bất đối xứng kiểm kê) — 2996 tag, tổng khớp đúng từng loại
    với `out/align_v2/` (EN 1605 = giữ 1097 + dịch chuyển 28 + giữ-không-đd
    176 + bỏ 304; VI 1391 = giữ 1058 + dịch chuyển 25 + thêm 308);
  - **comment Word trên TỪNG khối đánh dấu** (2.996 comment, tác giả
    “BDNC Group 9”): id tie, danh mục/loại phụ, hướng quy chiếu A/C/E, tiền
    trạm, độ tin cậy, kết quả căn cặp + đối tác EN/VI (điểm gộp liệt kê đủ
    các tie EN), ghi chú — rê chuột hoặc mở Review → Comments;
  - trên khối VI là điểm gộp của nhiều tie EN: ưu tiên hiển thị → (giữ),
    danh sách đầy đủ trong comment;
  - trang đầu có thêm bảng chú giải 7 kết quả căn cặp (màu + ý nghĩa).
- PDF (48 trang) xuất từ docx qua LibreOffice; comment chỉ hiển thị trong
  Word/LibreOffice, không in ra PDF.
- Pipeline: `scripts/rebuild/export_appendix1_v2.py` (IR marking tầng tin cậy
  + align v2 + tie tables → docx; QC inbuilt: đếm màu/run mũ/comment).

## Appendix 1 — bảng align dựng lại theo giao thức mới (v4)

- `BDNC/Appendix1_Align.docx` / `.pdf` — **bản dựng lại Giai đoạn D**: marking
  chuẩn như Appendix 1 (5 màu + chữ mũ A/C/E trên Reference) **+ annotation
  kết quả căn cặp** ngay sau mỗi khối đánh dấu (mũ nhỏ: → giữ · » dịch chuyển
  · ~ giữ-không-đánh-dấu · × bỏ · + thêm), kèm **bảng căn cặp chi tiết từng
  tie** (tiền trạm, kết quả có màu, ghi chú) cho cả 20 cặp và **bảng tổng hợp
  20 cặp** ở đầu.
- Bảng align được dựng từ **bản đồ câu** của 20 bản phân tích thủ công
  (`BDNC/semantic_analysis/`), không phải ghép thứ tự; đã qua **cổng kiểm 13**
  toàn bộ (0 lỗi): tổng giữ + dịch chuyển + giữ-không-đd + bỏ = 1605 ST tie;
  cờ bỏ gắn theo tie trong câu không dịch (không theo mã câu); link chỉ nhận
  khi câu VI nằm trong bản đồ câu của câu EN.
- Số liệu v4 (tin cậy, thay cho thống kê align cũ): giữ 1097 · dịch chuyển 28
  · giữ-không-đánh-dấu 176 · bỏ-khối-cắt 201 · bỏ-vi-lược 103 · thêm-thật 48
  · thêm-bất-đối-xứng-kiểm-kê 260. Đối chiếu độc lập với phân tích tay:
  P20 = 80 giữ / 40 bỏ / 4 thêm-thật (khớp chính xác §8.6); P12, P13, P16–P19
  khớp; P03 (biên tập lại) và P15 (đảo khối) dùng kèm cảnh báo.
- Dữ liệu: `out/align_v2/PXX_sent_map.json` (bản đồ câu) +
  `out/align_v2/PXX_align_v2.json` (align v2); pipeline:
  `scripts/rebuild/{sent_map,finalize_sent_maps,rebuild_align,export_align_docx}.py`.

## Appendix 2 — findings report

- `BDNC/Appendix2.md` — báo cáo phát hiện (A2.1–A2.7), kiểm định 5 tuyên bố
  ở mục 4 của PDF.
- `BDNC/stats.csv`, `BDNC/shifts.csv`, `BDNC/spot_check.csv` — dữ liệu định lượng.

## Pipeline (repo)

`scripts/` — extraction → segmentation → annotation → alignment → rendering:
`build_appendix_md.py` (md + html + IR), `export_docx.py` (docx).
Working tree: `out/pairs/P01–P20/` (ST/TT texts, segments, tie tables,
alignment, QC); `out/appendix1/` (final artefacts); `out/audit/` (audit v3.1).

Muốn tái lập với 20 cặp bài báo khác: đọc **`REPLICATION_GUIDE.md`** ở gốc repo
(quy ước gán nhãn, 8 bước pipeline, schema dữ liệu, bẫy đã gặp, audit checklist).
