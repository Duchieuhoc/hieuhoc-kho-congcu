# CẬP NHẬT KHO → 29m · Bổ hàm hình "độ chính xác làm tròn" (DS7 Hình 1)
**Soạn: OB Đại số · 2026-09-19 · mở phiếu DS7_CH02_B05**

## VÌ SAO
AI Soạn báo CHẶN khi dựng Hình 1 của B05 (trục số minh họa độ chính xác làm tròn — SGK Toán 7 Hình 2.1): kho thiếu 2 yếu tố khai nghĩa (tô dải "độ chính xác" + vạch đứt trung điểm). Đúng §4 (AI Soạn không tự sửa kho) → OB bổ.

## ĐÃ SỬA (3 file kho + 1 bản trích)
1. **hinh_daiso.py**:
   - `+truc_do_chinh_xac(trai, phai, a, do_chinh_xac, nhan_a)` — hàm CHUYÊN DỤNG dựng trọn cảnh làm tròn (khuyên dùng cho ca này). Trục [trai;phai] cục bộ, KHÔNG kéo tia về gốc 0 (sạch, đúng SGK).
   - `truc_so_huu_ti` +2 tham số tùy chọn `khoang_to`, `vach_dut` (ADDITIVE — dùng chung cho các hình trục có dải/vạch đứt về sau).
2. **hinh_coban.py**: +2 nhánh render `'khoang'` (mũi tên 2 đầu + nhãn độ dài) và `'truc2dau'` (đường mũi 2 đầu).
3. **00_KHO_VERSION.txt**: bump 29l → **29m**.
4. **BAN_TRICH_HAM_DS7_CH02__daiso.md**: regen (44 hàm phơi, có 2 hàm/tham số mới).

## KIỂM CHỨNG
- ✓ import-test: cả 2 hàm chạy OK.
- ✓ render Hình 1 ra PNG, mắt OB duyệt: trục 46–47 mũi 2 đầu · điểm a giữa (gần 46) · vạch đứt 46,5 · dải "0,5". Khớp SGK Hình 2.1. Xem DEMO_Hinh1_do_chinh_xac.png.
- ✓ CHỈ THÊM — không đổi API/hành vi hàm cũ. Mạch hình học/hóa không đụng. 0 hồi quy.
- Diff đầy đủ: PATCH_29m__*.diff.

## THẦY LÀM
1. **Upload đè GitHub** 4 file: `hinh_daiso.py`, `hinh_coban.py`, `00_KHO_VERSION.txt`, `BAN_TRICH_HAM_DS7_CH02__daiso.md`.
2. Không cần nạp lại Project (đây là file kho + bản trích, sống ở GitHub).

## ⚠️ ONE-WRITER — PHỐI HỢP MÁY HÌNH
`hinh_daiso.py` và `hinh_coban.py` là file CHUNG. Trước khi upload:
- Xác nhận máy Hình KHÔNG đang sửa 2 file này (kho vừa nhảy 29c→29l toàn phiếu Hình — nếu máy Hình còn phiên mở, hợp nhất trước).
- Gói này vá trên nền 29l hiện tại của GitHub. Nếu GitHub đã nhảy mốc khác → báo OB vá lại trên nền mới.
