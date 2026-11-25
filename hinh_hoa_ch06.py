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
              'mach_thu_dan_dien', 'thi_nghiem_dan_nhiet',
              'ong_nghiem_phan_ung', 'thi_nghiem_day_hoat_dong',
              'be_dien_phan_nhom', 'lo_cao_luyen_gang', 'lo_thoi_luyen_thep',
              'cot_loc_than'}

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
        r'\definecolor{ddhcl}{RGB}{230,239,228}'
        r'\definecolor{ddxanh}{RGB}{150,205,222}'
        r'\definecolor{bacxam}{RGB}{150,150,156}'
        r'\definecolor{nuocmau}{RGB}{198,110,165}'
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


# ═══════════════════════════════════════════════════════════════════
# [36b] HỌ ỐNG NGHIỆM PHẢN ỨNG — Dãy hoạt động hoá học (B19)
# ═══════════════════════════════════════════════════════════════════
def _ong_nghiem(mau_dd, muc=1.0):
    """Ống nghiệm đứng đáy tròn + nền dung dịch màu (mức chất lỏng = muc)."""
    tube = (r"\draw[thuytinh,line width=1.4pt] (-0.55,2.2) -- (-0.55,-1.5) "
            r"arc (180:360:0.55) -- (0.55,2.2);")
    # vành miệng loe nhẹ
    tube += (r"\draw[thuytinh,line width=1.4pt] (-0.62,2.26) -- (-0.55,2.2);"
             r"\draw[thuytinh,line width=1.4pt] (0.55,2.2) -- (0.62,2.26);")
    # nền dung dịch (clip theo lòng ống)
    fill = (r"\begin{scope}"
            r"\clip (-0.55,2.2) -- (-0.55,-1.5) arc (180:360:0.55) -- (0.55,2.2) -- cycle;"
            f"\\fill[{mau_dd}] (-0.65,-2.1) rectangle (0.65,{muc});"
            r"\end{scope}")
    return fill + tube   # dung dịch dưới, thành ống trên

def _dinh_sat():
    """Đinh sắt: mũ dẹt + thân + mũi nhọn, cắm trong dung dịch."""
    return (r"\fill[kimloai] (-0.15,0.95) rectangle (0.15,0.78);"    # mũ đinh
            r"\fill[kimloai] (-0.055,0.78) rectangle (0.055,-1.05);" # thân
            r"\fill[kimloai] (-0.055,-1.05) -- (0.055,-1.05) -- (0,-1.35) -- cycle;")  # mũi

def _bot_khi(xs):
    """Bọt khí nhỏ quanh vật (danh sách (x,y))."""
    s = ""
    for (x, y) in xs:
        s += f"\\draw[thuytinh,line width=0.7pt,fill=white] ({x},{y}) circle (0.045);"
    return s

def ong_nghiem_phan_ung(mau_dd, vat, nhan_vat=None, nhan_dd=None, bot=False,
                        bam=None, out='hoa6_ong', tra_bytes=False):
    """Kim loại phản ứng trong ỐNG NGHIỆM (thí nghiệm dãy hoạt động hoá học).
       mau_dd : màu dung dịch ('ddhcl' | 'ddxanh' | …).
       vat    : 'dinh' (đinh sắt) | 'loxo' (dây kim loại uốn lò xo).
       nhan_vat / nhan_dd : ký hiệu hoá học ASCII (vd 'Fe','Cu' | 'HCl','AgNO_3').
       bot    : True → vẽ bọt khí quanh vật (kim loại đẩy H2).
       bam    : màu lớp kim loại mới bám trên vật (vd 'bacxam' cho Ag bám lên Cu); None nếu không.
       PHANH: vat ∈ {dinh,loxo}."""
    if vat not in ('dinh', 'loxo'):
        raise ValueError(f"[PHANH hoa6] vat='{vat}' lạ (chỉ 'dinh'|'loxo').")
    body = _ong_nghiem(mau_dd)
    if vat == 'dinh':
        body += _dinh_sat()
        if bot:
            body += _bot_khi([(0.22, 0.4), (-0.2, 0.0), (0.18, -0.4), (-0.17, -0.8), (0.1, 0.7)])
    else:  # lò xo
        coilcol = bam or 'kimloai'
        if bam:  # lớp kim loại mới bám dày hơn, lõi kim loại thấy mờ
            body += (f"\\draw[{bam},line width=3pt,decorate,"
                     r"decoration={coil,amplitude=4.5pt,segment length=4.5pt}] (0,1.55) -- (0,-1.15);")
        body += (r"\draw[kimloai,line width=1.5pt,decorate,"
                 r"decoration={coil,amplitude=4.5pt,segment length=4.5pt}] (0,1.55) -- (0,-1.15);")
        if bot:
            body += _bot_khi([(0.22, 0.3), (-0.2, -0.2), (0.18, -0.6)])
    # nhãn vật (phải) + dung dịch (trái) — leader mảnh
    if nhan_vat:
        body += (f"\\node[font=\\footnotesize\\bfseries,black] at (1.15,0.5) {{${nhan_vat}$}};"
                 r"\draw[gray,line width=0.5pt] (0.95,0.5) -- (0.2,0.2);")
    if nhan_dd:
        body += (f"\\node[font=\\footnotesize,black,align=center] at (-1.25,-0.5) {{${nhan_dd}$}};"
                 r"\draw[gray,line width=0.5pt] (-0.9,-0.5) -- (-0.3,-0.6);")
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)

_ONG = {
    'Fe_HCl':   dict(mau_dd='ddhcl', vat='dinh', nhan_vat='Fe', nhan_dd='HCl', bot=True),
    'Cu_AgNO3': dict(mau_dd='ddxanh', vat='loxo', nhan_vat='Cu', nhan_dd='AgNO_3', bam='bacxam'),
}

def thi_nghiem_day_hoat_dong(ten, out=None, tra_bytes=False):
    """Gọi NHANH thí nghiệm dãy hoạt động hoá học B19 theo TÊN:
       'Fe_HCl' (đinh sắt + dd HCl, sủi bọt) · 'Cu_AgNO3' (dây đồng lò xo + dd AgNO3,
       bạc xám bám, dd hoá xanh). PHANH: tên phải có trong registry."""
    if ten not in _ONG:
        raise ValueError(f"[PHANH hoa6] chưa có thí nghiệm '{ten}' (có: {sorted(_ONG)}).")
    return ong_nghiem_phan_ung(out=out or f'hoa6_{ten}', tra_bytes=tra_bytes, **_ONG[ten])


# ═══════════════════════════════════════════════════════════════════
# [36c] SƠ ĐỒ CÔNG NGHIỆP — Tách kim loại (B20). Nhãn tiếng Việt KHÔNG
#   dựng được bằng pdflatex → dùng CALLOUT SỐ trong hình + chú giải ở Word.
#   Mỗi hàm trả kèm .CHU_GIAI (dict số→nghĩa) để AI Soạn in chú giải.
# ═══════════════════════════════════════════════════════════════════
def _callout(x, y, n):
    return (f"\\node[circle,draw,fill=white,line width=0.8pt,inner sep=1.3pt,"
            f"font=\\scriptsize\\bfseries] at ({x},{y}) {{{n}}};")

CHU_GIAI_DIEN_PHAN = {1: 'Cực dương bằng than chì (+)', 2: 'Cực âm bằng than chì (−)',
    3: 'Hỗn hợp Al₂O₃ và cryolite nóng chảy', 4: 'Al nóng chảy', 5: 'Al lỏng tháo ra'}

def be_dien_phan_nhom(out='hoa6_dienphan', tra_bytes=False):
    """Sơ đồ bể điện phân aluminium oxide nóng chảy (gốc Hình 20.1).
       Callout 1–5; chú giải xem be_dien_phan_nhom.CHU_GIAI / CHU_GIAI_DIEN_PHAN."""
    body = (
        # thùng điện phân (lớp than chì = cực âm) — thành dày
        r"\draw[kimloai,line width=5pt] (-3.1,1.6) -- (-3.1,-1.9) -- (3.1,-1.9) -- (3.1,1.6);"
        # nền hỗn hợp nóng chảy
        r"\fill[ddxanh!55!white] (-2.9,-1.5) rectangle (2.9,1.2);"
        # lớp Al nóng chảy lắng đáy
        r"\fill[kimloai!70!white] (-2.9,-1.75) rectangle (2.9,-1.3);"
        r"\node[font=\footnotesize\bfseries,white] at (0,-1.52) {Al};"
        # 3 cực dương than chì nhúng từ trên
    )
    for cx in (-1.7, 0.0, 1.7):
        body += (f"\\fill[kimloai!40!black] ({cx-0.33},2.3) rectangle ({cx+0.33},-0.3);"
                 f"\\node[font=\\scriptsize\\bfseries,white] at ({cx},1.8) {{+}};")
    # dấu cực âm trên thành
    body += r"\node[font=\footnotesize\bfseries] at (-3.45,-0.1) {$-$};"
    body += r"\node[font=\footnotesize\bfseries] at (3.45,-0.1) {$-$};"
    # cửa tháo Al lỏng (đáy phải) + mũi tên ra
    body += (r"\fill[kimloai!70!white] (3.1,-1.75) -- (3.6,-1.95) -- (3.6,-1.5) -- (3.1,-1.4) -- cycle;"
             r"\draw[-{Stealth},line width=1.2pt,kimloai!40!black] (3.6,-1.72) -- (4.15,-1.72);")
    # callouts
    body += _callout(0.0, 2.55, 1)      # cực dương
    body += _callout(-3.75, 0.5, 2)     # cực âm
    body += _callout(2.2, 0.6, 3)       # hỗn hợp nóng chảy
    body += _callout(-2.35, -1.5, 4)    # Al nóng chảy
    body += _callout(4.05, -1.4, 5)     # Al lỏng tháo ra
    out_b = _HC.render_tikz_doc(_doc(body), out, tra_bytes)
    return out_b
be_dien_phan_nhom.CHU_GIAI = CHU_GIAI_DIEN_PHAN


CHU_GIAI_LO_CAO = {1: 'Quặng sắt, than cốc, đá vôi', 2: 'Khí lò cao thoát ra',
    3: 'Nguyên liệu đi xuống', 4: 'Hỗn hợp khí đi lên', 5: 'Không khí nóng',
    6: 'Cửa tháo xỉ', 7: 'Cửa tháo gang'}

def lo_cao_luyen_gang(out='hoa6_locao', tra_bytes=False):
    """Sơ đồ lò cao luyện gang (gốc Hình 20.2). Callout 1–7; chú giải CHU_GIAI_LO_CAO."""
    prof = ("(-0.9,2.6) -- (-0.9,2.0) -- (-1.75,0.2) -- (-1.0,-1.8) -- (-1.0,-2.2) -- "
            "(1.0,-2.2) -- (1.0,-1.8) -- (1.75,0.2) -- (0.9,2.0) -- (0.9,2.6)")
    body = (
        f"\\fill[ddhcl!60!white] {prof.replace(' -- ', ' -- ')} -- cycle;"
        f"\\draw[kimloai,line width=3pt] {prof};"
        # miệng lò + phễu nạp liệu
        r"\draw[kimloai,line width=2pt] (-0.9,2.6) -- (0.9,2.6);"
        r"\draw[kimloai,line width=1.6pt] (-0.75,3.25) -- (-0.35,2.68) -- (0.35,2.68) -- (0.75,3.25);"
        r"\draw[-{Stealth},line width=1.3pt] (0,3.15) -- (0,2.75);"         # nạp liệu xuống
        # ống thu khí lò cao (trái, đi lên)
        r"\draw[kimloai,line width=1.6pt] (-0.9,2.35) -- (-1.7,2.35) -- (-1.7,3.2);"
        r"\draw[-{Stealth},line width=1.3pt,gray] (-1.7,2.9) -- (-1.7,3.5);"
        # mũi tên trong lò: nguyên liệu xuống (trái) + khí lên (phải)
        r"\draw[-{Stealth},line width=1.3pt] (-0.5,1.3) -- (-0.5,-0.9);"
        r"\draw[-{Stealth},line width=1.3pt,gray] (0.5,-0.9) -- (0.5,1.3);"
        # tuyere: không khí nóng thổi vào hai bên (y ~ -1.4)
        r"\draw[-{Stealth},line width=1.3pt,fecl3] (-2.0,-1.4) -- (-1.15,-1.4);"
        r"\draw[-{Stealth},line width=1.3pt,fecl3] (2.0,-1.4) -- (1.15,-1.4);"
        # cửa tháo xỉ (trái, trên) + mũi tên ra
        r"\draw[kimloai,line width=1.6pt] (-1.0,-1.0) -- (-1.5,-1.1);"
        r"\draw[-{Stealth},line width=1.1pt] (-1.5,-1.1) -- (-1.95,-1.2);"
        # cửa tháo gang (đáy phải) + mũi tên ra
        r"\draw[kimloai,line width=1.8pt] (1.0,-2.0) -- (1.6,-2.15);"
        r"\draw[-{Stealth},line width=1.3pt,kimloai!40!black] (1.6,-2.15) -- (2.15,-2.25);"
    )
    body += _callout(0.0, 3.5, 1)     # nạp liệu
    body += _callout(-1.7, 3.75, 2)   # khí lò cao
    body += _callout(-0.5, 0.2, 3)    # nguyên liệu xuống
    body += _callout(0.5, 0.2, 4)     # khí lên
    body += _callout(2.25, -1.4, 5)   # không khí nóng (nhãn ở tuyere phải; hai bên đối xứng)
    body += _callout(-2.2, -1.1, 6)   # cửa tháo xỉ
    body += _callout(2.35, -2.25, 7)  # cửa tháo gang
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
lo_cao_luyen_gang.CHU_GIAI = CHU_GIAI_LO_CAO


CHU_GIAI_LO_THOI = {1: 'Gang lỏng', 2: 'Khí oxygen (ống thổi)'}

def lo_thoi_luyen_thep(out='hoa6_lothoi', tra_bytes=False):
    """Sơ đồ lò thổi luyện thép (gốc Hình 20.3). Callout 1–2; chú giải CHU_GIAI_LO_THOI."""
    vessel = (r"(-0.5,1.9) .. controls (-1.15,1.5) and (-1.35,1.0) .. (-1.35,0.4) -- (-1.35,-0.9) "
              r".. controls (-1.35,-1.7) and (1.35,-1.7) .. (1.35,-0.9) -- (1.35,0.4) "
              r".. controls (1.35,1.0) and (1.15,1.5) .. (0.5,1.9)")
    body = (
        # nền gang lỏng (clip trong lò)
        r"\begin{scope}"
        f"\\clip {vessel} -- cycle;"
        r"\fill[orange!55!red!85] (-1.5,-1.7) rectangle (1.5,0.75);"
        r"\end{scope}"
        f"\\draw[kimloai,line width=2.6pt] {vessel};"
        # ống thổi oxygen (lance) từ trên xuống trong lò
        r"\draw[kimloai,line width=3pt] (0,3.0) -- (0,0.55);"
        r"\draw[-{Stealth},line width=1.4pt,thuytinh!60!black] (0,0.5) -- (0,-0.1);"
        r"\node[font=\footnotesize\bfseries] at (0.5,2.5) {$O_2$};"
        # vài tia lửa ở miệng
        r"\draw[orange!80!red,line width=1pt] (-0.35,1.95) -- (-0.5,2.3);"
        r"\draw[orange!80!red,line width=1pt] (0.35,1.95) -- (0.5,2.3);"
        r"\draw[orange!80!red,line width=1pt] (0,2.0) -- (0.12,2.4);"
    )
    body += _callout(1.05, -0.6, 1)   # gang lỏng
    body += _callout(-0.45, 2.75, 2)  # ống thổi oxygen
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
lo_thoi_luyen_thep.CHU_GIAI = CHU_GIAI_LO_THOI


# ═══════════════════════════════════════════════════════════════════
# [36d] CỘT LỌC THAN — thí nghiệm hấp phụ (B21). Callout + chú giải Word.
# ═══════════════════════════════════════════════════════════════════
CHU_GIAI_COT_THAN = {1: 'Nước màu', 2: 'Bông', 3: 'Bột than gỗ', 4: 'Bông',
    5: 'Cốc thuỷ tinh (dung dịch mất màu)'}

def cot_loc_than(out='hoa6_cotthan', tra_bytes=False):
    """Thí nghiệm hấp phụ của bột than gỗ (gốc Hình 21.1). Callout 1–5; chú giải CHU_GIAI_COT_THAN."""
    funnel = (r"(-0.95,2.4) -- (-0.22,0.55) -- (-0.22,-0.55) -- (0.22,-0.55) -- (0.22,0.55) -- (0.95,2.4)")
    body = (
        # giá đỡ
        r"\draw[kimloai,line width=2.5pt] (-2.3,-1.9) -- (-2.3,2.6);"
        r"\fill[kimloai] (-2.45,-1.95) rectangle (-1.0,-1.8);"            # chân đế
        r"\draw[kimloai,line width=2pt] (-2.3,1.35) -- (-0.75,1.35);"    # kẹp
        # các lớp trong phễu (clip theo phễu)
        r"\begin{scope}"
        f"\\clip {funnel} -- cycle;"
        r"\fill[nuocmau!75] (-1.1,2.4) rectangle (1.1,0.95);"            # nước màu (trên)
        r"\fill[white] (-1.1,0.95) rectangle (1.1,0.72);"               # bông
        r"\draw[gray,line width=0.4pt] (-1.1,0.83) -- (1.1,0.83);"
        r"\fill[black!88] (-1.1,0.72) rectangle (1.1,0.12);"            # bột than gỗ
        r"\fill[white] (-1.1,0.12) rectangle (1.1,-0.12);"             # bông
        r"\draw[gray,line width=0.4pt] (-1.1,0.0) -- (1.1,0.0);"
        r"\end{scope}"
        f"\\draw[thuytinh,line width=1.4pt] {funnel};"
        # giọt chảy xuống
        r"\fill[nuocmau!25] (0,-0.75) circle (0.05);"
        r"\fill[nuocmau!18] (0,-1.05) circle (0.045);"
        # cốc hứng (dd mất màu ~ gần trong)
        r"\begin{scope}"
        r"\clip (-0.8,-1.25) -- (-0.8,-1.85) arc (180:360:0.8) -- (0.8,-1.25) -- cycle;"
        r"\fill[nuocmau!10] (-0.9,-1.95) rectangle (0.9,-1.55);"
        r"\end{scope}"
        r"\draw[thuytinh,line width=1.3pt] (-0.8,-1.25) -- (-0.8,-1.85) arc (180:360:0.8) -- (0.8,-1.25);"
    )
    body += _callout(1.3, 1.75, 1)    # nước màu
    body += _callout(1.3, 0.83, 2)    # bông trên
    body += _callout(1.3, 0.42, 3)    # than gỗ
    body += _callout(1.3, 0.0, 4)     # bông dưới
    body += _callout(1.25, -1.7, 5)   # cốc dd mất màu
    return _HC.render_tikz_doc(_doc(body), out, tra_bytes)
cot_loc_than.CHU_GIAI = CHU_GIAI_COT_THAN
