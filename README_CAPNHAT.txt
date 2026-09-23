CẬP NHẬT KHO — MẪU TỜ PHÂN CHƯƠNG: +DÒNG "PHÂN MÔN"
=====================================================
NỀN: 30f (đã pull mới nhất). Đề xuất mốc: [30g] (2026-09-23) — nhánh Vật Lý.
⚠️ 3 file này = 30f + patch phanMon (KHÔNG phải nền 29y cũ). An toàn với 30a–30f.

toPhanChuong() +tham số phanMon (optional):
  - Có phanMon  → in "PHÂN MÔN: <…>" (20pt, xanh) dưới tên môn.
  - Không truyền → KHÔNG in (Toán Đại/Hình giữ nguyên bìa — ADDITIVE).
  - Chảy: 00_CHUONG.json {"phanMon":"VẬT LÝ"} → gop_chuong → noi_tai_lieu → toPhanChuong.

3 FILE THAY (đè vào kho):
  1. hieuhoc_template.js  2. gop_chuong.js  3. noi_tai_lieu.js
KHI PUSH: bump 00_KHO_VERSION.txt + dòng VERSION đầu template → [30g]; ĐỒNG BỘ 3 nhánh.
00_CHUONG.json KHTN: thêm "lop":"KHTN 6","phanMon":"VẬT LÝ" (hoặc "HÓA HỌC"). Toán không khai.
