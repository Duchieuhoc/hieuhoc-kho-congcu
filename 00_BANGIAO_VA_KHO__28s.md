# BÀN GIAO VÁ KHO — 28s · GUARD CHUỖI TRẦN
**OB Đại số · 2026-09-05 · nền clone SHA `9e2c22f9` (bản mới nhất) → mốc 28s · template v10.15**

> Đáp yêu cầu vá kho từ QC Vòng 2 DS7_CH01_B01. Đã vá cả 3 việc, test thật. File chung — thầy upload đè GitHub + đồng bộ 2 Project.

## Đã vá (nền = bản mới nhất, đúng one-writer)

**🔴 Việc 1 — Guard chuỗi trần trong `para()` → chọn phương án A (THROW).**
Quyết định thiết kế API: OB chốt **A**, không chọn B (tự bọc). Lý do: `para()` theo thiết kế nhận phần tử **đã chuẩn** (run/Math) — `paraInline()` mới là hàm cho string thô. Gọi `para(["string", omml])` là **dùng sai API**, không phải ca hợp lệ. Đối xứng guard B09 (đoạn-lồng-đoạn cũng THROW): biến lỗi âm thầm → ồn ào tại build, buộc gọi đúng, không âm thầm cứu (che thói quen sai). Đã kiểm: 108 lời gọi `para()` nội bộ đều qua `run()`/`toInline()` → **không ca nào vỡ**.

**🟠 Việc 2 — `_kiemTrinhBay` +cửa (a3)** bắt text trần dưới `<w:p>` (ngoài `<w:r>`). Lưới thứ hai của guard Việc 1 — chặn mọi nguồn kể cả hàm khác lỡ sinh ra, để AI Soạn tự bắt từ Vòng 1 (`kiemMay`).

**🟢 Việc 3 — `00_KHO_VERSION.txt`** bump 28q → **28s**, thêm khối [28r] (nội dung phiên trước chưa ghi) và [28s].

## Kiểm chứng (test thật, không đoán)
- Ca lỗi B01 `para(["Số hữu tỉ là ", phanSo(...), ...])` → **THROW** ✓ (báo đúng vị trí phần tử string).
- Cách gọi đúng (`run()` bọc sẵn · `paraInline()` · `para(run(...))`) → không throw ✓.
- Loạt hàm nội bộ (`mucTieu`/`viDu`/`paraInline`/oMath/tab) → không throw, cửa (a3) **không false-positive** ✓.
- File hỏng mô phỏng (Paragraph children=[string]) → `kiemMay` **bắt được** text-trần ✓.
- `node -c` sạch; mốc/version đồng bộ 28s · v10.15 (template + API_REFERENCE).

## Việc thầy làm
Upload đè GitHub `Duchieuhoc/hieuhoc-kho-congcu` **3 file** trong gói: `hieuhoc_template.js` (v10.15), `00_KHO_VERSION.txt` (28s), `API_REFERENCE.md` (v10.15). Đồng bộ `API_REFERENCE.md` sang **cả 2 Project**. Cập nhật "mốc kho yêu cầu" trong Instructions/00_NAP nếu muốn siết ≥ 28s (không bắt buộc — 28s tương thích ngược).

## Lưu ý cho luồng dựng (do chọn phương án A)
Từ 28s, **rebuild bất kỳ bài cũ nào** mà lỡ gọi `para([chuỗi])` sẽ **THROW** (trước đây âm thầm hỏng). Đây là tính năng, không phải hồi quy: gặp throw → sửa chỗ đó thành `paraInline([...])` hoặc bọc `run("...")`. B01 hiện tại AI Soạn đã tự sửa fast-path (`para`→`paraInline`) — độc lập với vá kho này.

*© Hệ thống Phát triển Nguồn lực Hiếu Học — Tài liệu nội bộ — CS2627 V11.8*
