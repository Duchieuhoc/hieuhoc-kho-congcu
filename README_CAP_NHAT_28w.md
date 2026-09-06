# CẬP NHẬT KHO → 28w (template v10.18) — KHOFIX canBac
OB vá + test trên bản CLONE MỚI NHẤT (nền 28v, SHA d74db15). KHÔNG có token push.

## ⚠️ ONE-WRITER: xác nhận máy Hình KHÔNG đang sửa template trước khi đè/push.
Bản 28w dựng từ bản mới nhất làm nền (đã gồm mọi thứ 28v). Chỉ đổi 1 dòng trong canBac; hinh_*.py nguyên.

## Đường A (git, giữ commit): merge `kho_28w.bundle` → push. Đường B: đè `hieuhoc_template.js` + `00_KHO_VERSION.txt`.

## SỬA (additive, không đổi API)
`canBac()` trả `_dmath(rad)` thay vì `new DMath(...)` → gắn `_hhComp` → gỡ vỏ khi lồng trong phanSo/luyThua/ngoac.
Trước: canBac lồng phân số/luỹ thừa sinh `<m:oMath>` lồng → Word chối mở (false-pass qua lxml/LibreOffice).

## Sau push
- regen API_REFERENCE.md (v10.18) — chữ ký public không đổi, chỉ dấu phiên bản.
- Sổ tồn DS8_CH01_B02: các ý √-trong-phân-số (SGK 1.8, SBT 1.7) đã dùng lại được ở ⑥-LTC.
