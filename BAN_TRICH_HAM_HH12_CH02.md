# BẢN TRÍCH HÀM — HH12_CH02 (alias `H12`)
## Hình không gian tổng hợp lớp 12 (Vectơ trong KG). Mốc kho ≥ [32w]. `import hinh_hh12_ch02 as H12` → `h = H12.HinhHH12CH02()`.
### A↔C: bài CHỈ gọi hàm trong bản trích này + base/khoihop. Thiếu hàm → DỪNG-báo-OB [QUYẾT], KHÔNG chế hàm/tự tính toạ độ (Đ5.9, PHANH).

## KHỐI NỀN (mới [32w])
| Hàm | Nghĩa | Ghi chú |
|---|---|---|
| `h.tu_dien(nhan='ABCD', dinh_tren=None, canh=3.0)` | Tứ diện: ký tự ĐẦU = apex, 3 sau = đáy. Cạnh đáy sau nét ĐỨT (khuất). | Góc nhìn do kho chốt. `dinh_tren` đổi apex. |
| `h.chop(day, dinh='S', cao=2.6, ten_day=['A','B','C','D'])` | Chóp đáy đa giác + apex trên tâm. Nét khuất tự tính. | `day`={'loai':'chu_nhat','a':_,'b':_} / 'tam_giac'{a,b,c} / 'binh_hanh'{canh_day,canh_ben,goc} / 'da_giac'{diem}. |
| `h.trong_tam(ten, *dinh)` | Đặt trọng tâm các đỉnh (trung bình). | Vd `h.trong_tam('G','B','C','D')`. |

## KHỐI KẾ THỪA (hinh_khoihop — KHÔNG vá thêm)
| Hàm | Nghĩa |
|---|---|
| `h.lang_tru_dung(day, cao, huong='ngang'/'dung', ten_dinh=['A','B','C'])` | Lăng trụ đứng đáy đa giác (nét khuất tự tính). **HỘP/LẬP PHƯƠNG**: day={'loai':'chu_nhat','a':_,'b':_}, huong='dung', ten_dinh=['A','B','C','D'] → ABCD.A'B'C'D'. |
| `h.khoi_hop_chu_nhat(dai,rong,cao,nhan={...})` | Khối hộp dạng kích-thước (đỉnh ẩn) — dùng khi KHÔNG cần nhãn đỉnh. |

## LỚP NGHĨA TRÊN KHỐI (base hinh_coban — chiếu affine nên chạy thẳng trên đỉnh 3D đã đặt)
| Hàm | Nghĩa |
|---|---|
| `h.vecto(A, B, nhan=r'\overrightarrow{AB}', mau=, net=, vi_tri_nhan=, rong='dam')` | VECTƠ-3D: mũi tên giữa 2 đỉnh đã đặt. |
| `h.trung_diem(M, A, B)` | Trung điểm cạnh (tự đặt M + gạch bằng 2 nửa). |
| `h.diem_giua(ten, A, B, ti_le=0.5, nhan=)` | Điểm chia đoạn theo tỉ lệ (vd I: AI=3IG → ti_le=0.75 từ A tới G). |
| `h.giao(ten, dt1, dt2)` | Giao 2 đường/đoạn (vd O = giao AB' và A'B). |
| `h.doan(A, B, net='lien'/'dut', mau=)` | Nối đoạn (đường phụ lời giải: mau='red', net='dut'). |
| `h.ghi_chu(x, y, chu)` · `h.so_do_goc(...)` · `h.to_mien(...)` | Ghi chú / cung góc / tô miền. |

## RENDER
`png = h.ve(out='tenfile', tra_bytes=True, nhan='Hình N. ...')` → PNG bytes (nhúng docx qua template).

## NGHIỆM THU [32w] (render-verify soi mắt, 2026-10-12)
tứ diện ABCD+vectơ · chóp S.ABCD đáy vuông (nét khuất SD+cạnh sau đúng) · tứ diện+trọng tâm G+I(AI=3IG) · lăng trụ tam giác+trung điểm+vectơ AA'/MM' · hộp+chéo KG AC'. Nét khuất đúng.
