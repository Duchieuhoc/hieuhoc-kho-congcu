# BẢN TRÍCH HÀM — ĐỒ THỊ GIẢI TÍCH THPT (hinh_ds11_giaitich.py) · kho [32b]
> import: `import hinh_ds11_giaitich as GT`. Render → PNG; build.js nhúng `H.hinhVe({ imageBuffer: buf })` (gọi hàm `tra_bytes=True`).
> Triết lý Đ5.9: hàm nhận NGHĨA (hệ số hàm / tọa độ), máy TỰ dựng đường cong (pgfplots) + TỰ tính chân đường cao — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
> Chương: DS11_CH05 (Giới hạn. Hàm số liên tục). Nghiệm thu pilot DS11_CH05_B16.

## do_thi_huu_ti(dang='doi_truc', a=1.0, b=2.0, c=1.0, k=1.0, xmin=None, xmax=None, ymin=None, ymax=None, nhan=None, hien_tc=True, out='dothi_ht', tra_bytes=False, scale=1.0)   ← [32b]
Đồ thị HÀM HỮU TỈ (pgfplots — đường cong sinh thẳng từ công thức; PHANH nội sinh: tiệm cận phải nằm trong khung). 2 nhánh tách qua tiệm cận đứng (không nối nét qua tiệm cận).
- **`dang='doi_truc'`** — $y = a + \dfrac{b}{x-c}$ (hyperbol dời trục). **TCĐ** $x=c$ (đứt dọc), **TCN** $y=a$ (đứt ngang). *(H5.4: `a=1,b=2,c=1`.)*
- **`dang='nghich_dao_binh'`** — $y = \dfrac{k}{(x-c)^2}$. $k>0$: hàm chữ "U", 2 nhánh trên $Ox$. **TCĐ** $x=c$, **TCN** $y=0$. *(H5.6: `k=1,c=0` → $y=1/x^2$.)*
- `xmin/xmax/ymin/ymax`: khung. None → tự chọn (doi_truc: $x\in[-8;8]$, $y\in[a-4;a+4]$; nghich_dao_binh: $x\in[-3.2;3.2]$, $y\in[-0.6;5]$). Chỉnh khi cần ôm trọn.
- `hien_tc`: vẽ tiệm cận đứt nét + nhãn `$x=c$`/`$y=a$`. **Tự BỎ nét trùng trục** khi `c=0` (TCĐ ≡ $Oy$) hoặc TCN `=0` (≡ $Ox$) — tránh vẽ đè trục.
- `nhan`: nhãn đường cong (None → tự sinh từ công thức). Truyền tường minh nếu muốn dạng khác.
- Trọng tài: SGK H5.4 ($y=1+\frac{2}{x-1}$), H5.6 ($y=1/x^2$). Dùng được cho mọi $y=a+\frac{b}{x-c}$ và $y=k/(x-c)^2$ khác (VD/BT giới hạn tại vô cực / vô cực tại một điểm).

## tam_giac_toa_do(a=2.0, ten_O='O', ten_A='A', ten_B='B', ten_H='H', nhan_h='h', hien_duong_cao=True, out='tamgiac_td', tra_bytes=False, scale=1.0)   ← [32b]
TAM GIÁC VUÔNG $OAB$ TRÊN HỆ $Oxy$ (H5.5). $O=(0;0)$, $A=(a;0)$ trên $Ox$, $B=(0;1)$ trên $Oy$; **vuông tại $O$** (ô vuông nhỏ, Đ41.1 — KHÔNG ghi 90°). Đường cao $OH$ hạ từ $O$ ⟂ $AB$, chân $H$ trên $AB$, nhãn độ dài $OH=h$.
- `a`: hoành độ điểm $A$ (số > 0). **Máy TỰ tính** $H=\left(\dfrac{a}{1+a^2};\dfrac{a^2}{1+a^2}\right)$ = chân đường vuông góc; **PHANH** kiểm $H\in AB$ và $OH\perp AB$ trước khi vẽ. *(Độ dài nét là HIỂN THỊ, không phải dữ liệu — $a$ chỉ để dựng hình minh họa; đáp số "$h$ theo $a$" HS tự tính.)*
- `ten_O/A/B/H`, `nhan_h`: nhãn (mặc định $O,A,B,H,h$).
- `hien_duong_cao`: vẽ $OH$ (đứt đỏ) + chân $H$ + ô vuông góc tại $H$ + nhãn $h$. Đặt `False` nếu chỉ cần tam giác trần.
- Trọng tài: SGK H5.5 (Vận dụng tr.115 — giới hạn khi $a\to0$ / $a\to+\infty$).

---
> **Lưu ý đặt hình (HP Đ18):** đồ thị hữu tỉ khổ ~11×9cm > 8cm → căn giữa dòng riêng (Đ18 ngoại lệ 1). Tam giác tọa độ nhỏ → neo phải mặc định. Hình minh họa lý thuyết (HĐ/Vận dụng) — KHÔNG lộ đáp án (Đ35): H5.5 chỉ dựng setup (tam giác + đường cao), KHÔNG ghi giá trị $h$ hay kết quả giới hạn.
> **Nghiệm thu [32b]:** 3 hình render + soi mắt QC V2 ĐẠT (đúng toán · trong chương · khớp khai nghĩa NGUON B16 · không lộ đáp án). pdflatex + pgfplots, dpi=200.
