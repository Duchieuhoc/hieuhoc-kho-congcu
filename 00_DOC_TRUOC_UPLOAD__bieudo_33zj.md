# ĐỌC TRƯỚC — UPLOAD KHO [33zj] (bổ 2 hàm biểu đồ cho DS8_CH05 Thống kê)

**Thầy đè 3 file này lên GitHub `hieuhoc-kho-congcu`** (web → kéo-thả → Commit). ADDITIVE, không xoá gì.

| File | Thay đổi |
|---|---|
| `bieudo_xstk.py` | +2 hàm cuối file: `bieu_do_quat` (quạt tròn %), `bieu_do_doan_thang` (đoạn thẳng 1/nhiều đường). 11 hàm cũ + helper giữ nguyên. |
| `BAN_TRICH_HAM_DS6__bieudo.md` | Tái sinh (13 hàm) — AI Soạn đọc bản này để gọi 2 hàm mới. |
| `00_KHO_VERSION.txt` | +entry `[33zj]`, Mốc kho → **2026-11-03**. |

**Vì sao:** chương V (DS8_CH05 Thống kê) dùng 5 loại biểu đồ; kho mới có 3 (cột/cột kép/tranh). 2 hàm này là quạt tròn + đoạn thẳng — 2 loại dùng nhiều nhất chương V, trước đây mới "dự phóng". Dựng theo đúng quy ước tham số đã định (`danh_muc/gia_tri/nhom/tieu_de/nhan_truc_*`).

**Đã nghiệm thu:** render dữ liệu thật ĐẠT (soi mắt) — quạt cầu THĐ 7/13/44/36; đoạn thẳng kép Canberra/Moscow 12 tháng cắt nhau T3·T9. Hàm cũ chạy lại OK (không vỡ).

**Kỷ luật lệch pha:** gói này clone trên HEAD `[33zi]` (mốc 2026-11-01) — bản mới nhất lúc dựng. template.js KHÔNG đổi → **không cần regen API_REFERENCE**.

**Sau khi thầy upload:** cập nhật "mốc kho yêu cầu ≥ 2026-11-03" trong Phụ lục Đại số (cho các bài DS8_CH05 dùng quạt/đoạn thẳng). AI Soạn tự bụng kho → có ngay 2 hàm.
