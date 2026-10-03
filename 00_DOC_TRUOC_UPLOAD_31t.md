# CẬP NHẬT KHO → mốc 31t (2026-10-03) — Ông Bụt Hình

## Việc: thêm primitive LÁT KÍN tổ ong (gỡ treo)
`hinh_dagiac.py`: +`lat_kin_luc_giac(tam='O', canh=1.6, so_hinh=3, xoay=0)`
— ghép `so_hinh` lục giác đều khít quanh MỘT điểm chung (mỗi góc 120° tại tâm;
so_hinh=3 → 360°, kín). Nhãn đỉnh ẩn, chỉ tâm hiện; không ràng buộc PHANH
(hình minh hoạ). ADDITIVE — chỉ THÊM 1 method, hàm cũ không đổi (0 regression).

Dùng cho **Hình 17 bài HH6_CH04_B18** (lát kín gạch lục giác) — trước đây OB
dựng tay ngoài kho; nay dựng chuẩn trên ô lưới 8mm qua hàm này.

## THẦY PUSH (upload đè GitHub repo hieuhoc-kho-congcu):
  1. hinh_dagiac.py
  2. 00_KHO_VERSION.txt
→ sau push: `git rev-parse HEAD` lấy SHA mới, điền vào 00_HOSO_BAI của gói
   LUU_BAI__HH6_CH04_B18 (chỗ "SHA: chờ push 31t").

## Ghi chú
- Hàm PHƠI mới (không prefix '_'). Nếu AI Soạn cần gọi trực tiếp ở bài sau →
  regen BAN_TRICH_HAM chương tương ứng. B18 do OB tự render nên chưa cần.
