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
