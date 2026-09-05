# CAPNHAT_KHO — KHOFIX-ngoac (28r → 28s · v10.14 → v10.15)
**Đóng: Ông Bụt Đại số · 2026-09-05 · phát sinh khi QC DS7_CH01_B02**

## ⚠️ LUẬT ONE-WRITER (đọc trước)
File CHUNG với máy Hình. **Xác nhận máy Hình KHÔNG đang sửa kho** trước khi push. Template upload là ĐÈ, không merge.
Lưu ý version thực tế: GitHub SHA `9e2c22f9` = **v10.14 [28r]** (KHÔNG phải "28s/v10.15" như một số phiếu ghi nhầm). Bản này bump ĐÚNG 28r→28s.

## Việc thầy làm
1. **Push GitHub** `hieuhoc-kho-congcu` — đè 3 file: `hieuhoc_template.js` · `API_REFERENCE.md` · `00_KHO_VERSION.txt`. Commit: "KHOFIX-ngoac 28s: bỏ m:e lồng đôi trong ngoac() + cửa kiemMay".
2. **Nạp lại `API_REFERENCE.md` sang CẢ 2 Project** (OB_DS + OB Hình) — thay bản cũ.
3. Sau push: kho ra **mốc 28s**. PIN SHA mới vào `00_HOSO_BAI` của các LƯU_BÀI về sau.

## Nội dung sửa (1 lỗi CHẶN XUẤT + 1 cửa)
- **ngoac()**: bỏ lớp `<m:e>` tự bọc — `createMathBase()` đã bọc sẵn. Trước: `<m:d><m:e><m:e>…</m:e></m:e>` (lồng đôi) → **Word TỪ CHỐI MỞ FILE**. Sau: mỗi `<m:d>` đúng 1 `<m:e>`.
- **kiemMay cửa (a3)**: chặn build nếu `<m:e>` lồng `<m:e>`. Lớp lỗi Word-only này trước lọt mọi cửa (lxml/LibreOffice không render OMML). API `ngoac(bieuThuc)` **không đổi**.

## Kiểm chứng (đã làm)
- Rebuild B02 bằng kho vá: `<m:e><m:e>` = **0**, 30 `<m:d>` mỗi cái đúng 1 `<m:e>`, nội dung ngoặc còn nguyên.
- Cửa a3 test: **BẮT** file lỗi cũ (1 lỗi), **CHO QUA** file đã vá (0 lỗi).
- **Cần thầy xác nhận cuối**: mở `BAI_DS7_CH01_B02_GV.docx` (đính kèm) bằng **Word thật** → mở được, ngoặc + phân số đúng. (Sandbox không có Word; đã verify cấu trúc OOXML.)

## Rà bài đã giao dùng ngoac
- **B02**: đã rebuild sạch bằng kho vá (file kèm).
- **B01**: KHÔNG dùng `ngoac` (`<m:e><m:e>`=0) → LƯU_BÀI B01 an toàn, khỏi dựng lại.
- Bài khác dùng `ngoac`: rebuild lại bằng kho 28s trước khi phát hành.

## Ghi chú
- `BAN_TRICH_HAM_DS6.md` sinh từ `hinh_daiso.py` (hàm HÌNH) — patch này chỉ đụng template `ngoac()`, KHÔNG cần regen bản trích hình.
- Yêu cầu vá "para chuỗi trần" (phiếu riêng trước đó) VẪN treo — nếu người khác làm, nên **chồng lên mốc 28s này** (không tách nhánh song song) để giữ one-writer.
