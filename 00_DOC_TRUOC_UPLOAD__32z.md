# ĐỌC TRƯỚC KHI UPLOAD — [32z] BẢNG BIẾN THIÊN (DS12_CH01)

## Việc của Thầy (3 file, kéo-thả web GitHub → Commit changes)
1. **hinh_ds12_giaitich.py** — file MỚI, thêm vào gốc repo.
2. **BAN_TRICH_HAM_DS12_CH01__giaitich.md** — file MỚI, thêm vào gốc repo.
3. **00_KHO_VERSION.txt** — ĐÈ bản cũ (đã prepend block [32z], giữ nguyên toàn bộ lịch sử bên dưới).

## An toàn
- Module ĐỘC LẬP, chỉ `import hinh_core` → KHÔNG đụng builder nào đang chạy (kể cả nhánh Hình hh12 vừa push [32x]/[32y]).
- Đã kiểm REGRESSION tại máy OB: import toàn bộ module chính OK + render lại builder cũ (parabol) nguyên vẹn.
- Dựng trên HEAD [32y] SHA `3e92eaf` (clone tươi ngay trước khi dựng) — đúng kỷ luật "một máy sửa / clone HEAD làm nền".

## Sau khi push
- HEAD ra mốc [32z]. OB/AI Soạn bụng kho sẽ có `bang_bien_thien`.
- Mốc kho yêu cầu của DS12_CH01 (ghi trong Phụ lục/Instructions) = **2026-10-16 / [32z]** — sẽ cập nhật khi mở pilot.
