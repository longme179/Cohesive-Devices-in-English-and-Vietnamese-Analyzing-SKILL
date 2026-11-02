# BDNC Group 9 — Corpus linguistics deliverables

Cohesion annotation of 20 EN–VI parallel news pairs.
EN: Halliday & Hasan (1976) · VI: Trần Ngọc Thêm (2006) · 5 colour-coded categories:

| Màu | Ký hiệu | Danh mục |
| :--- | :--- | :--- |
| 🟨 vàng | R | Reference (tham chiếu) |
| 🟩 xanh lá | S | Substitution (thay thế) |
| 🟦 xanh dương | E | Ellipsis (lược bỏ, ∅ = vị trí trống) |
| 🟧 cam | C | Conjunction (liên kết) |
| 🟪 tím | L | Lexical cohesion (liên kết từ vựng) |

## Appendix 1 — highlighted parallel texts (v3.1, đa màu + hướng tham chiếu A/C/E)

- `BDNC/Appendix1.html` — **bản đầy đủ nhất**: 20 bảng 2 cột EN|VI, highlight 5 màu,
  rê chuột lên mỗi đoạn đánh dấu để xem chi tiết (danh mục, hướng quy chiếu,
  tiền trạm, độ tin cậy).
- `BDNC/Appendix1.docx` — bản Word in ấn/offline: cùng thang màu 5 danh mục
  (shading từng run), header EN|VI kèm link nguồn, lặp header khi sang trang.
- `BDNC/Appendix1.pdf` — bản PDF đặt lên trên của file Word (dễ xem nhanh).
- `BDNC/Appendix1.md` — bản Markdown tham chiếu (GitHub lọc `style` inline nên
  màu có thể không hiển thị trên GitHub; mở bằng editor hỗ trợ HTML inline).

**Mới v3.1:** mỗi khối R kèm chữ mũ hướng quy chiếu — <sup>A</sup> = anaphoric
(234 EN + 135 VI), <sup>C</sup> = cataphoric (0), <sup>E</sup> = exophoric
(12 EN + 14 VI: chuỗi authorial “we/chúng ta” ở P07 và “bạn” hướng độc giả ở
P09-VI). Trang đầu mỗi định dạng có bảng đối chiếu khung lý thuyết
Halliday & Hasan (1976) ↔ Trần Ngọc Thêm (2006).

Độ phủ: **2996/2996 liên kết liên-câu đã render (EN 1605 + VI 1391, 100%)**,
0 straddle / 0 orphan / 0 deferred (xem `out/appendix1/match_stats.json`).

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
