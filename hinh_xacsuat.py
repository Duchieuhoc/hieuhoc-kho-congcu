# -*- coding: utf-8 -*-
# hinh_xacsuat.py — XÁC SUẤT: SƠ ĐỒ HÌNH CÂY (cây xác suất) — dùng chung DS10_CH09 + DS12_CH06.
# Generator ĐỘC LẬP (như hinh_ds12_giaitich.py / hinh_ds10_ch06.py) — KHÔNG đụng file dùng chung / hinh_core CHUNG.
#   Render qua hinh_core.render_tikz_doc (pdflatex + pdftoppm). Nhãn math-mode (pdflatex-safe);
#   Đ/đ (bút Đen) qua \newunicodechar; biến cố đối \overline{A} an toàn. KHÔNG nhúng ảnh SGK (Đ42).
# [pilot DS12_CH06 B18] 2026-10-21 — OB Đại số THPT dựng builder sơ đồ cây (HP Đ5.9) cho chương Xác suất có điều kiện.
#   Máy nhận NGHĨA (gốc + các tầng nhánh: nhãn nút · nhãn xác suất trên nhánh · nhãn lá) → TỰ dàn ngang,
#   TỰ đặt nhãn xác suất giữa cạnh. Tổng quát: cây 1 tầng hoặc 2 tầng, phân nhánh tùy ý (2,3,… con mỗi nút).
import hinh_core as _HC


def so_do_cay(goc='O', cap1=None, cap2=None,
              out='so_do_cay', tra_bytes=False, scale=1.0,
              dx=2.4, dy=2.3):
    r"""SƠ ĐỒ HÌNH CÂY xác suất (tikz) — chuẩn SGK (gốc trên, nhánh tỏa xuống).
       goc  : nhãn gốc (math-string). VD 'O' · r'Gốc\ O'.
       cap1 : list nút TẦNG 1, mỗi nút là dict:
                {'nhan': <nhãn nút, math-string vd 'A' · r'\overline{A}' · 'Đ'>,
                 'xs'  : <nhãn xác suất TRÊN nhánh gốc→nút, vd r'\frac{5}{12}' · '0,4'>}
       cap2 : list (CÙNG độ dài cap1) — cap2[i] là list CON của nút cap1[i], mỗi con là dict:
                {'nhan': <nhãn nút lá>, 'xs': <xs trên nhánh>, 'la': <nhãn kết quả dưới lá, optional>}.
              Cây 1 TẦNG: để cap2=None (hoặc []) → chỉ vẽ gốc → tầng 1 (các lá).
       dx, dy : khoảng cách ngang giữa lá / dọc giữa tầng.
       PHANH: len(cap2)==len(cap1) khi cap2 có; mỗi nhánh nên có 'xs'."""
    cap1 = cap1 or []
    assert len(cap1) >= 2, "[CAY] can >= 2 nhanh tang 1"
    hai_tang = bool(cap2)
    if hai_tang:
        assert len(cap2) == len(cap1), "[CAY] cap2 phai cung do dai cap1"

    # ---- bố trí tọa độ: dàn LÁ đều hàng dưới, nút cha = trung bình các con ----
    def _wrap(s):  # bọc $...$ an toàn (math-mode), giữ nguyên nếu đã là lệnh
        return r'$%s$' % s

    pos1 = []   # (x,y) nút tầng 1
    pos2 = []   # list[list[(x,y)]] nút tầng 2
    if hai_tang:
        la_x = []
        k = 0
        for con in cap2:
            xs_con = [k + j for j in range(len(con))]
            k += len(con)
            la_x.append(xs_con)
        tongla = k
        # chuẩn hóa về tâm 0
        off = (tongla - 1) / 2.0
        y1, y2 = -dy, -2 * dy
        for i, con in enumerate(cap2):
            xs_con = [(ix - off) * dx for ix in la_x[i]]
            pos2.append([(x, y2) for x in xs_con])
            pos1.append((sum(xs_con) / len(xs_con), y1))
    else:
        n = len(cap1)
        off = (n - 1) / 2.0
        y1 = -dy
        for i in range(n):
            pos1.append(((i - off) * dx, y1))

    xg = sum(p[0] for p in pos1) / len(pos1)   # gốc = trung bình tầng 1
    goc_xy = (xg, 0.0)

    # ---- dựng TikZ ----
    t = [r'\documentclass[border=5pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath,amssymb}',
         r'\usepackage[T1]{fontenc}\usepackage{newunicodechar}'
         r'\newunicodechar{Đ}{\text{\DJ}}\newunicodechar{đ}{\text{\dj}}',
         r'\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,line join=round,'
         r'nutS/.style={circle,fill=black,inner sep=1.7pt},'
         r'xsL/.style={font=\small,fill=white,inner sep=1pt}]' % scale]

    def _edge(p, q, xs, trai):
        # cạnh p->q + nhãn xác suất giữa cạnh (lệch sang trái/phải cho khỏi đè cạnh)
        t.append(r'\draw (%g,%g) -- (%g,%g);' % (p[0], p[1], q[0], q[1]))
        if xs:
            mx, my = (p[0] + q[0]) / 2.0, (p[1] + q[1]) / 2.0
            t.append(r'\node[xsL] at (%g,%g) {$%s$};' % (mx + (-0.28 if trai else 0.28), my, xs))

    # gốc
    t.append(r'\node[nutS,fill=orange] (G) at (%g,%g) {};' % goc_xy)
    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (goc_xy[0], goc_xy[1] + 0.33, goc))
    # tầng 1
    for i, (p1, c1) in enumerate(zip(pos1, cap1)):
        trai = p1[0] < goc_xy[0]
        _edge(goc_xy, p1, c1.get('xs'), trai)
        col = 'blue' if (not hai_tang and False) else 'black'
        t.append(r'\node[nutS] at (%g,%g) {};' % p1)
        # nhãn nút tầng 1: đặt phía trên-ngoài
        t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (p1[0] + (-0.3 if trai else 0.3), p1[1] + 0.28, c1['nhan']))
        if hai_tang:
            for q, c2 in zip(pos2[i], cap2[i]):
                traiC = q[0] < p1[0]
                _edge(p1, q, c2.get('xs'), traiC)
                t.append(r'\node[nutS] at (%g,%g) {};' % q)
                t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (q[0] + (-0.28 if traiC else 0.28), q[1] - 0.05, c2['nhan']))
                if c2.get('la'):
                    t.append(r'\node[font=\small] at (%g,%g) {$%s$};' % (q[0], q[1] - 0.5, c2['la']))

    t.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(t), out, tra_bytes, dpi=200)
