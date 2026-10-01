#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh10_ch03.py — ENTRY chương: Hình học 10 Chương III (Hệ thức lượng trong tam giác)
#   Bộ KNTT · HH10_CH03 · Ông Bụt Hình 2026-10-01.
#   COMPOSE: HinhDaGiac (tam giác + góc/cạnh/đường cao/trung tuyến + coban) + HinhTron
#   (đường tròn ngoại/nội tiếp tam giác — HĐ3 định lí sin Hình 3, HĐ4 diện tích Hình 7).
#   `import hinh_hh10_ch03 as H; h = H.Hinh()` cho AI Soạn.
#   MRO: Hinh → HinhDaGiac → HinhTron → HinhCoBan (chung nền ve()/PHANH).
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [10]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.


class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron):
    """Kho Chương III (Hình 10) = tam giác (góc/cạnh/đường cao/trung tuyến) + đường tròn
    ngoại/nội tiếp tam giác. Chỉ compose — không thêm hàm mới ở đây."""
    pass
