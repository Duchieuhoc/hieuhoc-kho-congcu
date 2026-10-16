# ĐỌC TRƯỚC KHI UPLOAD — [33b] hàm minMax (toán tử GTLN–GTNN)

## Việc của Thầy (3 file, kéo-thả web GitHub → Commit changes)
1. **hieuhoc_template.js** — ĐÈ (v10.41: THÊM `minMax`; mọi hàm cũ nguyên).
2. **API_REFERENCE.md** — ĐÈ (regen cùng snapshot v10.41).
3. **00_KHO_VERSION.txt** — ĐÈ (đã prepend block [33b]).

## An toàn
- CHỈ THÊM 1 hàm `minMax` + export → **0 regression** (gioiHan + hàm cũ nguyên; B01 rebuild byte-identical đã kiểm).
- `minMax` cấu trúc OMML Y HỆT `gioiHan` (lim) — đã nghiệm thu QC V2 + V3 Word thật [31za] → render Word đúng.
- ⚠️ **File CHUNG** (template + API dùng chung 4 Project): one-writer — xác nhận máy Hình KHÔNG sửa template song song trước khi đè. Sau push, phát bản y hệt mọi Project.

## Sau khi push
- HEAD ra mốc [33b]. OB/AI Soạn bụng kho có `minMax` cho chương GTLN–NN.
- Mốc kho yêu cầu cho B02 = **[33b]** (ghi trong 00_LUAT gói GIAO_AISOAN B02).
