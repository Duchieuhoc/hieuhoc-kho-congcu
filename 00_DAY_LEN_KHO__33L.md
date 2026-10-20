# CẬP NHẬT KHO — [33L] (v10.46) · 2026-10-20 · OB Hình áp
## KHOFIX `_accVectoCoChiSo` — VECTƠ NỐI-HAI-ĐIỂM CÓ CHỈ SỐ (A₁A₂, M₀M₁…)

### Vì sao
QC Vòng 2 **HH12_CH05_B15** (Giám đốc soi): 17 chỗ `kyHieuVecto('A_1A_2')` ra
**mũi tên trùm chuỗi literal "A_1A_2"** (gạch-dưới thô, chỉ số không hạ).
- Kho cũ: `_accVectoCoChiSo` chỉ bắt **1 token có chỉ số** (`u_1`→u⃗₁ đúng).
  Tên nối-2-điểm-có-chỉ-số `A_1A_2` KHÔNG khớp regex → rơi `_accVecto` =
  mũi tên trùm cả chuỗi "A_1A_2" literal. Kho **thiếu** case này.
- Bài "Phương trình đường thẳng" (và mọi bài dùng A⃗₁A₂, M⃗₀M₁) đụng.

### Sửa gì (ADDITIVE)
`_accVectoCoChiSo(ten)`: sau nhánh 1-token cũ, thêm nhánh **tách dãy
`<chữ>[_?<số>]`**; nếu ghép khít chuỗi gốc + ≥2 token + ≥1 token có chỉ số
→ base = dãy `MathSubScript`/`MathRunSized` trùm **1 mũi tên ⃗**.
- `kyHieuVecto('A_1A_2')` → ⟨mũi tên⟩ trùm [A₁][A₂] (2 m:sSub). ĐÚNG.
- Nhánh cũ 0 đổi: `AB`/`HM` vẫn trùm chuỗi (BYTE-IDENTICAL), `u_1` đã bắt ở
  `_mSubVecto`, `0` (vectơ-không) trùm "0". **Chữ ký `kyHieuVecto` KHÔNG đổi
  → KHÔNG cần regen API_REFERENCE/BAN_TRICH.**

### Nghiệm thu (OB)
Rebuild HH12_CH05_B15 (script AI GIỮ NGUYÊN) với kho [33L]:
- m:acc literal "_<số>" = **0** (trước: 17) · m:acc A₁A₂ đúng (≥2 m:sSub) = **17**
- m:e lồng = 0 · m:oMath lồng = 0 · undefined = 0 · ký tự cấm = 0 · 6 hình.
- Regression: AB/u_1/0 không đổi.

### Việc thầy
1. Đẩy `hieuhoc_template.js` [33L] đè lên GitHub `Duchieuhoc/hieuhoc-kho-congcu`
   (commit mẫu: "KHOFIX _accVectoCoChiSo [33L]: vectơ nối-hai-điểm có chỉ số A₁A₂").
2. **Trước khi giao B16**, kho GitHub phải có [33L] (B16 00_LUAT sẽ ghi mốc ≥[33L]).
   Nếu chưa đẩy, AI Soạn bụng HEAD [33k] vẫn đụng lỗi A₁A₂ cũ.
