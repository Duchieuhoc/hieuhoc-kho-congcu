# BẢN TRÍCH HÀM VẼ — DS12_CH01 — tự sinh từ `hinh_ds12_giaitich.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `hinh_ds12_giaitich.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 16/10/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_ds12_giaitich as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `bang_bien_thien(moc, dau, gia_tri, danh_dau=None, ten_bien='x', ten_dh="y'", ten_ham='y', ky_am_vc='-\\infty', ky_duong_vc='+\\infty', bar_trai=False, bar_phai=False, out='bangbienthien', tra_bytes=False, scale=1.0)` | BẢNG BIẾN THIÊN (BBT) tổng quát — chuẩn SGK Giải tích 12 (tikz). Máy TỰ dựng mũi tên + đặt giá trị (Đ5.9). moc : list NHÃN mốc x tăng dần (math-string). VD ['-1','3'] · ['-1','0','1'] · [r'e^{-\frac12}'] · [] (đơn điệu). dau : list dấu y' MỖI KHOẢNG, len = len(moc)+1, '+' (đồng biến ↗) hoặc '-' (nghịch biến ↘). gia_tri : list giá trị y tại các cột [-∞, mốc_1, …, mốc_n, +∞], len = len(moc)+2 (math-string). • Cột thường: 1 nhãn, vd '34' · r'-\infty' · r'-\tfrac12'. • Cột TIỆM CẬN ĐỨNG (danh_dau='||'): list 2 nhãn [giới-hạn-TRÁI, giới-hạn-PHẢI], vd [r'-\infty', r'+\infty']. danh_dau : list cùng độ dài moc: '0' (y'=0, cực trị — MẶC ĐỊNH) | '||' (TCĐ, y' không xác định — kẻ vạch đôi). ten_dh : nhãn dòng 2 (đạo hàm): "y'", "f'(x)", "S'(x)". ten_ham: nhãn dòng 3: 'y', 'f(x)', 'V'. ky_am_vc / ky_duong_vc : nhãn mốc ngoài cùng (mặc định ±∞). Hàm trên khoảng/đoạn: đặt '0', 'a', '-1'… bar_trai / bar_phai : True → kẻ vạch biên tại mốc ngoài trái/phải (GTLN–GTNN trên đoạn [a;b]: y' không xác định tại hai đầu mút nhưng y có giá trị hữu hạn). VD1 B02: bar_trai+bar_phai. PHANH: len(dau)==len(moc)+1 ; len(gia_tri)==len(moc)+2 ; mỗi cột '||' phải cấp list 2 phần tử. |

---

**Thống kê:** 1 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
