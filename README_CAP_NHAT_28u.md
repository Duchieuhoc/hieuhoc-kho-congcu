# CẬP NHẬT KHO → 28u — MẠCH KHỐI HỘP + ENTRY DS8_CH01 (Đa thức)

OB đã sửa + commit local nhưng KHÔNG có token để push. Thầy chọn 1 trong 2 đường:

## Đường A — git (giữ nguyên commit + message, khuyến nghị)
Trên máy đã đăng nhập GitHub, tại thư mục clone repo `hieuhoc-kho-congcu`:
```
git fetch /duong/dan/kho_28u.bundle HEAD
git merge FETCH_HEAD          # hoặc: git cherry-pick FETCH_HEAD
git push origin main
```

## Đường B — upload đè web
Tải các file MỚI/ĐỔI này thay thẳng bản trên repo/Project Knowledge:
- `hinh_khoihop.py`        (MỚI — mạch khối hộp)
- `hinh_ds8_ch01.py`       (MỚI — entry chương)
- `hinh_dagiac.py`         (ĐỔI — hinh_vuong +goc_o/+cham ; da_giac_vuong +cham/+goc_o)
- `hinh_coban.py`          (ĐỔI — +khong_luoi())
- `BAN_TRICH_HAM_DS8_CH01.md` (MỚI — cho AI Soạn / OB Đại số)
- `00_KHO_VERSION.txt`     (ĐỔI — block [28u])

## Đã đổi gì (tóm tắt)
1. **hinh_khoihop.py [MỚI]**: `khoi_hop_chu_nhat` (hộp phối cảnh xiên, cạnh khuất nét đứt) +
   `net_hop_cat_goc` (net bìa cắt 4 góc). Compose thuần base — không mổ lõi, không op renderer mới.
2. **hinh_ds8_ch01.py [MỚI]**: entry = đa giác + đường tròn + khối hộp (cho 5 hình Chương I Toán 8).
3. **hinh_dagiac.py**: hinh_vuong +goc_o +cham ; da_giac_vuong +cham +goc_o (tương thích ngược).
4. **hinh_coban.py**: +khong_luoi() (tắt nền lưới cho hình đại số).

## Template KHÔNG đổi → API_REFERENCE.md giữ nguyên (v10.16).

## Sau khi push: đồng bộ hạ nguồn
- Project Knowledge: thêm `BAN_TRICH_HAM_DS8_CH01.md`.
- OB Đại số: nhận 5 PNG + 5 entry/script + mốc 28u để ráp khâu soạn.
- Luật ghi "mốc kho yêu cầu": nếu Phụ lục Đại số cần pin mốc → cập nhật 28u.
