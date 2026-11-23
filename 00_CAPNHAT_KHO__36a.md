# CẬP NHẬT KHO — mốc [36a] · hinh_hoa_ch06.py (HÓA 9 · Chương VI)
### OB Hóa THCS · 2026-11-23 · ĐỀ XUẤT (thầy upload GitHub để kho một-nguồn)

## 1. Vì sao có bản này
Khối Hóa lớp 9 Chương VI (Kim loại) là khối MỚI. Khi dựng bài đầu
`HOA9_CH06_B18` (Tính chất chung của kim loại), AI Soạn phát hiện **kho
chưa có họ hàm vẽ DỤNG CỤ THÍ NGHIỆM**: category "Hoá học" cũ chỉ 8 hàm
cấu tạo nguyên tử/phân tử (`hinh_hoa_ch01/ch02` — Bohr, quả cầu-que,
liên kết ion/CHT, lớp 7–8). Không có bình khí, muỗng đốt, dây lò xo,
mạch điện, thìa dẫn nhiệt.

Mà **mục ② Hóa bắt buộc có hình cho phần thí nghiệm** (Phụ lục Hóa mục 3 ·
HP Đ22.5) và CẤM placeholder/mô tả chữ (Đ42). Theo Đ5.9 AI Soạn không tự
chế hàm vẽ → dừng, báo Giám đốc. Giám đốc uỷ quyền (23/11) cho dựng module
ngay trong phiên; OB thẩm định rồi áp kho.

## 2. Thêm gì (ADDITIVE — 0 đổi hàm cũ)
`hinh_hoa_ch06.py` — module một-phát (như `hinh_hoa_ch02`), render
TikZ/pdflatex qua `hinh_core.render_tikz_doc`. **4 hàm phơi cho AI Soạn:**

| Hàm | Dùng |
|---|---|
| `thi_nghiem_binh_khi(mau_khi, kieu_gia, nhan_khi, nhan_mau, nhan_sp, mau_sp)` | Engine: kim loại cháy trong bình khí (tác dụng phi kim). |
| `phan_ung_phi_kim(ten)` | Registry nhanh 3 TN chuẩn B18: `Fe_O2` · `Na_Cl2` · `Fe_Cl2`. |
| `mach_thu_dan_dien()` | Mạch thử tính dẫn điện (SBT 18.10) — không lộ đáp án (Đ41.4). |
| `thi_nghiem_dan_nhiet()` | Hai bát nóng/đá cắm 4 thìa (SBT 18.11) — không lộ đáp án. |

Đặc thù giữ đúng luật: NGHĨA-THUẦN + PHANH (tên/kiểu giá sai → raise);
text trong hình chỉ ASCII/ký hiệu hoá (O_2, Cl_2, Na, Fe, Fe_3O_4…),
chú thích tiếng Việt đặt ở Word.

## 3. File đi kèm (regen tự động)
- `BAN_TRICH_HAM_HOA9_CH06.md` — tự sinh bằng `sinh_bantrich.py hinh_hoa_ch06 HOA9_CH06`.
- `00_MUC_LUC_HAM.md` — regen bằng `sinh_mucluc.py` (nay 182 hàm Python).
- `00_KHO_VERSION.txt` — thêm mốc [36a] ở đầu log.

## 4. KHÔNG đụng
`hieuhoc_template.js` · `hinh_core.py` · mọi kho chương khác · mọi chữ ký
hàm cũ. Không regen API_REFERENCE (template không đổi).

## 5. Nghiệm thu
- `import hinh_hoa_ch06` OK sau `npm/pip` kho hiện hành.
- Render 5/5 hình sạch (Fe_O2 · Na_Cl2 · Fe_Cl2 · mạch điện · thìa nhiệt).
- Dựng `HOA9_CH06_B18` bản GV: xuất qua `kiemMay` **SẠCH** (0 lỗi);
  4 hình = 4 blip; 0 ký tự cấm; 0 "undefined"; mã `HOA9` đúng.

## 6. THẦY LÀM GÌ
1. Upload đè lên GitHub `Duchieuhoc/hieuhoc-kho-congcu` **4 file**:
   `hinh_hoa_ch06.py` · `BAN_TRICH_HAM_HOA9_CH06.md` ·
   `00_MUC_LUC_HAM.md` · `00_KHO_VERSION.txt` (+ kèm ghi chú này).
2. Đổi **"Mốc kho yêu cầu"** của khối Hóa 9 sang **[36a] / 2026-11-23**
   (Instructions AI Soạn Hóa + điền field ⚠️ trong gói GIAO nếu còn dùng).
3. Từ phiên sau, AI Soạn tự bụng kho là có đủ họ dụng cụ cho B18;
   B19–B21 (dãy hoạt động · tách kim loại/hợp kim · phi kim vs kim loại)
   dùng apparatus KHÁC → khi tới lượt sẽ bổ tiếp (báo riêng).
