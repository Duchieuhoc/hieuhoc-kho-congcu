<!-- 00_QUY_UOC_SUA_KHO.md · Quy ước sửa & dùng kho hàm · CS2627 · [29z] 2026-09-21 -->
<!-- Hợp nhất: ĐỀ NGHỊ (OB Đại số) + PHẢN BIỆN (OB Hình). Đặt cạnh các file 00_ trong kho. -->

# QUY ƯỚC SỬA & DÙNG KHO HÀM
**Mục đích:** dùng kho *hiệu quả* = **viết mới càng ít càng tốt**; chặn trùng lặp (tự-trùng lẫn hai-máy).
**Nguồn:** đề nghị OB-DS + phản biện OB-Hình (2026-09-21). Mọi thay đổi truy nguyên từ quyết định rõ ràng.

---

## 1. THANG BẬC DÙNG KHO — linh hồn của quy ước (đọc TRƯỚC mọi việc)

Trước mỗi nhu cầu hình/hàm, đi 4 bậc, **dừng ở bậc sớm nhất**:

| Bậc | Hỏi | Nếu ĐÚNG |
|---|---|---|
| **① Tra** | `00_MUC_LUC_HAM.md` có hàm nghĩa này chưa? | sang ② |
| **② Gọi lại** | Có hàm khớp nghĩa? | **GỌI LẠI — hết việc** |
| **③ Mở rộng** | Có hàm gần giống **và** đã có user thứ 2 THẬT? | **thêm tham số / `kieu=`**, không đẻ hàm song song |
| **④ Viết mới** | Không có + **có bài thật làm trọng tài** + qua **phép thử kế thừa** | viết mới, **đúng tầng**, **đặt tên theo nghĩa** |

> Sự cố DS9 (suýt viết lại `trục số` đã có) nổ vì **nhảy thẳng ④, bỏ ①②**. "Viết mới" là bậc CUỐI, không phải phản xạ đầu.

---

## 2. SÁU ĐIỀU (đã hợp nhất phản biện)

1. **LUẬT VÀNG — tra trước khi viết.** Không viết/đề xuất hàm trước khi: (a) kéo kho mới nhất; (b) tra `00_MUC_LUC_HAM.md` theo NGHĨA (Ctrl+F). *Chữa đúng bệnh DS9 nhất.*
2. **Mục lục hàm TỔNG `00_MUC_LUC_HAM.md`** — một chỗ tra "đã-có-chưa", gộp cả hàm vẽ hình (Python) lẫn hàm dựng Word (JS). **Tự sinh bởi `sinh_mucluc.py`, TÁI DÙNG `sinh_bantrich.py` + `API_REFERENCE.md`** (không parse độc lập → không đẻ nguồn-sự-thật thứ ba).
3. **Ưu tiên MỞ RỘNG hơn tách mới.** Biến thể → thêm `kieu=`/tham số (mẫu `hinhDienTichDaiSo` catghep|chia4|vien). **Ranh tách hàm mới: >3 nhánh khác hẳn VÀ ≥2 user THẬT** (hợp nhất "chống viết dư" của DS + "chống tổng-quát-hoá non" của Hình).
4. **Đặt tên theo NGHĨA, không theo bài/chương.** `hinhMatPhangToaDo` (tái dùng L7→9→THPT), KHÔNG `hinhCH1_…`. Generator standalone → tiền tố `hinh…`; method trên `Hinh` → snake_case ngữ nghĩa. *(Đây là hệ quả của phép thử kế thừa, không thay thế nó.)*
5. **Phân vùng SỞ HỮU + đồng bộ bằng mốc kho** (không khoá file cứng, dùng cơ chế sẵn có):
   - Đối chiếu **kho live** để chốt danh sách (không kê theo trí nhớ).
   - Vùng **dùng chung** (sửa: một-máy-một-lúc + CHANGELOG + bump `00_KHO_VERSION.txt`): `hinh_toado.py` *(sau B1)* · `hinh_core.py` · `hieuhoc_template.js` · các `sinh_*`.
   - Điểm đồng bộ = **lúc push GitHub**; máy kia thấy mốc bump ở **Bước 0 gate check** → biết có thay đổi.
6. **Checklist 6 gạch — dán đầu MỌI phiếu cập nhật kho:**
   ① Đã pull kho mới nhất? ② Quét trùng (`00_MUC_LUC_HAM.md`) — kết quả? ③ Mở rộng hàm cũ được không; nếu tách, vì sao (>3 nhánh + ≥2 user thật)? ④ Máy kia có đang sửa file dùng chung? **⑤ PHANH-test qua chưa (min example) — không qua PHANH = không giao. ⑥ Có bài thật SGK/SBT làm trọng tài chưa?**
   *Sau cài:* regen `sinh_apiref` / `sinh_bantrich` / `sinh_mucluc` → bump `00_KHO_VERSION.txt` + ghi CHANGELOG (nếu đụng file dùng chung).

---

## 3. GIỮ NGUYÊN (đã tốt)
Clone-nền · một-máy-một-lúc · upload đè · `sinh_apiref.js`/`sinh_bantrich.py` · tag mốc kho · triết lý Đ5.9 (khai nghĩa giá trị → máy tự tính toạ độ → PHANH kiểm; base compose per-bài **không** vào mục lục).

---

## 4. B1 — TÁCH `hinh_toado.py` (bước cấu trúc còn treo, làm riêng)

**Vì sao:** `hinh_daiso.py` đang giam các primitive **toạ độ cross-cutting** (trục số, mặt phẳng toạ độ, cắm điểm) trong silo sai tên — đúng vùng chồng lấn Hình↔Đại số, nơi trùng lặp dễ tái diễn. Đây là điều 4 ↔ điều 5 mâu thuẫn mà phản biện chỉ ra.

**Cách làm (an toàn, backward-compatible — qua KẾ THỪA, không cắt thô):**
1. Tạo `hinh_toado.py`: `class Hinh(HinhCoBan)` chứa `tia_so`, `truc_so_huu_ti`, `truc_do_chinh_xac`, `truc_doan_doc_diem`, `hinhMatPhangToaDo` (+ helper `_mptd_*`, `_vach*`, `_danh_dau`, `_so`).
2. `hinh_daiso.py`: đổi `class Hinh(HinhCoBan)` → `class Hinh(hinh_toado.Hinh)`, giữ lại phần **thuần đại số** (`dung_can_hai`, `hinhDienTichDaiSo`). Nhờ kế thừa, `import hinh_daiso; Hinh()` **vẫn đủ mọi method cũ** → DS6/DS7 chạy nguyên.
3. (Sau này) đường tròn-toạ độ (B07) là **việc bên Hình** dựng trong `hinh_toado.py` — Đại số **gọi lại, cấm viết mới** vùng này.
4. **Test bắt buộc:** import + render lại ít nhất 1 bài mỗi lớp đã dùng trục số (DS6/DS7) → không vỡ; regen `sinh_bantrich` các chương liên quan + `sinh_mucluc`.
5. Vì đụng vùng dùng chung: một-máy-một-lúc + CHANGELOG + bump mốc; báo máy Hình.

**Trạng thái:** chưa thực thi (là refactor lớp kế thừa của module đang chạy) — làm thành **một lượt riêng có test đầy đủ**, KHÔNG gộp vội. Mục lục auto-regen nên không phụ thuộc B1.

---

## 5. QUY TRÌNH CHUẨN KHI THÊM/SỬA HÀM (tóm tắt vận hành)
```
pull kho mới nhất
 → tra 00_MUC_LUC_HAM.md (theo NGHĨA)         [bậc ①②]
 → gọi lại / mở rộng nếu có                    [bậc ②③]
 → nếu viết mới: đúng tầng + tên theo nghĩa    [bậc ④]
 → PHANH-test + bài-thật-trọng-tài            [gạch ⑤⑥]
 → regen sinh_apiref / sinh_bantrich / sinh_mucluc
 → bump 00_KHO_VERSION.txt + CHANGELOG (nếu file dùng chung)
 → push (một-máy-một-lúc)
```

---
*© Hệ thống Phát triển Nguồn lực Hiếu Học — Quy ước sửa kho [29z] — hợp nhất OB-DS + OB-Hình 2026-09-21*
