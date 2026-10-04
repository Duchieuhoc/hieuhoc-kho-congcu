# -*- coding: utf-8 -*-
# hinh_ds11_mu_logarit.py — ĐỒ THỊ HÀM MŨ & HÀM LÔGARIT (Đại số 11 Ch6)
# Generator ĐỘC LẬP (như hinh_ds11_luonggiac.py) — KHÔNG đụng file dùng chung.
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (cơ số a), máy TỰ dựng đường cong từ công thức
#   (pgfplots: a^x = exp(x*ln a); log_a x = ln x / ln a) — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
# Nhãn math-mode (pdflatex-safe): O, x, y, 1, a, y=a^x, y=\log_a x. KHÔNG chữ tiếng Việt trong hình.
#
# HAI CHẾ ĐỘ: tong_quat=False (CỤ THỂ — hiện số trục; VD/BT) · tong_quat=True (TỔNG QUÁT — ẩn số trục, ký hiệu 1/a; Hình 6.1/6.3).
# duong_ngang=b: vẽ đường y=b cắt đồ thị (minh hoạ nghiệm PT/BPT — Hình 6.5–6.8, Bài 21).
#
# [31z] 2026-10-04 — VÁ pilot DS11_CH06_B20 (AI Soạn báo [SỬA] S1/S2/Đ1/Đ2):
#   • Nhãn trục x/y dời ra ĐẦU MŨI TÊN (anchor ngoài vùng tick) → hết đè tick "8"/đường cong (S1+Đ1).
#   • do_thi_ham_log: xmax + tick THÍCH ỨNG cơ số → (a;1) cơ số lớn (vd a=10, y=log x) luôn trong khung (S2).
#   • _nhan_*: chỉ format phân số khi KHỚP CHÍNH XÁC mẫu ≤ 12; cơ số vô tỉ (√3…) không đẹp → RAISE buộc truyền nhan (Đ2).
#   • +duong_ngang/nhan_ngang: đường y=b + điểm cắt + gióng (dự phòng Bài 21 — khỏi pilot lại).
import math
import hinh_core as _HC
from fractions import Fraction


def _fmt(v):
    return ('%g' % float(v))


def _phanso_dep(a):
    """Trả (tu, mau) nếu a là phân số 'đẹp' (mẫu ≤ 12, khớp CHÍNH XÁC); else None."""
    fr = Fraction(a).limit_denominator(12)
    if abs(float(fr) - a) < 1e-9 and fr.denominator <= 12:
        return fr.numerator, fr.denominator
    return None


def _nhan_mu(co_so, nhan):
    if nhan is not None:
        return nhan
    a = float(co_so)
    if abs(a - round(a)) < 1e-9:
        return r'y=%g^{x}' % a
    ps = _phanso_dep(a)
    if ps:
        return r'y=\left(\tfrac{%d}{%d}\right)^{x}' % ps
    raise ValueError("[do_thi_ham_mu] cơ số %s không 'đẹp' (vd √3) → PHẢI truyền nhan tường minh, "
                     "vd nhan=r'y=(\\sqrt3)^{x}'." % co_so)


def _nhan_log(co_so, nhan):
    if nhan is not None:
        return nhan
    a = float(co_so)
    if abs(a - round(a)) < 1e-9:
        return r'y=\log_{%g} x' % a
    ps = _phanso_dep(a)
    if ps:
        return r'y=\log_{\frac{%d}{%d}} x' % ps
    raise ValueError("[do_thi_ham_log] cơ số %s không 'đẹp' (vd √3) → PHẢI truyền nhan tường minh, "
                     "vd nhan=r'y=\\log_{\\sqrt3} x'." % co_so)


def _tick_list(lo, hi, step):
    """Chuỗi tick '1,2,...' (bỏ 0) trong [lo;hi] bước step."""
    vals = []
    k = step
    while k <= hi + 1e-9:
        if k >= lo - 1e-9:
            vals.append('%g' % k)
        k += step
    return ','.join(vals)


def do_thi_ham_mu(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False,
                  duong_ngang=None, nhan_ngang=None,
                  out='dothi_mu', tra_bytes=False, scale=1.0):
    """ĐỒ THỊ HÀM SỐ MŨ y = a^x (SGK H6.1/H6.2). pgfplots exp(x*ln a); qua (0;1),(1;a), tiệm cận ngang Ox.
      co_so a>0,a≠1 (a>1 đồng biến; 0<a<1 nghịch biến). nhan: nhãn đường cong (None→tự sinh; cơ số vô tỉ PHẢI truyền).
      hien_diem: chấm (0;1),(1;a) + gióng. tong_quat: False=cụ thể (số trục) / True=tổng quát (ký hiệu 1,a).
      duong_ngang=b: vẽ y=b cắt đồ thị tại x=log_a b (+ chấm + gióng) — minh hoạ nghiệm a^x=b (Bài 21)."""
    a = float(co_so)
    if a <= 0 or abs(a - 1.0) < 1e-9:
        raise ValueError("[do_thi_ham_mu] co_so phải > 0 và ≠ 1, nhận %s" % co_so)
    dong_bien = a > 1.0

    xmin, xmax = -3.3, 3.3
    ymin = -0.9
    # ymax thích ứng: đủ chứa (1;a) + (nếu có) đường y=b
    ycan = 8.2
    if a > 7:
        ycan = a * 1.18
    if duong_ngang is not None and float(duong_ngang) > 0:
        ycan = max(ycan, float(duong_ngang) * 1.15)
    ymax = ycan
    ystep = 1 if ymax <= 9 else 2

    d1 = math.log(0.02) / math.log(a); d2 = math.log(ymax) / math.log(a)
    lo = max(min(d1, d2), xmin); hi = min(max(d1, d2), xmax)

    lab = _nhan_mu(a, nhan)
    # nhãn đường cong về GÓC TRỐNG: a>1 → trên-trái; a<1 → trên-phải
    if dong_bien:
        lab_at = r'(axis cs:%g,%g)' % (xmin + 0.15, ymax - 0.3); lab_anchor = 'north west'
    else:
        lab_at = r'(axis cs:%g,%g)' % (xmax - 0.15, ymax - 0.3); lab_anchor = 'north east'

    xtick_s = r'\empty' if tong_quat else '-3,-2,-1,1,2,3'
    ytick_s = r'\empty' if tong_quat else _tick_list(1, math.floor(ymax), ystep)

    cs = [r'\documentclass[border=8pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g]' % scale,
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          # nhãn trục đặt NGAY ĐẦU MŨI TÊN, lệch ra ngoài vùng tick (vá S1/Đ1)
          r'  xlabel style={at={(axis cs:%g,0)}, anchor=south west, inner sep=1pt},' % xmax,
          r'  ylabel style={at={(axis cs:0,%g)}, anchor=south east, inner sep=1pt},' % ymax,
          r'  xtick={%s}, ytick={%s},' % (xtick_s, ytick_s),
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,',
          r']']
    cs.append(r'\addplot[blue,line width=1pt,samples=250,domain=%g:%g]{exp(x*ln(%s))};'
              % (lo, hi, _fmt(a)))
    cs.append(r'\node[blue,anchor=%s,font=\small] at %s {$%s$};' % (lab_anchor, lab_at, lab))
    if hien_diem:
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(1,0) (1,%g)};' % a)
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(0,%g) (1,%g)};' % (a, a))
        cs.append(r'\addplot[only marks,mark=*,mark size=1.4pt,black] coordinates {(0,1) (1,%g)};' % a)
        if tong_quat:
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,1) {$1$};')
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,%g) {$a$};' % a)
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:1,0) {$1$};')
    if duong_ngang is not None:
        b = float(duong_ngang)
        cs.append(r'\addplot[red,line width=0.9pt,domain=%g:%g]{%g};' % (xmin, xmax, b))
        cs.append(r'\node[red,anchor=south east,font=\small] at (axis cs:%g,%g) {$%s$};'
                  % (xmax - 0.1, b, nhan_ngang if nhan_ngang else ('y=%g' % b)))
        if b > 0:
            x0 = math.log(b) / math.log(a)
            if xmin < x0 < xmax:
                cs.append(r'\addplot[gray,dashed,line width=0.6pt] coordinates {(%g,0) (%g,%g)};' % (x0, x0, b))
                cs.append(r'\addplot[only marks,mark=*,mark size=1.5pt,red] coordinates {(%g,%g)};' % (x0, b))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)


def do_thi_ham_log(co_so=2.0, nhan=None, hien_diem=True, tong_quat=False,
                   duong_ngang=None, nhan_ngang=None,
                   out='dothi_log', tra_bytes=False, scale=1.0):
    """ĐỒ THỊ HÀM SỐ LÔGARIT y = log_a x (SGK H6.3/H6.4). pgfplots ln(x)/ln(a); TXĐ x>0; qua (1;0),(a;1).
      co_so a>0,a≠1. nhan: nhãn (None→tự sinh; cơ số vô tỉ PHẢI truyền). hien_diem: chấm (1;0),(a;1)+gióng.
      tong_quat: False=cụ thể / True=tổng quát. duong_ngang=b: vẽ y=b cắt đồ thị tại x=a^b (minh hoạ log_a x=b)."""
    a = float(co_so)
    if a <= 0 or abs(a - 1.0) < 1e-9:
        raise ValueError("[do_thi_ham_log] co_so phải > 0 và ≠ 1, nhận %s" % co_so)
    dong_bien = a > 1.0

    xmin = -0.9
    # xmax thích ứng: đủ chứa (a;1) khi cơ số lớn (vd a=10 → y=log x) — vá S2
    xcan = 8.2
    if a > 1 and a * 1.18 > xcan:
        xcan = a * 1.18
    xmax = xcan
    xstep = 1 if xmax <= 9 else 2
    ymin, ymax = -3.3, 3.3
    eps = 0.04
    x1 = a ** ymax; x2 = a ** ymin
    lo = max(eps, min(x1, x2)); hi = min(xmax - 0.05, max(x1, x2))
    if hi <= lo:
        lo, hi = eps, xmax - 0.05

    lab = _nhan_log(a, nhan)
    # nhãn đường cong về GÓC TRỐNG: a>1 → dưới-phải; a<1 → trên-phải
    if dong_bien:
        lab_at = r'(axis cs:%g,%g)' % (xmax - 0.2, ymin + 0.4); lab_anchor = 'south east'
    else:
        lab_at = r'(axis cs:%g,%g)' % (xmax - 0.2, ymax - 0.4); lab_anchor = 'north east'

    cs = [r'\documentclass[border=8pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g]' % scale,
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis cs:%g,0)}, anchor=south west, inner sep=1pt},' % xmax,
          r'  ylabel style={at={(axis cs:0,%g)}, anchor=south east, inner sep=1pt},' % ymax,
          r'  xtick={%s}, ytick={%s},' % (r'\empty' if tong_quat else _tick_list(1, math.floor(xmax), xstep),
                                          r'\empty' if tong_quat else '-3,-2,-1,1,2,3'),
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,',
          r']']
    cs.append(r'\addplot[blue,line width=1pt,samples=250,domain=%g:%g]{ln(x)/ln(%s)};'
              % (lo, hi, _fmt(a)))
    cs.append(r'\node[blue,anchor=%s,font=\small] at %s {$%s$};' % (lab_anchor, lab_at, lab))
    if hien_diem:
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(%g,0) (%g,1)};' % (a, a))
        cs.append(r'\addplot[gray,dashed,line width=0.5pt] coordinates {(0,1) (%g,1)};' % a)
        cs.append(r'\addplot[only marks,mark=*,mark size=1.4pt,black] coordinates {(1,0) (%g,1)};' % a)
        if tong_quat:
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:1,0) {$1$};')
            cs.append(r'\node[font=\small,anchor=north] at (axis cs:%g,0) {$a$};' % a)
            cs.append(r'\node[font=\small,anchor=east] at (axis cs:0,1) {$1$};')
    if duong_ngang is not None:
        b = float(duong_ngang)
        cs.append(r'\addplot[red,line width=0.9pt,domain=%g:%g]{%g};' % (0, xmax, b))
        cs.append(r'\node[red,anchor=south east,font=\small] at (axis cs:%g,%g) {$%s$};'
                  % (xmax - 0.1, b, nhan_ngang if nhan_ngang else ('y=%g' % b)))
        x0 = a ** b
        if 0 < x0 < xmax and ymin < b < ymax:
            cs.append(r'\addplot[gray,dashed,line width=0.6pt] coordinates {(%g,0) (%g,%g)};' % (x0, x0, b))
            cs.append(r'\addplot[only marks,mark=*,mark size=1.5pt,red] coordinates {(%g,%g)};' % (x0, b))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)
