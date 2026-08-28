#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_tamgiac.py — ENTRY mạch TAM GIÁC: Hình học 7 Chương IV (Tam giác
#   bằng nhau) trở đi (CH05 quan hệ trong tam giác · HH8 · HH9).
#   [28a] TÁCH THEO MẠCH (MO_HINH_KHO_HINH_THCS): file này CHỈ COMPOSE +
#     giữ metadata — KHÔNG đẻ hàm. `import hinh_tamgiac as HT; HT.Hinh()`.
#   Kế thừa: HinhDaGiac (tam giác/tam_giac_can/tứ giác/đa giác) + HinhTron
#     (đường tròn/cung compa — B13 HĐ2/HĐ3, B15 Luyện tập 3, B16 vẽ trung trực).
#   Ký hiệu bằng ở BASE HinhCoBan (dùng chung): dau_bang (vạch cạnh ×/××/×××)
#     · goc_vuong (ô vuông 90°) · dau_goc_bang (cung góc + tick — nhấc từ
#     hinh_gocdt mốc 28a). Góc ngoài: tia_doi. Trung trực: duong + trung_diem
#     + goc_vuong + dau_bang. Lưới: diem_luoi + noi. Ngôi sao: ngoi_sao.
#   ve()/PHANH/style ở hinh_coban.
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_tron_ve

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [7, 8, 9]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại (không '_', không CUA_RENDER) = KHAI NGHĨA.

class Hinh(hinh_dagiac.HinhDaGiac, hinh_tron_ve.HinhTron):
    """Kho mạch TAM GIÁC = cơ bản + đa giác + đường tròn. Chỉ compose.
    MRO: Hinh → HinhDaGiac → HinhTron → HinhCoBan (cùng nền ve()/PHANH/style)."""
    pass
