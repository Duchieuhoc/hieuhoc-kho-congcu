#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh7_ch10.py — ENTRY chương: Toán 7 Chương X "Một số hình khối
#   trong thực tiễn" (KNTT). Bài 36 (hình hộp chữ nhật & lập phương),
#   Bài 37 (lăng trụ đứng tam giác & tứ giác), Bài tập cuối chương X.
#   COMPOSE (MO_HINH_KHO_HINH_THCS):
#     đa giác (hinh_dagiac) + đường tròn (hinh_tron_ve) + khối hộp/lăng trụ (hinh_khoihop).
#   Trục hình 3D: khoi_hop_chu_nhat (hộp ghi kích thước) + lang_tru_dung
#     (lăng trụ đứng đáy đa giác bất kỳ, 2 hướng, nét khuất tự tính) — [29q].
#   Hộp CÓ NHÃN đỉnh + đường chéo: lang_tru_dung(đáy chu_nhat, huong='dung',
#     ten_dinh=[...]) rồi doan('A',"C'",net='dut') vẽ chéo không gian NÉT ĐỨT — KHÔNG cần hàm riêng.
#   `import hinh_hh7_ch10 as H; H.Hinh()`. ve()/PHANH/style ở hinh_coban.
#   [29q] Lập cho HH7_CH10 (Ông Bụt Hình 2026-09-20, Pha khai nghĩa DA HH7C10).
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve
import hinh_khoihop

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [7]
CUA_RENDER = {'ve'}


class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron, hinh_khoihop.HinhKhoiHop):
    """Kho HH7 Chương X = đa giác + đường tròn + khối hộp/lăng trụ. Chỉ compose.
    MRO: Hinh → HinhDaGiac → HinhTron → HinhKhoiHop → HinhCoBan."""
    pass
