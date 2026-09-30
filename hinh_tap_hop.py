#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_tap_hop.py — HÌNH TẬP HỢP (Đại số 10 KNTT, Chương I Bài Tập hợp)
#   [31d] Ông Bụt 2026-09-30 · nhánh ĐẠI SỐ THPT (PT2627) · pilot hình DS10_CH01_B02.
#
#   Hai hàm generator ĐỘC LẬP (theo mẫu hinh_daiso.hinhDienTichDaiSo — Đ khối [29c]):
#   biểu đồ Ven & trục số tập hợp là hình MINH HOẠ (không quan hệ toạ-độ-số cần
#   PHANH verify) → build .tex standalone đầy đủ + render_tikz_doc, KHÔNG qua
#   HinhCoBan/PHANH → 0 rủi ro regression 20+ hàm cũ. Giấu toạ độ vẽ (Đ5.9):
#   AI Soạn CHỈ khai nhãn/phần tử/miền tô, không đụng số vẽ.
#
#   ① bieu_do_ven(kieu, nhan, phan_tu, to, ...) :
#       kieu='don'  1 vòng           · 'cat' 2 vòng cắt  · 'roi' 2 vòng rời
#       kieu='long' vòng lồng (⊂)    · 'ba'  3 vòng cắt
#       to = 'giao'|'hop'|'hieu_ST'|'hieu_TS'|'phan_bu'|None
#       phan_tu điền phần tử/biểu thức (đếm) vào từng miền.
#   ② truc_so_tap_hop(cac_khoang, ...) :
#       mỗi khoảng {'tu','den','kin_tu','kin_den','nhan','to'} ; tu/den=None → ∓∞.
#       1 khoảng → 1 trục ; nhiều → xếp tầng (minh hoạ giao/hợp trên trục).
#   PT2627 · dùng chung repo kho-congcu.
# ═══════════════════════════════════════════════════════════════════
import hinh_core as _HC


# ─────────── tiện ích nội bộ ───────────
def _m(s, macdinh):
    """Nhãn: None → mặc định; ngược lại ép chuỗi (caller tự lo $..$ nếu cần)."""
    return macdinh if s is None else str(s)


def _txt(s):
    """Bọc nhãn tập hợp thành math in nghiêng nếu là chữ cái ASCII trần
    (S, T, A) → $S$; nếu đã có $ hoặc \\ (vd \\mathbb{R}) → giữ nguyên;
    có khoảng trắng / dấu tiếng Việt → text thường."""
    s = str(s)
    if '$' in s:
        return s
    if '\\' in s:                                   # lệnh LaTeX (\mathbb{R}) → math mode
        return '$%s$' % s
    if s.isascii() and ' ' not in s and s.isalnum():
        return '$%s$' % s
    return s


def _phantu(s):
    """Phần tử điền trong vùng: bọc $...$ để in toán (số/ký hiệu), giữ nếu có sẵn.
    [31i] Chuỗi chứa dấu tiếng Việt (non-ASCII) → text thường (xelatex đủ dấu),
    KHÔNG ép math mode (math italic Latin Modern rớt dấu: 'Bình'→'Bnh')."""
    if s is None:
        return ''
    s = str(s)
    if '$' in s:
        return s
    if not s.isascii():            # [31i] tên/nhãn tiếng Việt có dấu → text thường
        return s
    return '$%s$' % s


_PRE_VEN = (r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usepackage{amsmath}\usepackage{amssymb}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[line join=round, every node/.style={font=\normalsize},
  vien/.style={line width=0.9pt, black},
  to/.style={fill=cyan!35}, tolt/.style={fill=cyan!18}]
''')
_POST = r'''\end{tikzpicture}
\end{document}'''


def _caption(chuThich, x, y):
    if not chuThich:
        return ''
    return (r'\node[below,font=\itshape] at (%s,%s) {%s};'
            % (x, y, chuThich))


# ─────────── [31g] render RIÊNG cho hình tập hợp (KHÔNG đụng render_tikz_doc chung) ───────────
# BUG (QC pilot B02): render_tikz_doc dùng pdflatex, preamble thiếu font tiếng Việt →
#   nhãn "Bóng đá"→"Bóng á", "Cầu lông"→"Cu lông" (rớt dấu + "đ"). Nhãn tập hợp thường là
#   A/B/S/T/ℝ (không dấu) nên hiếm gặp, nhưng bài word-problem cần nhãn Việt.
# FIX (mẫu hinh_core._render): ƯU TIÊN xelatex + Latin Modern Roman (đủ dấu tiếng Việt);
#   THIẾU xelatex → LÙI pdflatex (bản gốc, ASCII/toán vẫn đúng, chỉ rớt dấu Việt như cũ).
# Đặt RIÊNG trong module này → 0 rủi ro hồi quy hinh_daiso (vẫn dùng render_tikz_doc chung).
import subprocess as _sp
import os as _os


def _render_th(tex_full, out, tra_bytes=False, dpi=200):
    for _e in ('.pdf', '-1.png'):
        try: _os.remove(f'/tmp/{out}{_e}')
        except OSError: pass
    # xelatex: chèn fontspec ngay sau \documentclass...{standalone}
    xe = tex_full.replace(
        '{standalone}',
        '{standalone}\n\\usepackage{fontspec}\\setmainfont{Latin Modern Roman}', 1)
    open(f'/tmp/{out}.tex', 'w').write(xe)
    try:
        _sp.run(['xelatex', '-interaction=nonstopmode', f'{out}.tex'],
                cwd='/tmp', capture_output=True)
    except (FileNotFoundError, OSError):
        pass
    # thiếu xelatex/font → lùi pdflatex với bản gốc (an toàn tuyệt đối)
    if not _os.path.exists(f'/tmp/{out}.pdf'):
        open(f'/tmp/{out}.tex', 'w').write(tex_full)
        try:
            _sp.run(['pdflatex', '-interaction=nonstopmode', f'{out}.tex'],
                    cwd='/tmp', capture_output=True)
        except (FileNotFoundError, OSError):
            pass
    _sp.run(['pdftoppm', '-png', '-r', str(dpi), f'{out}.pdf', out],
            cwd='/tmp', capture_output=True)
    png = f'/tmp/{out}-1.png'
    if not _os.path.exists(png):
        return None
    return open(png, 'rb').read() if tra_bytes else png


# ═══════════════════════ ① BIỂU ĐỒ VEN ═══════════════════════
def bieu_do_ven(kieu='cat', nhan=None, phan_tu=None, to=None,
                bao=None, out='ven', tra_bytes=False, chuThich=None):
    """BIỂU ĐỒ VEN minh hoạ tập hợp & phép toán (giấu toạ độ, Đ5.9).

    kieu :
      • 'don'  — 1 vòng.               nhan={'S':..}          phan_tu={'S':'1, 2, 3'}
      • 'cat'  — 2 vòng cắt nhau.      nhan={'S':..,'T':..}
                 phan_tu={'rieng_S':'7','chung':'2, 4','rieng_T':'-1, 6'}
      • 'roi'  — 2 vòng rời nhau.      nhan={'S':..,'T':..}   phan_tu={'S':..,'T':..}
      • 'long' — vòng lồng (tập con).  nhan={'ngoai':'S','trong':'T'}  hoặc
                 nhan={'chuoi':['R','Q','Z','N']} (ngoài→trong, minh hoạ N⊂Z⊂Q⊂R)
      • 'ba'   — 3 vòng cắt nhau.      nhan={'A':..,'B':..,'C':..}
    to (tô miền, chỉ 'cat' & 'long'):
      • 'cat' : 'giao' | 'hop' | 'hieu_ST' (S\\T) | 'hieu_TS' (T\\S)
      • 'long': 'phan_bu' (phần ngoài \\ trong)
    bao : nhãn tập bao/không gian (khung chữ nhật ngoài) — vd 'X' hoặc r'\\mathbb{R}'.
    chuThich : caption "Hình N" căn giữa dưới.
    """
    nhan = nhan or {}
    phan_tu = phan_tu or {}
    P = [_PRE_VEN]

    # khung tập bao (không gian) nếu có
    def _khung(x0, y0, x1, y1, ten):
        P.append(r'\draw[vien] (%s,%s) rectangle (%s,%s);' % (x0, y0, x1, y1))
        P.append(r'\node[above right] at (%s,%s) {%s};'
                 % (x0, y1, _txt(ten)))

    if kieu == 'don':
        S = _txt(_m(nhan.get('S'), 'S'))
        if bao:
            _khung(-2.6, -1.9, 2.6, 2.0, bao)
        P.append(r'\draw[vien] (0,0) circle [x radius=2, y radius=1.5];')
        P.append(r'\node[above] at (0,1.5) {%s};' % S)
        if phan_tu.get('S'):
            P.append(r'\node at (0,0) {%s};' % _phantu(phan_tu['S']))
        cx, cy = 0, -2.1

    elif kieu in ('cat', 'roi'):
        S = _txt(_m(nhan.get('S'), 'S'))
        T = _txt(_m(nhan.get('T'), 'T'))
        if kieu == 'cat':
            xS, xT, r = -0.95, 0.95, 1.7        # hai tâm gần → chồng lấn
        else:
            xS, xT, r = -2.0, 2.0, 1.5          # rời hẳn
        cS = r'(%s,0) circle [x radius=%s, y radius=1.55]' % (xS, r)
        cT = r'(%s,0) circle [x radius=%s, y radius=1.55]' % (xT, r)
        # tô miền TRƯỚC khi vẽ viền
        if kieu == 'cat' and to:
            if to == 'giao':
                P.append(r'\begin{scope}\clip %s;\fill[to] %s;\end{scope}' % (cS, cT))
            elif to == 'hop':
                P.append(r'\fill[to] %s;\fill[to] %s;' % (cS, cT))
            elif to == 'hieu_ST':
                P.append(r'\begin{scope}\clip %s;\fill[to] (-4,-2) rectangle (4,2);'
                         r'\fill[white] %s;\end{scope}' % (cS, cT))
            elif to == 'hieu_TS':
                P.append(r'\begin{scope}\clip %s;\fill[to] (-4,-2) rectangle (4,2);'
                         r'\fill[white] %s;\end{scope}' % (cT, cS))
        P.append(r'\draw[vien] %s;' % cS)
        P.append(r'\draw[vien] %s;' % cT)
        P.append(r'\node[above] at (%s,1.55) {%s};' % (xS, S))
        P.append(r'\node[above] at (%s,1.55) {%s};' % (xT, T))
        # điền phần tử
        if kieu == 'cat':
            if phan_tu.get('rieng_S'):
                P.append(r'\node at (%s,0) {%s};' % (xS - 0.55, _phantu(phan_tu['rieng_S'])))
            if phan_tu.get('chung'):
                P.append(r'\node at (0,0) {%s};' % _phantu(phan_tu['chung']))
            if phan_tu.get('rieng_T'):
                P.append(r'\node at (%s,0) {%s};' % (xT + 0.55, _phantu(phan_tu['rieng_T'])))
        else:
            if phan_tu.get('S'):
                P.append(r'\node at (%s,0) {%s};' % (xS, _phantu(phan_tu['S'])))
            if phan_tu.get('T'):
                P.append(r'\node at (%s,0) {%s};' % (xT, _phantu(phan_tu['T'])))
        cx, cy = 0, -2.0

    elif kieu == 'long':
        chuoi = nhan.get('chuoi')
        if not chuoi:
            chuoi = [_m(nhan.get('ngoai'), 'S'), _m(nhan.get('trong'), 'T')]
        n = len(chuoi)                          # ngoài→trong
        # bán kính giảm dần; nhãn đặt gần đỉnh mỗi vòng
        rx0, ry0, dr = 3.0, 2.2, 0
        step_x = (rx0 - 0.7) / max(n - 1, 1) if n > 1 else 0
        step_y = (ry0 - 0.55) / max(n - 1, 1) if n > 1 else 0
        # tô phần bù (ngoài trừ trong) khi n==2 & to='phan_bu'
        if to == 'phan_bu' and n == 2:
            P.append(r'\begin{scope}'
                     r'\clip (0,0) ellipse (%s and %s);'
                     r'\fill[to] (-4,-3) rectangle (4,3);'
                     r'\fill[white] (0,%s) ellipse (%s and %s);'
                     r'\end{scope}'
                     % (rx0, ry0, 0, rx0 - step_x, ry0 - step_y))
        for i, ten in enumerate(chuoi):
            rx = rx0 - i * step_x
            ry = ry0 - i * step_y
            P.append(r'\draw[vien] (0,0) ellipse (%s and %s);' % (rx, ry))
            # nhãn nằm GIỮA VÀNH TRÊN mỗi vòng (dưới đỉnh arc, trong băng) → không chạm viền
            y_nhan = ry - (step_y / 2 if (i < n - 1 and step_y) else 0.30)
            P.append(r'\node at (0,%s) {%s};' % (round(y_nhan, 3), _txt(ten)))
        cx, cy = 0, -(ry0 + 0.35)

    elif kieu == 'ba':
        A = _txt(_m(nhan.get('A'), 'A'))
        B = _txt(_m(nhan.get('B'), 'B'))
        C = _txt(_m(nhan.get('C'), 'C'))
        cA = r'(-0.9,0.55) circle [radius=1.75]'
        cB = r'(0.9,0.55) circle [radius=1.75]'
        cC = r'(0,-0.95) circle [radius=1.75]'
        P.append(r'\draw[vien] %s;' % cA)
        P.append(r'\draw[vien] %s;' % cB)
        P.append(r'\draw[vien] %s;' % cC)
        P.append(r'\node[above left]  at (-1.9,1.3) {%s};' % A)
        P.append(r'\node[above right] at (1.9,1.3) {%s};' % B)
        P.append(r'\node[below] at (0,-2.55) {%s};' % C)
        cx, cy = 0, -2.9

    else:
        raise ValueError("[bieu_do_ven] kieu='%s' không hợp lệ "
                         "(don|cat|roi|long|ba)" % kieu)

    P.append(_caption(chuThich, cx, cy))
    P.append(_POST)
    return _render_th('\n'.join(P), out, tra_bytes)


# ═══════════════════════ ② TRỤC SỐ TẬP HỢP ═══════════════════════
_PRE_TRUC = (r'''\documentclass[border=5pt]{standalone}
\usepackage{tikz}\usepackage{amsmath}
\usetikzlibrary{arrows.meta,decorations.pathreplacing}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.6mm]},
  every node/.style={font=\normalsize},
  toduong/.style={line width=2pt, cyan!75!blue}]
''')

_INF = 1.15          # chiều dài tia vượt mút hữu hạn (về phía ∞)


def truc_so_tap_hop(cac_khoang, out='truc_tap', tra_bytes=False, chuThich=None):
    """TRỤC SỐ biểu diễn tập con của R: khoảng/đoạn/nửa khoảng/tia (giấu toạ độ vẽ).

    cac_khoang : list các dict, mỗi khoảng:
        {'tu':<số|None>, 'den':<số|None>,      # None = ∓∞
         'kin_tu':bool,  'kin_den':bool,        # True → ngoặc vuông [ ]; False → ( )
         'nhan':'[1;3]', 'to':True}             # nhan: nhãn dưới trục (tuỳ); to: có tô?
      • 1 khoảng  → 1 trục số.
      • nhiều     → XẾP TẦNG (trên xuống) minh hoạ giao/hợp; trục dùng THANG ĐO CHUNG.
    Tự tính khoảng số nguyên hiển thị từ mọi mút hữu hạn.
    """
    if isinstance(cac_khoang, dict):
        cac_khoang = [cac_khoang]
    if not cac_khoang:
        raise ValueError("[truc_so_tap_hop] cac_khoang rỗng")

    # thang đo chung: gom mọi mút hữu hạn
    huu_han = [k[key] for k in cac_khoang for key in ('tu', 'den')
              if k.get(key) is not None]
    lo = min(huu_han) if huu_han else -1
    hi = max(huu_han) if huu_han else 1
    if lo == hi:
        lo, hi = lo - 1, hi + 1
    lo_i, hi_i = int(_floor(lo)) - 1, int(_ceil(hi)) + 1
    xL, xR = lo_i - _INF, hi_i + _INF
    sc = 1.1                              # đơn vị cm mỗi bước số

    def X(v):
        return round((v - lo_i) * sc, 3)

    P = [_PRE_TRUC]
    n = len(cac_khoang)
    dy = 1.35                             # khoảng cách tầng

    for idx, k in enumerate(cac_khoang):
        y = -idx * dy
        tu, den = k.get('tu'), k.get('den')
        kin_tu, kin_den = k.get('kin_tu', False), k.get('kin_den', False)
        to = k.get('to', True)
        # trục ngang có mũi tên 2 đầu
        P.append(r'\draw[->,line width=0.6pt] (%s,%s) -- (%s,%s);'
                 % (X(lo_i) - _INF, y, X(hi_i) + _INF, y))
        P.append(r'\draw[<-,line width=0.6pt] (%s,%s) -- (%s,%s);'
                 % (X(lo_i) - _INF, y, X(lo_i) - _INF + 0.4, y))
        # vạch + số nguyên (chỉ tầng dưới cùng để đỡ rối; nếu 1 tầng thì luôn hiện)
        hien_so = (idx == n - 1)
        for v in range(lo_i, hi_i + 1):
            P.append(r'\draw[line width=0.5pt] (%s,%s) -- (%s,%s);'
                     % (X(v), y + 0.09, X(v), y - 0.09))
            if hien_so:
                # gốc ghi "O" (gốc toạ độ), các mốc khác ghi số
                nhan_v = 'O' if v == 0 else '%d' % v
                P.append(r'\node[below,font=\small] at (%s,%s) {$%s$};'
                         % (X(v), y - 0.12, nhan_v))

        # đoạn tô
        xa = X(tu) if tu is not None else X(lo_i) - _INF
        xb = X(den) if den is not None else X(hi_i) + _INF
        if to:
            P.append(r'\draw[toduong] (%s,%s) -- (%s,%s);' % (xa, y, xb, y))
            # tia ∞ → mũi tên nhọn ở đầu vô cực
            if tu is None:
                P.append(r'\draw[toduong,->] (%s,%s) -- (%s,%s);'
                         % (X(lo_i) + 0.3, y, xa if False else X(lo_i) - _INF, y))
            if den is None:
                P.append(r'\draw[toduong,->] (%s,%s) -- (%s,%s);'
                         % (xb - 0.3, y, X(hi_i) + _INF, y))
        # ngoặc mút hữu hạn
        if tu is not None:
            _ngoac(P, X(tu), y, '[' if kin_tu else '(')
        if den is not None:
            _ngoac(P, X(den), y, ']' if kin_den else ')')
        # nhãn tập (bên phải trục)
        if k.get('nhan'):
            P.append(r'\node[right,font=\small] at (%s,%s) {%s};'
                     % (X(hi_i) + _INF + 0.15, y, _nhan_khoang(k['nhan'])))

    if chuThich:
        P.append(r'\node[below,font=\itshape] at (%s,%s) {%s};'
                 % (X((lo_i + hi_i) / 2), -(n - 1) * dy - 0.7, chuThich))
    P.append(_POST)
    return _render_th('\n'.join(P), out, tra_bytes)


def _ngoac(P, x, y, ch):
    """Vẽ ngoặc [ ] ( ) tại mút, căn giữa trục, màu tô."""
    P.append(r'\node[toduong,font=\large,inner sep=0pt] at (%s,%s) {$%s$};'
             % (x, y, ch if ch in '()' else ('{%s}' % ch)))


def _nhan_khoang(s):
    s = str(s)
    return s if ('$' in s) else '$%s$' % s


# ─────────── floor/ceil không cần numpy ───────────
def _floor(x):
    xi = int(x)
    return xi if (x >= 0 or x == xi) else xi - 1


def _ceil(x):
    xi = int(x)
    return xi if (x <= 0 or x == xi) else xi + 1
