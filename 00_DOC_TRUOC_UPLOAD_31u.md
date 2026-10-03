# CẬP NHẬT KHO → mốc 31u (2026-10-03) — Ông Bụt
# (GỘP: [31t] hình lát kín + [31u] vá tờ phân chương — PUSH 1 LẦN)

## Có gì trong gói
1. **hinh_dagiac.py** — [31t] thêm primitive `lat_kin_luc_giac(tam='O', canh=1.6,
   so_hinh=3, xoay=0)`: ghép so_hinh lục giác đều khít quanh 1 điểm chung (so_hinh=3
   → 360°, kín). Dùng Hình 17 bài B18. ADDITIVE — 0 regression.
2. **hieuhoc_template.js** — [31u] vá hàm `toPhanChuong` (tờ phân chương): mọi
   `spacing.line` nay kèm `lineRule:"auto"`; danh sách bài giãn thoáng
   (before/after:60, line:300). SỬA lỗi LibreOffice/PDF bóp dòng chật. Chữ ký hàm
   KHÔNG đổi → 0 regression (chỉ tờ bìa chương dùng hàm này).
3. **00_KHO_VERSION.txt** — nhật ký (đã gồm [31t]+[31u] ở đầu).

## THẦY PUSH (upload đè GitHub repo hieuhoc-kho-congcu):
  1. hinh_dagiac.py
  2. hieuhoc_template.js
  3. 00_KHO_VERSION.txt
→ sau push: `git rev-parse HEAD` lấy SHA mới, điền vào 00_HOSO_BAI của gói
   LUU_BAI__HH6_CH04_B18 (chỗ "SHA: chờ push 31t") — nay là SHA 31u.

## Ghi chú
- Cả 2 thay đổi đều additive/không-đổi-chữ-ký → KHÔNG cần regen API_REFERENCE,
  00_MUC_LUC_HAM, hay BAN_TRICH_HAM (trừ khi AI Soạn cần gọi trực tiếp
  lat_kin_luc_giac ở bài sau).
- Gói 31u THAY cho gói 31t cũ (đã gồm trọn [31t]). Chỉ cần push gói này.
