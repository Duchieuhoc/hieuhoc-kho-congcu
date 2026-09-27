# UPLOAD KHO — Bộ hàm BIỂU ĐỒ & MÔ HÌNH XÁC SUẤT (mốc 2026-09-28, tag 31a)
> Thầy upload đè 4 file dưới lên repo **Duchieuhoc/hieuhoc-kho-congcu** (web → Add file/Upload → Commit).
> Đều nằm ở GỐC repo. Không xóa file nào khác.

## File cần upload (4)
1. `bieudo_xstk.py`            — MODULE MỚI (lớp figure matplotlib: 8 hàm biểu đồ/mô hình XS).
2. `sinh_bantrich.py`          — VÁ: +chế độ module one-shot. **Tương thích ngược** — module hình học cũ không đổi.
3. `BAN_TRICH_HAM_DS6__bieudo.md` — bản trích 8 hàm (tự sinh cho AI Soạn).
4. `00_KHO_VERSION.txt`        — bump mốc 2026-09-28 (entry 31a ở đầu).

## Sau khi upload
- Mốc kho mới = **2026-09-28**. Khi soạn XS-TK, luật (Phụ lục Đại số) ghi "mốc kho yêu cầu ≥ 2026-09-28".
- Đã test render 8/8 hàm (cột, cột âm, cột kép, thanh ngang kép, tranh icon lẻ ½, vòng quay, xúc xắc, đồng xu, túi bi, trục 0–1) — đạt.
- Chưa đụng `hieuhoc_template.js`. Không bump version JS.

## Kiểm nhanh sau upload (tùy chọn, ở thread khác)
`import bieudo_xstk as BD; BD.bieu_do_cot(['6A','6B'],[32,27], out='t'); ` → ra /tmp/t.png.
