# BẢN TRÍCH HÀM — HÌNH LƯỢNG GIÁC THPT (hinh_ds11_luonggiac.py) · kho [31s]
> import: `import hinh_ds11_luonggiac as LG` (tự gắn vào HinhTron). Render qua render script (Python) → PNG, build.js nhúng bằng `H.hinhVe`.

## hinh_khuc_xa(goc_toi=50.0, goc_kx_ve=37.0, nhan_i='i', nhan_r='r', nhan_mt1='Không khí', nhan_mt2=r'$n_2 = 1{,}33$', out='khucxa', scale=1.0)   ← [31s] MỚI
Hiện tượng KHÚC XẠ ÁNH SÁNG qua mặt phân cách 2 môi trường (bài toán thực tiễn SGK 1.36): mặt phân cách ngang, pháp tuyến NN' (nét đứt dọc), tia tới SI (đỏ) hợp pháp tuyến góc i, tia phản xạ IS' (nét đứt), tia khúc xạ IR (xanh) hợp pháp tuyến góc r; môi trường (2) tô nền xanh nhạt.
- `goc_toi`/`goc_kx_ve`: góc tới i và góc khúc xạ r (độ) — CHỈ để VẼ minh họa, không phải đáp số. `nhan_i`/`nhan_r`: nhãn 2 góc (math-mode).
- `nhan_mt1`/`nhan_mt2`: nhãn 2 môi trường — nhập chuỗi **ASCII-safe** hoặc math-mode `$...$` (pdflatex không dựng được ư/ơ; đã đặt mặc định an toàn). KHÔNG lộ đáp số.

## hinh_chu_nhat_noi_tiep(goc_theta=35.0, nhan_theta=r'\theta', duong_kinh='30 cm', R=2.5, out='cnnt', scale=1.0)   ← [31s] MỚI
Hình CHỮ NHẬT NỘI TIẾP đường tròn (bài toán tối ưu SBT 1.64 — xà gỗ): đường tròn tâm O, chữ nhật ABCD nội tiếp, đường chéo AC = ĐƯỜNG KÍNH (đỏ, qua O), góc θ tại A giữa cạnh AB và đường chéo AC. Máy TỰ tính 4 đỉnh từ θ và R (Đ5.9), KHÔNG nhập toạ độ tay.
- `goc_theta`: góc θ (độ) — CHỈ để vẽ minh họa. `nhan_theta`: nhãn góc (math-mode, vd `r'\theta'`).
- `duong_kinh`: nhãn đặt trên đường chéo (vd `'30 cm'`). A=(−a,−b), B=(a,−b), C=(a,b), D=(−a,b) với a=R·cosθ, b=R·sinθ.

## duong_tron_nghiem(loai='sin', m=0.5, m_tex=None, ten1='M_1', ten2='M_2', R=2.6, out='dtng', scale=1.0)   ← [31p] MỚI
Đường tròn nghiệm phương trình LG cơ bản (SGK Bài 4): đường tròn đơn vị + đường thẳng cắt tại 2 ĐIỂM NGHIỆM. Máy TỰ tính giao điểm từ m (Đ5.9), KHÔNG nhúng ảnh SGK (Đ42).
- `loai='sin'`: đường NGANG y=m, 2 nghiệm đối xứng Oy (α và π−α). `loai='cos'`: đường DỌC x=m, 2 nghiệm đối xứng Ox (α và −α).
- `m` ∈ [−1;1] (vế phải). `m_tex`: nhãn LaTeX cho m (vd `r'\tfrac{1}{2}'`); None→in số.
- `ten1`/`ten2`: nhãn 2 điểm nghiệm (math-mode). Trọng tài: SGK Bài 4 (phương trình sin x=m / cos x=m).

## do_thi_luong_giac(ham='sin', out='dothi_lg', scale=1.0)   ← [31o] MỚI
Đồ thị hàm số lượng giác trên [-2π; 2π]: máy TỰ dựng đường cong từ công thức (pgfplots), KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
- `ham` ∈ {`'sin'`, `'cos'`, `'tan'`, `'cot'`}.
- sin/cos: đường liền, y∈[-1;1], mốc trục Ox theo bội π.
- tan: vẽ từng nhánh (tâm kπ), tiệm cận đứng nét đứt tại x=π/2+kπ; cot: nhánh (kπ,(k+1)π), tiệm cận tại x=kπ.
- Nhãn tick có nền trắng (không bị tiệm cận cắt qua). Trọng tài: SGK H1.14 (sin) / H1.15 (cos) / H1.16 (tan) / H1.17 (cot).

## duong_tron_luong_giac(goc=None, ten_M='M', hien_sin_cos=True, goc_phan_tu=False, hien_A=True, R=2.6, out='dtlg', scale=1.0)
Đường tròn lượng giác đầy đủ: tâm O, bán kính 1, điểm gốc A(1;0), chiều dương (+), trục x=cos/y=sin.
- `goc`: số đo góc α (độ) đặt điểm M; None → chỉ đường tròn nền + A.
- `hien_sin_cos`: gióng nét đứt + nhãn sin α (trên Oy), cos α (trên Ox) + cung α.
- `goc_phan_tu`: nhãn I, II, III, IV.
- Máy TỰ tính (cosα,sinα) từ góc (Đ5.9). Trọng tài: SGK H1.7/H1.9b/H1.10.

## goc_luong_giac(goc_v=55.0, goc_m=None, chieu='duong', out='goc_lg', scale=1.0)
Góc lượng giác: tia đầu Ou (ngang), tia cuối Ov tại `goc_v`°, cung cong + dấu (+/−) chỉ chiều.
- `goc_m`: nếu có → thêm tia quay Om (nét đứt xanh). `chieu`: 'duong' (ngược kim đồng hồ, +) / 'am' (−).
- Trọng tài: SGK H1.3.
