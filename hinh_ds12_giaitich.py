# -*- coding: utf-8 -*-
# hinh_ds12_giaitich.py — GIẢI TÍCH 12 (Chương I: Ứng dụng đạo hàm để khảo sát & vẽ đồ thị hàm số)
# Generator ĐỘC LẬP (như hinh_ds10_ch06.py / hinh_ds11_giaitich.py) — KHÔNG đụng file dùng chung / file máy khác.
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (mốc + dấu đạo hàm + giá trị), máy TỰ dựng mũi tên ↗↘ (đồng/nghịch biến),
#   TỰ đặt giá trị cực trị / giới hạn LÊN TRÊN hay XUỐNG DƯỚI theo dấu y' — KHÔNG vẽ mũi tên tay.
#   Nhãn math-mode (pdflatex-safe): x, y, số, \infty, \tfrac, e^{...} — KHÔNG chữ tiếng Việt trong hình.
#   KHÔNG nhúng ảnh SGK (Đ42). Render qua hinh_core.render_tikz_doc (pdflatex + pdftoppm).
#
# [32z] 2026-10-16 — ĐƯỜNG GĂNG DS12_CH01 (Ứng dụng đạo hàm). OB dựng builder BẢNG BIẾN THIÊN (HP Đ5.9).
#   Dựng trên HEAD tươi [32y] SHA 3e92eaf (clone chống lệch pha §2; module Hình hh12 additive không ảnh hưởng).
import math
import hinh_core as _HC


def _fmt_toado(v):
    """format 1 số → nhãn toán: nguyên %g · phân số mẫu≤12 → \\tfrac · còn lại thập phân."""
    from fractions import Fraction
    v = float(v)
    if abs(v - round(v)) < 1e-9:
        return '%g' % round(v)
    fr = Fraction(v).limit_denominator(12)
    if abs(float(fr) - v) < 1e-9:
        sign = '-' if fr.numerator < 0 else ''
        return r'%s\tfrac{%d}{%d}' % (sign, abs(fr.numerator), fr.denominator)
    return ('%g' % v)


# ═══════════════════════════════════════════════════════════════════════════
# [32z] bang_bien_thien — BẢNG BIẾN THIÊN (BBT) tổng quát, chuẩn SGK Giải tích 12.
#   Máy nhận (mốc x · dấu y' mỗi khoảng · giá trị y mỗi cột) → TỰ dựng: mũi tên ↗ (y'>0) / ↘ (y'<0),
#   TỰ đặt giá trị LÊN/XUỐNG theo dấu (cực đại ở trên, cực tiểu ở dưới), vạch đôi ‖ ở tiệm cận đứng.
# ═══════════════════════════════════════════════════════════════════════════
def bang_bien_thien(moc, dau, gia_tri, danh_dau=None,
                    ten_bien='x', ten_dh="y'", ten_ham='y',
                    ky_am_vc=r'-\infty', ky_duong_vc=r'+\infty',
                    bar_trai=False, bar_phai=False,
                    out='bangbienthien', tra_bytes=False, scale=1.0):
    r"""BẢNG BIẾN THIÊN (BBT) tổng quát — chuẩn SGK Giải tích 12 (tikz). Máy TỰ dựng mũi tên + đặt giá trị (Đ5.9).
       moc      : list NHÃN mốc x tăng dần (math-string). VD ['-1','3'] · ['-1','0','1'] · [r'e^{-\frac12}'] · [] (đơn điệu).
       dau      : list dấu y' MỖI KHOẢNG, len = len(moc)+1, '+' (đồng biến ↗) hoặc '-' (nghịch biến ↘).
       gia_tri  : list giá trị y tại các cột [-∞, mốc_1, …, mốc_n, +∞], len = len(moc)+2 (math-string).
                  • Cột thường: 1 nhãn, vd '34' · r'-\infty' · r'-\tfrac12'.
                  • Cột TIỆM CẬN ĐỨNG (danh_dau='||'): list 2 nhãn [giới-hạn-TRÁI, giới-hạn-PHẢI], vd [r'-\infty', r'+\infty'].
       danh_dau : list cùng độ dài moc: '0' (y'=0, cực trị — MẶC ĐỊNH) | '||' (TCĐ, y' không xác định — kẻ vạch đôi).
       ten_dh   : nhãn dòng 2 (đạo hàm): "y'", "f'(x)", "S'(x)". ten_ham: nhãn dòng 3: 'y', 'f(x)', 'V'.
       ky_am_vc / ky_duong_vc : nhãn mốc ngoài cùng (mặc định ±∞). Hàm trên khoảng/đoạn: đặt '0', 'a', '-1'…
       bar_trai / bar_phai    : True → kẻ vạch biên tại mốc ngoài trái/phải (GTLN–GTNN trên đoạn [a;b]:
                                y' không xác định tại hai đầu mút nhưng y có giá trị hữu hạn). VD1 B02: bar_trai+bar_phai.
       PHANH: len(dau)==len(moc)+1 ; len(gia_tri)==len(moc)+2 ; mỗi cột '||' phải cấp list 2 phần tử."""
    n = len(moc)
    assert len(dau) == n + 1, "[BBT] dau phai co len = so moc + 1 (so khoang)"
    assert len(gia_tri) == n + 2, "[BBT] gia_tri phai co len = so moc + 2 (so cot)"
    danh_dau = danh_dau or (['0'] * n)
    assert len(danh_dau) == n, "[BBT] danh_dau phai cung do dai moc"
    for d in dau:
        assert d in ('+', '-'), "[BBT] dau chi nhan '+' hoac '-'"
    for j, mk in enumerate(danh_dau):
        if mk == '||':
            assert isinstance(gia_tri[j + 1], (list, tuple)) and len(gia_tri[j + 1]) == 2, \
                "[BBT] cot TCD (||) phai cap list 2 nhan [gh_trai, gh_phai] tai gia_tri[%d]" % (j + 1)

    # mức dọc trong dòng y: '+' → đi từ ĐÁY (B) lên ĐỈNH (T); '-' → từ T xuống B
    yHi, yLo = 0.55, -1.05
    def startY(i): return yLo if dau[i] == '+' else yHi   # mức đầu khoảng i
    def endY(i):   return yHi if dau[i] == '+' else yLo   # mức cuối khoảng i

    # hình học bảng
    L = 1.6                      # bề rộng cột nhãn (x / y' / y)
    iw = 2.5                     # bề rộng mỗi khoảng
    yX_T, yX_B = 2.15, 1.55      # dòng x (trên)
    yD_T, yD_B = 1.55, 0.95      # dòng y' (giữa)
    yY_T, yY_B = 0.95, -1.55     # dòng y (dưới, cao để chứa mũi tên)
    xs = [L + 0.9 + i * iw for i in range(n + 2)]
    R = xs[-1] + 0.9
    cX = (yX_T + yX_B) / 2.0
    cD = (yD_T + yD_B) / 2.0
    BAR = 0.07                   # nửa khoảng cách vạch đôi ‖
    OFF = 0.42                   # lùi mũi tên khỏi node giá trị

    t = [r'\documentclass[border=4pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath,amssymb}',
         r'\usepackage[T1]{fontenc}\usepackage{newunicodechar}\newunicodechar{Đ}{\text{\DJ}}\newunicodechar{đ}{\text{\dj}}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,line join=round,>={Stealth[length=5pt]}]' % scale]
    # khung ngoài + vách cột nhãn + 2 đường ngang
    t.append(r'\draw[line width=0.8pt] (0,%g) rectangle (%g,%g);' % (yY_B, R, yX_T))
    t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (L, yY_B, L, yX_T))
    t.append(r'\draw[line width=0.8pt] (0,%g) -- (%g,%g);' % (yX_B, R, yX_B))   # x | y'
    t.append(r'\draw[line width=0.8pt] (0,%g) -- (%g,%g);' % (yD_B, R, yD_B))   # y' | y
    # nhãn 3 dòng
    t.append(r'\node at (%g,%g) {$%s$};' % (L / 2.0, cX, ten_bien))
    t.append(r'\node at (%g,%g) {$%s$};' % (L / 2.0, cD, ten_dh))
    t.append(r'\node at (%g,%g) {$%s$};' % (L / 2.0, (yY_T + yY_B) / 2.0, ten_ham))
    # dòng x: -∞ , các mốc , +∞
    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[0], cX, ky_am_vc))
    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[-1], cX, ky_duong_vc))
    for i, lab in enumerate(moc):
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xs[i + 1], cX, lab))
    # dòng y': dấu giữa mỗi khoảng
    for i, d in enumerate(dau):
        xmid = (xs[i] + xs[i + 1]) / 2.0
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (xmid, cD, d))
    # tại mỗi mốc: dòng y' ghi '0' hoặc vạch đôi ‖ ; vạch ‖ xuyên cả dòng y
    for j, mk in enumerate(danh_dau):
        xr = xs[j + 1]
        if mk == '||':
            for dx in (-BAR, BAR):
                t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (xr + dx, yD_T, xr + dx, yY_B))
        else:
            t.append(r'\node[font=\small] at (%g,%g) {$0$};' % (xr, cD))
    # vạch biên ngoài (GTLN-NN trên đoạn/nửa khoảng: y' không xác định tại đầu mút)
    if bar_trai:
        for dx in (-BAR, BAR):
            t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (xs[0] + dx, yD_T, xs[0] + dx, yY_B))
    if bar_phai:
        for dx in (-BAR, BAR):
            t.append(r'\draw[line width=0.8pt] (%g,%g) -- (%g,%g);' % (xs[-1] + dx, yD_T, xs[-1] + dx, yY_B))
    # dòng y: mũi tên mỗi khoảng (lùi khỏi node + né vạch ‖)
    _bars = [xs[j + 1] for j, m in enumerate(danh_dau) if m == '||']
    for i in range(n + 1):
        xA, xB = xs[i], xs[i + 1]
        # né vạch ‖: cột i là vạch (||/biên trái) → xuất phát bên PHẢI; cột i+1 là vạch (||/biên phải) → kết thúc bên TRÁI
        aL = (xs[i] in _bars) or (i == 0 and bar_trai)
        bR = (xs[i + 1] in _bars) or (i + 1 == n + 1 and bar_phai)
        x1 = xA + (BAR + 0.12 if aL else OFF)
        x2 = xB - (BAR + 0.12 if bR else OFF)
        t.append(r'\draw[->,line width=0.9pt] (%g,%g) -- (%g,%g);' % (x1, startY(i), x2, endY(i)))

    # đặt node giá trị y tại từng cột
    def put(x, y, lab):
        t.append(r'\node[font=\small,fill=white,inner sep=1.5pt] at (%g,%g) {$%s$};' % (x, y, lab))
    # cột 0 (-∞): mức = startY(0) ; nếu có vạch biên trái → dịch giá trị sang phải vạch
    put(xs[0] + (BAR + 0.30 if bar_trai else 0.0), startY(0), gia_tri[0])
    # cột n+1 (+∞): mức = endY(n) ; nếu có vạch biên phải → dịch sang trái vạch
    put(xs[-1] - (BAR + 0.30 if bar_phai else 0.0), endY(n), gia_tri[-1])
    # cột trong (1..n)
    for j in range(1, n + 1):
        mk = danh_dau[j - 1]
        xr = xs[j]
        if mk == '||':
            gl, gr = gia_tri[j]
            put(xr - (BAR + 0.30), endY(j - 1), gl)     # giới hạn TRÁI (cuối khoảng j-1)
            put(xr + (BAR + 0.30), startY(j), gr)       # giới hạn PHẢI (đầu khoảng j)
        else:
            # cực trị: mức = endY(j-1) (khớp startY(j) nếu đổi dấu); lệch dấu (uốn) → giữa
            lv = endY(j - 1) if endY(j - 1) == startY(j) else 0.5 * (yHi + yLo)
            put(xr, lv, gia_tri[j])

    t.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)


# ═══════════════════════════════════════════════════════════════════════════
# [33a] do_thi_khao_sat — ĐỒ THỊ KHẢO SÁT HÀM SỐ, chuẩn SGK Giải tích 12 (pgfplots).
#   Máy nhận BIỂU THỨC f(x) + các NHÁNH domain + tiệm cận (đứng/ngang/xiên) + điểm đặc biệt
#   → TỰ plot đường cong mượt (restrict y to domain cắt sạch tại TCĐ, KHÔNG đường dọc giả),
#   TỰ vẽ tiệm cận nét đứt, chấm + nhãn điểm đặc biệt (cực trị · tâm đối xứng · giao trục).
#   Phủ 3 dạng Bài 4: bậc ba · phân thức b1/b1 (2 nhánh hyperbol + TCN) · phân thức b2/b1 (TCĐ + TCX).
# ═══════════════════════════════════════════════════════════════════════════
def do_thi_khao_sat(ham, nhanh=None, tcd=None, tcn=None, tcx=None,
                    diem=None, xmin=-5, xmax=5, ymin=-5, ymax=5,
                    xtick=None, ytick=None, xticklabels=None, yticklabels=None,
                    mau='blue', samples=300, width=8.0, height=8.0,
                    out='dothikhaosat', tra_bytes=False, scale=1.0):
    r"""ĐỒ THỊ KHẢO SÁT HÀM SỐ — chuẩn SGK Giải tích 12 (pgfplots). Máy TỰ plot + vẽ tiệm cận + đặt điểm (Đ5.9).
       ham       : BIỂU THỨC f(x) cú pháp pgfplots theo biến x (KHÔNG \x). VD '-x^3+3*x^2-4' · '(x+1)/(x-2)'
                   · 'x+1+1/(x-2)' (viết dạng tách để qua TCX cho đẹp). Phép: + - * / ^ , hàm sqrt(), abs()…
       nhanh     : list KHOẢNG domain (a,b) để plot. None → một nhánh [(xmin,xmax)] (hàm bậc ba liền mạch).
                   Hàm có TCĐ tại x=c → tách 2 nhánh né c, VD [(-5, 1.6),(2.4, 5)] cho TCĐ x=2 (lùi ~0.4).
       tcd       : list x (số) → TIỆM CẬN ĐỨNG, đường dọc nét đứt xám + nhãn 'x=<x>' trên đỉnh. None→không.
       tcn       : list y (số) → TIỆM CẬN NGANG, đường ngang nét đứt + nhãn 'y=<y>' bên phải. None→không.
       tcx       : list (a,b) → TIỆM CẬN XIÊN y=a·x+b, đường xiên nét đứt phủ cả view + nhãn. None→không.
       diem      : list dict điểm đặc biệt {xy:(x,y), nhan:'', noi?:'above right', mo?:False}.
                   mo=True → điểm rỗng (vòng tròn không tô, dùng cho điểm giới hạn/không thuộc). noi: vị trí nhãn.
       xtick/ytick       : list số hiện vạch+số trên trục. None → pgfplots tự chọn (nên khai theo nguồn).
       xticklabels/...   : list NHÃN math thay số (khớp thứ tự xtick), cho mốc phân số/vô tỉ. VD [r'\tfrac{2}{3}'].
       width/height      : cỡ khung (cm). PHANH: len(xticklabels)==len(xtick) nếu khai; mỗi nhánh (a,b) có a<b."""
    nhanh = nhanh or [(xmin, xmax)]
    for (a, b) in nhanh:
        assert a < b, "[DOTHI] moi nhanh (a,b) phai co a<b"
    if xticklabels is not None:
        assert xtick is not None and len(xticklabels) == len(xtick), "[DOTHI] xticklabels phai khop xtick"
    if yticklabels is not None:
        assert ytick is not None and len(yticklabels) == len(ytick), "[DOTHI] yticklabels phai khop ytick"

    def _ticks(vals, labs):
        if vals is None:
            return ''
        tk = 'xtick={%s}' if False else None
        s = '{%s}' % ','.join('%g' % v for v in vals)
        if labs is None:
            return s, None
        ls = '{%s}' % ','.join('$%s$' % l for l in labs)
        return s, ls

    opt = [r'axis lines=middle', r'axis line style={-{Stealth[length=6pt]}}',
           r'xlabel={$x$}', r'ylabel={$y$}',
           r'x label style={at={(ticklabel* cs:1.0)},anchor=west}',
           r'y label style={at={(ticklabel* cs:1.0)},anchor=south}',
           r'xmin=%g' % xmin, r'xmax=%g' % xmax, r'ymin=%g' % ymin, r'ymax=%g' % ymax,
           r'restrict y to domain=%g:%g' % (ymin - 0.5, ymax + 0.5),
           r'samples=%d' % samples, r'width=%gcm' % width, r'height=%gcm' % height,
           r'tick label style={font=\footnotesize}', r'clip=true',
           r'enlargelimits=false']
    if xtick is not None:
        opt.append(r'xtick={%s}' % ','.join('%g' % v for v in xtick))
        if xticklabels is not None:
            opt.append(r'xticklabels={%s}' % ','.join('$%s$' % l for l in xticklabels))
    else:
        opt.append(r'xtick=\empty')
    if ytick is not None:
        opt.append(r'ytick={%s}' % ','.join('%g' % v for v in ytick))
        if yticklabels is not None:
            opt.append(r'yticklabels={%s}' % ','.join('$%s$' % l for l in yticklabels))
    else:
        opt.append(r'ytick=\empty')

    t = [r'\documentclass[border=5pt]{standalone}',
         r'\usepackage{pgfplots}\pgfplotsset{compat=1.18}',
         r'\usepackage{amsmath,amssymb}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g]' % scale,
         r'\begin{axis}[%s]' % (',\n  '.join(opt))]

    # TIỆM CẬN (vẽ trước, nằm dưới đường cong) — nét đứt xám
    if tcd:
        for c in tcd:
            t.append(r'\draw[gray,dashed,thick] (axis cs:%g,%g) -- (axis cs:%g,%g);' % (c, ymin, c, ymax))
            t.append(r'\node[gray,font=\footnotesize,anchor=south] at (axis cs:%g,%g) {$x=%g$};' % (c, ymax, c))
    if tcn:
        for c in tcn:
            t.append(r'\draw[gray,dashed,thick] (axis cs:%g,%g) -- (axis cs:%g,%g);' % (xmin, c, xmax, c))
            t.append(r'\node[gray,font=\footnotesize,anchor=east] at (axis cs:%g,%g) {$y=%g$};' % (xmax, c, c))
    if tcx:
        for (a, b) in tcx:
            t.append(r'\addplot[gray,dashed,thick,domain=%g:%g,samples=2]{%g*x+%g};' % (xmin, xmax, a, b))

    # ĐƯỜNG CONG — mỗi nhánh một addplot
    for (a, b) in nhanh:
        t.append(r'\addplot[%s,very thick,domain=%g:%g]{%s};' % (mau, a, b, ham))

    # ĐIỂM ĐẶC BIỆT — chấm + nhãn (trên cùng)
    if diem:
        for d in diem:
            x0, y0 = d['xy']
            noi = d.get('noi', 'above right')
            nhan = d.get('nhan', '')
            if d.get('mo'):
                t.append(r'\draw[%s,thick,fill=white] (axis cs:%g,%g) circle (2pt);' % (mau, x0, y0))
            else:
                t.append(r'\fill[%s] (axis cs:%g,%g) circle (2pt);' % (mau, x0, y0))
            if nhan:
                t.append(r'\node[font=\footnotesize,anchor=%s] at (axis cs:%g,%g) {$%s$};'
                         % (_anchor(noi), x0, y0, nhan))

    # gốc O
    t.append(r'\node[font=\footnotesize,anchor=north east] at (axis cs:0,0) {$O$};')
    t.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)


def _anchor(noi):
    """đổi 'above right' → anchor 'south west' (nhãn nằm trên-phải điểm ⇒ neo góc dưới-trái)."""
    m = {'above': 'south', 'below': 'north', 'left': 'east', 'right': 'west',
         'above right': 'south west', 'above left': 'south east',
         'below right': 'north west', 'below left': 'north east'}
    return m.get(noi, 'south west')


def to_mien(ham, a, b, ham2=None, nhan_ham=None, nhan_ham2=None,
            xmin=-1.0, xmax=5.0, ymin=-1.0, ymax=6.0,
            mau='blue', mau2='red!70!black', mau_to='blue!12',
            nhan_can=('a', 'b'), hien_can=True,
            nhan_mien=None, nhan_mien_xy=None, nhan_pos=0.55,
            xtick=None, xticklabels=None, ytick=None, yticklabels=None,
            samples=200, width=8.0, height=7.0,
            out='tomien', tra_bytes=False, scale=1.0):
    r"""TÔ MIỀN DIỆN TÍCH tích phân (pgfplots) — chuẩn SGK Giải tích 12 (Bài 12 hình thang cong · Bài 13 diện tích).
       ham   : f(x) cú pháp pgfplots theo biến x (KHÔNG \x). VD 'x^2' · '-x^2+4*x' · 'sqrt(x)'. Phép + - * / ^, sqrt(), abs()…
       a,b   : cận tích phân (số, a<b). Miền tô + CẠNH DỌC tại x=a, x=b tự vẽ (viền miền).
       ham2  : g(x) → tô miền KẸP giữa hai đường cong f,g (fill between). None → tô hình thang cong xuống trục Ox.
       nhan_ham/nhan_ham2 : nhãn math đặt dọc đường cong (vd 'y=f(x)'); None → không nhãn.
       nhan_can : (nhãn_a, nhãn_b) math-string hiện dưới trục Ox tại x=a,x=b (vd ('0','2') hoặc ('a','b')). hien_can=False → ẩn.
       nhan_mien : nhãn trong miền tô (vd 'S', 'S_1'); CẦN nhan_mien_xy=(x,y) để đặt, None → không nhãn miền.
       xtick/ytick + labels : như do_thi_khao_sat (None → ẩn vạch, chỉ hiện nhãn cận).
       PHANH: a<b; nếu khai nhan_mien phải kèm nhan_mien_xy."""
    assert a < b, "[TOMIEN] can a<b"
    if nhan_mien is not None:
        assert nhan_mien_xy is not None, "[TOMIEN] nhan_mien can kem nhan_mien_xy=(x,y)"

    opt = [r'axis lines=middle', r'axis line style={-{Stealth[length=6pt]}}',
           r'xlabel={$x$}', r'ylabel={$y$}',
           r'x label style={at={(ticklabel* cs:1.0)},anchor=west}',
           r'y label style={at={(ticklabel* cs:1.0)},anchor=south}',
           r'xmin=%g' % xmin, r'xmax=%g' % xmax, r'ymin=%g' % ymin, r'ymax=%g' % ymax,
           r'restrict y to domain=%g:%g' % (ymin - 0.5, ymax + 0.5),
           r'samples=%d' % samples, r'width=%gcm' % width, r'height=%gcm' % height,
           r'tick label style={font=\footnotesize}', r'clip=true', r'enlargelimits=false']
    if xtick is not None:
        opt.append(r'xtick={%s}' % ','.join('%g' % v for v in xtick))
        if xticklabels is not None:
            opt.append(r'xticklabels={%s}' % ','.join('$%s$' % l for l in xticklabels))
    else:
        opt.append(r'xtick=\empty')
    if ytick is not None:
        opt.append(r'ytick={%s}' % ','.join('%g' % v for v in ytick))
        if yticklabels is not None:
            opt.append(r'yticklabels={%s}' % ','.join('$%s$' % l for l in yticklabels))
    else:
        opt.append(r'ytick=\empty')

    t = [r'\documentclass[border=5pt]{standalone}',
         r'\usepackage{pgfplots}\pgfplotsset{compat=1.18}',
         r'\usepgfplotslibrary{fillbetween}',
         r'\usepackage{amsmath,amssymb}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g]' % scale,
         r'\begin{axis}[%s]' % (',\n  '.join(opt))]

    if ham2 is None:
        # Hình thang cong: tô giữa f và trục Ox trên [a;b] (viền miền có cạnh dọc tại a,b).
        t.append(r'\addplot[draw=%s!60!black,fill=%s,domain=%g:%g,samples=%d] {%s} \closedcycle;'
                 % (mau, mau_to, a, b, samples, ham))
    else:
        # Miền kẹp giữa f (trên) và g (dưới) trên [a;b] — fill between.
        t.append(r'\addplot[name path=TM_f,draw=none,domain=%g:%g,samples=%d] {%s};' % (a, b, samples, ham))
        t.append(r'\addplot[name path=TM_g,draw=none,domain=%g:%g,samples=%d] {%s};' % (a, b, samples, ham2))
        t.append(r'\addplot[%s] fill between[of=TM_f and TM_g];' % mau_to)

    # Đường cong f (vẽ trọn view cho ngữ cảnh) + nhãn dọc đường (pos vừa phải, kẹp trong khung)
    lab_f = (r' node[pos=%g,anchor=south east,font=\footnotesize,fill=white,inner sep=1pt]{$%s$}'
             % (nhan_pos, nhan_ham)) if nhan_ham else ''
    t.append(r'\addplot[%s,very thick,domain=%g:%g] {%s}%s;' % (mau, xmin, xmax, ham, lab_f))
    if ham2 is not None:
        lab_g = (r' node[pos=%g,anchor=north west,font=\footnotesize,fill=white,inner sep=1pt]{$%s$}'
                 % (nhan_pos, nhan_ham2)) if nhan_ham2 else ''
        t.append(r'\addplot[%s,very thick,domain=%g:%g] {%s}%s;' % (mau2, xmin, xmax, ham2, lab_g))

    # Cạnh dọc + nhãn cận trên trục Ox (bỏ cạnh dọc khi cận trùng trục Oy x=0)
    if hien_can:
        for x0, lab in ((a, nhan_can[0]), (b, nhan_can[1])):
            if abs(x0) > 1e-6:
                t.append(r'\draw[gray,dashed,thick] (axis cs:%g,%g) -- (axis cs:%g,%g);' % (x0, ymin, x0, ymax))
            anc = 'north east' if abs(x0) < 1e-6 else 'north'
            t.append(r'\node[font=\footnotesize,anchor=%s] at (axis cs:%g,0) {$%s$};' % (anc, x0, lab))

    # Nhãn miền
    if nhan_mien is not None:
        mx, my = nhan_mien_xy
        t.append(r'\node[font=\small] at (axis cs:%g,%g) {$%s$};' % (mx, my, nhan_mien))

    t.append(r'\node[font=\footnotesize,anchor=north east] at (axis cs:0,0) {$O$};')
    t.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)


def khoi_tron_xoay(ham, a, b, ra=0.0, rb=0.0, cat_trong=None, nhan_ham=None, nhan_can=('a', 'b'),
                   hien_sinh=False, nhan_khoi=None, nhan_khoi_xy=None,
                   mau='blue', mau_to='blue!12',
                   xmin=None, xmax=None, ymin=None, ymax=None,
                   sau=None, samples=160, width=9.0, height=6.0,
                   out='khoitronxoay', tra_bytes=False, scale=1.0):
    r"""KHỐI TRÒN XOAY 3D (silhouette phối cảnh chuẩn SGK Giải tích 12 Bài 13) — pgfplots.
       Vẽ khối sinh ra khi QUAY hình phẳng [y=f(x), Ox, x=a, x=b] quanh TRỤC Ox.
       Một hàm phủ: NÓN (f=kx, ra=0) · TRỤ (f=R hằng) · CẦU (f=√(R²−x²), [−R;R]) ·
                    CHỎM CẦU (f=√(R²−x²), [R−h;R]) · NÓN CỤT (f tuyến tính) · khối quay tổng quát.
       ham   : f(x) cú pháp pgfplots (biến x), f≥0 trên [a;b]. VD '0.5*x' · 'sqrt(1-x^2)' · '1' · 'sqrt(x)'.
       a,b   : cận (số, a<b).
       ra,rb : BÁN KÍNH mặt cắt tại x=a, x=b = f(a), f(b) (caller tự tính — dễ: nón ra=0/rb=R; trụ ra=rb=R; cầu ra=rb=0).
               ra/rb>0 → vẽ ELLIPSE mặt đáy (rim) tại cận đó; =0 → đỉnh nhọn (nón/cầu), bỏ ellipse.
       nhan_ham : nhãn math đặt dọc đường sinh f (vd 'y=f(x)'); None → không.
       nhan_can : (nhãn_a, nhãn_b) math-string dưới trục Ox tại a,b.
       hien_sinh: True → tô NHẠT nửa trên (hình phẳng sinh f↔Ox) để minh họa miền quay.
       nhan_khoi + nhan_khoi_xy=(x,y): nhãn tên khối (vd '(\\mathcal{B})') đặt trong khối.
       sau   : độ 'sâu' ellipse (bán trục x, đơn vị trục x) — None → 0,10·(b−a).
       PHANH: a<b; ra,rb≥0."""
    assert a < b, "[KTX] can a<b"
    assert ra >= 0 and rb >= 0, "[KTX] ra,rb >= 0"
    if sau is None:
        sau = 0.10 * (b - a)
    rmax = max(ra, rb, 0.5)
    if xmin is None: xmin = a - 0.5 * (b - a) - sau
    if xmax is None: xmax = b + 0.35 * (b - a) + sau
    if ymin is None: ymin = -rmax * 1.5
    if ymax is None: ymax = rmax * 1.5

    opt = [r'axis lines=middle', r'axis line style={-{Stealth[length=6pt]}}',
           r'xlabel={$x$}', r'ylabel={$y$}',
           r'x label style={at={(ticklabel* cs:1.0)},anchor=west}',
           r'y label style={at={(ticklabel* cs:1.0)},anchor=south}',
           r'xmin=%g' % xmin, r'xmax=%g' % xmax, r'ymin=%g' % ymin, r'ymax=%g' % ymax,
           r'restrict y to domain=%g:%g' % (ymin - 1, ymax + 1),
           r'samples=%d' % samples, r'width=%gcm' % width, r'height=%gcm' % height,
           r'xtick=\empty', r'ytick=\empty', r'clip=true', r'enlargelimits=false']

    t = [r'\documentclass[border=5pt]{standalone}',
         r'\usepackage{pgfplots}\pgfplotsset{compat=1.18}',
         r'\usepgfplotslibrary{fillbetween}',
         r'\usepackage{amsmath,amssymb}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g]' % scale,
         r'\begin{axis}[%s]' % (',\n  '.join(opt))]

    # (1) KHỐI: tô giữa đường sinh trên f và đường dưới -f trên [a;b] → thân khối tròn xoay (lát dọc)
    t.append(r'\addplot[name path=KTXt,draw=none,domain=%g:%g,samples=%d] {%s};' % (a, b, samples, ham))
    t.append(r'\addplot[name path=KTXb,draw=none,domain=%g:%g,samples=%d] {-(%s)};' % (a, b, samples, ham))
    t.append(r'\addplot[%s] fill between[of=KTXt and KTXb];' % mau_to)

    # (2) tùy chọn: tô NHẠT hơn nửa trên (hình phẳng sinh) + đường sinh đậm
    if hien_sinh:
        t.append(r'\addplot[draw=none,fill=%s,domain=%g:%g,samples=%d] {%s} \closedcycle;'
                 % ('black!6', a, b, samples, ham))

    # đường sinh trên (đậm) + đường dưới (mảnh hơn)
    lab = (r' node[pos=0.5,anchor=south,font=\footnotesize,fill=white,inner sep=1pt]{$%s$}' % nhan_ham) if nhan_ham else ''
    t.append(r'\addplot[%s,very thick,domain=%g:%g,samples=%d] {%s}%s;' % (mau, a, b, samples, ham, lab))
    t.append(r'\addplot[%s,thick,domain=%g:%g,samples=%d] {-(%s)};' % (mau, a, b, samples, ham))

    # (3) ELLIPSE mặt đáy tại cận (rim 3D): nửa trước liền, nửa sau (xa) đứt
    def ellipse(x0, r):
        if r <= 1e-9:
            return
        # nửa trước (bên phải, gần người xem) liền; nửa sau (bên trái) đứt
        t.append(r'\draw[%s,thick] (axis cs:%g,%g) arc[start angle=90,end angle=-90,x radius=%g,y radius=%g];'
                 % (mau, x0, r, sau, r))
        t.append(r'\draw[%s,thick,dashed] (axis cs:%g,%g) arc[start angle=90,end angle=270,x radius=%g,y radius=%g];'
                 % (mau, x0, r, sau, r))
    ellipse(a, ra)
    ellipse(b, rb)
    # mặt cắt GIỮA (xích đạo cầu, vành trong) — list (x, r); front liền + back đứt
    if cat_trong:
        for (xc, rc) in cat_trong:
            ellipse(xc, rc)

    # (4) trục quay Ox đoạn trong khối (nét chấm nhẹ) + nhãn cận
    for x0, labc, r in ((a, nhan_can[0], ra), (b, nhan_can[1], rb)):
        t.append(r'\node[font=\footnotesize,anchor=north] at (axis cs:%g,%g) {$%s$};' % (x0, min(-0.03, ymin*0.04), labc))
        # vạch mảnh nối trục tới mép trên tại cận (gợi mặt phẳng cắt)
        if r > 1e-9:
            t.append(r'\draw[gray,dotted] (axis cs:%g,0) -- (axis cs:%g,%g);' % (x0, x0, r))

    if nhan_khoi is not None and nhan_khoi_xy is not None:
        kx, ky = nhan_khoi_xy
        t.append(r'\node[font=\small] at (axis cs:%g,%g) {$%s$};' % (kx, ky, nhan_khoi))

    t.append(r'\node[font=\footnotesize,anchor=north east] at (axis cs:0,0) {$O$};')
    t.append(r'\end{axis}\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)
