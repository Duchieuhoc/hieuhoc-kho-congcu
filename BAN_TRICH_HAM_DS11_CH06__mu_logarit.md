# BẢN TRÍCH HÀM — ĐỒ THỊ HÀM MŨ & HÀM LÔGARIT THPT (hinh_ds11_mu_logarit.py) · kho [31y]
> import: `import hinh_ds11_mu_logarit as ML`. Render qua render script (Python) → PNG; build.js nhúng bằng `H.hinhVe({ imageBuffer: buf })` (gọi hàm với `tra_bytes=True`).
> Triết lý Đ5.9: hàm nhận NGHĨA (cơ số a), máy TỰ dựng đường cong từ công thức (pgfplots) — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).

## do_thi_ham_mu(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, out='dothi_mu', tra_bytes=False, scale=1.0)   ← [31y] MỚI
Đồ thị HÀM SỐ MŨ $y=a^x$ (SGK H6.1 dạng tổng quát / H6.2 cụ thể). Máy tự dựng đường cong bằng pgfplots `exp(x·ln a)`; luôn nằm trên Ox (tiệm cận ngang Ox), đi qua $(0;1)$ và $(1;a)$.
- `co_so`: cơ số $a>0,\ a\ne1$ (số). $a>1$ → đồng biến; $0<a<1$ → nghịch biến. Phân số truyền dạng số (vd `1/2`, `1/3`).
- `nhan`: nhãn đường cong (None → tự sinh `y=2^x` / `y=\left(\tfrac12\right)^x`…). Dạng tổng quát truyền chuỗi LaTeX, vd `r'y=a^{x}\ (a>1)'`.
- `hien_diem`: True → chấm 2 điểm mốc $(0;1),(1;a)$ + gióng nét đứt tới trục.
- `tong_quat`: **False** = đồ thị CỤ THỂ (hiện số trục 1..8 / −3..3; dùng cho VD1 $y=(\tfrac12)^x$, LT $y=(\tfrac32)^x$, BT 6.15 $y=3^x$/$(\tfrac13)^x$, SBT 6.21). **True** = DẠNG TỔNG QUÁT (ẩn số trục, chỉ hiện ký hiệu $1$ và $a$) — dùng cho **Hình 6.1** (gọi 2 lần: `co_so=2, tong_quat=True, nhan=r'y=a^{x}\ (a>1)'` và `co_so=0.5, …nhan=r'y=a^{x}\ (0<a<1)'`).
- Trọng tài: SGK H6.1 (dạng $y=a^x$) / H6.2 ($y=(\tfrac12)^x$).

## do_thi_ham_log(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, out='dothi_log', tra_bytes=False, scale=1.0)   ← [31y] MỚI
Đồ thị HÀM SỐ LÔGARIT $y=\log_a x$ (SGK H6.3 dạng tổng quát / H6.4 cụ thể). Máy tự dựng bằng pgfplots `ln(x)/ln(a)`; tập xác định $x>0$ (tiệm cận đứng Oy), đi qua $(1;0)$ và $(a;1)$.
- `co_so`: cơ số $a>0,\ a\ne1$. $a>1$ → đồng biến; $0<a<1$ → nghịch biến.
- `nhan`: nhãn đường cong (None → tự sinh). Dạng tổng quát: `r'y=\log_a x\ (a>1)'`.
- `hien_diem`: True → chấm $(1;0),(a;1)$ + gióng nét đứt.
- `tong_quat`: **False** = CỤ THỂ (hiện số trục; dùng VD2 $y=\log_{\frac12}x$, BT 6.16 $y=\log x$/$\log_{\frac13}x$, SBT 6.22). **True** = TỔNG QUÁT (ẩn số trục, ký hiệu $1,a$) — dùng **Hình 6.3** (gọi 2 lần cho $a>1$ và $0<a<1$).
- Trọng tài: SGK H6.3 (dạng $y=\log_a x$) / H6.4 ($y=\log_{\frac12}x$).

> **Lưu ý dựng Hình 6.1 & 6.3 (dạng tổng quát 2 panel):** mỗi hình SGK là 2 đồ thị cạnh nhau ($a>1$ và $0<a<1$) → gọi hàm **2 lần** (2 PNG rời), build.js xếp cạnh nhau. Cơ số đại diện: $a=2$ (cho $a>1$), $a=0{,}5$ (cho $0<a<1$) — chỉ lấy DÁNG, nhãn ghi tổng quát.
> **Bài 21 (Hình 6.5–6.8 minh hoạ nghiệm PT/BPT):** chưa có hàm riêng — khi dựng B21, nếu cần đường thẳng $y=b$ cắt đồ thị, báo `[SỬA]` để OB bổ tham số `duong_ngang=b` vào 2 hàm trên (đã dự phòng, pilot B20 chưa cần).
