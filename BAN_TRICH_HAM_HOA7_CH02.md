# BẢN TRÍCH HÀM VẼ — `HOA7_CH02` (module `hinh_hoa_ch02`)
### Thư viện hình Chương II Hóa 7 — Phân tử · Liên kết · mốc kho 29f
<!-- Tự sinh từ hinh_hoa_ch02.py bằng inspect. A↔C khép: AI Soạn CHỈ gọi hàm dưới đây. -->
<!-- Module hàm-độc-lập (render trực tiếp) → KHÔNG có .ve(); sinh bằng inspect thay sinh_bantrich (class-only, hiện dựng khuôn khai-nghĩa rỗng cho module này). -->

**Gọi:** `import hinh_hoa_ch02 as H2` → `H2.<hàm>(..., tra_bytes=True)` trả **PNG buffer** cho `hinhVe`/`hinhBenPhai`.
**Text trong hình chỉ ASCII/ký hiệu** (Na, Cl, +11, 1e, →, Na^+…) — chú thích tiếng Việt đặt ở Word, KHÔNG nhồi vào hình (pdflatex không dựng dấu tiếng Việt).

| Chữ ký hàm | Vẽ gì (NGHĨA-THUẦN — máy tự bố trí, layout ẩn trong kho) |
|---|---|
| `phan_tu(cong_thuc, out, tra_bytes)` | Mô hình quả cầu-que của 1 phân tử (lớp 7): H2,Cl2,O2,N2,HCl,CO2,H2O,CH4,NH3. Quả cầu = nguyên tử (màu theo nguyên tố); que = liên kết (đơn/đôi/ba). NGHĨA-THUẦN. |
| `mo_hinh_hat(loai, nguyen_to=None, cong_thuc=None, ion_duong=None, ion_am=None, out, tra_bytes)` | Mô hình HẠT của một mẫu chất. loai: 'kim_loai' (nguyen_to): lưới quả cầu cùng màu xếp khít (vd Cu rắn); 'khi_don' (nguyen_to): các quả cầu đơn lẻ rời (khí hiếm, vd He); 'phan_tu' (cong_thuc): nhiều phân tử rời cùng loại (vd O2, CO2); 'mang_ion' (ion_duong,ion_am): mạng 2 màu xen kẽ (vd Na+ / Cl-). |
| `hop_hat(items, nhan=None, out, tra_bytes)` | Hộp chữ nhật chứa 'hạt' trừu tượng để phân loại đơn/hợp chất/hỗn hợp. items: list mô tả — mỗi phần tử là: ('don', mau) → 1 nguyên tử lẻ; ('cap', mau1, mau2) → 1 phân tử 2 nguyên tử (mau1==mau2: đơn chất; khác: hợp chất). Máy tự rải trong hộp. nhan: nhãn hộp (vd 'A'). |
| `lien_ket_ion(cho_Z, cho_ch, cho_ten, nhan_Z, nhan_ch, nhan_ten, so_e, ion_duong, ion_am, out, tra_bytes)` | Sơ đồ: nguyên tử KIM LOẠI (cho) nhường so_e electron cho nguyên tử PHI KIM (nhan) → ion dương + ion âm. Vẽ 2 nguyên tử Bohr + mũi tên chuyển e + kết quả ion. vd NaCl: (11,[2,8,1],'Na',17,[2,8,7],'Cl',1,'Na^+','Cl^-'). |
| `lien_ket_cht(cong_thuc, out, tra_bytes)` | Sơ đồ liên kết cộng hoá trị (dùng chung cặp electron): H2,Cl2,N2,O2,HCl,H2O. Mỗi nguyên tử = vòng tròn có ký hiệu; cặp electron DÙNG CHUNG = 2 chấm giữa 2 nguyên tử (mỗi liên kết có so_cap cặp); electron riêng = chấm quanh nguyên tử. NGHĨA-THUẦN. |

**Layout phân tử có sẵn** (`phan_tu`/`mo_hinh_hat loai=phan_tu`): H2, Cl2, O2, N2, HCl, CO2, H2O, CH4, NH3.
**Sơ đồ CHT có sẵn** (`lien_ket_cht`): H2, Cl2, N2, O2, HCl, H2O.
**PHANH:** layout/công thức phải có trong registry; `lien_ket_ion` kiểm sum(cấu hình)=Z. Sai → raise (DỪNG).

*Tự sinh: 5 hàm · module hinh_hoa_ch02 · mốc kho 29f (2026-09-16).*
