#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hoa_ch08.py — ENTRY chương: Hóa (KHTN) lớp 9 Chương VIII
#   "Ethylic alcohol và acetic acid". Dựng SƠ ĐỒ THÍ NGHIỆM (mục ②, Đ22.5):
#     • na_ethylic         : Na + ethylic alcohol (Hình 26.4, B26)
#     • chay_ethylic       : đốt cháy ethylic alcohol trong bát sứ (B26)
#     • ester_hoa          : ester hoá acetic acid + ethylic alcohol (B27)
#     • so_sanh_hcl_acetic : đá vôi + HCl vs + CH3COOH → Ca(OH)2 (Hình 27.1 SBT, B27)
#   Generator ĐỘC LẬP, NGHĨA-THUẦN. Text trong hình CHỈ ASCII/ký hiệu hoá;
#   dấu tiếng Việt in ở Word qua .CHU_GIAI. [38a ĐỀ XUẤT] Ông Bụt (Hóa) 2026-11-28.
#   ADDITIVE — module riêng chương, KHÔNG đụng 36d/37a.
# ═══════════════════════════════════════════════════════════════════
import hinh_core as _HC

LOP_MODULE = [9]
CUA_RENDER = {'na_ethylic', 'chay_ethylic', 'ester_hoa', 'so_sanh_hcl_acetic'}

_PRE = (r'\documentclass[border=5pt]{standalone}'
        r'\usepackage{tikz}\usepackage{amsmath}'
        r'\usetikzlibrary{arrows.meta,decorations.pathmorphing}'
        r'\definecolor{thuytinh}{RGB}{90,120,140}'
        r'\definecolor{lua}{RGB}{245,150,40}'
        r'\definecolor{luaxanh}{RGB}{90,150,230}'
        r'\definecolor{luado}{RGB}{230,90,30}'
        r'\definecolor{chatlong}{RGB}{214,232,240}'
        r'\definecolor{nuocnong}{RGB}{236,214,210}'
        r'\definecolor{voi}{RGB}{224,224,228}'
        r'\definecolor{kimloai}{RGB}{120,124,130}'
        r'\begin{document}')

def _doc(body):
    return _PRE + r'\begin{tikzpicture}[line join=round,line cap=round]' + body + \
           r'\end{tikzpicture}\end{document}'

def _callout(x, y, n):
    return (f"\\node[circle,draw,fill=white,line width=0.8pt,inner sep=1.3pt,"
            f"font=\\scriptsize\\bfseries] at ({x},{y}) {{{n}}};")

def _lua(x, y, s=1.0, col='lua', loi='luado'):
    return (f"\\fill[{col}] ({x},{y}) .. controls ({x-0.22*s},{y+0.32*s}) and ({x-0.14*s},{y+0.55*s}) .. "
            f"({x},{y+0.72*s}) .. controls ({x+0.14*s},{y+0.55*s}) and ({x+0.22*s},{y+0.32*s}) .. ({x},{y});"
            f"\\fill[{loi}] ({x},{y+0.08*s}) .. controls ({x-0.1*s},{y+0.26*s}) and ({x-0.06*s},{y+0.4*s}) .. "
            f"({x},{y+0.5*s}) .. controls ({x+0.06*s},{y+0.4*s}) and ({x+0.1*s},{y+0.26*s}) .. ({x},{y+0.08*s});")

def _ong_nghiem(cx, by, w=0.55, h=2.3, muc=0.9, mau='chatlong'):
    """Ống nghiệm đứng, tâm cx, đáy by; chất lỏng cao 'muc'. Trả body."""
    l, r = cx-w, cx+w
    s  = f"\\fill[{mau}] ({l},{by+0.001}) rectangle ({r},{by+muc});"
    s += f"\\fill[{mau}] ({cx},{by}) ++(0,0) arc (0:0:0);"
    # đáy cong
    s += f"\\fill[{mau}] ({l},{by}) arc (180:360:{w}) -- ({r},{by+muc}) -- ({l},{by+muc}) -- cycle;"
    s += (f"\\draw[thuytinh,line width=1.5pt] ({l},{by+h}) -- ({l},{by}) "
          f"arc (180:360:{w}) -- ({r},{by+h});")
    return s


# ── B26 · Hình 26.4 — Na + ethylic alcohol ───────────────────────
CHU_GIAI_NA_ETHYLIC = {
    1: 'Ethylic alcohol',
    2: 'Mẩu natri',
    3: 'Bọt khí hydrogen (H₂) thoát ra',
}
def na_ethylic(out='hoa8_na_ethylic', tra_bytes=False):
    """Na phản ứng với ethylic alcohol trong ống nghiệm (gốc Hình 26.4, B26)."""
    body = _ong_nghiem(0, -1.2, w=0.6, h=3.0, muc=1.6)
    # mẩu natri
    body += r"\fill[kimloai] (-0.16,-0.2) rectangle (0.16,0.1);"
    # bọt khí
    for (bx, byy, rr) in [(-0.28,0.3,0.07),(0.22,0.5,0.06),(-0.1,0.75,0.08),(0.3,0.95,0.05),(0.0,1.15,0.06),(-0.3,1.0,0.05)]:
        body += f"\\draw[thuytinh,line width=0.7pt] ({bx},{byy}) circle ({rr});"
    body += r"\node[font=\scriptsize\bfseries,thuytinh] at (0,-2.05) {$2C_2H_5OH + 2Na$};"
    body += _callout(1.05, -0.4, 1)   # chất lỏng
    body += _callout(0.55, -0.05, 2)  # natri
    body += _callout(1.05, 0.8, 3)    # bọt khí
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
na_ethylic.CHU_GIAI = CHU_GIAI_NA_ETHYLIC


# ── B26 · Đốt cháy ethylic alcohol trong bát sứ ───────────────────
CHU_GIAI_CHAY_ETHYLIC = {
    1: 'Bát sứ đựng ethylic alcohol',
    2: 'Ngọn lửa (ethylic alcohol cháy, toả nhiệt)',
}
def chay_ethylic(out='hoa8_chay_ethylic', tra_bytes=False):
    """Đốt cháy ethylic alcohol trong bát sứ (B26, mục III.1)."""
    # bát sứ (chén nông)
    body  = r"\fill[voi] (-1.3,0) arc (180:360:1.3 and 0.55) -- cycle;"
    body += r"\draw[kimloai,line width=1.6pt] (-1.45,0.08) arc (180:360:1.45 and 0.62);"
    body += r"\draw[kimloai,line width=1.6pt] (-1.45,0.08) -- (-1.3,0.08) (1.3,0.08) -- (1.45,0.08);"
    # chất lỏng trong bát
    body += r"\fill[chatlong] (-1.0,0.02) arc (180:360:1.0 and 0.38) -- cycle;"
    # ngọn lửa xanh (alcohol) nhiều ngọn
    body += _lua(-0.45, 0.1, 1.15, col='luaxanh', loi='lua')
    body += _lua(0.0, 0.05, 1.5, col='luaxanh', loi='lua')
    body += _lua(0.45, 0.1, 1.15, col='luaxanh', loi='lua')
    body += _callout(1.75, -0.2, 1)
    body += _callout(0.95, 1.65, 2)
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
chay_ethylic.CHU_GIAI = CHU_GIAI_CHAY_ETHYLIC


# ── B27 · Phản ứng ester hoá ──────────────────────────────────────
CHU_GIAI_ESTER_HOA = {
    1: 'Hỗn hợp: ethylic alcohol + acetic acid + H₂SO₄ đặc',
    2: 'Cốc nước nóng (60–70 °C)',
    3: 'Lớp ester (ethyl acetate) nổi lên, có mùi thơm',
}
def ester_hoa(out='hoa8_ester', tra_bytes=False):
    """Ester hoá acetic acid + ethylic alcohol trong cốc nước nóng (B27, mục III.2)."""
    # cốc nước nóng
    body  = r"\fill[nuocnong] (-2.0,-2.0) rectangle (2.0,-0.2);"
    body += r"\draw[thuytinh,line width=1.6pt] (-2.1,0.3) -- (-2.0,-2.1) -- (2.0,-2.1) -- (2.1,0.3);"
    # mặt nước gợn
    body += r"\draw[thuytinh!50,line width=0.7pt] (-2.0,-0.2) .. controls (-1.2,-0.05) and (-0.4,-0.35) .. (0.4,-0.2) .. controls (1.2,-0.05) and (1.6,-0.35) .. (2.0,-0.2);"
    # ống nghiệm nghiêng nhẹ trong cốc (đặt thẳng cho gọn)
    body += _ong_nghiem(0, -1.7, w=0.5, h=3.2, muc=1.2, mau='chatlong')
    # lớp ester nổi (dải trên mặt chất lỏng)
    body += r"\fill[lua!35] (-0.5,-0.5) rectangle (0.5,-0.32);"
    # hơi/mùi
    body += r"\draw[thuytinh!60,line width=0.7pt] (-0.15,1.5) .. controls (-0.3,1.8) and (0.0,1.95) .. (-0.1,2.25);"
    body += r"\draw[thuytinh!60,line width=0.7pt] (0.15,1.5) .. controls (0.3,1.8) and (0.0,1.95) .. (0.1,2.25);"
    body += r"\node[font=\scriptsize\bfseries,thuytinh] at (0,-2.4) {$CH_3COOH + C_2H_5OH$};"
    body += _callout(0.95, 0.9, 1)    # hỗn hợp
    body += _callout(-2.35, -1.1, 2)  # cốc nước nóng
    body += _callout(0.95, -0.42, 3)  # lớp ester
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
ester_hoa.CHU_GIAI = CHU_GIAI_ESTER_HOA


# ── B27 · Hình 27.1 (SBT) — so sánh đá vôi + HCl vs + CH3COOH ──────
CHU_GIAI_SO_SANH = {
    1: 'Đá vôi (CaCO₃) + dung dịch HCl 1 M',
    2: 'Đá vôi (CaCO₃) + dung dịch CH₃COOH 1 M',
    3: 'Dung dịch Ca(OH)₂ (nhận khí CO₂ → vẩn đục)',
}
def _bo_thi_nghiem(x0, nhan):
    """Một bộ: bình tam giác (đá vôi+acid) + ống dẫn → ống nghiệm Ca(OH)2.
       x0 = dịch ngang; nhan = ký hiệu acid in trong bình."""
    s  = f"\\fill[chatlong] ({x0-0.9},{-0.9}) -- ({x0+0.9},{-0.9}) -- ({x0+0.35},{0.0}) -- ({x0-0.35},{0.0}) -- cycle;"
    # bình tam giác
    s += (f"\\draw[thuytinh,line width=1.4pt] ({x0-0.9},{-0.9}) -- ({x0-0.35},{0.0}) -- ({x0-0.35},{0.45});")
    s += (f"\\draw[thuytinh,line width=1.4pt] ({x0+0.9},{-0.9}) -- ({x0+0.35},{0.0}) -- ({x0+0.35},{0.45});")
    s += (f"\\draw[thuytinh,line width=1.4pt] ({x0-0.9},{-0.9}) -- ({x0+0.9},{-0.9});")
    # đá vôi (vài cục) dưới đáy
    for dx in (-0.4, -0.05, 0.3):
        s += f"\\fill[voi] ({x0+dx},{-0.82}) rectangle ({x0+dx+0.2},{-0.66});"
    s += f"\\node[font=\\scriptsize\\bfseries,thuytinh] at ({x0},{-0.35}) {{{nhan}}};"
    # ống dẫn: nút → lên → sang phải → cắm vào ống nghiệm Ca(OH)2
    s += (f"\\draw[thuytinh,line width=1.3pt] ({x0},{0.45}) -- ({x0},{1.1}) -- ({x0+1.7},{1.1}) -- ({x0+1.7},{0.2});")
    # ống nghiệm Ca(OH)2
    s += _ong_nghiem(x0+1.7, -1.0, w=0.42, h=2.0, muc=1.0, mau='voi')
    return s
def so_sanh_hcl_acetic(out='hoa8_sosanh', tra_bytes=False):
    """So sánh tốc độ sinh CO2: đá vôi + HCl (a) vs đá vôi + CH3COOH (b),
       dẫn vào Ca(OH)2 (gốc Hình 27.1 SBT, B27 — câu 27.16)."""
    body  = _bo_thi_nghiem(-3.6, r"$+\,HCl$")
    body += r"\node[font=\scriptsize\bfseries] at (-3.1,-1.55) {(a)};"
    body += _bo_thi_nghiem(1.3, r"$+\,CH_3COOH$")
    body += r"\node[font=\scriptsize\bfseries] at (1.8,-1.55) {(b)};"
    body += _callout(-4.55, -0.45, 1)   # bình (a)
    body += _callout(0.35, -0.45, 2)    # bình (b)
    body += _callout(3.6, 0.55, 3)      # ống Ca(OH)2 (b)
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
so_sanh_hcl_acetic.CHU_GIAI = CHU_GIAI_SO_SANH
