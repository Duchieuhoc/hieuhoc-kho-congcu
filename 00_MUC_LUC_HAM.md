# 00_MUC_LUC_HAM — MỤC LỤC HÀM TỔNG (tra "đã-có-chưa" TRƯỚC khi viết)

> **Tự sinh** bởi `sinh_mucluc.py` — TÁI DÙNG `sinh_bantrich.py` (Python) + `API_REFERENCE.md` (output `sinh_apiref.js`, JS). KHÔNG sửa tay.
> Regen: `python3 sinh_mucluc.py > 00_MUC_LUC_HAM.md`. Sinh ngày 19/11/2026.
> **LUẬT VÀNG:** trước khi viết hàm mới → tra file này (Ctrl+F theo NGHĨA). Có hàm khớp → GỌI LẠI. Gần giống → MỞ RỘNG. Viết mới là bậc CUỐI.

*Ẩn: hàm hạ tầng (`_…`) + cửa render (`ve`) theo Đ5.9. Base compose per-bài không vào kho → không liệt kê.*

## Theo chương / khác  · 79 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `ba_giao_tuyen(quan_he='dong_quy', nhan_mp=('(P)', '(Q)', '(R)'), nhan_gt=('a', 'b', 'c'), goc=(0.0, 0.0))` | ĐỊNH LÍ BA ĐƯỜNG GIAO TUYẾN (H4.23/H4.24): ba mặt phẳng (P),(Q),(R) đôi một cắt nhau theo BA giao tuyến PHÂN BIỆT c=(P)∩(Q), a=(R)∩(P), b=(R)∩(Q) | `hinh_hh11_ch04.py` | method | — |
| `ba_mp(quan_he='song_song', nhan=('(P)', '(Q)', '(R)'), cat_tuyen=False)` | BA MẶT PHẲNG | `hinh_hh11_ch04.py` | method | — |
| `ban_song(alpha=35, L_rieng=2.2, L_nuoc=1.6, cao=3.0, nhan_r='\\vec{v}_r', nhan_n='\\vec{v}_n', nhan_v='\\vec{v}')` | H4.17 — thuyền sang sông: hai bờ SONG SONG (d_1 dưới, d_2 trên) + tổng hợp vận tốc | `hinh_hh10_ch04.py` | method | — |
| `bang_bien_thien(moc, dau, gia_tri, danh_dau=None, ten_bien='x', ten_dh="y'", ten_ham='y', ky_am_vc='-\\infty', ky_duong_vc='+\\infty', bar_trai=False, bar_phai=False, out='bangbienthien', tra_bytes=False, scale=1.0)` | BẢNG BIẾN THIÊN (BBT) tổng quát — chuẩn SGK Giải tích 12 (tikz) | `hinh_ds12_giaitich.py` | method | — |
| `bang_xet_dau(moc, dau, ten_ham='f(x)', danh_dau=None, ky_am_vc='-\\infty', ky_duong_vc='+\\infty', out='bangxetdau', tra_bytes=False, scale=1.0)` | BẢNG XÉT DẤU tổng quát (tikz) — chuẩn SGK Việt Nam | `hinh_ds10_ch06.py` | method | — |
| `bang_xet_dau_tam_thuc(a, b, c, ten_ham='f(x)', out='bxd_tamthuc', tra_bytes=False, scale=1.0)` | BẢNG XÉT DẤU TAM THỨC BẬC HAI f(x)=ax^2+bx+c (a!=0) — máy TỰ tính Δ, nghiệm, dấu (Đ5.9) | `hinh_ds10_ch06.py` | method | — |
| `bat_dien(day, cao_tren=2.6, cao_duoi=2.6, dinh_tren='S', dinh_duoi="S'", ten_day=None, goc_o=(0.0, 0.0))` | BÁT DIỆN / SONG-CHÓP — hai chóp đáy ĐA GIÁC CHUNG ĐÁY, một đỉnh LÊN (dinh_tren) một đỉnh XUỐNG (dinh_duoi) — vd 2 chóp tứ giác đều ghép đáy (SBT 10.20 | `hinh_hh12_ch02.py` | method | — |
| `bieu_do_ven(kieu='cat', nhan=None, phan_tu=None, to=None, bao=None, out='ven', tra_bytes=False, chuThich=None)` | BIỂU ĐỒ VEN minh hoạ tập hợp & phép toán (giấu toạ độ, Đ5.9) | `hinh_tap_hop.py` | method | — |
| `cau_parabol_doc(W=4.0, H=2.0, xP=-2.2, nhan_nua='200 m', nhan_doc='Độ dốc tại $P$', nhan_cao='?', ten_A='A', ten_B='B', ten_P='P', out='cau_parabol', tra_bytes=False, scale=1.0)` | SƠ ĐỒ CẦU VƯỢT PARABOL (H9.5) | `hinh_ds11_giaitich.py` | method | — |
| `che_khuat(P0, P1, faces3, nsamp=200, eps=0.006, cop=0.005)` | Đoạn 3D P0→P1 bị các MẶT faces3 che tới đâu | `hinh_netkhuat.py` | method | — |
| `chop(day, dinh='S', cao=2.6, ten_day=None, goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=False)` | CHÓP đáy ĐA GIÁC bất kỳ + 1 đỉnh (apex) trên tâm đáy — phối cảnh xiên, NÉT KHUẤT tự tính theo che | `hinh_hh12_ch02.py` | method | — |
| `chop(day, dinh='S', cao=2.6, ten_day=None, goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=True)` | CHÓP đáy ĐA GIÁC bất kỳ + 1 đỉnh (apex) trên tâm đáy — phối cảnh xiên, NÉT KHUẤT tự tính theo che | `hinh_hh11_ch04.py` | method | — |
| `chop_canh_ben_vuong(day, dinh='S', tren='A', cao=2.6, ten_day=None, goc_o=(0.0, 0.0), net_khuat=True, o_vuong=True)` | CHÓP có CẠNH BÊN ⊥ ĐÁY — apex 'dinh' nằm THẲNG TRÊN đỉnh đáy 'tren' (cạnh dinh–tren ⊥ mặt đáy; khác chop chuẩn: apex trên tâm đáy) | `hinh_hh11_ch07.py` | method | — |
| `chop_cut_deu(n=4, canh_lon=3.2, canh_nho=1.7, cao=2.4, ten_duoi=None, ten_tren=None, goc_o=(0.0, 0.0), duong_cao=False, O='O', Ou="O'")` | CHÓP CỤT ĐỀU n cạnh — đáy lớn (dưới) ∥ đáy nhỏ (trên), tâm thẳng trục; mặt bên hình thang cân; nét khuất tự tính (đỉnh sau = đứt) | `hinh_hh11_ch07.py` | method | — |
| `cung_goc_3d(ten, nhan=None, mau='orange', br=6)` | Vẽ CUNG đánh dấu GÓC cho hình PHỐI CẢNH — KHÔNG ràng PHANH số đo | `hinh_hh11_ch07.py` | method | — |
| `dang_ky(loai, ham_kiem)` | Đăng ký 1 luật kiểm cho PHANH | `hinh_core.py` | method | — |
| `diem(ten, x, y, z, nhan='above right', mau=None, moc=True, hop_chieu=False, net_hop='dut', vecto_OM=False, O='O')` | ĐẶT ĐIỂM M theo TỌA ĐỘ (x;y;z) — dữ liệu đề; máy chiếu ra màn hình | `hinh_hh12_oxyz.py` | method | — |
| `diem_giua(ten, A, B, ti_le=0.5, mau=None, nhan='above')` | Điểm 'ten' nằm giữa A,B | `hinh_hh12_ch02.py` | method | — |
| `do_thi_bac_thang(doan, diem_dac=None, diem_ho=None, nhan_ham=None, xmax=1.3, ymax=1.4, xticks=(0.5, 1.0), yticks=(0.5, 1.0), xtick_lab=None, ytick_lab=None, out='bacthang', tra_bytes=False, scale=3.4)` | ĐỒ THỊ HÀM BẬC THANG / PIECEWISE-LINEAR (H5.7 — minh họa liên tục/gián đoạn) | `hinh_ds11_giaitich.py` | method | — |
| `do_thi_cat_tiep(x0=2.2, xQ=5.0, nhan_P='P', nhan_Q='Q', nhan_tt='t', nhan_ham='y=f(x)', out='cat_tiep', tra_bytes=False, scale=1.0)` | CÁT TUYẾN & TIẾP TUYẾN (H9.3 — khi Q→P, cát tuyến PQ dần về tiếp tuyến tại P) | `hinh_ds11_giaitich.py` | method | — |
| `do_thi_ghep(nhanh, xmin=None, xmax=None, ymin=None, ymax=None, nhan=None, hien_nhan=True, out='dothighep', tra_bytes=False)` | ĐỒ THỊ HÀM NHIỀU CÔNG THỨC — ghép nhánh tuyến tính / parabol trên từng khoảng | `hinh_ds10_ch06.py` | method | — |
| `do_thi_ham_log(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, duong_ngang=None, nhan_ngang=None, out='dothi_log', tra_bytes=False, scale=1.0)` | ĐỒ THỊ HÀM SỐ LÔGARIT y = log_a x (SGK H6.3/H6.4) | `hinh_ds11_mu_logarit.py` | method | — |
| `do_thi_ham_mu(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, duong_ngang=None, nhan_ngang=None, out='dothi_mu', tra_bytes=False, scale=1.0)` | ĐỒ THỊ HÀM SỐ MŨ y = a^x (SGK H6.1/H6.2) | `hinh_ds11_mu_logarit.py` | method | — |
| `do_thi_huu_ti(dang='doi_truc', a=1.0, b=2.0, c=1.0, k=1.0, xmin=None, xmax=None, ymin=None, ymax=None, nhan=None, hien_tc=True, out='dothi_ht', tra_bytes=False, scale=1.0)` | ĐỒ THỊ HÀM HỮU TỈ (pgfplots — máy dựng đường cong thẳng từ công thức; PHANH nội sinh) | `hinh_ds11_giaitich.py` | method | — |
| `do_thi_khao_sat(ham, nhanh=None, tcd=None, tcn=None, tcx=None, diem=None, xmin=-5, xmax=5, ymin=-5, ymax=5, xtick=None, ytick=None, xticklabels=None, yticklabels=None, mau='blue', samples=300, width=8.0, height=8.0, out='dothikhaosat', tra_bytes=False, scale=1.0)` | ĐỒ THỊ KHẢO SÁT HÀM SỐ — chuẩn SGK Giải tích 12 (pgfplots) | `hinh_ds12_giaitich.py` | method | — |
| `do_thi_luong_giac(ham='sin', out='dothi_lg', tra_bytes=False, scale=1.0)` | ĐỒ THỊ HÀM SỐ LƯỢNG GIÁC (SGK H1.14–1.17): y=sin x, y=cos x, y=tan x, y=cot x trên [-2π; 2π] | `hinh_ds11_luonggiac.py` | method | — |
| `do_thi_nhan_dang(loai, cx=0.0, cy=0.0, r=3.0, a=1.0, b=1.0, h=0.0, k=0.0, xmin=None, xmax=None, ymin=None, ymax=None, nhan=None, out='nhandang', tra_bytes=False)` | ĐỒ THỊ NHẬN DẠNG (pgfplots) — vẽ 1 đường cong trên Oxy để hỏi "có là đồ thị hàm số?" | `hinh_ds10_ch06.py` | method | — |
| `doan_oxyz(A, B, net='lien', mau=None)` | Nối 2 điểm Oxyz đã đặt (tên) — tiện ích; = doan base. | `hinh_hh12_oxyz.py` | method | — |
| `doc_ba_do_thi(out='ba_do_thi', tra_bytes=False, scale=1.0)` | BA ĐỒ THỊ VỊ TRÍ–VẬN TỐC–GIA TỐC (H9.10 — SGK 9.32, bài đọc đồ thị) | `hinh_ds11_giaitich.py` | method | — |
| `duong_thang(qua=None, vtcp=None, ten='\\Delta', nhan_u='\\vec u', diem_qua=None, pos=(0.0, 0.0), huong=(2.6, 1.3), ve_vtcp=True)` | ĐƯỜNG THẲNG + VTCP | `hinh_hh12_ch05.py` | method | — |
| `duong_tron_luong_giac(goc=None, ten_M='M', hien_sin_cos=True, goc_phan_tu=False, hien_A=True, R=2.6, out='dtlg', tra_bytes=False, scale=1.0)` | ĐƯỜNG TRÒN LƯỢNG GIÁC đầy đủ (SGK H1.7/H1.9b): tâm O, bán kính 1, điểm gốc A(1;0), chiều dương (ngược kim đồng hồ) | `hinh_ds11_luonggiac.py` | method | — |
| `duong_tron_nghiem(loai='sin', m=0.5, m_tex=None, ten1='M_1', ten2='M_2', R=2.6, out='dtng', tra_bytes=False, scale=1.0)` | ĐƯỜNG TRÒN NGHIỆM phương trình LG cơ bản (SGK Bài 4 — minh họa nghiệm sin x=m / cos x=m): đường tròn đơn vị + đường thẳng cắt tại 2 ĐIỂM NGHIỆM → chỉ  | `hinh_ds11_luonggiac.py` | method | — |
| `duong_vuong_goc_mp(S='S', H='H', K='M', nhan_mp='(P)', u=0.0, v=0.0, cao=2.3, rw=2.2, rd=1.4, goc=(0.0, 0.0), net_SH='lien', o_vuong=True, duong=None)` | DỰNG mặt phẳng (P) + đường SH ⊥ (P) tại chân H | `hinh_hh11_ch07.py` | method | — |
| `giao(ten, dt1, dt2, mau=None)` | ĐIỂM 'ten' = giao của 2 đường (tên) HOẶC 2 đoạn (tuple mút) | `hinh_hh12_ch02.py` | method | — |
| `goc_luong_giac(goc_v=55.0, goc_m=None, chieu='duong', out='goc_lg', tra_bytes=False, scale=1.0)` | GÓC LƯỢNG GIÁC (SGK H1.3): tia đầu Ou (ngang), tia cuối Ov tại góc goc_v°, tia quay Om (nét đứt, tuỳ chọn) + cung cong chỉ CHIỀU quay (dương=ngược kim | `hinh_ds11_luonggiac.py` | method | — |
| `goc_nhi_dien(canh='a', O='O', x='x', y='y', goc_mo=62.0, rw=2.3, rd=1.5, xr=1.5, nhan_mat=(None, None), vuong=False, hien_cung=True, goc=(0.0, 0.0))` | GÓC NHỊ DIỆN cạnh 'canh' — 2 nửa mặt phẳng chung bờ (gấp như quyển sách) | `hinh_hh11_ch07.py` | method | — |
| `hai_duong_thang(quan_he='cheo', ten=('\\Delta_1', '\\Delta_2'), vtcp=True)` | HAI ĐƯỜNG THẲNG schematic: 'cat' | 'song_song' | 'cheo' | 'vuong_goc' | `hinh_hh12_ch05.py` | method | — |
| `hai_hbh_chung_canh(ten1=('A', 'B', 'C', 'D'), ten2=('A', 'B', 'E', 'F'), goc=(0.0, 0.0))` | HAI HÌNH BÌNH HÀNH chung cạnh AB, không đồng phẳng (H4.16/H4.42): hbh1 = ten1 (nằm ~ngang), hbh2 = ten2 (dựng ~đứng), chung cạnh đầu (A,B) | `hinh_hh11_ch04.py` | method | — |
| `hai_mat_phang(quan_he='cat', nhan=('(P)', '(Q)'), nhan_duong=('b', 'a'), goc=(0.0, 0.0), rw=2.0, rd=1.15, cao=1.9, ve_duong=True, duong2=None)` | HAI MẶT PHẲNG biểu diễn (schematic, Đ5.9 chế độ 2) | `hinh_hh11_ch04.py` | method | — |
| `hai_mat_phang(quan_he='cat', nhan=('(P)', '(Q)'), vtpt=True)` | HAI MẶT PHẲNG ở quan hệ: 'song_song' | 'vuong_goc' | 'cat' | `hinh_hh12_ch05.py` | method | — |
| `he_truc(dai_x=3.2, dai_y=4.2, dai_z=4.2, mp_toado=False, vecto_dv=True, O='O', ten_truc=('x', 'y', 'z'))` | HỆ TRỤC Oxyz: 3 trục đôi một vuông góc (mũi tên + nhãn) + vectơ đơn vị i,j,k | `hinh_hh12_oxyz.py` | method | — |
| `hinh_chu_nhat_noi_tiep(goc_theta=35.0, nhan_theta='\\theta', duong_kinh='30 cm', R=2.5, out='cnnt', tra_bytes=False, scale=1.0)` | CHỮ NHẬT NỘI TIẾP ĐƯỜNG TRÒN (SBT xà gỗ — mặt cắt, ứng dụng LG): đường tròn tâm O; chữ nhật ABCD nội tiếp, đường chéo AC = đường kính (qua O); góc θ g | `hinh_ds11_luonggiac.py` | generator | — |
| `hinh_khuc_xa(goc_toi=50.0, goc_kx_ve=37.0, nhan_i='i', nhan_r='r', nhan_mt1='Không khí', nhan_mt2='$n_2 = 1{,}33$', out='khucxa', tra_bytes=False, scale=1.0)` | KHÚC XẠ ÁNH SÁNG (SGK Bài tập cuối chương, H1.26 — ứng dụng LG): mặt phân cách ngang + pháp tuyến NN' thẳng đứng tại I; tia tới SI (góc tới i với pháp | `hinh_ds11_luonggiac.py` | generator | — |
| `keo_dai(ten, A, B, dai=None, nhan='below right', ve_doan=True, mau=None)` | KÉO DÀI đoạn A→B QUA B: đặt 'ten' sao cho A, B, ten THẲNG HÀNG và B nằm GIỮA A và 'ten' (ten trên TIA ĐỐI của tia BA) | `hinh_hh12_ch02.py` | method | — |
| `khoi_hop_oxyz(a, b, c, goc=(0.0, 0.0, 0.0), ten_dinh=None, nhan=None, net_khuat='dut', hien_dinh=True)` | KHỐI HỘP CHỮ NHẬT đặt trong Oxyz, cạnh song song 3 trục (nét khuất tự tính) | `hinh_hh12_oxyz.py` | method | — |
| `khoi_tron_xoay(ham, a, b, ra=0.0, rb=0.0, cat_trong=None, nhan_ham=None, nhan_can=('a', 'b'), hien_sinh=False, nhan_khoi=None, nhan_khoi_xy=None, mau='blue', mau_to='blue!12', xmin=None, xmax=None, ymin=None, ymax=None, sau=None, samples=160, width=9.0, height=6.0, out='khoitronxoay', tra_bytes=False, scale=1.0)` | KHỐI TRÒN XOAY 3D (silhouette phối cảnh chuẩn SGK Giải tích 12 Bài 13) — pgfplots | `hinh_ds12_giaitich.py` | method | — |
| `khoi_tu_dinh(dinh, canh, mat=None, to_mat=None, net_khuat='dut', hien_dinh=True, mau_dinh=None)` | KHỐI TỔNG QUÁT trong Oxyz từ TOẠ ĐỘ ĐỈNH (đề cho) + CẠNH (+ MẶT) — tự tính nét khuất | `hinh_hh12_oxyz.py` | method | — |
| `lang_tru_xien(day, cao=2.4, lech=1.1, ten_duoi=None, ten_tren=None, goc_o=(0.0, 0.0), apex=None, chan=None, ten_chan='H', duong_cao=False, o_vuong=True, nhan_chan='below')` | LĂNG TRỤ/HỘP XIÊN — đáy trên = đáy dưới TỊNH TIẾN theo cạnh bên nghiêng (lệch 'lech' theo phương ngang + lên 'cao'); cạnh bên KHÔNG ⊥ đáy | `hinh_hh11_ch07.py` | method | — |
| `luoi_mp(nx, ny, nz=0, mau='black!18')` | LƯỚI Ô VUÔNG đơn vị trên MẶT PHẲNG (Oxy) (sàn) — nx×ny ô, để đọc toạ độ (H.2.38/2.39) | `hinh_hh12_oxyz.py` | method | — |
| `luoi_xien(goc_b=60, dai_b=1.0, m=4, n=5, luoi=True, co_so=True, nhan_a='\\vec{a}', nhan_b='\\vec{b}', vectos=None)` | H4.27/H4.28 — hệ CƠ SỞ XIÊN: a = (1;0) (ngang), b nghiêng 'goc_b'° dài 'dai_b' | `hinh_hh10_ch04.py` | method | — |
| `mat_cau(tam=(0.0, 0.0, 0.0), R=1.3, nhan='(S)', tam_ten='I', ban_kinh=True, diem=None, duong_kinh=None, rb_ti=0.34)` | MẶT CẦU tâm I(tam) bán kính R — coordinate-tied (toạ độ + R từ đề) | `hinh_hh12_ch05.py` | method | — |
| `mat_nghieng_luc(goc=30, day=6.0, ti_le_C=0.58, L_P=1.9, L_w=1.25, L_F=1.6, nhan_P='\\vec{P}', nhan_w='\\vec{w}', nhan_F='\\vec{F}')` | H4.18 — kéo vật lên mặt dốc nghiêng góc 'goc'° so phương ngang | `hinh_hh10_ch04.py` | method | — |
| `mat_phang(nhan='(P)', goc=(0.0, 0.0), rw=2.0, rd=1.3, mau='blue!8', diem=None, duong=None, diem_ngoai=None, pre=None, to=True)` | MẶT PHẲNG schematic = hình bình hành phối cảnh nghiêng (nền cao w=0) | `hinh_hh11_ch04.py` | method | — |
| `mat_phang(nhan='(\\alpha)', vtpt=False, nhan_n='\\vec n', cap_vtcp=False, nhan_uv=('\\vec u', '\\vec v'), diem_ngoai=False, mau='blue!9', pos=(0.0, 0.0), rw=1.75, rd=1.15)` | MẶT PHẲNG schematic = hình bình hành phối cảnh (hình bình hành trên nền z=0) | `hinh_hh12_ch05.py` | method | — |
| `mat_phang_doan_chan(a, b, c, nhan='(\\alpha)', to=True, ten=('A', 'B', 'C'))` | MẶT PHẲNG cắt 3 trục tại A(a;0;0), B(0;b;0), C(0;0;c) — coordinate-tied | `hinh_hh12_ch05.py` | method | — |
| `mien_nghiem(bpt, diem=None, khung=None, nhan_duong=None, ten_mien=None, out='mien_nghiem', tra_bytes=False, dpi=200)` | Vẽ miền nghiệm của 1 BPT hoặc hệ BPT bậc nhất hai ẩn trên mặt phẳng Oxy | `hinh_bpt.py` | method | — |
| `nhan_toado(ten, x, y, z, nhan='above right', mau=None, moc=True)` | Đặt + GHI NHÃN TOẠ ĐỘ cho đỉnh (khối 'thả' trong Oxyz — H.2.42) | `hinh_hh12_oxyz.py` | method | — |
| `o_vuong_3d(ten, mau=None)` | Đánh Ô VUÔNG ⊥ cho hình PHỐI CẢNH — KHÔNG ràng PHANH do=90 | `hinh_hh11_ch07.py` | method | — |
| `parabol(a, b, c, xmin=None, xmax=None, ymin=None, ymax=None, hien_dinh=True, ten_dinh='I', hien_truc=True, hien_giao_ox=True, hien_giao_oy=True, diem_doi_xung=True, diem_them=None, nhan=None, hien_nhan=True, out='parabol', tra_bytes=False, scale=1.0)` | DO THI PARABOL y = a x^2 + b x + c (a!=0) tren he Oxy — pgfplots, may tu dung tu cong thuc | `hinh_ds10_ch06.py` | method | — |
| `parabol_2tiep(k=0.22, q=3.6, net='dut', nhan=('L_1', 'L_2'), ten_P='P', ten_Q='Q', out='parabol_2tiep', tra_bytes=False, scale=1.0)` | PARABOL ÚP + 2 TIẾP TUYẾN NÉT ĐỨT (H9.6b — đường ray tàu lượn, dùng ở BT 9.5) | `hinh_ds11_giaitich.py` | method | — |
| `phanh(V, rang_buoc)` | rang_buoc: list dict, mỗi cái có 'loai' + tham số riêng (xem hinh_phang) | `hinh_core.py` | method | — |
| `phep_chieu_ss(dinh_goc, canh, cao=2.6, phuong=(0.7, -0.35), ten_goc=None, ten_bong=None, goc=(0.0, 0.0), mp_chieu=True, nhan_mp='(\\alpha)', elip=False)` | PHÉP CHIẾU SONG SONG: hình GỐC (ở độ cao 'cao') đổ bóng xuống mặt phẳng chiếu (sàn, w=0) theo phương chiếu; vẽ tia chiếu đôi một song song | `hinh_hh11_ch04.py` | method | — |
| `proj(p)` | (u,v,w) → (x,y) màn. | `hinh_netkhuat.py` | method | — |
| `recon3d(x, y, v)` | Dựng lại (u,v,w) từ vị trí màn (x,y) + độ sâu v đã gán (giữ NGUYÊN vị trí màn → layout bài cũ 0 lệch). | `hinh_netkhuat.py` | method | — |
| `render_tikz_doc(tex_full, out, tra_bytes=False, dpi=200)` | Biên dịch MỘT tài liệu TikZ standalone ĐẦY ĐỦ (documentclass→end) → PNG | `hinh_core.py` | method | — |
| `so_do_cay(goc='O', cap1=None, cap2=None, out='so_do_cay', tra_bytes=False, scale=1.0, dx=2.4, dy=2.3)` | SƠ ĐỒ HÌNH CÂY xác suất (tikz) — chuẩn SGK (gốc trên, nhánh tỏa xuống) | `hinh_xacsuat.py` | method | — |
| `so_do_cay_dem(goc, con, out='so_do_cay_dem', tra_bytes=False, scale=1.0, dx=2.2, dy=2.0, dem_la=False)` | Sơ đồ hình cây ĐẾM (quy tắc cộng/nhân): gốc→nhánh→lá, nhãn cụm từ tiếng Việt, đa tầng & lệch độ sâu; dem_la=True tự đánh số lá | `hinh_ds10_ch08.py` | method | — |
| `so_do_ham_hop(nhan_g='g', nhan_f='f', nhan_x='x', nhan_u='u=g(x)', nhan_y='y=f(u)', nhan_hop='y=f(g(x))', out='ham_hop', tra_bytes=False, scale=1.0)` | SƠ ĐỒ HÀM SỐ HỢP (H9.8, B32) | `hinh_ds11_giaitich.py` | method | — |
| `so_do_hinh(diem, canh=None, canh_dut=None, goc_vuong=None, nhan_canh=None, nhan_diem=None, nua_tron=None, duong_tron=None, nhan_tong=None, diem_cham=None, out='sodohinh', tra_bytes=False, scale=1.0)` | SƠ ĐỒ HÌNH HỌC PHẲNG (tikz) — bài mô hình hóa (tam giác vuông, tứ giác, nửa tròn+HCN...) | `hinh_ds10_ch06.py` | method | — |
| `tam_giac_toa_do(a=2.0, ten_O='O', ten_A='A', ten_B='B', ten_H='H', nhan_h='h', hien_duong_cao=True, out='tamgiac_td', tra_bytes=False, scale=1.0)` | TAM GIÁC VUÔNG OAB TRÊN HỆ Oxy (H5.5) | `hinh_ds11_giaitich.py` | method | — |
| `thiet_dien(*dinh, mau='cyan!16', net='lien', mau_vien=None)` | Tô + viền đa giác THIẾT DIỆN theo các đỉnh (tên) đã đặt | `hinh_hh11_ch04.py` | method | — |
| `tia_so_vi_tri(ten_truc='s', xP=3.0, xQ=7.0, L=9.0, nhan_P='Vị trí tại $t_0$', nhan_Q='Vị trí tại $t$', nhan_doan='$s(t)-s(t_0)$', out='tia_vitri', tra_bytes=False, scale=1.0)` | TIA SỐ VỊ TRÍ VẬT (H9.2 — minh họa quãng đường đi được từ t0 đến t) | `hinh_ds11_giaitich.py` | method | — |
| `to_mien(ham, a, b, ham2=None, nhan_ham=None, nhan_ham2=None, xmin=-1.0, xmax=5.0, ymin=-1.0, ymax=6.0, mau='blue', mau2='red!70!black', mau_to='blue!12', nhan_can=('a', 'b'), hien_can=True, nhan_mien=None, nhan_mien_xy=None, nhan_pos=0.55, xtick=None, xticklabels=None, ytick=None, yticklabels=None, samples=200, width=8.0, height=7.0, out='tomien', tra_bytes=False, scale=1.0)` | TÔ MIỀN DIỆN TÍCH tích phân (pgfplots) — chuẩn SGK Giải tích 12 (Bài 12 hình thang cong · Bài 13 diện tích) | `hinh_ds12_giaitich.py` | method | — |
| `trong_tam(ten, *dinh, nhan='right', moc=True, mau=None)` | Đặt TRỌNG TÂM của các đỉnh đã có (trung bình toạ độ — chiếu affine nên trùng trọng tâm hình học) | `hinh_hh12_ch02.py` | method | — |
| `truc_so_tap_hop(cac_khoang, out='truc_tap', tra_bytes=False, chuThich=None)` | TRỤC SỐ biểu diễn tập con của R: khoảng/đoạn/nửa khoảng/tia (giấu toạ độ vẽ) | `hinh_tap_hop.py` | method | — |
| `trung_diem(M, A, B, mau=None)` | M = TRUNG ĐIỂM đoạn AB | `hinh_hh12_ch02.py` | method | — |
| `tu_dien(nhan='ABCD', dinh_tren=None, canh=3.0, goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=False)` | TỨ DIỆN phối cảnh chuẩn — 4 đỉnh, 6 cạnh (1 cạnh đáy sau KHUẤT nét đứt) | `hinh_hh12_ch02.py` | method | — |
| `tu_dien(nhan='ABCD', dinh_tren=None, canh=3.0, goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=True)` | TỨ DIỆN phối cảnh chuẩn — 4 đỉnh, 6 cạnh (1 cạnh đáy sau KHUẤT nét đứt) | `hinh_hh11_ch04.py` | method | — |
| `vat_phong_dung(nhan_v0='$\\vec{v}_0$', nhan_h='h', ten_O='O', H=3.0, out='vat_phong', tra_bytes=False, scale=1.0)` | SƠ ĐỒ VẬT PHÓNG THẲNG ĐỨNG (H9.7, B32 mở đầu) | `hinh_ds11_giaitich.py` | method | — |

## Đa giác  · 24 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `chu_so_7doan(so, x0=0.0, y0=0.0, rong=1.0, cao=2.0, mau=None, rong_net='dam')` | CHỮ SỐ kiểu 7-ĐOẠN (0..9) — cho bài TÂM đối xứng (lật nửa vòng 6↔9, giữ 0/1/2/5/8) | `hinh_dagiac.py` | method | — |
| `da_giac_canh_goc(ten, canh, goc, goc_o=(0.0, 0.0), huong_dau=0.0, chieu=-1, khep=False, nhan_canh=None, danh_dau_goc=True)` | ĐƯỜNG GẤP KHÚC / ĐA GIÁC dựng theo chuỗi CẠNH + GÓC TRONG (đi quanh chu vi) | `hinh_dagiac.py` | method | — |
| `da_giac_deu(*ten, canh=2.0, xoay=0, to=None)` | Đa giác đều n cạnh (n = số tên truyền vào ≥ 3), đỉnh theo chiều kim đồng hồ, một cạnh nằm ngang phía trên khi xoay=0 | `hinh_dagiac.py` | method | — |
| `da_giac_vuong(ten, buoc, nhan='below right', cham=True, goc_o=(0.0, 0.0))` | Đa giác mọi cạnh song song trục (góc vuông) — hình chữ L, bậc thang, mặt bằng | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_qua_trung_truc(new, P, A, B, nhan='above', mau=None)` | Đặt 'new' = ẢNH của P qua ĐƯỜNG TRUNG TRỰC của đoạn AB (phản chiếu biến A↔B) | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_tam(new, P, O, nhan='below', mau=None)` | Đặt điểm 'new' = ẢNH của P qua TÂM ĐỐI XỨNG O (phép đối xứng tâm) — new = 2·O − P, tức O là TRUNG ĐIỂM của đoạn P–new | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_truc(new, P, A, B, nhan='above right', mau=None)` | Đặt điểm 'new' = ẢNH của điểm P qua TRỤC (đường thẳng) AB — phản chiếu | `hinh_dagiac.py` | method | — |
| `hinh_thang(A, B, Cc, D, day_tren=3.0, day_duoi=5.0, cao=2.5, lech=0.8)` | Hình THANG thường: A,B = đáy trên (day_tren); D,C = đáy dưới (day_duoi); AB ∥ DC (PHANH song_song) | `hinh_dagiac.py` | generator | — |
| `hinh_thang_can(A, B, Cc, D, day_nho=3.0, day_lon=5.0, cao=2.5, cheo=False)` | Hình thang cân đối xứng qua trục dọc: A,B = đáy nhỏ (trên); D,C = đáy lớn (dưới) | `hinh_dagiac.py` | generator | — |
| `hinh_thoi(A, B, Cc, D, a=4, b=3, cheo=True, tam='O')` | Hình thoi "kim cương" dựng theo 2 nửa chéo NGUYÊN ô → tâm + 4 đỉnh rơi NÚT lưới | `hinh_dagiac.py` | generator | — |
| `hinh_vuong(M, N, P_, Q, canh=4, goc_o=(0.0, 0.0), cham=True)` | Hình VUÔNG: M dưới-trái, N trên-trái, P trên-phải, Q dưới-phải | `hinh_dagiac.py` | generator | — |
| `la_ban(goc_O='O', huong=None, dai=3.0, scale=1.0, out='la_ban', tra_bytes=False, chuThich=None)` | LA BÀN định hướng hàng hải — trục N–S (dọc) & W–E (ngang) giao tại O, nhãn 4 phương; mỗi 'tia hướng' theo quy ước Sα°E / Nα°W… + cung góc α với trục m | `hinh_dagiac.py` | method | — |
| `lat_kin_luc_giac(tam='O', canh=1.6, so_hinh=3, xoay=0)` | LÁT KÍN tổ ong: so_hinh lục giác đều cạnh 'canh' ghép khít quanh MỘT điểm chung 'tam' (mỗi góc trong 120° tại tâm; so_hinh × 120° phủ quanh tâm — với  | `hinh_dagiac.py` | method | — |
| `luc_giac_deu(A, B, Cc, D, E, F, canh=2.0, xoay=0, cheo=None, tam=None)` | Lục giác đều 6 đỉnh, thứ tự A→B→C→D→E→F theo chiều kim đồng hồ | `hinh_dagiac.py` | method | — |
| `ngoi_sao(tam, so_canh=5, ban_kinh=2.0, xoay=90, ti_le_trong=None, to=None, nhan=None, cham_tam=False)` | NGÔI SAO so_canh cánh (mặc định 5 — cờ VN/Quốc kỳ; dùng cả 4/6/8 cánh cho Chương V) | `hinh_dagiac.py` | method | — |
| `phoi_canh(O, bo_diem, k, noi_canh=None, net_tia='dut', mau_tia=None, nhan_O='below left', kin=False, to_nguon=None, to_anh=None)` | HÌNH PHỐI CẢNH / VỊ TỰ tâm O tỉ số k (Bài 37 — hình đồng dạng phối cảnh) | `hinh_dagiac.py` | method | — |
| `so_do_tu_duy(trung_tam, nhanh, mau='blue', scale=1.0, out='so_do_tu_duy', tra_bytes=False)` | SƠ ĐỒ TƯ DUY KẺ KHUNG (hộp chữ nhật phân cấp, nối đường) — mục ② TỔNG KẾT / ÔN TẬP CHƯƠNG | `hinh_dagiac.py` | method | — |
| `tam_giac(A, B, Cc, noi=True, goc_o=(0.0, 0.0))` | Tam giác 3 đỉnh (không thẳng hàng) | `hinh_dagiac.py` | method | — |
| `tam_giac_can(A, B, Cc, canh_ben=3.0, day=2.4, danh_dau=True, goc_o=(0.0, 0.0))` | Tam giác CÂN tại đỉnh A (A đỉnh trên; B–C đáy nằm ngang, B trái–C phải) | `hinh_dagiac.py` | method | — |
| `tam_giac_canh(A, B, Cc, AB, BC, CA, goc_o=(0.0, 0.0))` | Tam giác ABC dựng từ 3 CẠNH cho sẵn (SSS): |AB|, |BC|, |CA| (đơn vị bất kỳ, giữ ĐÚNG TỈ LỆ) | `hinh_dagiac.py` | method | — |
| `tam_giac_deu(A, B, Cc, canh=3.0, xoay=0, goc_o=(0.0, 0.0))` | Tam giác ĐỀU 3 đỉnh: B dưới-trái, C dưới-phải, A đỉnh trên | `hinh_dagiac.py` | method | — |
| `tam_giac_goc(A, B, Cc, goc_B, goc_C, day=4.0, goc_o=(0.0, 0.0), an_nhan=False)` | Tam giác ABC với GÓC cho sẵn: góc tại B = goc_B, góc tại C = goc_C (góc A tự = 180 − goc_B − goc_C) | `hinh_dagiac.py` | method | — |
| `tu_giac(A, B, Cc, D, loai=None)` | Tứ giác 4 đỉnh lồi, chiều kim đồng hồ | `hinh_dagiac.py` | method | — |
| `tu_giac_goc(A, B, Cc, D, goc_A, goc_B, goc_C, ab=4.0, bc=3.0, chieu=-1, goc_o=(0.0, 0.0), danh_dau_goc=False)` | Tứ giác LỒI ABCD biết GÓC TRONG tại A, B, C (góc D tự = 360 − tổng) | `hinh_dagiac.py` | method | — |

## Số & Đại số (tia số/trục số/toạ độ/diện tích đại số)  · 2 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `dung_can_hai(canh=2, nhan_diem='A', nhan_can=None)` | DỰNG √2 TRÊN TRỤC SỐ bằng compa — SGK Toán 7 Hình 2.3 (2 panel a/b) | `hinh_daiso.py` | method | L6→9→THPT |
| `hinhDienTichDaiSo(kieu='catghep', nhan=None, chuThich=None, out='dientich_daiso', tra_bytes=False)` | HÌNH DIỆN TÍCH đại số (nhãn BIẾN, giấu toạ độ) | `hinh_daiso.py` | generator | L6→9→THPT |

## Đối xứng  · 2 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `tam_doi_xung(O, *cap_doi_dinh, nhan='O', ve_cheo=True, net='dut')` | TÂM ĐỐI XỨNG O = giao các đường chéo (chấm + nhãn O) | `hinh_doixung.py` | method | — |
| `truc_doi_xung(diem1, diem2, nhan=None, net='dut')` | TRỤC ĐỐI XỨNG: đường thẳng NÉT ĐỨT màu ĐEN, tự kéo dài đều ~15% ra ngoài mỗi đầu (thò ra như SGK) | `hinh_doixung.py` | method | — |

## Góc & đường thẳng  · 2 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `cat_tuyen_2duong(a='a', b='b', c='c', A='A', B='B', song_song=True, xoay_ab=8, xoay_c=108, khoang=1.9, danh_so=True, nhan_dinh=True, danh_dau_ss=False, rut_c_tren=0.5, dai=2.2)` | Cát tuyến c cắt đường a (trên) tại A và đường b (dưới) tại B | `hinh_gocdt.py` | method | — |
| `hai_duong_cat_4goc(ten1='xx′', ten2='yy′', O='O', xoay1=10, xoay2=105, danh_so=True, nhan_dinh=True, prefix='', dai=2.2)` | Hai đường thẳng ten1, ten2 cắt nhau tại đỉnh O | `hinh_gocdt.py` | method | — |

## Khối tròn xoay (trụ · nón · cầu)  · 15 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `bon_xang(R=1.0, L=3.2, nhan=None, out='bon_xang', tra_bytes=False)` | BỒN NẰM NGANG — trụ nằm ngang dài L + 2 NỬA CẦU hai đầu (H10.32). | `hinh_hh9_ch10.py` | method | — |
| `cat_cau(R=1.7, cao=0.0, nhan_mc='R', qua_tam=True, tam='O', nhan_mp='(P)', out='cat_cau', tra_bytes=False)` | MẶT CẦU cắt bởi mặt phẳng → mặt cắt là hình tròn | `hinh_hh9_ch10.py` | method | — |
| `hcn_quay(R=1.3, h=2.8, ten=("O'", 'A', 'B', 'O'), hien_tru=True, out='hcn_quay', tra_bytes=False)` | HÌNH CHỮ NHẬT quay quanh một CẠNH (trục đứng) sinh HÌNH TRỤ (H10.3) | `hinh_hh9_ch10.py` | method | — |
| `hinh_cau(R=1.6, nhan_R=None, tam='O', hien_tam=True, hien_xichdao=True, duong_kinh=None, diem=None, out='cau', tra_bytes=False)` | HÌNH CẦU / MẶT CẦU phối cảnh (viền tròn + xích đạo elip) | `hinh_hh9_ch10.py` | generator | — |
| `hinh_non(R=1.6, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None, dinh='S', tam='O', trai='A', phai='B', hien_dinh_ten=True, hien_tam=True, hien_trai_phai=False, o_vuong=True, out='non', tra_bytes=False)` | HÌNH NÓN phối cảnh đứng (đỉnh trên, đáy elip, 2 đường sinh biên) | `hinh_hh9_ch10.py` | generator | — |
| `hinh_tru(R=1.4, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None, tam_tren="O'", tam_duoi='O', dinh_tren=None, dinh_duoi=None, hien_truc=True, out='tru', tra_bytes=False)` | HÌNH TRỤ phối cảnh đứng (2 đáy elip + 2 đường sinh biên) | `hinh_hh9_ch10.py` | generator | — |
| `khai_trien_non(R=1.0, l=2.6, nhan_l=None, nhan_R=None, dinh='S', out='kt_non', tra_bytes=False)` | KHAI TRIỂN hình nón = hình quạt tròn (bán kính l, cung = 2πR) + hình tròn đáy (bán kính R). | `hinh_hh9_ch10.py` | method | — |
| `khai_trien_tru(R=0.9, h=2.4, nhan_cv=None, nhan_h=None, nhan_R=None, out='kt_tru', tra_bytes=False)` | KHAI TRIỂN hình trụ = hình chữ nhật (rộng = chu vi 2πR, cao = h) + 2 hình tròn đáy. | `hinh_hh9_ch10.py` | method | — |
| `non_trong_lapphuong(a='a', canh=3.2, dinh='O', out='non_lapphuong', tra_bytes=False)` | HÌNH NÓN nội tiếp trong LẬP PHƯƠNG (H10.38): đỉnh = tâm O mặt trên ABCD, đáy = hình tròn nội tiếp mặt đáy A'B'C'D' (tiếp xúc 4 cạnh) | `hinh_hh9_ch10.py` | method | — |
| `nua_cau_non(R=1.2, h_non=2.4, nhan=None, up=True, out='nuacau_non', tra_bytes=False)` | GHÉP: NÓN + NỬA CẦU chung đáy — ốc quế kem (H10.39): nón chúc XUỐNG, vòm cầu trên | `hinh_hh9_ch10.py` | method | — |
| `nua_cau_tru(R=1.3, h=2.2, nhan=None, out='nuacau_tru', tra_bytes=False)` | GHÉP: hình TRỤ (dưới) + NỬA HÌNH CẦU (vòm trên) — H10.37a. | `hinh_hh9_ch10.py` | method | — |
| `tamgiac_quay(R=1.5, h=2.8, ten=('S', 'O', 'A'), hien_non=True, o_vuong=True, out='tg_quay', tra_bytes=False)` | TAM GIÁC VUÔNG quay quanh CẠNH GÓC VUÔNG (trục đứng) sinh HÌNH NÓN (H10.9a) | `hinh_hh9_ch10.py` | method | — |
| `tru_khoan_non(R=1.3, h=2.4, nhan=None, out='tru_khoan_non', tra_bytes=False)` | HÌNH TRỤ bị KHOAN mất phần hình NÓN (đáy nón = đáy trên trụ, đỉnh ở tâm đáy dưới) — H10.28. | `hinh_hh9_ch10.py` | method | — |
| `tru_non(R=1.3, h_tru=2.0, h_non=1.8, nhan=None, out='tru_non', tra_bytes=False)` | GHÉP: hình TRỤ (dưới) + hình NÓN (trên, chung đáy) — H10.16 dụng cụ | `hinh_hh9_ch10.py` | method | — |
| `vong_bi(R=1.6, r=0.9, h=1.3, nhan=None, out='vong_bi', tra_bytes=False)` | VÒNG BI / ỐNG TRỤ RỖNG — trụ ngoài R khoét trụ trong r, cao h (H10.30). | `hinh_hh9_ch10.py` | method | — |

## Hoá học  · 8 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `hop_hat(items, nhan=None, out='hoa2_hop', tra_bytes=False)` | Hộp chữ nhật chứa 'hạt' trừu tượng để phân loại đơn/hợp chất/hỗn hợp | `hinh_hoa_ch02.py` | method | — |
| `lien_ket_cht(cong_thuc, out='hoa2_cht', tra_bytes=False)` | Sơ đồ liên kết cộng hoá trị (dùng chung cặp electron): H2,Cl2,N2,O2,HCl,H2O | `hinh_hoa_ch02.py` | method | — |
| `lien_ket_ion(cho_Z, cho_ch, cho_ten, nhan_Z, nhan_ch, nhan_ten, so_e, ion_duong, ion_am, out='hoa2_ion', tra_bytes=False)` | Sơ đồ: nguyên tử KIM LOẠI (cho) nhường so_e electron cho nguyên tử PHI KIM (nhan) → ion dương + ion âm | `hinh_hoa_ch02.py` | method | — |
| `mo_hinh_hanh_tinh(out='hoa_hanhtinh', tra_bytes=False)` | Mô hình hành tinh Rutherford: hạt nhân dương ở tâm, electron trên NHIỀU quỹ đạo elip nghiêng | `hinh_hoa_ch01.py` | method | — |
| `mo_hinh_hat(loai, nguyen_to=None, cong_thuc=None, ion_duong=None, ion_am=None, out='hoa2_hat', tra_bytes=False)` | Mô hình HẠT của một mẫu chất | `hinh_hoa_ch02.py` | method | — |
| `nguyen_tu_bo(Z, cau_hinh, nhan=None, hien_e=True, out='hoa_ntbo', tra_bytes=False)` | Mô hình Bohr: hạt nhân tâm ghi +Z; vòng đồng tâm = số lớp trong cau_hinh; e là chấm phân bố đều trên mỗi vòng (từ trong ra ngoài) | `hinh_hoa_ch01.py` | method | — |
| `nguyen_tu_hat_nhan(so_p, so_n, cau_hinh_vo, nhan=None, out='hoa_nthn', tra_bytes=False)` | Mô hình chi tiết: hạt nhân vẽ RÕ các quả cầu proton (màu p) + neutron (màu n) + vỏ electron (chấm màu e) trên vòng theo cau_hinh_vo | `hinh_hoa_ch01.py` | method | — |
| `phan_tu(cong_thuc, out='hoa2_pt', tra_bytes=False)` | Mô hình quả cầu-que của 1 phân tử (lớp 7): H2,Cl2,O2,N2,HCl,CO2,H2O,CH4,NH3 | `hinh_hoa_ch02.py` | method | — |

## Khối / không gian  · 11 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `khai_trien_chop(loai, a, b, nhan=None, nhan_canh_ben=None, goc_o=(0.0, 0.0), ten='KC')` | KHAI TRIỂN (net) HÌNH CHÓP ĐỀU — đáy đa giác đều ở GIỮA + các mặt bên là tam giác cân GẤP RA NGOÀI mỗi cạnh đáy (H10.4·10.14·10.20·10.26·10.39 · SBT 1 | `hinh_khoihop.py` | method | — |
| `khai_trien_hop(dai, rong, cao, nhan=None, so_mat=False, goc_o=(0.0, 0.0), ten='KT')` | KHAI TRIỂN (net) HÌNH HỘP CHỮ NHẬT dạng CHỮ THẬP (H10.4 · H10.6): 4 mặt bên thành DẢI ngang (rộng dai·rong·dai·rong, cao=cao) + mặt TRÊN & DƯỚI gắn và | `hinh_khoihop.py` | method | — |
| `khai_trien_lang_tru(day, cao, nhan_cao=None, so_mat=False, goc_o=(0.0, 0.0), ten='KL')` | KHAI TRIỂN (net) LĂNG TRỤ ĐỨNG đáy đa giác (H10.22 · H10.24 · H10.32): DẢI n mặt bên hình chữ nhật (rộng = độ dài từng CẠNH ĐÁY, cao = chiều cao lăng  | `hinh_khoihop.py` | method | — |
| `khoiLapPhuongKhoetGoc(canhLon='2x+3', canhCon='x+1', chuThich=None, out='khoi_khoet_goc', tra_bytes=False, S=4.0, a=1.6)` | KHỐI LẬP PHƯƠNG cạnh 'canhLon' khoét 1 khối lập phương cạnh 'canhCon' ở góc TRÊN-TRƯỚC-PHẢI (phối cảnh xiên cavalier) | `hinh_khoihop.py` | method | — |
| `khoi_ghep_lapphuong(danh_sach_o, goc_o=(0.0, 0.0), ten='GL')` | KHỐI GHÉP từ các LẬP PHƯƠNG ĐƠN VỊ đặt theo Ô NGUYÊN (x,y,z) — gốc (0,0,0) (H10.11 bài 10.1 đếm khối · H10.18 khay đá) | `hinh_khoihop.py` | method | — |
| `khoi_hop_chia_o(dai, rong, cao, o_roi=True, nhan_donvi='1 dm', goc_o=(0.0, 0.0), ten='CO')` | KHỐI HỘP CHỮ NHẬT chia dai×rong×cao Ô ĐƠN VỊ (H10.8 — giới thiệu thể tích: hộp 5×2×4) | `hinh_khoihop.py` | method | — |
| `khoi_hop_chu_nhat(dai, rong, cao, nhan=None, to_day=False, nhan_day=None, an_nap=False, goc_o=(0.0, 0.0), ten='K')` | KHỐI HỘP CHỮ NHẬT phối cảnh xiên (cạnh khuất nét đứt) — chuẩn SGK | `hinh_khoihop.py` | method | — |
| `khoi_hop_ghep(danh_sach_khoi, goc_o=(0.0, 0.0), ten='HG')` | KHỐI GHÉP từ nhiều HỘP CHỮ NHẬT kích thước TỰ DO (H10.35 — 2 lăng trụ ghép hình chữ L) | `hinh_khoihop.py` | method | — |
| `khoi_lap_phuong_chia_o(n, o_roi=True, nhan_donvi='1 dm', goc_o=(0.0, 0.0), ten='CO')` | KHỐI LẬP PHƯƠNG chia n×n×n Ô ĐƠN VỊ (trường hợp riêng của khoi_hop_chia_o, dai=rong=cao=n). | `hinh_khoihop.py` | method | — |
| `lang_tru_dung(day, cao, huong='ngang', sau='phai', nhan_canh_ben=None, ten_dinh=None, chu_thich=None, to_day=False, goc_o=(0.0, 0.0), ten='L')` | LĂNG TRỤ ĐỨNG đáy ĐA GIÁC bất kỳ — phối cảnh xiên, NÉT KHUẤT tự tính theo che | `hinh_khoihop.py` | method | — |
| `net_hop_cat_goc(dai, rong, canh_goc, nhan=None, to_goc=True, goc_o=(0.0, 0.0), ten='N')` | NET (khai triển 2D) miếng bìa chữ nhật CẮT 4 GÓC hình vuông → gấp thành hộp | `hinh_khoihop.py` | method | — |

## Toạ độ & trục số (DÙNG CHUNG)  · 8 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `hinhMatPhangToaDo(xRange=(-5, 5), yRange=(-5, 5), buoc=1, luoi=True, duongThang=None, diem=None, vecto=None, chuThich=None, cungGoc=None, chanVuongGoc=None, duongTron=None, tiepTuyen=None, doan=None, elip=None, hypebol=None, parabol=None, scale=0.72, out='mp_toado', tra_bytes=False)` | MẶT PHẲNG TOẠ ĐỘ Oxy — trục có mũi tên + nhãn O,x,y; lưới mờ tuỳ chọn; đồ thị ĐƯỜNG THẲNG (theo phương trình / 2 điểm) + ĐIỂM có nhãn + đường gióng né | `hinh_toado.py` | generator | L6→9→THPT |
| `kim_tu_thap(hang, o_canh=0.95)` | KIM TỰ THÁP SỐ (2D) — tháp ô vuông, ô trên gối lệch nửa ô giữa 2 ô dưới | `hinh_toado.py` | method | L6→9→THPT |
| `nhiet_ke_cot(cot, thang=(-20, 50), buoc=10, don_vi='°C', hien_muc_so=False)` | NHIET KE COT — nhieu thang do DUNG canh nhau, doc muc thuy ngan | `hinh_toado.py` | method | L6→9→THPT |
| `tia_diem(*args, **kwargs)` | [Đại số] sơ đồ điểm trên đường thẳng — NỀN SẠCH (base hinh_coban mặc định có lưới). | `hinh_toado.py` | method | L6→9→THPT |
| `tia_so(gia_tri_max=None, buoc=1, diem=None, hien_nhan_diem=True, moc_nhan=None, ti_le=True, mui_ten=True, goc_ten='O', nhay=None)` | TIA SỐ tự nhiên — gốc bên trái, mũi tên sang phải; vạch chia + nhãn số + điểm đánh dấu | `hinh_toado.py` | method | L6→9→THPT |
| `truc_do_chinh_xac(trai, phai, a, do_chinh_xac=None, nhan_a='a')` | TRỤC SỐ 'ĐỘ CHÍNH XÁC LÀM TRÒN' — đoạn cục bộ [trai; phai] (KHÔNG cần gốc 0) | `hinh_toado.py` | method | L6→9→THPT |
| `truc_doan_doc_diem(trai, phai, chia=10, diem=None, hien_nhan_diem=False, moc_nhan=None)` | TRỤC SỐ ĐOẠN PHÓNG TO để ĐỌC ĐIỂM — biên THẬP PHÂN, chia nhỏ, kéo rộng | `hinh_toado.py` | method | L6→9→THPT |
| `truc_so_huu_ti(tu=-1, den=4, chia=1, diem=None, hien_nhan_diem=True, moc_nhan=None, mui_ten_am=False, goc_ten='0', khoang_to=None, vach_dut=None, mui_ten_dc=None, ti_le=True)` | TRỤC SỐ biểu diễn số hữu tỉ — gốc O ở giá trị 0, có phần âm & dương | `hinh_toado.py` | method | L6→9→THPT |

## Đường tròn (dựng)  · 19 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `cung(tam, goc_dau, goc_cuoi, mau='red', net='lien', ban_kinh=None)` | CUNG của đường tròn tâm 'tam', quét từ 'goc_dau' đến 'goc_cuoi' (độ, góc ở tâm) | `hinh_tron_ve.py` | method | — |
| `cung_qua(tam, qua, ban_kinh=None, mo=28, mau='black', net='dut')` | Vẽ CUNG NGẮN của đường tròn tâm 'tam' ĐI QUA điểm 'qua' — đánh dấu chỗ giao compa, KHÔNG vẽ trọn đường tròn | `hinh_tron_ve.py` | method | — |
| `diem_ban_kinh(ten, tam, goc, ban_kinh, nhan='above right', mau=None, hien=True)` | Điểm 'ten' cách tâm 'tam' đúng 'ban_kinh' (đơn vị vẽ) theo hướng 'goc' (độ, ngược chiều kim từ ngang) — KHÔNG tọa độ | `hinh_tron_ve.py` | method | — |
| `diem_tren_tron(ten, tam, goc_o_tam, nhan='above right', mau=None)` | Điểm 'ten' NẰM TRÊN đường tròn tâm 'tam', định vị bằng GÓC Ở TÂM 'goc_o_tam' (độ, đo ngược chiều kim đồng hồ từ hướng ngang) — KHÔNG tọa độ | `hinh_tron_ve.py` | method | — |
| `duong_tron(tam, ban_kinh=2.0, mau=None, net='lien', hien_tam=True)` | ĐƯỜNG TRÒN tâm 'tam', bán kính 'ban_kinh' (đơn vị vẽ) | `hinh_tron_ve.py` | method | — |
| `duong_tron_ngoai_tiep(A, B, C, tam='O', mau=None, net='lien', hien_tam=True, noi_tam=False)` | ĐƯỜNG TRÒN NGOẠI TIẾP tam giác A,B,C (3 đỉnh ĐÃ đặt, không thẳng hàng) | `hinh_tron_ve.py` | method | — |
| `duong_tron_noi_tiep(A, B, C, tam='I', mau=None, net='lien', hien_tam=True, chan_vuong=False)` | ĐƯỜNG TRÒN NỘI TIẾP tam giác A,B,C (3 đỉnh ĐÃ đặt) | `hinh_tron_ve.py` | method | — |
| `duong_tron_qua(tam, qua, mau=None, net='lien', hien_tam=True)` | ĐƯỜNG TRÒN tâm 'tam' đi QUA điểm 'qua' (cả hai ĐÃ đặt) | `hinh_tron_ve.py` | method | — |
| `goc_o_tam(tam, A, B, do=None, danh_dau=True)` | Góc ở tâm chắn bởi 2 bán kính 'tam'A, 'tam'B (A,B đã đặt trên đường tròn) | `hinh_tron_ve.py` | method | — |
| `hai_tiep_tuyen(tam, M, A='A', B='B', mau=None, o_vuong=True, noi_tam=False)` | HAI TIẾP TUYẾN kẻ từ điểm 'M' NẰM NGOÀI đường tròn 'tam': tạo hai tiếp điểm A, B trên đường tròn + vẽ hai đoạn MA, MB | `hinh_tron_ve.py` | method | — |
| `hinh_quat(tam, A, B, mau='cyan!18', vien=True)` | TÔ MÀU HÌNH QUẠT TRÒN giới hạn bởi cung nhỏ AB và hai bán kính (tam)A, (tam)B (A,B đã đặt trên đường tròn) | `hinh_tron_ve.py` | generator | — |
| `kim(R, vi_tri, loai='gio', tam='O')` | Vẽ MỘT kim đồng hồ từ tâm 'tam' ra hướng 'vi_tri' (thang 12 giờ, cho phép LẺ: vd 3.5 = giữa số 3 và 4) | `hinh_tron_ve.py` | method | — |
| `mat_dong_ho(gio=None, phut=0, giay=None, R=2.4, tam='O')` | ĐỒNG HỒ chuẩn HH6 — MỘT hàm ra đồng hồ hoàn chỉnh: vành tròn tâm 'tam' + 12 số (đặt bằng diem_tren_tron, nhãn toả ra ngoài) + tuỳ chọn các kim | `hinh_tron_ve.py` | method | — |
| `nua_duong_tron_don_vi(diem=None, R=3.0, scale=1.0, nhan_ABC=False, chuThich=None, out='nua_dt_don_vi', tra_bytes=False)` | NỬA ĐƯỜNG TRÒN ĐƠN VỊ (định nghĩa GTLG góc 0°–180°, SGK H3.2–3.6) | `hinh_tron_ve.py` | method | — |
| `so_quanh_tam(tam, ban_kinh, danh_sach, goc_dau=90, chieu=-1)` | Rải các nhãn 'danh_sach' ĐỀU quanh tâm 'tam' trên vòng bán kính 'ban_kinh', bắt đầu ở hướng 'goc_dau'° (mặc định 90 = trên đỉnh), bước 'chieu'*360/n ( | `hinh_tron_ve.py` | method | — |
| `tiep_tuyen(tam, tiep_diem, dai=1.7, mau=None, net='lien', o_vuong=False)` | TIẾP TUYẾN của đường tròn 'tam' tại 'tiep_diem' (đã đặt TRÊN đường tròn) — đoạn thẳng qua tiếp điểm, VUÔNG GÓC bán kính, nửa dài 'dai' mỗi phía | `hinh_tron_ve.py` | method | — |
| `tiep_tuyen_chung(tam1, tam2, loai='ngoai', phia=1, mau=None, net='lien', tiep1='T', tiep2='T2', dai=0.7)` | TIẾP TUYẾN CHUNG NGOÀI của hai đường tròn 'tam1','tam2' (đã khai): tạo hai tiếp điểm tiep1∈(tam1), tiep2∈(tam2) + vẽ đường tiếp tuyến qua chúng (kéo d | `hinh_tron_ve.py` | method | — |
| `vanhKhan(R='R', r='r', toVanh=True, chuThich=None, nua=False, out='vanh_khan', tra_bytes=False)` | VÀNH KHĂN — hai đường tròn đồng tâm tâm O; bán kính ngoài R, trong r (r<R), mỗi bán kính có nhãn ĐẶT GIỮA đoạn; vành giữa tô nhạt (toVanh) | `hinh_tron_ve.py` | method | — |
| `vien_phan(tam, A, B, mau='cyan!18', vien=True)` | TÔ MÀU HÌNH VIÊN PHÂN giới hạn bởi dây AB và cung nhỏ AB (A,B trên đường tròn 'tam') | `hinh_tron_ve.py` | method | — |

## Dựng Word (template JS v10.50)  · 87 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `approxLen(item)` | Ước lượng độ dài hiển thị — dùng để quyết định xếp cột/xuống hàng (công thức Math không có .length nên tính tượng trưng 3 ký tự) | `hieuhoc_template.js` | JS | — |
| `baiTapTaiLop({ soBai, mucDo, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai, anLoiGiai, dai = false })` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `bangDapAnPhanI(dapAnArr)` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `bangDungSai(menhDeArr, opts = {})` | 14. BẢNG ĐÚNG/SAI — tỉ lệ CỐ ĐỊNH 80%-10%-10%, nền trắng chữ đen | `hieuhoc_template.js` | JS | — |
| `bangNguonGoc({ soChuong, dsNguon })` | — | `hieuhoc_template.js` | JS | — |
| `bangSoLieu(duLieu, opts = {})` | [28r] 14b. BẢNG SỐ LIỆU TỔNG QUÁT — dữ liệu thực tiễn nhiều cột (dân số, tuổi thọ, hồ, hành tinh, khí hiếm, pizza…) — DS7 dày bảng. GỐC: kho chỉ có bả | `hieuhoc_template.js` | JS | — |
| `canBac(soHang, bacCan = 2)` | — | `hieuhoc_template.js` | JS | — |
| `cauTracNghiem({ soCau, cauHoi, dapAn, thamChieu })` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `chiSoDuoi(coSo, chiSo)` | — | `hieuhoc_template.js` | JS | — |
| `danDungSai(soCau, moTa)` | [28m] DÒNG DẪN Đúng/Sai — nhãn "Câu N." TỰ ĐẬM (khớp nhãn câu template tự sinh ở cauTracNghiem/traLoiNgan/tự luận). GỐC: dòng dẫn Đ/S trước đây dựng T | `hieuhoc_template.js` | JS | — |
| `dangToanDayDu({ saiLamArr, soDang, ghiNhoArr, viDuLoiGiai, loiGiaiND, tenDang, ma, viDuDeBai, viDuCacCau, viDuThamChieu, viDuCoHinh, viDuHinhBenPhai, viDuHinhBenTrai, phanTich, soBai, mucDo, deBai, cacCau, thamChieu })` | Gộp toàn bộ 1 Dạng toán thành 1 lệnh gọi duy nhất — khuyến khích AI Soạn dùng hàm này | `hieuhoc_template.js` | JS | — |
| `doDaiBieuThuc(bieuThuc)` | [33k] Chỉ đạo: vá backlog |a⃗ ± b⃗| (mảng A5 luyện thi _LT). Độ dài của BIỂU THỨC vectơ bất kỳ (nhiều vectơ + toán tử), KHÁC doDaiVecto(1 tên). doDaiB | `hieuhoc_template.js` | JS | — |
| `doDaiVecto(ten)` | [33k] Chỉ đạo: vá backlog |a⃗ ± b⃗| (mảng A5 luyện thi _LT). Độ dài của BIỂU THỨC vectơ bất kỳ (nhiều vectơ + toán tử), KHÁC doDaiVecto(1 tên). doDaiB | `hieuhoc_template.js` | JS | — |
| `footerTPC()` | Footer riêng cho tờ phân chương (khác footer file bài học — không số trang) | `hieuhoc_template.js` | JS | — |
| `ghiChuGiangDay({ dsLopBai } = {})` | — | `hieuhoc_template.js` | JS | — |
| `ghiNhoNhanh(dongArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `gioiHan(duoi, than)` | [33b] TOÁN TỬ GTLN–GTNN: min/max với CHỈ SỐ DƯỚI (limLow) — chuẩn SGK $\min\limits_{D} f(x)$. Mirror gioiHan nhưng tên toán tử truyền vào (ten='min'|' | `hieuhoc_template.js` | JS | — |
| `hangHinh(items, { caoCm = 3.2, _tuLuoi = false } = {})` | 22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4] HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa. `hangHinh`: 1 hàng ≤3  | `hieuhoc_template.js` | JS | — |
| `hePhuongTrinh(danhSachPT)` | [31q] TUYỂN NGHIỆM — ngoặc vuông "[" (HOẶC) cho nghiệm phương trình LG Mirror hePhuongTrinh nhưng begChr="[" (tuyển: x=... HOẶC x=...). KHÁC hệ "{" (đ | `hieuhoc_template.js` | JS | — |
| `headerDeKiemTra({ tenDe, phut })` | 16. HEADER ĐỀ KIỂM TRA (tên đề + thời gian + bảng Họ tên/Điểm/NX) | `hieuhoc_template.js` | JS | — |
| `headerFooterBaiHoc({ soBai, tenBai, lop })` | header/footer trang Word cho ĐỀ KIỂM TRA — ĐÚNG MẪU headerFooterBaiHoc, KHÔNG làm khác. Chỉ thay định danh: "Bài n. Tên | Lớp" → tên đề (dạng thường,  | `hieuhoc_template.js` | JS | — |
| `headerFooterDeKT({ tenDe })` | header/footer trang Word cho ĐỀ KIỂM TRA — ĐÚNG MẪU headerFooterBaiHoc, KHÔNG làm khác. Chỉ thay định danh: "Bài n. Tên | Lớp" → tên đề (dạng thường,  | `hieuhoc_template.js` | JS | — |
| `headerRong()` | Header rỗng — dùng để NGẮT KẾ THỪA header khi tạo section riêng cho Trang cuối chương (OOXML mặc định section sau kế thừa header/footer section trước  | `hieuhoc_template.js` | JS | — |
| `hinhIcon(tenIcon, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `hinhIconHang(danhSachTen, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `hinhVe({ imageBuffer, rongCm = 8, tiLeGoc, chuThich })` | 22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4] HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa. `hangHinh`: 1 hàng ≤3  | `hieuhoc_template.js` | JS | — |
| `hinhVeTextBox({ imageBuffer, rongCm = 6, tiLeGoc, chuThich })` | — | `hieuhoc_template.js` | JS | — |
| `kiemMay(bufOrPath, opts = {})` | [v9.7] CỬA KIỂM MÁY CHUNG — kiemMay(bufOrPath, opts) Code hóa checklist máy (HP Điều 61). AI Soạn (qua xuatFile) và AI QC (gọi trực tiếp trên file nhậ | `hieuhoc_template.js` | JS | — |
| `kyHieuGoc(tenGoc)` | 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam | `hieuhoc_template.js` | JS | — |
| `kyHieuMu(ten)` | 22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4] HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa. `hangHinh`: 1 hàng ≤3  | `hieuhoc_template.js` | JS | — |
| `kyHieuToHop(ten, duoi, tren)` | — | `hieuhoc_template.js` | JS | — |
| `kyHieuVecto(ten)` | [33k] Chỉ đạo: vá backlog |a⃗ ± b⃗| (mảng A5 luyện thi _LT). Độ dài của BIỂU THỨC vectơ bất kỳ (nhiều vectơ + toán tử), KHÁC doDaiVecto(1 tên). doDaiB | `hieuhoc_template.js` | JS | — |
| `layoutCauHoi(cauArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `logarit(coSo, bieuThuc, opts = {})` | A10 [33x] — LÔGARIT — toán tử log/ln ĐỨNG (OMML m:func > m:fName, giống lim/min/max → Word render roman). logarit(coSo, bieuThuc) → log_(coSo) bieuThu | `hieuhoc_template.js` | JS | — |
| `loiGiai(noiDung)` | — | `hieuhoc_template.js` | JS | — |
| `luoiHinh(items, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `luyThua(coSo, soMu)` | — | `hieuhoc_template.js` | JS | — |
| `luyThuaUnicode(coSo, soMu)` | — | `hieuhoc_template.js` | JS | — |
| `lyThuyet(text)` | 4. LÝ THUYẾT — 1 dòng nội dung thường | `hieuhoc_template.js` | JS | — |
| `minMax(ten, duoi, than)` | [33b] TOÁN TỬ GTLN–GTNN: min/max với CHỈ SỐ DƯỚI (limLow) — chuẩn SGK $\min\limits_{D} f(x)$. Mirror gioiHan nhưng tên toán tử truyền vào (ten='min'|' | `hieuhoc_template.js` | JS | — |
| `mucTieu({ kienThuc, kyNang, nangLuc })` | 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm) | `hieuhoc_template.js` | JS | — |
| `ngoac(bieuThuc)` | — | `hieuhoc_template.js` | JS | — |
| `nhanDang(yArr)` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `nhatKyCaiTien({ dsPhienBan } = {})` | — | `hieuhoc_template.js` | JS | — |
| `para(children, opts = {})` | A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng) keepNext: gi | `hieuhoc_template.js` | JS | — |
| `paraCoHinhPhai(anhFloating, noiDungInline, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `paraHePhuongTrinh(danhSachPT, opts = {})` | [31q] TUYỂN NGHIỆM — ngoặc vuông "[" (HOẶC) cho nghiệm phương trình LG Mirror hePhuongTrinh nhưng begChr="[" (tuyển: x=... HOẶC x=...). KHÁC hệ "{" (đ | `hieuhoc_template.js` | JS | — |
| `paraInline(input, opts = {})` | Dựng nhanh 1 Paragraph từ nội dung string|mảng trộn — dùng nội bộ | `hieuhoc_template.js` | JS | — |
| `paraTuyenNghiem(danhSachPT, opts = {})` | Bản tiện dụng — trả 1 Paragraph căn giữa chứa khối tuyển nghiệm (chèn thẳng vào cacBuoc loiGiai). | `hieuhoc_template.js` | JS | — |
| `patchDocPrIds(docBuffer)` | [v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer). AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang. | `hieuhoc_template.js` | JS | — |
| `phanSo(tuSo, mauSo)` | — | `hieuhoc_template.js` | JS | — |
| `phanTich(noiDung)` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `phuongPhapGiai(buocArr, opts = {})` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `run(text, opts = {})` | A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng) keepNext: gi | `hieuhoc_template.js` | JS | — |
| `saiLamThuongGap(loiArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `soGachTren(noiDung)` | [33b] TOÁN TỬ GTLN–GTNN: min/max với CHỈ SỐ DƯỚI (limLow) — chuẩn SGK $\min\limits_{D} f(x)$. Mirror gioiHan nhưng tên toán tử truyền vào (ten='min'|' | `hieuhoc_template.js` | JS | — |
| `tabLine(parts, opts = {})` | A2 v9.0: tab stop thật chia đều 18.4cm (TOTAL_W tính theo twip = 10432 ≈ 18.4cm) Thay khoảng trắng giả bằng \t + tabStops chuẩn — căn đều bất kể font/ | `hieuhoc_template.js` | JS | — |
| `taoTaiLieu({ soBai, tenBai, lop, children })` | [v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer). AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang. | `hieuhoc_template.js` | JS | — |
| `taoTaiLieuDeKT({ tenDe, children, headerFooter = true })` | taoTaiLieuDeKT — dựng Document cho ĐỀ KIỂM TRA (thay khối Document tự dựng trong build script mỗi đề). Header/footer đề KT tự gắn (ĐÚNG MẪU headerFoot | `hieuhoc_template.js` | JS | — |
| `tenBaiHoc({ soBai, tenBai, tiet, sgkTr, sbtTr, ma })` | 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm) | `hieuhoc_template.js` | JS | — |
| `theoChan(bieuThuc, duoi, tren)` | — | `hieuhoc_template.js` | JS | — |
| `tichPhan(than, duoi, tren)` | A10 [33x] — LÔGARIT — toán tử log/ln ĐỨNG (OMML m:func > m:fName, giống lim/min/max → Word render roman). logarit(coSo, bieuThuc) → log_(coSo) bieuThu | `hieuhoc_template.js` | JS | — |
| `tieuDeDang({ soDang, tenDang, ma })` | — | `hieuhoc_template.js` | JS | — |
| `tieuDeKhoiTracNghiem()` | [V12.1 · 29y] SƠ ĐỒ KHỐI ④ BÀI TẬP VỀ NHÀ — 2 KHỐI: A. Trắc nghiệm (Phần I/II/III con) + B. Tự luận Thay sơ đồ PHẲNG cũ A/B/C/D (tieuDePhanI/II/III +  | `hieuhoc_template.js` | JS | — |
| `tieuDeKhoiTuLuan(soBai, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDeMuc(stt, ten)` | 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm) | `hieuhoc_template.js` | JS | — |
| `tieuDeMucChinh(stt, ten)` | 4. LÝ THUYẾT — 1 dòng nội dung thường | `hieuhoc_template.js` | JS | — |
| `tieuDePhanI(soCau, tongDiem)` | Tiêu đề khối "A. PHẦN I - CHỌN ĐÁP ÁN (...)" | `hieuhoc_template.js` | JS | — |
| `tieuDePhanII(soCau, soMenhDe, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDePhanIII(soCau, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDePhanIII_DeKT(soCau, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDePhanIII_TN(soCau, tongDiem)` | [v9.7] CỬA KIỂM MÁY CHUNG — kiemMay(bufOrPath, opts) Code hóa checklist máy (HP Điều 61). AI Soạn (qua xuatFile) và AI QC (gọi trực tiếp trên file nhậ | `hieuhoc_template.js` | JS | — |
| `tieuDePhanII_DeKT(soCau, soMenhDe, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDePhanII_TN(soCau, soMenhDe, tongDiem)` | [v9.7] CỬA KIỂM MÁY CHUNG — kiemMay(bufOrPath, opts) Code hóa checklist máy (HP Điều 61). AI Soạn (qua xuatFile) và AI QC (gọi trực tiếp trên file nhậ | `hieuhoc_template.js` | JS | — |
| `tieuDePhanIV_DeKT(soBai, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDePhanI_DeKT(soCau, tongDiem)` | 23. TIÊU ĐỀ CÁC PHẦN ĐỀ KIỂM TRA (I/II/III/IV — khác BTVN dùng A/B/C/D) | `hieuhoc_template.js` | JS | — |
| `tieuDePhanI_TN(soCau, tongDiem)` | — | `hieuhoc_template.js` | JS | — |
| `tieuDeTuLuan(soBai, tongDiem)` | Tiêu đề khối "D. TỰ LUẬN (n bài = Xđ)" | `hieuhoc_template.js` | JS | — |
| `toInline(input, opts = {})` | Dựng nhanh 1 Paragraph từ nội dung string|mảng trộn — dùng nội bộ | `hieuhoc_template.js` | JS | — |
| `traLoiNgan({ soCau, cauHoi, dapAn, thamChieu, anDapAn })` | 16. HEADER ĐỀ KIỂM TRA (tên đề + thời gian + bảng Họ tên/Điểm/NX) | `hieuhoc_template.js` | JS | — |
| `trangCuoiChuong({ dsLopBai, dsPhienBan })` | — | `hieuhoc_template.js` | JS | — |
| `triTuyetDoi(bieuThuc)` | 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam | `hieuhoc_template.js` | JS | — |
| `tuLuanBTVN({ soBai, mucDo, diem, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai, anLoiGiai })` | Tiêu đề khối "D. TỰ LUẬN (n bài = Xđ)" | `hieuhoc_template.js` | JS | — |
| `tuyenNghiem(danhSachPT)` | [31q] TUYỂN NGHIỆM — ngoặc vuông "[" (HOẶC) cho nghiệm phương trình LG Mirror hePhuongTrinh nhưng begChr="[" (tuyển: x=... HOẶC x=...). KHÁC hệ "{" (đ | `hieuhoc_template.js` | JS | — |
| `viDu({ nhan = "Ví dụ", deBai, cacCau, dapAn, loiGiaiND, viDuLoiGiai, thamChieu, coHinh, hinhBenTrai, hinhBenPhai, dai = false })` | — | `hieuhoc_template.js` | JS | — |
| `viDuLyThuyet({ cacCau, deBai, nhan, dapAn, loiGiaiND, viDuLoiGiai, thamChieu, coHinh, hinhBenPhai, hinhBenTrai })` | — | `hieuhoc_template.js` | JS | — |
| `xacSuatDK(A, B)` | 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam | `hieuhoc_template.js` | JS | — |

---
**Thống kê:** 170 hàm Python (vẽ hình) + 87 hàm JS (dựng Word) = 257.
