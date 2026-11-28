# CẬP NHẬT KHO — mốc 38a (2026-11-28) — Ông Bụt (Hóa)

**Thêm module hình chương VIII (Hóa 9):** `hinh_hoa_ch08.py` + `kiemtra_hinh_hoa_ch08.py`.

## Nội dung — 4 hàm sơ đồ thí nghiệm (mục ② Hóa, Đ22.5)
- `na_ethylic()`         — Na + ethylic alcohol, ống nghiệm sủi bọt H₂ (Hình 26.4, B26). Callout 1–3.
- `chay_ethylic()`       — đốt cháy ethylic alcohol trong bát sứ, lửa xanh (B26). Callout 1–2.
- `ester_hoa()`          — ester hoá acetic acid + ethylic alcohol trong cốc nước nóng (B27). Callout 1–3.
- `so_sanh_hcl_acetic()` — đá vôi + HCl vs + CH₃COOH → Ca(OH)₂ (Hình 27.1 SBT, B27; câu 27.16). Callout 1–3.
- Mỗi hàm kèm `.CHU_GIAI` (dict số→nghĩa TV) để in chú giải dưới hình.
- `kiemtra_hinh_hoa_ch08.py` — self-test (render 4/4 + kiểm CHU_GIAI + CUA_RENDER).

## Tính chất
- **ADDITIVE** — module RIÊNG chương, KHÔNG đụng `hinh_hoa_ch06.py` (36d), `hinh_hoa_ch07.py` (37a).
- Text trong hình chỉ ASCII/ký hiệu hoá; dấu TV ở `.CHU_GIAI` (in tại Word).

## THẨM ĐỊNH OB
- `python3 kiemtra_hinh_hoa_ch08.py` → render 4/4 OK.
- Xem mắt 4 PNG: bố cục đúng (ống nghiệm Na sủi bọt; bát sứ lửa xanh; ống trong cốc nóng + lớp ester; 2 bộ so sánh → Ca(OH)₂). Lửa/dụng cụ không chồng lệch.
- Không sửa file chung khác → không lệch chuẩn nhánh khác.

## SAU KHI PUSH
- Điền SHA (`git rev-parse HEAD`) vào `00_LUAT.txt` của `GIAO_AISOAN__HOA9_CH08` (đang ghi mốc 38a / SHA CHỜ).
