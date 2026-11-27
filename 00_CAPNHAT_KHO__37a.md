# CẬP NHẬT KHO — mốc 37a (2026-11-27) — Ông Bụt (Hóa)

**Thêm module hình chương VII (Hóa 9):** `hinh_hoa_ch07.py` + `kiemtra_hinh_hoa_ch07.py`.

## Nội dung
- `hinh_hoa_ch07.py` — ENTRY chương VII. 2 hàm sơ đồ thí nghiệm:
  - `dot_butane()` — đốt butane trong bình tam giác úp ngược (Hình 23.2, B23). Callout 1–3.
  - `dieu_che_ethylene()` — điều chế + thử tính chất ethylene: bình cầu có nhánh → NaOH → đốt đầu vuốt nhọn + ống nghiệm nước Br₂ (Hình 24.1, B24). Callout 1–6.
  - Mỗi hàm kèm `.CHU_GIAI` (dict số→nghĩa tiếng Việt) để AI Soạn in chú giải dưới hình.
- `kiemtra_hinh_hoa_ch07.py` — self-test (render 2/2 + kiểm CHU_GIAI + CUA_RENDER).

## Tính chất
- **ADDITIVE** — module RIÊNG chương, KHÔNG đụng `hinh_hoa_ch06.py` (36d) hay hàm cũ.
- Text trong hình chỉ ASCII/ký hiệu hoá (C₂H₄, Br₂…); dấu tiếng Việt ở `.CHU_GIAI` (in tại Word).
- Pipeline: `_HC.render_tikz_doc` (pdflatex→pdftoppm), như họ hình CH06.

## THẨM ĐỊNH OB
- `python3 kiemtra_hinh_hoa_ch07.py` → render 2/2 OK (dot_butane 10 KB · dieu_che_ethylene 22 KB).
- Xem mắt 2 PNG: bố cục đúng SGK (bình úp ngược + bật lửa; bình cầu→NaOH→đốt+Br₂). Lửa không chồng dụng cụ.
- Không sửa file chung khác → không lệch chuẩn nhánh khác.

## SAU KHI PUSH
- Điền SHA (`git rev-parse HEAD`) vào `00_LUAT.txt` của `GIAO_AISOAN__HOA9_CH07` (đang ghi mốc 37a / SHA CHỜ).
