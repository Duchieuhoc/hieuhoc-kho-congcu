# UPLOAD KHO — Chốt chặn tofu cho biểu đồ tranh (mốc giữ 2026-09-28, tag 31b)
> Thầy upload đè **2 file** dưới lên repo **Duchieuhoc/hieuhoc-kho-congcu** (web → Add file/Upload → Commit).
> Đều ở GỐC repo. Không xóa file nào khác. (Nối tiếp 31a — nếu chưa up 31a thì up cả bộ 31a trước.)

## File cần upload (2)
1. `bieudo_xstk.py`      — VÁ: `bieu_do_tranh()` kiểm glyph, thêm hằng `ICON_AN_TOAN`. **Tương thích ngược** (chữ ký không đổi).
2. `00_KHO_VERSION.txt`  — thêm entry [31b] ở đầu.

## Vì sao vá (phát hiện khi khai nghĩa B39)
- Biểu đồ tranh SGK dùng icon ô tô 🚗, sách 📕, người 👦, bóng ⚽… **Font hiện có (DejaVu Sans) KHÔNG có glyph các emoji này** → matplotlib vẽ ra **ô vuông ▯ câm**, build vẫn chạy nhưng hình HỎNG.
- Nay `bieu_do_tranh` **chặn trước**: gặp biểu tượng thiếu glyph → báo lỗi rõ, buộc dùng **bộ an toàn** `☺ ☹ ● ★ ✿ ✉ ☎ ◐`. AI Soạn không thể lỡ ship hình tofu.

## Nợ kho (cần thầy quyết sau)
- Muốn icon **đúng hình vật** (ô tô, sách, quyển vở, người) → phải bổ **1 font symbol đen** (Noto Emoji monochrome, ~vài trăm KB) vào kho + cho `bieudo_xstk` đăng ký font đó cho lớp icon.
- Phiên này **mạng chặn tải font** → chưa làm được. Tạm thời: icon vật thể dùng `●` và **khoá ghi tên vật** ("Mỗi ● ứng với 3 ô tô") — nghĩa toán không đổi, chỉ mất hình minh hoạ.
- Khi thầy sẵn sàng: tải `NotoEmoji-Regular.ttf` (bản đen) đưa vào kho, OB sẽ vá `bieudo_xstk` dùng nó — khi đó dùng thẳng 🚗📕⚽👦 được.

## Sau khi upload
- Mốc kho GIỮ **2026-09-28** (chỉ vá nội bộ, không đổi API). Luật XS-TK vẫn "mốc kho ≥ 2026-09-28".
- Đã test: chặn tofu báo lỗi đúng với 🚗; 9/9 hình bộ vẽ B39 render sạch (icon lẻ ½ của VD3 hoa đạt).
