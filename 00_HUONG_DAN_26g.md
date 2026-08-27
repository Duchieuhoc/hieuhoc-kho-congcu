# CẬP NHẬT KHO 26g + CHUẨN HÌNH LƯỚI — HH6_CH05_B22
**Ông Bụt · 2026-08-27** · Chỉ đạo Giám đốc: ô lưới 4mm thống nhất + tâm rơi nút.

## ROUTING
1. **KHO → push GitHub (làm trước):** áp patch 26g:
   `cd hieuhoc-kho-congcu && git apply CAP_NHAT_KHO_2026-08-26g.patch` → `python3 quet_stamp.py` (SẠCH V11.6) → push (mốc **2026-08-26g**).
   4 file đổi: `hinh_dagiac.py` (hinh_thoi chéo-lưới; hinh_vuong/tu_giac chẵn), `hieuhoc_template.js` (hangHinh nhận rongCm riêng), `00_KHO_VERSION.txt`, `BAN_TRICH_HAM_HH6_CH05.md`. (Dự phòng: 4 file bản đầy đủ kèm đây, thay trực tiếp nếu patch lỗi.)
2. **CHUẨN:** nối `CHUAN_v10_5_BOSUNG.md` vào Chuẩn trình bày (QT-1 ô 4mm, QT-2 tâm nút).
3. **SCRIPTS B22:** `render_b22.py` (thoi a,b + vuông chẵn), `build_b22.js` (rongCm = 0,8×số ô kẹp 1,6-4; hình gói 2–5 ô; mục ② dòng riêng) — AI Soạn dùng bản này cho các lần dựng sau; đồng bộ quy tắc cho các bài kế.

## GHI CHÚ
- Bản dựng B22 đã dựng lại đạt chuẩn (ô 4mm + tâm nút): `BANDUNG__HH6_CH05_B22__L1.docx` (7 trang) — chờ thầy Vòng 3.
- Hình định lượng (thoi THGT B7) nay vẽ đúng tỉ lệ 4:3 (8×6 ô), số đo trùng thực tế.
