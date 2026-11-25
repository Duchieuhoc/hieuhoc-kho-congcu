# BẢN TRÍCH HÀM VẼ — HOA9_CH06 — tự sinh từ `hinh_hoa_ch06.py` (module one-shot)

> **Cho AI Soạn.** Module HÀM MỘT-PHÁT: mỗi hàm nhận DỮ LIỆU/KÍCH THƯỚC THẬT → trả PNG (biểu đồ, mô hình, hoặc hình khối). Không theo lối builder `h.ve()`.
> Tự sinh bằng introspect `hinh_hoa_ch06.py` qua `sinh_bantrich.py` — KHÔNG sửa tay.
> Sinh ngày 23/11/2026. AI Soạn khai nghĩa theo phiếu → GỌI HÀM → nhúng qua `H.hinhVe`.

Import trong script bài: `import hinh_hoa_ch06 as BD`.
Gọi hàm với `tra_bytes=True` để lấy PNG buffer: `buf = BD.be_dien_phan_nhom(...); H.hinhVe({ imageBuffer: buf })`.

---

## HÀM — AI Soạn GỌI theo phiếu

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `be_dien_phan_nhom(out='hoa6_dienphan', tra_bytes=False)` | Sơ đồ bể điện phân aluminium oxide nóng chảy (gốc Hình 20.1). Callout 1–5; chú giải xem be_dien_phan_nhom.CHU_GIAI / CHU_GIAI_DIEN_PHAN. |
| `cot_loc_than(out='hoa6_cotthan', tra_bytes=False)` | Thí nghiệm hấp phụ của bột than gỗ (gốc Hình 21.1). Callout 1–5; chú giải CHU_GIAI_COT_THAN. |
| `lo_cao_luyen_gang(out='hoa6_locao', tra_bytes=False)` | Sơ đồ lò cao luyện gang (gốc Hình 20.2). Callout 1–7; chú giải CHU_GIAI_LO_CAO. |
| `lo_thoi_luyen_thep(out='hoa6_lothoi', tra_bytes=False)` | Sơ đồ lò thổi luyện thép (gốc Hình 20.3). Callout 1–2; chú giải CHU_GIAI_LO_THOI. |
| `mach_thu_dan_dien(out='hoa6_mach', tra_bytes=False)` | Mạch nối tiếp thử tính dẫn điện: pin -> công tắc -> bóng đèn -> hai kẹp vật liệu (vật cần thử kẹp giữa). CẤM lộ đáp án (Đ41.4): KHÔNG tô sáng/không-sáng. Nhãn ASCII: '1,5V', 'K', vật thử để trống. |
| `ong_nghiem_phan_ung(mau_dd, vat, nhan_vat=None, nhan_dd=None, bot=False, bam=None, out='hoa6_ong', tra_bytes=False)` | Kim loại phản ứng trong ỐNG NGHIỆM (thí nghiệm dãy hoạt động hoá học). mau_dd : màu dung dịch ('ddhcl' | 'ddxanh' | …). vat : 'dinh' (đinh sắt) | 'loxo' (dây kim loại uốn lò xo). nhan_vat / nhan_dd : ký hiệu hoá học ASCII (vd 'Fe','Cu' | 'HCl','AgNO_3'). bot : True → vẽ bọt khí quanh vật (kim loại đẩy H2). bam : màu lớp kim loại mới bám trên vật (vd 'bacxam' cho Ag bám lên Cu); None nếu không. PHANH: vat ∈ {dinh,loxo}. |
| `phan_ung_phi_kim(ten, out=None, tra_bytes=False)` | Gọi NHANH 1 trong 3 sơ đồ thí nghiệm chuẩn của B18 theo TÊN: 'Fe_O2' (sắt cháy trong oxygen) · 'Na_Cl2' (natri + chlorine) · 'Fe_Cl2' (sắt + chlorine). PHANH: tên phải có trong registry. |
| `thi_nghiem_binh_khi(mau_khi, kieu_gia, nhan_khi=None, nhan_mau=None, nhan_sp=None, mau_sp=None, out='hoa6_binhkhi', tra_bytes=False)` | Kim loại cháy trong BÌNH KHÍ (sơ đồ thí nghiệm tác dụng với phi kim). mau_khi : màu nền khí trong bình ('o2gas' | 'clgas' | …). kieu_gia: 'loxo' (dây kim loại uốn lò xo) | 'muong' (muỗng đốt chứa mẫu). nhan_mau: ký hiệu mẫu kim loại trên giá (vd 'Fe', 'Na') — ASCII/math. nhan_khi: ký hiệu khí trong bình (vd 'O_2', 'Cl_2'). nhan_sp / mau_sp: ký hiệu + màu sản phẩm đọng đáy bình (vd 'Fe_3O_4','feoxide'). PHANH: kieu_gia ∈ {loxo,muong}. |
| `thi_nghiem_dan_nhiet(out='hoa6_nhiet', tra_bytes=False)` | Hai bát: 'HOT' (nước nóng ~90C) và 'ICE' (nước đá); mỗi bát cắm 4 thìa (kim loại / nhựa / gỗ / sứ). CẤM lộ đáp án (Đ41.4): không đánh dấu thìa nào nóng nhanh. Nhãn thìa ASCII: KL, Nh, Go, Su. |
| `thi_nghiem_day_hoat_dong(ten, out=None, tra_bytes=False)` | Gọi NHANH thí nghiệm dãy hoạt động hoá học B19 theo TÊN: 'Fe_HCl' (đinh sắt + dd HCl, sủi bọt) · 'Cu_AgNO3' (dây đồng lò xo + dd AgNO3, bạc xám bám, dd hoá xanh). PHANH: tên phải có trong registry. |

---

**Thống kê:** 10 hàm một-phát (phơi cho AI Soạn).
