# CAPNHAT_KHO [33zg] — +1 builder đọc đồ thị (H9.10) cho ONTAP CH09
Chiều A: Ông Bụt → Giám đốc (upload đè GitHub kho). 2026-10-31. DỰNG TRÊN HEAD [33zf].

VIỆC GIÁM ĐỐC: upload đè 3 file này vào repo github.com/Duchieuhoc/hieuhoc-kho-congcu:
  • hinh_ds11_giaitich.py            (+ hàm doc_ba_do_thi — ADDITIVE, 7 hàm)
  • 00_KHO_VERSION.txt               (thêm block [33zg] ở đầu)
  • BAN_TRICH_HAM_DS11_CH05__giaitich.md  (tái sinh, 10 hàm)

NỘI DUNG:
  • doc_ba_do_thi (H9.10, SGK 9.32) — 3 đồ thị vị trí/vận tốc/gia tốc trên 1 hệ Oty.
    MÁY TỰ TÍNH (Đ5.9): vận tốc bướu v=t²(6-t)²; vị trí=nguyên hàm (chữ S); gia tốc=v' (lên rồi lao xuống).
    Nhãn TRUNG TÍNH a/b/c — KHÔNG lộ đáp (Đ41.4).
  • ADDITIVE: 0 đụng 6 hàm trước; regression 6 builder PASS. template.js vẫn [33za] (không đổi).
  • Render-verify ĐẠT (soi mắt: a lên-xuống cắt 0 tại đỉnh b; b bướu; c chữ S bão hòa — đúng quan hệ đạo hàm).

SAU KHI PUSH: điền SHA mới vào HOSO ONTAP (pin). GATE phiên sau: AI Soạn bụng [33zg].
