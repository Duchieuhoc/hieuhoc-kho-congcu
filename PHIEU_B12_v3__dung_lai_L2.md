<!-- PHIẾU KHAI NGHĨA HÌNH · Pha A · OB Hình học · 2026-10-09 · v3: sửa quy ước nhãn 'C' (không 'Cc') + hàm chan_phan_giac_canh cho LT2 -->
# PHIẾU KHAI NGHĨA HÌNH — HH8_CH03_B12
## Bài 12. HÌNH BÌNH HÀNH · SGK + SBT · KNTT Toán 8 Tập 1

- **Mã bài:** `HH8_CH03_B12` · SGK tr.57–61 · SBT tr.35–37 (bài chữ, không hình đề)
- **ENTRY kho:** `import hinh_tamgiac as H3; h = H3.Hinh()` (MRO: Hinh → HinhDaGiac → HinhTron → HinhCoBan). Bản trích: `BAN_TRICH_HAM_HH8_CH03.md` (SHA a98dbf8). Hàm chính: `tu_giac(loai='binh_hanh')`; `chan_vuong_goc` (VD2 AH,CK⊥BD); `chan_phan_giac_canh` (LT2 phân giác D,B hạ lên AB/CD); `giao`/`trung_diem` (đường chéo O); `tia_doi` (tia/góc ngoài); `so_do_goc`/`tu_giac_goc` (3.14/3.16/VD3); `diem_luoi`/`noi` (H.3.28 nền lưới).
- **Người khai:** OB · **Ngày:** 2026-10-07
- **Quy ước phiếu:** xem §0 phiếu B10. Trỏ luật: `BAN_DO_PHAN_CONG_HINH`.
- **⚠ QUY ƯỚC NHÃN ĐỈNH (bắt buộc đọc):** truyền **NHÃN đỉnh thật** `'A','B','C','D'` vào mọi hàm. Ký hiệu `Cc` trong CHỮ KÝ hàm kho (vd `tu_giac(A, B, Cc, D)`, `noi(A,B,Cc,D)`) **chỉ là TÊN THAM SỐ VỊ TRÍ** (đặt `Cc` để tránh trùng ký tự trong thân hàm) — **KHÔNG phải nhãn**. Truyền giá trị `'C'`, KHÔNG BAO GIỜ truyền chuỗi `'Cc'` (sẽ in nhãn "Cc" lên hình — lỗi CHẶN, đã gặp ở L1).
- **A↔C:** OB đã kiểm bản trích — ĐỦ hàm B12. Hàm `chan_phan_giac_canh` (hạ chân phân giác góc lên MỘT cạnh bất kỳ — cho LT2) **OB đã bổ vào kho** (commit sau a98dbf8). Không phải bổ thêm.

---

## 1. BẢNG DANH MỤC HÌNH (SGK tr.57–61)
| Mã | SGK | Vị trí | Loại | ĐỀ | LỜI GIẢI | Nền lưới | Khai §2 |
|---|---|---|---|---|---|---|---|
| `B12-01` | H.3.27 | Mở đầu (hai con đường a,b) | ②⚠ | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-02` | H.3.28a·b·c | HĐ1 (nhận biết HBH) | ① | OB cấp | – | ✔ | ✔ |
| `B12-03` | H.3.29 | Ví dụ 1 | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-04` | H.3.30 | HĐ3 (tính chất) | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-05` | H.3.31 | Ví dụ 2 | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-06` | H.3.32 | Luyện tập 2 | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-07` | H.3.33 | Thực hành 2 (dây xích) | ②⚠ | OB cấp | – | – | ✔ |
| `B12-08` | H.3.34a·b·c | Ví dụ 3 | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-09` | H.3.35 | Bài 3.14 | ① | OB cấp | AI mở-rộng-base | – | ✔ |
| `B12-10` | H.3.36a·b·c | Bài 3.16 | ① | OB cấp | AI mở-rộng-base | – | ✔ |

> Bài 3.13, 3.15, 3.17, 3.18 (SGK): đề-chữ, không hình đề → hình lời giải AI tự vẽ.

---

## 2. KHAI NGHĨA — HÌNH OB CẤP

### `B12-01` — H.3.27 · Mở đầu `[②⚠]`
- Hai con đường thẳng `a` (đi lên chéo) và `b` (nằm ngang) cắt nhau tạo một góc; **điểm dân cư `O`** nằm trong góc; đường thẳng qua `O` cắt `a` tại `A` (trên), cắt `b` tại `B` (dưới-phải). *Lõi giữ:* góc `xOy` (hai đường `a`, `b`), `O` trong góc, đường thẳng qua `O` cắt hai cạnh tại `A`, `B`. Bóc chi tiết ảnh đường/nhà.

### `B12-02` — H.3.28 · HĐ1 `[① · NỀN LƯỚI]`
- Trên lưới ô vuông, **ba tứ giác `ABCD`** — dựng qua `diem_luoi(ten, cột, hàng)` + `noi(A,B,Cc,D, kin=True)`. **Tọa độ ô (OB đặt — xem CỜ §3):**
  - **a) tứ giác thường** (không HBH): `A(1,4)`, `B(4,5)`, `C(5,1)`, `D(0,2)`. *(cạnh đối không song song → không HBH.)*
  - **b) "cái diều"** (không HBH): `A(2,5)`, `B(4,3)`, `C(2,0)`, `D(0,3)`. *(AB=AD, CB=CD — hai cặp cạnh KỀ bằng; đối xứng trục dọc qua A,C.)*
  - **c) hình bình hành**: `A(1,4)`, `B(4,4)`, `C(5,1)`, `D(2,1)`. *(AB∥DC & AB=DC=3 ô; AD∥BC — cạnh đối song song & bằng.)*
- Hình nhận-biết: câu hỏi HĐ1 = "tứ giác nào là HBH" → **đáp án c**. Đáp án KHÔNG phụ thuộc tọa độ cụ thể (chỉ cần a/b không-HBH, c là HBH). HS giải thích bằng đếm ô (cạnh đối // & bằng ở c).

### `B12-03` — H.3.29 · Ví dụ 1 `[①]`
- Tứ giác `ABCD`: `A` (trên-trái), `B` (trên-phải), `D` (dưới-trái, trên tia `x`), `C` (dưới-phải); cạnh `DA` kéo dài thành tia `x`, tia `By` tại `B`; **ba góc đánh dấu bằng nhau** (tại `A`, `D`, `B` — dữ kiện đề). (CM là HBH.) *(→ `tu_giac` + `tia_doi` + `dau_goc_bang` 3 góc.)*

### `B12-04` — H.3.30 · HĐ3 `[①]`
- Hình bình hành `ABCD` (`A` trên-trái, `B` trên-phải, `D` dưới-trái, `C` dưới-phải) với **hai đường chéo `AC`, `BD` cắt nhau tại `O`**. (CM các tính chất.) *(→ `tu_giac(loai='binh_hanh')` + `duong_qua` 2 chéo + `giao('O',...)`.)*

### `B12-05` — H.3.31 · Ví dụ 2 `[①]`
- Hình bình hành `ABCD`; đường chéo `BD`; `AH⊥BD` tại `H`, `CK⊥BD` tại `K` (ô vuông tại `H`, `K`); góc `D₁` tại `D`, `B₁` tại `B`. (CM `AHCK` là HBH.) *(→ `tu_giac(loai='binh_hanh')` + `duong_qua('B','D')` + `chan_vuong_goc('H','A','B','D')`, `chan_vuong_goc('K','C','B','D')`.)*

### `B12-06` — H.3.32 · Luyện tập 2 `[①]`
- Hình bình hành `ABCD` (`AB>BC`): `E` thuộc `AB` (trên), `F` thuộc `CD` (dưới); đoạn `DE`, `BF` (tia phân giác góc `D`, `B`); ký hiệu nửa góc bằng nhau tại `D`, `B`. (CM tam giác cân + `DEBF` hình gì.) *(→ `tu_giac('A','B','C','D', loai='binh_hanh')` + `chan_phan_giac_canh('E','D','A','C', cat=('A','B'))` (phân giác góc D cắt AB) + `chan_phan_giac_canh('F','B','A','C', cat=('C','D'))` (phân giác góc B cắt CD) + `dau_goc_bang` nửa góc. **Dùng `chan_phan_giac_canh`, KHÔNG dùng `chan_phan_giac`** — cái sau chỉ hạ chân lên cạnh nằm GIỮA hai tia.)*

### `B12-07` — H.3.33 · Thực hành 2 (dây xích) `[②⚠]`
- Tứ giác `ABCD` dạng **HBH làm bằng dây xích** (`A`, `B` trên; `D`, `C` dưới). *Lõi giữ:* HBH hai cặp cạnh đối bằng nhau (hai đoạn dài, hai đoạn ngắn xen kẽ). Bóc hoạ tiết mắt xích. *(→ `tu_giac(loai='binh_hanh')` + `dau_bang` 2 cặp cạnh.)*

### `B12-08` — H.3.34 · Ví dụ 3 `[①]`
- Ba tứ giác `ABCD`:
  - **a)** `AB=DC` (một vạch), `AD=BC` (hai vạch) — các cạnh đối bằng nhau; *(→ `tu_giac(loai='binh_hanh')` + `dau_bang`.)*
  - **b)** `\widehat{A}=110°` (trên-trái), `\widehat{D}=80°` (dưới-trái), `\widehat{C}=100°` (dưới-phải), `B` (trên-phải) — không ghi; *(→ `tu_giac`+`so_do_goc` 3 góc cho sẵn; B không ghi — KHÔNG điền.)*
  - **c)** hai đường chéo cắt nhau, ký hiệu hai nửa mỗi đường chéo bằng nhau (cắt tại trung điểm mỗi đường). *(→ `tu_giac` + 2 chéo + `giao` + `dau_bang` 4 nửa chéo.)*

### `B12-09` — H.3.35 · Bài 3.14 `[①]`
- Hình bình hành `ABCD`: `\widehat{A}=100°` (`A` trên-trái), `B`/`D`/`C` = **`?`**. (Tính các góc còn lại.) *(→ `tu_giac(loai='binh_hanh')` + `so_do_goc` A=100°, các góc khác `nhan_goc('?')`.)*
- ⚠ Hình ĐỀ: ghi `100°` tại A, `?` tại B,C,D — KHÔNG điền giá trị (Đ35).

### `B12-10` — H.3.36 · Bài 3.16 `[①]`
- Ba tứ giác `ABCD`:
  - **a)** `\widehat{A}=100°`, `\widehat{B}=80°`, `\widehat{C}=100°` (`D` không ghi); *(→ `tu_giac_goc(goc_A=100,goc_B=80,goc_C=100)`.)*
  - **b)** `\widehat{A}=75°` (trên-trái), `\widehat{D}` **góc vuông** (dưới-trái, ô vuông), `\widehat{C}=75°` (dưới-phải), `B` (phải); *(→ `tu_giac` + `so_do_goc` A=75,C=75 + `goc_vuong` tại D.)*
  - **c)** `\widehat{A}=70°` (trên-trái), `\widehat{B}=110°` (trên-phải), `\widehat{D}=110°` (dưới-trái), `C` (dưới-phải). *(→ `tu_giac` + `so_do_goc` 3 góc.)*

---

## 3. CỜ NGUỒN / LƯU Ý
- 🟡 **H.3.28 (HĐ1) nền lưới — TỌA ĐỘ Ô DO OB TỰ ĐẶT (chưa đối chiếu ảnh SGK tr.57).** Đây là hình **nhận-biết**: câu hỏi chỉ hỏi "tứ giác nào là HBH" → **đáp án c là HBH, bất biến theo vị trí cụ thể**. Tọa độ OB đặt bảo đảm a/b KHÔNG-HBH, c LÀ HBH (đếm ô kiểm được). **Thầy V3 đối chiếu ảnh SGK tr.57**: muốn khớp y sách → gửi ảnh, OB hiệu chỉnh tọa độ (không đổi đáp án).
- H.3.27, H.3.33: ②⚠ — trừu tượng hóa lõi, bóc ảnh minh họa.
- H.3.31 (VD2): hình lời giải = base + 2 chân vuông góc `chan_vuong_goc` (đỏ).
- Số caption nội bộ theo bài (Đ41.3).

*© Hiếu Học — CS2627 · PHIEU_KHAI_NGHIA__HH8_CH03_B12 · v3 (2026-10-09, OB) — sửa quy ước nhãn 'C' (không 'Cc'), hàm chan_phan_giac_canh cho LT2, H.3.28 tọa độ OB đặt (cờ V3)*
