#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_ds8_ch01.py — ENTRY chương: Toán 8 Chương I "Đa thức" (Đại số).
#   5 hình khai nghĩa từ đa thức (diện tích/thể tích): mảnh đất bậc thang,
#   tam giác vuông + 2 hình vuông, 2 khối hộp, 2 hình vuông khoét tròn,
#   net gấp hộp không nắp. COMPOSE (MO_HINH_KHO_HINH_THCS):
#   đa giác (hinh_dagiac) + đường tròn (hinh_tron_ve) + khối hộp (hinh_khoihop).
#   `import hinh_ds8_ch01 as H; H.Hinh()`. ve()/PHANH/style ở hinh_coban.
#   [28u] Lập cho DS8_CH01 (yêu cầu OB Đại số 2026-09-06).
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve
import hinh_khoihop

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [8]
CUA_RENDER = {'ve'}


class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron, hinh_khoihop.HinhKhoiHop):
    """Kho DS8 Chương I = đa giác + đường tròn + khối hộp. Chỉ compose.
    MRO: Hinh → HinhDaGiac → HinhTron → HinhKhoiHop → HinhCoBan."""
    pass
