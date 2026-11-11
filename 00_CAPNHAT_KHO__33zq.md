# CẬP NHẬT KHO [33zq] — 2026-11-11
## hieuhoc_template.js v10.52 → v10.53 · _RE_TOAN +∽ (ký hiệu ĐỒNG DẠNG)

### Một dòng
Thêm `∽` (U+223D SIMILAR TO) vào lớp ký tự hằng `_RE_TOAN` → `∽` định tuyến sang **Cambria Math** (font-proof), hết tofu ▯ trên Word.

### Vì sao
- `∽` = ký hiệu đồng dạng tam giác (△ABC ∽ △A′B′C′). Trước nay kho chỉ tách-font các ký hiệu trong `_RE_GLYPH` (△ ∥ ⊥ góc…) và `_RE_TOAN` (∈ ⇒ × ∞ ⋅ ≈…). **`∽` không nằm trong cả hai** → rơi Times New Roman.
- Times New Roman ở nhiều máy Word **không có glyph U+223D** → hiển thị ô vuông ▯ (tofu).
- Lộ ở **HH8_CH09_B34** — bài đồng dạng ĐẦU TIÊN của hệ thống (dùng `∽` 46 lần). Các chương trước chỉ dùng `=` (tam giác bằng nhau) nên chưa chạm. AI Soạn phát hiện khi dựng B34-L1, vá LOCAL để build chạy; OB QC Vòng 2 xác nhận + áp bản gốc lên kho.

### Thay đổi (ADDITIVE, 1 ký tự)
- `hieuhoc_template.js` dòng 578: `_RE_TOAN` cuối lớp ký tự `…→°′]` → `…→°′∽]`.
- Version header v10.52 → **v10.53 [33zq]**.
- `FONT_TOAN = "Cambria Math"` (không đổi) — đích định tuyến.

### KHÔNG đổi
- Chữ ký hàm KHÔNG đổi → **KHÔNG regen** `BAN_TRICH_HAM` / `API_REFERENCE`.
- Bài cũ 0 đổi (không bài nào dùng `∽` trước B34).
- `△ ∥ ⊥` vẫn Segoe UI Symbol; góc vẫn `kyHieuGoc` (OMML); chữ Việt vẫn TNR.

### Nghiệm thu
- `node --check hieuhoc_template.js` → sạch.
- Regex test: `∽` match `_RE_TOAN` = true; `△` vẫn ngoài `_RE_TOAN` (giữ Segoe).
- docx B34-L1 (AI Soạn vá local từ trước) đã xác nhận 46/46 `∽` = Cambria Math.

### Hưởng lợi
Mọi bài đồng dạng sau — B35, B36, B37, LTC, Ôn tập Chương IX (THCS) + các chương đồng dạng THPT — khỏi cần vá local `∽` nữa.
