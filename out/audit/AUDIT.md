# BÁO CÁO AUDIT NỘI DUNG — PHỤ LỤC 1 (bản v3.1, có A/C/E)

**Ngày audit:** 2026-11-02 · **Phạm vi:** 20 cặp bài báo EN–VI · **Đơn vị:** liên kết liên-câu (intersentential ties)

**Tổng số tie:** 2.996 (EN 1.605 / VI 1.391) — *không thay đổi so với bản v3* (audit không thêm/bớt tie, chỉ gắn nhãn hướng quy chiếu và đính chính 2 lỗi dữ liệu).

---

## 1. Khung lý thuyết đã đối chiếu

| Ký hiệu | EN — Halliday & Hasan (1976) | VI — Trần Ngọc Thêm (2006) |
| :--- | :--- | :--- |
| R | reference (personal, demonstrative, comparative, quantified) | phép thế đại từ (đại từ / chỉ từ) — cùng nhóm với S |
| S | substitution (nominal, verbal, clausal) | phép thế đại từ (phần thế danh từ / động từ / mệnh đề) |
| E | ellipsis | phép tỉnh lược |
| C | conjunction (adversative, additive, temporal, causal) | phép nối |
| L | lexical cohesion (repetition, synonymy, antonymy, collocation) | phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng |

Đối chiếu gần đúng giữa hai khung: **phép thế đại từ ≈ reference + substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ conjunction; phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng ≈ lexical cohesion.** Bảng này đã được đưa vào trang đầu của cả ba file Appendix1 (.md/.html/.docx).

## 2. Cập nhật mới: hướng quy chiếu A/C/E cho tham chiếu (R)

Mỗi khối R trong phụ lục giờ kèm **chữ mũ**: `Rᴬ` (anaphoric), `Rᶜ` (cataphoric), `Rᴱ` (exophoric). Tooltip (bản HTML) hiển thị đủ "dir: anaphoric/cataphoric/exophoric".

### 2.1. Quy tắc vận hành (để bảo đảm tính tái lập)

- **A — anaphoric (hồi quy):** tiền trạm truy xuất được từ văn bản đứng trước: thực thể đã nêu, mệnh đề/định nghĩa trước đó, hoặc *attribution của người được trích dẫn nằm ở câu trước* (ví dụ: “Chúng tôi đã triển khai BetStop…” ← thủ tướng được nêu tên ở câu trước).
- **C — cataphoric (tiến chỉ):** tiền trạm nằm ở câu sau. **Không có trường hợp nào trong ngữ liệu** — kết quả này phù hợp với nhận định của Halliday & Hasan rằng cataphora hiếm gặp và chủ yếu hoạt động nội câu; ở register tin tức, hầu như mọi tham chiếu liên câu đều hồi quy.
- **E — exophoric (ngoại văn bản):** tiền trạm nằm ngoài văn bản, trong bối cảnh phát ngôn: (i) đại từ ngôi thứ nhất *authorial/generic* (người viết + độc giả, “we Aussies”); (ii) đại từ ngôi thứ hai hướng độc giả (bạn/you). Riêng với tie E, trường `ante` chỉ mang tính thông tin (mỏi chuỗi hoặc mô tả bối cảnh), không bắt buộc có mã câu Sxxx.

### 2.2. Kết quả phân loại (395 R tie)

| Hướng | EN | VI | Cộng | Ghi chú |
| :--- | ---: | ---: | ---: | :--- |
| A (anaphoric) | 234 | 135 | 369 | mặc định của register tin tức |
| C (cataphoric) | 0 | 0 | 0 | không có ở cấp độ liên-câu |
| E (exophoric) | 12 | 14 | 26 | xem chi tiết dưới |
| **Cộng (R)** | **246** | **149** | **395** | |

**26 tie E gồm:** P07 (bài feature tiếng Anh về Australian English): chuỗi *authorial we/us/our/my/I* (12 tie EN) và chuỗi dịch *chúng ta/ta/tôi/của chúng ta* (13 tie VI) — người viết không được nêu tên, referent = “chúng ta (tác giả + độc giả)”; P09-VI-025 *bạn* (S009) — địa chỉ hoá độc giả trong phần trích mô tả của Cleanbill.

## 3. Phát hiện và đính chính trong audit

### 3.1. Đính chính dữ liệu (đã áp dụng)

1. **P09-VI-025** (*bạn*, S009): `ante` cũ = “S008: bạn (the reader addressed)” — **sai**, vì S008 không chứa “bạn” (lỗi thoát QC gate cũ do chuỗi ante có mã S). Đã sửa thành “ngoài văn bản: người đọc (bối cảnh phát ngôn)” và gắn `ref: E`.
2. **P20-VI-017** (*chúng tôi*, S012): `ante` cũ = “S011: Chúng ta” (chuỗi của ông Trent) — **sai referent**: “chúng tôi” nằm trong trích dẫn gián tiếp của **Ủy hội Âu châu** (“Những gì các ông làm không thỏa mãn chúng tôi”). Đã sửa ante thành “S011: Ủy hội Âu châu (lời trích dẫn gián tiếp trong câu Trent)”. Hướng: A.
3. **render.py QC gate (d)** cập nhật: tie R với `ref='E'` được miễn yêu cầu ante phải chứa mã câu; bổ sung **gate (f)**: mọi tie R phải có `ref ∈ {A, C, E}`; qc.txt in thêm phân bố hướng.

### 3.2. Kiểm tra tự động (toàn bộ 2.996 tie)

- **Danh mục C (liên từ):** 100% item là liên từ/cụm từ nối hợp lệ. 10 item nằm ngoài từ điển thu gọn đều là liên từ đúng: *additionally, on the contrary, to top it off* (EN); *bên cạnh, hiện tại, kể từ đó, nói cách khác, riêng, thứ nhất, đầu tuần này* (VI). Phân bố: EN — adversative 27, additive 30, temporal 4, causal 4; VI — adversative 30, additive 32, temporal 4, causal 1.
- **Taxonomy `sub`:** R ⊆ {personal, demonstrative, comparative, quantified}; L ⊆ {repetition, synonym, collocation, general word, superordinate, …}; E (ellipsis) có đủ gap_after + recovered. Không vi phạm.
- **Số liệu đặc trưng register:** S (substitution) = 0; E (ellipsis) = 1 (P07-EN-004: đáp lời “Who’s a ‘mate’?” — ∅ = *a mate*). Lexical cohesion chiếm áp đảo: EN 1.293/1.605 (80,4%), VI 1.175/1.391 (84,5%), trong đó *repetition* là chủ đạo (EN 1.240, VI 1.146) — tương thích với trọng tâm *phép lặp* trong hệ thống của Trần Ngọc Thêm.

### 3.3. 76 tie conf=low

Chủ yếu là **bridging** (đề cập lần đầu của thực thể hàm ý trong bối cảnh, ví dụ “the announcement” sau “has said”; “Luật sư” trong bài viết về vụ bắt giữ; “Hoa Kỳ” nêu lần đầu). Nguyên tắc ban đầu giữ nguyên (tính cả hai bên đều có, tương đối đối xứng: EN 37, VI 39). **Khuyến nghị:** khi báo cáo kết quả quantitative nên kèm phân tích độ nhạy (tổng số có/loại nhóm conf=low).

### 3.4. Bất đối xứng EN–VI phát hiện (ghi nhận, không sửa)

| Vị trí | EN | VI | Ghi chú |
| :--- | :--- | :--- | :--- |
| P09 S008/S009 | “you” ×2 không đánh dấu | “bạn” đánh dấu (R-E) | cùng hiện tượng, hai cách xử lý |
| P02 S016–S029 | “we” đánh dấu (4 tie, attribution trước) | “chúng ta” không đánh dấu (dịch giả dùng generic) | khác nhau do lựa chọn từ của bản dịch |
| P16 S008 | “we” không đánh dấu (attribution sau trích dẫn) | “chúng tôi” đánh dấu (Bà Suladda nêu ở S005) | VI nêu tên người nói trước |
| P20 S010/S012 | “us” không đánh dấu | “chúng tôi” đánh dấu | trích dẫn gián tiếp |
| P04, P05, P06, P10 | we/you authorial-generic không đánh dấu | bạn/chúng ta tương ứng không đánh dấu | **nhất quán hai bên** |

Nguyên nhân gốc: ranh giới giữa “đại từ trong trích dẫn có attribution” (đánh dấu được) và “đại từ authorial/generic” (theo H&H không tạo liên kết nội văn bản) chưa được luật hoá tuyệt đối ở vòng gán nhãn trước. **Khuyến nghị cho vòng sau:** (i) luật thống nhất — mọi đại từ ngôi 1/2 trong trích dẫn có attribution ở câu trước đều đánh dấu; mọi đại từ authorial/generic đều đánh dấu kèm nhãn E; (ii) quyết định rõ việc thêm tie EN cho P09 “you” nếu muốn đối xứng tuyệt đối (hiện không thêm để giữ nguyên inventory và các số liệu Appendix 2).

## 4. Kiểm tra render sau cập nhật

- QC 40/40 (20 pair × 2 phía) **PASS**, kể cả gate (f) mới.
- Marker coverage: **EN 1.605/1.605 (100%), VI 1.391/1.391 (100%)**; straddle 0, orphan 0.
- Chữ mũ A/C/E: MD 395 trong văn bản (369 A + 26 E; 0 C); HTML 395 + tooltip đầy đủ; DOCX 395 superscript run (369 A + 26 E). Riêng legend giải thích có thêm các chữ mũ minh hoạ.
- Trang đầu cả ba định dạng đều có: chú giải màu, chú thích hướng A/C/E, bảng đối chiếu khung H&H ↔ TNT.

## 5. Kết luận

**AUDIT: ĐẠT.** Nội dung annotation nhất quán với hai khung lý thuyết theo bảng đối chiếu; việc tách A/C/E đã được hiện thực hoá trong cả ba định dạng phụ lục; hai lỗi dữ liệu (`ante` của P09-VI-025, P20-VI-017) đã đính chính; các điểm cần lưu ý (conf=low, bất đối xứng EN–VI nhỏ) đã được định lượng kèm khuyến nghị. Không thay đổi tổng số tie — các số liệu trong Appendix 2 vẫn hợp lệ.
