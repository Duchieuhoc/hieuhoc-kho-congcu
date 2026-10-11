# -*- coding: utf-8 -*-
# hinh_ds10_ch06.py — ĐỒ THỊ HÀM SỐ (Đại số 10, Chương VI: Hàm số, Đồ thị và Ứng dụng)
# Generator ĐỘC LẬP (như hinh_ds11_giaitich.py) — KHÔNG đụng file dùng chung / file máy Hình.
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (hệ số a,b,c), máy TỰ dựng đường cong từ công thức (pgfplots),
#   TỰ tính đỉnh / trục đối xứng / giao Ox,Oy / điểm đối xứng — KHÔNG nhập điểm tay, KHÔNG nhúng ảnh SGK (Đ42).
#   Nhãn math-mode (pdflatex-safe): O, x, y, số, I, x=..  — KHÔNG chữ tiếng Việt trong hình.
#
# [33a] 2026-10-05 — PILOT DS10_CH06_B16 (Hàm số bậc hai). OB dựng trước builder parabol (HP Đ5.9).
#   • parabol(a,b,c, ...) — vẽ y=ax^2+bx+c trên Oxy: bề lõm theo dấu a, đỉnh I, trục đối xứng x=-b/2a (đứt nét),
#     giao Ox (nếu Δ≥0), giao Oy (0;c), điểm đối xứng của giao Oy qua trục. PHANH: a≠0; đỉnh/nghiệm trong khung.
import math
import hinh_core as _HC


def _fmt(v):
    return ('%g' % float(v))


def _fmt_toado(v):
    # format 1 toa do cho nhan: nguyen -> %g ; phan so dep (mau <=12) -> \tfrac (gon 1 dong) ; con lai -> thap phan
    from fractions import Fraction
    v = float(v)
    if abs(v - round(v)) < 1e-9:
        return '%g' % round(v)
    fr = Fraction(v).limit_denominator(12)
    if abs(float(fr) - v) < 1e-9:
        sign = '-' if fr.numerator < 0 else ''
        return r'%s\tfrac{%d}{%d}' % (sign, abs(fr.numerator), fr.denominator)
    return ('%g' % v)


def parabol(a, b, c, xmin=None, xmax=None, ymin=None, ymax=None,
            hien_dinh=True, ten_dinh='I', hien_truc=True,
            hien_giao_ox=True, hien_giao_oy=True, diem_doi_xung=True,
            diem_them=None, nhan=None, hien_nhan=True, out='parabol', tra_bytes=False, scale=1.0):
    """DO THI PARABOL y = a x^2 + b x + c  (a!=0) tren he Oxy — pgfplots, may tu dung tu cong thuc.
       May TU tinh: dinh I(-b/2a ; -Delta/4a); truc doi xung x=-b/2a; giao Ox (neu Delta>=0); giao Oy (0;c);
         diem doi xung cua (0;c) qua truc la (-b/a ; c).
       hien_dinh: cham + nhan dinh I.  hien_truc: truc doi xung dut net.
       hien_giao_ox/oy: cham giao diem.  diem_doi_xung: cham diem doi xung cua giao Oy.
       nhan: nhan duong (None->tu sinh).  Khung None->tu om dinh+giao (co the truyen tay cho bai so lon)."""
    a = float(a); b = float(b); c = float(c)
    assert abs(a) > 1e-12, "[parabol] a phai khac 0 (ham bac hai)"
    delta = b * b - 4 * a * c
    xI = -b / (2 * a)
    yI = -delta / (4 * a)
    roots = []
    if delta >= 0:
        sq = math.sqrt(delta)
        roots = sorted([(-b - sq) / (2 * a), (-b + sq) / (2 * a)])
    x_dx = 2 * xI  # diem doi xung cua giao Oy (0;c) qua truc x=xI

    def _y(x):
        return a * x * x + b * x + c

    # ── khung tu dong ──
    interest_x = [0.0, xI, x_dx] + roots
    if xmin is None or xmax is None:
        hw = max(2.4, max(abs(ix - xI) for ix in interest_x) + 1.0)
        hw = min(hw, 7.0)
        if xmin is None:
            xmin = xI - hw
        if xmax is None:
            xmax = xI + hw
    interest_y = [0.0, c, yI, _y(xmin), _y(xmax)]
    if ymin is None or ymax is None:
        lo = min(interest_y); hi = max(interest_y)
        pad = max(0.8, 0.12 * (hi - lo))
        # nới thêm phía ĐỈNH để có chỗ đặt nhãn đỉnh (a>0 đỉnh dưới → nới ymin; a<0 đỉnh trên → nới ymax)
        pad_dinh = 1.15 if hien_dinh else 0.0
        if ymin is None:
            ymin = lo - pad - (pad_dinh if a > 0 else 0.0)
        if ymax is None:
            ymax = hi + pad + (pad_dinh if a < 0 else 0.0)
    # PHANH noi sinh
    assert xmin < xI < xmax, "[parabol] dinh x_I=%g ngoai khung [%g;%g]" % (xI, xmin, xmax)
    assert ymin - 1e-6 <= yI <= ymax + 1e-6, "[parabol] dinh y_I=%g ngoai khung [%g;%g]" % (yI, ymin, ymax)

    expr = r'%s*x^2 + (%s)*x + (%s)' % (_fmt(a), _fmt(b), _fmt(c))
    if nhan is None:
        def _ta():
            if a == 1: return 'x^2'
            if a == -1: return '-x^2'
            return r'%sx^2' % _fmt(a)
        def _tb():
            if b == 0: return ''
            if b == 1: return '+x'
            if b == -1: return '-x'
            return ('+%sx' % _fmt(b)) if b > 0 else ('%sx' % _fmt(b))
        def _tc():
            if c == 0: return ''
            return ('+%s' % _fmt(c)) if c > 0 else ('%s' % _fmt(c))
        nhan = 'y=' + _ta() + _tb() + _tc()

    cs = [r'\documentclass[border=8pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.16}',
          r'\usepackage{amsmath}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g]' % scale,
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis cs:%g,0)}, anchor=south west, inner sep=2pt},' % xmax,
          r'  ylabel style={at={(axis cs:0,%g)}, anchor=south east, inner sep=2pt},' % ymax,
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,',
          r']']
    # truc doi xung dut net (bo neu trung Oy)
    if hien_truc and abs(xI) > 1e-9:
        cs.append(r'\addplot[gray,dashed,line width=0.7pt] coordinates {(%g,%g) (%g,%g)};' % (xI, ymin, xI, ymax))
        # nhan truc dx dat GIUA doan dut (giua dinh va mep xa), nen trang che net dut, lech phai khoi truc tung
        y_lbl = (yI + ymax) / 2.0 if a > 0 else (yI + ymin) / 2.0
        cs.append(r'\node[gray,anchor=west,font=\footnotesize,fill=white,inner sep=1.3pt] at (axis cs:%g,%g) {$x=%s$};'
                  % (xI + 0.15, y_lbl, _fmt_toado(xI)))
    # duong parabol
    cs.append(r'\addplot[blue,line width=1pt,samples=180,domain=%g:%g]{%s};' % (xmin, xmax, expr))
    # giao Oy
    if hien_giao_oy:
        cs.append(r'\addplot[blue,only marks,mark=*,mark size=1.4pt] coordinates {(0,%g)};' % c)
    # diem doi xung cua giao Oy
    if diem_doi_xung and abs(x_dx) > 1e-9:
        cs.append(r'\addplot[blue,only marks,mark=*,mark size=1.4pt] coordinates {(%g,%g)};' % (x_dx, c))
    # giao Ox
    if hien_giao_ox and delta >= 0:
        pts = ' '.join('(%g,0)' % r for r in roots)
        cs.append(r'\addplot[blue,only marks,mark=*,mark size=1.4pt] coordinates {%s};' % pts)
    # diem danh dau them (vd bang gia tri H6.10) — VERIFY: y moi diem phai nam tren parabol
    if diem_them:
        for (px, py) in diem_them:
            assert abs(_y(px) - py) < 1e-6, "[parabol] diem (%g;%g) KHONG thuoc parabol (y=%g)" % (px, py, _y(px))
        dp = ' '.join('(%g,%g)' % (px, py) for (px, py) in diem_them)
        cs.append(r'\addplot[blue,only marks,mark=*,mark size=1.2pt] coordinates {%s};' % dp)
    # dinh I
    if hien_dinh:
        cs.append(r'\addplot[red,only marks,mark=*,mark size=1.6pt] coordinates {(%g,%g)};' % (xI, yI))
        if a > 0:
            anch = 'north'; dy = -0.34
        else:
            anch = 'south'; dy = 0.34
        cs.append(r'\node[red,anchor=%s,font=\footnotesize] at (axis cs:%g,%g) {$%s(%s;\,%s)$};'
                  % (anch, xI, yI + dy, ten_dinh, _fmt_toado(xI), _fmt_toado(yI)))
    # nhan duong cong: dat tren NHANH PHAI o ~70% chieu cao khung (tranh de truc + moc)
    if hien_nhan:
        span = ymax - ymin
        yt = (ymin + 0.70 * span) if a > 0 else (ymax - 0.70 * span)
        disc = b * b - 4 * a * (c - yt)
        if disc > 0:
            xr = (-b + math.sqrt(disc)) / (2 * a)  # nhanh phai (x>xI khi a>0; x<xI khi a<0 -> lay nghiem lon hon)
            xr = max((-b + math.sqrt(disc)) / (2 * a), (-b - math.sqrt(disc)) / (2 * a))
            if xr > xmax - 0.1:
                xr = xmax - 0.1; yt = _y(xr)
            cs.append(r'\node[blue,anchor=east,font=\small] at (axis cs:%g,%g) {$%s$};' % (xr - 0.1, yt, nhan))
        else:
            cs.append(r'\node[blue,anchor=east,font=\small] at (axis cs:%g,%g) {$%s$};' % (xmax - 0.15, yt, nhan))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)


# ═══════════════════════════════════════════════════════════════════════════
# [32p] 2026-10-11 — PILOT DS10_CH06_B17 (Dấu của tam thức bậc hai).
#   BẢNG XÉT DẤU (tikz, chuẩn SGK): dòng x (mốc ±∞ + nghiệm) + dòng f(x) (dấu giữa khoảng, 0/|| tại mốc).
#   bang_xet_dau(moc, dau, ...) TỔNG QUÁT (tam thức / tích / thương — tái dùng giải tích sau).
#   bang_xet_dau_tam_thuc(a,b,c) — máy TỰ tính Δ, nghiệm, dấu từng khoảng (Đ5.9: nhận nghĩa, máy dựng).
# ═══════════════════════════════════════════════════════════════════════════
def bang_xet_dau(moc, dau, ten_ham='f(x)', danh_dau=None,
                 ky_am_vc=r'-\infty', ky_duong_vc=r'+\infty',
                 out='bangxetdau', tra_bytes=False, scale=1.0):
    """BẢNG XÉT DẤU tổng quát (tikz) — chuẩn SGK Việt Nam.
       moc : list NHÃN các mốc (nghiệm) tăng dần, dạng math-string. VD ['-4','1'] · ['x_1','x_2'] · [r'1-\\sqrt2', r'1+\\sqrt2'] · [] (vô nghiệm).
       dau : list dấu MỖI KHOẢNG, len = len(moc)+1, phần tử '+' hoặc '-'.
       danh_dau : list cùng độ dài moc — ký hiệu tại mốc: '0' (nghiệm, f=0 — mặc định) | '||' (không xác định, mẫu=0, kẻ gạch đứng đôi).
       ten_ham : nhãn dòng dưới (vd 'f(x)', 'g(x)', r\"f'(x)\")."""
    n = len(moc)
    assert len(dau) == n + 1, "[bang_xet_dau] dau phai co len = so moc + 1 (so khoang)"
    danh_dau = danh_dau or (['0'] * n)
    assert len(danh_dau) == n, "[bang_xet_dau] danh_dau phai cung do dai moc"
    for d in dau:
        assert d in ('+', '-'), "[bang_xet_dau] dau chi nhan '+' hoac '-'"

    L = 2.1 if ('frac' in ten_ham or '/' in ten_ham) else 1.5   # [32r] nới cột nhãn khi ten_ham là phân số
    iw = 2.0         # bề rộng mỗi khoảng
    yT, yMid, yB = 1.0, 0.0, -1.0
    # vị trí các mốc: x[0]=-∞ ... x[n+1]=+∞
    xs = [L + 0.6 + i * iw for i in range(n + 2)]
    R = xs[-1] + 0.6

    t = [r'\documentclass[border=4pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath,amssymb}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,line join=round]' % scale]
    # khung ngoài + vách ngăn cột nhãn + đường ngang giữa 2 dòng
    t.append(r'\draw[line width=0.8pt] (0,%g) rectangle (%g,%g);' % (yB, R, yT))
    t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (L, yB, L, yT))      # vách cột nhãn
    t.append(r'\draw[line width=0.8pt] (0,%g) -- (%g,%g);' % (yMid, R, yMid))      # ngang giữa
    # nhãn 2 dòng
    t.append(r'\node at (%g,%g) {$x$};' % (L / 2.0, (yMid + yT) / 2.0))
    t.append(r'\node at (%g,%g) {$%s$};' % (L / 2.0, (yB + yMid) / 2.0, ten_ham))
    # dòng x: các mốc
    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[0], (yMid + yT) / 2.0, ky_am_vc))
    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[-1], (yMid + yT) / 2.0, ky_duong_vc))
    for i, lab in enumerate(moc):
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[i + 1], (yMid + yT) / 2.0, lab))
    # tại mỗi mốc nghiệm: gạch đứng xuyên dòng f(x) + ký hiệu (0 / ||)
    yf = (yB + yMid) / 2.0
    for i, mk in enumerate(danh_dau):
        xr = xs[i + 1]
        if mk == '||':
            t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (xr - 0.07, yMid, xr - 0.07, yB))
            t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (xr + 0.07, yMid, xr + 0.07, yB))
        else:
            t.append(r'\draw[line width=0.6pt] (%g,%g) -- (%g,%g);' % (xr, yMid, xr, yB))
            t.append(r'\node[font=\small,fill=white,inner sep=1pt] at (%g,%g) {$%s$};' % (xr, yf, mk))
    # dòng f(x): dấu giữa mỗi khoảng
    for i, d in enumerate(dau):
        xmid = (xs[i] + xs[i + 1]) / 2.0
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xmid, yf, d))
    t.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)


def bang_xet_dau_tam_thuc(a, b, c, ten_ham='f(x)', out='bxd_tamthuc', tra_bytes=False, scale=1.0):
    """BẢNG XÉT DẤU TAM THỨC BẬC HAI f(x)=ax^2+bx+c (a!=0) — máy TỰ tính Δ, nghiệm, dấu (Đ5.9).
       Định lí dấu: Δ<0 -> f cùng dấu a mọi x; Δ=0 -> cùng dấu a, bằng 0 tại nghiệm kép;
                    Δ>0 -> trái dấu a trong (x1;x2), cùng dấu a ngoài."""
    a = float(a); b = float(b); c = float(c)
    assert abs(a) > 1e-12, "[bxd_tamthuc] a phai khac 0"
    delta = b * b - 4 * a * c
    sgn_a = '+' if a > 0 else '-'
    opp_a = '-' if a > 0 else '+'
    if delta < 0:
        return bang_xet_dau([], [sgn_a], ten_ham=ten_ham, out=out, tra_bytes=tra_bytes, scale=scale)
    if abs(delta) < 1e-9:
        x0 = -b / (2 * a)
        return bang_xet_dau([_fmt_toado(x0)], [sgn_a, sgn_a], ten_ham=ten_ham, out=out, tra_bytes=tra_bytes, scale=scale)
    sq = math.sqrt(delta)
    x1, x2 = sorted([(-b - sq) / (2 * a), (-b + sq) / (2 * a)])
    return bang_xet_dau([_fmt_toado(x1), _fmt_toado(x2)], [sgn_a, opp_a, sgn_a],
                        ten_ham=ten_ham, out=out, tra_bytes=tra_bytes, scale=scale)


# ═══════════════════════════════════════════════════════════════════════════
# [32q] 2026-10-11 — PILOT DS10_CH06_B18 (PT quy về bậc hai — HÌNH HỌC MÔ HÌNH HÓA).
#   so_do_hinh(diem, canh, ...) — sơ đồ hình học phẳng TỔNG QUÁT (tikz): điểm + đoạn thẳng
#   + góc vuông + nhãn cạnh/điểm + nửa đường tròn / đường tròn. Cho bài mô hình hóa lập PT.
#   AI Soạn truyền TỌA ĐỘ điểm (tính từ đề) + khai cạnh/nhãn. PHANH: góc vuông khai phải ⟂ thật.
# ═══════════════════════════════════════════════════════════════════════════
def so_do_hinh(diem, canh=None, canh_dut=None, goc_vuong=None,
               nhan_canh=None, nhan_diem=None, nua_tron=None, duong_tron=None,
               nhan_tong=None, diem_cham=None, out='sodohinh', tra_bytes=False, scale=1.0):
    """SƠ ĐỒ HÌNH HỌC PHẲNG (tikz) — bài mô hình hóa (tam giác vuông, tứ giác, nửa tròn+HCN...).
       diem: dict {ten:(x,y)} — tọa độ các điểm (AI Soạn tính từ đề).
       canh: list [(A,B),...] đoạn LIỀN. canh_dut: list [(A,B),...] đoạn ĐỨT (đường phụ).
       goc_vuong: list [(A,V,B),...] — ký hiệu góc vuông tại V (giữa VA, VB). PHANH: VA·VB≈0.
       nhan_canh: {(A,B):'label'} — nhãn độ dài, đặt giữa cạnh lệch ra ngoài (xa trọng tâm).
       nhan_diem: {ten:'huong'} huong∈{above,below,left,right,above left,...}; None→tự theo trọng tâm.
       nua_tron: list [(A,B,'tren'|'duoi'),...] — nửa đường tròn đường kính AB, vòng phía trên/dưới.
       duong_tron: list [(tam,bankinh),...] hoặc [((x,y),r),...] — đường tròn.
       nhan_tong: list [(A,B,'label'),...] — [32r] DẤU NGOẶC ÔM (brace) + nhãn cho ĐOẠN TỔNG qua nhiều điểm
                  (vd B–C chứa M: ghi độ dài tổng BC mà không lẫn đoạn con). Brace đặt phía xa trọng tâm.
       diem_cham: list ten — chấm đậm các điểm này (mặc định chấm hết điểm có trong canh)."""
    import math as _m
    canh = canh or []; canh_dut = canh_dut or []; goc_vuong = goc_vuong or []
    nhan_canh = nhan_canh or {}; nhan_diem = nhan_diem or {}
    nua_tron = nua_tron or []; duong_tron = duong_tron or []; nhan_tong = nhan_tong or []
    P = {k: (float(v[0]), float(v[1])) for k, v in diem.items()}
    # trọng tâm (để lệch nhãn ra ngoài)
    cx = sum(p[0] for p in P.values()) / len(P)
    cy = sum(p[1] for p in P.values()) / len(P)

    # PHANH góc vuông
    for (A, V, B) in goc_vuong:
        ax, ay = P[A]; vx, vy = P[V]; bx, by = P[B]
        u = (ax - vx, ay - vy); w = (bx - vx, by - vy)
        dot = u[0] * w[0] + u[1] * w[1]
        nu = _m.hypot(*u); nw = _m.hypot(*w)
        assert nu > 1e-9 and nw > 1e-9, "[so_do_hinh] góc vuông: điểm trùng " + V
        assert abs(dot) / (nu * nw) < 1e-6, "[so_do_hinh] góc tại %s KHÔNG vuông (cos=%.4f)" % (V, dot / (nu * nw))

    t = [r'\documentclass[border=6pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath}',
         r'\usetikzlibrary{calc,decorations.pathreplacing}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,line join=round,line cap=round]' % scale]
    # đường tròn
    for item in duong_tron:
        tam, r = item
        tx, ty = (P[tam] if isinstance(tam, str) else (float(tam[0]), float(tam[1])))
        t.append(r'\draw[blue,line width=1pt] (%g,%g) circle (%g);' % (tx, ty, float(r)))
    # nửa đường tròn (đường kính AB)
    for (A, B, phia) in nua_tron:
        ax, ay = P[A]; bx, by = P[B]
        mx, my = (ax + bx) / 2.0, (ay + by) / 2.0
        r = _m.hypot(bx - ax, by - ay) / 2.0
        a0 = _m.degrees(_m.atan2(ay - my, ax - mx))
        a1 = _m.degrees(_m.atan2(by - my, bx - mx))
        # chọn chiều quét (±180°) sao cho bụng cung nằm ĐÚNG phía khai (trên/dưới theo y; trái/phải nếu AB dọc)
        doc = abs(by - ay) > abs(bx - ax)
        a1 = a0
        for dirn in (180.0, -180.0):
            midang = _m.radians(a0 + dirn / 2.0)
            xmid = mx + r * _m.cos(midang); ymid = my + r * _m.sin(midang)
            if doc:
                ok = (xmid > mx) if phia in ('phai', 'tren') else (xmid < mx)
            else:
                ok = (ymid > my) if phia == 'tren' else (ymid < my)
            if ok:
                a1 = a0 + dirn; break
        t.append(r'\draw[blue,line width=1pt] (%g,%g) arc (%g:%g:%g);' % (ax, ay, a0, a1, r))
    # cạnh liền
    for (A, B) in canh:
        t.append(r'\draw[blue,line width=1pt] (%g,%g) -- (%g,%g);' % (P[A][0], P[A][1], P[B][0], P[B][1]))
    # cạnh đứt
    for (A, B) in canh_dut:
        t.append(r'\draw[gray,dashed,line width=0.7pt] (%g,%g) -- (%g,%g);' % (P[A][0], P[A][1], P[B][0], P[B][1]))
    # góc vuông (ô vuông nhỏ)
    for (A, V, B) in goc_vuong:
        ax, ay = P[A]; vx, vy = P[V]; bx, by = P[B]
        u = (ax - vx, ay - vy); w = (bx - vx, by - vy)
        nu = _m.hypot(*u); nw = _m.hypot(*w)
        s = 0.28 * min(nu, nw, 1.0 / max(scale, 0.5)) if False else 0.3
        ux, uy = u[0] / nu * s, u[1] / nu * s
        wx, wy = w[0] / nw * s, w[1] / nw * s
        t.append(r'\draw[black,line width=0.6pt] (%g,%g) -- (%g,%g) -- (%g,%g);'
                 % (vx + ux, vy + uy, vx + ux + wx, vy + uy + wy, vx + wx, vy + wy))
    # chấm điểm
    pts_in = set()
    for (A, B) in canh + canh_dut: pts_in.add(A); pts_in.add(B)
    for a, v, b in goc_vuong: pts_in.update([a, v, b])
    cham = diem_cham if diem_cham is not None else list(pts_in)
    for k in cham:
        t.append(r'\fill[blue] (%g,%g) circle (1.6pt);' % (P[k][0], P[k][1]))
    # nhãn điểm (tự hướng ra ngoài trọng tâm nếu không khai)
    for k in P:
        px, py = P[k]
        if k in nhan_diem:
            huong = nhan_diem[k]
        else:
            dx, dy = px - cx, py - cy
            hz = 'right' if dx > 0.3 else ('left' if dx < -0.3 else '')
            vt = 'above' if dy >= 0 else 'below'
            huong = (vt + ' ' + hz).strip()
        t.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};' % (huong, px, py, k))
    # nhãn cạnh (giữa cạnh, lệch ra ngoài)
    for (A, B), lab in nhan_canh.items():
        ax, ay = P[A]; bx, by = P[B]
        mx, my = (ax + bx) / 2.0, (ay + by) / 2.0
        # pháp tuyến
        dx, dy = bx - ax, by - ay
        L = _m.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        # chọn phía xa trọng tâm
        if (mx + nx - cx) ** 2 + (my + ny - cy) ** 2 < (mx - nx - cx) ** 2 + (my - ny - cy) ** 2:
            nx, ny = -nx, -ny
        off = 0.32
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (mx + nx * off, my + ny * off, lab))
    # nhãn-tổng: dấu ngoặc ôm (brace) + nhãn cho đoạn qua nhiều điểm ([32r])
    for (A, B, lab) in nhan_tong:
        ax, ay = P[A]; bx, by = P[B]
        mx, my = (ax + bx) / 2.0, (ay + by) / 2.0
        dx, dy = bx - ax, by - ay
        Ln = _m.hypot(dx, dy); nx, ny = -dy / Ln, dx / Ln
        if (mx + nx - cx) ** 2 + (my + ny - cy) ** 2 < (mx - nx - cx) ** 2 + (my - ny - cy) ** 2:
            nx, ny = -nx, -ny
        braceoff = 0.55
        t.append(r'\draw[decorate,decoration={brace,amplitude=5pt,raise=%gpt},line width=0.6pt] (%g,%g) -- (%g,%g);'
                 % (18 * braceoff, ax, ay, bx, by))
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (mx + nx * (braceoff + 0.45), my + ny * (braceoff + 0.45), lab))
    t.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)


# ═══════════════════════════════════════════════════════════════════════════
# [32r] 2026-10-11 — PILOT DS10_CH06_B15 (Hàm số). do_thi_ghep — ĐỒ THỊ HÀM NHIỀU CÔNG THỨC
#   (nhánh TUYẾN TÍNH và/hoặc PARABOL trên từng khoảng) + điểm đặc/hở tại mút. pgfplots.
# ═══════════════════════════════════════════════════════════════════════════
def do_thi_ghep(nhanh, xmin=None, xmax=None, ymin=None, ymax=None,
                nhan=None, hien_nhan=True, out='dothighep', tra_bytes=False):
    """ĐỒ THỊ HÀM NHIỀU CÔNG THỨC — ghép nhánh tuyến tính / parabol trên từng khoảng.
       nhanh: list dict:
         {'loai':'thang','m':..,'c':..,'tu':x1,'den':x2,'dong_tu':True|False|None,'dong_den':...}
         {'loai':'parabol','a':..,'b':..,'c':..,'tu':x1,'den':x2,'dong_tu':..,'dong_den':..}
       dong_tu/dong_den: True→chấm ĐẶC (điểm thuộc đồ thị); False→vòng RỖNG (điểm hở); None→không chấm (mút ra biên/mũi tên).
       Máy vẽ từng nhánh (pgfplots domain) + chấm điểm tại mút HỮU HẠN. PHANH: parabol a≠0; tu<den."""
    import math as _m
    def val(br, x):
        if br['loai'] == 'thang': return br['m'] * x + br['c']
        return br['a'] * x * x + br['b'] * x + br['c']
    for br in nhanh:
        assert br['loai'] in ('thang', 'parabol'), "[do_thi_ghep] loai phải 'thang'|'parabol'"
        assert br['tu'] < br['den'], "[do_thi_ghep] tu < den"
        if br['loai'] == 'parabol':
            assert abs(br['a']) > 1e-12, "[do_thi_ghep] parabol a≠0"
    # khung tự ôm
    xs_int = []; ys_int = []
    for br in nhanh:
        for x in [br['tu'], br['den']]:
            xs_int.append(x); ys_int.append(val(br, x))
        if br['loai'] == 'parabol':  # thêm đỉnh nếu trong khoảng
            xv = -br['b'] / (2 * br['a'])
            if br['tu'] <= xv <= br['den']:
                xs_int.append(xv); ys_int.append(val(br, xv))
    if xmin is None: xmin = _m.floor(min(xs_int) - 1)
    if xmax is None: xmax = _m.ceil(max(xs_int) + 1)
    if ymin is None: ymin = _m.floor(min(ys_int) - 1)
    if ymax is None: ymax = _m.ceil(max(ys_int) + 1)

    cs = [r'\documentclass[border=4pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.17}',
          r'\usepackage{amsmath}',
          r'\begin{document}', r'\begin{tikzpicture}',
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis cs:%g,0)}, anchor=south west, inner sep=2pt},' % xmax,
          r'  ylabel style={at={(axis cs:0,%g)}, anchor=south east, inner sep=2pt},' % ymax,
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          r'  width=11cm, height=9cm,',
          r'  tick label style={font=\small, fill=white, inner sep=1.3pt},',
          r'  clip=true,', r']']
    # vẽ từng nhánh
    for br in nhanh:
        if br['loai'] == 'thang':
            expr = r'%g*x+%g' % (br['m'], br['c'])
            smp = 2
        else:
            expr = r'%g*x^2+%g*x+%g' % (br['a'], br['b'], br['c'])
            smp = 100
        cs.append(r'\addplot[blue,line width=1.1pt,domain=%g:%g,samples=%d]{%s};'
                  % (br['tu'], br['den'], smp, expr))
    # chấm điểm đặc/hở tại mút hữu hạn
    for br in nhanh:
        for (x, key) in [(br['tu'], 'dong_tu'), (br['den'], 'dong_den')]:
            flag = br.get(key, None)
            if flag is None: continue
            y = val(br, x)
            if flag:
                cs.append(r'\addplot[blue,mark=*,only marks,mark size=1.6pt]coordinates{(%g,%g)};' % (x, y))
            else:
                cs.append(r'\addplot[blue,mark=o,only marks,mark size=1.8pt,mark options={fill=white,line width=0.8pt}]coordinates{(%g,%g)};' % (x, y))
    # nhãn đường
    if hien_nhan and nhan:
        cs.append(r'\node[blue,anchor=south west,font=\small] at (axis cs:%g,%g) {$%s$};'
                  % (xmin + 0.2, ymax - 0.5, nhan))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)


# ═══════════════════════════════════════════════════════════════════════════
# [32s] 2026-10-11 — DS10_CH06 ⑤/⑥. do_thi_nhan_dang — ĐỒ THỊ NHẬN DẠNG trên Oxy
#   (đường tròn / hyperbol ngang / y=√x) cho bài "hình nào là đồ thị hàm số?".
# ═══════════════════════════════════════════════════════════════════════════
def do_thi_nhan_dang(loai, cx=0.0, cy=0.0, r=3.0, a=1.0, b=1.0, h=0.0, k=0.0,
                     xmin=None, xmax=None, ymin=None, ymax=None, nhan=None,
                     out='nhandang', tra_bytes=False):
    """ĐỒ THỊ NHẬN DẠNG (pgfplots) — vẽ 1 đường cong trên Oxy để hỏi "có là đồ thị hàm số?".
       loai='tron'          : đường tròn tâm (cx;cy) bán kính r (mỗi x→2 y: KHÔNG là hàm số).
       loai='hyperbol_ngang': x²/a² − y²/b² = 1, 2 nhánh mở TRÁI-PHẢI, đỉnh (±a;0) (KHÔNG là hàm số).
       loai='can'           : y = k + √(x − h) (nhánh x≥h, LÀ hàm số; vd y=√x: h=k=0).
       Máy vẽ + khung tự ôm. Dùng ở bài nhận-dạng (SBT 6.4, Cuối chương 6.34)."""
    import math as _m
    if loai == 'tron':
        if xmin is None: xmin = _m.floor(cx - r - 1); xmax = _m.ceil(cx + r + 1)
        if ymin is None: ymin = _m.floor(cy - r - 1); ymax = _m.ceil(cy + r + 1)
    elif loai == 'hyperbol_ngang':
        if xmin is None: xmin = -_m.ceil(3 * a + 1); xmax = _m.ceil(3 * a + 1)
        if ymin is None: ymin = -8; ymax = 8
    else:  # can
        if xmin is None: xmin = _m.floor(h - 1); xmax = _m.ceil(h + 9)
        if ymin is None: ymin = -1; ymax = _m.ceil(k + _m.sqrt(max(xmax - h, 0)) + 1)
    cs = [r'\documentclass[border=4pt]{standalone}',
          r'\usepackage{pgfplots}\pgfplotsset{compat=1.17}',
          r'\usepackage{amsmath}', r'\begin{document}', r'\begin{tikzpicture}',
          r'\begin{axis}[',
          r'  axis lines=middle, axis line style={-{Stealth[length=2mm]}},',
          r'  xlabel={$x$}, ylabel={$y$},',
          r'  xlabel style={at={(axis cs:%g,0)}, anchor=south west, inner sep=2pt},' % xmax,
          r'  ylabel style={at={(axis cs:0,%g)}, anchor=south east, inner sep=2pt},' % ymax,
          r'  xmin=%g, xmax=%g, ymin=%g, ymax=%g,' % (xmin, xmax, ymin, ymax),
          (r'  axis equal image, ' if loai == 'tron' else r'  width=10cm, height=9cm, ') +
          r'tick label style={font=\small, fill=white, inner sep=1.3pt}, clip=true,', r']']
    if loai == 'tron':
        cs.append(r'\draw[blue,line width=1.1pt] (axis cs:%g,%g) circle [radius=%g];' % (cx, cy, r))
    elif loai == 'hyperbol_ngang':
        # nhánh phải x=a*cosh t, y=b*sinh t ; nhánh trái x=-a*cosh t
        cs.append(r'\addplot[blue,line width=1.1pt,domain=-2.1:2.1,samples=80,variable=\t]({%g*cosh(\t)},{%g*sinh(\t)});' % (a, b))
        cs.append(r'\addplot[blue,line width=1.1pt,domain=-2.1:2.1,samples=80,variable=\t]({-%g*cosh(\t)},{%g*sinh(\t)});' % (a, b))
    else:  # can: y=k+sqrt(x-h)
        cs.append(r'\addplot[blue,line width=1.1pt,domain=%g:%g,samples=100]{%g+sqrt(x-(%g))};' % (h, xmax, k, h))
    if nhan:
        cs.append(r'\node[blue,anchor=north east,font=\small] at (axis cs:%g,%g) {$%s$};' % (xmax - 0.2, ymax - 0.3, nhan))
    cs.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes, dpi=200)
