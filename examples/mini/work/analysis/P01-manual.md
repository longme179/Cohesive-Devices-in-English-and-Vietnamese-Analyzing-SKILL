# P01 — Phân tích ngữ nghĩa liên kết (ví dụ mẫu)

**ST (EN):** City opens a new shelter as demand rises

**TT (VI):** Thành phố mở nơi trú ẩn mới khi nhu cầu tăng

## 1. Tổng quan nội dung, thể loại, bản đồ câu

Cặp tin ngắn 5 câu, trật tự 1–1. Chuỗi trường nghĩa: shelter / beds / demand.
Bản đồ câu: ST S001–S005 ↔ TT S001–S005.

| ST | TT | Ghi chú |
|---|---|---|
| S001 | S001 | mở nơi trú ẩn |
| S002 | S002 | số giường |
| S003 | S003 | nhu cầu cao |
| S004 | S004 | quan chức hứa bổ sung |
| S005 | S005 | một nơi đã đầy |

## 2. Phép tỉnh lược (ellipsis)

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-EN1 | S004 | “add more ∅” | lược danh từ {beds} sau “more” | [LC] |
| E-VI1 | S004 | “bổ sung thêm ∅” | lược danh từ {giường} | [LC] |

## 3. Phép thế (substitution)

| # | Ngôn ngữ | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| S-EN1 | EN | “One is already full” | One ← a new shelter (S001) | [LC] |

## 4. Phép quy chiếu (reference)

| # | EN | VI | Hướng | Tiền trạm |
|---|---|---|---|---|
| R-EN1 | It (S002) | — | A | S001: a new shelter |
| R-VI1 | Nơi này (S002) | — | A | S001: nơi trú ẩn |
| R-EN2 | they (S004) | họ (S004) | A | S004: Officials / Các quan chức (trong câu) |

## 5. Phép nối (conjunction)

| # | EN | VI | Kiểu |
|---|---|---|---|
| C-EN1 | But (S003) | Nhưng (S003) | adversative |

## 6. Liên kết từ vựng (lexical cohesion)

- EN: shelter → beds → demand; VI: nơi trú ẩn → giường → nhu cầu.
- Lặp “nơi” ở VI S005 liên kết với “nơi trú ẩn” S001.

## 7. Các dịch chuyển liên kết nổi bật

| Kiểu | Số lần | Ví dụ |
|---|---:|---|
| EN đại từ → VI danh ngữ demonstrative | 1 | It → Nơi này |
| EN đại từ trong câu → VI đại từ | 1 | they → họ |
| Tỉnh lược song song | 1 | add more ∅ ↔ bổ sung thêm ∅ |

## 8. Bất thường dữ liệu nguồn

Không có; đây là ví dụ tổng hợp để kiểm tra pipeline, không dùng làm bằng chứng
nghiên cứu thật.

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table

| Chỉ số | Đọc tay | Tie table |
|---|---:|---:|
| EN — R | 2 | 2 |
| EN — S | 1 | 1 |
| EN — E | 1 | 1 |
| EN — C | 1 | 1 |
| EN — L | 0 | 0 |
| VI — R | 2 | 2 |
| VI — S | 0 | 0 |
| VI — E | 1 | 1 |
| VI — C | 1 | 1 |
| VI — L | 1 | 1 |

**Kết luận:** ví dụ này chỉ để kiểm tra luồng ingest → segment → annotate →
render → appendix → docx/pdf; các quyết định tie vẫn do người đọc chọn.
