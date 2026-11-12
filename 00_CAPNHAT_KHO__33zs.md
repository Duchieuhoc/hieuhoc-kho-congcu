# CẬP NHẬT KHO [33zs] — 2026-11-12
## hinh_dagiac.py + so_do_tu_duy() · PRIMITIVE SƠ ĐỒ TƯ DUY KẺ KHUNG — Tổng kết chương

### Một dòng
Thêm `so_do_tu_duy(trung_tam, nhanh, mau, scale)` → **sơ đồ tư duy KẺ KHUNG** (hộp chữ nhật phân cấp nối đường) cho mục ② TỔNG KẾT / ÔN TẬP CHƯƠNG. Render qua xelatex (đủ dấu tiếng Việt).

### Vì sao
- Chỉ đạo Giám đốc: Ôn tập chương = tổng kết (hệ thống kiến thức) có **sơ đồ tư duy** — kiểu **KẺ KHUNG chuẩn VN** (hộp nối đường thể hiện quan hệ), KHÔNG phải bong bóng mindmap.
- Kho cũ chỉ có sơ đồ cây chuyên biệt (xác suất/hàm hợp) — không có sơ đồ tư duy tổng quát. Dùng cho tổng kết MỌI chương/môn.

### Thay đổi (ADDITIVE)
- `hinh_dagiac.py`: **+hàm** `so_do_tu_duy(trung_tam, nhanh, mau='blue', scale=1.0, out=…, tra_bytes=False)` + staticmethod ⇒ `h.so_do_tu_duy(...)`.
  - **Kiểu:** hộp TÂM (trái) → hộp NHÁNH (giữa) → hộp Ý CON (phải), nối bằng đường (quan hệ phân cấp).
  - `trung_tam` = chuỗi. `nhanh` = list: chuỗi (nhánh lá) HOẶC `(nhãn, [con,…])` (nhánh có ý con).
  - `mau` = **TÊN MÀU TRẦN** ('blue','teal','orange'…) — hàm tự pha !xx. KHÔNG truyền 'blue!30'.
  - Render **xelatex + Latin Modern Roman** (đủ dấu Việt); thiếu xelatex → lùi pdflatex. Nhãn tự escape + tự xuống dòng theo bề rộng hộp (KHÔNG tự thêm `\\`).
  - Generator ĐỘC LẬP (nhãn-chữ, KHÔNG toạ-độ-số → KHÔNG PHANH, như `la_ban`).
- `hieuhoc_template.js`: header **v10.54 → v10.55 [33zs]** (chỉ comment).
- `BAN_TRICH_HAM_HH8_CH09.md`: **REGEN** (so_do_tu_duy có mặt).
- `00_KHO_VERSION.txt`: **+block [33zs] VÀ [33zr]** lên đầu (gộp cả [33zr] lần trước chưa vào version file).

### KHÔNG đổi
- Bài cũ 0 đổi. `API_REFERENCE.md` KHÔNG đổi (so_do_tu_duy là hàm HÌNH). Code JS template.js KHÔNG đổi (chỉ header).

### Nghiệm thu
- Render tổng kết Chương IX: tâm `TAM GIÁC ĐỒNG DẠNG` + 5 nhánh (Hai tam giác đồng dạng · Ba trường hợp [c.c.c/c.g.c/g.g] · Pythagore [thuận/đảo] · Đồng dạng tam giác vuông [cgv/cạnh huyền-cgv/đường cao] · Hình đồng dạng [phối cảnh/tâm-tỉ số]) → **hộp phân cấp, đường nối rõ quan hệ, đủ dấu tiếng Việt** (xem `renders/so_do_tu_duy_CH9.png`).
- `node require(template)` OK.

### File đính kèm (thầy upload đè lên kho)
- `hinh_dagiac.py` (GIỮ phoi_canh [33zr] + so_do_tu_duy KẺ KHUNG [33zs])
- `hieuhoc_template.js` (header v10.55 [33zs])
- `BAN_TRICH_HAM_HH8_CH09.md` (regen — phoi_canh + so_do_tu_duy)
- `00_KHO_VERSION.txt` ([33zs] + [33zr] + [33zq]…)
- `00_CAPNHAT_KHO__33zs.md` (file này)
- `renders/so_do_tu_duy_CH9.png` (nghiệm thu)
