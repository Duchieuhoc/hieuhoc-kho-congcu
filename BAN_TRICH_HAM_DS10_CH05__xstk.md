# BẢN TRÍCH HÀM VẼ — DS10_CH05 — tự sinh từ `bieudo_xstk.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `bieudo_xstk.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 10/10/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import bieudo_xstk as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `bieu_do_cham(tan_so, truc=None, nhan_truc='', tieu_de='', out='dot', tra_bytes=False)` | Biểu đồ chấm điểm (dot plot). tan_so: dict {gia_tri(int): so_cham}. Trên mỗi giá trị xếp CHỒNG các chấm tròn, số chấm = tần số của giá trị đó. truc=(min,max): ép chung thang để so sánh cặp A/B (2 biểu đồ cùng trục). Ghép cặp: gọi 2 lần cùng truc rồi H.luoiHinh([pngA, pngB]). Trả PNG (hoặc bytes nếu tra_bytes=True). |
| `bieu_do_cot(danh_muc, gia_tri, nhan_truc_dung='', nhan_truc_ngang='', tieu_de='', huong='dung', hien_nhan=True, mau=None, so_nguyen=True, out='bd_cot', tra_bytes=False)` | Biểu đồ cột. Tự xử lí CỘT ÂM (giá trị <0 dưới trục). huong='ngang' → thanh ngang. |
| `bieu_do_cot_kep(danh_muc, nhom, nhan_truc_dung='', nhan_truc_ngang='', tieu_de='', huong='dung', hien_nhan=True, so_nguyen=True, out='bd_cot_kep', tra_bytes=False)` | Cột kép/đa nhóm + chú giải. nhom=[{'ten','gia_tri':[...]}]. Tự xử cột âm; huong='ngang'. |
| `bieu_do_hop(q1=None, q2=None, q3=None, rau_trai=None, rau_phai=None, bat_thuong=None, moc_truc=None, nhan_truc='', so_do=False, tieu_de='', out='box', tra_bytes=False)` | Biểu đồ hộp (box plot) nằm ngang — mạch Thống kê THPT (độ phân tán, giá trị bất thường). • Dạng SỐ LIỆU (mặc định): q1≤q2≤q3; rau_trai≤q1; q3≤rau_phai; bat_thuong=[...] các giá trị NẰM NGOÀI [rau_trai; rau_phai]; moc_truc=[...] mốc ghi trên trục. PHANH: sai thứ tự / bất thường nằm trong râu → raise (không ra hình sai). • Dạng SƠ ĐỒ (so_do=True): KHUNG CHÚ THÍCH tổng quát (H5.5) — nhãn Q₁/Q₂/Q₃, ngoặc ΔQ, hai mốc (Q₁−1,5·ΔQ)/(Q₃+1,5·ΔQ), vùng giá trị bất thường. KHÔNG số liệu, KHÔNG lộ đáp án (Đ41.4). Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe. |
| `bieu_do_tranh(hang, moi_icon, bieu_tuong='●', mau_icon='#2F5C8F', cho_phep_le=True, tieu_de='', chu_thich_khoa=None, out='bd_tranh', tra_bytes=False)` | Biểu đồ tranh. hang=[{'nhan','so_luong'}]. Vẽ so_luong/moi_icon biểu tượng, lẻ ½. chu_thich_khoa mặc định 'Mỗi <bt> ứng với <k> đơn vị'. CHẶN TOFU: biểu tượng thiếu glyph → raise (không vẽ ô vuông câm). |
| `dong_xu(mat='sap', out='dong_xu', tra_bytes=False)` | Đồng xu. mat='sap'|'ngua' → in chữ S/N. |
| `truc_kha_nang(out='truc_kha_nang', tra_bytes=False)` | Trục khả năng 0 — ½ — 1 (Không xảy ra / Có thể / Luôn xảy ra) — H.9.28. |
| `tui_bi(bi, tieu_de='', out='tui_bi', tra_bytes=False)` | Túi bi. bi=[{'mau','so_luong'}] (mau: tên VN 'đỏ/xanh/vàng/đen/tím/trắng' hoặc hex). |
| `vong_quay(o, mui_ten_chi_vao=None, tieu_de='', out='vong_quay', tra_bytes=False)` | Vòng quay/tấm bìa. o=[{'nhan','mau'?,'ti_le'?}]. mui_ten_chi_vao = nhãn ô mũi tên chỉ. |
| `xuc_xac(mat, kieu='don', out='xuc_xac', tra_bytes=False)` | Xúc xắc. mat=[n] (đơn) hoặc [n1,n2] (đôi). n = số chấm 1..6. |

---

**Thống kê:** 10 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
