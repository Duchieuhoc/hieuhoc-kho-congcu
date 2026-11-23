#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hoa_ch06.py — ENTRY chương: Hóa (KHTN) lớp 9 Chương VI
#   "Kim loại. Sự khác nhau cơ bản giữa phi kim và kim loại".
#   Dựng SƠ ĐỒ THÍ NGHIỆM (dụng cụ) — họ còn thiếu trong kho:
#     • thi_nghiem_binh_khi  : kim loại cháy trong bình khí (phi kim)
#       → phủ Fe+O2, Na+Cl2, Fe+Cl2 (mục ② B18, Đ22.5 bắt buộc hình)
#     • mach_thu_dan_dien    : mạch điện thử tính dẫn điện (SBT 18.10)
#     • thi_nghiem_dan_nhiet : thìa dẫn nhiệt trong bát nước (SBT 18.11)
#   Generator ĐỘC LẬP, NGHĨA-THUẦN: hàm nhận NGHĨA (tên thí nghiệm /
#   màu khí / kiểu giá mẫu), MÁY tự bố trí (layout ẩn trong kho, Đ5.9);
#   PHANH ngữ nghĩa → sai thì DỪNG. Xuất PNG buffer (hinhVe/hinhBenPhai).
#   Text trong hình CHỈ ASCII/ký hiệu hoá (O_2, Cl_2, Na, Fe, Fe_3O_4…);
#   chú thích tiếng Việt đặt ở Word (pdflatex không dựng dấu tiếng Việt).
#   [36a ĐỀ XUẤT] Ông Bụt (Hóa) 2026-11-23. ADDITIVE — 0 đổi hàm cũ.
# ═══════════════════════════════════════════════════════════════════
import hinh_core as _HC

LOP_MODULE = [9]
CUA_RENDER = {'thi_nghiem_binh_khi', 'phan_ung_phi_kim',
              'mach_thu_dan_dien', 'thi_nghiem_dan_nhiet'}

# Preamble TikZ chung cho module (màu dụng cụ + thư viện lò xo/mũi tên)
_PRE = (r'\documentclass[border=5pt]{standalone}'
        r'\usepackage{tikz}\usepackage{amsmath}'
        r'\usetikzlibrary{arrows.meta,decorations.pathmorphing}'
        r'\definecolor{thuytinh}{RGB}{90,120,140}'
        r'\definecolor{o2gas}{RGB}{226,244,250}'
        r'\definecolor{clgas}{RGB}{206,228,116}'
        r'\definecolor{feoxide}{RGB}{96,46,34}'
        r'\definecolor{fecl3}{RGB}{150,64,44}'
        r'\definecolor{muoitr}{RGB}{245,245,245}'
        r'\definecolor{kimloai}{RGB}{120,124,130}'
        r'\begin{document}')

def _doc(body):
    return _PRE + r'\begin{tikzpicture}[line join=round,line cap=round]' + body + \
           r'\end{tikzpicture}\end{document}'

# ── Bình thu khí miệng rộng + nắp (lọ thuỷ tinh) ──────────────────
def _binh(mau_khi):
    """Thân lọ thu khí: khung thuỷ tinh + nền khí màu + nắp đậy."""
    return (
        # nền khí (bên trong)
        f"\\fill[{mau_khi}] (-1.15,-2.05) rectangle (1.15,1.15);\n"
        # thành thuỷ tinh
        r"\draw[thuytinh,line width=1.5pt] (-1.2,1.2) -- (-1.2,-2.0)"
        r" arc (180:270:0.2) -- (1.0,-2.2) arc (270:360:0.2) -- (1.2,1.2);"
        "\n"
        # nắp/miệng lọ
        r"\draw[thuytinh,line width=1.5pt] (-1.4,1.2) rectangle (1.4,1.5);"
        r"\fill[thuytinh!25] (-1.4,1.2) rectangle (1.4,1.5);"
    )

# ── Giá mẫu: muỗng đốt (spoon) hoặc dây lò xo (coil) ──────────────
def _muong(sample, glow):
    """Muỗng đốt: cán xuyên nắp → đĩa nhỏ chứa mẫu + quầng cháy."""
    s = (r"\draw[kimloai,line width=1.6pt] (0,1.5) -- (0,-0.35);"
         r"\draw[kimloai,line width=1.6pt] (-0.28,-0.5) arc (180:360:0.28);")  # đĩa muỗng
    s += f"\\shade[ball color={glow}] (0,-0.5) circle (0.2);"
    s += _quang(0, -0.5, glow)
    if sample:
        s += f"\\node[font=\\footnotesize\\bfseries,black] at (0,-0.95) {{${sample}$}};"
    return s

def _loxo(sample, glow):
    """Dây kim loại uốn lò xo treo từ nắp, đang cháy sáng."""
    s = (r"\draw[kimloai,line width=1.6pt] (0,1.5) -- (0,0.2);"
         r"\draw[kimloai,line width=1.5pt,decorate,"
         r"decoration={coil,amplitude=5pt,segment length=5pt}] (0,0.2) -- (0,-0.9);")
    s += _quang(0, -0.35, glow)
    if sample:
        s += f"\\node[font=\\footnotesize\\bfseries,black] at (0.72,0.1) {{${sample}$}};"
    return s

def _quang(x, y, glow):
    """Quầng cháy sáng: lõi sáng + tia toé."""
    out = f"\\shade[ball color={glow}!90!white] ({x},{y}) circle (0.26);"
    import math
    for k in range(8):
        a = k * 45
        dx, dy = 0.52 * math.cos(math.radians(a)), 0.52 * math.sin(math.radians(a))
        ex, ey = 0.30 * math.cos(math.radians(a)), 0.30 * math.sin(math.radians(a))
        out += f"\\draw[{glow}!80!red,line width=1pt] ({x+ex:.2f},{y+ey:.2f})--({x+dx:.2f},{y+dy:.2f});"
    return out

# ═══════════ ENGINE — thi_nghiem_binh_khi ═══════════
def thi_nghiem_binh_khi(mau_khi, kieu_gia, nhan_khi=None, nhan_mau=None,
                        nhan_sp=None, mau_sp=None, out='hoa6_binhkhi', tra_bytes=False):
    """Kim loại cháy trong BÌNH KHÍ (sơ đồ thí nghiệm tác dụng với phi kim).
       mau_khi : màu nền khí trong bình ('o2gas' | 'clgas' | …).
       kieu_gia: 'loxo' (dây kim loại uốn lò xo) | 'muong' (muỗng đốt chứa mẫu).
       nhan_mau: ký hiệu mẫu kim loại trên giá (vd 'Fe', 'Na') — ASCII/math.
       nhan_khi: ký hiệu khí trong bình (vd 'O_2', 'Cl_2').
       nhan_sp / mau_sp: ký hiệu + màu sản phẩm đọng đáy bình (vd 'Fe_3O_4','feoxide').
       PHANH: kieu_gia ∈ {loxo,muong}."""
    if kieu_gia not in ('loxo', 'muong'):
        raise ValueError(f"[PHANH hoa6] kieu_gia='{kieu_gia}' lạ (chỉ 'loxo'|'muong').")
    glow = 'orange'
    body = _binh(mau_khi)
    body += _loxo(nhan_mau, glow) if kieu_gia == 'loxo' else _muong(nhan_mau, glow)
    # sản phẩm đáy bình
    if nhan_sp:
        c = mau_sp or 'feoxide'
        chu = 'black' if c in ('muoitr',) else 'white'   # nền sáng → chữ đen
        body += f"\\fill[{c}] (-0.8,-1.95) .. controls (-0.3,-1.6) and (0.3,-1.6) .. (0.8,-1.95) -- cycle;"
        body += f"\\node[font=\\scriptsize\\bfseries,{chu}] at (0,-1.75) {{${nhan_sp}$}};"
    # nhãn khí (góc trên trong bình)
    if nhan_khi:
        body += f"\\node[font=\\footnotesize\\bfseries,thuytinh!60!black] at (0.75,0.95) {{${nhan_khi}$}};"
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)

# ── Registry 3 thí nghiệm chuẩn B18 (NGHĨA-THUẦN, gọi theo tên) ──
_TN = {
    'Fe_O2':  dict(mau_khi='o2gas', kieu_gia='loxo',  nhan_khi='O_2',
                   nhan_mau='Fe', nhan_sp='Fe_3O_4', mau_sp='feoxide'),
    'Na_Cl2': dict(mau_khi='clgas', kieu_gia='muong', nhan_khi='Cl_2',
                   nhan_mau='Na', nhan_sp='NaCl', mau_sp='muoitr'),
    'Fe_Cl2': dict(mau_khi='clgas', kieu_gia='loxo',  nhan_khi='Cl_2',
                   nhan_mau='Fe', nhan_sp='FeCl_3', mau_sp='fecl3'),
}

def phan_ung_phi_kim(ten, out=None, tra_bytes=False):
    """Gọi NHANH 1 trong 3 sơ đồ thí nghiệm chuẩn của B18 theo TÊN:
       'Fe_O2' (sắt cháy trong oxygen) · 'Na_Cl2' (natri + chlorine) ·
       'Fe_Cl2' (sắt + chlorine). PHANH: tên phải có trong registry."""
    if ten not in _TN:
        raise ValueError(f"[PHANH hoa6] chưa có thí nghiệm '{ten}' (có: {sorted(_TN)}).")
    sp = dict(_TN[ten]);
    # sản phẩm NaCl trắng → chữ nhãn đen cho dễ đọc
    kw = dict(sp)
    return thi_nghiem_binh_khi(out=out or f'hoa6_{ten}', tra_bytes=tra_bytes, **kw)

# ═══════════ SBT 18.10 — mạch điện thử tính dẫn điện ═══════════
def mach_thu_dan_dien(out='hoa6_mach', tra_bytes=False):
    """Mạch nối tiếp thử tính dẫn điện: pin -> công tắc -> bóng đèn ->
       hai kẹp vật liệu (vật cần thử kẹp giữa). CẤM lộ đáp án (Đ41.4):
       KHÔNG tô sáng/không-sáng. Nhãn ASCII: '1,5V', 'K', vật thử để trống."""
    body = (
        # khung dây chữ nhật
        r"\draw[black,line width=1.2pt] (-2.6,-1.4) rectangle (2.6,1.4);"
        # pin 1,5V (cạnh dưới)
        r"\draw[black,line width=1.2pt] (-0.35,-1.4) -- (-0.35,-1.75);"
        r"\draw[black,line width=1.2pt] (0.35,-1.4) -- (0.35,-1.75);"
        r"\draw[black,line width=2.4pt] (-0.35,-1.95) -- (-0.35,-1.55);"   # bản dài (+)
        r"\draw[black,line width=1.2pt] (0.35,-1.85) -- (0.35,-1.65);"     # bản ngắn (-)
        r"\draw[black,line width=1.2pt] (-0.35,-1.75) -- (0.35,-1.75);"
        r"\node[font=\scriptsize] at (0,-2.2) {1,5V};"
        # công tắc K (cạnh trên trái)
        r"\fill (-1.6,1.4) circle (0.05);\fill (-0.8,1.4) circle (0.05);"
        r"\draw[black,line width=1.2pt] (-1.6,1.4) -- (-0.75,1.72);"
        r"\node[font=\scriptsize] at (-1.2,1.95) {K};"
        # bóng đèn (cạnh trên phải) — vòng tròn + chữ thập
        r"\draw[black,line width=1.2pt,fill=white] (1.4,1.4) circle (0.34);"
        r"\draw[black,line width=1pt] (1.16,1.16) -- (1.64,1.64);"
        r"\draw[black,line width=1pt] (1.16,1.64) -- (1.64,1.16);"
        # hai kẹp vật liệu (cạnh phải) + khe kẹp vật thử
        r"\draw[black,line width=1.2pt] (2.6,0.4) -- (3.05,0.4);"
        r"\draw[black,line width=1.2pt] (2.6,-0.4) -- (3.05,-0.4);"
        r"\draw[black,line width=2pt] (3.05,0.62) -- (3.05,0.18);"
        r"\draw[black,line width=2pt] (3.05,-0.18) -- (3.05,-0.62);"
        r"\draw[black,dashed,line width=0.8pt] (3.05,0.3) rectangle (3.75,-0.3);"
        r"\node[font=\scriptsize] at (3.4,-0.75) {(?)};"
    )
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)

# ═══════════ SBT 18.11 — thìa dẫn nhiệt trong bát nước ═══════════
def thi_nghiem_dan_nhiet(out='hoa6_nhiet', tra_bytes=False):
    """Hai bát: 'HOT' (nước nóng ~90C) và 'ICE' (nước đá); mỗi bát cắm
       4 thìa (kim loại / nhựa / gỗ / sứ). CẤM lộ đáp án (Đ41.4): không
       đánh dấu thìa nào nóng nhanh. Nhãn thìa ASCII: KL, Nh, Go, Su."""
    def bat(cx, nhan, mau_nuoc):
        s = (f"\\fill[{mau_nuoc}] ({cx-1.15},0.0) .. controls ({cx-1.0},-0.95) and "
             f"({cx+1.0},-0.95) .. ({cx+1.15},0.0) -- cycle;"
             f"\\draw[black,line width=1.3pt] ({cx-1.25},0.15) .. controls ({cx-1.05},-1.05) and "
             f"({cx+1.05},-1.05) .. ({cx+1.25},0.15);"
             f"\\draw[black,line width=1.3pt] ({cx-1.25},0.15) -- ({cx+1.25},0.15);")
        labs = ['KL', 'Nh', 'Go', 'Su']
        for i, xx in enumerate([-0.75, -0.25, 0.25, 0.75]):
            s += (f"\\draw[kimloai,line width=1.4pt] ({cx+xx},0.9) -- ({cx+xx},-0.5);"
                  f"\\node[font=\\tiny] at ({cx+xx},1.1) {{{labs[i]}}};")
        s += f"\\node[font=\\scriptsize\\bfseries] at ({cx},-1.35) {{{nhan}}};"
        return s
    body = bat(-1.7, 'HOT', 'red!18!white') + bat(1.7, 'ICE', 'cyan!22!white')
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
