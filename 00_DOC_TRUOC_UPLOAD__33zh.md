# UPLOAD KHO [33zh] — KHOFIX-logarit

**Nền:** clone từ HEAD [33zg] `3fee6ba` (đã đối chiếu — không máy nào bump thêm).
**Cách upload:** GitHub web → repo `hieuhoc-kho-congcu` → **ĐÈ** 3 file dưới (upload là ĐÈ, không merge).
Một thời điểm CHỈ máy này sửa kho.

## 3 file cần upload (ĐÈ):
1. `hieuhoc_template.js` — v10.51 [33za] → **v10.52 [33zh]** (vá logarit + cửa kiemMay).
2. `00_KHO_VERSION.txt` — đã chèn dòng mốc [33zh] lên đầu.
3. `00_CAPNHAT_KHO__33zh.md` — MỚI (biên bản cập nhật).

## Nội dung vá
- `logarit()` ln/log trơn: `fName` nhận run TRỰC TIẾP (bỏ `createMathBase` → hết `<m:fName><m:e>`).
- +Cửa kiemMay `[33zh]`: chặn `<m:e>` nằm thẳng trong `<m:fName>`.
- Chữ ký hàm KHÔNG đổi → KHÔNG regen API_REFERENCE / BẢN TRÍCH.

## Sau khi upload
- Re-LƯU B32/B33 bản [33zh] (bản LƯU cũ còn lỗi).
- Rà hồi tố CH06 Mũ–Log (dùng logarit, có thể dính log/ln trơn).
