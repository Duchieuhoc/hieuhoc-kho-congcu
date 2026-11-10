# BẢN TRÍCH HÀM VẼ — DS6__bieudo — tự sinh từ `bieudo_xstk.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `bieudo_xstk.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 09/11/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import bieudo_xstk as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `bieu_do_cham(tan_so, truc=None, nhan_truc='', tieu_de='', out='dot', tra_bytes=False)` | Biểu đồ chấm điểm (dot plot). tan_so: dict {gia_tri(int): so_cham}. Trên mỗi giá trị xếp CHỒNG các chấm tròn, số chấm = tần số của giá trị đó. truc=(min,max): ép chung thang để so sánh cặp A/B (2 biểu đồ cùng trục). Ghép cặp: gọi 2 lần cùng truc rồi H.luoiHinh([pngA, pngB]). Trả PNG (hoặc bytes nếu tra_bytes=True). |
| `bieu_do_cot(danh_muc, gia_tri, nhan_truc_dung='', nhan_truc_ngang='', tieu_de='', huong='dung', hien_nhan=True, mau=None, so_nguyen=True, goc_truc_dung=None, out='bd_cot', tra_bytes=False)` | Biểu đồ cột. Tự xử lí CỘT ÂM (giá trị <0 dưới trục). huong='ngang' → thanh ngang. |
| `bieu_do_cot_kep(danh_muc, nhom, nhan_truc_dung='', nhan_truc_ngang='', tieu_de='', huong='dung', hien_nhan=True, so_nguyen=True, out='bd_cot_kep', tra_bytes=False)` | Cột kép/đa nhóm + chú giải. nhom=[{'ten','gia_tri':[...]}]. Tự xử cột âm; huong='ngang'. |
| `bieu_do_doan_thang(truc, gia_tri=None, duong=None, nhan_truc_dung='', nhan_truc_ngang='', tieu_de='', hien_nhan=True, so_nguyen=True, bat_dau_0=True, cach_deu=True, vi_tri=None, dao_truc_dung=False, gioi_han_dung=None, out='bd_doan_thang', tra_bytes=False)` | Biểu đồ đoạn thẳng (biểu diễn thay đổi theo thời gian). truc=[nhãn trục ngang]. MỘT đường: gia_tri=[...]. NHIỀU đường: duong=[{'ten','gia_tri':[...]}, ...] (có chú giải). bat_dau_0=True → trục đứng từ 0 (đúng chuẩn, tránh bẫy gốc≠0). Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe. |
| `bieu_do_hop(q1=None, q2=None, q3=None, rau_trai=None, rau_phai=None, bat_thuong=None, moc_truc=None, nhan_truc='', so_do=False, tieu_de='', out='box', tra_bytes=False)` | Biểu đồ hộp (box plot) nằm ngang — mạch Thống kê THPT (độ phân tán, giá trị bất thường). • Dạng SỐ LIỆU (mặc định): q1≤q2≤q3; rau_trai≤q1; q3≤rau_phai; bat_thuong=[...] các giá trị NẰM NGOÀI [rau_trai; rau_phai]; moc_truc=[...] mốc ghi trên trục. PHANH: sai thứ tự / bất thường nằm trong râu → raise (không ra hình sai). • Dạng SƠ ĐỒ (so_do=True): KHUNG CHÚ THÍCH tổng quát (H5.5) — nhãn Q₁/Q₂/Q₃, ngoặc ΔQ, hai mốc (Q₁−1,5·ΔQ)/(Q₃+1,5·ΔQ), vùng giá trị bất thường. KHÔNG số liệu, KHÔNG lộ đáp án (Đ41.4). Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe. |
| `bieu_do_quat(nhan, phan_tram, tieu_de='', mau=None, out='bd_quat', tra_bytes=False)` | Biểu đồ hình quạt tròn (%). nhan=[...], phan_tram=[...] (tổng ~100). % in trên mỗi hình quạt (dấu phẩy VN), chú giải bên phải. Nan đầu bắt đầu từ đỉnh (12 giờ), đi THEO chiều kim đồng hồ (như SGK). Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe. |
| `bieu_do_tan_so_tuong_doi(mocs, tan_so_tuong_doi, nhan_truc_dung='Tần số tương đối', nhan_truc_ngang='', tieu_de='', don_vi='%', hien_nhan=True, buoc_truc_dung=None, out='bd_tstd', tra_bytes=False)` | HISTOGRAM tần số tương đối cho mẫu số liệu GHÉP NHÓM (cột LIỀN KỀ — chuẩn SGK/SBT 12). mocs : list MỐC nhóm (n+1 số) — vd [48.5,49,49.5,50,50.5,51] → 5 nhóm liền kề. tan_so_tuong_doi : list chiều cao n cột theo don_vi (mặc định %) — vd [5,10,35,40,10]. don_vi : hậu tố nhãn trục tung + nhãn cột ("%" mặc định; "" nếu tần số tương đối thập phân). buoc_truc_dung : bước chia trục tung (vd 5 → 0,5,10,…); None = tự chọn vạch đẹp. Cột span [mocs[i]; mocs[i+1]] → XỬ ĐƯỢC nhóm KHÔNG đều rộng. Số thập phân IN dấu phẩy (VN). |
| `bieu_do_tranh(hang, moi_icon, bieu_tuong='●', mau_icon='#2F5C8F', cho_phep_le=True, tieu_de='', chu_thich_khoa=None, out='bd_tranh', tra_bytes=False)` | Biểu đồ tranh. hang=[{'nhan','so_luong'}]. Vẽ so_luong/moi_icon biểu tượng, lẻ ½. chu_thich_khoa mặc định 'Mỗi <bt> ứng với <k> đơn vị'. CHẶN TOFU: biểu tượng thiếu glyph → raise (không vẽ ô vuông câm). |
| `do_thi_duong_cong(moc, nhan_truc_ngang='', nhan_truc_dung='', tieu_de='', giong=None, mau=None, x_max=None, y_max=None, buoc_ngang=1, buoc_dung=1, out='dt_cong', tra_bytes=False)` | ĐỒ THỊ HÀM SỐ dạng ĐƯỜNG CONG MƯỢT LIỀN đi qua các mốc (đọc đồ thị thực tế: nhiệt độ theo giờ SGK 7.23, …). moc=[(x,y),…] đọc từ đồ thị (x TĂNG DẦN). Nội suy PCHIP: giữ đơn điệu từng đoạn → lên đỉnh rồi xuống MƯỢT, KHÔNG vọt lố (không bướu giả như spline bậc 3). giong=[(x,y),…] vẽ nét đứt gióng + chấm mốc chốt (vd (4;5) SGK). buoc_ngang/buoc_dung bước vạch. Trả PNG/bytes. |
| `do_thi_gap_khuc(moc, nhan_truc_ngang='', nhan_truc_dung='', tieu_de='', giong=None, cham_dinh=True, mau=None, x_max=None, y_max=None, buoc_ngang=1, buoc_dung=1, out='dt_gapkhuc', tra_bytes=False)` | ĐỒ THỊ ĐƯỜNG GẤP KHÚC LIỀN trên lưới Oxy (đọc đồ thị thực tế liên tục: cân nặng cả đời SBT Vd2, vận tốc–thời gian SBT 7.24, …). moc=[(x,y),…] các ĐỈNH theo thứ tự (nối thẳng liền). Khác bieu_do_doan_thang (biểu đồ THỐNG KÊ, vạch theo mục): hàm này vẽ TRỤC SỐ ĐỀU (vạch nguyên cách buoc_ngang) nên ĐỈNH THẬP PHÂN (4,2 · 7,4 · 9,1) ĐỌC ÁP LƯỚI, KHÔNG gắn nhãn lên đỉnh → không chồng chữ. cham_dinh=True chấm đỉnh; giong=[(x,y),…] nét đứt gióng mốc chốt. Trả PNG/bytes. |
| `dong_xu(mat='sap', out='dong_xu', tra_bytes=False)` | Đồng xu. mat='sap'|'ngua' → in chữ S/N. |
| `mp_toado_diem(diem, nhan_truc_ngang='', nhan_truc_dung='', tieu_de='', x_max=None, y_max=None, buoc_ngang=1, buoc_dung=1, giong=False, mau=None, out='mp_diem', tra_bytes=False)` | ĐIỂM RỜI RẠC CÓ NHÃN TÊN trên mặt phẳng toạ độ — HAI TRỤC LỆCH TỈ LỆ. matplotlib tự scale 2 trục độc lập → 'một đơn vị trục tung = k lần trục hoành' hiện ra TỰ NHIÊN khi buoc_dung ≠ buoc_ngang (vd SGK 7.22 tuổi–cân nặng: buoc_ngang=1 (tuổi), buoc_dung=5 (kg) → mỗi ô lưới = 1 tuổi × 5 kg). diem=[{'x','y','ten','mau'?,'lech'?:(dx,dy) lệch nhãn}]. giong=True → mỗi điểm gióng nét đứt xuống 2 trục (đọc toạ độ). Trả PNG/bytes. |
| `truc_kha_nang(out='truc_kha_nang', tra_bytes=False)` | Trục khả năng 0 — ½ — 1 (Không xảy ra / Có thể / Luôn xảy ra) — H.9.28. |
| `tui_bi(bi, tieu_de='', out='tui_bi', tra_bytes=False)` | Túi bi. bi=[{'mau','so_luong'}] (mau: tên VN 'đỏ/xanh/vàng/đen/tím/trắng' hoặc hex). |
| `vong_quay(o, mui_ten_chi_vao=None, tieu_de='', out='vong_quay', tra_bytes=False)` | Vòng quay/tấm bìa. o=[{'nhan','mau'?,'ti_le'?}]. mui_ten_chi_vao = nhãn ô mũi tên chỉ. |
| `xuc_xac(mat, kieu='don', out='xuc_xac', tra_bytes=False)` | Xúc xắc. mat=[n] (đơn) hoặc [n1,n2] (đôi). n = số chấm 1..6. |

---

**Thống kê:** 16 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
