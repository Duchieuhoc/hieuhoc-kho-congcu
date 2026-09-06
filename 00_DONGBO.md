# ĐỒNG BỘ PROJECT KNOWLEDGE — sau mốc kho 28v (2026-09-06)

Kho GitHub: **thầy ĐÃ push 28v** (template v10.17). Việc còn lại là đồng bộ các file hạ nguồn.

## Thay trong Project Knowledge (CHUNG cả 2 máy OB Đại số + Hình)
1. **API_REFERENCE.md** → thay bằng bản trong gói này (đã regen v10.17: baiTapTaiLop +anLoiGiai; 2 cửa mới).
   Nạp Y HỆT cho MỌI Project cùng vai (OB Đại số + OB Hình + AI Soạn cả 2). *(1 bản chân lý — đừng đè lệch.)*
2. **Quy_Trinh_QC_OngBut.md** (Lớp 1) → thêm 1 dòng cửa quét `"undefined"`/`"[object Object]"` (đồng bộ kiemMay 28v):
   > 1.17 | **Chuỗi rác render** | quét `\bundefined\b` và `[object Object]` = 0 (nhãn/field/tham số render hụt — Word hiện chữ rác). Cửa kiemMay 28v đã chặn xuất.

## Riêng nhánh Đại số
3. **TON_CHUONG__DS8_CH01.md** (trong gói) → đưa vào Project nhánh Đại số làm sổ tồn chương (seed 4 mục; bổ sung dần).
4. Nếu Phụ lục Đại số pin "mốc kho yêu cầu" → cập nhật lên **28v**.

## KHÔNG cần regen
- BAN_TRICH_HAM_* : API public không đổi chữ ký (baiTapTaiLop chỉ +param tùy chọn) → giữ nguyên.
- hinh_*.py : 28v không đụng hình.
