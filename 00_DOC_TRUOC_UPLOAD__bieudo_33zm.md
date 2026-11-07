# UPLOAD KHO — Vòng quay: mũi tên không trùm nhãn (33zm, mốc 2026-11-07)
> Thầy upload đè **2 file** lên repo **Duchieuhoc/hieuhoc-kho-congcu** (web → Upload → Commit). Cả 2 ở GỐC repo.
> Gói này **gồm CẢ 33zl** (vạch trục phẩy) + 33zm (mũi tên). Nếu chưa upload 33zl thì file này THAY LUÔN. Clone từ HEAD mới nhất rồi vá → không lệch pha.

## File cần upload (2)
1. `bieudo_xstk.py`      — VÁ: `vong_quay` rút mũi tên 0,7R→0,55R (không che nhãn ô đích) + [33zl] vạch trục phẩy. **Tương thích ngược** (không đổi chữ ký/số liệu).
2. `00_KHO_VERSION.txt`  — thêm [33zm] + [33zl] ở đầu.

## Vì sao vá (phát hiện khi QC B42)
- Vòng quay (`vong_quay`) có `mui_ten_chi_vao`: đầu mũi tên dài 0,7R trùng vị trí nhãn ô (0,62R) → **che nhãn ô đích** ("3" bị che hẳn, "Nai" che một phần).
- Nay rút mũi tên về 0,55R: đầu dừng trước nhãn → nhãn đọc rõ, mũi tên vẫn chỉ đúng hướng ô.

## Sau khi upload
- Mốc kho **2026-11-07 [33zm]**. B43 (còn dùng vòng quay) + mọi vòng quay về sau tự đúng.
- **B42 đã được OB dựng lại** bằng kho vá (bản trong LƯU_BÀI B42 đã sạch — nhãn ô vòng quay rõ).
- Nợ cũ vẫn giữ: B40 + DS8_CH05 bản cũ còn vạch trục dấu chấm (rà khi tiện).
