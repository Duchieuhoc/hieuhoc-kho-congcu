# CẬP NHẬT KHO GITHUB: 28z → 29a
Repo: github.com/Duchieuhoc/hieuhoc-kho-congcu · OB Vật Lý 2026-09-14

## Vì sao
GitHub kho đang **28z**; mẫu tờ phân chương mới (29a) + gop_chuong tách file mới chỉ nằm ở gói rời,
CHƯA lên GitHub. Không push → phiên sau bụng kho kéo nhầm 28z, mất mẫu bìa mới.

## Commit đúng 4 file này (copy ĐÈ vào repo rồi push)
- hieuhoc_template.js   (v10.21 → v10.22 — toPhanChuong viết lại; tương thích ngược, chỉ đụng tờ phân chương)
- gop_chuong.js         (xuất TOPHANCHUONG riêng · TONGHOP bỏ bìa · lọc tổng kết khỏi danh sách bài)
- noi_tai_lieu.js       (lề bìa 1021 · footer 1560)
- 00_KHO_VERSION.txt    (thêm mục [29a])

Lệnh gợi ý:
    cd <repo clone>
    cp <4 file này> ./
    git add -A && git commit -m "kho 29a: toPhanChuong mẫu mới + gop_chuong tách tờ phân chương"
    git push
(hoặc upload đè 4 file trên web GitHub → Commit changes)

## KHÔNG cần đụng
- khung_bia.png + logo_hieuhoc.png: GitHub 28z ĐÃ có, GIỐNG HỆT 29a. (Gói kho_29a rời thiếu logo — chỉ lỗi gói rời.)
- hinh_*.py, package.json, API_REFERENCE...: 29a KHÔNG đổi.

## Sau khi push
- Từ nay bụng kho TỪ GITHUB (đủ logo+khung). **Bỏ dùng gói kho_29a rời** (thiếu logo).
- Template 29a là file CHUNG 3 nhánh (Đại·Hình·Vật lý). Thay đổi chỉ ở toPhanChuong (khâu nối) →
  KHÔNG ảnh hưởng soạn bài. Không cần rebuild bài cũ.

## Dọn kho (TÙY CHỌN — sau này)
GitHub đang đọng nhiều file tạm (kho_28*.bundle, *.patch, README_CAP_NHAT_28*, 00_DOC_TRUOC_KHI_PUSH_*).
Có thể xoá gọn 1 đợt như mốc [27c] để repo nhẹ — không gấp.
