# CẬP NHẬT KHO → 28t (v10.16) — KHOFIX-mathLong + KHOFIX-deKT

OB đã sửa + commit local nhưng KHÔNG có token để push. Thầy chọn 1 trong 2 đường:

## Đường A — git (giữ nguyên commit + message, khuyến nghị)
Trên máy đã đăng nhập GitHub, tại thư mục clone repo `hieuhoc-kho-congcu`:
```
git fetch /duong/dan/kho_28t.bundle HEAD
git merge FETCH_HEAD          # hoặc: git cherry-pick FETCH_HEAD
git push origin main
```
(hoặc `git pull /duong/dan/kho_28t.bundle HEAD` rồi `git push`.)

## Đường B — upload đè web (theo quy ước "template upload = đè, không merge")
Tải 2 file này thay thẳng bản trên repo/Project Knowledge:
- `hieuhoc_template.js`  (đã đóng dấu v10.16 / mốc 28t)
- `00_KHO_VERSION.txt`   (đã thêm block [28t])

## Đã đổi gì (chi tiết trong KHOFIX_deKT.patch + KHOFIX__GHICHU.md)
1. **mathLong (CỐT LÕI, mở Word):** `_mathChild` đệ quy gỡ vỏ → hết `<m:oMath>` lồng `<m:oMath>` khiến Word chối mở. +cửa kiemMay chặn oMath-lồng.
2. **deKT:** cửa nhận chữ ký "THỜI GIAN: … PHÚT" (Đ57.1) + căn lề chỉ đếm `<w:jc>` (bỏ tab-stop TN).
3. **bản HS (additive, hiện chưa dùng):** `bangDungSai({banHS})`, `tuLuanBTVN({anLoiGiai})`.

## Sau khi push: đồng bộ hạ nguồn
- API_REFERENCE.md (Project Knowledge): bổ sung ghi chú `_mathChild` nhận mảng lồng an toàn + 2 cửa mới.
- HOSO/LƯU_BÀI của ⑥ + 4 đề: pin SHA 28t sau khi push (hiện 5 .docx dựng bằng clone-vá, khớp 28t).
