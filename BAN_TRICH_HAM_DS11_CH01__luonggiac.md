# BẢN TRÍCH HÀM — HÌNH LƯỢNG GIÁC THPT (hinh_ds11_luonggiac.py) · kho [31o]
> import: `import hinh_ds11_luonggiac as LG` (tự gắn vào HinhTron). Render qua render script (Python) → PNG, build.js nhúng bằng `H.hinhVe`.

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
