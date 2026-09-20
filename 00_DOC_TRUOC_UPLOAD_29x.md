# CẬP NHẬT KHO → 29x · Bổ 2 hàm hình trục số (DS7 B07)
**Soạn: OB Đại số · 2026-09-20 · phiếu DS7_CH02_B07**

## VÌ SAO
AI Soạn báo 2 CHẶN khi dựng hình B07 — cả 2 là bổ hàm kho (đúng §4):
1. **Hình 1 (dựng √2 bằng compa):** class Đại số `Hinh` không có `duong_tron`; append op 'tron' thô = lộ toạ độ (Đ5.9). Cần hàm compose ngữ nghĩa.
2. **Hình 5 (đọc điểm A,B,C,D):** `truc_so_huu_ti` chỉ nhận biên NGUYÊN + SCALE quá nhỏ (đoạn [0;1] chỉ ~2,3cm, 10 vạch chồng). `truc_do_chinh_xac` chỉ 1 điểm. Đoạn [4,6;4,7] biên thập phân không dựng được.

## ĐÃ BỔ (hinh_daiso.py — 2 hàm, ADDITIVE)
1. `dung_can_hai(canh=2, nhan_diem, nhan_can)` — dựng √2 trên trục (SGK Hình 2.3): máy tự dựng hình vuông cạnh c + 2 đường chéo + E + trục Ox + đường tròn tâm O bán kính OE → điểm A = nửa đường chéo. Compose ngữ nghĩa, KHÔNG phơi bán kính thô.
2. `truc_doan_doc_diem(trai, phai, chia, diem, hien_nhan_diem)` — trục đoạn PHÓNG TO, biên THẬP PHÂN OK, kéo rộng 10 đơn vị vẽ để đọc điểm không chồng. Mặc định KHÔNG in đáp số (Đ35).

## KIỂM CHỨNG (render mắt OB)
- ✓ dung_can_hai(2): hình vuông MNPQ + đường chéo + E + đường tròn cắt trục tại A=√2. Khớp SGK 2.3. (DEMO_Hinh1)
- ✓ truc_doan_doc_diem(0,1,10, A=0,7 B=0,9): 10 vạch rộng, điểm rõ, không đáp số. (DEMO_Hinh5a)
- ✓ truc_doan_doc_diem(4,6, 4,7, 10, C=4,62 D=4,67): biên thập phân chạy, rộng, không đáp số. (DEMO_Hinh5b)
- ✓ Rebuild toàn bài B07 (3 hình L1): kiemMay=[], oMath depth=1, [object Object]=0. Reproducible.
- ADDITIVE, nền 29w giữ nguyên mạch Hình, 0 hồi quy. Diff: PATCH_29x__hinh_daiso.diff.

## THẦY LÀM
1. **Upload đè GitHub** 3 file: `hinh_daiso.py`, `00_KHO_VERSION.txt`, `BAN_TRICH_HAM_DS7_CH02__daiso.md`.
2. Không cần nạp Project.

## ⚠️ ONE-WRITER
`hinh_daiso.py` là file CHUNG. Vá trên nền GitHub 29w hiện tại. Nếu GitHub nhảy mốc khác → báo OB vá lại. Xác nhận máy Hình không đang sửa hinh_daiso trước khi push.
