# CẬP NHẬT KHO [33zr] — 2026-11-11
## hinh_dagiac.py + phoi_canh() · PRIMITIVE VỊ TỰ / PHỐI CẢNH (Bài 37 "Hình đồng dạng")

### Một dòng
Thêm `phoi_canh(O, bo_diem, k, …)` vào `HinhDaGiac` → dựng **hình vị tự / phối cảnh tâm O tỉ số k**: đỉnh ảnh = O + k·(đỉnh nguồn − O), chùm **tia nét đứt đồng quy** về tâm O. Giải phóng Bài 37 (mắt xích phối cảnh cuối cùng).

### Vì sao
- Bài 37 (HH8_CH09) nửa số hình là **hình đồng dạng phối cảnh** (HĐ1, HĐ2, ví dụ, bài 9.29, SBT VD3): hai hình cùng dạng khác cỡ + tâm phối cảnh + chùm tia đồng quy.
- Phiếu khai nghĩa B37 đã cờ: **"Kiểm bản trích phép vị tự / tia đồng quy về tâm — Thiếu → OB bổ TRƯỚC (A↔C)."**
- Kho cũ có đa giác đều / lục giác / vuông / tam giác đều / **ngôi sao** — nhưng **KHÔNG có** cơ chế vị tự + chùm tia đồng quy. Đây là mắt xích thiếu duy nhất.

### Thay đổi (ADDITIVE)
- `hinh_dagiac.py`: **+method mới** `phoi_canh(O, bo_diem, k, noi_canh=None, net_tia='dut', mau_tia=None, nhan_O='below left', kin=False, to_nguon=None, to_anh=None)` trong class `HinhDaGiac` (⇒ `Hinh.phoi_canh` qua MRO).
  - `O=(ten,x,y)` tâm; `bo_diem=[(ten_nguon,x,y,ten_anh),…]`; `k>0,≠1`.
  - Ảnh đặt tại `O + k·(P−O)` (thẳng hàng, đúng vị tự); tia đứt O→đỉnh-xa (qua đỉnh gần); nối cạnh nguồn + ảnh.
  - `noi_canh=None` → tự nối chu vi (`kin=True` khép kín); `[]` → cặp điểm/đoạn rời.
  - PHANH: `thang_hang` mỗi bộ (O, nguồn, ảnh).
- `hieuhoc_template.js`: version header **v10.53 → v10.54 [33zr]** (chỉ comment header, 0 đổi code JS).
- `BAN_TRICH_HAM_HH8_CH09.md`: **REGEN** (chữ ký hàm MỚI → phoi_canh xuất hiện cho AI Soạn).

### KHÔNG đổi
- Bài cũ 0 đổi — không hàm nào dùng vị tự trước đây (hàm hoàn toàn mới).
- `API_REFERENCE.md` KHÔNG đổi (đó là bản trích hàm **template.js** dựng docx; phoi_canh là hàm **hình** → nằm ở BAN_TRICH_HAM theo chương).
- Code JS template.js KHÔNG đổi (chỉ header version).

### Nghiệm thu
- 3 ca render qua `h.ve()` (PHANH chạy, không throw):
  - **Tam giác k=2** (HĐ1): A′B′C′ nhỏ gần O → ABC lớn; 3 tia đứt O→A/B/C qua A′/B′/C′, đồng quy O. ✓
  - **Đoạn k=½** (Bài 9.29): AB lớn xa O → A″B″ nhỏ gần; 2 tia đứt đồng quy O. ✓
  - **Tứ giác k=2** (HĐ2): PQRS nhỏ → P′Q′R′S′ lớn; 4 tia đứt đồng quy O. ✓
- `thang_hang` (O, nguồn, ảnh) PHANH sạch (vị tự chính xác theo dựng).
- `node -e "require('hieuhoc_template.js')"` → nạp OK (header đổi không vỡ JS).

### Hưởng lợi
- Bài 37 dựng được trọn bộ hình phối cảnh. Tái dùng cho mọi bài vị tự / phối cảnh về sau (HH THPT: phép vị tự chương biến hình nếu có).

### File đính kèm (để thầy upload lên kho)
- `hinh_dagiac.py` (đã +phoi_canh)
- `hieuhoc_template.js` (header v10.54 [33zr])
- `BAN_TRICH_HAM_HH8_CH09.md` (regen)
- `00_CAPNHAT_KHO__33zr.md` (file này)
- `renders/` — 3 PNG nghiệm thu (tham khảo, KHÔNG cần đẩy kho)
