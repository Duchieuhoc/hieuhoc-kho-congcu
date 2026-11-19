# BẢN TRÍCH HÀM VẼ — HH9_CH10 — tự sinh từ `hinh_hh9_ch10.py` (module one-shot)

> **Cho AI Soạn.** Module HÀM MỘT-PHÁT: mỗi hàm nhận DỮ LIỆU/KÍCH THƯỚC THẬT → trả PNG (biểu đồ, mô hình, hoặc hình khối). Không theo lối builder `h.ve()`.
> Tự sinh bằng introspect `hinh_hh9_ch10.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 19/11/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_hh9_ch10 as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bon_xang(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `bon_xang(R=1.0, L=3.2, nhan=None, out='bon_xang', tra_bytes=False)` | BỒN NẰM NGANG — trụ nằm ngang dài L + 2 NỬA CẦU hai đầu (H10.32). |
| `cat_cau(R=1.7, cao=0.0, nhan_mc='R', qua_tam=True, tam='O', nhan_mp='(P)', out='cat_cau', tra_bytes=False)` | MẶT CẦU cắt bởi mặt phẳng → mặt cắt là hình tròn. cao : độ cao mặt cắt so tâm (0 = qua tâm → đường tròn lớn). qua_tam : True ghi "đường tròn lớn" (bán kính R); False → đường tròn nhỏ. nhan_mc : nhãn bán kính mặt cắt. |
| `cau_trong_lapphuong(a='a', canh=3.0, tam='O', out='cau_lapphuong', tra_bytes=False)` | HÌNH CẦU nội tiếp LẬP PHƯƠNG (H10.4-SBT): cầu tiếp xúc 6 mặt, bán kính a/2, tâm = tâm lập phương. Phối cảnh xiên cavalier. |
| `ghep_ncau_tru_non(R=1.1, h_tru=1.6, h_non=1.8, nhan=None, out='ghep_ncau_tru_non', tra_bytes=False)` | GHÉP 3 TẦNG (H10.37c): NỬA CẦU (vòm trên) + TRỤ (giữa) + NÓN (chúc xuống, dưới). |
| `hcn_quay(R=1.3, h=2.8, ten=("O'", 'A', 'B', 'O'), hien_tru=True, out='hcn_quay', tra_bytes=False)` | HÌNH CHỮ NHẬT quay quanh một CẠNH (trục đứng) sinh HÌNH TRỤ (H10.3). ten=(trên-trục, trên-ngoài, dưới-ngoài, dưới-trục). |
| `hinh_cau(R=1.6, nhan_R=None, tam='O', hien_tam=True, hien_xichdao=True, duong_kinh=None, diem=None, out='cau', tra_bytes=False)` | HÌNH CẦU / MẶT CẦU phối cảnh (viền tròn + xích đạo elip). R : bán kính (độ dài VẼ). >0. nhan_R : nhãn bán kính — vẽ O→mép phải, ghi nhãn. None=ẩn. tam : tên tâm (mặc định O). hien_tam: ghi tâm + chấm. hien_xichdao : vẽ đường tròn lớn nằm ngang (xích đạo): nửa trước liền, sau đứt. duong_kinh=('A','B') : vẽ đường kính ngang AB (mép trái–phải) + ghi 2 tên. diem=('M', goc_do) : điểm M trên mặt cầu ở góc 'goc_do' (độ) + bán kính OM. |
| `hinh_non(R=1.6, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None, dinh='S', tam='O', trai='A', phai='B', hien_dinh_ten=True, hien_tam=True, hien_trai_phai=False, o_vuong=True, out='non', tra_bytes=False)` | HÌNH NÓN phối cảnh đứng (đỉnh trên, đáy elip, 2 đường sinh biên). R, h : bán kính đáy, chiều cao. >0. nhan_R : nhãn bán kính (O→mép phải đáy). None=ẩn. nhan_h : nhãn chiều cao (trục SO, nét đứt). None=ẩn. nhan_l : nhãn đường sinh (cạnh biên phải S→B). None=ẩn. dinh,tam,trai,phai : tên đỉnh S, tâm đáy O, mép trái A, mép phải B. o_vuong : đánh dấu góc vuông tại O (SO ⊥ đáy). |
| `hinh_tru(R=1.4, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None, tam_tren="O'", tam_duoi='O', dinh_tren=None, dinh_duoi=None, hien_truc=True, out='tru', tra_bytes=False)` | HÌNH TRỤ phối cảnh đứng (2 đáy elip + 2 đường sinh biên). R, h : bán kính đáy, chiều cao (độ dài VẼ, đơn vị ô). >0. nhan_R : nhãn bán kính đáy (vẽ đoạn O→mép phải đáy dưới). None=ẩn. nhan_h : nhãn chiều cao (trục O'O). None=ẩn nhãn (trục vẫn vẽ nếu hien_truc). nhan_l : nhãn 1 đường sinh (cạnh biên phải). None=ẩn. tam_tren/tam_duoi : tên 2 tâm đáy (mặc định O', O). '' = không ghi. dinh_tren/dinh_duoi : tên điểm mép phải đáy trên/dưới (vd 'A'/'B' khi cần l=AB). hien_truc : vẽ trục O'O (nét đứt) hay không. |
| `khai_trien_non(R=1.0, l=2.6, nhan_l=None, nhan_R=None, dinh='S', out='kt_non', tra_bytes=False)` | KHAI TRIỂN hình nón = hình quạt tròn (bán kính l, cung = 2πR) + hình tròn đáy (bán kính R). |
| `khai_trien_tru(R=0.9, h=2.4, nhan_cv=None, nhan_h=None, nhan_R=None, out='kt_tru', tra_bytes=False)` | KHAI TRIỂN hình trụ = hình chữ nhật (rộng = chu vi 2πR, cao = h) + 2 hình tròn đáy. |
| `mu_non_vanh(R_non=1.1, l=2.4, R_vanh=1.9, nhan=None, out='mu_non_vanh', tra_bytes=False)` | MŨ (chú hề) = hình NÓN + VÀNH (hình vành khăn phẳng) — H10.31. R_non bán kính đáy nón, l đường sinh, R_vanh bán kính ngoài vành. |
| `non_trong_lapphuong(a='a', canh=3.2, dinh='O', out='non_lapphuong', tra_bytes=False)` | HÌNH NÓN nội tiếp trong LẬP PHƯƠNG (H10.38): đỉnh = tâm O mặt trên ABCD, đáy = hình tròn nội tiếp mặt đáy A'B'C'D' (tiếp xúc 4 cạnh). Phối cảnh xiên cavalier. a : nhãn cạnh (hiển thị 3 cạnh), vd 'a'. canh : độ dài VẼ. dinh : tên đỉnh nón (tâm mặt trên), mặc định 'O'. |
| `nua_cau(R=1.6, nhan_R=None, up=True, mat_phang=False, tam='O', out='nua_cau', tra_bytes=False)` | NỬA HÌNH CẦU đứng độc lập (vòm / chao đèn / bát) — H chao đèn, mái vòm. up=True : vòm hướng LÊN (mặt phẳng tròn ở dưới, cung cong phía trên). up=False : vòm hướng XUỐNG (chao đèn treo: mặt phẳng tròn ở trên, cong phía dưới). mat_phang: tô nhạt mặt cắt tròn (đĩa phẳng). nhan_R: nhãn bán kính trên đĩa. |
| `nua_cau_non(R=1.2, h_non=2.4, nhan=None, up=True, out='nuacau_non', tra_bytes=False)` | GHÉP: NÓN + NỬA CẦU chung đáy — ốc quế kem (H10.39): nón chúc XUỐNG, vòm cầu trên. up=True: nón đỉnh dưới, nửa cầu vòm trên (kem). up=False: nón trên. |
| `nua_cau_tru(R=1.3, h=2.2, nhan=None, out='nuacau_tru', tra_bytes=False)` | GHÉP: hình TRỤ (dưới) + NỬA HÌNH CẦU (vòm trên) — H10.37a. |
| `tamgiac_quay(R=1.5, h=2.8, ten=('S', 'O', 'A'), hien_non=True, o_vuong=True, out='tg_quay', tra_bytes=False)` | TAM GIÁC VUÔNG quay quanh CẠNH GÓC VUÔNG (trục đứng) sinh HÌNH NÓN (H10.9a). ten=(đỉnh trên S, chân vuông O, đỉnh ngoài A). |
| `them_caption(anh, chu_thich, out='fig_caption', tra_bytes=False, mau='#555')` | Nướng dòng CHÚ THÍCH "Hình N…" căn giữa DƯỚI ảnh (nền trong suốt) — cho hình NEO PHẢI (text-wrap) vốn không nhận chuThich qua template. Thay workaround Pillow per-bài: AI Soạn gọi `K.them_caption(K.hinh_tru(...), "Hình 5. …")`. anh : đường dẫn PNG hoặc bytes (kết quả 1 hàm hình). chu_thich: chuỗi caption. Trả về đường dẫn PNG (hoặc bytes nếu tra_bytes) — ảnh gốc + dải caption dưới. |
| `tru_chua_cau(R=1.2, n=3, nhan=None, out='tru_chua_cau', tra_bytes=False)` | HỘP/TRỤ chứa n quả CẦU xếp dọc khít (H10.29 bóng tennis · H10.7-SBT) — trụ đứng, cao = n·2R, mỗi cầu bán kính R. nhan={'R','d'} (d = đường kính cầu). |
| `tru_khoan_non(R=1.3, h=2.4, nhan=None, out='tru_khoan_non', tra_bytes=False)` | HÌNH TRỤ bị KHOAN mất phần hình NÓN (đáy nón = đáy trên trụ, đỉnh ở tâm đáy dưới) — H10.28. |
| `tru_khoet_2cau(R=1.2, h=3.0, nhan=None, out='tru_khoet_2cau', tra_bytes=False)` | TRỤ khoét 2 NỬA CẦU hai đầu (H10.8-SBT): đường tròn đáy trụ = đường tròn lớn mỗi nửa cầu (bán kính nửa cầu = R). Vòm khoét nét đứt (lõm vào trong). |
| `tru_non(R=1.3, h_tru=2.0, h_non=1.8, nhan=None, out='tru_non', tra_bytes=False)` | GHÉP: hình TRỤ (dưới) + hình NÓN (trên, chung đáy) — H10.16 dụng cụ. nhan=dict {'R','h_tru','h_non'} nhãn kích thước (tùy chọn). |
| `tru_trong_hop(R=1.0, L=3.4, nhan=None, out='tru_trong_hop', tra_bytes=False)` | HÌNH TRỤ (bóng đèn) đặt khít trong HỘP CHỮ NHẬT (H10.4/10.15) — trụ nằm ngang, hộp đáy vuông cạnh 2R, dài L. Phối cảnh xiên cavalier. |
| `vong_bi(R=1.6, r=0.9, h=1.3, nhan=None, out='vong_bi', tra_bytes=False)` | VÒNG BI / ỐNG TRỤ RỖNG — trụ ngoài R khoét trụ trong r, cao h (H10.30). |

---

**Thống kê:** 23 hàm một-phát (phơi cho AI Soạn).
