# CẬP NHẬT KHO — mốc [36d] · hinh_hoa_ch06.py bản ĐỦ chương VI (B18–B21)
### OB Hóa THCS · 2026-11-24 · ĐỀ XUẤT · THAY/GỘP các mốc 36a..36c

## Gộp một lần
Mốc này THAY gói `CAPNHAT_KHO__36a` cũ (chỉ có B18). `hinh_hoa_ch06.py` nay là bản
ĐỦ cho cả 4 bài B18–B21 của Chương VI — push 1 lần là xong cả chương.

## 10 hàm phơi cho AI Soạn (4 họ sơ đồ · ADDITIVE · 0 đổi hàm cũ)
| Bài | Hàm |
|---|---|
| B18 | thi_nghiem_binh_khi · phan_ung_phi_kim(Fe_O2·Na_Cl2·Fe_Cl2) · mach_thu_dan_dien · thi_nghiem_dan_nhiet |
| B19 | ong_nghiem_phan_ung · thi_nghiem_day_hoat_dong(Fe_HCl·Cu_AgNO3) |
| B20 | be_dien_phan_nhom · lo_cao_luyen_gang · lo_thoi_luyen_thep |
| B21 | cot_loc_than |

**Sơ đồ công nghiệp B20** dùng CALLOUT SỐ trong hình + chú giải tiếng Việt in ở Word
(pdflatex không dựng được dấu tiếng Việt; đã thử vietnam/vntex/babel đều rớt "ử","ươ").
Mỗi hàm B20/B21 kèm thuộc tính `.CHU_GIAI` (dict số→nghĩa) để AI Soạn in chú giải.

## File (push đè GitHub)
- hinh_hoa_ch06.py (bản đủ 10 hàm)
- BAN_TRICH_HAM_HOA9_CH06.md (regen — 10 hàm)
- 00_MUC_LUC_HAM.md (regen — 188 hàm Python)
- 00_KHO_VERSION.txt (thêm mốc [36d])

## KHÔNG đụng
hieuhoc_template.js · API_REFERENCE · hinh_core.py · mọi kho chương khác · chữ ký hàm cũ.

## Nghiệm thu
- import OK; render 11/11 hình sạch (5 B18 + 2 B19 + 3 B20 + 1 B21).
- Dựng B18, B19, B20, B21 bản GV: cả 4 xuất qua kiemMay SẠCH (0 lỗi), đủ blip hình.

## THẦY LÀM GÌ
1. Chạy `python3 kiemtra_hinh_hoa_ch06.py` trong ~/kho (sau khi đặt module) — phải "ĐẠT".
2. Push đè GitHub 4 file trên (KHÔNG push kiemtra_*.py, 00_DANH_MUC, 00_CAPNHAT).
3. Đặt "Mốc kho yêu cầu" khối Hóa 9 = [36d] / 2026-11-24.
