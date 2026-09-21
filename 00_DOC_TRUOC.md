# GÓI B1 [30a] — TÁCH `hinh_toado.py` (primitive toạ độ dùng chung)

## Làm gì
Tách các primitive toạ độ **cross-cutting** ra khỏi `hinh_daiso.py` (silo sai tên) sang
**`hinh_toado.py` (DÙNG CHUNG)** — vá đúng gốc DS9 (điều 4↔5 trong Quy ước sửa kho).
- `hinh_toado.py` (MỚI): `class Hinh(HinhCoBan)` + `tia_so, truc_so_huu_ti, truc_do_chinh_xac,
  truc_doan_doc_diem` (+ helper `_vach*/_danh_dau/_so`) + `hinhMatPhangToaDo` (+ `_mptd_*`).
- `hinh_daiso.py` (SỬA): `class Hinh(hinh_toado.Hinh)` — kế thừa toạ độ, giữ phần THUẦN đại số
  (`dung_can_hai`, `hinhDienTichDaiSo`). **Backward-compatible**: `hinh_daiso.Hinh()` vẫn đủ mọi method cũ.

## Kiểm chứng (đã chạy)
- **7/7 hình render PIXEL-KHỚP** trước vs sau (md5 trùng): tia_so, truc_so_huu_ti, truc_do_chinh_xac,
  truc_doan_doc_diem, dung_can_hai, hinhDienTichDaiSo, hinhMatPhangToaDo → **không vỡ DS6/DS7**.
- `hinh_daiso.Hinh()` đủ 7 method; `hinh_toado.Hinh()` có primitive toạ độ.
- `sinh_mucluc` → **vẫn 132**, không double-count (tia_so 1 lần); re-home đúng nhóm
  "Toạ độ & trục số (DÙNG CHUNG)" (5) + "Số & Đại số" (2).
- Bản trích DS9_CH01 regen: AI Soạn vẫn thấy đủ hàm (qua kế thừa) — không đổi cách gọi.

## Up thế nào
| File | Thao tác |
|---|---|
| `hinh_toado.py` | **THÊM MỚI** |
| `hinh_daiso.py` | **THAY** (hoặc áp `PATCH_30a…diff`) |
| `00_MUC_LUC_HAM.md` | **THAY** (regen, vẫn 132, đã re-home) |
| `BAN_TRICH_HAM_DS9_CH01__daiso.md` | **THAY** (regen) |

→ Bump `00_KHO_VERSION.txt` tag **[30a]**.

## LƯU Ý VÙNG DÙNG CHUNG (quan trọng)
`hinh_toado.py` từ nay là **module DÙNG CHUNG** (Hình ↔ Đại số). **Báo máy Hình pull về**; từ nay
sửa vùng toạ độ theo luật: một-máy-một-lúc + CHANGELOG + bump mốc (Quy ước §5). Đại số/Hình
**GỌI LẠI** primitive toạ độ ở đây, **cấm viết mới** trùng.

KHÔNG đụng: `hieuhoc_template.js` · `API_REFERENCE.md` · `sinh_*` · các file [29z].
