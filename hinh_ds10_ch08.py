# -*- coding: utf-8 -*-
# hinh_ds10_ch08.py — SƠ ĐỒ HÌNH CÂY ĐẾM (Đại số 10, Chương VIII: Đại số tổ hợp)
# Generator ĐỘC LẬP (như hinh_ds10_ch06.py) — KHÔNG đụng file dùng chung / file máy Hình / hinh_core.
#   LÝ DO RA ĐỜI (pilot B23, cửa [SỬA] Đ5.9): so_do_cay() (hinh_xacsuat) là CÂY XÁC SUẤT — nhãn render
#   ở MATH-MODE (preamble chỉ \newunicodechar Đ/đ) → RỤNG dấu tiếng Việt + nuốt dấu cách ("riêu cua"→
#   "rieucua"); và CHỐT tối đa 2 tầng + độ sâu ĐỒNG ĐỀU → KHÔNG dựng được H.8.2 (3 tầng, lệch độ sâu).
#   Builder này: nhãn TEXT tiếng Việt (xelatex + fontspec DejaVu Serif) + ĐỆ QUY đa tầng, lệch độ sâu
#   tùy ý. Render path riêng (_render_xe, xelatex) tách hẳn hinh_core.render_tikz_doc (pdflatex) ⇒ 0
#   regression. Nhãn có nền trắng (fill=white) chống cạnh xuyên chữ ở nút trong.
#
# [33y] 2026-10-28 — PILOT DS10_CH08_B23 (Quy tắc đếm). OB thẩm định + áp vá AI Soạn trên HEAD [33x].
#   • so_do_cay_dem(goc, con, ...) — sơ đồ hình cây ĐẾM (quy tắc cộng/nhân): gốc → nhánh → lá, nhãn cụm
#     từ tiếng Việt, đa tầng & lệch độ sâu; dem_la=True tự đánh số lá (minh hoạ "không bỏ sót").
#   Dùng cho DS10_CH08 (đếm). TÁCH BẠCH với so_do_cay() (cây XÁC SUẤT, nhãn cạnh) của DS10_CH09/DS12_CH06.
#
# API:
#   so_do_cay_dem(goc, con, out='so_do_cay_dem', tra_bytes=False, scale=1.0, dx=2.2, dy=2.0, dem_la=False)
#     goc : str  — nhãn gốc (text tiếng Việt OK). VD 'Món ăn sáng'.
#     con : list[node] — nhánh con của gốc. node = dict:
#              {'nhan': <str nhãn ở nút>, 'con': <list[node] con; bỏ/[] nếu LÁ>, 'la': <str optional dưới lá>}
#           Đệ quy: mỗi nút có 'con' riêng ⇒ tầng tùy ý, nhánh lệch độ sâu tùy ý.
#     dem_la : True → tự đánh số thứ tự các lá.
#     Trả: đường dẫn PNG (mặc định) hoặc bytes PNG (tra_bytes=True); None nếu render hỏng.
import os, subprocess

LOP_MODULE = "DS10_CH08 (Đại số tổ hợp) — sơ đồ hình cây ĐẾM"
HA_TANG = "độc lập (xelatex riêng, không dùng hinh_core)"
CUA_RENDER = "xelatex + fontspec DejaVu Serif (nhãn text tiếng Việt)"

_TMP = '/tmp'


def _render_xe(tex_full, out, tra_bytes=False, dpi=200):
    """Render TikZ standalone bằng XELATEX (fontspec → tiếng Việt đủ dấu).
       Tách riêng khỏi hinh_core.render_tikz_doc (pdflatex) để KHÔNG đụng hàm cũ."""
    with open(os.path.join(_TMP, out + '.tex'), 'w') as f:
        f.write(tex_full)
    subprocess.run(['xelatex', '-interaction=nonstopmode', out + '.tex'],
                   cwd=_TMP, capture_output=True)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), out + '.pdf', out],
                   cwd=_TMP, capture_output=True)
    png = os.path.join(_TMP, out + '-1.png')
    if not os.path.exists(png):
        return None
    if tra_bytes:
        with open(png, 'rb') as f:
            return f.read()
    return png


def _esc(s):
    """Escape ký tự đặc biệt LaTeX trong nhãn text."""
    if s is None:
        return ''
    out = []
    for ch in str(s):
        if ch in '#$%&_{}':
            out.append('\\' + ch)
        elif ch == '~':
            out.append(r'\textasciitilde{}')
        elif ch == '^':
            out.append(r'\textasciicircum{}')
        elif ch == '\\':
            out.append(r'\textbackslash{}')
        else:
            out.append(ch)
    return ''.join(out)


def so_do_cay_dem(goc, con, out='so_do_cay_dem', tra_bytes=False,
                  scale=1.0, dx=2.2, dy=2.0, dem_la=False):
    """Sơ đồ hình cây ĐẾM (quy tắc cộng/nhân): gốc→nhánh→lá, nhãn cụm từ tiếng Việt,
    đa tầng & lệch độ sâu; dem_la=True tự đánh số lá. VD H.8.2 vé tàu, H.8.3 phở/bún."""
    con = con or []
    assert len(con) >= 2, "[CAY-DEM] goc can >= 2 nhanh"

    # ---- 1) duyệt gán toạ độ: lá xếp đều hàng theo ĐỘ SÂU; cha = trung bình con ----
    leaf_counter = [0]        # chỉ số x chạy theo thứ tự lá (in-order)
    la_index = [0]            # đánh số lá nếu dem_la
    nodes = []                # [x, y, nhan, la, is_root, is_leaf]
    edges = []                # (x1,y1,x2,y2)

    def walk(node, depth):
        children = node.get('con') or []
        y = -depth * dy
        if not children:                       # LÁ
            x = leaf_counter[0]
            leaf_counter[0] += 1
            la_txt = node.get('la')
            if dem_la:
                la_index[0] += 1
                la_txt = (la_txt + ' ' if la_txt else '') + '(%d)' % la_index[0]
            nodes.append([x, y, node.get('nhan'), la_txt, False, True])
            return x
        xs = [walk(c, depth + 1) for c in children]
        x = sum(xs) / len(xs)
        nodes.append([x, y, node.get('nhan'), node.get('la'), depth == 0, False])
        for c, xc in zip(children, xs):
            yc = -(depth + 1) * dy
            edges.append((x, y, xc, yc))
        return x

    root = {'nhan': goc, 'con': con}
    walk(root, 0)

    # chuẩn hoá tâm ngang về 0
    xs_all = [n[0] for n in nodes]
    off = (min(xs_all) + max(xs_all)) / 2.0
    for n in nodes:
        n[0] = (n[0] - off) * dx
    E = [((a - off) * dx, b, (c - off) * dx, d) for (a, b, c, d) in edges]

    # ---- 2) dựng TikZ (xelatex + fontspec DejaVu Serif) ----
    t = [r'\documentclass[border=8pt]{standalone}',
         r'\usepackage{fontspec}',
         r'\setmainfont{DejaVu Serif}',
         r'\usepackage{tikz}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,line join=round,'
         r'nutS/.style={circle,fill=black,inner sep=1.7pt},'
         r'lbl/.style={font=\small,fill=white,inner sep=1.2pt},'
         r'lblLa/.style={font=\scriptsize,inner sep=1pt}]' % scale]
    for (x1, y1, x2, y2) in E:
        t.append(r'\draw (%.4f,%.4f) -- (%.4f,%.4f);' % (x1, y1, x2, y2))
    for (x, y, nhan, la, is_root, is_leaf) in nodes:
        fill = 'orange' if is_root else 'black'
        t.append(r'\node[nutS,fill=%s] at (%.4f,%.4f) {};' % (fill, x, y))
        if nhan:
            if is_root:
                anchor, dyl = 'south', 0.34
            elif is_leaf:
                anchor, dyl = 'north', -0.30
            else:                               # nút trong: nhãn trên, nền trắng che cạnh
                anchor, dyl = 'south', 0.32
            t.append(r'\node[lbl,anchor=%s] at (%.4f,%.4f) {%s};'
                     % (anchor, x, y + dyl, _esc(nhan)))
        if la:
            t.append(r'\node[lblLa,anchor=north] at (%.4f,%.4f) {%s};'
                     % (x, y - 0.62, _esc(la)))
    t.append(r'\end{tikzpicture}\end{document}')
    return _render_xe('\n'.join(t), out, tra_bytes)
