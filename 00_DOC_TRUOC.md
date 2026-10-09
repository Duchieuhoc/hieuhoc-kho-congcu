# CẬP NHẬT KHO — chan_phan_giac_canh (LT2 Bài 12 HBH)
Ngày 2026-10-09 · OB · kho `hieuhoc-kho-congcu`

## VIỆC: push 1 commit lên GitHub (OB không có quyền push).

**Cách 1 — git apply (khuyên dùng):**
```
cd <thư mục kho đã clone>
git checkout main && git pull
git am 0001-chan_phan_giac_canh.patch
git push origin main
```

**Cách 2 — thay file rồi commit tay:** chép đè 2 file vào kho:
- `hinh_coban.py`  (thêm method `chan_phan_giac_canh`)
- `BAN_TRICH_HAM_HH8_CH03.md`  (regen 82→83 hàm)
rồi `git add -A && git commit -m "Thêm chan_phan_giac_canh (LT2 B12)" && git push`.

## HÀM MỚI
`chan_phan_giac_canh(ten, dinh, tia1, tia2, cat, nhan='above', mau=None, ve_doan=True, danh_dau_nua_goc=False)`
— Hạ chân tia phân giác góc (tia1·dinh·tia2) lên MỘT đoạn `cat=(P,Q)` bất kỳ
(khác `chan_phan_giac` chỉ hạ lên cạnh nằm GIỮA hai tia). Dùng cho Luyện tập 2:
phân giác góc D cắt AB, phân giác góc B cắt CD.

## BẰNG CHỨNG (test_chan_phan_giac_canh.py)
- góc ADE = góc EDC: lệch **0.000000°**
- góc ABF = góc FBC: lệch **0.000000°**
- AE = AD (tam giác cân): lệch **0.000000**  → đúng tính chất LT2
- E ∈ AB, F ∈ CD: True · PHANH tổng: PASS · render: OK (xem test_render_LT2.png)
- 26/26 module kho import sạch (0 regression).

Commit: ff42f05 (trên a98dbf8).
