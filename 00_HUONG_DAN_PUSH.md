# CẬP NHẬT KHO → mốc 2026-08-26a
**Ngày:** 2026-08-26 · **Người làm:** Ông Bụt · **Lý do:** thầy chốt "nền ô lưới 4mm mờ cho MỌI hình".

## Push lên GitHub (qua web) — 2 file thay thế TRỌN VẸN
Repo: `github.com/Duchieuhoc/hieuhoc-kho-congcu`
1. `hinh_coban.py` → thay file cùng tên.
2. `00_KHO_VERSION.txt` → thay file cùng tên (mốc đầu bảng đã là **2026-08-26a**).

## Có gì mới (26a)
- `ve()` tự vẽ **nền ô lưới mờ** (`black!12` — viền thật nhạt) phủ **cả khung mọi hình** (kể cả hình không gọi `luoi`: thoi/lục giác/tròn…). Bbox tính cả bán kính đường tròn.
- `ve()` đặt `self.so_o_ngang / self.so_o_doc` → **chèn docx `rongCm = 0,4 × so_o_ngang`** ⇒ ô = **4mm/trang**. (Thay hệ số K=0.256 treo từ 25/08.)
- Lưới tường minh (`luoi`) đổi màu `gray!35 → black!12` cho đồng nhất.
- Tắt nền khi cần: `h._nen_luoi = False`.
- **KHÔNG đổi chữ ký hàm** → bản trích `BAN_TRICH_HAM_HH6_CH05.md` giữ nguyên, không cần sinh lại.

## Kiểm sau khi push
- `python3 quet_stamp.py` → thấy **2026-08-26a**.
- Bất kỳ hình nào gọi `.ve()` → có nền ô lưới mờ; đọc `h.so_o_ngang` ra số nguyên.
