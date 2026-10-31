# BẢN TRÍCH HÀM VẼ — DS11_CH05 — tự sinh từ `hinh_ds11_giaitich.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `hinh_ds11_giaitich.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 30/10/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_ds11_giaitich as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `cau_parabol_doc(W=4.0, H=2.0, xP=-2.2, nhan_nua='200 m', nhan_doc='Độ dốc tại $P$', nhan_cao='?', ten_A='A', ten_B='B', ten_P='P', out='cau_parabol', tra_bytes=False, scale=1.0)` | SƠ ĐỒ CẦU VƯỢT PARABOL (H9.5). Cung úp y=H(1-(x/W)^2) nối A(-W,0),B(W,0), đỉnh (0,H). P trên cung (xP<0) + tiếp tuyến tại P + cung góc 'độ dốc tại P'; mũi tên đứt '?' từ đỉnh xuống nền; nhịp 2 nửa 'nhan_nua'. Máy TỰ tính hệ số góc tiếp tuyến (Đ5.9). |
| `do_thi_bac_thang(doan, diem_dac=None, diem_ho=None, nhan_ham=None, xmax=1.3, ymax=1.4, xticks=(0.5, 1.0), yticks=(0.5, 1.0), xtick_lab=None, ytick_lab=None, out='bacthang', tra_bytes=False, scale=3.4)` | ĐỒ THỊ HÀM BẬC THANG / PIECEWISE-LINEAR (H5.7 — minh họa liên tục/gián đoạn). doan: list đoạn thẳng [[(x1,y1),(x2,y2)], ...] — vẽ đường LIỀN từng đoạn (nối trong 1 đoạn). diem_dac: [(x,y),...] chấm ĐẶC (điểm thuộc đồ thị). diem_ho: [(x,y),...] vòng RỖNG (điểm KHÔNG thuộc — điểm hở). xticks/yticks: mốc chia (số); xtick_lab/ytick_lab: nhãn tường minh (None → tự format phân số đẹp). nhan_ham: nhãn hàm (vd r'y=f(x)') góc trên-phải. Máy chỉ VẼ nghĩa đã khai — không tự sinh điểm. |
| `do_thi_cat_tiep(x0=2.2, xQ=5.0, nhan_P='P', nhan_Q='Q', nhan_tt='t', nhan_ham='y=f(x)', out='cat_tiep', tra_bytes=False, scale=1.0)` | CÁT TUYẾN & TIẾP TUYẾN (H9.3 — khi Q→P, cát tuyến PQ dần về tiếp tuyến tại P). Cung lồi cố định f(x)=-0.18(x-1)(x-7) (máy TỰ tính tọa độ + hệ số góc, Đ5.9). P(x0;f(x0)), Q(xQ;f(xQ)), 1<x0<xQ<7. Cát tuyến (đỏ) qua P,Q + tiếp tuyến (teal) tại P hệ số góc f'(x0). Gióng đứt x0,x→Ox và f(x0)→Oy. Hình LÝ THUYẾT. |
| `do_thi_huu_ti(dang='doi_truc', a=1.0, b=2.0, c=1.0, k=1.0, xmin=None, xmax=None, ymin=None, ymax=None, nhan=None, hien_tc=True, out='dothi_ht', tra_bytes=False, scale=1.0)` | ĐỒ THỊ HÀM HỮU TỈ (pgfplots — máy dựng đường cong thẳng từ công thức; PHANH nội sinh). dang='doi_truc' : y = a + b/(x-c). Hyperbol dời trục. TCĐ x=c (đứng), TCN y=a (ngang). 2 nhánh. (H5.4: a=1,b=2,c=1) dang='nghich_dao_binh' : y = k/(x-c)^2. Hàm chữ U (k>0: 2 nhánh trên Ox). TCĐ x=c, TCN y=0. (H5.6: k=1,c=0) hien_tc: vẽ tiệm cận đứt nét (bỏ nét trùng trục khi c=0 / a=0). nhan: nhãn đường cong (None→tự sinh). |
| `parabol_2tiep(k=0.22, q=3.6, net='dut', nhan=('L_1', 'L_2'), ten_P='P', ten_Q='Q', out='parabol_2tiep', tra_bytes=False, scale=1.0)` | PARABOL ÚP + 2 TIẾP TUYẾN NÉT ĐỨT (H9.6b — đường ray tàu lượn, dùng ở BT 9.5). y=-k x(x-q): P=O=(0;0), Q=(q;0) trên Ox. L1 tiếp tuyến tại P (dốc lên), L2 tại Q (dốc xuống) — nét đứt. Máy TỰ tính hệ số góc tiếp tuyến (Đ5.9). Hình đề KHÔNG lộ kết quả: không ghi giá trị số (Đ41.4). |
| `tam_giac_toa_do(a=2.0, ten_O='O', ten_A='A', ten_B='B', ten_H='H', nhan_h='h', hien_duong_cao=True, out='tamgiac_td', tra_bytes=False, scale=1.0)` | TAM GIÁC VUÔNG OAB TRÊN HỆ Oxy (H5.5). O=(0;0), A=(a;0) trên Ox, B=(0;1) trên Oy; vuông tại O. Đường cao OH hạ từ O vuông góc xuống cạnh huyền AB, chân H trên AB, OH=h. Máy TỰ tính H = foot(O, AB) từ tọa độ (Đ5.9 VERIFY); PHANH: kiểm OH⊥AB + H∈AB. |
| `tia_so_vi_tri(ten_truc='s', xP=3.0, xQ=7.0, L=9.0, nhan_P='Vị trí tại $t_0$', nhan_Q='Vị trí tại $t$', nhan_doan='$s(t)-s(t_0)$', out='tia_vitri', tra_bytes=False, scale=1.0)` | TIA SỐ VỊ TRÍ VẬT (H9.2 — minh họa quãng đường đi được từ t0 đến t). Trục ngang 'ten_truc', gốc 0, KHÔNG vạch số. 2 mốc vị trí (0<xP<xQ<L, danh nghĩa không tỉ lệ) có mũi tên chỉ XUỐNG + nhãn trên; đoạn [P;Q] đo bằng ngoặc dưới (nhan_doan). Schematic — không dữ liệu số để PHANH; chỉ kiểm thứ tự mốc. |

---

**Thống kê:** 7 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
