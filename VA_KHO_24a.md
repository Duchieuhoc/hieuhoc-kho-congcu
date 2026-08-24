# VÁ KHO 2026-08-24a — Ông Bụt (Pha A hình B11)
Tương thích ngược. Áp: đè 4 file vào repo → kiểm `python3 quet_stamp.py` SẠCH → mốc ≥ 24a.

1. **hinh_gocdt._tach_ten** — tên có dấu phẩy kép ″ (`d″`, `x″`) giữ nguyên 1 nhãn.
   Trước 24a: `"d″"` bị tách nhầm thành 2 đầu `d` | `″` (nhãn đường sai). Cần cho hVD.
2. **hinh_coban.so_do_goc(ten, do=None, …)** — `do=None` → TỰ ĐO từ toạ độ; vẽ cung đánh dấu góc
   không cần khai số, không đụng `h.V` trong script (qua cổng AST). Cần cho cung Â₁/B̂₁/B̂₂ ở h346.
   Bản trích `BAN_TRICH_HAM_HH7_CH03.md` đã tái sinh theo chữ ký mới.
