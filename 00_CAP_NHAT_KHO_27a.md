# CẬP NHẬT KHO → 2026-08-27a
**Ông Bụt · 2026-08-27** · Routing: **push GitHub** `Duchieuhoc/hieuhoc-kho-congcu`.

## NỘI DUNG (1 dòng, không đụng hàm hình)
`hieuhoc_template.js` — hàm **`hangHinh`**: ô căn dọc **CENTER → BOTTOM** (căn ĐÁY).
- Khi các hình trong 1 hàng/lưới có chiều cao THẬT khác nhau (giữ ô 8mm, không chuẩn-hoá caoCm),
  căn giữa làm chú thích lệch mức. Căn đáy → **chú thích thẳng hàng**, đáy hình thẳng.
- Ảnh hưởng: MỌI hàng/lưới hình mọi bài (gồm B22) — cải thiện thuần, tương thích ngược
  (không đổi chữ ký, không đổi hàm hình). *(Thầy duyệt 2026-08-27.)*

## FILE ĐỔI (1)
- `hieuhoc_template.js` (kèm bản đầy đủ dự phòng trong thư mục này).

## CÁCH ÁP (chọn 1)
**A. Áp patch:**
```
cd hieuhoc-kho-congcu
git apply CAP_NHAT_KHO_2026-08-27a.patch
python3 quet_stamp.py        # phải: ✅ SẠCH — V11.6
# cập nhật 00_KHO_VERSION.txt → mốc 2026-08-27a (thêm dòng [27a])
git add -A && git commit -m "kho 27a: hangHinh can day (chu thich thang hang)" && git push
```
**B. Thay trực tiếp** `hieuhoc_template.js` (bản đầy đủ trong thư mục này) rồi commit & push.

## KIỂM SAU PUSH
```
python3 quet_stamp.py         # ✅ SẠCH V11.6
node -e "require('./hieuhoc_template.js'); console.log('template OK')"
```
Đầu 00_KHO_VERSION.txt hiển thị: **Mốc kho : 2026-08-27a**.

## GHI CHÚ CHUẨN (nối Project)
CHUAN_v10_5_BOSUNG.md · QT-4 thêm 1 gạch:
- *Hàng/lưới nhiều hình (cỡ khác nhau): ô CĂN ĐÁY để chú thích thẳng hàng.*

## B22 (đồng bộ)
B22 đang chờ Vòng 3 — khi dựng lại trên kho 27a sẽ **tự căn đáy**, không cần sửa script B22.
