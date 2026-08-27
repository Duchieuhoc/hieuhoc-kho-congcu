# CẬP NHẬT KHO → 2026-08-26f
**Ông Bụt · 2026-08-27** · Routing: **push GitHub** `Duchieuhoc/hieuhoc-kho-congcu`.

## NỘI DUNG THAY ĐỔI (1 hàm mới, không đụng hàm cũ)
`hinh_dagiac.chu_so_7doan(so, x0, y0, rong=1.0, cao=2.0, mau=None, rong_net='dam')`
— chữ số 0..9 kiểu 7 đoạn (mỗi đoạn nét đậm), cho bài TÂM đối xứng (lật nửa vòng 6↔9, giữ 0/1/2/5/8).
Bài thật: SBT B22 bài 5.20 (ghép thẻ số có tâm). Đã render kiểm cả 10 số.

## FILE KHO ĐÃ ĐỔI (3)
- `hinh_dagiac.py` — thêm hàm.
- `00_KHO_VERSION.txt` — mốc 26e → **26f** + ghi chú.
- `BAN_TRICH_HAM_HH6_CH05.md` — tái sinh (thêm chữ ký hàm mới).

## CÁCH ÁP (chọn 1)
**A. Áp patch:**
```
cd hieuhoc-kho-congcu
git apply CAP_NHAT_KHO_2026-08-26f.patch
python3 quet_stamp.py        # phải: ✅ SẠCH — V11.6
git add -A && git commit -m "kho 26f: chu_so_7doan (B22 tâm đối xứng)" && git push
```
**B. Thay 3 file trực tiếp** (dùng bản trong gói này) rồi `git add -A && git commit && git push`.

## KIỂM SAU PUSH
```
python3 quet_stamp.py                      # ✅ SẠCH V11.6
python3 -c "import hinh_ch5 as H5; H5.Hinh().chu_so_7doan(8,x0=0)"   # không lỗi
```
Đầu 00_KHO_VERSION.txt phải hiển thị: **Mốc kho : 2026-08-26f**.
