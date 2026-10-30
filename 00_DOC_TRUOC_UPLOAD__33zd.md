# CẬP NHẬT KHO [33zc] → [33zd] — thầy UPLOAD ĐÈ GitHub
### Repo: https://github.com/Duchieuhoc/hieuhoc-kho-congcu (public)
### OB Hình THPT · 2026-10-30 · phát sinh khi soạn HH11_CH07_B27 (khối xiên H.7.95/7.97/7.31)

## 1. VÌ SAO
`lang_tru_xien` (đã có từ [33zb]) chỉ dựng lăng trụ/hộp xiên **tịnh tiến đều** → không ghim được đỉnh trên vào đúng **chân chiếu** (trung điểm AC, tâm O, hình chiếu H) nên đường cao A′H/A′O vẽ bị xiên, sai nghĩa "⊥ đáy". Vá [33zd] **MỞ RỘNG** hàm này (thêm tham số), KHÔNG viết hàm mới (bậc ③ `QUY_UOC_SUA_KHO`). ADDITIVE — bài cũ 0 đổi.

## 2. FILE ĐÈ (4 file — kéo-thả lên GitHub, Commit changes)
| File | Thay đổi |
|---|---|
| `hinh_hh11_ch07.py` | `lang_tru_xien` +kwargs `apex / chan / ten_chan / duong_cao / o_vuong / nhan_chan` (ghim chân + đường cao ⊥ + ô vuông) |
| `00_KHO_VERSION.txt` | +khối [33zd] trên đầu (bump mốc + CHANGELOG) |
| `BAN_TRICH_HAM_HH11_CH07.md` | tái sinh (`sinh_bantrich.py`) — chữ ký `lang_tru_xien` mới |
| `00_MUC_LUC_HAM.md` | tái sinh (`sinh_mucluc.py`) |

## 3. SAU PUSH
- Mốc kho GitHub ra **[33zd]** (2026-10-30). Bài nào dùng khối xiên pin SHA mới vào `00_HOSO_BAI` khi LƯU BÀI.
- Cập nhật "mốc kho yêu cầu" khối xiên trong Phụ lục/Instructions nếu cần (CH07 ≥ [33zd] cho hình nghiêng có đường cao).
- Đồng bộ phiếu khai nghĩa B27 (C.2: R-khoi-xien ✅ CÓ) — xem GUI_OB.

## 4. KIỂM TRƯỚC KHI ĐÈ (OB đã chạy)
- `node`/`python3 -c "import hinh_hh11_ch07"` OK · render 3 khối xiên (apex+chan+duong_cao) đạt · regression `lang_tru_xien` cũ + `chop_cut_deu` PASS.
