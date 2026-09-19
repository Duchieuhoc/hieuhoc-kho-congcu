# CẬP NHẬT KHO → 29p · KHOFIX canBac nhận OMML (DS7 B06)
**Soạn: OB Đại số · 2026-09-20 · phiếu DS7_CH02_B06**

## VÌ SAO
AI Soạn báo CHẶN khi build B06 (bài đầu dùng căn với biểu thức phức): `canBac()` là hàm math CUỐI còn ép `String(soHang)` (các hàm phanSo/luyThua/ngoac/soGachTren đã chuyển `_mathChild` từ 28r). Hậu quả: √(191²), √(3²/7²), phân số có tổng căn ở tử/mẫu… serialize thành `[object Object]` → cửa kiemMay chặn xuất. Đúng §4 (AI Soạn không tự sửa kho) → OB áp upstream.

## ⚠️ LỆCH PHA ĐÃ XỬ
Khi đóng gói, kho GitHub đã ở mốc **29o** (máy Hình push thêm 29n "ẩn điểm phụ dựng" + 29o "trung trực bất đối xứng"). Patch canBac ban đầu AI Soạn đề xuất số 29n — TRÙNG. OB đã:
- Clone bản GitHub mới nhất (29o) làm nền.
- Đặt lại patch canBac là **29p** (mốc kế tiếp).
- Xác nhận mạch Hình 29n/29o CÒN NGUYÊN (không đè): `nua_dai_lui` + ẩn điểm `_` đều còn.

## ĐÃ SỬA (3 file)
1. **hieuhoc_template.js** `canBac()` (1 dòng): `[new MathRunSized(String(soHang))]` → `_mathChild(soHang)`.
2. **00_KHO_VERSION.txt**: bump 29o → **29p** (chèn khối, giữ nguyên 29n/29o của Hình).
3. **BAN_TRICH_HAM_DS7_CH02__daiso.md**: regen.

## KIỂM CHỨNG (OB tự chạy độc lập)
- ✓ stress-test 7/7 biểu thức khó (√(191²), √(3²/7²) lồng, tổng căn tử/mẫu, 1/√962, 4/(3+√(2-x)), số thường, string) — hết [object Object].
- ✓ Rebuild toàn bài B06: docx 30300 byte = bản nộp (reproducible). 98 khối căn, oMath depth=1, kiemMay=[], [object Object]=0.
- ✓ ADDITIVE — string/number chạy y nguyên, tương thích ngược. 0 hồi quy.
- Diff: PATCH_29p__canBac.diff.

## THẦY LÀM
1. **Upload đè GitHub** 3 file: `hieuhoc_template.js`, `00_KHO_VERSION.txt`, `BAN_TRICH_HAM_DS7_CH02__daiso.md`.
2. Không cần nạp Project (file kho + bản trích, sống ở GitHub).

## ⚠️ ONE-WRITER
`hieuhoc_template.js` là file CHUNG. Gói vá trên nền GitHub 29o hiện tại. Nếu GitHub đã nhảy mốc khác (máy Hình push tiếp) → báo OB vá lại trên nền mới. Xác nhận máy Hình không đang sửa `canBac`/template trước khi push.
