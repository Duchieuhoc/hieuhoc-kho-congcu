# ĐỌC TRƯỚC KHI UPLOAD — CAPNHAT_KHO [33z]  (repo: hieuhoc-kho-congcu)
## OB Đại số THPT · 28/10/2026 · dựng TRƯỚC hàm cho pilot DS10_CH08_B24

MỤC ĐÍCH: +ký hiệu **tổ hợp/chỉnh hợp $C_n^k$ / $A_n^k$** vào template (hàm `kyHieuToHop`).
B24 (Hoán vị–Chỉnh hợp–Tổ hợp) dùng dày đặc → OB dựng trước để B24 không phải [SỬA].
Dựng trên **HEAD [33y] (SHA 1ca4a61)**. **ADDITIVE — 0 regression** (B23 rebuild lại kiemMay sạch).

## 🔴 CHỐNG LỆCH PHA — TRƯỚC KHI COMMIT
1. Xem `00_KHO_VERSION.txt` HEAD GitHub:
   - Dòng đầu là **[33y]** → upload bình thường (mốc [33z] trống).
   - Đã có **[33z]** (máy khác chiếm) → đổi nhãn **[34a]** trong 00_KHO_VERSION trước commit.
2. ⚠️ **File CHUNG `hieuhoc_template.js` sửa** → một thời điểm chỉ MỘT máy sửa template. Nếu máy Hình đang mở cửa template → chờ xong rồi upload.

## FILE TRONG GÓI → UPLOAD ĐÈ (Commit changes)
| File | Thao tác | Ghi chú |
|------|----------|---------|
| hieuhoc_template.js | ĐÈ | v10.48[33r]→**v10.50[33z]**: +kyHieuToHop + import MathSubSuperScript + export. ADDITIVE. |
| API_REFERENCE.md | ĐÈ | Regen (có mục kyHieuToHop). |
| 00_KHO_VERSION.txt | ĐÈ | +block [33z] đầu file. |
| 00_MUC_LUC_HAM.md | ĐÈ | Dựng Word 79→80; tổng 156; +dòng kyHieuToHop. |

Sau upload: kho **[33z]**. AI Soạn bụng kho → có `kyHieuToHop` → dựng B24 bình thường.
Cách gọi: `kyHieuToHop('C',7,4)`=C_7^4 · `kyHieuToHop('A',30,4)`=A_30^4 · `kyHieuToHop('C','n','k')`=C_n^k. (P_n: chiSoDuoi('P','n'); n!: text.)
