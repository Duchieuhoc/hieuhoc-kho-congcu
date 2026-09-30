# CAPNHAT_KHO __ [31d] — HÌNH TẬP HỢP (pilot hình DS10_CH01_B02)
> Đẩy GitHub `Duchieuhoc/hieuhoc-kho-congcu` bằng **UPLOAD WEB (kéo-thả-ĐÈ / thêm mới)**. KHÔNG patch.
> Ông Bụt Đại số THPT · 30/09/2026 · Mốc kho công khai sau push = **2026-09-30 [31d]**.

## 4 file trong gói

| File | Loại | Nội dung |
|---|---|---|
| `hinh_tap_hop.py` | **THÊM MỚI** | 2 hàm hình tập hợp: `bieu_do_ven` · `truc_so_tap_hop` (generator độc lập) |
| `BAN_TRICH_HAM_DS10_CH01__taphop.md` | **THÊM MỚI** | bản trích 2 hàm cho AI Soạn (tự sinh) |
| `00_KHO_VERSION.txt` | **ĐÈ** | +mục [31d] ở đầu |
| `00_MUC_LUC_HAM.md` | **ĐÈ** | +mục "Tập hợp" (2 hàm) |

## KHÔNG đụng
- `hieuhoc_template.js` (giữ v10.27 [31c]) · `API_REFERENCE.md` · Hiến Pháp HH2627 · mọi module hình cũ.
- File mới **thuần additive** — bài cũ dựng lại: 0 hỏng.

## Kiểm nhanh sau push (tuỳ)
```
git clone https://github.com/Duchieuhoc/hieuhoc-kho-congcu kho_check && cd kho_check
python3 -c "import hinh_tap_hop, hinh_daiso, hinh_core; print('import OK')"
```

## ⚠ CHỐNG LỆCH PHA
- Gói này build trên **HEAD [31c] = 80fc474** (đã fetch xác nhận trùng origin trước khi vá).
- **Một thời điểm chỉ MỘT máy sửa file chung.** Sau khi push [31d], các máy khác (OB_DS, OB_HH THCS/THPT) phải clone lại bản mới trước khi sửa tiếp file chung.
- **AI Soạn B02 phải bung kho ≥ [31d]** mới có 2 hàm này — nếu bung kho cũ sẽ thiếu hàm → STOP báo OB.

---
### Kiểm chứng OB trước khi giao
- 17 ca render (mọi hình bài B02: Ven đơn/cắt/rời/lồng ℕℤℚℝ/3 vòng, tô giao·hợp·hiệu·phần bù, điền số & biểu thức đếm; trục đoạn/tia/nửa khoảng/giao/hợp) → **ĐẠT 100%**.
- Soi mắt 6 ca khó (giao, hiệu, phần bù, điền số, ℕ⊂ℤ⊂ℚ⊂ℝ, trục giao xếp tầng) → đúng chuẩn SGK.
- `import hinh_tap_hop` cùng hinh_core/hinh_coban/hinh_daiso → không xung đột.
