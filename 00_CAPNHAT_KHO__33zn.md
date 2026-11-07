[33zn] bieudo_xstk.py — NHÃN QUẠT NHỎ RA NGOÀI VÀNH. OB Đại số THCS, 2026-11-07; phát hiện khi QC B18 (DS7_CH05 biểu đồ quạt tròn).
LỖI: nhãn % của hình quạt rất nhỏ (<5%) đặt ở giữa cung 0,60R → 2 quạt nhỏ liền kề có nhãn CHỒNG lên nhau / tràn sang màu khác, không đọc được (H01 "2%2%" dính; H07 "0,55%" chồng "13,11%"; H11 "0,5%1,4%" dính).
VÁ: trong bieu_do_quat, quạt < 5% → đặt nhãn NGOÀI vành (x=±1,33) màu đen + đường dẫn mảnh xám (annotate arrowstyle "-"); tách y các nhãn cùng bên khoảng tối thiểu 0,17 để chống chồng. Quạt ≥ 5% giữ nhãn trong (trắng, 0,60R) như cũ. Mở rộng xlim (-1,65..1,65) chứa nhãn ngoài.
ADDITIVE: KHÔNG đổi chữ ký hàm / số liệu / nhãn quạt lớn → tương thích ngược (bài cũ pin SHA cũ không ảnh hưởng). Render-verify ĐẠT (H01/H07/H11 nhãn đọc rõ).
