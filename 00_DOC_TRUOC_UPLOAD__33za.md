# ĐỌC TRƯỚC KHI UPLOAD — CAPNHAT_KHO [33za]  (repo: hieuhoc-kho-congcu)
## OB Đại số THPT · 28/10/2026 · vá format điểm tiêu đề (chỉ đạo Giám đốc)

MỤC ĐÍCH: tiêu đề phần in **"3,0đ"/"2,0đ"** thay "3đ"/"2đ" (tồn lộ ở B23+B24, dính MỌI bài THPT).
Dựng trên **HEAD [33z] (SHA 64c701f)**. **ADDITIVE — chỉ đổi hiển thị nhãn tổng điểm; 0 regression** (B23+B24 rebuild kiemMay sạch, nội dung khác 0).

## 🔴 CHỐNG LỆCH PHA — TRƯỚC KHI COMMIT
1. `00_KHO_VERSION.txt` HEAD: dòng đầu **[33z]** → upload bình thường ([33za] trống). Nếu đã có [33za] (máy khác) → đổi nhãn kế tiếp trước commit.
2. File CHUNG `hieuhoc_template.js` — một thời điểm chỉ MỘT máy sửa.

## FILE TRONG GÓI → UPLOAD ĐÈ
| File | Thao tác | Ghi chú |
|------|----------|---------|
| hieuhoc_template.js | ĐÈ | v10.50→**v10.51 [33za]**: +_fmtDiem (module) + 8 chỗ tiêu đề. ADDITIVE. |
| 00_KHO_VERSION.txt | ĐÈ | +block [33za]. |

KHÔNG regen API (chữ ký hàm không đổi). KHÔNG đổi 00_MUC_LUC (không hàm export mới).
Sau upload: kho [33za]. Mọi bài THPT (B25 trở đi + gop_chuong) hiện "3,0đ" chuẩn.
