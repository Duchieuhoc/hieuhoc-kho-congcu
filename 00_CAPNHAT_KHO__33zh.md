# CẬP NHẬT KHO [33zh] — KHOFIX-logarit (m:fName bọc thừa m:e)

**Ngày:** 2026-10-31 · **Người:** Ông Bụt Đại số THPT · **HEAD nền:** [33zg] `3fee6ba`
**File đổi:** `hieuhoc_template.js` (v10.51 [33za] → **v10.52 [33zh]**) · `00_KHO_VERSION.txt`

## Lỗi
`logarit(coSo, bieuThuc, {ten})` nhánh **ln / log trơn** (không cơ số) dựng:
`<m:func><m:fName><m:e>…ln…</m:e></m:fName><m:e>…</m:e></m:func>`
→ `<m:fName>` bọc thừa một lớp `<m:e>` (do `createMathBase` tự sinh m:e).
**Sai chuẩn OOXML:** `m:fName` nhận nội dung TRỰC TIẾP (run / sSub / limLow), KHÔNG qua `m:e`.

## Hệ quả (tương quan xác nhận trên 4 bài)
- **Word TỪ CHỐI MỞ FILE** ("experienced an error trying to open").
- **pandoc NUỐT tên hàm** → "y = ln(2x+3)" thành "y = (2x+3)" (SAI nội dung toán).
- lxml / LibreOffice / cửa kiemMay cũ ĐỀU LỌT (m:e và m:fName đều whitelist; không phải m:e-lồng-m:e).
- Lộ khi OB QC Vòng 2 **DS11_CH09_B32 (4 lỗi) + B33 (7 lỗi)**. B31/⑤ SẠCH vì dùng `gioiHan`/`minMax` (fName chứa `m:limLow` — hợp lệ).
- **HỒI TỐ:** mọi bài có log/ln trơn qua `logarit()` đều dính → cần rà + dựng lại khi gặp.

## Sửa
1. `logarit()`: `fnameChild = new MathRunSized(ten);` (bỏ `createMathBase`). Nhánh log-có-cơ-số (m:sSub trong fName) VỐN ĐÚNG, giữ nguyên.
2. **+Cửa kiemMay [33zh]** (`_scanOmmlLong`): bắt `<m:e>` có CHA TRỰC TIẾP `<m:fName>` → chặn xuất. Mirror KHOFIX ngoac[28s]/triTuyetDoi[33f].

Chữ ký hàm KHÔNG đổi → **KHÔNG regen API_REFERENCE / BẢN TRÍCH**.

## Nghiệm thu
- B32 rebuild: fName 9 đúng / 0 lỗi · B33 rebuild: 7 đúng / 0 lỗi · oMath nguyên (291/150) · "ln" đủ.
- Trả lại logarit lỗi (giữ cửa) → `xuatFile` THROW đúng lỗi 33zh, KHÔNG ra file ✓.
- MỞ WORD THẬT: Giám đốc xác nhận B32+B33 mở được 31/10.
