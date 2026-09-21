<!-- PHIẾU CẬP NHẬT KHO · [29z] · 2026-09-21 · OB Đại số (hợp nhất phản biện OB Hình) -->
# PHIẾU CẬP NHẬT KHO — [29z] · Quy ước + Mục lục hàm tổng

## Thêm vào kho (an toàn, không sửa file đang chạy)
| File | Vai trò |
|---|---|
| `sinh_mucluc.py` | Sinh mục lục hàm TỔNG — tái dùng `sinh_bantrich.py` + `API_REFERENCE.md` (không parse độc lập) |
| `00_MUC_LUC_HAM.md` | Mục lục tự sinh: **58 hàm Python + 74 JS = 132**, gộp theo nghĩa. Tra "đã-có-chưa" TRƯỚC khi viết |
| `00_QUY_UOC_SUA_KHO.md` | Quy ước hợp nhất (Thang bậc dùng kho + 6 điều + checklist 6 gạch + kế hoạch B1) |

## Cài
1. Chép 3 file trên vào gốc kho (cạnh các file `00_`).
2. Regen mục lục bất cứ lúc nào: `python3 sinh_mucluc.py > 00_MUC_LUC_HAM.md`.
3. Bump `00_KHO_VERSION.txt` (tag [29z]).

## CÒN TREO — B1 (làm lượt riêng)
Tách `hinh_toado.py` (gom primitive toạ độ khỏi `hinh_daiso.py`, qua kế thừa, backward-compatible) — xem mục 4 của `00_QUY_UOC_SUA_KHO.md`. Là refactor module đang chạy → làm riêng có test đầy đủ, đụng vùng dùng chung nên báo máy Hình trước.

## KHÔNG đổi
`hieuhoc_template.js` · `hinh_daiso.py` (bản [29y] giữ nguyên) · `API_REFERENCE.md`.
