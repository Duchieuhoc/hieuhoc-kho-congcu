# BẢN TRÍCH HÀM — ĐỒ THỊ HÀM MŨ & HÀM LÔGARIT THPT (hinh_ds11_mu_logarit.py) · kho [31z]
> import: `import hinh_ds11_mu_logarit as ML`. Render → PNG; build.js nhúng `H.hinhVe({ imageBuffer: buf })` (gọi hàm `tra_bytes=True`).
> Triết lý Đ5.9: hàm nhận NGHĨA (cơ số a), máy TỰ dựng đường cong (pgfplots) — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).

## do_thi_ham_mu(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, duong_ngang=None, nhan_ngang=None, out='dothi_mu', tra_bytes=False, scale=1.0)   ← [31z]
Đồ thị HÀM SỐ MŨ $y=a^x$ (SGK H6.1/H6.2). Qua $(0;1),(1;a)$, tiệm cận ngang $Ox$.
- `co_so`: cơ số $a>0,\ a\ne1$ (số). $a>1$ đồng biến; $0<a<1$ nghịch biến. Phân số truyền dạng số (`1/2`, `1/3`).
- `nhan`: nhãn đường cong. None → tự sinh (số nguyên / phân số đẹp mẫu ≤12). **Cơ số vô tỉ (√2, √3) → BẮT BUỘC truyền `nhan`** (vd `nhan=r'y=(\sqrt3)^{x}'`), nếu không hàm **raise** (chống nhãn rác).
- `hien_diem`: chấm $(0;1),(1;a)$ + gióng nét đứt.
- `tong_quat`: **False** = CỤ THỂ (hiện số trục; VD1, LT, BT 6.15, SBT 6.21). **True** = TỔNG QUÁT (ẩn số trục, ký hiệu $1,a$) — **Hình 6.1** (gọi 2 lần: `co_so=2,tong_quat=True,nhan=r'y=a^{x}\ (a>1)'` và `co_so=0.5,…nhan=r'y=a^{x}\ (0<a<1)'`).
- `duong_ngang=b`: vẽ đường $y=b$ (đỏ) cắt đồ thị tại $x=\log_a b$ + chấm giao + gióng đứng — **minh hoạ nghiệm $a^x=b$ (Bài 21: Hình 6.5/6.7)**. `nhan_ngang`: nhãn đường (mặc định `y=b`). Thường kèm `hien_diem=False`.
- Trọng tài: SGK H6.1/H6.2.

## do_thi_ham_log(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False, duong_ngang=None, nhan_ngang=None, out='dothi_log', tra_bytes=False, scale=1.0)   ← [31z]
Đồ thị HÀM SỐ LÔGARIT $y=\log_a x$ (SGK H6.3/H6.4). TXĐ $x>0$ (tiệm cận đứng $Oy$), qua $(1;0),(a;1)$.
- `co_so`, `nhan` (vô tỉ phải truyền, else raise), `hien_diem`, `tong_quat` — như trên. **Hình 6.3**: gọi 2 lần ($a>1$ và $0<a<1$).
- **Khung thích ứng cơ số:** cơ số lớn (vd $a=10$ → $y=\log x$, BT 6.16a) tự nới `xmax` + tick thưa để điểm $(a;1)$ luôn trong khung.
- `duong_ngang=b`: vẽ $y=b$ cắt tại $x=a^b$ + chấm + gióng — **minh hoạ nghiệm $\log_a x=b$ (Bài 21: Hình 6.6/6.8)**.
- `tong_quat`: CỤ THỂ (VD2, BT 6.16, SBT 6.22) / TỔNG QUÁT (Hình 6.3).
- Trọng tài: SGK H6.3/H6.4.

> **Hình 6.1 & 6.3 (2 panel):** mỗi hình = 2 PNG rời ($a>1$ + $0<a<1$), xếp `hinhBenTrai`/`hinhBenPhai`.
> **Bài 21 (Hình 6.5–6.8 minh hoạ nghiệm PT/BPT):** dùng `duong_ngang=b` (+ `hien_diem=False`) — đã render-verify, **KHÔNG cần pilot lại**. VD: `ML.do_thi_ham_mu(2.0, duong_ngang=4, nhan_ngang='y=4', hien_diem=False)` (Hình 6.7); `ML.do_thi_ham_log(2.0, duong_ngang=2, nhan_ngang='y=2', hien_diem=False)` (Hình 6.8).
