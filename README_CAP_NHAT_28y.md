# CẬP NHẬT KHO — mốc 28y (template v10.20) · 2026-09-08

## Đợt "A.1 mới" — sửa khung Dạng toán (chỉ đạo Giám đốc, sau khi in dạy DS8 thấy hợp lý)

**File đổi trong kho:**
- `hieuhoc_template.js` → **v10.20** (từ v10.19/28x)
- `API_REFERENCE.md` → tự sinh lại (`node sinh_apiref.js hieuhoc_template.js > API_REFERENCE.md`)
- `Instructions_AI_Soan_DaiSo.md` → đồng bộ khung Dạng mới

**Thay đổi code `hieuhoc_template.js`:**
1. `phanTich()` — đổi nhãn **"Phân tích: " → "Phân tích và hướng dẫn giải:"**, nhãn đứng RIÊNG 1 dòng, nội dung xuống dòng chảy tự nhiên. Nhận thêm khe `{ doan:[block1, block2,…] }` để tách NHIỀU đoạn (chỉ khi sang ý thật sự khác).
2. `dangToanDayDu()` — **BỎ render `phuongPhapArr`** (không còn khối "Phương pháp chung"). Phần định hướng viết luôn vào `phanTich`.
3. **+`ghiNhoGop(ghiNhoArr, saiLamArr)`** — render GỘP: điều cần nhớ + dòng ✗→✓ (cần tránh) dưới **MỘT nhãn "Ghi nhớ:"**; bỏ nhãn "Sai lầm thường gặp" riêng. Guard **≤ 3 DÒNG** cả khối.
4. Guard khung A.1 cập nhật thông báo (vẫn yêu cầu đủ `saiLamArr` + `ghiNhoArr` — cả hai nuôi khối Ghi nhớ).

**Tương thích:** `saiLamThuongGap()` / `ghiNhoNhanh()` / `phuongPhapGiai()` GIỮ nguyên (dùng ngoài khối Dạng: `ghiNhoNhanh` cho Ghi nhớ mục ②). Bài cũ truyền `phuongPhapArr` sẽ bị BỎ QUA (không render) — đúng chủ trương retrofit chỉ áp bài mới.

**Đã test:** dựng 2 Dạng mẫu (một `phanTich` chuỗi, một `{doan:[...]}`), render Word + XSD PASS; guard ≤3 chặn đúng.

**Đồng bộ tài liệu (Project Knowledge):** HP V11.9 · CHUAN_TRINH_BAY · PhuLuc Đại số v1.5 · Instructions · Quy_Trinh_QC.

**RIÊNG của Hình (Phụ lục Hình + Instructions Hình): CHƯA đụng** — máy Hình nghỉ. Khi Hình chạy lại phải đổi cùng A.1 mới cho khớp CHUNG.
