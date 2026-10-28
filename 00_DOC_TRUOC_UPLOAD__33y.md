# ĐỌC TRƯỚC KHI UPLOAD — CAPNHAT_KHO [33y]  (repo: hieuhoc-kho-congcu)
## OB Đại số THPT · 28/10/2026 · đóng cửa [SỬA] pilot DS10_CH08_B23

MỤC ĐÍCH: thêm hàm vẽ **sơ đồ hình cây ĐẾM** (Đại số tổ hợp) — blocker pilot B23.
Dựng trên **HEAD [33x]** (logarit, 2026-10-26). **ADDITIVE — 0 regression** (module độc lập, không đụng file cũ).

## 🔴 CHỐNG LỆCH PHA — LÀM TRƯỚC KHI COMMIT (bài học 04/10 clobber 00_KHO_VERSION)
1. Mở GitHub, xem `00_KHO_VERSION.txt` HEAD hiện tại.
   - Nếu dòng đầu vẫn là **[33x]** → upload gói này bình thường (mốc [33y] còn trống).
   - Nếu HEAD đã có **[33y]** (máy Hình/CH06 chiếm trước) → **ĐỔI nhãn thành [33z]** trong `00_KHO_VERSION.txt`
     (và ghi "nối tiếp" đúng mốc HEAD mới) trước khi commit — KHÔNG đè mất log máy khác.
2. Một thời điểm chỉ MỘT máy sửa kho. Nếu máy Hình đang mở cửa sửa kho → chờ xong rồi hãy upload.

## FILE TRONG GÓI → UPLOAD ĐÈ (Commit changes)
| File | Thao tác | Ghi chú |
|------|----------|---------|
| hinh_ds10_ch08.py | **THÊM MỚI** | Module cây đếm. so_do_cay_dem(). Độc lập, xelatex riêng. |
| 00_KHO_VERSION.txt | ĐÈ | +block [33y] ở đầu (nối tiếp [33x]). |
| BAN_TRICH_HAM_DS10_CH08.md | **THÊM MỚI** | Bản trích cho AI Soạn (tự sinh). |
| 00_MUC_LUC_HAM.md | ĐÈ | +1 dòng so_do_cay_dem (nhóm "Theo chương/khác" 3→4; tổng 155). |

Sau upload: kho ra **[33y]**. AI Soạn bụng lại GitHub (BUNG_KHO) → có hàm cây → **mở khoá soạn B23**.
KHÔNG đụng: hinh_core / hieuhoc_template.js / API_REFERENCE (không sửa template, hàm là Python).
