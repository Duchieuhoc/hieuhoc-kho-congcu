# CHUẨN TRÌNH BÀY — BỔ SUNG v10.5 (2026-08-27, ô 8mm · hình 1,6–4cm)
**Chỉ đạo Giám đốc · Ông Bụt biên tập · nối vào CHUAN_TRINH_BAY_HIEUHOC.md**

## Quy tắc HÌNH TRÊN LƯỚI (bắt buộc, mọi khối THCS)

### QT-1. Ô lưới = 8mm · hình 1,6–4cm (mỗi hình gói trong 2–5 ô)
- **Ô lưới = 8mm cố định** cho mọi hình. Bề rộng nhúng Word: **rongCm = 0,8 × số_ô_ngang**, kẹp **1,6cm → 4cm**; cao tự theo tỉ lệ (cũng 1,6–4cm). Đổi hằng `CO_O` (build) là toàn hệ theo.
- **Thiết kế mọi hình gói trong 2–5 ô mỗi chiều** (2 ô = 1,6cm; 5 ô = 4cm). Hình bản chất rộng → thu gọn:
  · **Hình vẽ-thêm** (đề + ảnh qua O): đặt **đề nhỏ (≤2–3 ô)** và **O sát/tại góc đề** → hình lời giải ≤ 4–5 ô.
  · **Thoi:** nửa chéo nhỏ (vd a=2, b=1) → 4×2 ô. **Hình định lượng vẽ tỉ lệ minh hoạ**, số đo ghi ở **nhãn/đề** (không ép 1 ô = 1 đơn vị khi sẽ vượt 5 ô).
- **BỎ "sàn cứng 5,5cm"** và **bỏ chuẩn-hoá caoCm** cho hàng/lưới hình. Hàng nhiều hình: mỗi hình truyền `rongCm` riêng; hình mục ② để **dòng riêng căn giữa**.

### QT-2. TÂM hình rơi đúng NÚT lưới
- Tâm đối xứng (và các đỉnh) phải rơi **giao điểm đường lưới**, không rơi giữa ô.
- **Thoi:** dựng theo 2 nửa chéo **nguyên ô** — `hinh_thoi(A,B,C,D, a, b, ...)`; O + 4 đỉnh nút.
- **Vuông / chữ nhật / bình hành:** mỗi cạnh **chẵn ô** ⇒ tâm (giao chéo) rơi nút.
- **Lục giác đều:** giữ (tâm đã nút). Đường tròn / sao / đoạn: đặt O tại toạ độ **nguyên**.
- Kiểm nhanh khi QC: chấm tâm O phải nằm trên giao 2 vạch lưới.

*(Kho hiện thực: mốc 2026-08-26g — hinh_thoi đổi chữ ký; hinh_vuong/tu_giac toạ độ chẵn; template hangHinh nhận rongCm riêng.)*


### QT-3. Nhãn câu ở Phần Đúng/Sai & Trả lời ngắn — IN ĐẬM
- "**Câu 1.**", "**Câu 2.**"… ở Phần II (Đúng/Sai) và Phần III (Trả lời ngắn): **nhãn câu in đậm**, phần đề còn lại in thường. (Dựng: `para([run("Câu N. ",{bold:true}), run("…đề…")])`.)

### QT-4. Bố cục hình bài tập
- **Hình đề mục ③④⑤ + hình lời giải tách: NEO PHẢI** (`hinhBenPhai` cho đề; `loiGiaiND.hinhLoiGiai` cho lời giải — tự float phải). Chỉ hình mục ② & Phần II để **dòng riêng căn giữa**.
- **Hàng/lưới nhiều hình cỡ khác nhau:** ô **CĂN ĐÁY** (verticalAlign BOTTOM) → chú thích thẳng hàng, đáy hình thẳng. *(kho 2026-08-27a)*
- **Hàng nhiều hình nhận biết:** khi ô nhỏ (8mm) và mọi hình có `rongCm`, `hangHinh` cho **tối đa 4 hình/hàng** nếu tổng bề rộng ≤ 17cm (vd Bài 1 nhận biết 4 hình).
- **Phần III (trả lời ngắn):** đề định lượng đơn giản (đoạn thẳng, thoi cho sẵn số đo) **không cần hình** — bỏ hình cho gọn.
