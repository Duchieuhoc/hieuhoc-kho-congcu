#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_ch4.py — ENTRY chương: Toán 6 Chương IV (Bài 18–20)
#   "Một số hình phẳng trong thực tiễn" (hình học trực quan).
#   COMPOSE theo mạch (MO_HINH_KHO_HINH_THCS): cơ bản + đa giác + đường tròn.
#   `import hinh_ch4 as H4; H4.Hinh()`.
#   Kế thừa: HinhCoBan → HinhDaGiac → HinhTron → Hinh. ve()/PHANH/style ở hinh_coban.
#   [20/08] Lập cho Chương IV; dùng luc_giac_deu + da_giac_deu (mới 20/08).
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve       # mạch ĐƯỜNG TRÒN (B19: H.4.15 SBT — đường tròn tâm O)

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [6]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại (không '_', không CUA_RENDER) = KHAI NGHĨA.

class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron):
    """Kho Chương IV = cơ bản + đa giác + đường tròn. Chỉ compose.
    MRO: Hinh → HinhDaGiac → HinhTron → HinhCoBan (cùng nền ve()/PHANH/style)."""
    pass
