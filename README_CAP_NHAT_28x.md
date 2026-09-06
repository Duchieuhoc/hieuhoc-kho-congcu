# CẬP NHẬT KHO → 28x (template v10.19) — 3 SỬA phát sinh khi QC DS8_CH01_B03
OB vá + test trên CLONE MỚI NHẤT (nền 28w, SHA dfd5afc). KHÔNG có token push.

## ⚠️ ONE-WRITER: xác nhận máy Hình KHÔNG sửa template trước khi đè/push.
Nền là bản mới nhất (gồm mọi thứ 28w). hinh_*.py KHÔNG đổi.

## Đường A (git): merge `kho_28x.bundle` → push. Đường B: đè `hieuhoc_template.js` + `00_KHO_VERSION.txt`.

## 3 SỬA (additive, output bài cũ KHÔNG đổi — đã verify document.xml B03 giống hệt)
1. `dangToanDayDu`: `loiGiaiND` = bí danh của `viDuLoiGiai` + CHẶN fail-im-lặng (thiếu lời giải mẫu → THROW).
2. `viDu`/`viDuLyThuyet`: thêm khe `loiGiaiND`/`viDuLoiGiai` → Ví dụ ② có lời giải từng bước (giữ `dapAn` cũ).
3. `+soGachTren()`: overline OMML `<m:bar>` qua `_dmath` (số học gạch-trên, cho ⑥/⑦).

## Sau push
- regen API_REFERENCE.md (v10.19). LƯU Ý: `sinh_apiref.js` đọc SAI hàm kiểu `(p)` (dangToanDayDu) →
  chữ ký ghi nhầm `loiGiaiND`, thiếu `viDuLoiGiai`. Nay đã có bí danh nên KHÔNG chặn AI Soạn, nhưng
  NÊN sửa sinh_apiref.js để chữ ký in đúng (việc riêng, chưa làm ở phiên này).
- Sổ tồn chia-hết số học (DS8_CH01_B02/B03) nay có `soGachTren` → soạn được ở ⑥/⑦.
