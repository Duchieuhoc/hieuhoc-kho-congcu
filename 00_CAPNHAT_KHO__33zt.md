# CẬP NHẬT KHO [33zt] — 2026-11-12 (gộp [33zs] + [33zr])
## hinh_coban.py: trung_diem +so_vach — SỬA LỖI KÝ HIỆU ĐOẠN BẰNG NHAU

### Một dòng
`trung_diem(M, A, B, mau=None, so_vach=1)` — thêm `so_vach` để **phân biệt các nhóm trung điểm KHÁC nhau trong cùng một hình** (trước đây mọi trung điểm trùng 1 vạch → ngầm hiểu mọi đoạn bằng nhau, SAI).

### Vì sao (Giám đốc phát hiện)
- Soi hình Ôn tập Chương IX: Hình 3 (AN=NB vs AM=MC), Hình 4 (AM=MH vs HN=NB), Hình 6 (AM=MH vs BN=NH vs HP=PC) — mọi cặp nửa dùng **cùng 1 vạch** → người đọc hiểu nhầm tất cả đoạn bằng nhau (trong khi AH≠BH≠CH…).
- Gốc: `trung_diem` luôn phát op `'gach_bang'` (1 vạch cứng), không có tham số số vạch.

### Thay đổi (ADDITIVE, tương thích ngược)
- `hinh_coban.py`: `trung_diem(M, A, B, mau=None, so_vach=1)` — phát `'dau_bang_n'` (đã hỗ trợ 1/2/3 vạch) thay `'gach_bang'`. Mặc định `so_vach=1` (bài cũ 1 trung điểm giữ nguyên). Nhiều trung điểm khác nhóm trong 1 hình → truyền `so_vach=1,2,3…`.
- `hieuhoc_template.js`: header **v10.55 → v10.56 [33zt]**.
- `BAN_TRICH_HAM_HH8_CH09.md`: REGEN.

### GỘP sẵn trong gói này (phòng khi kho chưa kịp lên mốc)
- **[33zs]** `so_do_tu_duy` (sơ đồ tư duy KẺ KHUNG) ở `hinh_dagiac.py`.
- **[33zr]** `phoi_canh` (vị tự/phối cảnh) ở `hinh_dagiac.py`.
→ Upload gói này là kho đầy đủ cả 3 mốc.

### Nghiệm thu
- Dựng lại Hình 3/4/6 Ôn tập: AM=MH (1 vạch) / HN=NB (2 vạch) / HP=PC (3 vạch) — phân biệt rõ, đúng toán.
- `trung_diem(...so_vach=2)` chạy OK; `node require(template)` OK; BAN_TRICH có cả 3 hàm.

### File đính kèm (thầy upload đè lên kho)
- `hinh_coban.py` (trung_diem +so_vach [33zt])
- `hinh_dagiac.py` (phoi_canh [33zr] + so_do_tu_duy KẺ KHUNG [33zs])
- `hieuhoc_template.js` (header v10.56)
- `BAN_TRICH_HAM_HH8_CH09.md` (regen — trung_diem/so_vach + so_do_tu_duy + phoi_canh)
- `00_KHO_VERSION.txt` ([33zt]+[33zs]+[33zr]+[33zq]…)
- `00_CAPNHAT_KHO__33zt.md` (file này)
