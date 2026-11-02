# BDNC Group 9 — Gán nhãn liên kết ngôn bản EN–VI (20 cặp bài báo song song)

Corpus linguistics working session: annotation of grammatical cohesion over
20 English–Vietnamese parallel news pairs (2.996 intersentential ties).

- **EN** theo Halliday & Hasan (1976): reference · substitution · ellipsis ·
  conjunction · lexical cohesion.
- **VI** đối chiếu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh Tùng 2020):
  phép thế đại từ ≈ reference + substitution; phép tỉnh lược ≈ ellipsis;
  phép nối ≈ conjunction; phép lặp, phép đối, phép thế đồng nghĩa,
  phép liên tưởng ≈ lexical cohesion.
- Reference (R) được tách hướng quy chiếu: **A** anaphoric (369) ·
  **C** cataphoric (0) · **E** exophoric (26).

## Điểm bắt đầu

- **`REPLICATION_GUIDE.md`** — hướng dẫn tái lập toàn bộ quy trình với 20 cặp
  bài báo **khác** (quy ước gán nhãn, 8 bước pipeline, schema dữ liệu, bẫy đã
  gặp, audit checklist). Đây là tài liệu dành cho AI agent / người muốn replicate.
- `out/audit/AUDIT.md` — báo cáo audit nội dung v3.1 (phân loại A/C/E, đính
  chính dữ liệu, bất đối xứng EN–VI, khuyến nghị).
- `download/BDNC/` — sản phẩm giao: `Appendix1.{html,docx,pdf,md}` (phụ lục
  highlight 5 màu + chữ mũ A/C/E, 20 bảng 2 cột EN|VI), `Appendix2.md`
  (báo cáo phát hiện), `stats.csv`, `shifts.csv`, `spot_check.csv`,
  `audit_report.{md,docx}`.

## Cấu trúc

```
upload/      đầu vào (PDF song ngữ + markdown tham chiếu) — không sửa
scripts/     pipeline: extract → build_texts → segment → annotate → align
             → render (QC) → build_appendix_md → export_docx → stats
out/pairs/   P01–P20: văn bản chuẩn, câu, tie tables, alignment, QC, highlight
out/audit/   audit v3.1: dump R-tie, kiểm tra tự động, thống kê A/C/E
```

## Chỉ số chính (vòng hiện tại)

| Chỉ số | Giá trị |
| :--- | :--- |
| Tie liên-câu (EN / VI) | 1.605 / 1.391 |
| R (EN / VI) | 246 / 149 — A 234/135, E 12/14, C 0/0 |
| S · Ellipsis · C · L (EN) | 0 · 1 · 65 · 1.293 |
| S · Ellipsis · C · L (VI) | 0 · 0 · 67 · 1.175 |
| Marker coverage khi render | 100% (2.996/2.996), 0 straddle/orphan |
| QC từng pair | 40/40 PASS |
