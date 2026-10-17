# CẬP NHẬT KHO [33f] — KHOFIX triTuyetDoi()
2026-10-17 · Ông Bụt Đại số THPT · nối tiếp [33e] SHA 671f356 (máy Hình nghỉ — one-writer)

## Lỗi
`triTuyetDoi(bieuThuc)` tạo `m:e` tay rồi đưa vào `createMathBase` (hàm này ĐÃ tự bọc `m:e`) → sinh `<m:e><m:e>` lồng trong `<m:d>` → **Word TỪ CHỐI MỞ FILE** ("unreadable content"). lxml / LibreOffice / kiemMay-regex cũ ĐỀU LỌT (cùng lớp lỗi đã vá cho `ngoac` [KHOFIX-ngoac 28s] + `soGachTren`; `triTuyetDoi` còn sót). Lộ khi AI Soạn dựng ⑤ Tổng kết (phương án |x| câu 5) — né tạm bằng |x| chữ thường.

## Vá (mirror KHOFIX-ngoac)
- Bỏ lớp `m:e` tự bọc: `createMathBase({ children: _mathChild(bieuThuc) })`.
- `_mathChild` → nhận OMML lồng (phân số/căn trong |·|). Trả `_dmath(d)` → nestable.
- CHỮ KÝ KHÔNG ĐỔI → KHÔNG regen API_REFERENCE.

## Nghiệm thu
- render-test `|x-3|` + `|2x+1/2|`: **m:e lồng = 0**, dấu | begChr = 4, **oMath depth = 1**, kiemMay PASS.
- **REGRESSION:** ⑤ `DS12_CH01_ONTAP_TK` rebuild [33f] **BYTE-IDENTICAL** [33e] (⑤ không dùng triTuyetDoi → chứng minh additive, 0 ảnh hưởng).
- hinh_*.py KHÔNG đụng → regression [33e..] nguyên.

## Sau push → HEAD [33f]
Cập nhật "mốc kho yêu cầu" Phụ lục DaiSo_THPT v2.4 = [33f]. Mọi bài dùng |f(x)| OMML (nếu có) nay an toàn.
