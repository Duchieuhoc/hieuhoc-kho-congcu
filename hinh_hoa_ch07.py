#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hoa_ch07.py — ENTRY chương: Hóa (KHTN) lớp 9 Chương VII
#   "Giới thiệu về chất hữu cơ. Hydrocarbon và nguồn nhiên liệu".
#   Dựng 2 SƠ ĐỒ THÍ NGHIỆM bắt buộc (mục ② Hóa, Đ22.5):
#     • dot_butane        : đốt butane trong bình tam giác úp ngược (Hình 23.2, B23)
#     • dieu_che_ethylene : điều chế + thử tính chất ethylene (Hình 24.1, B24)
#   Generator ĐỘC LẬP, NGHĨA-THUẦN. Text trong hình CHỈ ASCII/ký hiệu
#   hoá (C_2H_4, Br_2, O_2…); chú thích tiếng Việt in ở Word qua .CHU_GIAI
#   (pdflatex không dựng dấu tiếng Việt trong TikZ) — mẫu callout như CH06.
#   [37a ĐỀ XUẤT] Ông Bụt (Hóa) 2026-11-27. ADDITIVE — module riêng chương.
# ═══════════════════════════════════════════════════════════════════
import hinh_core as _HC

LOP_MODULE = [9]
CUA_RENDER = {'dot_butane', 'dieu_che_ethylene'}

_PRE = (r'\documentclass[border=5pt]{standalone}'
        r'\usepackage{tikz}\usepackage{amsmath}'
        r'\usetikzlibrary{arrows.meta,decorations.pathmorphing}'
        r'\definecolor{thuytinh}{RGB}{90,120,140}'
        r'\definecolor{lua}{RGB}{245,150,40}'
        r'\definecolor{luado}{RGB}{230,90,30}'
        r'\definecolor{con}{RGB}{225,236,244}'
        r'\definecolor{naoh}{RGB}{214,232,220}'
        r'\definecolor{br2}{RGB}{226,196,70}'
        r'\definecolor{kimloai}{RGB}{120,124,130}'
        r'\definecolor{mobinh}{RGB}{214,226,232}'
        r'\begin{document}')

def _doc(body):
    return _PRE + r'\begin{tikzpicture}[line join=round,line cap=round]' + body + \
           r'\end{tikzpicture}\end{document}'

def _callout(x, y, n):
    return (f"\\node[circle,draw,fill=white,line width=0.8pt,inner sep=1.3pt,"
            f"font=\\scriptsize\\bfseries] at ({x},{y}) {{{n}}};")

def _lua(x, y, s=1.0):
    """Ngọn lửa: giọt cam ngoài + lõi đỏ."""
    return (f"\\fill[lua] ({x},{y}) .. controls ({x-0.22*s},{y+0.32*s}) and ({x-0.14*s},{y+0.55*s}) .. "
            f"({x},{y+0.72*s}) .. controls ({x+0.14*s},{y+0.55*s}) and ({x+0.22*s},{y+0.32*s}) .. ({x},{y});"
            f"\\fill[luado] ({x},{y+0.08*s}) .. controls ({x-0.1*s},{y+0.26*s}) and ({x-0.06*s},{y+0.4*s}) .. "
            f"({x},{y+0.5*s}) .. controls ({x+0.06*s},{y+0.4*s}) and ({x+0.1*s},{y+0.26*s}) .. ({x},{y+0.08*s});")


# ── Hình 23.2 — Đốt butane trong bình tam giác úp ngược ───────────
CHU_GIAI_DOT_BUTANE = {
    1: 'Bình tam giác (úp ngược)',
    2: 'Thành bình mờ đi do hơi nước ngưng tụ',
    3: 'Ngọn lửa đốt khí butane (bật lửa gas)',
}

def dot_butane(out='hoa7_dotbutane', tra_bytes=False):
    """Sơ đồ thí nghiệm đốt cháy butane (gốc Hình 23.2, B23).
       Bình tam giác úp ngược trên giá, bật lửa gas đốt dưới miệng.
       Callout 1–3; chú giải xem dot_butane.CHU_GIAI."""
    body = (
        # ── giá đỡ: trụ đứng + chân đế + tay kẹp ──
        r"\draw[kimloai,line width=2.2pt] (-3.0,-2.2) -- (-3.0,2.6);"
        r"\fill[kimloai] (-3.7,-2.35) rectangle (-2.3,-2.2);"
        r"\draw[kimloai,line width=1.8pt] (-3.0,1.9) -- (-1.55,1.9);"   # tay kẹp
        r"\fill[kimloai] (-1.75,1.72) rectangle (-1.5,2.08);"          # ngàm kẹp
        # ── bình tam giác ÚP NGƯỢC (đáy rộng ở trên, cổ chúc xuống) ──
        # nền trong bình (mờ do hơi nước)
        r"\fill[mobinh] (-1.6,2.2) -- (1.6,2.2) -- (0.42,-0.2) -- (-0.42,-0.2) -- cycle;"
        # thành thuỷ tinh
        r"\draw[thuytinh,line width=1.6pt] (-1.6,2.2) -- (-0.42,-0.2) -- (-0.42,-0.75);"
        r"\draw[thuytinh,line width=1.6pt] (1.6,2.2) -- (0.42,-0.2) -- (0.42,-0.75);"
        r"\draw[thuytinh,line width=1.6pt] (-1.6,2.2) -- (1.6,2.2);"    # đáy bình (trên)
        # gờ miệng bình (dưới)
        r"\draw[thuytinh,line width=1.6pt] (-0.52,-0.75) -- (0.52,-0.75);"
        # ── bật lửa gas dưới miệng bình ──
        r"\fill[kimloai!70!black] (-0.33,-2.05) rectangle (0.33,-1.35);"  # thân bật lửa
        r"\fill[luado!60!black] (-0.2,-1.35) rectangle (0.2,-1.2);"        # đầu kim loại
    )
    body += _lua(0.0, -1.15, 1.25)     # ngọn lửa butane lên tới miệng bình
    # callouts
    body += _callout(1.95, 1.2, 1)     # bình tam giác
    body += _callout(-1.95, 0.7, 2)    # thành bình mờ
    body += _callout(0.95, -1.55, 3)   # ngọn lửa butane
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
dot_butane.CHU_GIAI = CHU_GIAI_DOT_BUTANE


# ── Hình 24.1 — Điều chế và thử tính chất của ethylene ────────────
CHU_GIAI_DIEU_CHE_ETHYLENE = {
    1: 'Bình cầu có nhánh: cồn 96° + H₂SO₄ đặc',
    2: 'Đá bọt',
    3: 'Nguồn nhiệt (đun nóng)',
    4: 'Dung dịch NaOH (rửa khí)',
    5: 'Đốt khí C₂H₄ ở đầu ống vuốt nhọn',
    6: 'Ống nghiệm đựng nước Br₂ (bị mất màu)',
}

def dieu_che_ethylene(out='hoa7_ethylene', tra_bytes=False):
    """Sơ đồ điều chế và thử tính chất ethylene (gốc Hình 24.1, B24).
       Bình cầu có nhánh + nguồn nhiệt → ống dẫn qua NaOH → đốt đầu vuốt nhọn;
       nhánh dẫn vào ống nghiệm nước Br2. Callout 1–6; chú giải .CHU_GIAI."""
    body = (
        # ── giá đỡ trái ──
        r"\draw[kimloai,line width=2.0pt] (-4.6,-2.3) -- (-4.6,2.4);"
        r"\fill[kimloai] (-5.2,-2.45) rectangle (-4.0,-2.3);"
        r"\draw[kimloai,line width=1.6pt] (-4.6,1.5) -- (-3.75,1.5);"   # tay kẹp cổ bình
        # ── bình cầu có nhánh ──
        r"\fill[con] (-3.3,-0.35) circle (0.92);"                        # chất lỏng trong bình (nền)
        r"\draw[thuytinh,line width=1.6pt] (-3.3,-0.35) circle (0.92);"
        r"\draw[thuytinh,line width=1.6pt] (-3.62,0.5) -- (-3.62,1.65);" # cổ bình
        r"\draw[thuytinh,line width=1.6pt] (-2.98,0.5) -- (-2.98,1.65);"
        r"\draw[thuytinh,line width=1.4pt] (-2.75,0.72) -- (-1.95,1.15);" # nhánh dẫn khí
        # đá bọt + bề mặt chất lỏng
        r"\draw[con!40!thuytinh,line width=0.8pt] (-4.1,-0.2) .. controls (-3.6,-0.05) and (-3.0,-0.05) .. (-2.5,-0.2);"
        r"\fill[kimloai!60!white] (-3.55,-0.95) circle (0.07);"
        r"\fill[kimloai!60!white] (-3.15,-1.05) circle (0.07);"
        r"\fill[kimloai!60!white] (-3.35,-0.8) circle (0.06);"
        # ── nguồn nhiệt (đèn cồn) dưới bình ──
        r"\fill[kimloai!70!black] (-3.62,-2.3) rectangle (-2.98,-1.85);"
        r"\draw[thuytinh,line width=1.2pt] (-3.3,-1.85) -- (-3.3,-1.72);"
    )
    body += _lua(-3.3, -1.72, 0.72)
    body += (
        # ── ống dẫn khí: nhánh → xuống nhúng vào bình NaOH ──
        r"\draw[thuytinh,line width=1.4pt] (-1.95,1.15) -- (-1.3,1.15) -- (-1.3,-0.7);"
        # ── bình/cốc NaOH ──
        r"\fill[naoh] (-1.75,-1.55) rectangle (-0.55,-0.1);"
        r"\draw[thuytinh,line width=1.5pt] (-1.75,0.2) -- (-1.75,-1.55) -- (-0.55,-1.55) -- (-0.55,0.2);"
        # ống ra khỏi NaOH → lên, sang phải tới đầu vuốt nhọn
        r"\draw[thuytinh,line width=1.4pt] (-0.9,0.1) -- (-0.9,1.55) -- (1.15,1.55);"
        # đầu ống vuốt nhọn (thu nhỏ) + đốt
        r"\draw[thuytinh,line width=1.4pt] (1.15,1.55) -- (1.55,1.68) -- (1.42,1.5) -- (1.15,1.55);"
    )
    body += _lua(1.5, 1.68, 0.9)
    body += r"\node[font=\scriptsize\bfseries,thuytinh] at (0.2,1.78) {$C_2H_4$};"
    body += (
        # ── nhánh dẫn khí hình chữ L → ống nghiệm nước Br2 (phần b) ──
        r"\draw[thuytinh,line width=1.4pt] (-0.9,0.7) -- (2.9,0.7) -- (2.9,-0.1) -- (3.15,-0.1);"
        # ống nghiệm nước Br2
        r"\fill[br2] (2.95,-1.85) rectangle (3.75,-0.35);"
        r"\draw[thuytinh,line width=1.5pt] (2.95,0.35) -- (2.95,-1.75) arc (180:360:0.4) -- (3.75,0.35);"
    )
    # callouts
    body += _callout(-3.3, -0.1, 1)    # bình cầu (chất lỏng)
    body += _callout(-2.15, -0.85, 2)  # đá bọt
    body += _callout(-3.3, -2.6, 3)    # nguồn nhiệt
    body += _callout(-1.15, -1.55, 4)  # NaOH
    body += _callout(1.85, 1.95, 5)    # đốt C2H4
    body += _callout(3.35, -2.1, 6)    # ống nghiệm Br2
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
dieu_che_ethylene.CHU_GIAI = CHU_GIAI_DIEU_CHE_ETHYLENE
