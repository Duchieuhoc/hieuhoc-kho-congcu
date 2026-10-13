<!-- Bản trích hàm kho Oxyz (A↔C) cho AI Soạn — mốc [32x]. Code CHỈ gọi hàm có ở đây. -->
# BẢN TRÍCH HÀM — `hinh_hh12_oxyz` (HỆ TRỤC Oxyz lớp 12)
## Mạch Hình học 12, Chương II, Bài 7–8 · mốc kho **≥ [32x]** · OB dựng 2026-10-13
> A↔C khép: **code CHỈ gọi hàm liệt kê ở đây**; thiếu hàm → DỪNG-báo-OB, KHÔNG chế hàm / tự tính toạ độ màn hình / gõ tay ký hiệu (Đ5.9, Đ34).
> Import: `import hinh_hh12_oxyz as H12OX` → `h = H12OX.HinhOxyz()` → khai nghĩa → `png = h.ve(out=..., tra_bytes=True, nhan='Hình N. …')`.
> **Đ5.9 (Oxyz):** toạ độ (x;y;z) truyền vào là **dữ liệu ĐỀ BÀI** (lấy nguyên từ nguồn); máy lo phép chiếu. KHÔNG tự chế toạ độ hình học.

## KHỞI TẠO
- `HinhOxyz(scale=1.0, goc=(0,0))` — lớp hình Oxyz. `goc` = vị trí gốc O trên hệ vẽ (đặt nhiều hình 1 khung).

## HỆ TRỤC NỀN
- `he_truc(dai_x=3.2, dai_y=4.2, dai_z=4.2, mp_toado=False, vecto_dv=True, O='O', ten_truc=('x','y','z'))`
  — 3 trục Ox/Oy/Oz (mũi tên + nhãn) + vectơ đơn vị i,j,k. `mp_toado=True` tô 3 mặt phẳng toạ độ (H.2.35). `vecto_dv=False` ẩn i,j,k.
  **Gọi TRƯỚC** các hàm đặt điểm/khối (để có gốc O).

## ĐIỂM THEO TOẠ ĐỘ
- `diem(ten, x, y, z, nhan='above right', mau=None, moc=True, hop_chieu=False, net_hop='dut', vecto_OM=False, O='O')`
  — đặt điểm M(x;y;z); `hop_chieu=True` vẽ hình hộp chữ nhật chiếu O→M (đọc toạ độ, H.2.37/38); `vecto_OM=True` vẽ $\overrightarrow{OM}$.
- `nhan_toado(ten, x, y, z, nhan='above right', mau=None, moc=True)` — đặt + chấm đỉnh theo toạ độ (khối 'thả' H.2.42).

## LƯỚI
- `luoi_mp(nx, ny, nz=0, mau='black!18')` — lưới ô vuông đơn vị trên sàn (Oxy), nx×ny ô, để đọc toạ độ (H.2.38/39).

## KHỐI
- `khoi_hop_oxyz(a, b, c, goc=(0,0,0), ten_dinh=None, nhan=None, net_khuat='dut', hien_dinh=True)`
  — HỘP CHỮ NHẬT cạnh ∥ 3 trục; `a,b,c` kích thước theo Ox,Oy,Oz; `goc` toạ độ đỉnh gốc; `ten_dinh`=8 tên theo thứ tự [đáy: gốc,+x,+x+y,+y ; nắp: +z,+x+z,+x+y+z,+y+z]. Nét khuất tự tính (H.2.40/45/51; lập phương = a=b=c).
- `khoi_tu_dinh(dinh, canh, mat=None, to_mat=None, net_khuat='dut', hien_dinh=True, mau_dinh=None)`
  — KHỐI TỔNG QUÁT (chóp/lăng trụ/khối thả). `dinh`=dict{tên:(x,y,z)} toạ độ đề; `canh`=list[(u,v)]; **`mat`=list các mặt** (để tính nét khuất che theo mặt — NÊN khai đủ mặt khối đặc); `to_mat`=mặt cần tô. `hien_dinh=False` → chỉ vẽ cạnh (không chấm/nhãn tên), dùng khi tự ghi nhãn toạ độ. Nét khuất chuẩn (H.2.42/47b/48).

## VECTƠ & NỐI (kế thừa base)
- `h.vecto('A','B', nhan=r'\overrightarrow{AB}', mau=, net=)` — vectơ (mũi tên A→B).
- `h.doan_oxyz('A','B', net='lien'|'dut', mau=)` hoặc `h.doan('A','B', net=)` — nối 2 điểm đã đặt.
- `h.trung_diem`, `h.diem_giua`, `h.ghi_chu(x,y,chữ)`, `h._P(x,y,z)` (toạ độ màn hình để tự đặt nhãn) — base, chạy trên đỉnh đã chiếu (affine).

## CỬA RENDER
- `h.ve(out='hinh', tra_bytes=True, nhan='Hình N. …')` — render → PNG bytes (nhúng docx). Gọi CUỐI.

---
### GHI CHÚ DỰNG
- Phép chiếu xiên: Oz đứng-lên · Oy ngang-phải · Ox chếch xuống-trái (chiều sâu, `_K_SAU=0.62`, `_GOC_OX=218°`). Affine ⇒ trung điểm/trọng tâm/giao chiếu chính xác.
- Nét khuất: `khoi_hop_oxyz` tự đủ; `khoi_tu_dinh` cần `mat` để che chuẩn (thiếu mat → lùi heuristic bao lồi, chỉ hợp khối lồi đơn giản).
- Hướng hình (đỉnh nào ra trước/sau) do TOẠ ĐỘ quyết; muốn 1 cạnh nổi (vd đường cao SA) hiện liền → chọn gốc/hướng toạ độ cho đỉnh đó ra TRƯỚC (x lớn). Khai nghĩa nêu rõ.
- Nhãn toạ độ đỉnh (khối thả H2.42): dựng `khoi_tu_dinh(..., hien_dinh=False)` rồi lặp đặt chấm `_diem` + `ghi_chu(h._P(x,y,z) + lệch, f"${nm}({x};{y};{z})$")`.
