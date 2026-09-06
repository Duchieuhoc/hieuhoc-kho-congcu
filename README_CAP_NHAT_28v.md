# CẬP NHẬT KHO → 28v (template v10.17) — 3 SỬA phát sinh khi QC DS8_CH01_B01

OB đã sửa + test trên bản CLONE MỚI NHẤT (nền 28u, SHA 8f35eb3) nhưng KHÔNG có token để push.

## ⚠️ ONE-WRITER (bắt buộc đọc trước khi đè)
Template là file CHUNG với máy Hình. Trước khi đè/push: **xác nhận máy Hình KHÔNG đang sửa template**.
Nếu máy Hình có sửa riêng → HỢP NHẤT trước, KHÔNG đè mù. Bản 28v này dựng từ bản mới nhất làm nền nên
đã gồm mọi thứ của 28u (khối hộp, entry DS8, v.v.) — chỉ thêm 3 sửa ở template, KHÔNG đụng hinh_*.py.

## Đường A — git (khuyến nghị, giữ commit)
```
git fetch /duong/dan/kho_28v.bundle HEAD
git merge FETCH_HEAD
git push origin main
```
## Đường B — upload đè web
Thay 2 file: `hieuhoc_template.js` (v10.17) + `00_KHO_VERSION.txt` (có block [28v]).

## 3 SỬA (đều CHỈ-SỬA-LỖI/THÊM-GUARD, không đổi API public)
1. **KHOFIX `baiTapTaiLop` +anLoiGiai** — regression 28t (ReferenceError mọi lần gọi mục ④). 1 dòng, additive.
2. **GUARD `_dapAnViDu`** — `dapAn` mảng-TRỘN chữ+công thức quên bọc `[[…]]` → THROW chỉ cách sửa
   (trước đây render "undefined)"). Tương thích ngược 100% với cách gọi ĐÚNG.
3. **+Cửa `kiemMay` quét "undefined"** → CHẶN XUẤT (bổ sung cho cửa "[object Object]" đã có).

## Sau khi push — đồng bộ hạ nguồn
- **API_REFERENCE.md** (Project Knowledge): regen `node sinh_apiref.js hieuhoc_template.js > API_REFERENCE.md`
  (chữ ký baiTapTaiLop +anLoiGiai; ghi chú 2 cửa mới). BAN_TRICH KHÔNG đổi.
- **Quy_Trinh_QC_OngBut.md** (Lớp 1): thêm 1 dòng cửa quét `"undefined"`/`"[object Object]"` (đồng bộ với kiemMay).
- **Phạm vi hồi quy:** bài CŨ dùng dapAn mảng-trộn (nếu có) nay rebuild sẽ THROW — phơi lỗi để sửa,
  KHÔNG phải mới hỏng (trước nay chúng đã bể "undefined" âm thầm).
