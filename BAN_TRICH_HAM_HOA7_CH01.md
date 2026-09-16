# BẢN TRÍCH HÀM VẼ — HOA7_CH01 (Hình học lớp 7) — tự sinh từ `hinh_hoa_ch01.py`

> **Cho AI Soạn.** Đây là *CÁCH vẽ* (chữ ký hàm + tham số). *VẼ CÁI GÌ* nằm ở **phiếu khai nghĩa** Ông Bụt giao kèm nguồn.
> Tự sinh bằng introspect `hinh_hoa_ch01.py` qua `sinh_bantrich.py` — vá kho → chạy lại → khớp. KHÔNG sửa tay file này.
> Sinh ngày 16/09/2026. Mô hình (X): OB khai nghĩa → AI Soạn GỌI HÀM theo phiếu → PHANH kiểm.

Import trong script bài: `import hinh_hoa_ch01 as H1` rồi `h = H1.Hinh()`.
Gọi các method KHAI NGHĨA (mục 1) theo phiếu; cuối cùng `png = h.ve(out=..., tra_bytes=True)`.

---

## 1. HÀM KHAI NGHĨA — AI Soạn GỌI theo phiếu

Mỗi hàm nhận NGHĨA (tên đỉnh/tia, số đo, loại quan hệ). Máy tự tính tọa độ + PHANH kiểm.

| Hàm (chữ ký) | Dùng khi |
|---|---|

## 2. CỬA RENDER

| Hàm (chữ ký) | Dùng khi |
|---|---|
| `mo_hinh_hanh_tinh(out='hoa_hanhtinh', tra_bytes=False)` | Mô hình hành tinh Rutherford: hạt nhân dương ở tâm, electron trên NHIỀU quỹ đạo elip nghiêng. Không tham số (hình định tính, một-lần). |
| `nguyen_tu_bo(Z, cau_hinh, nhan=None, hien_e=True, out='hoa_ntbo', tra_bytes=False)` | Mô hình Bohr: hạt nhân tâm ghi +Z; vòng đồng tâm = số lớp trong cau_hinh; e là chấm phân bố đều trên mỗi vòng (từ trong ra ngoài). cau_hinh: list số e mỗi lớp, vd [2,8,7]. hien_e=False → sơ đồ 'CHƯA HOÀN THIỆN' (vòng trống, KHÔNG chấm e) cho đề 'hoàn thiện Hình' (oxygen 2.11, silicon 2.20); đáp án gọi hien_e=True. nhan → nhãn nguyên tố tùy chọn (vd 'Cl'). PHANH: sum(cau_hinh)==Z; lớp1≤2; lớp2≤8. |
| `nguyen_tu_hat_nhan(so_p, so_n, cau_hinh_vo, nhan=None, out='hoa_nthn', tra_bytes=False)` | Mô hình chi tiết: hạt nhân vẽ RÕ các quả cầu proton (màu p) + neutron (màu n) + vỏ electron (chấm màu e) trên vòng theo cau_hinh_vo. PHANH: sum(cau_hinh_vo)==so_p (trung hòa). |

## 3. HÀM HẠ TẦNG — máy dùng nội bộ, **AI Soạn KHÔNG gọi**

Các hàm hạ tầng (nhận tọa độ thô hoặc cần điểm đặt trước) do các hàm khai nghĩa ở mục 1 tự gọi bên trong. Theo Đ5.9, người không cho tọa độ → **AI Soạn không gọi trực tiếp nhóm này**. Danh sách đã ẩn khỏi bản trích. Gặp hình mà mục 1 chưa phủ (vd đa giác thường) → **DỪNG báo Ông Bụt bổ sung hàm thuần-nghĩa** (khép vòng A↔C), KHÔNG tự dùng hàm hạ tầng.

---

**Thống kê:** 0 hàm khai nghĩa (phơi) · 3 cửa render · 0 hàm hạ tầng (ẩn khỏi bản phát).
