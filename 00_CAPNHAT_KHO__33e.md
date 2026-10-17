# CAPNHAT_KHO — [33e] · Ông Bụt Đại số THPT · 2026-10-17
## Thầy UPLOAD ĐÈ 3 file này lên GitHub kho (BUNG_KHO §4) → HEAD thành [33e]. OB KHÔNG tự push.

### Nền dựng: clone tươi HEAD [33d] SHA `e7855f7` (máy Hình xác nhận ĐANG NGHỈ — an toàn cửa one-writer).

## 2 VÁ (cả 2 ADDITIVE, 0 regression):

**1. glyph "Đ" math-mode — `hinh_ds12_giaitich.py` (bang_bien_thien)**
- Preamble +`\usepackage[T1]{fontenc}` +`\newunicodechar{Đ}{\text{\DJ}}` +`{đ}{\text{\dj}}`.
- → Nhãn cực trị **y_{CĐ} / y_{CT} HIỆN ĐÚNG chữ Đ** trong math-mode (trước rơi glyph → phải né bằng nhãn ASCII/giá trị số như B04 f(-1)/f(2), B05 số).
- Nguyên nhân gốc: Đ (U+0110) trong math-mode không có glyph; `\DJ` (lệnh T1, không đệ quy) + `\text{}` escape sang text font.
- CHỈ vá `bang_bien_thien`. **`do_thi_khao_sat` KHÔNG đụng** (thử thêm fontenc T1 vào pgfplots → đổi output đồ thị → gỡ bỏ, giữ nguyên).

**2. tồn "(1đ)"→"(1,0đ)" — `hieuhoc_template.js` v10.41→v10.42 (tuLuanBTVN)**
- `nhanDiem` dùng `_fmtDiem(diem)`: integer→1 chữ số thập phân ("1,0đ"/"2,0đ"), thập phân giữ ("0,25đ"/"0,5đ"), dấu "."→",".
- Chữ ký hàm KHÔNG đổi → **KHÔNG regen API_REFERENCE**.
- ⚠️ Ảnh hưởng CHUNG 4 Project: nhãn điểm tự luận BTVN mọi môn/cấp giờ "x,0đ" (đồng bộ style "0,25đ"). Hợp chuẩn trình bày.

## NGHIỆM THU (OB render + rebuild thật):
- BBT test nhãn y_{CĐ}/y_{CT} → Đ hiển thị đúng (soi mắt ✓).
- **REGRESSION: 6/6 hình B05 BYTE-IDENTICAL** (bbt_vd5_tru, bbt_vd6_giave, bbt_sbt150, dt_onhiem, dt_loinhuan, sodo_thuyen) — do_thi_khao_sat + BBT không-Đ không đổi.
- B05 docx rebuild: "1,0đ"×2, "1đ" lẻ=0, kiemMay=[], 0 ký tự cấm, 0 undefined.

## SAU KHI PUSH:
- HEAD [33e]. ⑤/⑥ cuối chương dùng được nhãn BBT y_{CĐ}/y_{CT} thẳng (không cần né).
- Mốc kho Phụ lục: cập nhật [33e] khi OB dựng ⑤/⑥ (hoặc để nguyên [33b]+[33a] — builder cũ vẫn chạy; [33e] chỉ thêm nhãn Đ).

## DANH MỤC (3 file upload đè):
- hinh_ds12_giaitich.py  (vá bang_bien_thien)
- hieuhoc_template.js    (v10.42, tuLuanBTVN)
- 00_KHO_VERSION.txt     (thêm mục [33e] đầu file)
