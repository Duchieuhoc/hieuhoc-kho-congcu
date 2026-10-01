# BẢN TRÍCH HÀM — HÌNH LƯỢNG GIÁC THPT (hinh_ds11_luonggiac.py) · kho [31n]
> import: `import hinh_ds11_luonggiac as LG` (tự gắn vào HinhTron). Render qua render script (Python) → PNG, build.js nhúng bằng `H.hinhVe`.

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
