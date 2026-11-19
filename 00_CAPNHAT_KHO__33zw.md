===== CAPNHAT_KHO — [33zw ĐỀ XUẤT] MẠCH HÌNH KHỐI TRÒN XOAY (trụ · nón · cầu) =====
Chiều: OB Hình THCS → Giám đốc PUSH GitHub (github.com/Duchieuhoc/hieuhoc-kho-congcu)
Ngày: 2026-11-19 · Nền: HEAD mốc 33zt/33zv (template v10.56) · **Mốc mới: [33zw] — THẦY GÁN LẠI nếu trùng**
Phạm vi: Pha A HH9_CH10 (Chương X "Một số hình khối trong thực tiễn" — hình học trực quan).

## VÌ SAO
Chương X cần mạch hình MỚI: khối tròn xoay vẽ phối cảnh (trụ/nón/cầu + khai triển + ghép khối).
Soi kho THẬT trước khi dựng (chỉ đạo Giám đốc "hàm nào chưa có mới xây"):
- `mat_cau` CÓ ở `hinh_hh12_ch05.py` nhưng BUỘC Oxyz (lớp 12, hệ trục + vectơ) → không hợp bản lớp 9.
- `hinh_khoihop.py` chỉ có KHỐI ĐA DIỆN (cạnh thẳng) — không dùng cho mặt cong.
- Mạch elip-mặt-cong-tròn-xoay: 0 hàm → dựng mới.

## THÊM — `hinh_hh9_ch10.py` (MỚI) · 14 hàm một-phát (matplotlib, nền trong suốt)
Theo tiền lệ `khoiLapPhuongKhoetGoc` (generator độc lập, `hinh_core` cho phép với hình minh hoạ
nhãn — KHÔNG quan hệ toạ-độ-số để PHANH). AI Soạn chỉ khai `R, h, l, nhãn`; nét khuất nửa sau = đứt.
- Lõi: `hinh_tru` · `hinh_non` · `hinh_cau` (yếu tố H10.2/10.9/10.20).
- Phép quay sinh khối: `hcn_quay` (H10.3) · `tamgiac_quay` (H10.9a).
- Khai triển: `khai_trien_tru` (H10.5) · `khai_trien_non` (H10.11).
- Mặt cắt cầu: `cat_cau` (H10.23).
- Ghép khối: `tru_non` (H10.16) · `nua_cau_tru` (H10.37a) · `nua_cau_non` ốc quế (H10.39) ·
  `vong_bi` (H10.30) · `bon_xang` (H10.32) · `tru_khoan_non` (H10.28).
→ Bản trích: `BAN_TRICH_HAM_HH9_CH10.md` (sinh tự động, mode module one-shot).

## VÁ GENERIC (fix ở nguồn gốc, không sửa tay bản trích)
1. `sinh_bantrich.py` — header mode one-shot trước đóng cứng "thống kê & xác suất" (viết cho
   `bieudo_xstk`). Nay TRUNG TÍNH: "Module HÀM MỘT-PHÁT … (biểu đồ, mô hình, hoặc hình khối)";
   ví dụ gọi lấy TÊN HÀM ĐẦU động thay `bieu_do_cot` cứng. ADDITIVE, chữ ký 0 đổi.
2. `sinh_mucluc.py` — `quet_python()` trước BỎ QUA module không-class → module one-shot
   (`hinh_hh9_ch10`, và cả `bieudo_xstk` nếu đổi tên glob) VÔ HÌNH trong mục lục "tra đã-có-chưa".
   Nay liệt kê hàm module-level công khai. +NHOM['hinh_hh9_ch10']='Khối tròn xoay (trụ · nón · cầu)'.
→ Regenerate `00_MUC_LUC_HAM.md`: +category "Khối tròn xoay (trụ · nón · cầu) · 14 hàm".

## KIỂM
- Smoke import toàn bộ `hinh_*.py` trong 1 process: 0 lỗi.
- Render 14/14 hàm sạch (test `python3 hinh_hh9_ch10.py`).
- Đối chiếu trực quan khung "yếu tố" SGK — Giám đốc duyệt style 3 lõi (2026-11-19).

## KHÔNG ĐỤNG
`hieuhoc_template.js`, `hinh_core.py`, các kho chương khác, chữ ký hàm cũ — tất cả nguyên vẹn.

## CÒN TINH (iterate theo bài thật)
Nhãn `r/R` vòng bi hơi sát; màu đỏ mặt cắt cầu — tinh khi gặp bài thật đầu tiên.
