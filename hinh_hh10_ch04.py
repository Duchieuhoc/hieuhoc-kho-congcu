#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh10_ch04.py — ENTRY chương: Hình học 10 Chương IV (Vectơ)
#   Bộ KNTT · HH10_CH04 · Ông Bụt Hình 2026-10-04.
#   COMPOSE: HinhDaGiac (hình vuông/thoi/thang-cân/lục giác/tam giác + coban)
#            + HinhToaDo (trục số, mặt phẳng Oxy — hinhMatPhangToaDo)
#            + VECTƠ (mũi tên A→B — HinhCoBan.vecto, mới vá 2026-10-04).
#   `import hinh_hh10_ch04 as H; h = H.Hinh()` cho AI Soạn (mạch khai nghĩa),
#    HOẶC H.Hinh.hinhMatPhangToaDo(... vecto=[...]) cho hình trên hệ trục (static).
#   MRO: Hinh → HinhDaGiac → HinhToaDo(=hinh_toado.Hinh) → HinhCoBan.
#
#   PRIMITIVE VECTƠ (vá [CH04], additive, 0 regression):
#     • h.vecto(A, B, nhan='\\vec a'|'\\overrightarrow{AB}', mau, net, vi_tri_nhan, rong)
#       — vectơ trên nền đa giác/lưới (đỉnh đã đặt). Mũi tên ĐÚNG A→B (khác tia/doan).
#     • hinhMatPhangToaDo(..., vecto=[{tu,den,nhan,mau,net,viTriNhan}])
#       — vectơ trong hệ trục Oxy (B10/B11 tọa độ).
#   Hình vuông/thoi/thang/lục giác/tam giác + trục/hệ trục: DÙNG HÀM KHO SẴN CÓ,
#   chỉ phủ thêm mũi tên vectơ lên trên.
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_toado

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [10]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.


class Hinh(hinh_dagiac.HinhDaGiac, hinh_toado.Hinh):
    """Kho Chương IV (Hình 10, Vectơ) = đa giác (hình vuông/thoi/thang-cân/lục giác/
    tam giác) + toạ độ (trục số, mặt phẳng Oxy) + VECTƠ (mũi tên A→B, kế thừa
    HinhCoBan.vecto). Chỉ compose — primitive vectơ nằm ở HinhCoBan (dùng chung)."""
    pass
