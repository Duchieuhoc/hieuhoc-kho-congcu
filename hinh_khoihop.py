#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_khoihop.py — MẠCH KHỐI HỘP (phối cảnh xiên/cavalier) — dùng chung
#   Đại số 8 (thể tích/diện tích qua đa thức) + Hình học trực quan 5→9.
#   class HinhKhoiHop(HinhCoBan): thêm primitive `khoi_hop_chu_nhat`.
#   COMPOSE THUẦN base (điểm ẩn + doan liền/đứt + to_mien + ghi_chu) —
#   KHÔNG mổ lõi, KHÔNG thêm op renderer mới (khối hộp = 8 đỉnh + 12 cạnh:
#   9 cạnh nhìn thấy nét liền + 3 cạnh khuất nét đứt, đúng chuẩn SGK).
#   [28u] Ông Bụt 2026-09-06, Pha A DS8_CH01 (Đa thức): kho 28t KHÔNG có
#         bất kỳ hàm khối hộp/3D nào (grep hinh_*.py) → khe hở khi soạn
#         Bài 5 (2 khối hộp) + Ôn tập 1.46 (hộp gấp không nắp).
#   Triết lý giữ base: khai GIÁ TRỊ ngữ nghĩa (dai/rong/cao là độ dài VẼ),
#   máy TỰ TÍNH toạ độ phối cảnh → không lộ toạ độ thô (Đ5.9), qua cổng AST.
# CS2627.
# ═══════════════════════════════════════════════════════════════════
import math
from hinh_coban import HinhCoBan

# Hằng phối cảnh xiên (cavalier) — chuẩn SGK: chiều sâu nghiêng ~40°, co ~0,5.
_GOC_SAU = 40.0          # độ nghiêng cạnh chiều sâu (độ)
_CO_SAU  = 0.5           # hệ số co chiều sâu (foreshortening)


def _mathwrap(s):
    """Nhãn kích thước: bọc $...$ để in nghiêng toán (2x, 3y, S = 2xy). Đã có $ → giữ nguyên."""
    if s is None:
        return None
    s = str(s)
    return s if '$' in s else f'${s}$'


class HinhKhoiHop(HinhCoBan):
    """Mạch khối hộp chữ nhật. Kế thừa toàn bộ base HinhCoBan."""

    def khoi_hop_chu_nhat(self, dai, rong, cao, nhan=None,
                          to_day=False, nhan_day=None, an_nap=False,
                          goc_o=(0.0, 0.0), ten='K'):
        """KHỐI HỘP CHỮ NHẬT phối cảnh xiên (cạnh khuất nét đứt) — chuẩn SGK.

        dai, rong, cao : ba KÍCH THƯỚC (độ dài VẼ, đơn vị ô) — rộng-ngang mặt trước,
                         chiều sâu (lùi sau), chiều cao. Đều phải > 0.
        nhan           : dict {'dai':.., 'rong':.., 'cao':..} — nhãn 3 cạnh kích thước;
                         nhận STRING hoặc biểu thức ('2x','3y','x'…) — tự bọc $…$ in nghiêng.
                         Bỏ khoá nào → cạnh đó không ghi (vd cạnh 'cần tìm' để trống).
        to_day         : True → tô nhạt MẶT ĐÁY (dưới) — dùng khi đề cho diện tích đáy.
        nhan_day       : nhãn ghi giữa mặt đáy (vd 'S = 2xy'); chỉ ghi khi to_day hoặc khai rõ.
        an_nap         : True → hộp KHÔNG nắp (hộp gấp từ bìa) — vành trên là miệng hở
                         (khung nét vẫn 12 cạnh như SGK Hình 1.3; đáy/miệng đọc theo ngữ cảnh).
        goc_o          : (dx,dy) DỜI cả khối — đặt NHIỀU khối cạnh nhau trong 1 hình.
        ten            : tiền tố tên đỉnh (ẩn) — đổi khi vẽ >1 khối để tránh trùng tên.

        Máy tự tính 8 đỉnh từ 3 kích thước — AI Soạn không đụng toạ độ (Đ5.9).
        """
        if not (dai > 0 and rong > 0 and cao > 0):
            raise ValueError("[khoi_hop_chu_nhat] dai, rong, cao đều phải > 0")
        self._nen_luoi = False        # khối hộp phối cảnh: nền sạch, không ô lưới
        ox, oy = goc_o
        p = ten

        # ── vector chiều sâu (phối cảnh xiên) ──
        dpx = rong * _CO_SAU * math.cos(math.radians(_GOC_SAU))
        dpy = rong * _CO_SAU * math.sin(math.radians(_GOC_SAU))

        # ── 8 đỉnh (ẩn: moc=False, nhan=None → không chấm, không nhãn) ──
        # mặt TRƯỚC: A dưới-trái, B dưới-phải, C trên-phải, D trên-trái
        A, B, Cc, D = f'{p}A', f'{p}B', f'{p}C', f'{p}D'
        # mặt SAU (lùi theo vector sâu): A2,B2,C2,D2
        A2, B2, C2, D2 = f'{p}A2', f'{p}B2', f'{p}C2', f'{p}D2'
        self._diem(A,  ox,            oy,            nhan=None, moc=False)
        self._diem(B,  ox + dai,      oy,            nhan=None, moc=False)
        self._diem(Cc, ox + dai,      oy + cao,      nhan=None, moc=False)
        self._diem(D,  ox,            oy + cao,      nhan=None, moc=False)
        self._diem(A2, ox + dpx,      oy + dpy,      nhan=None, moc=False)
        self._diem(B2, ox + dai + dpx, oy + dpy,     nhan=None, moc=False)
        self._diem(C2, ox + dai + dpx, oy + cao + dpy, nhan=None, moc=False)
        self._diem(D2, ox + dpx,      oy + cao + dpy, nhan=None, moc=False)

        # ── PHANH: khối hộp = LĂNG TRỤ đứng → 4 cạnh chiều sâu BẰNG NHAU
        #    + mặt trước là hình chữ nhật (góc tại A vuông). Máy đối chiếu, sai → DỪNG.
        self.rb.append({'loai': 'canh_bang',
                        'cac_doan': [(A, A2), (B, B2), (Cc, C2), (D, D2)]})
        self.rb.append({'loai': 'goc', 'ten': [D, A, B], 'do': 90})

        # ── TÔ ĐÁY (nằm dưới mọi nét) ──
        if to_day:
            self.to_mien(A, B, B2, A2, mau='cyan!16')

        # ── 12 CẠNH: 9 nhìn thấy (liền) + 3 khuất tại đỉnh sau-dưới-trái A2 (đứt) ──
        # mặt trước (liền)
        for u, v in [(A, B), (B, Cc), (Cc, D), (D, A)]:
            self.doan(u, v)
        # cạnh nối + mặt sau NHÌN THẤY (liền)
        for u, v in [(B, B2), (Cc, C2), (D, D2), (B2, C2), (C2, D2)]:
            self.doan(u, v)
        # 3 cạnh KHUẤT tại A2 (nét đứt)
        for u, v in [(A, A2), (A2, B2), (A2, D2)]:
            self.doan(u, v, net='dut')

        # ── NHÃN kích thước ──
        nhan = nhan or {}
        def _giua(P1, P2):
            (x1, y1), (x2, y2) = self.V[P1], self.V[P2]
            return (x1 + x2) / 2, (y1 + y2) / 2
        if nhan.get('dai'):                       # cạnh dưới-trước A-B → nhãn DƯỚI
            mx, my = _giua(A, B); self.ghi_chu(mx, my - 0.34, _mathwrap(nhan['dai']))
        if nhan.get('cao'):                       # cạnh đứng-trước-trái D-A → nhãn TRÁI
            mx, my = _giua(D, A); self.ghi_chu(mx - 0.34, my, _mathwrap(nhan['cao']))
        if nhan.get('rong'):                      # cạnh sâu-phải B-B2 → nhãn PHẢI-DƯỚI
            mx, my = _giua(B, B2); self.ghi_chu(mx + 0.30, my - 0.20, _mathwrap(nhan['rong']))

        # ── nhãn mặt đáy (diện tích đáy) ──
        if nhan_day:
            cx = ox + dai / 2 + dpx / 2
            cy = oy + dpy / 2
            self.ghi_chu(cx, cy, _mathwrap(nhan_day))

        return self

    def net_hop_cat_goc(self, dai, rong, canh_goc, nhan=None,
                        to_goc=True, goc_o=(0.0, 0.0), ten='N'):
        """NET (khai triển 2D) miếng bìa chữ nhật CẮT 4 GÓC hình vuông → gấp thành hộp.
        Chuẩn SGK: bao ngoài chữ nhật ĐẦY ĐỦ (để ghi đủ 2 cạnh dài/rộng) + 4 ô vuông
        góc (cạnh canh_goc) + 4 NẾP GẤP nét đứt (chữ nhật trong = mặt đáy hộp).

        dai, rong  : độ dài VẼ 2 cạnh miếng bìa (dai ngang, rong đứng). Cần > 2·canh_goc.
        canh_goc   : cạnh ô vuông cắt ở góc (độ dài VẼ).
        nhan       : dict {'dai':.., 'rong':.., 'goc':..} — nhãn 2 cạnh bìa + ô góc.
                     'goc' ghi vào CẢ 4 ô vuông góc. Nhận string/biểu thức ('y','z','x').
        to_goc     : True → tô nhạt 4 ô vuông góc (phần bị cắt bỏ).
        goc_o, ten : DỜI net + tiền tố tên đỉnh (ẩn) — đặt cạnh khối hộp trong 1 hình.

        Máy tự tính toạ độ — AI Soạn không đụng toạ độ (Đ5.9).
        """
        a, W, Hh = canh_goc, dai, rong
        if not (a > 0 and W > 2 * a and Hh > 2 * a):
            raise ValueError("[net_hop_cat_goc] cần canh_goc>0 và dai,rong > 2·canh_goc")
        self._nen_luoi = False
        ox, oy = goc_o
        p = ten

        def P(nm, x, y):
            self._diem(f'{p}{nm}', ox + x, oy + y, nhan=None, moc=False)
            return f'{p}{nm}'
        # 4 góc chữ nhật + 8 điểm mép (nơi vết cắt gặp cạnh) + 4 góc trong (nếp gấp)
        NA, NB, NC, ND = P('A', 0, 0), P('B', W, 0), P('C', W, Hh), P('D', 0, Hh)
        B1, B2 = P('b1', a, 0), P('b2', W - a, 0)          # mép dưới
        R1, R2 = P('r1', W, a), P('r2', W, Hh - a)         # mép phải
        T1, T2 = P('t1', W - a, Hh), P('t2', a, Hh)        # mép trên
        L1, L2 = P('l1', 0, Hh - a), P('l2', 0, a)         # mép trái
        Ibl, Ibr = P('ibl', a, a), P('ibr', W - a, a)      # góc trong (nếp gấp)
        Itr, Itl = P('itr', W - a, Hh - a), P('itl', a, Hh - a)

        # ── tô 4 ô góc (phần cắt bỏ) — nằm dưới nét ──
        if to_goc:
            self.to_mien(NA, B1, Ibl, L2, mau='cyan!14')
            self.to_mien(B2, NB, R1, Ibr, mau='cyan!14')
            self.to_mien(Itr, R2, NC, T1, mau='cyan!14')
            self.to_mien(L1, Itl, T2, ND, mau='cyan!14')

        # ── bao ngoài chữ nhật đầy đủ (liền) ──
        for u, v in [(NA, NB), (NB, NC), (NC, ND), (ND, NA)]:
            self.doan(u, v)
        # ── vết cắt trong của 4 ô góc (liền) ──
        for u, v in [(B1, Ibl), (Ibl, L2), (B2, Ibr), (Ibr, R1),
                     (R2, Itr), (Itr, T1), (L1, Itl), (Itl, T2)]:
            self.doan(u, v)
        # ── 4 nếp gấp (chữ nhật trong = mặt đáy) — nét đứt ──
        for u, v in [(Ibl, Ibr), (Ibr, Itr), (Itr, Itl), (Itl, Ibl)]:
            self.doan(u, v, net='dut')

        # ── nhãn ──
        nhan = nhan or {}
        if nhan.get('dai'):
            self.ghi_chu(ox + W / 2, oy - 0.30, _mathwrap(nhan['dai']))
        if nhan.get('rong'):
            self.ghi_chu(ox - 0.30, oy + Hh / 2, _mathwrap(nhan['rong']))
        if nhan.get('goc'):
            g = _mathwrap(nhan['goc'])
            for cx, cy in [(a / 2, a / 2), (W - a / 2, a / 2),
                           (W - a / 2, Hh - a / 2), (a / 2, Hh - a / 2)]:
                self.ghi_chu(ox + cx, oy + cy, g)
        return self


# ═══ [29c] Ông Bụt 2026-09-16 · DS8 Chương 2 (Hằng đẳng thức) ═══
def khoiLapPhuongKhoetGoc(canhLon='2x+3', canhCon='x+1', chuThich=None,
                          out='khoi_khoet_goc', tra_bytes=False, S=4.0, a=1.6):
    """KHỐI LẬP PHƯƠNG cạnh 'canhLon' khoét 1 khối lập phương cạnh 'canhCon' ở góc
       TRÊN-TRƯỚC-PHẢI (phối cảnh xiên cavalier). Nét khuất = đường đứt. Nhãn BIẾN.
       (Port render_b07.py đã đạt — engine TikZ 2D không dựng phối cảnh 3D khoét-mặt-L)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    _ANG = math.radians(40.0); _CO = 0.5
    def PP(x, y, z): return (x + _CO*z*math.cos(_ANG), y + _CO*z*math.sin(_ANG))
    def canh(ax, p1, p2, dut=False, rong=1.6, mau="#1a1a1a"):
        A, B = PP(*p1), PP(*p2)
        ax.plot([A[0], B[0]], [A[1], B[1]],
                linestyle=(0, (4, 3)) if dut else "-",
                linewidth=rong, color=mau, solid_capstyle="round", zorder=5)
    def mat(ax, pts, mau):
        ax.add_patch(Polygon([PP(*p) for p in pts], closed=True,
                             facecolor=mau, edgecolor="none", zorder=1))
    def nh(ax, p, t, dx=0.0, dy=0.0, ha="center", va="center"):
        q = PP(*p)
        ax.text(q[0]+dx, q[1]+dy, f"${t}$", fontsize=17, ha=ha, va=va, zorder=8, color="#111")
    c = S - a
    fig, ax = plt.subplots(figsize=(4.2, 4.0)); ax.set_aspect("equal"); ax.axis("off")
    C_TRUOC="#ffffff"; C_TREN="#eef1f5"; C_PHAI="#e2e7ee"; C_TRONG="#c9d2df"; C_DAY="#d6dde7"
    mat(ax, [(0,0,0),(S,0,0),(S,c,0),(c,c,0),(c,S,0),(0,S,0)], C_TRUOC)
    mat(ax, [(0,S,0),(c,S,0),(c,S,a),(S,S,a),(S,S,S),(0,S,S)], C_TREN)
    mat(ax, [(S,0,0),(S,c,0),(S,c,a),(S,S,a),(S,S,S),(S,0,S)], C_PHAI)
    mat(ax, [(c,c,a),(S,c,a),(S,S,a),(c,S,a)], C_TRONG)
    mat(ax, [(c,c,0),(S,c,0),(S,c,a),(c,c,a)], C_DAY)
    mat(ax, [(c,c,0),(c,S,0),(c,S,a),(c,c,a)], C_TRONG)
    canh(ax, (0,0,S), (S,0,S), dut=True, rong=1.2)
    canh(ax, (0,0,S), (0,S,S), dut=True, rong=1.2)
    canh(ax, (0,0,0), (0,0,S), dut=True, rong=1.2)
    for seg in [((0,0,0),(S,0,0)),((S,0,0),(S,c,0)),((S,c,0),(c,c,0)),((c,c,0),(c,S,0)),
                ((c,S,0),(0,S,0)),((0,S,0),(0,0,0)),((S,0,0),(S,0,S)),((0,S,0),(0,S,S)),
                ((0,S,S),(S,S,S)),((S,0,S),(S,S,S)),((c,c,a),(S,c,a)),((c,c,a),(c,S,a)),
                ((c,S,a),(S,S,a)),((S,c,a),(S,S,a)),((c,c,0),(c,c,a)),((S,c,0),(S,c,a)),
                ((c,S,0),(c,S,a))]:
        canh(ax, *seg)
    nh(ax, (0, S/2.0, 0), canhLon, dx=-0.28, ha="right")
    nh(ax, ((c+S)/2.0, (c+S)/2.0, a), canhCon, dy=0.02)
    if chuThich:
        ax.text(0.5, -0.02, chuThich, transform=ax.transAxes, ha="center", va="top",
                fontsize=13, fontstyle="italic", color="#111")
    xs=[PP(x,y,z)[0] for x in (0,S) for y in (0,S) for z in (0,S)]
    ys=[PP(x,y,z)[1] for x in (0,S) for y in (0,S) for z in (0,S)]
    m=0.9
    ax.set_xlim(min(xs)-m-0.6, max(xs)+m+0.6); ax.set_ylim(min(ys)-m-(0.4 if chuThich else 0), max(ys)+m)
    png = f'/tmp/{out}.png'
    fig.savefig(png, dpi=200, bbox_inches="tight", pad_inches=0.06, transparent=True)
    plt.close(fig)
    return open(png, 'rb').read() if tra_bytes else png

# [29c] gắn làm staticmethod class entry → vào bản trích + gọi qua instance
HinhKhoiHop.khoiLapPhuongKhoetGoc = staticmethod(khoiLapPhuongKhoetGoc)
