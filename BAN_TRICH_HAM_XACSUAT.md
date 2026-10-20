# BẢN TRÍCH HÀM — hinh_xacsuat.py (SƠ ĐỒ CÂY XÁC SUẤT)
## Dùng chung: DS10_CH09 (Xác suất cổ điển) · DS12_CH06 (Xác suất có điều kiện). Mốc [33m] · 2026-10-21.
> `import hinh_xacsuat as X`. Nhúng Word: `...H.hinhVe({ imageBuffer: X.so_do_cay(...tra_bytes=True...), rongCm: 8, chuThich: "..." })` (spread `...`).
> Render TikZ/pdflatex. Nhãn math-mode; Đ/đ qua `\newunicodechar`; biến cố đối `\overline{A}`. KHÔNG nhúng ảnh SGK (Đ42).

---

## so_do_cay(goc='O', cap1, cap2=None, out='so_do_cay', tra_bytes=False, scale=1.0, dx=2.4, dy=2.3)
Sơ đồ hình cây xác suất, chuẩn SGK (gốc trên cam, nhánh tỏa xuống, nhãn xác suất giữa cạnh).
- **goc**: nhãn gốc (math-string), vd `'O'`.
- **cap1**: list nút tầng 1, mỗi nút `{'nhan': <math>, 'xs': <math nhãn xác suất trên nhánh>}`. VD `{'nhan':'Đ','xs':r'\frac{5}{12}'}`.
- **cap2**: list CÙNG độ dài cap1; `cap2[i]` = list con của nút `cap1[i]`, mỗi con `{'nhan', 'xs', 'la'(optional, nhãn kết quả dưới lá)}`. Để `None` → cây 1 tầng.
- **PHANH**: `len(cap2)==len(cap1)`; `len(cap1)>=2`.

**VD4 B18 (bút bi — phân số):**
```python
X.so_do_cay(goc='O',
  cap1=[{'nhan':'Đ','xs':r'\frac{5}{12}'}, {'nhan':'X','xs':r'\frac{7}{12}'}],
  cap2=[[{'nhan':'Đ','xs':r'\frac{4}{11}','la':'ĐĐ'}, {'nhan':'X','xs':r'\frac{7}{11}','la':'ĐX'}],
        [{'nhan':'Đ','xs':r'\frac{5}{11}','la':'XĐ'}, {'nhan':'X','xs':r'\frac{6}{11}','la':'XX'}]],
  tra_bytes=True)
```
**Hình 6.2 B19 (ông An — thập phân, biến cố đối):**
```python
X.so_do_cay(goc='O',
  cap1=[{'nhan':'A','xs':'0,4'}, {'nhan':r'\overline{A}','xs':'0,6'}],
  cap2=[[{'nhan':'B','xs':'0,3'}, {'nhan':r'\overline{B}','xs':'0,7'}],
        [{'nhan':'B','xs':'0,4'}, {'nhan':r'\overline{B}','xs':'0,6'}]],
  tra_bytes=True)
```
→ Nghiệm thu OB 21/10 (render + soi mắt ĐẠT).

---
## BẢNG DỮ LIỆU THỐNG KÊ 2×2 — KHÔNG hàm mới
Dùng `bangSoLieu` (template.js) có sẵn: `bangSoLieu({ tieuDe:[...], hang:[[...],...] })`. Ô góc để text thường (vd "Điều kiện \\ Kết quả"); gạch chéo ô góc là tồn cosmetic — vá sau nếu Thầy cần.
