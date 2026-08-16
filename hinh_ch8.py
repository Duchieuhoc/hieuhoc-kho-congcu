#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_ch8.py — ENTRY chương: Hình học 6 Chương VIII (Bài 32–37)
#   [13/08] TÁCH THEO MẠCH (MO_HINH_KHO_HINH_THCS): hàm dời sang
#     hinh_coban (cơ bản) + hinh_dagiac (đa giác). File này chỉ COMPOSE +
#     giữ metadata. `import hinh_ch8 as H8; H8.Hinh()` KHÔNG đổi cho AI Soạn.
#   Kế thừa: HinhCoBan → HinhDaGiac → Hinh. ve()/PHANH/style ở hinh_coban.
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve       # [15/08] mạch ĐƯỜNG TRÒN (đồng hồ/vòng quay/compa L6)

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [6]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại (không '_', không CUA_RENDER) = KHAI NGHĨA.

class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron):
    """Kho Chương VIII = cơ bản + đa giác + đường tròn. Chỉ compose.
    MRO: Hinh → HinhDaGiac → HinhTron → HinhCoBan (cùng nền ve()/PHANH/style)."""
    pass
