# ĐỒNG BỘ PROJECT KNOWLEDGE — sau mốc kho 28x (v10.19) · 2026-09-06
Kho GitHub: **thầy ĐÃ push 28x** (SHA f3cdacb, template v10.19). Gói này để nạp lại các file hạ nguồn.

## THAY trong Project Knowledge — nạp Y HỆT cho MỌI Project cùng vai (OB Đại số · OB Hình · AI Soạn)
1. **`API_REFERENCE.md`** → thay bằng bản trong gói (regen v10.19 từ template LIVE; đã có `soGachTren`,
   `baiTapTaiLop` +anLoiGiai, các cửa mới). *(1 bản chân lý — đừng đè lệch giữa 2 máy.)*
2. **`Instructions_AI_Soan_DaiSo.md`** → thay bằng bản trong gói (RIÊNG Đại số): 2 luật mới
   (KHÔNG khối MỞ RỘNG; `dapAn` bọc `[[…]]`) + mốc kho ≥28v.

## SỬA TAY 1 dòng (Lớp 1)
3. **`Quy_Trinh_QC_OngBut.md`** → thêm vào Lớp 1:
   > 1.17 | **Chuỗi rác render** | quét `\bundefined\b` và `[object Object]` = 0 (nhãn/field/tham số render hụt). Cửa `kiemMay` 28v đã chặn xuất; QC soi lại theo tổ-tiên, không regex kề.

## Ghi chú `dangToanDayDu` trong API_REFERENCE (auto-gen)
Chữ ký nay in **cả `viDuLoiGiai, loiGiaiND`** (side-effect tốt của bí danh 28x — hết thiếu khóa như trước).
Khóa CHUẨN là **`viDuLoiGiai`**; `loiGiaiND` được nhận làm bí danh; thiếu cả hai → THROW rõ (hết fail-im-lặng).
Còn lẫn vài khóa của `baiTapTaiLop` (soBai/mucDo/deBai/cacCau/thamChieu) do `sinh_apiref.js` đọc hàm kiểu `(p)`
chưa chuẩn — KHÔNG ảnh hưởng dùng. Việc treo: sửa `sinh_apiref.js` (đã ghi trong BÀN_GIAO_LUONG).

## KHÔNG cần đụng
- `BAN_TRICH_HAM_*` : API public không đổi chữ ký (chỉ thêm hàm/bí danh) → giữ nguyên.
- `hinh_*.py` : 28v→28x không đổi hình.
