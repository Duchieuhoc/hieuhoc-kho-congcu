<!-- Bản trích hàm kho CH05 (A↔C) cho AI Soạn — mốc [33c]. Code CHỈ gọi hàm có ở đây. -->
# BẢN TRÍCH HÀM — `hinh_hh12_ch05` (ĐỐI TƯỢNG GIẢI TÍCH Oxyz lớp 12)
## Mạch Hình học 12, Chương V (PP toạ độ không gian) · mốc kho **≥ [33c]** · OB dựng 2026-10-14
> A↔C khép: **code CHỈ gọi hàm liệt kê ở đây**; thiếu hàm → DỪNG-báo-OB, KHÔNG chế hàm / tự tính toạ độ màn hình / gõ tay ký hiệu (Đ5.9, Đ34).
> Import: `import hinh_hh12_ch05 as C5` → `h = C5.HinhCh05()` → khai nghĩa → `png = h.ve(out=..., tra_bytes=True, nhan='Hình N. …')`.
> **Nối tiếp [32y]:** `HinhCh05(HinhOxyz)` kế thừa TRỌN hàm Oxyz (`he_truc`, `diem`, `luoi_mp`, `khoi_hop_oxyz`, `khoi_tu_dinh`, `nhan_toado`, `vecto`, `doan_oxyz`, `ve`) — xem `BAN_TRICH_HAM_HH12_OXYZ`. File này chỉ thêm 6 hàm đối-tượng-giải-tích.
> **Đ5.9 hai chế độ:** *coordinate-tied* (mặt cầu · đoạn chắn · đt cho toạ độ) → truyền toạ-độ-toán từ ĐỀ, máy chiếu. *schematic* (mp α tổng quát · cặp VTCP · 2 đt minh hoạ) → kho đặt phối cảnh canonical; OB khai PHẦN TỬ + QUAN HỆ, KHÔNG cấp toạ độ.

## KHỞI TẠO
- `HinhCh05(scale=1.0, goc=(0,0))` — kế thừa `HinhOxyz`. Hình coordinate-tied gọi `he_truc(...)` TRƯỚC.

## (a) MẶT PHẲNG — schematic
- `mat_phang(nhan=r'(\alpha)', vtpt=False, nhan_n=r'\vec n', cap_vtcp=False, nhan_uv=(r'\vec u',r'\vec v'), diem_ngoai=False, mau='blue!9', pos=(0,0), rw=1.75, rd=1.15)`
  — hình bình hành phối cảnh biểu diễn 1 mặt phẳng (nền z=0). `vtpt=True` → VTPT hướng lên + dấu góc vuông (H5.2). `cap_vtcp=True` → cặp VTCP $\vec u,\vec v$ trong mp (H5.5). `diem_ngoai=True` → điểm M ngoài + chân N + đoạn d=MN (H5.13/§khoảng cách). `pos` dời tâm để đặt nhiều mp. **Schematic — KHÔNG truyền toạ độ.**

## (a′) HAI MẶT PHẲNG — quan hệ, schematic
- `hai_mat_phang(quan_he='cat', nhan=(r'(P)',r'(Q)'), vtpt=True)`
  — `quan_he`: `'song_song'` (2 bình hành chồng + VTPT cùng hướng — H5.11) · `'vuong_goc'` (mp ngang + mp đứng + dấu góc vuông — H5.9) · `'cat'` (2 bình hành cắt theo giao tuyến + VTPT $\vec n,\vec{n'}$ — H5.36).

## (b) MẶT CẦU — coordinate-tied
- `mat_cau(tam=(0,0,0), R=1.3, nhan=r'(S)', tam_ten='I', ban_kinh=True, diem=None, duong_kinh=None, rb_ti=0.34)`
  — mặt cầu tâm $I$(=`tam`, toạ độ đề) bán kính $R$: viền = đường tròn (quy ước SGK) + xích đạo ellipse (nửa sau nét đứt) + tâm $I$. `diem=('M',x,y,z)` → điểm trên/ngoài mặt + bán kính $R$ tới $M$ (H5.41). `duong_kinh=(('A',xa,ya,za),('B',xb,yb,zb))`. `rb_ti` tỉ lệ bán trục phụ xích đạo. **Gọi `he_truc` trước** (nếu muốn hiện trục).

## (d) MẶT PHẲNG THEO ĐOẠN CHẮN — coordinate-tied
- `mat_phang_doan_chan(a, b, c, nhan=r'(\alpha)', to=True, ten=('A','B','C'))`
  — mp cắt 3 trục tại $A(a;0;0), B(0;b;0), C(0;0;c)$ (a,b,c>0, toạ độ đề) → tam giác vết + tô nhạt (H5.8). **Gọi `he_truc` TRƯỚC.**

## (c) ĐƯỜNG THẲNG — schematic / coordinate-tied
- `duong_thang(qua=None, vtcp=None, ten=r'\Delta', nhan_u=r'\vec u', pos=(0,0), huong=(2.6,1.3))`
  — đoạn đường thẳng + VTCP (mũi tên đỏ). Truyền `qua=(x,y,z)+vtcp=(a,b,c)` → coordinate-tied (cần `he_truc`); để None → schematic theo `huong` (H5.23).

## (c′) HAI ĐƯỜNG THẲNG — quan hệ, schematic
- `hai_duong_thang(quan_he='cheo', ten=(r'\Delta_1',r'\Delta_2'), vtcp=True)`
  — `'cat'` · `'song_song'` · `'cheo'` (đoạn giữa đt sau = NÉT ĐỨT, biểu thị đi sau — H5.29) · `'vuong_goc'`. VTCP $\vec{u_1}$ (đỏ), $\vec{u_2}$ (xanh).

## CỬA RENDER
- `h.ve(out='hinh', tra_bytes=True, nhan='Hình N. …')` — render TikZ→PNG bytes. Gọi CUỐI.

---
### GHI CHÚ DỰNG
- Phép chiếu + nét khuất kế thừa [32y] (Oz↑/Oy→/Ox 218°, K_sâu 0,62). Mặt cầu vẽ viền TRÒN (chuẩn SGK) + xích đạo ellipse ngang; đt chéo vẽ đoạn giao sau nét đứt.
- **Tinh chỉnh VỊ TRÍ NHÃN theo từng hình** ở khâu khai nghĩa (pos/nhan_* ) — primitive đặt nhãn mặc định, có thể chồng nhẹ ở vài bố cục; khai nghĩa dịch nhãn cho sạch.
- Hình ĐỀ = CHỈ dữ kiện (Đ35): số cần tìm ẩn/`?`; hình lời giải chỉ vẽ khi khác hình đề (Đ36.1).
- Mảng còn chờ (lớp 11 không gian tổng hợp quan hệ đường–mặt) KHÔNG thuộc module này.
