# VÁ KHO [32i]+[32j] — gộp 1 lần upload — 2026-10-06

> **Phiếu này THAY phiếu `00_DOC_TRUOC_UPLOAD__32i.md`** (bản template mới đã gộp cả 2 mốc). Chỉ cần upload theo phiếu này.

## THẦY LÀM GÌ: upload đè 2 file này lên GitHub (repo hieuhoc-kho-congcu)
Vào https://github.com/Duchieuhoc/hieuhoc-kho-congcu → Add file → Upload files →
kéo-thả 2 file dưới → Commit changes. (Upload ĐÈ, giữ nguyên các file khác.)

## 2 FILE:
| File | Loại | Ghi chú |
|---|---|---|
| hieuhoc_template.js | SỬA (additive) | Mang CẢ [32i] (tách ý a)b)c) trong đề) + [32j] (dấu ⋅ tích vô hướng → Cambria Math) |
| 00_KHO_VERSION.txt | BUMP | Thêm mốc [32i] + [32j] (nối tiếp [32h]) |

## VÁ GÌ (2 mốc trong 1 file template):

**[32i] — Ý con a)b)c) của ĐỀ → mỗi ý 1 dòng** (chỉ đạo Giám đốc 06/10):
- +2 helper nội bộ `_tachYDeBai` + `_deBaiParas`; wire vào viDu / baiTapTaiLop / tuLuanBTVN. Đề nhiều ý nướng trong `deBai` → tách mỗi ý 1 dòng (nhãn đậm, căn trái).
- Nghiệm thu B10: Ví dụ 2/3/4 + 5 Bài tập mẫu ra a)/b)/c)/d) riêng dòng; Ví dụ 1 giữ nguyên.

**[32j] — Dấu ⋅ tích vô hướng → Cambria Math** (lộ khi QC B11 "Tích vô hướng hai vectơ"):
- `_RE_TOAN` +`⋅` (⋅ = `\cdot`). AI Soạn dùng ⋅ (lọt cửa vì chỉ · U+00B7 bị chặn) nhưng 136/138 dấu rơi font TNR = rủi ro tofu trong Word thật. Route sang Cambria Math là font-proof.
- Nghiệm thu B11 rebuild: 136 dấu ⋅ chuyển TNR→Cambria Math; kiemMay=[]; 9 hình=9 blip.

## AN TOÀN (0 regression):
- CHỮ KÝ HÀM KHÔNG ĐỔI (helper [32i] không export; [32j] chỉ +1 ký tự regex) → KHÔNG regen BAN_TRICH/API.
- [32i]: string thuần / không ≥2 ý từ a) → giữ hành vi cũ. Đối sánh B07/B08/B09/B11 cũ↔mới: 0 đổi (đã dùng `cacCau` đúng).
- [32j]: không bài nào dùng ⋅ (U+22C5) làm gì khác → 0 regression. CẤM · (U+00B7, dấu nhân) VẪN bị cửa `xuatFile` chặn.
- KHÔNG đụng: hinh_core.py, các hinh_*.py, gop_chuong.js, noi_tai_lieu.js.

## SAU KHI UPLOAD:
- Mốc kho GitHub = [32j] @ HEAD mới. Thread sau `git clone` có cả 2 bản vá.
- B10 + B11 rebuild (tôi đã dựng sẵn bằng template mới) sẵn sàng cho V3.
- Cập nhật "mốc kho yêu cầu CH04" trong Instructions = ≥ [32i] (đã sửa trong Project).
