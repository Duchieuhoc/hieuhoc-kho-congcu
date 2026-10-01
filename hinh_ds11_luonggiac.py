# -*- coding: utf-8 -*-
# hinh_ds11_luonggiac.py — HÌNH LƯỢNG GIÁC THPT (Đại số 11 Ch1)
# Generator ĐỘC LẬP (như nua_duong_tron_don_vi) — KHÔNG đụng file máy Hình (hinh_tron_ve.py).
# Triết lý VERIFY (Đ5.9): hàm nhận NGHĨA (góc α), máy TỰ tính toạ độ (cosα,sinα); KHÔNG nhập toạ độ tay.
# Nhãn math-mode (pdflatex-safe): O, A, M, x, y, α, sin α, cos α. KHÔNG chữ tiếng Việt trong hình.
import math
import hinh_core as _HC
import hinh_tron_ve as _HT   # chỉ để gắn staticmethod vào class entry chung


def goc_luong_giac(goc_v=55.0, goc_m=None, chieu='duong', out='goc_lg', tra_bytes=False, scale=1.0):
    """GÓC LƯỢNG GIÁC (SGK H1.3): tia đầu Ou (ngang), tia cuối Ov tại góc goc_v°,
    tia quay Om (nét đứt, tuỳ chọn) + cung cong chỉ CHIỀU quay (dương=ngược kim đồng hồ, +).
    Nhãn: O, u, v, (m); dấu + hoặc - ở cung."""
    L = float(goc_v); R = 2.3
    out_r = R + 0.5
    duong = (chieu == 'duong')
    dau = '+' if duong else '-'
    cs = [r'\documentclass[border=6pt]{standalone}',
          r'\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.4mm]},font=\normalsize]' % scale]
    # tia đầu Ou (ngang phải)
    cs.append(r'\draw[->,thick] (0,0) -- (%g,0) node[right] {$u$};' % out_r)
    # tia cuối Ov
    vx = out_r * math.cos(math.radians(L)); vy = out_r * math.sin(math.radians(L))
    cs.append(r'\draw[->,thick] (0,0) -- (%g,%g) node[above right] {$v$};' % (vx, vy))
    # tia quay Om (nét đứt) nếu có
    if goc_m is not None:
        mg = float(goc_m)
        mx = out_r * math.cos(math.radians(mg)); my = out_r * math.sin(math.radians(mg))
        cs.append(r'\draw[->,thick,green!55!black,dashed] (0,0) -- (%g,%g) node[above right,green!55!black] {$m$};' % (mx, my))
    # cung chỉ chiều quay (từ Ou tới Ov) + dấu
    cr = 0.9
    if duong:
        cs.append(r'\draw[->,orange,thick] (%g:%g) arc (0:%g:%g);' % (0.0, cr, L, cr))
    else:
        cs.append(r'\draw[<-,orange,thick] (%g:%g) arc (0:%g:%g);' % (0.0, cr, L, cr))
    cs.append(r'\node[orange] at (%g:%g) {$%s$};' % (L / 2.0, cr + 0.33, dau))
    cs.append(r'\fill (0,0) circle (1.5pt); \node[below left,font=\small] at (0,0) {$O$};')
    cs.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes)


def duong_tron_luong_giac(goc=None, ten_M='M', hien_sin_cos=True, goc_phan_tu=False,
                          hien_A=True, R=2.6, out='dtlg', tra_bytes=False, scale=1.0):
    """ĐƯỜNG TRÒN LƯỢNG GIÁC đầy đủ (SGK H1.7/H1.9b): tâm O, bán kính 1, điểm gốc A(1;0),
    chiều dương (ngược kim đồng hồ). Điểm M biểu diễn góc lượng giác số đo `goc`° (bất kỳ,
    máy tự quy về vị trí (cosα,sinα)). Trục hoành = trục cos, trục tung = trục sin.
      goc: số đo góc α (độ) để đặt M; None → chỉ vẽ đường tròn + A (hình nền khái niệm).
      hien_sin_cos=True → gióng nét đứt + nhãn 'sin α' (trên Oy), 'cos α' (trên Ox) + cung α.
      goc_phan_tu=True → nhãn I, II, III, IV bốn góc phần tư.
    PHANH nội sinh: điểm M buộc nằm trên đường tròn (|OM|=R theo dựng cos/sin)."""
    R = float(R); rac = R + 0.55
    cs = [r'\documentclass[border=6pt]{standalone}',
          r'\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}',
          r'\begin{document}',
          r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.4mm]},font=\normalsize]' % scale]
    # trục cos (Ox) + trục sin (Oy), hai đầu mũi tên
    cs.append(r'\draw[<->,thick] (-%g,0) -- (%g,0) node[right] {$x\,(\cos)$};' % (rac, rac))
    cs.append(r'\draw[<->,thick] (0,-%g) -- (0,%g) node[above] {$y\,(\sin)$};' % (rac, rac))
    # đường tròn đơn vị
    cs.append(r'\draw[blue,line width=0.9pt] (0,0) circle (%g);' % R)
    # mốc ±1
    cs.append(r'\node[below right,font=\small] at (%g,0) {$1$};' % R)
    cs.append(r'\node[below left,font=\small] at (-%g,0) {$-1$};' % R)
    cs.append(r'\node[above left,font=\small] at (0,%g) {$1$};' % R)
    cs.append(r'\node[below left,font=\small] at (0,-%g) {$-1$};' % R)
    # chiều dương (cung mũi tên ngoài, đặt ở góc phần tư II để KHÔNG đè điểm M ở phần tư I)
    cs.append(r'\draw[->,orange,thick] (102:%g) arc (102:168:%g);' % (R + 0.28, R + 0.28))
    cs.append(r'\node[orange,font=\small] at (135:%g) {$+$};' % (R + 0.6))
    if goc_phan_tu:
        for ang, lb in [(45, 'I'), (135, 'II'), (225, 'III'), (315, 'IV')]:
            cs.append(r'\node[gray,font=\small] at (%g:%g) {$\mathrm{%s}$};' % (ang, R * 0.62, lb))
    # điểm gốc A(1;0) — nhãn A đặt TRÊN trục (above right) để không đè mốc "1" (below right)
    if hien_A:
        cs.append(r'\fill (%g,0) circle (1.6pt); \node[above right,font=\small] at (%g,0.03) {$A$};' % (R, R))
    cs.append(r'\fill (0,0) circle (1.5pt); \node[below left,font=\small] at (-0.04,0) {$O$};')
    # điểm M tại góc α
    if goc is not None:
        a = float(goc)
        mx = R * math.cos(math.radians(a)); my = R * math.sin(math.radians(a))
        # bán kính OM + điểm M
        cs.append(r'\draw[thick,red] (0,0) -- (%g,%g);' % (mx, my))
        anc = 'above right' if mx >= -0.05 else 'above left'
        cs.append(r'\fill[red] (%g,%g) circle (1.9pt); \node[%s,red] at (%g,%g) {$%s$};'
                  % (mx, my, anc, mx, my, _lab(ten_M)))
        # cung α từ OA đến OM
        cr = 0.72
        cs.append(r'\draw[orange,thick] (0:%g) arc (0:%g:%g);' % (cr, a, cr))
        cs.append(r'\node[orange,font=\small] at (%g:%g) {$\alpha$};' % (a / 2.0, cr + 0.3))
        if hien_sin_cos:
            # gióng nét đứt: M→chân Ox (cos), M→chân Oy (sin)
            cs.append(r'\draw[dashed,gray] (%g,%g) -- (%g,0);' % (mx, my, mx))
            cs.append(r'\draw[dashed,gray] (%g,%g) -- (0,%g);' % (mx, my, my))
            cs.append(r'\fill (%g,0) circle (1.3pt);' % mx)
            cs.append(r'\fill (0,%g) circle (1.3pt);' % my)
            # nhãn cos α (trên Ox), sin α (trên Oy)
            vpos = 'above' if my >= 0 else 'below'
            cs.append(r'\node[%s,font=\small] at (%g,%g) {$\cos\alpha$};' % (vpos, mx, 0.0 + (0.12 if my >= 0 else -0.12)))
            hpos = 'left' if mx >= 0 else 'right'
            cs.append(r'\node[%s,font=\small] at (%g,%g) {$\sin\alpha$};' % (hpos, 0.0 + (-0.1 if mx >= 0 else 0.1), my))
    cs.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(cs), out, tra_bytes)


def _lab(s):
    s = str(s)
    return s if '$' in s else s  # tên điểm đơn (M, N) in thẳng trong $...$ ở caller


# Gắn vào class entry chung để AI Soạn gọi qua instance H.HinhTron hoặc trực tiếp
_HT.HinhTron.goc_luong_giac = staticmethod(goc_luong_giac)
_HT.HinhTron.duong_tron_luong_giac = staticmethod(duong_tron_luong_giac)
