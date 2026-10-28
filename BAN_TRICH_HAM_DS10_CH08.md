# BẢN TRÍCH HÀM VẼ — DS10_CH08 — tự sinh từ `hinh_ds10_ch08.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `hinh_ds10_ch08.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 28/10/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_ds10_ch08 as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `so_do_cay_dem(goc, con, out='so_do_cay_dem', tra_bytes=False, scale=1.0, dx=2.2, dy=2.0, dem_la=False)` | Sơ đồ hình cây ĐẾM (quy tắc cộng/nhân): gốc→nhánh→lá, nhãn cụm từ tiếng Việt, đa tầng & lệch độ sâu; dem_la=True tự đánh số lá. VD H.8.2 vé tàu, H.8.3 phở/bún. |

---

**Thống kê:** 1 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
