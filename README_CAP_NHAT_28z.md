# CẬP NHẬT KHO — mốc 28z (template v10.21) · 2026-09-10

## Đợt "A1 · Điều 18 neo phải" — nghiệm thu NEO PHẢI (Ông Bụt Hình)

**File đổi trong kho:**
- `hieuhoc_template.js` → **v10.21** (từ v10.20/28y)
- `API_REFERENCE.md` → tự sinh lại (`node sinh_apiref.js hieuhoc_template.js > API_REFERENCE.md`)
- `00_KHO_VERSION.txt` → mốc 28z

**Thay đổi code `hieuhoc_template.js`:**
1. `viDuLyThuyet()` — **GỠ guard cấm neo hình mục ②** (HP cũ Điều 18.1). Nay nhận `hinhBenPhai`/`hinhBenTrai` và cho chảy qua `viDu` như các mục khác → hình lý thuyết ② **mặc định neo phải, chữ wrap trái**.
2. `hinhVeTextBox()` — ngưỡng chặn **9.1cm → 8cm** (Điều 18 mới): hình rộng > 8cm để **dòng riêng căn giữa** (`H.hinhVe()`); ≤ 8cm neo phải.

**Ngoại lệ giữ nguyên (căn giữa):** hình > 8cm (#1) và hình trong câu Đúng/Sai (#2).

**Đã test:** build lại `PILOT_HINH.docx` (HH7_CH04_B14) từ template v10.21 → soi XML **4/4 đúng**: neo② (4.6cm phải) · neo Các dạng (4.6cm phải) · fig 9.0cm inline căn giữa · fig Đúng/Sai 5.0cm inline căn giữa. `quet_stamp .` = SẠCH (V11.8). Smoke require: 88 hàm load OK.

**Tương thích:** thuần mở rộng hành vi mục ②; bài Hình cũ không có hình ② thì output KHÔNG đổi.
