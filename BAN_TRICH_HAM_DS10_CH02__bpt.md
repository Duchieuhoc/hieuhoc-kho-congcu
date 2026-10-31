# BẢN TRÍCH HÀM VẼ — DS10_CH02 — tự sinh từ `hinh_bpt.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `hinh_bpt.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 31/10/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_bpt as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `mien_nghiem(bpt, diem=None, khung=None, nhan_duong=None, ten_mien=None, out='mien_nghiem', tra_bytes=False, dpi=200)` | Vẽ miền nghiệm của 1 BPT hoặc hệ BPT bậc nhất hai ẩn trên mặt phẳng Oxy. bpt : list (a, b, c, dau) — a·x+b·y <dau> c ; dau ∈ '<=','>=','<','>','=' ('=' chỉ vẽ đường, không tô). diem : list (x, y, 'nhãn') đỉnh/điểm đánh dấu (có thể None). khung : (xmin,xmax,ymin,ymax) ; None → tự canh. nhan_duong : list nhãn mỗi đường (theo thứ tự bpt) ; None → không ghi. ten_mien : nhãn giữa miền nghiệm ; None → bỏ. |

---

**Thống kê:** 1 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
