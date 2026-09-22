# 00_MUC_LUC_HAM — MỤC LỤC HÀM TỔNG (tra "đã-có-chưa" TRƯỚC khi viết)

> **Tự sinh** bởi `sinh_mucluc.py` — TÁI DÙNG `sinh_bantrich.py` (Python) + `API_REFERENCE.md` (output `sinh_apiref.js`, JS). KHÔNG sửa tay.
> Regen: `python3 sinh_mucluc.py > 00_MUC_LUC_HAM.md`. Sinh ngày 22/09/2026.
> **LUẬT VÀNG:** trước khi viết hàm mới → tra file này (Ctrl+F theo NGHĨA). Có hàm khớp → GỌI LẠI. Gần giống → MỞ RỘNG. Viết mới là bậc CUỐI.

*Ẩn: hàm hạ tầng (`_…`) + cửa render (`ve`) theo Đ5.9. Base compose per-bài không vào kho → không liệt kê.*

## Đa giác  · 18 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `chu_so_7doan(so, x0=0.0, y0=0.0, rong=1.0, cao=2.0, mau=None, rong_net='dam')` | CHỮ SỐ kiểu 7-ĐOẠN (0..9) — cho bài TÂM đối xứng (lật nửa vòng 6↔9, giữ 0/1/2/5/8) | `hinh_dagiac.py` | method | — |
| `da_giac_deu(*ten, canh=2.0, xoay=0, to=None)` | Đa giác đều n cạnh (n = số tên truyền vào ≥ 3), đỉnh theo chiều kim đồng hồ, một cạnh nằm ngang phía trên khi xoay=0 | `hinh_dagiac.py` | method | — |
| `da_giac_vuong(ten, buoc, nhan='below right', cham=True, goc_o=(0.0, 0.0))` | Đa giác mọi cạnh song song trục (góc vuông) — hình chữ L, bậc thang, mặt bằng | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_qua_trung_truc(new, P, A, B, nhan='above', mau=None)` | Đặt 'new' = ẢNH của P qua ĐƯỜNG TRUNG TRỰC của đoạn AB (phản chiếu biến A↔B) | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_tam(new, P, O, nhan='below', mau=None)` | Đặt điểm 'new' = ẢNH của P qua TÂM ĐỐI XỨNG O (phép đối xứng tâm) — new = 2·O − P, tức O là TRUNG ĐIỂM của đoạn P–new | `hinh_dagiac.py` | method | — |
| `diem_doi_xung_truc(new, P, A, B, nhan='above right', mau=None)` | Đặt điểm 'new' = ẢNH của điểm P qua TRỤC (đường thẳng) AB — phản chiếu | `hinh_dagiac.py` | method | — |
| `hinh_thang(A, B, Cc, D, day_tren=3.0, day_duoi=5.0, cao=2.5, lech=0.8)` | Hình THANG thường: A,B = đáy trên (day_tren); D,C = đáy dưới (day_duoi); AB ∥ DC (PHANH song_song) | `hinh_dagiac.py` | generator | — |
| `hinh_thang_can(A, B, Cc, D, day_nho=3.0, day_lon=5.0, cao=2.5, cheo=False)` | Hình thang cân đối xứng qua trục dọc: A,B = đáy nhỏ (trên); D,C = đáy lớn (dưới) | `hinh_dagiac.py` | generator | — |
| `hinh_thoi(A, B, Cc, D, a=4, b=3, cheo=True, tam='O')` | Hình thoi "kim cương" dựng theo 2 nửa chéo NGUYÊN ô → tâm + 4 đỉnh rơi NÚT lưới | `hinh_dagiac.py` | generator | — |
| `hinh_vuong(M, N, P_, Q, canh=4, goc_o=(0.0, 0.0), cham=True)` | Hình VUÔNG: M dưới-trái, N trên-trái, P trên-phải, Q dưới-phải | `hinh_dagiac.py` | generator | — |
| `luc_giac_deu(A, B, Cc, D, E, F, canh=2.0, xoay=0, cheo=None, tam=None)` | Lục giác đều 6 đỉnh, thứ tự A→B→C→D→E→F theo chiều kim đồng hồ | `hinh_dagiac.py` | method | — |
| `ngoi_sao(tam, so_canh=5, ban_kinh=2.0, xoay=90, ti_le_trong=None, to=None, nhan=None, cham_tam=False)` | NGÔI SAO so_canh cánh (mặc định 5 — cờ VN/Quốc kỳ; dùng cả 4/6/8 cánh cho Chương V) | `hinh_dagiac.py` | method | — |
| `tam_giac(A, B, Cc, noi=True, goc_o=(0.0, 0.0))` | Tam giác 3 đỉnh (không thẳng hàng) | `hinh_dagiac.py` | method | — |
| `tam_giac_can(A, B, Cc, canh_ben=3.0, day=2.4, danh_dau=True, goc_o=(0.0, 0.0))` | Tam giác CÂN tại đỉnh A (A đỉnh trên; B–C đáy nằm ngang, B trái–C phải) | `hinh_dagiac.py` | method | — |
| `tam_giac_canh(A, B, Cc, AB, BC, CA, goc_o=(0.0, 0.0))` | Tam giác ABC dựng từ 3 CẠNH cho sẵn (SSS): |AB|, |BC|, |CA| (đơn vị bất kỳ, giữ ĐÚNG TỈ LỆ) | `hinh_dagiac.py` | method | — |
| `tam_giac_deu(A, B, Cc, canh=3.0, xoay=0, goc_o=(0.0, 0.0))` | Tam giác ĐỀU 3 đỉnh: B dưới-trái, C dưới-phải, A đỉnh trên | `hinh_dagiac.py` | method | — |
| `tam_giac_goc(A, B, Cc, goc_B, goc_C, day=4.0, goc_o=(0.0, 0.0), an_nhan=False)` | Tam giác ABC với GÓC cho sẵn: góc tại B = goc_B, góc tại C = goc_C (góc A tự = 180 − goc_B − goc_C) | `hinh_dagiac.py` | method | — |
| `tu_giac(A, B, Cc, D, loai=None)` | Tứ giác 4 đỉnh lồi, chiều kim đồng hồ | `hinh_dagiac.py` | method | — |

## Số & Đại số (tia số/trục số/toạ độ/diện tích đại số)  · 2 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `dung_can_hai(canh=2, nhan_diem='A', nhan_can=None)` | DỰNG √2 (hoặc √(canh²/2)) TRÊN TRỤC SỐ bằng compa — SGK Toán 7 Hình 2.3 | `hinh_daiso.py` | method | L6→9→THPT |
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

## Khối / không gian  · 10 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
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
| `hinhMatPhangToaDo(xRange=(-5, 5), yRange=(-5, 5), buoc=1, luoi=True, duongThang=None, diem=None, chuThich=None, scale=0.72, out='mp_toado', tra_bytes=False)` | MẶT PHẲNG TOẠ ĐỘ Oxy — trục có mũi tên + nhãn O,x,y; lưới mờ tuỳ chọn; đồ thị ĐƯỜNG THẲNG (theo phương trình / 2 điểm) + ĐIỂM có nhãn + đường gióng né | `hinh_toado.py` | generator | L6→9→THPT |
| `kim_tu_thap(hang, o_canh=0.95)` | KIM TỰ THÁP SỐ (2D) — tháp ô vuông, ô trên gối lệch nửa ô giữa 2 ô dưới | `hinh_toado.py` | method | L6→9→THPT |
| `nhiet_ke_cot(cot, thang=(-20, 50), buoc=10, don_vi='°C', hien_muc_so=False)` | NHIET KE COT — nhieu thang do DUNG canh nhau, doc muc thuy ngan | `hinh_toado.py` | method | L6→9→THPT |
| `tia_diem(*args, **kwargs)` | [Đại số] sơ đồ điểm trên đường thẳng — NỀN SẠCH (base hinh_coban mặc định có lưới). | `hinh_toado.py` | method | L6→9→THPT |
| `tia_so(gia_tri_max=None, buoc=1, diem=None, hien_nhan_diem=True, moc_nhan=None, ti_le=True, mui_ten=True, goc_ten='O', nhay=None)` | TIA SỐ tự nhiên — gốc bên trái, mũi tên sang phải; vạch chia + nhãn số + điểm đánh dấu | `hinh_toado.py` | method | L6→9→THPT |
| `truc_do_chinh_xac(trai, phai, a, do_chinh_xac=None, nhan_a='a')` | TRỤC SỐ 'ĐỘ CHÍNH XÁC LÀM TRÒN' — đoạn cục bộ [trai; phai] (KHÔNG cần gốc 0) | `hinh_toado.py` | method | L6→9→THPT |
| `truc_doan_doc_diem(trai, phai, chia=10, diem=None, hien_nhan_diem=False, moc_nhan=None)` | TRỤC SỐ ĐOẠN PHÓNG TO để ĐỌC ĐIỂM — biên THẬP PHÂN, chia nhỏ, kéo rộng | `hinh_toado.py` | method | L6→9→THPT |
| `truc_so_huu_ti(tu=-1, den=4, chia=1, diem=None, hien_nhan_diem=True, moc_nhan=None, mui_ten_am=False, goc_ten='0', khoang_to=None, vach_dut=None, mui_ten_dc=None)` | TRỤC SỐ biểu diễn số hữu tỉ — gốc O ở giá trị 0, có phần âm & dương | `hinh_toado.py` | method | L6→9→THPT |

## Đường tròn (dựng)  · 11 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `cung(tam, goc_dau, goc_cuoi, mau='red', net='lien', ban_kinh=None)` | CUNG của đường tròn tâm 'tam', quét từ 'goc_dau' đến 'goc_cuoi' (độ, góc ở tâm) | `hinh_tron_ve.py` | method | — |
| `cung_qua(tam, qua, ban_kinh=None, mo=28, mau='black', net='dut')` | Vẽ CUNG NGẮN của đường tròn tâm 'tam' ĐI QUA điểm 'qua' — đánh dấu chỗ giao compa, KHÔNG vẽ trọn đường tròn | `hinh_tron_ve.py` | method | — |
| `diem_ban_kinh(ten, tam, goc, ban_kinh, nhan='above right', mau=None, hien=True)` | Điểm 'ten' cách tâm 'tam' đúng 'ban_kinh' (đơn vị vẽ) theo hướng 'goc' (độ, ngược chiều kim từ ngang) — KHÔNG tọa độ | `hinh_tron_ve.py` | method | — |
| `diem_tren_tron(ten, tam, goc_o_tam, nhan='above right', mau=None)` | Điểm 'ten' NẰM TRÊN đường tròn tâm 'tam', định vị bằng GÓC Ở TÂM 'goc_o_tam' (độ, đo ngược chiều kim đồng hồ từ hướng ngang) — KHÔNG tọa độ | `hinh_tron_ve.py` | method | — |
| `duong_tron(tam, ban_kinh=2.0, mau=None, net='lien', hien_tam=True)` | ĐƯỜNG TRÒN tâm 'tam', bán kính 'ban_kinh' (đơn vị vẽ) | `hinh_tron_ve.py` | method | — |
| `duong_tron_qua(tam, qua, mau=None, net='lien', hien_tam=True)` | ĐƯỜNG TRÒN tâm 'tam' đi QUA điểm 'qua' (cả hai ĐÃ đặt) | `hinh_tron_ve.py` | method | — |
| `goc_o_tam(tam, A, B, do=None, danh_dau=True)` | Góc ở tâm chắn bởi 2 bán kính 'tam'A, 'tam'B (A,B đã đặt trên đường tròn) | `hinh_tron_ve.py` | method | — |
| `kim(R, vi_tri, loai='gio', tam='O')` | Vẽ MỘT kim đồng hồ từ tâm 'tam' ra hướng 'vi_tri' (thang 12 giờ, cho phép LẺ: vd 3.5 = giữa số 3 và 4) | `hinh_tron_ve.py` | method | — |
| `mat_dong_ho(gio=None, phut=0, giay=None, R=2.4, tam='O')` | ĐỒNG HỒ chuẩn HH6 — MỘT hàm ra đồng hồ hoàn chỉnh: vành tròn tâm 'tam' + 12 số (đặt bằng diem_tren_tron, nhãn toả ra ngoài) + tuỳ chọn các kim | `hinh_tron_ve.py` | method | — |
| `so_quanh_tam(tam, ban_kinh, danh_sach, goc_dau=90, chieu=-1)` | Rải các nhãn 'danh_sach' ĐỀU quanh tâm 'tam' trên vòng bán kính 'ban_kinh', bắt đầu ở hướng 'goc_dau'° (mặc định 90 = trên đỉnh), bước 'chieu'*360/n ( | `hinh_tron_ve.py` | method | — |
| `vanhKhan(R='R', r='r', toVanh=True, chuThich=None, out='vanh_khan', tra_bytes=False)` | VÀNH KHĂN — hai đường tròn đồng tâm tâm O; bán kính ngoài R, trong r (r<R), mỗi bán kính có nhãn ĐẶT GIỮA đoạn; vành giữa tô nhạt (toVanh). | `hinh_tron_ve.py` | method | — |

## Dựng Word (template JS v10.26)  · 74 hàm

| Hàm | Nghĩa | File | Kiểu | Tầng |
|---|---|---|---|---|
| `approxLen(item)` | Ước lượng độ dài hiển thị — dùng để quyết định xếp cột/xuống hàng (công thức Math không có .length nên tính tượng trưng 3 ký tự) | `hieuhoc_template.js` | JS | — |
| `baiTapTaiLop({ soBai, mucDo, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai, anLoiGiai })` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `bangDapAnPhanI(dapAnArr)` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `bangDungSai(menhDeArr, opts = {})` | 14. BẢNG ĐÚNG/SAI — tỉ lệ CỐ ĐỊNH 80%-10%-10%, nền trắng chữ đen | `hieuhoc_template.js` | JS | — |
| `bangNguonGoc({ soChuong, dsNguon })` | — | `hieuhoc_template.js` | JS | — |
| `bangSoLieu(duLieu, opts = {})` | [28r] 14b. BẢNG SỐ LIỆU TỔNG QUÁT — dữ liệu thực tiễn nhiều cột (dân số, tuổi thọ, hồ, hành tinh, khí hiếm, pizza…) — DS7 dày bảng. GỐC: kho chỉ có bả | `hieuhoc_template.js` | JS | — |
| `canBac(soHang, bacCan = 2)` | — | `hieuhoc_template.js` | JS | — |
| `cauTracNghiem({ soCau, cauHoi, dapAn, thamChieu })` | 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hà | `hieuhoc_template.js` | JS | — |
| `chiSoDuoi(coSo, chiSo)` | 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam | `hieuhoc_template.js` | JS | — |
| `danDungSai(soCau, moTa)` | [28m] DÒNG DẪN Đúng/Sai — nhãn "Câu N." TỰ ĐẬM (khớp nhãn câu template tự sinh ở cauTracNghiem/traLoiNgan/tự luận). GỐC: dòng dẫn Đ/S trước đây dựng T | `hieuhoc_template.js` | JS | — |
| `dangToanDayDu({ saiLamArr, soDang, ghiNhoArr, viDuLoiGiai, loiGiaiND, tenDang, ma, viDuDeBai, viDuCacCau, viDuThamChieu, viDuCoHinh, viDuHinhBenPhai, viDuHinhBenTrai, phanTich, soBai, mucDo, deBai, cacCau, thamChieu })` | Gộp toàn bộ 1 Dạng toán thành 1 lệnh gọi duy nhất — khuyến khích AI Soạn dùng hàm này | `hieuhoc_template.js` | JS | — |
| `footerTPC()` | Footer riêng cho tờ phân chương (khác footer file bài học — không số trang) | `hieuhoc_template.js` | JS | — |
| `ghiChuGiangDay({ dsLopBai } = {})` | — | `hieuhoc_template.js` | JS | — |
| `ghiNhoNhanh(dongArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `hangHinh(items, { caoCm = 3.2, _tuLuoi = false } = {})` | 22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4] HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa. `hangHinh`: 1 hàng ≤3  | `hieuhoc_template.js` | JS | — |
| `hePhuongTrinh(danhSachPT)` | 23. TIÊU ĐỀ CÁC PHẦN ĐỀ KIỂM TRA (I/II/III/IV — khác BTVN dùng A/B/C/D) | `hieuhoc_template.js` | JS | — |
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
| `layoutCauHoi(cauArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `loiGiai(noiDung)` | — | `hieuhoc_template.js` | JS | — |
| `luoiHinh(items, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `luyThua(coSo, soMu)` | — | `hieuhoc_template.js` | JS | — |
| `luyThuaUnicode(coSo, soMu)` | — | `hieuhoc_template.js` | JS | — |
| `lyThuyet(text)` | 4. LÝ THUYẾT — 1 dòng nội dung thường | `hieuhoc_template.js` | JS | — |
| `mucTieu({ kienThuc, kyNang, nangLuc })` | 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm) | `hieuhoc_template.js` | JS | — |
| `ngoac(bieuThuc)` | — | `hieuhoc_template.js` | JS | — |
| `nhanDang(yArr)` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `nhatKyCaiTien({ dsPhienBan } = {})` | — | `hieuhoc_template.js` | JS | — |
| `para(children, opts = {})` | A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng) keepNext: gi | `hieuhoc_template.js` | JS | — |
| `paraCoHinhPhai(anhFloating, noiDungInline, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `paraHePhuongTrinh(danhSachPT, opts = {})` | 23. TIÊU ĐỀ CÁC PHẦN ĐỀ KIỂM TRA (I/II/III/IV — khác BTVN dùng A/B/C/D) | `hieuhoc_template.js` | JS | — |
| `paraInline(input, opts = {})` | Dựng nhanh 1 Paragraph từ nội dung string|mảng trộn — dùng nội bộ | `hieuhoc_template.js` | JS | — |
| `patchDocPrIds(docBuffer)` | [v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer). AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang. | `hieuhoc_template.js` | JS | — |
| `phanSo(tuSo, mauSo)` | — | `hieuhoc_template.js` | JS | — |
| `phanTich(noiDung)` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `phuongPhapGiai(buocArr, opts = {})` | [A.1-mới] Phân tích và hướng dẫn giải — mục A.1 giữa "Bài tập mẫu" và "Lời giải"; gánh nhận dạng + định hướng cách giải (THAY "Phương pháp chung" cũ). | `hieuhoc_template.js` | JS | — |
| `run(text, opts = {})` | A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng) keepNext: gi | `hieuhoc_template.js` | JS | — |
| `saiLamThuongGap(loiArr, opts = {})` | — | `hieuhoc_template.js` | JS | — |
| `soGachTren(noiDung)` | — | `hieuhoc_template.js` | JS | — |
| `tabLine(parts, opts = {})` | A2 v9.0: tab stop thật chia đều 18.4cm (TOTAL_W tính theo twip = 10432 ≈ 18.4cm) Thay khoảng trắng giả bằng \t + tabStops chuẩn — căn đều bất kể font/ | `hieuhoc_template.js` | JS | — |
| `taoTaiLieu({ soBai, tenBai, lop, children })` | [v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer). AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang. | `hieuhoc_template.js` | JS | — |
| `taoTaiLieuDeKT({ tenDe, children, headerFooter = true })` | taoTaiLieuDeKT — dựng Document cho ĐỀ KIỂM TRA (thay khối Document tự dựng trong build script mỗi đề). Header/footer đề KT tự gắn (ĐÚNG MẪU headerFoot | `hieuhoc_template.js` | JS | — |
| `tenBaiHoc({ soBai, tenBai, tiet, sgkTr, sbtTr, ma })` | 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm) | `hieuhoc_template.js` | JS | — |
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
| `traLoiNgan({ soCau, cauHoi, dapAn, thamChieu })` | 16. HEADER ĐỀ KIỂM TRA (tên đề + thời gian + bảng Họ tên/Điểm/NX) | `hieuhoc_template.js` | JS | — |
| `trangCuoiChuong({ dsLopBai, dsPhienBan })` | — | `hieuhoc_template.js` | JS | — |
| `triTuyetDoi(bieuThuc)` | 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam | `hieuhoc_template.js` | JS | — |
| `tuLuanBTVN({ soBai, mucDo, diem, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai, anLoiGiai })` | Tiêu đề khối "D. TỰ LUẬN (n bài = Xđ)" | `hieuhoc_template.js` | JS | — |
| `viDu({ nhan = "Ví dụ", deBai, cacCau, dapAn, loiGiaiND, viDuLoiGiai, thamChieu, coHinh, hinhBenTrai, hinhBenPhai })` | — | `hieuhoc_template.js` | JS | — |
| `viDuLyThuyet({ cacCau, deBai, nhan, dapAn, thamChieu, coHinh, hinhBenPhai, hinhBenTrai })` | — | `hieuhoc_template.js` | JS | — |

---
**Thống kê:** 61 hàm Python (vẽ hình) + 74 hàm JS (dựng Word) = 135.
