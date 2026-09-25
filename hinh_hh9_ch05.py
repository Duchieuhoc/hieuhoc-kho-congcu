#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh9_ch05.py — ENTRY chương: Hình học 9 Chương V (ĐƯỜNG TRÒN) · 25/09/2026
#   COMPOSE: HinhDoiXung (trục/tâm đối xứng — B13) + HinhDaGiac (tam giác/tứ giác/
#   tam giác đều·cân — nội tiếp) + HinhTron (đường tròn + dây + cung + góc ở tâm +
#   [30i] tiếp tuyến · hai tiếp tuyến · tiếp tuyến chung · hình quạt · viên phân · nửa vành khuyên).
#   `import hinh_hh9_ch05 as H9C5; h = H9C5.Hinh()` cho AI Soạn.
#   MRO: Hinh → HinhDoiXung → HinhDaGiac → HinhTron → HinhCoBan (chung nền ve()/PHANH).
# ═══════════════════════════════════════════════════════════════════
import hinh_doixung
import hinh_tron_ve

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [9]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.


class Hinh(hinh_doixung.HinhDoiXung, hinh_tron_ve.HinhTron):
    """Kho Chương V lớp 9 = đối xứng (trục/tâm) + đa giác + đường tròn (dây·cung·
    góc ở tâm·tiếp tuyến·quạt·viên phân). Chỉ compose."""
    pass
