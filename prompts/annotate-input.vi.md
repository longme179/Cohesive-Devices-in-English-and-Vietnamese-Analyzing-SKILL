# Prompt mẫu — dán vào agent, đính kèm file markdown 2 cột

> **Cách dùng:** mở chat với agent, đính kèm file `.md` đã chia 2 cột EN|VI,
> copy nguyên khối trong “Prompt copy-paste” dưới đây, thay
> `[TÊN_FILE_ĐÍNH_KÈM]` bằng tên file, rồi gửi. Không cần viết thêm gì.

---

## Prompt copy-paste

```text
Bạn đang ở repo skill COHESION EN–VI (thư mục repo đã clone, nơi có SKILL.md).

File đính kèm: [TÊN_FILE_ĐÍNH_KÈM] — bảng markdown 2 cột EN | VI.

Hãy thực hiện toàn bộ quy trình trong SKILL.md và giao cho tôi Appendix 1
hoàn chỉnh (DOCX + PDF). Không hỏi lại nếu file đọc được; chỉ hỏi nếu file
không mở được hoặc không có bảng 2 cột.

YÊU CẦU BẮT BUỘC

1. Đọc trước: SKILL.md, templates/analysis_template.md,
   templates/tie_table_template.md, README.md.
2. Không sửa file input. Nếu input là PDF, chuyển sang markdown bằng
   `python -m pipeline.pdf_to_md`, đọc và sửa lỗi bóc tách (merge cell,
   xuống dòng, thiếu dấu cách) trước khi phân tích. Nếu input là markdown,
   dùng trực tiếp.
3. Chạy:
   python -m pipeline.ingest --input <file> --work work
   python -m pipeline.segment --work work
4. Với TỪNG cặp, làm đúng thứ tự:
   a. Đọc EN + VI + sentence map; hiểu nội dung, thể loại, tiền trạm.
   b. Viết work/analysis/PXX_semantic.md đủ 9 mục theo template, nêu rõ
      [LC] liên câu và [TC] trong câu.
   c. Viết tay work/tie_tables/PXX.py (13 trường): text/gap_after nguyên văn,
      ante có mã câu, level LC/TC, và với R phải tự quyết ref A/C/E.
   d. Chạy:
      python -m pipeline.annotate --work work --pair PXX
      python -m pipeline.render   --work work --pair PXX
      đến khi cả EN và VI đều PASS.
5. Build và xuất:
   python -m pipeline.build_appendix --work work --out out/appendix1
   .venv/bin/python -m pipeline.export_docx --out out/appendix1
   .venv/bin/python -m pipeline.export_pdf  --out out/appendix1
   python -m pipeline.validate --work work --out out/appendix1
   Nếu thiếu python-docx/WeasyPrint: tạo .venv và cài requirements.txt.
6. Kiểm tra trực quan file PDF/DOCX: đủ 5 màu, ∅ nền xanh, mũ A/C/E trên
   Reference, không có tag → » ~ × +, không tràn lề.

QUY TẮC KHÔNG ĐƯỢC VI PHẠM

- Trọng tâm là COHESION BEYOND THE SENTENCE LEVEL (Halliday & Hasan 1976
  vs Trần Ngọc Thêm 2006). [LC] là đơn vị chính; [TC] chỉ là lớp bổ sung S/E.
- KHÔNG sinh tie bằng regex, danh sách đại từ/từ nối, đếm từ trùng, so khớp
  chuỗi hay vòng lặp. Mọi dòng tie do bạn đọc ngữ cảnh rồi viết tay.
- KHÔNG mặc định ref="A"; mỗi R phải có quyết định A/C/E.
- KHÔNG bịa ∅ nếu bản dịch đã lấp đầy chỗ trống; pro-form thay thế ghi S.
- KHÔNG thêm tie không có trong analysis; không copy tie từ cặp khác.
- KHÔNG bỏ qua phân tích thủ công để chạy nhanh. Chất lượng > tốc độ.
- Nếu có nhiều cặp: làm tuần tự từng cặp. Nếu chạy song song, mỗi agent một
  cặp, tất cả dùng cùng quy ước.

TRẢ LỜI CUỐI

- Bảng: cặp, số tie EN/VI, coverage, QC.
- Đường dẫn: out/appendix1/Appendix1.docx, .pdf, .md, .html.
- Các mục [TD]/chỗ chưa render và mọi cảnh báo dữ liệu nguồn.
```

---

## Bản ngắn (nếu agent đã quen repo)

```text
Đính kèm là file markdown 2 cột EN|VI. Hãy đọc SKILL.md và chạy toàn bộ
pipeline manual-first: ingest → segment → với từng cặp viết analysis 9 mục +
tie table 13 trường bằng tay → annotate/render PASS → build_appendix →
export DOCX/PDF → validate. Không dùng regex/word list để sinh tie, không
mặc định ref, không bịa ∅. Xuất out/appendix1/Appendix1.docx + .pdf và báo
lại số tie/coverage/QC.
```

---

## Ghi chú

- Prompt giả định agent có quyền chạy shell trong repo. Nếu agent chỉ đọc file,
  nó vẫn phải làm bước phân tích thủ công và có thể đưa tie table cho người
  dùng chạy.
- Với input nhiều cặp, thời gian chạy phụ thuộc số cặp và độ dài; không nên
  yêu cầu “làm nhanh” vì khâu đọc là khâu chính.
- Nếu file PDF là bản scan hoặc bảng quá phức tạp, agent phải nói rõ cần
  transcribe tay; không được phân tích text bóc tách sai.
