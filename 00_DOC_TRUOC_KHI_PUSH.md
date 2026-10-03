# BẢN VÁ KHO — goc_vuong(mau=) · OB 2026-10-04

## Việc
Thêm tham số `mau` cho `Hinh.goc_vuong(ten, mau=None)` (hinh_coban.py) để tô màu Ô VUÔNG góc vuông.
Dùng cho **ô vuông góc vuông KẾT QUẢ** ở hình lời giải (mau='red'), phân biệt với góc vuông ĐỀ (cam).

## Vì sao (fix ở nguồn gốc)
Khi hoàn thiện B10 (HH7_CH03), hình lời giải Hình 15 cần ô vuông ⊥ KẾT QUẢ (By⊥HK) tô ĐỎ để
phân biệt với ô vuông ĐỀ (HK⊥Ax′). Hàm `goc_vuong` cũ KHÔNG nhận màu, dù primitive `_o_vuong`
(hinh_phang.py) đã sẵn tham số `mau`. Vá = nối thông tham số qua, KHÔNG đụng primitive.

## Thay đổi (ADDITIVE — bài cũ 0 đổi)
- `goc_vuong(self, ten)` → `goc_vuong(self, ten, mau=None)`; tikz đẩy thêm el[2]=mau.
- Renderer (elif k=='goc_vuong'): `_o_vuong(..., el[2] if có else "orange")`.
- Gọi cũ `goc_vuong(ten)` → el 2 phần tử → "orange" (Y HỆT trước). Đã test: góc vuông cũ KHÔNG đổi.

## File thay đổi
- hinh_coban.py (xem hinh_coban.patch — 2 chỗ). Nền trên mốc kho d02efa7130a47aa025b2c58df6170e37f4b591a1 (31v).

## Cần làm khi push
1. Áp hinh_coban.py (hoặc hinh_coban.patch) lên kho.
2. Bump 00_KHO_VERSION.txt (vd 31v → 31w): "goc_vuong(mau=) — ô vuông góc vuông nhận màu (B10 hình lời giải)".
3. KHÔNG regen BAN_TRICH/API (chữ ký thêm tham số optional, tương thích ngược).
4. commit + push GitHub Duchieuhoc/hieuhoc-kho-congcu.
