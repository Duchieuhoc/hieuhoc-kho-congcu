# GÓI [29y] — thêm hinhMatPhangToaDo vào hinh_daiso.py (dựng lại trên nền live có [29z])

**Vì sao có gói này:** kho live đã có [29z] (mục lục + quy ước) nhưng THIẾU [29y] → `00_MUC_LUC_HAM.md`
đang nhắc `hinhMatPhangToaDo` mà `hinh_daiso.py` chưa có (lệch). Up gói này là khớp lại (132 hàm).

## Up thế nào
- Thay `hinh_daiso.py` trong kho bằng file trong gói (hoặc áp `PATCH_29y…diff` — thuần append +101 dòng).
- Thay `BAN_TRICH_HAM_DS9_CH01__daiso.md` bằng bản regen kèm đây.
- KHÔNG cần đổi `00_MUC_LUC_HAM.md` (bản đã commit vốn đã tính 132 — sau khi up code này là khớp).
- Bump 00_KHO_VERSION.txt (tag [29y]).

## Kiểm chứng (đã chạy)
- import + render OK; backward-compat: `tia_so`, `truc_so_huu_ti`… còn nguyên.
- `sinh_mucluc.py` trên nền có file này → **132 hàm**, khớp mục lục đã commit.

KHÔNG đụng: hieuhoc_template.js · API_REFERENCE.md · các file [29z].
