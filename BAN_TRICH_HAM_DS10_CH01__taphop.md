# BẢN TRÍCH HÀM VẼ — DS10_CH01 — tự sinh từ `hinh_tap_hop.py` (module one-shot)

> **Cho AI Soạn.** Module BIỂU ĐỒ/MÔ HÌNH (thống kê & xác suất): mỗi hàm nhận DỮ LIỆU THẬT → trả PNG. Không theo lối builder `h.ve()` của hình học.
> Tự sinh bằng introspect `hinh_tap_hop.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 30/09/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_tap_hop as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.bieu_do_cot(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM BIỂU ĐỒ / MÔ HÌNH — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `bieu_do_ven(kieu='cat', nhan=None, phan_tu=None, to=None, bao=None, out='ven', tra_bytes=False, chuThich=None)` | BIỂU ĐỒ VEN minh hoạ tập hợp & phép toán (giấu toạ độ, Đ5.9). kieu : • 'don' — 1 vòng. nhan={'S':..} phan_tu={'S':'1, 2, 3'} • 'cat' — 2 vòng cắt nhau. nhan={'S':..,'T':..} phan_tu={'rieng_S':'7','chung':'2, 4','rieng_T':'-1, 6'} • 'roi' — 2 vòng rời nhau. nhan={'S':..,'T':..} phan_tu={'S':..,'T':..} • 'long' — vòng lồng (tập con). nhan={'ngoai':'S','trong':'T'} hoặc nhan={'chuoi':['R','Q','Z','N']} (ngoài→trong, minh hoạ N⊂Z⊂Q⊂R) • 'ba' — 3 vòng cắt nhau. nhan={'A':..,'B':..,'C':..} to (tô miền, chỉ 'cat' & 'long'): • 'cat' : 'giao' | 'hop' | 'hieu_ST' (S\T) | 'hieu_TS' (T\S) • 'long': 'phan_bu' (phần ngoài \ trong) bao : nhãn tập bao/không gian (khung chữ nhật ngoài) — vd 'X' hoặc r'\mathbb{R}'. chuThich : caption "Hình N" căn giữa dưới. |
| `truc_so_tap_hop(cac_khoang, out='truc_tap', tra_bytes=False, chuThich=None)` | TRỤC SỐ biểu diễn tập con của R: khoảng/đoạn/nửa khoảng/tia (giấu toạ độ vẽ). cac_khoang : list các dict, mỗi khoảng: {'tu':<số|None>, 'den':<số|None>, # None = ∓∞ 'kin_tu':bool, 'kin_den':bool, # True → ngoặc vuông [ ]; False → ( ) 'nhan':'[1;3]', 'to':True} # nhan: nhãn dưới trục (tuỳ); to: có tô? • 1 khoảng → 1 trục số. • nhiều → XẾP TẦNG (trên xuống) minh hoạ giao/hợp; trục dùng THANG ĐO CHUNG. Tự tính khoảng số nguyên hiển thị từ mọi mút hữu hạn. |

---

**Thống kê:** 2 hàm biểu đồ/mô hình (one-shot, phơi cho AI Soạn).
