# Quy ước bổ sung S / E thủ công vào tie table

Mục tiêu: đưa **các vị trí phép thế (S) và phép tỉnh lược (E) đã được con người
phân tích trong `download/BDNC/semantic_analysis/Pair_XX/PXX_phan-tich-ngu-nghia.md`**
vào bảng gán nhãn, để Appendix 1 có đủ 5 màu thay vì chỉ R/C/L.

## Nguyên tắc bất di bất dịch

- Người đọc bản phân tích + đọc câu gốc rồi **quyết định** tie. Không dùng regex,
  danh sách từ, đếm chuỗi, vòng lặp hay script để sinh tie.
- `scripts/find_quote.py` chỉ là công cụ **định vị** chuỗi người đã chọn:
  `python3 scripts/find_quote.py P01 TT "đưa nước qua"`.
- Không sửa các tie cũ (R/C/L) trừ khi chúng che mất một tie mới (QC overlap).
  Thêm dòng mới vào **cuối** list `ST` / `TT` để ID cũ không đổi.
- Mỗi dòng ứng với **một mục trong bảng phân tích** (§2 cho E, §3 cho S). Nếu
  mục đó gộp nhiều chỗ trống, chọn chỗ trống đầu tiên làm marker và ghi rõ các
  chỗ còn lại trong `note`. Không tự thêm mục không có trong phân tích.
- Bỏ qua mục `[TD]` (tiêu đề) vì tiêu đề chưa được render trong bảng Appendix1;
  ghi lại trong báo cáo.
- Nếu phân tích ghi "biên" nhưng vẫn xác định là tỉnh lược/thế thật, thêm với
  `conf='low'` và ghi "biên" trong note. Nếu phân tích kết luận không phải
  tỉnh lược/thế, không thêm.
- **Không bịa chỗ trống**: nếu phân tích nói phía ngôn ngữ đó đã *lấp đầy* chỗ
  trống bằng danh từ/trợ động từ (vd P19 "five more ∅" → "5 hãng máy bay",
  P20 nor-gap → "và cũng không được"), thì KHÔNG thêm E ở phía đó — bề mặt
  không có ∅. Nếu thay bằng pro-form (vd P14 "don't" → "không làm vậy"), thêm S.
  Ghi các trường hợp này vào báo cáo.

## Định dạng dòng

```python
# text tie (S):
('S005', 'those', 'S', 'nominal',
 'S004: the projects', 'high', None,
 '[TC] those ← the projects trong cùng câu', 1, None, None, 'TC'),

# ellipsis tie (E):
('S007', None, 'E', 'nominal',
 'S007: {nước} (trong câu)', 'high', None,
 '[TC] lược tân ngữ {nước} của “đưa … trở lại”', 1,
 'để có thể đưa', '{nước}', 'TC'),
```

Thứ tự 12 trường:
`sent, text, cat, sub, ante, conf, alt, note, occ, gap_after, recovered, level`

- `text=None` cho E; `gap_after` là **chuỗi con nguyên văn** kết thúc ngay trước
  chỗ trống; `recovered` là phần bù trong `{...}`.
- `occ`: 1 nếu `gap_after`/`text` chỉ xuất hiện một lần trong câu; nếu lặp, đếm
  đúng lần xuất hiện (1, 2, ...). `find_quote.py` in offset để kiểm.
- `level`: `'LC'` nếu bảng phân tích ghi `[LC]`; `'TC'` nếu `[TC]`; `'TD'` nếu
  `[TD]` (thường bỏ qua).
- `ante` phải chứa mã câu. Với `TC`, ghi `'Sxxx: ... (trong câu)'`.
- `sub` dùng các nhãn hiện có: `nominal`, `verbal`, `clausal`.

## Ví dụ chuẩn (P01, đã làm)

Xem cuối `scripts/tie_tables/P01.py`, khối
`# ---- S/E bổ sung thủ công từ semantic_analysis/Pair_01`.

## Kiểm tra bắt buộc

```bash
python3 scripts/annotate.py PXX
python3 scripts/render.py PXX
```

`render.py` phải in `PASS` cho cả EN và VI. Nếu FAIL:
- `occurrence ... not found`: chọn lại `gap_after`/`text` đúng nguyên văn.
- `overlap`: dịch marker sang một gap khác trong cùng mục, hoặc điều chỉnh
  `gap_after` để điểm rơi ra ngoài span cũ.
- `R tie without valid ref`: chạy lại `python3 scripts/annotate.py PXX` (script
  giữ `ref` cũ theo ID); không sửa tay R.

## Báo cáo cuối

Ghi rõ: số tie trước/sau theo cat; danh sách mục đã thêm (mã E-EN/E-VI/S-EN/S-VI);
mục bị bỏ và lý do; kết quả QC.
