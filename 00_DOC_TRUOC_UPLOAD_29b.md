# CẬP NHẬT KHO → 29b · Thống nhất nhãn "Bài tập mẫu"
**Soạn: OB Đại số · 2026-09-15 · chỉ đạo Giám đốc (V12.1)**

## VÌ SAO
Toàn bộ hệ luật V12.1 đã chốt nhãn nhịp 1 = **"Bài tập mẫu"** (HP Điều 22.4·23.2 · Chuẩn trình bày v10.9 · Phụ lục Đại số v1.7 · API_REFERENCE). Cả HP lẫn Chuẩn tự ghi *"CẦN kiểm template: nếu nhãn hardcode → đổi Bài tập mẫu"*.

**Kho GitHub thực tế còn ở 29a** — template vẫn hardcode "Bài toán mẫu" (chỗ DUY NHẤT render ra Word: `dangToanDayDu` dòng 1462). Instructions V12.1 tưởng đã lên 29b nhưng kho chưa có việc đổi nhãn này → nếu giao AI Soạn bằng kho 29a, Word in sai nhãn.

**29b chỉ chồng thêm việc đổi nhãn lên nền 29a. Neo ② (gỡ ở v10.21/28z) GIỮ NGUYÊN.**

## ĐÃ SỬA (3 file trong gói này)
1. **hieuhoc_template.js** — 4 chỗ đổi "Bài toán mẫu" → "Bài tập mẫu":
   - dòng 1462: nhãn render hardcode (chỗ DUY NHẤT in Word) ← QUAN TRỌNG NHẤT
   - dòng 23, 1371, 1448: chú thích + thông báo lỗi (đồng bộ chữ, KHÔNG đổi hành vi)
   - Version template GIỮ v10.22 (chỉ đổi chuỗi, không đổi API).
2. **API_REFERENCE.md** — 1 chỗ: mô tả `phanTich()` đổi nhãn.
3. **00_KHO_VERSION.txt** — Mốc kho 29a → **29b (2026-09-15)** + khối changelog 29b.

## ĐÃ KIỂM
- ✓ grep: không còn "Bài toán mẫu" trong template + API kho.
- ✓ import-test: `dangToanDayDu` render OK (10 phần tử), nhãn ra đúng "Bài tập mẫu".
- Diff đầy đủ ở PATCH_29b__template.diff và PATCH_29b__apiref.diff.

## THẦY LÀM
1. **Upload đè GitHub** 3 file: `hieuhoc_template.js`, `API_REFERENCE.md`, `00_KHO_VERSION.txt` (web GitHub → kéo-thả → Commit changes).
2. **Nạp lại API_REFERENCE.md vào MỌI Project OB** (file CHUNG mọi môn — Đại số + Hình + Lý + Hóa). Template sống ở GitHub nên chỉ cần push; API_REFERENCE có bản trong Project nên phải nạp lại.

## ⚠️ ONE-WRITER — PHỐI HỢP MÁY HÌNH
File CHUNG (`hieuhoc_template.js`, `API_REFERENCE.md`) = 1 bản chân lý. Trước khi thầy upload đè:
- Xác nhận **máy Hình KHÔNG đang sửa template** cùng lúc (nếu có sửa riêng chưa đồng bộ → hợp nhất trước, không đè mù).
- Gói này vá trên nền 29a hiện tại của GitHub — nếu GitHub đã nhảy mốc khác (máy Hình push sau) thì báo OB để vá lại trên nền mới.
