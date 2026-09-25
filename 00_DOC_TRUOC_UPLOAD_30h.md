# CẬP NHẬT KHO → 30h · Fix "câu/đề rỗng" + vẽ lại hình dựng √2
**OB Đại số · 2026-09-25 · QC lại DS7_CH02_B07 theo phản hồi Giám đốc**

## VÌ SAO (2 lỗi thật, QC trước để lọt)
1. **Câu/đề bài RỖNG** ở B07 (Bài tập mẫu Dạng 4, Trả lời ngắn Câu 11/12…): toàn bộ chữ biến mất, chỉ còn dấu chấm cuối. Gốc: `toInline` trong template làm `flat(Infinity)` SAU khi map → khi câu chứa MẢNG LỒNG (AI Soạn viết `ABS('-7,5')` mà quên spread `...ABS(...)`), mảng lồng rơi thành CHUỖI TRẦN không qua `run()` → docx BỎ. **kiemMay và LibreOffice đều LỌT** (file vẫn well-formed) — đó là lý do lọt QC. Bài học: phải soi TEXT trong `<w:t>`, không tin render LibreOffice cho phần chữ.
2. **Hình dựng √2 (Hình 1) vô nghĩa**: bản `dung_can_hai` cũ vẽ hình vuông rời một góc, đường tròn vẽ riêng — đoạn ME trong hình vuông KHÔNG bằng bán kính đường tròn vẽ ra, tâm ghi "0". Nhìn "không ăn nhặp với bài".

## ĐÃ SỬA (2 file kho)
1. `hieuhoc_template.js` — `toInline()`: `flat(Infinity)` TRƯỚC rồi `run()` từng chuỗi. Mảng lồng nay render đúng; mảng phẳng y hệt cũ (test 4 ca đạt). **Chặn tận gốc** cho MỌI bài/môn — AI Soạn lỡ quên spread cũng không mất chữ nữa.
2. `hinh_daiso.py` — `dung_can_hai()`: vẽ lại đúng SGK Hình 2.3, 2 panel a)/b): a) hình vuông MNPQ đường chéo nét đứt + E; b) trục số gốc **O** (chữ), đường tròn nét đứt tâm O bán kính ME, điểm A. Xem DEMO_f1_dung_can_hai_MOI.png.

## KIỂM CHỨNG
- Rebuild B07: kiemMay=[] · [object Object]=0 · undefined=0 · oMath depth=1 · 141 dấu căn KHÔNG cái nào rỗng · text đầy đủ (đã soi `<w:t>`).
- toInline test: flat [a,OMML,b]→3 · nested [a,[|,x,|],b]→5 (fixed) · không hồi quy.
- Diff: PATCH_30h__toInline.diff, PATCH_30h__dung_can_hai.diff (mỗi cái nhỏ, additive).

## THẦY LÀM
1. **Upload đè GitHub** 3 file: `hieuhoc_template.js`, `hinh_daiso.py`, `00_KHO_VERSION.txt`.
2. Không cần nạp Project (file kho). Không đổi chữ ký hàm → không cần regen API_REFERENCE.

## ⚠️ ONE-WRITER
Kho GitHub đang ở **30g** (máy Hình/Lý/Hóa đã push tới đó). Bản này vá trên nền 30g, chỉ đụng 2 hàm (`toInline`, `dung_can_hai`) — KHÔNG đụng mạch Hình. Trước khi push: xác nhận máy khác không đang sửa 2 file này; nếu GitHub đã nhảy mốc > 30g, báo OB vá lại trên nền mới.
