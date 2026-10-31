#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_bpt.py — MIỀN NGHIỆM BẤT PHƯƠNG TRÌNH / HỆ BPT BẬC NHẤT HAI ẨN
#   (Đại số 10 KNTT, Chương II: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn)
#   [33zi] Ông Bụt 2026-11-01 · nhánh ĐẠI SỐ THPT (PT2627) · pilot hình DS10_CH02_B03.
#
#   Generator ĐỘC LẬP (mẫu hinh_tap_hop.py [31d]): miền nghiệm là hình MINH HOẠ trên
#   mặt phẳng toạ độ — không có quan hệ hình-học cần PHANH verify → build .tex standalone
#   đầy đủ + render xelatex (đủ dấu tiếng Việt), KHÔNG qua HinhCoBan/PHANH → 0 rủi ro
#   regression kho cũ. Giấu toạ độ vẽ (Đ5.9): AI Soạn CHỈ khai BẤT PHƯƠNG TRÌNH
#   (a, b, c, dấu) + điểm cần đánh dấu; MÁY tự tính miền + đỉnh + vẽ.
#
#   ① mien_nghiem(bpt, diem=None, khung=None, nhan_duong=None, ten_mien=None, ...) :
#       bpt  = list các (a, b, c, dau) với dau ∈ {'<=','>=','<','>','='} nghĩa a·x+b·y <dau> c ('=' → chỉ vẽ đường, không tô).
#              1 phần tử → 1 BPT (nửa mặt phẳng). Nhiều → HỆ BPT (giao các nửa mp).
#       Nét bờ: '<=' '>=' → NÉT LIỀN (kể bờ) · '<' '>' → NÉT ĐỨT (không kể bờ).
#       Miền nghiệm (giao) tô xanh nhạt ("miền KHÔNG bị gạch").
#       diem = list (x, y, 'nhãn') — đỉnh/điểm đánh dấu (vd [(0,100,'A(0; 100)')]).
#       khung = (xmin, xmax, ymin, ymax); None → tự canh theo giao điểm + điểm.
#       nhan_duong = list 'nhãn đường' theo thứ tự bpt (vd 'd: x+y=100'); None → bỏ.
#       ten_mien = nhãn đặt giữa miền (vd 'OABC'); None → bỏ.
#   PT2627 · dùng chung repo kho-congcu.
# ═══════════════════════════════════════════════════════════════════
import subprocess as _sp
import os as _os

_EPS = 1e-9

# ─────────── preamble TikZ (scale chèn động theo khung) ───────────
def _pre(scale):
    return (r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usepackage{amsmath}\usepackage{amssymb}
\usetikzlibrary{arrows.meta}
\definecolor{hhbo}{RGB}{197,48,38}
\definecolor{hhmien}{RGB}{191,227,240}
\begin{document}
\begin{tikzpicture}[scale=%s, >=Stealth, line join=round,
  every node/.style={font=\normalsize},
  truc/.style={->, line width=1pt, black},
  bo/.style={line width=1.2pt, hhbo},
  bodut/.style={line width=1.2pt, hhbo, dash pattern=on 4pt off 3pt}]
''' % _fmt(scale))
_POST = r'''\end{tikzpicture}
\end{document}'''


# ─────────── render xelatex (mẫu hinh_tap_hop._render_th) ───────────
def _render(tex_full, out, tra_bytes=False, dpi=200):
    for _e in ('.pdf', '-1.png'):
        try: _os.remove(f'/tmp/{out}{_e}')
        except OSError: pass
    xe = tex_full.replace(
        '{standalone}',
        '{standalone}\n\\usepackage{fontspec}\\setmainfont{Latin Modern Roman}', 1)
    open(f'/tmp/{out}.tex', 'w').write(xe)
    try:
        _sp.run(['xelatex', '-interaction=nonstopmode', f'{out}.tex'],
                cwd='/tmp', capture_output=True)
    except (FileNotFoundError, OSError):
        pass
    if not _os.path.exists(f'/tmp/{out}.pdf'):           # lùi pdflatex (ASCII/toán vẫn đúng)
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


# ─────────── hình học: clip đa giác bởi nửa mặt phẳng (Sutherland–Hodgman) ───────────
def _trong(p, a, b, c):
    """True nếu điểm p thoả a·x + b·y <= c (tính cả biên, nới EPS)."""
    return a * p[0] + b * p[1] <= c + _EPS

def _giao_canh(p, q, a, b, c):
    """Giao của đoạn p→q với đường a·x+b·y=c (p,q khác phía)."""
    fp = a * p[0] + b * p[1] - c
    fq = a * q[0] + b * q[1] - c
    t = fp / (fp - fq)
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))

def _clip(poly, a, b, c):
    """Giữ phần đa giác thoả a·x+b·y <= c."""
    if not poly:
        return poly
    out = []
    n = len(poly)
    for i in range(n):
        cur, nxt = poly[i], poly[(i + 1) % n]
        cin, nin = _trong(cur, a, b, c), _trong(nxt, a, b, c)
        if cin:
            out.append(cur)
            if not nin:
                out.append(_giao_canh(cur, nxt, a, b, c))
        else:
            if nin:
                out.append(_giao_canh(cur, nxt, a, b, c))
    return out

def _chuan_bpt(a, b, c, dau):
    """Đưa mọi BPT về dạng a'·x+b'·y <= c' để clip (đảo dấu nếu >, >=)."""
    if dau in ('>=', '>'):
        return -a, -b, -c
    return a, b, c

def _don(poly):
    """Bỏ đỉnh trùng khít liên tiếp."""
    r = []
    for p in poly:
        if not r or abs(p[0] - r[-1][0]) > 1e-6 or abs(p[1] - r[-1][1]) > 1e-6:
            r.append(p)
    if len(r) > 1 and abs(r[0][0] - r[-1][0]) < 1e-6 and abs(r[0][1] - r[-1][1]) < 1e-6:
        r.pop()
    return r


def _cat_khung(a, b, c, kh):
    """Hai đầu mút của đường a·x+b·y=c cắt khung (xmin,xmax,ymin,ymax) — để vẽ bờ."""
    xmin, xmax, ymin, ymax = kh
    pts = []
    if abs(b) > _EPS:
        for x in (xmin, xmax):
            y = (c - a * x) / b
            if ymin - _EPS <= y <= ymax + _EPS:
                pts.append((x, y))
    if abs(a) > _EPS:
        for y in (ymin, ymax):
            x = (c - b * y) / a
            if xmin - _EPS <= x <= xmax + _EPS:
                pts.append((x, y))
    # khử trùng
    uniq = []
    for p in pts:
        if not any(abs(p[0] - q[0]) < 1e-6 and abs(p[1] - q[1]) < 1e-6 for q in uniq):
            uniq.append(p)
    return uniq[:2]


def _fmt(v):
    v = round(v, 3)
    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))
    return ('%g' % v)


# ═══════════════════════ ① MIỀN NGHIỆM ═══════════════════════
def mien_nghiem(bpt, diem=None, khung=None, nhan_duong=None, ten_mien=None,
                out='mien_nghiem', tra_bytes=False, dpi=200):
    """Vẽ miền nghiệm của 1 BPT hoặc hệ BPT bậc nhất hai ẩn trên mặt phẳng Oxy.

    bpt        : list (a, b, c, dau) — a·x+b·y <dau> c ; dau ∈ '<=','>=','<','>','=' ('=' chỉ vẽ đường, không tô).
    diem       : list (x, y, 'nhãn') đỉnh/điểm đánh dấu (có thể None).
    khung      : (xmin,xmax,ymin,ymax) ; None → tự canh.
    nhan_duong : list nhãn mỗi đường (theo thứ tự bpt) ; None → không ghi.
    ten_mien   : nhãn giữa miền nghiệm ; None → bỏ.
    """
    if not bpt:
        raise ValueError('[mien_nghiem] cần ít nhất 1 bất phương trình')
    diem = list(diem or [])

    # --- tự canh khung nếu thiếu: từ giao các đường đôi một + giao trục + điểm ---
    if khung is None:
        xs, ys = [0.0], [0.0]
        for (x, y, _n) in diem:
            xs.append(x); ys.append(y)
        n = len(bpt)
        for i in range(n):
            a1, b1, c1, _ = bpt[i]
            if abs(a1) > _EPS: xs.append(c1 / a1)   # giao trục Ox (y=0)
            if abs(b1) > _EPS: ys.append(c1 / b1)   # giao trục Oy (x=0)
            for j in range(i + 1, n):
                a2, b2, c2, _ = bpt[j]
                det = a1 * b2 - a2 * b1
                if abs(det) > _EPS:
                    xs.append((c1 * b2 - c2 * b1) / det)
                    ys.append((a1 * c2 - a2 * c1) / det)
        xmn, xmx, ymn, ymx = min(xs), max(xs), min(ys), max(ys)
        dx = max(xmx - xmn, 1.0) * 0.12 + 1
        dy = max(ymx - ymn, 1.0) * 0.12 + 1
        khung = (xmn - dx, xmx + dx, ymn - dy, ymx + dy)
    xmin, xmax, ymin, ymax = khung

    # scale sao cho cạnh lớn nhất ~ 9cm (giữ tỉ lệ 1:1; nét & chữ cố định pt)
    scale = 9.0 / max(xmax - xmin, ymax - ymin, 1.0)
    P = [_pre(scale)]

    # --- 1) tô miền nghiệm (giao các nửa mp) = clip khung bởi từng BPT ---
    #   dau='=' → đường TRUNG TÍNH (chỉ vẽ, không tô — vd H.2.1 xét điểm thuộc nửa mp nào)
    co_bpt_thuc = any(dau in ('<=', '>=', '<', '>') for (_a, _b, _c, dau) in bpt)
    poly = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
    for (a, b, c, dau) in bpt:
        if dau == '=':
            continue
        aa, bb, cc = _chuan_bpt(a, b, c, dau)
        poly = _clip(poly, aa, bb, cc)
    poly = _don(poly)
    if co_bpt_thuc and len(poly) >= 3:
        path = ' -- '.join('(%s,%s)' % (_fmt(x), _fmt(y)) for (x, y) in poly)
        P.append(r'\fill[hhmien] %s -- cycle;' % path)

    # --- 2) trục Oxy ---
    P.append(r'\draw[truc] (%s,0) -- (%s,0) node[right]{$x$};' % (_fmt(xmin), _fmt(xmax)))
    P.append(r'\draw[truc] (0,%s) -- (0,%s) node[above]{$y$};' % (_fmt(ymin), _fmt(ymax)))
    P.append(r'\node[below left] at (0,0) {$O$};')

    # --- 3) các đường bờ (nét liền nếu ≤,≥ ; nét đứt nếu <,>) ---
    for i, (a, b, c, dau) in enumerate(bpt):
        # bờ trùng trục toạ độ (x=0 ≡ Oy ; y=0 ≡ Ox) → để trục đen lo, không vẽ đè đỏ
        if abs(c) < _EPS and (abs(b) < _EPS or abs(a) < _EPS):
            continue
        pts = _cat_khung(a, b, c, khung)
        if len(pts) < 2:
            continue
        sty = 'bodut' if dau in ('<', '>') else 'bo'
        P.append(r'\draw[%s] (%s,%s) -- (%s,%s);'
                 % (sty, _fmt(pts[0][0]), _fmt(pts[0][1]),
                    _fmt(pts[1][0]), _fmt(pts[1][1])))
        if nhan_duong and i < len(nhan_duong) and nhan_duong[i]:
            mx = (pts[0][0] + pts[1][0]) / 2
            my = (pts[0][1] + pts[1][1]) / 2
            P.append(r'\node[font=\small, hhbo, fill=white, inner sep=1pt] at (%s,%s) {%s};'
                     % (_fmt(mx), _fmt(my), _bocmath(nhan_duong[i])))

    # --- 4) nhãn giữa miền ---
    if ten_mien and co_bpt_thuc and len(poly) >= 3:
        cx = sum(p[0] for p in poly) / len(poly)
        cy = sum(p[1] for p in poly) / len(poly)
        P.append(r'\node[font=\itshape] at (%s,%s) {%s};'
                 % (_fmt(cx), _fmt(cy), _bocmath(ten_mien)))

    # --- 5) điểm đánh dấu (đỉnh) ---
    for (x, y, nh) in diem:
        goc = abs(x) < _EPS and abs(y) < _EPS       # gốc O đã có nhãn từ trục
        P.append(r'\fill[black] (%s,%s) circle (1.6pt);' % (_fmt(x), _fmt(y)))
        if nh and not goc:
            pos = 'above right' if (x >= (xmin + xmax) / 2) else 'above left'
            P.append(r'\node[font=\small, %s] at (%s,%s) {%s};'
                     % (pos, _fmt(x), _fmt(y), _bocmath(nh)))

    P.append(_POST)
    return _render('\n'.join(P), out, tra_bytes, dpi)


def _bocmath(s):
    """Nhãn: đã có $ → giữ; có chữ tiếng Việt (non-ASCII) → text thường; còn lại → $...$."""
    s = str(s)
    if '$' in s:
        return s
    if not s.isascii():
        return s
    return '$%s$' % s


# ─────────── tự kiểm nhanh khi chạy trực tiếp ───────────
if __name__ == '__main__':
    # VD3 B03: x + y >= 100 (nửa mp không chứa O, bờ liền)
    mien_nghiem([(1, 1, 100, '>=')],
                diem=[(100, 0, '100'), (0, 100, '100')],
                nhan_duong=['d: x+y=100'], out='_test_b03_vd3')
    # VD3 B04: hệ tối ưu → tứ giác OABC
    mien_nghiem([(1, 0, 0, '>='), (0, 1, 0, '>='),
                 (1, 1, 100, '<='), (2, 1, 120, '<=')],
                diem=[(0, 100, 'A(0; 100)'), (20, 80, 'B(20; 80)'),
                      (60, 0, 'C(60; 0)')],
                ten_mien='OABC', out='_test_b04_vd3')
    print('OK')
