# UPLOAD KHO — Nhãn vạch trục dùng dấu PHẨY (33zl, mốc 2026-11-07)
> Thầy upload đè **2 file** lên repo **Duchieuhoc/hieuhoc-kho-congcu** (web → Upload → Commit). Cả 2 ở GỐC repo.
> Bản này clone từ HEAD mới nhất (đã có 33zk/33zj của máy DS8) rồi vá thêm → KHÔNG lệch pha, cứ đè.

## File cần upload (2)
1. `bieudo_xstk.py`      — VÁ: thêm `_ap_truc_phay()` + áp cho bieu_do_cot / bieu_do_cot_kep / bieu_do_doan_thang. **Tương thích ngược** (chỉ đổi hiển thị vạch trục, không đổi số liệu/chữ ký).
2. `00_KHO_VERSION.txt`  — thêm entry [33zl] ở đầu.

## Vì sao vá (phát hiện khi QC B41)
- Nhãn GIÁ TRỊ trên cột đã đúng dấu phẩy (15,6; −3; 26,5…) nhưng **NHÃN VẠCH TRỤC** để matplotlib mặc định → ra **dấu chấm** ("0.0", "2.5", "17.5") ở biểu đồ thập phân và thanh ngang. Sai chuẩn số thập phân VN.
- Nay vạch trục cũng dùng phẩy; số nguyên không đổi, phụ thêm "0.0"→"0" cho gọn.

## Sau khi upload
- Mốc kho **2026-11-07**. Các bài XS-TK từ **B42 trở đi** (và mọi biểu đồ thập phân/ngang về sau) tự động đúng.
- **B41 đã được OB dựng lại** bằng kho vá (bản trong LƯU_BÀI B41 đã sạch — vạch trục phẩy).
- **Nợ rà lại (không gấp):** B40 (DS6_CH09) + các bài DS8_CH05 có biểu đồ thập phân/ngang/đoạn thẳng — bản đã lưu còn vạch trục dấu chấm. Dựng lại khi tiện (nhãn giá trị đã đúng nên không chặn dùng). OB có thể rà khi thầy cho phép.
