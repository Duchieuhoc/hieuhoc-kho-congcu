# ĐỌC TRƯỚC KHI UPLOAD — [33a] ĐỒ THỊ KHẢO SÁT HÀM SỐ (DS12_CH01, Bài 4)

## Việc của Thầy (3 file, kéo-thả web GitHub → Commit changes)
1. **hinh_ds12_giaitich.py** — ĐÈ bản [32z] (đã THÊM hàm `do_thi_khao_sat`; `bang_bien_thien` nguyên vẹn bên trên).
2. **BAN_TRICH_HAM_DS12_CH01__giaitich.md** — ĐÈ bản cũ (tự sinh lại, nay 2 hàm).
3. **00_KHO_VERSION.txt** — ĐÈ bản cũ (đã prepend block [33a], giữ nguyên lịch sử bên dưới).

## An toàn
- CHỈ thêm 1 hàm vào module ĐỘC LẬP (chỉ `import hinh_core`) → KHÔNG đụng builder nào đang chạy.
- REGRESSION tại máy OB: import `hinh_ds12_giaitich` sạch + `bang_bien_thien` render nguyên. (Lỗi `hinh_phang._o_vuong` nếu gặp là tiền-tồn nhánh Hình, không do gói này.)
- Dựng trên HEAD [32z] SHA `27d466e` (clone tươi ngay trước khi dựng) — đúng kỷ luật "một máy sửa / clone HEAD làm nền".

## do_thi_khao_sat phủ 3 dạng Bài 4
- Hàm bậc ba (1 nhánh liền) · phân thức b1/b1 (2 nhánh hyperbol + TCN) · phân thức b2/b1 (TCĐ + TCX).
- Máy TỰ plot mượt (cắt sạch tại TCĐ, không đường dọc giả) + vẽ tiệm cận nét đứt + chấm/nhãn điểm đặc biệt. Đ5.9.
- NGHIỆM THU 5 ca khớp SGK: H1.28 · H1.29 · H1.30 · H1.31 · H1.32.

## Sau khi push
- HEAD ra mốc [33a]. OB/AI Soạn bụng kho sẽ có ĐỦ 2 builder đường găng ⇒ **mở khóa pilot B01**.
