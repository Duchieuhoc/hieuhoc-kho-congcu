# CAP_NHAT_KHO — mốc 2026-08-25c  (HỢP NHẤT: thay cho gói 25b lẻ)
## Đẩy GitHub `Duchieuhoc/hieuhoc-kho-congcu` bằng UPLOAD WEB (kéo-thả-ĐÈ / thêm mới). KHÔNG patch.
> Gói này gộp cả 2 việc trong phiên (kim giây + đối xứng). Nếu **chưa** push gói `25b` trước đó → **bỏ qua 25b, push thẳng 25c này**. Nếu đã push 25b rồi → push tiếp 25c (chỉ thêm 3 file đối xứng + đè version).

| File | Loại | Nội dung |
|---|---|---|
| `hinh_doixung.py` | **THÊM MỚI** | 2 tiện ích: `truc_doi_xung` · `tam_doi_xung` (mạch đối xứng L6) |
| `hinh_ch5.py` | **THÊM MỚI** | entry Chương V: `Hinh(HinhDoiXung, HinhTron)` |
| `BAN_TRICH_HAM_HH6_CH05.md` | **THÊM MỚI** | bản trích Chương V (alias H5) |
| `hinh_tron_ve.py` | ĐÈ | kim() 3 loại (giờ/phút/giây đỏ) + `mat_dong_ho(giay=)` |
| `BAN_TRICH_HAM_HH6_CH08.md` | ĐÈ | tái sinh — kim `loai=`, mat_dong_ho `giay=` |
| `BAN_TRICH_HAM_HH6_CH04.md` | ĐÈ | tái sinh — đồng bộ chữ ký kim qua MRO |
| `00_KHO_VERSION.txt` | ĐÈ | mốc → **25c** (25c đối xứng · 25b kim giây) |

**Sau khi đẩy:** mốc kho công khai = `2026-08-25c`. Không đụng HP (V11.6), không đụng template.
**Kiểm nhanh (tuỳ):** clone lại → `quet_stamp.py` SẠCH · `python3 -c "import hinh_ch5, hinh_ch8"`.
