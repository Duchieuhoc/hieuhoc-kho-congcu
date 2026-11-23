# BẢN TRÍCH HÀM VẼ — HOA9_CH06 — tự sinh từ `hinh_hoa_ch06.py` (module one-shot)

> **Cho AI Soạn.** Module HÀM MỘT-PHÁT: mỗi hàm nhận DỮ LIỆU/KÍCH THƯỚC THẬT → trả PNG (biểu đồ, mô hình, hoặc hình khối). Không theo lối builder `h.ve()`.
> Tự sinh bằng introspect `hinh_hoa_ch06.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 23/11/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_hoa_ch06 as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.mach_thu_dan_dien(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `mach_thu_dan_dien(out='hoa6_mach', tra_bytes=False)` | Mạch nối tiếp thử tính dẫn điện: pin -> công tắc -> bóng đèn -> hai kẹp vật liệu (vật cần thử kẹp giữa). CẤM lộ đáp án (Đ41.4): KHÔNG tô sáng/không-sáng. Nhãn ASCII: '1,5V', 'K', vật thử để trống. |
| `phan_ung_phi_kim(ten, out=None, tra_bytes=False)` | Gọi NHANH 1 trong 3 sơ đồ thí nghiệm chuẩn của B18 theo TÊN: 'Fe_O2' (sắt cháy trong oxygen) · 'Na_Cl2' (natri + chlorine) · 'Fe_Cl2' (sắt + chlorine). PHANH: tên phải có trong registry. |
| `thi_nghiem_binh_khi(mau_khi, kieu_gia, nhan_khi=None, nhan_mau=None, nhan_sp=None, mau_sp=None, out='hoa6_binhkhi', tra_bytes=False)` | Kim loại cháy trong BÌNH KHÍ (sơ đồ thí nghiệm tác dụng với phi kim). mau_khi : màu nền khí trong bình ('o2gas' | 'clgas' | …). kieu_gia: 'loxo' (dây kim loại uốn lò xo) | 'muong' (muỗng đốt chứa mẫu). nhan_mau: ký hiệu mẫu kim loại trên giá (vd 'Fe', 'Na') — ASCII/math. nhan_khi: ký hiệu khí trong bình (vd 'O_2', 'Cl_2'). nhan_sp / mau_sp: ký hiệu + màu sản phẩm đọng đáy bình (vd 'Fe_3O_4','feoxide'). PHANH: kieu_gia ∈ {loxo,muong}. |
| `thi_nghiem_dan_nhiet(out='hoa6_nhiet', tra_bytes=False)` | Hai bát: 'HOT' (nước nóng ~90C) và 'ICE' (nước đá); mỗi bát cắm 4 thìa (kim loại / nhựa / gỗ / sứ). CẤM lộ đáp án (Đ41.4): không đánh dấu thìa nào nóng nhanh. Nhãn thìa ASCII: KL, Nh, Go, Su. |

---

**Thống kê:** 4 hàm một-phát (phơi cho AI Soạn).
