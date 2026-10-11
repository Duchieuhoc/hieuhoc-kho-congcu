# BẢN TRÍCH HÀM — ĐỒ THỊ HÀM SỐ THPT (hinh_ds10_ch06.py) · kho [32p]
> import: `import hinh_ds10_ch06 as HS`. Render → PNG; build.js nhúng `H.hinhVe({ imageBuffer: buf })` (gọi hàm `tra_bytes=True`).
> Triết lý Đ5.9: hàm nhận NGHĨA (hệ số $a,b,c$ / nghiệm + dấu), máy TỰ dựng đường cong (pgfplots) + TỰ tính đỉnh / trục đối xứng / giao Ox,Oy / điểm đối xứng / dấu từng khoảng — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
> Chương: DS10_CH06 (Hàm số, Đồ thị và Ứng dụng). Nghiệm thu pilot DS10_CH06_B16 (parabol [32n]) · DS10_CH06_B17 (bảng xét dấu [32p]).
> **HÀM:** `parabol` (đồ thị hàm bậc hai) · `bang_xet_dau` + `bang_xet_dau_tam_thuc` (bảng xét dấu).

## parabol(a, b, c, xmin=None, xmax=None, ymin=None, ymax=None, hien_dinh=True, ten_dinh='I', hien_truc=True, hien_giao_ox=True, hien_giao_oy=True, diem_doi_xung=True, diem_them=None, nhan=None, hien_nhan=True, out='parabol', tra_bytes=False, scale=1.0)   ← [32n]
ĐỒ THỊ PARABOL $y = ax^2 + bx + c$ ($a\neq0$) trên hệ $Oxy$ (pgfplots — đường cong sinh thẳng từ công thức). **Máy TỰ tính** đỉnh $I\left(-\dfrac{b}{2a};-\dfrac{\Delta}{4a}\right)$, trục đối xứng $x=-\dfrac{b}{2a}$, giao $Ox$ (nếu $\Delta\ge0$), giao $Oy$ $(0;c)$, điểm đối xứng của giao $Oy$ qua trục $\left(-\dfrac{b}{a};c\right)$. **PHANH nội sinh:** $a\neq0$; đỉnh phải nằm trong khung (lệch → DỪNG).
- **`a, b, c`** — ba hệ số (số thực, `a≠0`). Bề lõm **quay lên** nếu `a>0`, **xuống** nếu `a<0` (máy tự theo dấu `a`).
- `xmin/xmax/ymin/ymax`: khung. **None → tự ôm** đỉnh + giao + 2 biên nhánh (nới thêm phía đỉnh để có chỗ nhãn $I$). **Truyền tay cho bài số lớn** (vd H6.10 `xmin=0,xmax=10.5,ymin=-3,ymax=56`).
- `hien_dinh` (mặc định True): chấm ĐỎ đỉnh + nhãn $I(x_I;y_I)$ (toạ độ tự format phân số đẹp `\tfrac`). `ten_dinh`: đổi tên đỉnh.
- `hien_truc`: trục đối xứng đứt nét xám + nhãn `$x=...$` (tự BỎ khi trục ≡ $Oy$, tức `b=0`).
- `hien_giao_ox` / `hien_giao_oy`: chấm giao điểm với $Ox$ (khi $\Delta\ge0$) / $Oy$. `diem_doi_xung`: chấm điểm đối xứng của giao $Oy$ (giúp HS vẽ chính xác hơn — kỹ thuật SGK VD2).
- `diem_them`: `[(x,y),...]` chấm thêm (vd bảng giá trị H6.10). **VERIFY:** máy kiểm mọi điểm phải thuộc parabol ($|ax^2+bx+c-y|<10^{-6}$) → sai thì DỪNG.
- `nhan`: nhãn đường cong (None → tự sinh `y=ax^2+bx+c` rút gọn hệ số ±1/0). `hien_nhan=False` để ẩn.
- **Trọng tài (nghiệm thu soi mắt [32n], 4 ca):** VD2 SGK `parabol(-2,-2,4)` (H6.12: $a<0$, cắt $Ox$ tại $-2;1$, đỉnh $(-\frac12;\frac92)$, giao $Oy$ $(0;4)$, điểm đx $(-1;4)$) · HĐ3 `parabol(1,2,2)` ($a>0$, KHÔNG cắt $Ox$, đỉnh $(-1;1)$) · LT2 `parabol(3,-10,7)` (đỉnh $(\frac53;-\frac43)$, cắt $Ox$ $1;\frac73$) · H6.10 `parabol(-2,20,0, xmin=0,xmax=10.5,ymin=-3,ymax=56, diem_them=[(1,18),(2,32),(3,42),(4,48),(6,48),(7,42),(8,32),(9,18)], hien_giao_oy=False, diem_doi_xung=False)` (parabol trên khoảng + bảng giá trị). **Dùng cho mọi parabol $y=ax^2+bx+c$ khác** (vẽ đồ thị hàm bậc hai, đọc đỉnh/trục đx/đơn điệu từ đồ thị, GTLN/GTNN, mô hình hóa quỹ đạo/diện tích/doanh thu).

## bang_xet_dau(moc, dau, ten_ham='f(x)', danh_dau=None, ky_am_vc='-\\infty', ky_duong_vc='+\\infty', out='bangxetdau', tra_bytes=False, scale=1.0)   ← [32p]
**BẢNG XÉT DẤU tổng quát** (tikz, chuẩn SGK) — khung 2 dòng: dòng `x` (mốc $-\infty$ · nghiệm · $+\infty$) + dòng `f(x)` (dấu GIỮA mỗi khoảng, ký hiệu tại mốc). Dùng cho xét dấu **tam thức · tích · thương · đạo hàm** (tái dùng giải tích).
- **`moc`** — list NHÃN các mốc (nghiệm) tăng dần, **math-string**: `['-4','1']` · `['x_1','x_2']` · `[r'1-\sqrt2', r'1+\sqrt2']` · `[]` (vô nghiệm, 1 khoảng duy nhất).
- **`dau`** — list dấu MỖI KHOẢNG, **len = len(moc)+1**, phần tử `'+'`/`'-'`.
- `danh_dau`: ký hiệu tại mỗi mốc (len = len(moc)): `'0'` (nghiệm → f=0, **mặc định**) | `'||'` (không xác định — mẫu=0, kẻ **gạch đứng đôi**, dùng cho BPT phân thức/thương).
- `ten_ham`: nhãn dòng dưới (`'f(x)'`, `'g(x)'`, `r"f'(x)"`, hay cả phân thức `r'\dfrac{g(x)}{h(x)}'`).

## bang_xet_dau_tam_thuc(a, b, c, ten_ham='f(x)', out='bxd_tamthuc', tra_bytes=False, scale=1.0)   ← [32p]
**BẢNG XÉT DẤU TAM THỨC BẬC HAI** $f(x)=ax^2+bx+c$ ($a\neq0$) — **máy TỰ tính** $\Delta$, nghiệm, dấu từng khoảng theo **định lí dấu** (Đ5.9). Wrapper của `bang_xet_dau`.
- Máy tự: $\Delta<0$ → cùng dấu $a$ mọi $x$ (1 khoảng); $\Delta=0$ → cùng dấu $a$, `0` tại nghiệm kép; $\Delta>0$ → trái dấu $a$ trong $(x_1;x_2)$, cùng dấu $a$ ngoài.
- **Nghiệm HỮU TỈ** → dùng thẳng wrapper (tự format `\tfrac`). **Nghiệm VÔ TỈ** (vd $1\pm\sqrt2$) → gọi `bang_xet_dau` TRỰC TIẾP với nhãn tường minh `[r'1-\sqrt2', r'1+\sqrt2']` (wrapper sẽ ra thập phân — KHÔNG dùng).
- **Trọng tài (nghiệm thu soi mắt [32p], 5 ca):** `bang_xet_dau_tam_thuc(2,6,-8)` (VD $\Delta>0,a>0$: $+\,0\,-\,0\,+$) · `bang_xet_dau([r'1-\sqrt2',r'1+\sqrt2'],['-','+','-'])` (VD $a<0$ vô tỉ) · `bang_xet_dau_tam_thuc(1,12,36)` ($\Delta=0$: $+\,0\,+$) · `bang_xet_dau_tam_thuc(1,1,1)` ($\Delta<0$: $+$) · `bang_xet_dau(['2','5'],['+','-','+'],danh_dau=['0','||'])` (BPT phân thức, `||` tại mẫu=0).

---
> **Lưu ý đặt hình (HP Đ18):** parabol khổ ~11×9cm > 8cm → căn giữa dòng riêng (Đ18 ngoại lệ 1). Bảng xét dấu rộng → cũng căn giữa dòng riêng. Ghép 2 parabol cạnh nhau (vd HĐ3 a>0 & a<0) → `H.hangHinh([...])` (Đ18.1).
> **Không lộ đáp án (Đ35):** hình minh họa lý thuyết/HĐ (cho sẵn trong SGK) dựng được bình thường. **Bài yêu cầu HS "vẽ parabol"** (vd BT 6.7, 6.30) — KHÔNG vẽ sẵn đáp ở đề; chỉ dựng ở phần LỜI GIẢI/đáp án giáo viên.
> **Nghiệm thu [32n]:** 4 hình render + soi mắt QC ĐẠT (đúng toán · trong chương · khớp khai nghĩa NGUON B16 · nhãn rõ · không lộ đáp án). pdflatex + pgfplots, dpi=200. ADDITIVE — module ĐỘC LẬP (chỉ import `hinh_core`), `hieuhoc_template.js` KHÔNG đổi (v10.35 [31za]); KHÔNG đụng file máy Hình / giaitich CH05.
> **Nghiệm thu [32p] (bảng xét dấu):** 5 ca render + soi mắt QC ĐẠT (Δ>0 a±, nghiệm vô tỉ nhãn tường minh, Δ=0, Δ<0, thương `||`). Đúng chuẩn SGK (dấu giữa khoảng, 0/|| tại mốc, gạch đứng tại nghiệm). ADDITIVE — chỉ THÊM 2 hàm vào module độc lập, `parabol` + bài cũ 0 đổi (regression parabol đã chạy lại OK).
> **⏳ CHƯA dựng (bổ khi gặp trong pilot sau):** (1) **parabol ký hiệu tổng quát** (H6.11: nhãn $x_1,x_2,-\frac{b}{2a},-\frac{\Delta}{4a}$ — minh họa công thức); (2) **đồ thị hàm nhiều công thức có nhánh parabol** (chữ V $|x|$ B15 — dùng `do_thi_bac_thang`; ghép đường thẳng + **parabol** H6.19/H6.26 SBT → cần bổ hàm `do_thi_ghep`, PILOT B15); (3) **hình hình-học** B17 H6.19 (3 đường tròn "vầng trăng" → tạm KHO⑦), B18 (tam giác/tứ giác/mặt cắt → kho Hình học). Thiếu hàm → AI Soạn DỪNG báo `[SỬA]`, OB bổ (Đ5.9).
