# CAPNHAT_KHO — A.1-MỚI (28x → 28y · template v10.19 → v10.20)
**Đóng: Ông Bụt Đại số · 2026-09-08 · chỉ đạo Giám đốc (in dạy DS8 thấy hợp lý)**

## ⚠️ LUẬT ONE-WRITER (đọc trước)
File CHUNG với máy Hình. **Máy Hình ĐANG NGHỈ → cửa one-writer mở, push an toàn.** Template upload là ĐÈ, không merge.

## Việc thầy làm — PUSH GitHub `Duchieuhoc/hieuhoc-kho-congcu`
Đè/thêm 5 file:
- `hieuhoc_template.js`            (v10.20)
- `API_REFERENCE.md`              (tự sinh lại từ template)
- `Instructions_AI_Soan_DaiSo.md` (khung Dạng mới)
- `00_KHO_VERSION.txt`            (mốc 28y)
- `README_CAP_NHAT_28y.md`        (ghi chú mốc — thêm mới)

**Commit:** `[28y] A.1-mới: Phân tích và hướng dẫn giải + Ghi nhớ gộp; dangToanDayDu bỏ phuongPhapArr — template v10.20`

Sau push → kho ra **mốc 28y**. PIN SHA mới vào `00_HOSO_BAI` của các LƯU_BÀI về sau.

### (Tùy chọn) Nạp bằng git bundle
Kèm `kho_28y.bundle`. Nạp:  `git clone kho_28y.bundle kho-28y`  (hoặc `git fetch ../kho_28y.bundle`).

## Nội dung sửa (khớp README_CAP_NHAT_28y.md)
1. `phanTich()` — nhãn **"Phân tích và hướng dẫn giải:"** đứng RIÊNG dòng, nội dung chảy; +khe `{doan:[...]}`.
2. `dangToanDayDu()` — **BỎ** render `phuongPhapArr` (hết "Phương pháp chung").
3. **+`ghiNhoGop()`** — gộp cần nhớ + ✗→✓ dưới một nhãn **"Ghi nhớ:"** (bỏ nhãn "Sai lầm thường gặp"), guard **≤3 dòng**.
4. Guard khung A.1: cập nhật thông báo (vẫn cần `saiLamArr` + `ghiNhoArr`).

## Tương thích / Retrofit
`saiLamThuongGap` · `ghiNhoNhanh` · `phuongPhapGiai` GIỮ nguyên (dùng ngoài Dạng; `ghiNhoNhanh` cho Ghi nhớ mục ②). Bài cũ truyền `phuongPhapArr` → **bỏ qua** (không render). **Áp bài MỚI**; DS6/DS7/DS8 giữ nguyên.

## Kiểm chứng (đã làm)
- Build 1 Dạng qua `dangToanDayDu` (v10.20) → có "Phân tích và hướng dẫn giải:" + "Ghi nhớ:" (kèm ✗→✓); **KHÔNG** còn "Phương pháp chung"/"Sai lầm thường gặp"; "Vậy" ở lời giải; **XSD PASS**; guard ≤3 dòng chặn đúng; cửa `kiemMay` bắt thiếu khối định danh đúng.

## Sau push — nạp lại sang Project Knowledge
- `API_REFERENCE.md` + `Instructions_AI_Soan_DaiSo.md` → nạp CẢ 2 Project (OB Đại số + OB Hình).
- Tài liệu quản trị còn lại (HP V11.9 · CHUAN_TRINH_BAY · PhuLuc Đại số v1.5 · Quy_Trinh_QC) → xem phiếu Project Knowledge riêng.

## RIÊNG Hình — CHƯA đụng
Phụ lục Hình + Instructions Hình đổi cùng A.1-mới khi máy Hình chạy lại (khớp CHUNG).
