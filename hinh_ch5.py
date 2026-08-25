#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_ch5.py — ENTRY chương: Hình học 6 Chương V (Tính đối xứng) · 25/08/2026
#   COMPOSE: HinhDoiXung (trục/tâm + đa giác + coban) + HinhTron (đường tròn — Chương V
#   dùng "đường tròn + trục qua tâm" HĐ2/HĐ4 B21 và "hình tròn + tâm" HĐ2 B22).
#   `import hinh_ch5 as H5; h = H5.Hinh()` cho AI Soạn.
#   MRO: Hinh → HinhDoiXung → HinhDaGiac → HinhTron → HinhCoBan (chung nền ve()/PHANH).
# ═══════════════════════════════════════════════════════════════════
import hinh_doixung
import hinh_tron_ve

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [6]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.


class Hinh(hinh_doixung.HinhDoiXung, hinh_tron_ve.HinhTron):
    """Kho Chương V = đối xứng (trục/tâm) + đa giác + đường tròn. Chỉ compose."""
    pass
