# -*- coding: utf-8 -*-
# hinh_ds11_giaitich.py — ĐỒ THỊ GIẢI TÍCH (Đại số & Giải tích 11, Ch5: Giới hạn. Hàm số liên tục)
# Generator ĐỘC LẬP (như hinh_ds11_luonggiac.py / hinh_ds11_mu_logarit.py) — KHÔNG đụng file dùng chung.
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (hệ số hàm), máy TỰ dựng đường cong từ công thức (pgfplots)
#   — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42). Nhãn math-mode (pdflatex-safe): O, x, y, số,
#   x=c, y=a. KHÔNG chữ tiếng Việt trong hình.
#
# [32c] 2026-10-04 — +do_thi_bac_thang (PILOT DS11_CH05_B17, hàm số liên tục H5.7). Dưới: [32b] 2026-10-04 — PILOT DS11_CH05_B16 (Giới hạn hàm số). 3 hàm:
#   • do_thi_huu_ti(dang='doi_truc')      — hyperbol dời trục y=a+b/(x-c): 2 nhánh, TCĐ x=c, TCN y=a (H5.4).
#   • do_thi_huu_ti(dang='nghich_dao_binh') — y=k/(x-c)^2: hàm chẵn chữ U, TCĐ x=c, TCN y=0 (H5.6).
#   • tam_giac_toa_do(a)                  — tam giác vuông OAB trên Oxy, A=(a;0) B=(0;1), đường cao OH (H5.5).
import math
import hinh_core as _HC


def _fmt(v):
    return ('%g' % float(v))


def do_thi_huu_ti(dang='doi_truc', a=1.0, b=2.0, c=1.0, k=1.0,
                  xmin=None, xmax=None, ymin=None, ymax=None,
                  nhan=None, hien_tc=True, out='dothi_ht', tra_bytes=False, scale=1.0):
    """ĐỒ THỊ HÀM HỮU TỈ (pgfplots — máy dựng đường cong thẳng từ công thức; PHANH nội sinh).
      dang='doi_truc'        : y = a + b/(x-c). Hyperbol dời trục. TCĐ x=c (đứng), TCN y=a (ngang). 2 nhánh. (H5.4: a=1,b=2,c=1)
      dang='nghich_dao_binh' : y = k/(x-c)^2.  Hàm chữ U (k>0: 2 nhánh trên Ox). TCĐ x=c, TCN y=0. (H5.6: k=1,c=0)
      hien_tc: vẽ tiệm cận đứt nét (bỏ nét trùng trục khi c=0 / a=0). nhan: nhãn đường cong (None→tự sinh)."""
    if dang == 'doi_truc':
        xmin = -8.0 if xmin is None else xmin
        xmax = 8.0 if xmax is None else xmax
        # khung y ôm TCN y=a: chừa 4 đơn vị mỗi phía quanh a
        ymin = (a - 4.0) if ymin is None else ymin
        ymax = (a + 4.0) if ymax is None else ymax
        eps = 0.04
        # PHANH nội sinh: TCĐ x=c, TCN y=a phải nằm trong khung
        assert xmin < c < xmax, "[huu_ti] TCĐ x=%g ngoài khung [%g;%g]" % (c, xmin, xmax)
        assert ymin < a < ymax, "[huu_ti] TCN y=%g ngoài khung [%g;%g]" % (a, ymin, ymax)
        expr = r'%s + (%s)/(x-(%s))' % (_fmt(a), _fmt(b), _fmt(c))
        if nhan is None:
            # y = a + b/(x-c), rút gọn hiển thị
            nhan = r'y=%g+\dfrac{%g}{x-%g}' % (a, b, c) if c != 0 else r'y=%g+\dfrac{%g}{x}' % (a, b)
        # 2 nhánh: trái (xmin..c-eps), phải (c+eps..xmax)
        branches = [(xmin, c - eps), (c + eps, xmax)]
    elif dang == 'nghich_dao_binh':
        xmin = -3.2 if xmin is None else xmin
        xmax = 3.2 if xmax is None else xmax
        ymin = -0.6 if ymin is None else ymin
        ymax = 5.0 if ymax is None else ymax
        eps = 0.02
        assert xmin < c < xmax, "[huu_ti] TCĐ x=%g ngoài khung" % c
        expr = r'(%s)/((x-(%s))^2)' % (_fmt(k), _fmt(c))
        if nhan is None:
            nhan = r'y=\dfrac{%g}{x^2}' % k if c == 0 else r'y=\dfrac{%g}{(x-%g)^2}' % (k, c)
        branches = [(xmin, c - eps), (c + eps, xmax)]
    else:
        raise ValueError("[do_thi_huu_ti] dang phải 'doi_truc' | 'nghich_dao_binh', nhận %r" % dang)

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
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  restrict y to domain=%g:%g,' % (ymin - 1, ymax + 1),  # cắt gọn khi vọt tiệm cận
          r'  unbounded coords=jump,',
          r'  clip=true,',
          r']']
    # tiệm cận đứt nét (bỏ nét trùng trục Oy khi c=0; bỏ TCN trùng Ox khi a=0)
    if hien_tc:
        if abs(c) > 1e-9:
            cs.append(r'\addplot[gray,dashed,line width=0.7pt] coordinates {(%g,%g) (%g,%g)};' % (c, ymin, c, ymax))
            # nhãn TCĐ đặt ở ĐỈNH, lệch trái đường đứt (tránh đè nhánh đi xuống -∞ ở đáy)
            cs.append(r'\node[gray,anchor=north east,font=\footnotesize] at (axis cs:%g,%g) {$x=%g$};' % (c - 0.12, ymax - 0.25, c))
        tcn = a if dang == 'doi_truc' else 0.0
        if abs(tcn) > 1e-9:
            cs.append(r'\addplot[gray,dashed,line width=0.7pt] coordinates {(%g,%g) (%g,%g)};' % (xmin, tcn, xmax, tcn))
            cs.append(r'\node[gray,anchor=west,font=\footnotesize] at (axis cs:%g,%g) {$y=%g$};' % (xmin + 0.25, tcn + 0.3, tcn))
    # đường cong 2 nhánh (cùng màu, cùng công thức)
    for (lo, hi) in branches:
        cs.append(r'\addplot[blue,line width=1pt,samples=260,domain=%g:%g]{%s};' % (lo, hi, expr))
    # nhãn đường cong: góc trên-phải khung
    cs.append(r'\node[blue,anchor=north east,font=\small] at (axis cs:%g,%g) {$%s$};'
              % (xmax - 0.2, ymax - 0.2, nhan))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)


def tam_giac_toa_do(a=2.0, ten_O='O', ten_A='A', ten_B='B', ten_H='H',
                    nhan_h='h', hien_duong_cao=True, out='tamgiac_td', tra_bytes=False, scale=1.0):
    """TAM GIÁC VUÔNG OAB TRÊN HỆ Oxy (H5.5). O=(0;0), A=(a;0) trên Ox, B=(0;1) trên Oy; vuông tại O.
      Đường cao OH hạ từ O vuông góc xuống cạnh huyền AB, chân H trên AB, OH=h.
      Máy TỰ tính H = foot(O, AB) từ tọa độ (Đ5.9 VERIFY); PHANH: kiểm OH⊥AB + H∈AB."""
    a = float(a)
    assert a > 0, "[tam_giac_toa_do] a phải > 0"
    # H = chân đường vuông góc từ O xuống AB. Đường AB: x + a*y = a  →  H=(a/(1+a^2), a^2/(1+a^2))
    Hx = a / (1 + a * a)
    Hy = a * a / (1 + a * a)
    # PHANH: H thuộc AB (x + a*y = a) và OH ⊥ AB (OH · (B-A) = 0)
    assert abs((Hx + a * Hy) - a) < 1e-9, "[tam_giac] H không thuộc AB"
    assert abs(Hx * (-a) + Hy * 1.0) < 1e-9, "[tam_giac] OH không ⊥ AB"

    # khung vẽ (hiển thị; độ dài nét là HIỂN THỊ không phải dữ liệu — Đ triết lý VERIFY)
    xmax = a + 0.9
    tz = [r'\documentclass[border=8pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g,>=stealth,line join=round]' % scale,
          # trục
          r'\draw[->] (-0.6,0) -- (%g,0) node[below left]{$x$};' % xmax,
          r'\draw[->] (0,-0.5) -- (0,1.7) node[below left]{$y$};',
          # tam giác OAB
          r'\draw[blue,line width=1pt] (0,0) -- (%g,0) -- (0,1) -- cycle;' % a,
          # góc vuông tại O (ô vuông nhỏ — Đ41.1, KHÔNG ghi 90°)
          r'\draw[blue,line width=0.7pt] (0.14,0) -- (0.14,0.14) -- (0,0.14);',
          # điểm + nhãn
          r'\fill (0,0) circle (1.1pt) node[below left]{$%s$};' % ten_O,
          r'\fill (%g,0) circle (1.1pt) node[below]{$%s$};' % (a, ten_A),
          r'\fill (0,1) circle (1.1pt) node[left]{$%s$};' % ten_B]
    if hien_duong_cao:
        # ô vuông góc vuông tại H: 2 cạnh theo hướng H→O (dọc OH) và H→A (dọc AB)
        oh = math.hypot(Hx, Hy); ab = math.hypot(a, 1.0); s = 0.13
        ux, uy = -Hx / oh, -Hy / oh          # H → O
        vx, vy = a / ab, -1.0 / ab           # H → A (dọc AB)
        p1 = (Hx + s * ux, Hy + s * uy)
        p2 = (Hx + s * ux + s * vx, Hy + s * uy + s * vy)
        p3 = (Hx + s * vx, Hy + s * vy)
        tz += [
            # đường cao OH (đứt nét) + chân H
            r'\draw[red,dashed,line width=0.9pt] (0,0) -- (%g,%g);' % (Hx, Hy),
            # ký hiệu góc vuông tại H (OH ⟂ AB)
            r'\draw[red,line width=0.6pt] (%g,%g) -- (%g,%g) -- (%g,%g);' % (p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]),
            r'\fill (%g,%g) circle (1.1pt) node[above right]{$%s$};' % (Hx, Hy, ten_H),
            # nhãn độ dài h đặt giữa OH
            r'\node[red,font=\small] at (%g,%g) {$%s$};' % (Hx * 0.5 - 0.12, Hy * 0.5 + 0.1, nhan_h),
        ]
    tz.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(tz), out, tra_bytes, dpi=200)


def _fmt_tick(v):
    # format mốc trục: 0.5 -> \frac{1}{2}, 1 -> 1, nguyên -> %g
    from fractions import Fraction
    if abs(v - round(v)) < 1e-9:
        return '%g' % round(v)
    fr = Fraction(v).limit_denominator(12)
    return r'\frac{%d}{%d}' % (fr.numerator, fr.denominator)


def do_thi_bac_thang(doan, diem_dac=None, diem_ho=None, nhan_ham=None,
                     xmax=1.3, ymax=1.4, xticks=(0.5, 1.0), yticks=(0.5, 1.0),
                     xtick_lab=None, ytick_lab=None, out='bacthang', tra_bytes=False, scale=3.4):
    """ĐỒ THỊ HÀM BẬC THANG / PIECEWISE-LINEAR (H5.7 — minh họa liên tục/gián đoạn).
       doan: list đoạn thẳng [[(x1,y1),(x2,y2)], ...] — vẽ đường LIỀN từng đoạn (nối trong 1 đoạn).
       diem_dac: [(x,y),...] chấm ĐẶC (điểm thuộc đồ thị). diem_ho: [(x,y),...] vòng RỖNG (điểm KHÔNG thuộc — điểm hở).
       xticks/yticks: mốc chia (số); xtick_lab/ytick_lab: nhãn tường minh (None → tự format phân số đẹp).
       nhan_ham: nhãn hàm (vd r'y=f(x)') góc trên-phải. Máy chỉ VẼ nghĩa đã khai — không tự sinh điểm."""
    diem_dac = diem_dac or []
    diem_ho = diem_ho or []
    xl = xtick_lab or [_fmt_tick(t) for t in xticks]
    yl = ytick_lab or [_fmt_tick(t) for t in yticks]
    tz = [r'\documentclass[border=6pt]{standalone}',
          r'\usepackage{tikz}\usepackage{amsmath}',
          r'\usetikzlibrary{arrows.meta}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g,>={Stealth[length=1.6mm]},line join=round]' % scale,
          # trục
          r'\draw[->] (-0.12,0) -- (%g,0) node[below right]{$x$};' % xmax,
          r'\draw[->] (0,-0.12) -- (0,%g) node[left]{$y$};' % ymax,
          r'\node[below left,font=\footnotesize] at (0,0) {$O$};']
    # mốc trục x
    for t, lab in zip(xticks, xl):
        tz.append(r'\draw (%g,0.02) -- (%g,-0.02) node[below,font=\scriptsize]{$%s$};' % (t, t, lab))
    for t, lab in zip(yticks, yl):
        tz.append(r'\draw (0.02,%g) -- (-0.02,%g) node[left,font=\scriptsize]{$%s$};' % (t, t, lab))
    # đường liền từng đoạn
    for seg in doan:
        pts = ' -- '.join('(%g,%g)' % (x, y) for (x, y) in seg)
        tz.append(r'\draw[blue,line width=1pt] %s;' % pts)
    # điểm đặc
    for (x, y) in diem_dac:
        tz.append(r'\fill[blue] (%g,%g) circle (1.4pt);' % (x, y))
    # điểm hở (vòng tròn rỗng, nền trắng)
    for (x, y) in diem_ho:
        tz.append(r'\draw[blue,line width=0.8pt,fill=white] (%g,%g) circle (1.6pt);' % (x, y))
    if nhan_ham:
        tz.append(r'\node[blue,anchor=south west,font=\small] at (%g,%g) {$%s$};' % (xmax*0.42, ymax-0.18, nhan_ham))
    tz.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(tz), out, tra_bytes, dpi=200)


# ═══════════════════════════════════════════════════════════════════
# [33ze] 2026-10-31 — Ông Bụt Đại số THPT · PILOT DS11_CH09_B31 (Chương IX Đạo hàm)
#   +4 builder hình đạo hàm (H1–H4) — ADDITIVE, KHÔNG đụng 3 hàm cũ (Ch5).
#   Render qua _render_doc_vn: xelatex (fontspec Latin Modern → ĐỦ dấu tiếng Việt) →
#   lùi pdflatex nếu thiếu xelatex. Triết lý VERIFY (Đ5.9): máy tự tính tọa độ/hệ số
#   góc tiếp tuyến từ công thức; KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
#     • tia_so_vi_tri     — tia số vị trí vật, 2 mốc + ngoặc đo (H9.2).
#     • do_thi_cat_tiep   — cung lồi + cát tuyến PQ + tiếp tuyến tại P (H9.3).
#     • cau_parabol_doc   — sơ đồ cầu parabol + độ dốc tại P + chiều cao (H9.5).
#     • parabol_2tiep     — parabol úp + 2 tiếp tuyến nét đứt tại P,Q (H9.6b, BT 9.5).
# ═══════════════════════════════════════════════════════════════════
import subprocess as _sp, os as _os


def _render_doc_vn(body, out, tra_bytes=False, dpi=200):
    """Biên dịch tikzpicture (body) → PNG. Ưu tiên xelatex + Latin Modern (ĐỦ dấu
       tiếng Việt cho nhãn), lùi pdflatex nếu thiếu xelatex (rớt dấu, hình vẫn ra)."""
    libs = (r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}\usepackage{amsmath}'
            r'\usetikzlibrary{arrows.meta,calc,angles,quotes,decorations.pathreplacing}')
    for _e in ('.pdf', '-1.png'):
        try: _os.remove('/tmp/%s%s' % (out, _e))
        except OSError: pass
    xe = (r'\documentclass[border=5pt]{standalone}'
          r'\usepackage{fontspec}\setmainfont{Latin Modern Roman}' + libs +
          r'\begin{document}' + body + r'\end{document}')
    open('/tmp/%s.tex' % out, 'w').write(xe)
    try: _sp.run(['xelatex', '-interaction=nonstopmode', '%s.tex' % out], cwd='/tmp', capture_output=True)
    except (FileNotFoundError, OSError): pass
    if not _os.path.exists('/tmp/%s.pdf' % out):
        pl = (r'\documentclass[border=5pt]{standalone}'
              r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}' + libs +
              r'\begin{document}' + body + r'\end{document}')
        open('/tmp/%s.tex' % out, 'w').write(pl)
        try: _sp.run(['pdflatex', '-interaction=nonstopmode', '%s.tex' % out], cwd='/tmp', capture_output=True)
        except (FileNotFoundError, OSError): pass
    _sp.run(['pdftoppm', '-png', '-r', str(dpi), '%s.pdf' % out, out], cwd='/tmp', capture_output=True)
    png = '/tmp/%s-1.png' % out
    if not _os.path.exists(png):
        return None
    return open(png, 'rb').read() if tra_bytes else png


def tia_so_vi_tri(ten_truc='s', xP=3.0, xQ=7.0, L=9.0,
                  nhan_P=r'Vị trí tại $t_0$', nhan_Q=r'Vị trí tại $t$',
                  nhan_doan=r'$s(t)-s(t_0)$', out='tia_vitri', tra_bytes=False, scale=1.0):
    """TIA SỐ VỊ TRÍ VẬT (H9.2 — minh họa quãng đường đi được từ t0 đến t).
       Trục ngang 'ten_truc', gốc 0, KHÔNG vạch số. 2 mốc vị trí (0<xP<xQ<L, danh nghĩa
       không tỉ lệ) có mũi tên chỉ XUỐNG + nhãn trên; đoạn [P;Q] đo bằng ngoặc dưới
       (nhan_doan). Schematic — không dữ liệu số để PHANH; chỉ kiểm thứ tự mốc."""
    assert 0 < xP < xQ < L, "[tia_so_vi_tri] cần 0<xP<xQ<L"
    b = [r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.4mm]}]' % scale,
         r'\draw[->,line width=0.9pt] (-0.4,0) -- (%g,0) node[below right]{$%s$};' % (L + 0.5, ten_truc),
         r'\node[below,font=\footnotesize] at (0,-0.04) {$0$};',
         r'\fill (%g,0) circle (1.6pt);' % xP,
         r'\fill (%g,0) circle (1.6pt);' % xQ,
         r'\draw[->,line width=0.8pt] (%g,1.15) -- (%g,0.13);' % (xP, xP),
         r'\draw[->,line width=0.8pt] (%g,1.15) -- (%g,0.13);' % (xQ, xQ),
         r'\node[above,align=center,font=\footnotesize] at (%g,1.15) {%s};' % (xP, nhan_P),
         r'\node[above,align=center,font=\footnotesize] at (%g,1.15) {%s};' % (xQ, nhan_Q),
         r'\draw[decorate,decoration={brace,amplitude=5pt,mirror},line width=0.7pt] (%g,-0.42) -- (%g,-0.42);' % (xP, xQ),
         r'\node[below,font=\footnotesize] at (%g,-0.58) {%s};' % ((xP + xQ) / 2.0, nhan_doan),
         r'\end{tikzpicture}']
    return _render_doc_vn('\n'.join(b), out, tra_bytes, dpi=200)


def do_thi_cat_tiep(x0=2.2, xQ=5.0, nhan_P='P', nhan_Q='Q', nhan_tt='t',
                    nhan_ham='y=f(x)', out='cat_tiep', tra_bytes=False, scale=1.0):
    """CÁT TUYẾN & TIẾP TUYẾN (H9.3 — khi Q→P, cát tuyến PQ dần về tiếp tuyến tại P).
       Cung lồi cố định f(x)=-0.18(x-1)(x-7) (máy TỰ tính tọa độ + hệ số góc, Đ5.9).
       P(x0;f(x0)), Q(xQ;f(xQ)), 1<x0<xQ<7. Cát tuyến (đỏ) qua P,Q + tiếp tuyến (teal)
       tại P hệ số góc f'(x0). Gióng đứt x0,x→Ox và f(x0)→Oy. Hình LÝ THUYẾT."""
    f = lambda x: -0.18 * (x - 1) * (x - 7)
    df = lambda x: -0.18 * (2 * x - 8)
    assert 1 < x0 < xQ < 7, "[do_thi_cat_tiep] cần 1<x0<xQ<7 (trong miền cung)"
    y0, yQ = f(x0), f(xQ)
    m = df(x0)
    msec = (yQ - y0) / (xQ - x0)
    b = [r'\begin{tikzpicture}[scale=%g]' % scale,
         r'\begin{axis}[axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
         r'  xlabel={$x$}, ylabel={$y$}, xlabel style={anchor=north west}, ylabel style={anchor=south east},',
         r'  xmin=0, xmax=7.8, ymin=0, ymax=2.0, width=12cm, height=8.4cm,',
         r'  xtick=\empty, ytick=\empty, clip=false,]',
         r'\addplot[blue,line width=1.1pt,samples=200,domain=1:7]{-0.18*(x-1)*(x-7)};',
         r'\node[blue,anchor=south west,font=\small] at (axis cs:5.4,%g){$%s$};' % (f(5.4) + 0.05, nhan_ham),
         r'\addplot[red,line width=0.9pt,domain=%g:%g]{%g*(x-%g)+%g};' % (x0 - 0.6, xQ + 0.8, msec, x0, y0),
         r'\addplot[teal,line width=1.0pt,domain=%g:%g]{%g*(x-%g)+%g};' % (max(0.6, x0 - 1.7), x0 + 2.4, m, x0, y0),
         r'\node[teal,font=\small] at (axis cs:%g,%g){$%s$};' % (x0 + 2.3, m * 2.3 + y0 + 0.07, nhan_tt),
         r'\draw[gray,dashed,line width=0.6pt](axis cs:%g,0)--(axis cs:%g,%g);' % (x0, x0, y0),
         r'\draw[gray,dashed,line width=0.6pt](axis cs:%g,0)--(axis cs:%g,%g);' % (xQ, xQ, yQ),
         r'\draw[gray,dashed,line width=0.6pt](axis cs:0,%g)--(axis cs:%g,%g);' % (y0, x0, y0),
         r'\fill(axis cs:%g,%g)circle(2pt);' % (x0, y0),
         r'\fill(axis cs:%g,%g)circle(2pt);' % (xQ, yQ),
         r'\node[anchor=south east,font=\small]at(axis cs:%g,%g){$%s$};' % (x0, y0 + 0.02, nhan_P),
         r'\node[anchor=south west,font=\small]at(axis cs:%g,%g){$%s$};' % (xQ, yQ + 0.03, nhan_Q),
         r'\node[anchor=north,font=\footnotesize]at(axis cs:%g,0){$x_0$};' % x0,
         r'\node[anchor=north,font=\footnotesize]at(axis cs:%g,0){$x$};' % xQ,
         r'\node[anchor=east,font=\footnotesize]at(axis cs:0,%g){$f(x_0)$};' % y0,
         r'\end{axis}\end{tikzpicture}']
    return _render_doc_vn('\n'.join(b), out, tra_bytes, dpi=200)


def cau_parabol_doc(W=4.0, H=2.0, xP=-2.2, nhan_nua='200 m',
                    nhan_doc=r'Độ dốc tại $P$', nhan_cao='?',
                    ten_A='A', ten_B='B', ten_P='P', out='cau_parabol',
                    tra_bytes=False, scale=1.0):
    """SƠ ĐỒ CẦU VƯỢT PARABOL (H9.5). Cung úp y=H(1-(x/W)^2) nối A(-W,0),B(W,0), đỉnh (0,H).
       P trên cung (xP<0) + tiếp tuyến tại P + cung góc 'độ dốc tại P'; mũi tên đứt '?' từ
       đỉnh xuống nền; nhịp 2 nửa 'nhan_nua'. Máy TỰ tính hệ số góc tiếp tuyến (Đ5.9)."""
    import math
    assert -W < xP < 0, "[cau_parabol_doc] cần -W<xP<0"
    f = lambda x: H * (1 - (x / W) ** 2)
    m = H * (-2 * xP / W ** 2)
    yP = f(xP)
    Lt = 1.25
    dx = Lt / math.hypot(1.0, m)
    th = math.degrees(math.atan(m))
    b = [r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.2mm]}]' % scale,
         r'\draw[line width=0.9pt] (%g,0) -- (%g,0);' % (-W - 0.8, W + 0.8),
         r'\draw[blue,line width=1.2pt,smooth,samples=90,domain=%g:%g] plot (\x,{%g*(1-(\x/%g)^2)});' % (-W, W, H, W),
         r'\fill (%g,0) circle (1.4pt) node[below]{$%s$};' % (-W, ten_A),
         r'\fill (%g,0) circle (1.4pt) node[below]{$%s$};' % (W, ten_B),
         r'\draw[<->,line width=0.6pt] (%g,-0.55) -- (0,-0.55) node[midway,below,font=\footnotesize]{%s};' % (-W, nhan_nua),
         r'\draw[<->,line width=0.6pt] (0,-0.55) -- (%g,-0.55) node[midway,below,font=\footnotesize]{%s};' % (W, nhan_nua),
         r'\fill (%g,%g) circle (1.5pt) node[above left,font=\footnotesize]{$%s$};' % (xP, yP, ten_P),
         r'\draw[red,line width=1pt] (%g,%g) -- (%g,%g);' % (xP - dx, yP - m * dx, xP + dx, yP + m * dx),
         r'\draw[gray,line width=0.6pt] (%g,%g) -- (%g,%g);' % (xP, yP, xP + 1.15, yP),
         r'\draw[red,line width=0.6pt] ([shift={(0.6,0)}]%g,%g) arc (0:%g:0.6);' % (xP, yP, th),
         r'\node[red,font=\footnotesize,anchor=south] at (%g,%g) {%s};' % (xP - 0.1, yP + 0.5, nhan_doc),
         r'\draw[<->,dashed,line width=0.7pt] (0,%g) -- (0,0);' % H,
         r'\node[right,font=\footnotesize] at (0.08,%g) {%s};' % (H / 2.0, nhan_cao),
         r'\end{tikzpicture}']
    return _render_doc_vn('\n'.join(b), out, tra_bytes, dpi=200)


def parabol_2tiep(k=0.22, q=3.6, net='dut', nhan=('L_1', 'L_2'),
                  ten_P='P', ten_Q='Q', out='parabol_2tiep', tra_bytes=False, scale=1.0):
    """PARABOL ÚP + 2 TIẾP TUYẾN NÉT ĐỨT (H9.6b — đường ray tàu lượn, dùng ở BT 9.5).
       y=-k x(x-q): P=O=(0;0), Q=(q;0) trên Ox. L1 tiếp tuyến tại P (dốc lên), L2 tại Q
       (dốc xuống) — nét đứt. Máy TỰ tính hệ số góc tiếp tuyến (Đ5.9). Hình đề KHÔNG lộ
       kết quả: không ghi giá trị số (Đ41.4)."""
    import math
    assert k > 0 and q > 0, "[parabol_2tiep] cần k>0, q>0"
    f = lambda x: -k * x * (x - q)
    mP = -k * (0 - q)      # = k*q  > 0
    mQ = -k * (2 * q - q)  # = -k*q < 0
    peak = f(q / 2.0)
    sty = 'dashed' if net == 'dut' else 'solid'
    b = [r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.2mm]}]' % scale,
         r'\draw[->,line width=0.8pt] (-1.4,0) -- (%g,0) node[below right]{$x$};' % (q + 1.6),
         r'\draw[->,line width=0.8pt] (0,-1.2) -- (0,%g) node[left]{$y$};' % (peak + 0.8),
         r'\draw[blue,line width=1.2pt,smooth,samples=90,domain=%g:%g] plot (\x,{-%g*\x*(\x-%g)});' % (-0.55, q + 0.55, k, q),
         r'\draw[red,%s,line width=0.9pt] (%g,%g) -- (%g,%g);' % (sty, -1.0, -1.0 * mP, 1.0, 1.0 * mP),
         r'\node[red,font=\footnotesize] at (%g,%g) {$%s$};' % (-1.05, -1.0 * mP - 0.12, nhan[0]),
         r'\draw[red,%s,line width=0.9pt] (%g,%g) -- (%g,%g);' % (sty, q - 0.9, -0.9 * mQ, q + 1.3, 1.3 * mQ),
         r'\node[red,font=\footnotesize] at (%g,%g) {$%s$};' % (q + 1.35, 1.3 * mQ - 0.1, nhan[1]),
         r'\fill (0,0) circle (1.6pt) node[below left,font=\footnotesize]{$%s$};' % ten_P,
         r'\fill (%g,0) circle (1.6pt) node[below right,font=\footnotesize]{$%s$};' % (q, ten_Q),
         r'\end{tikzpicture}']
    return _render_doc_vn('\n'.join(b), out, tra_bytes, dpi=200)
