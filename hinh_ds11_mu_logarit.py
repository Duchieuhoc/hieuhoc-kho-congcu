# -*- coding: utf-8 -*-
# hinh_ds11_mu_logarit.py — ĐỒ THỊ HÀM MŨ & HÀM LÔGARIT (Đại số 11 Ch6)
# Generator ĐỘC LẬP (như hinh_ds11_luonggiac.py) — KHÔNG đụng file dùng chung.
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (cơ số a), máy TỰ dựng đường cong từ công thức
#   (pgfplots: a^x = exp(x*ln a); log_a x = ln x / ln a) — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
# Nhãn math-mode (pdflatex-safe): O, x, y, 1, a, y=a^x, y=\log_a x. KHÔNG chữ tiếng Việt trong hình.
#
# HAI CHẾ ĐỘ:
#   tong_quat=False (mặc định, ĐỒ THỊ CỤ THỂ — VD1/LT/BT vẽ y=(1/2)^x, y=3^x, y=log_(1/2) x…):
#       hiện số trục (1..8 / -3..3); chấm 2 điểm mốc + gióng nét đứt; KHÔNG ghi nhãn số trùng tick.
#   tong_quat=True  (DẠNG TỔNG QUÁT — Hình 6.1 / 6.3: y=a^x, y=log_a x tổng quát):
#       ẩn số trục; chỉ hiện ký hiệu '1' và 'a' tại 2 điểm mốc. Dùng cơ số đại diện để lấy DÁNG
#       (a>1: truyền 2.0; 0<a<1: truyền 0.5) + nhan=r'y=a^x\ (a>1)' để ghi nhãn tổng quát.
import math
import hinh_core as _HC


def _fmt(v):
    return ('%g' % float(v))


def _nhan_mu(co_so, nhan):
    if nhan is not None:
        return nhan
    a = float(co_so)
    if abs(a - round(a)) < 1e-9:
        return r'y=%g^{x}' % a
    from fractions import Fraction
    fr = Fraction(a).limit_denominator(100)
    return r'y=\left(\tfrac{%d}{%d}\right)^{x}' % (fr.numerator, fr.denominator)


def _nhan_log(co_so, nhan):
    if nhan is not None:
        return nhan
    a = float(co_so)
    if abs(a - round(a)) < 1e-9:
        return r'y=\log_{%g} x' % a
    from fractions import Fraction
    fr = Fraction(a).limit_denominator(100)
    return r'y=\log_{\frac{%d}{%d}} x' % (fr.numerator, fr.denominator)


def do_thi_ham_mu(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False,
                  out='dothi_mu', tra_bytes=False, scale=1.0):
    """ĐỒ THỊ HÀM SỐ MŨ y = a^x (SGK H6.1/H6.2). Máy TỰ dựng từ công thức (pgfplots exp(x*ln a)).
      co_so: cơ số a>0, a≠1. a>1 → đồng biến; 0<a<1 → nghịch biến.
      nhan : nhãn đường cong (None → tự sinh 'y=a^x' / 'y=(1/2)^x'…).
      hien_diem: True → chấm (0;1) & (1;a) + gióng nét đứt.
      tong_quat: False = đồ thị cụ thể (hiện số trục); True = dạng tổng quát (ẩn số trục, ký hiệu 1/a).
    PHANH nội sinh: đường cong sinh thẳng từ hàm mũ → luôn trên Ox (tiệm cận ngang Ox), qua (0;1),(1;a)."""
    a = float(co_so)
    if a <= 0 or abs(a - 1.0) < 1e-9:
        raise ValueError("[do_thi_ham_mu] co_so phải > 0 và ≠ 1, nhận %s" % co_so)
    dong_bien = a > 1.0

    xmin, xmax = -3.3, 3.3
    ymin, ymax = -0.9, 8.2
    # domain để đường gọn trong khung (clip vẫn cắt phần vượt)
    d1 = math.log(0.02) / math.log(a); d2 = math.log(ymax) / math.log(a)
    lo = max(min(d1, d2), xmin); hi = min(max(d1, d2), xmax)

    lab = _nhan_mu(a, nhan)
    if tong_quat:
        xtick, ytick = r'\empty', r'\empty'
    else:
        xtick, ytick = r'-3,-2,-1,1,2,3', r'1,2,3,4,5,6,7,8'

    cs = [r'\documentclass[border=6pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g]' % scale,
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis description cs:1,0.5)},anchor=north east},',
          r'  ylabel style={at={(axis description cs:0.5,1)},anchor=south west},',
          r'  xtick={%s}, ytick={%s},' % (xtick, ytick),
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,',
          r']']
    cs.append(r'\addplot[blue,line width=1pt,samples=250,domain=%g:%g]{exp(x*ln(%s))};'
              % (lo, hi, _fmt(a)))
    # nhãn đường cong (đặt trong vùng trống phía có đường)
    lab_x = (xmax - 0.15) if dong_bien else (xmin + 0.15)
    lab_anchor = 'south east' if dong_bien else 'south west'
    cs.append(r'\node[blue,anchor=%s,font=\small] at (axis cs:%g,%g) {$%s$};'
              % (lab_anchor, lab_x, 6.6, lab))
    if hien_diem:
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(1,0) (1,%g)};' % a)
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(0,%g) (1,%g)};' % (a, a))
        cs.append(r'\addplot[only marks,mark=*,mark size=1.4pt,black] coordinates {(0,1) (1,%g)};' % a)
        if tong_quat:
            # chỉ ở dạng tổng quát mới ghi ký hiệu 1/a (không có số trục để trùng)
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,1) {$1$};')
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,%g) {$a$};' % a)
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:1,0) {$1$};')
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)


def do_thi_ham_log(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False,
                   out='dothi_log', tra_bytes=False, scale=1.0):
    """ĐỒ THỊ HÀM SỐ LÔGARIT y = log_a x (SGK H6.3/H6.4). Máy TỰ dựng (pgfplots ln(x)/ln(a)).
      co_so: cơ số a>0, a≠1. a>1 → đồng biến; 0<a<1 → nghịch biến.
      nhan : nhãn đường cong (None → tự sinh).
      hien_diem: True → chấm (1;0) & (a;1) + gióng nét đứt.
      tong_quat: False = cụ thể (hiện số trục); True = dạng tổng quát (ẩn số trục, ký hiệu 1/a).
    PHANH nội sinh: tập xác định x>0 (tiệm cận đứng Oy), qua (1;0),(a;1)."""
    a = float(co_so)
    if a <= 0 or abs(a - 1.0) < 1e-9:
        raise ValueError("[do_thi_ham_log] co_so phải > 0 và ≠ 1, nhận %s" % co_so)
    dong_bien = a > 1.0

    xmin, xmax = -0.9, 8.2
    ymin, ymax = -3.3, 3.3
    eps = 0.04
    x1 = a ** ymax; x2 = a ** ymin
    lo = max(eps, min(x1, x2)); hi = min(xmax - 0.05, max(x1, x2))
    if hi <= lo:
        lo, hi = eps, xmax - 0.05

    lab = _nhan_log(a, nhan)
    if tong_quat:
        xtick, ytick = r'\empty', r'\empty'
    else:
        xtick, ytick = r'1,2,3,4,5,6,7,8', r'-3,-2,-1,1,2,3'
    lab_y = (ymax - 0.4) if dong_bien else (ymin + 0.4)
    lab_anchor = 'north east' if dong_bien else 'south east'

    cs = [r'\documentclass[border=6pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g]' % scale,
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis description cs:1,0.5)},anchor=north east},',
          r'  ylabel style={at={(axis description cs:0.5,1)},anchor=south west},',
          r'  xtick={%s}, ytick={%s},' % (xtick, ytick),
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,',
          r']']
    cs.append(r'\addplot[blue,line width=1pt,samples=250,domain=%g:%g]{ln(x)/ln(%s)};'
              % (lo, hi, _fmt(a)))
    cs.append(r'\node[blue,anchor=%s,font=\small] at (axis cs:%g,%g) {$%s$};'
              % (lab_anchor, xmax - 0.2, lab_y, lab))
    if hien_diem:
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(%g,0) (%g,1)};' % (a, a))
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(0,1) (%g,1)};' % a)
        cs.append(r'\addplot[only marks,mark=*,mark size=1.4pt,black] coordinates {(1,0) (%g,1)};' % a)
        if tong_quat:
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:1,0) {$1$};')
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:%g,0) {$a$};' % a)
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,1) {$1$};')
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)
