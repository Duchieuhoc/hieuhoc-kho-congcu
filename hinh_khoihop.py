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


# ─────────── helper hình học cho lăng trụ (module-level, thuần hàm) ───────────
def _in_poly(pt, poly):
    """Điểm pt CÓ nằm TRONG đa giác poly [(x,y)...] (ray-casting). Dùng test che
    (hướng NGANG: đỉnh mặt sau bị mặt trước che ⇔ nằm trong mặt trước)."""
    x, y = pt; n = len(poly); inside = False; j = n - 1
    for i in range(n):
        xi, yi = poly[i]; xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and \
           (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi):
            inside = not inside
        j = i
    return inside


def _hull(pts):
    """Bao lồi (Andrew monotone chain) — GIỮ điểm cộng tuyến trên biên. Trả SET toạ
    độ làm tròn (test thuộc bao). Dùng che hướng ĐỨNG: đỉnh đáy dưới nằm TRONG bao
    (near∪far) ⇔ bị tường bên che ⇒ khuất."""
    P = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))
    if len(P) <= 2:
        return set((round(x, 4), round(y, 4)) for x, y in P)
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo = []
    for q in P:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) < 0:
            lo.pop()
        lo.append(q)
    up = []
    for q in reversed(P):
        while len(up) >= 2 and cross(up[-2], up[-1], q) < 0:
            up.pop()
        up.append(q)
    return set((round(x, 4), round(y, 4)) for x, y in (lo[:-1] + up[:-1]))


def _day_polygon(day):
    """SPEC ngữ nghĩa của ĐÁY → (điểm [(u,v)...] CCW, nhãn_cạnh [str|None...] khớp cạnh i→i+1).
    Máy tính toạ độ; AI Soạn CHỈ khai loại đáy + số đo (Đ5.9). Loại hỗ trợ:
      chu_nhat(a,b) · tam_giac(a,b,c) · thang_vuong(day_lon,day_nho,cao) ·
      thang_can(day_lon,day_nho,cao) · binh_hanh(canh_day,canh_ben,goc) ·
      ngu_giac_nha(rong,cao_than,cao_dinh) · da_giac(diem=[...],nhan_canh=[...]).
    Mỗi loại nhận 'nhan' dict để ghi số đo lên cạnh tương ứng (bỏ khoá = cạnh trống)."""
    if isinstance(day, (list, tuple)) and day and isinstance(day[0], (list, tuple)):
        pts = [(float(x), float(y)) for x, y in day]
        return pts, [None] * len(pts)
    d = dict(day); loai = d.get('loai'); nh = d.get('nhan', {}) or {}
    def g(k):
        v = nh.get(k); return _mathwrap(v) if v else None
    if loai == 'chu_nhat':
        a, b = float(d['a']), float(d['b'])
        return [(0,0),(a,0),(a,b),(0,b)], [g('a'), g('b'), g('a_tren'), g('b_trai')]
    if loai == 'tam_giac':
        a, b, c = float(d['a']), float(d['b']), float(d['c'])
        x = (a*a + c*c - b*b) / (2*a); y = math.sqrt(max(c*c - x*x, 1e-9))
        return [(0,0),(a,0),(x,y)], [g('a'), g('b'), g('c')]
    if loai == 'thang_vuong':
        dl, dn, h = float(d['day_lon']), float(d['day_nho']), float(d['cao'])
        return [(0,0),(dl,0),(dn,h),(0,h)], [g('day_lon'), g('canh_xien'), g('day_nho'), g('cao')]
    if loai == 'thang_can':
        dl, dn, h = float(d['day_lon']), float(d['day_nho']), float(d['cao'])
        off = (dl - dn) / 2.0
        return [(0,0),(dl,0),(dl-off,h),(off,h)], [g('day_lon'), g('canh_ben'), g('day_nho'), g('canh_ben')]
    if loai == 'binh_hanh':
        cd, cb = float(d['canh_day']), float(d['canh_ben']); go = math.radians(float(d.get('goc', 60)))
        dx, dy = cb*math.cos(go), cb*math.sin(go)
        return [(0,0),(cd,0),(cd+dx,dy),(dx,dy)], [g('canh_day'), g('canh_ben'), g('canh_day_tren'), g('canh_ben_trai')]
    if loai == 'ngu_giac_nha':
        r, ht, hd = float(d['rong']), float(d['cao_than']), float(d['cao_dinh'])
        return [(0,0),(r,0),(r,ht),(r/2,ht+hd),(0,ht)], [g('rong'), g('cao_than'), g('mai'), g('mai'), g('cao_than')]
    if loai == 'da_giac':
        pts = [(float(x), float(y)) for x, y in d['diem']]
        nl = d.get('nhan_canh') or [None] * len(pts)
        return pts, [(_mathwrap(x) if x else None) for x in nl]
    raise ValueError(f"[lang_tru_dung] đáy loại '{loai}' chưa hỗ trợ")


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

    def lang_tru_dung(self, day, cao, huong='ngang', sau='phai',
                      nhan_canh_ben=None, ten_dinh=None, chu_thich=None,
                      to_day=False, goc_o=(0.0, 0.0), ten='L'):
        """LĂNG TRỤ ĐỨNG đáy ĐA GIÁC bất kỳ — phối cảnh xiên, NÉT KHUẤT tự tính theo che.

        day     : dict SPEC đáy {'loai':.., <số đo>, 'nhan':{cạnh:nhãn}}. Loại + KHOÁ số đo:
                  · tam_giac     {a,b,c}                  nhan {a,b,c}
                  · thang_vuong  {day_lon,day_nho,cao}    nhan {day_lon,day_nho,cao,canh_xien}
                  · thang_can    {day_lon,day_nho,cao}    nhan {day_lon,day_nho,canh_ben}
                  · chu_nhat     {a,b}                    nhan {a,b}
                  · binh_hanh    {canh_day,canh_ben,goc}  nhan {canh_day,canh_ben}
                  · ngu_giac_nha {rong,cao_than,cao_dinh} nhan {rong,cao_than,mai}
                  · da_giac      {diem:[(x,y)..], nhan_canh:[..]}
                  VD: lang_tru_dung({'loai':'tam_giac','a':6,'b':10,'c':8,'nhan':{'a':'6 cm'}}, cao=12, huong='ngang')
        cao     : ĐỘ DÀI cạnh bên = chiều cao lăng trụ đứng (>0).
        huong   : 'ngang' — hai mặt đáy là mặt TRƯỚC/SAU, trục lùi sâu (lăng kính/lều/máng/khay/bể);
                  'dung'  — hai mặt đáy NẰM NGANG (trên/dưới), cạnh bên THẲNG ĐỨNG (H10.19/10.21).
        sau     : 'phai'|'trai' — (chỉ 'ngang') chiều lùi sâu lên phải hay lên trái.
        nhan_canh_ben : nhãn ghi 1 cạnh bên thấy rõ (vd '20 cm').
        ten_dinh: list tên đỉnh ĐÁY GỐC (vd ['A','B','C']) → đáy còn lại tự thêm dấu phẩy (A',B',C');
                  HOẶC (đáy_dưới, đáy_trên) = 2 bộ tên KHÁC CHỮ (vd (['M','N','P','Q'],['E','F','G','H']) → MNPQ.EFGH).
                  None → đỉnh ẩn (không chấm, không nhãn) như hình minh hoạ số đo.
        chu_thich: list (part, chữ) chú thích có nét dẫn — part∈{dinh,canh_ben,canh_day,mat_day,mat_ben}
                  (H10.19 Đỉnh/Cạnh bên/Mặt đáy/Cạnh đáy).
        to_day  : tô nhạt mặt đáy thấy rõ (near).
        goc_o,ten: dời khối + tiền tố tên đỉnh ẩn (đặt >1 khối/1 hình).

        Máy tự tính toạ độ + nét khuất — AI Soạn không đụng toạ độ (Đ5.9).
        """
        pts, canh_nhan = _day_polygon(day)
        n = len(pts)
        if n < 3:
            raise ValueError("[lang_tru_dung] đáy cần ≥ 3 đỉnh")
        if not (cao > 0):
            raise ValueError("[lang_tru_dung] cao (chiều dài lăng trụ) phải > 0")
        self._nen_luoi = False
        ox, oy = goc_o
        p = ten

        # ── toạ độ near/far + phát hiện đỉnh khuất theo che THẬT ──
        if huong == 'ngang':
            dr = -1.0 if sau == 'trai' else 1.0
            Dx = dr * cao * _CO_SAU * math.cos(math.radians(_GOC_SAU))
            Dy = cao * _CO_SAU * math.sin(math.radians(_GOC_SAU))
            near = [(ox + u, oy + v) for (u, v) in pts]
            far  = [(ox + u + Dx, oy + v + Dy) for (u, v) in pts]
            hull = _hull(near + far)                              # đỉnh sau KHUẤT ⇔ nằm TRONG bao lồi
            an = [(round(far[i][0], 4), round(far[i][1], 4)) not in hull for i in range(n)]
        elif huong == 'dung':
            c = math.cos(math.radians(_GOC_SAU)); s = math.sin(math.radians(_GOC_SAU))
            floor = [(ox + u + _CO_SAU * v * c, oy + _CO_SAU * v * s) for (u, v) in pts]
            far  = floor                                          # đáy DƯỚI (khuất một phần)
            near = [(x, y + cao) for (x, y) in floor]             # đáy TRÊN (thấy rõ)
            hull = _hull(near + far)
            an = [(round(far[i][0], 4), round(far[i][1], 4)) not in hull for i in range(n)]
        else:
            raise ValueError("[lang_tru_dung] huong phải 'ngang' hoặc 'dung'")

        # ── tên đỉnh: đáy GỐC (không phẩy) = near(ngang) / far=đáy dưới(dung) ──
        if ten_dinh:
            # ten_dinh: list PHẲNG ['A','B','C'] → đáy kia tự thêm dấu phẩy (A'B'C');
            #   HOẶC (đáy_dưới, đáy_trên) = 2 bộ tên RÕ cho 2 đáy khác chữ (MNPQ.EFGH — bài 10.7).
            if len(ten_dinh) == 2 and all(isinstance(x, (list, tuple)) for x in ten_dinh):
                duoi, tren = list(ten_dinh[0]), list(ten_dinh[1])
            else:
                duoi = list(ten_dinh); tren = [b + "'" for b in duoi]
            if len(duoi) != n or len(tren) != n:
                raise ValueError(f"[lang_tru_dung] mỗi bộ ten_dinh cần đủ {n} tên")
            # 'dung': đáy DƯỚI = far, đáy TRÊN = near · 'ngang': đáy TRƯỚC(gốc)=near, SAU=far
            near_names, far_names = (tren, duoi) if huong == 'dung' else (duoi, tren)
        else:
            near_names = [f'{p}n{i}' for i in range(n)]
            far_names  = [f'{p}f{i}' for i in range(n)]

        allp = near + far
        cx = sum(x for x, _ in allp) / len(allp)
        cy = sum(y for _, y in allp) / len(allp)
        def _pos(pt):
            dx, dy = pt[0] - cx, pt[1] - cy
            if abs(dx) >= abs(dy):
                return 'right' if dx >= 0 else 'left'
            return 'above' if dy >= 0 else 'below'
        show = bool(ten_dinh)
        for i in range(n):
            self._diem(near_names[i], near[i][0], near[i][1],
                       nhan=(_pos(near[i]) if show else None), moc=show)
            self._diem(far_names[i], far[i][0], far[i][1],
                       nhan=(_pos(far[i]) if show else None), moc=show)

        # ── PHANH: cạnh bên BẰNG NHAU (bất biến lăng trụ đứng) ──
        self.rb.append({'loai': 'canh_bang',
                        'cac_doan': [(near_names[i], far_names[i]) for i in range(n)]})

        if to_day:
            self.to_mien(*near_names, mau='cyan!16')

        # ── vẽ: near (liền) · far (liền/đứt theo che) · cạnh bên (liền/đứt) ──
        for i in range(n):
            self.doan(near_names[i], near_names[(i + 1) % n])
        for i in range(n):
            j = (i + 1) % n
            self.doan(far_names[i], far_names[j], net=('dut' if (an[i] or an[j]) else 'lien'))
        for i in range(n):
            self.doan(near_names[i], far_names[i], net=('dut' if an[i] else 'lien'))

        # ── nhãn cạnh đáy (đẩy ra ngoài tâm) ──
        for i in range(n):
            if canh_nhan[i]:
                (x1, y1), (x2, y2) = near[i], near[(i + 1) % n]
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                vx, vy = mx - cx, my - cy; L = math.hypot(vx, vy) or 1.0
                self.ghi_chu(mx + vx / L * 0.36, my + vy / L * 0.36, canh_nhan[i])

        # ── nhãn cạnh bên (chiều cao) trên 1 cạnh bên thấy rõ ──
        if nhan_canh_ben:
            i0 = next((i for i in range(n) if not an[i]), 0)
            (x1, y1), (x2, y2) = near[i0], far[i0]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            vx, vy = mx - cx, my - cy; L = math.hypot(vx, vy) or 1.0
            self.ghi_chu(mx + vx / L * 0.40, my + vy / L * 0.40, _mathwrap(nhan_canh_ben))

        if chu_thich:
            self._callout_langtru(chu_thich, near, far, an)
        return self

    def _callout_langtru(self, chu_thich, near, far, an):
        """Chú thích nét dẫn ĐẸP (H10.19): mỗi part → 1 điểm đích rõ ràng phía PHẢI hình;
        nhãn xếp cột phải Ở NGANG TẦM điểm đích (ép khoảng cách tối thiểu để không đè) →
        nét dẫn NÉT ĐỨT gần song song, KHÔNG cắt nhau."""
        n = len(near)
        def mid(a, b): return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        i_vis = next((i for i in range(n) if not an[i]), 0)
        # đỉnh: góc trên-phải (near) rõ nhất
        i_dinh = max(range(n), key=lambda i: near[i][0] + near[i][1])
        # cạnh bên THẤY RÕ nằm phải nhất
        i_cb = max((i for i in range(n) if not an[i]),
                   key=lambda i: mid(near[i], far[i])[0], default=i_vis)
        # cạnh đáy: cạnh đáy dưới (far) THẤY RÕ nằm phải nhất
        vfe = [i for i in range(n) if not an[i] and not an[(i + 1) % n]]
        i_cd = max(vfe, key=lambda i: mid(far[i], far[(i + 1) % n])[0], default=i_vis)
        tg = {
            'dinh':     near[i_dinh],
            'canh_ben': mid(near[i_cb], far[i_cb]),
            'mat_ben':  mid(mid(near[i_cb], far[i_cb]),
                            mid(near[(i_cb + 1) % n], far[(i_cb + 1) % n])),
            'mat_day':  (sum(x for x, _ in near) / n, sum(y for _, y in near) / n),
            'canh_day': mid(far[i_cd], far[(i_cd + 1) % n]),
        }
        items = [(p, t) for (p, t) in
                 (chu_thich.items() if isinstance(chu_thich, dict) else chu_thich) if p in tg]
        if not items:
            return self
        items.sort(key=lambda it: -tg[it[0]][1])       # theo y đích giảm dần (trên → dưới)
        xmax = max(x for x, _ in (near + far))
        tx = xmax + 1.9
        gap = 0.62
        ys = []                                        # nhãn ở NGANG TẦM đích, ép min-gap
        for p, _ in items:
            y = tg[p][1]
            if ys and y > ys[-1] - gap:
                y = ys[-1] - gap
            ys.append(y)
        for k, (part, txt) in enumerate(items):
            gx, gy = tg[part]
            ty = ys[k]
            a1, a2 = f'_ctA{k}', f'_ctB{k}'
            self._diem(a1, tx - 0.15, ty, nhan=None, moc=False)   # đầu nét dẫn sát mép trái nhãn
            self._diem(a2, gx, gy, nhan=None, moc=False)
            self.doan(a1, a2, mau='gray', net='dut')
            self.ghi_chu(tx + 0.05, ty, txt)
        return self


    def _ve_net(self, faces, to_mat=None):
        """Vẽ 1 KHAI TRIỂN (net): mỗi mặt = list tên đỉnh (đa giác). Cạnh CHUNG 2 mặt = NẾP GẤP
        (nét đứt); cạnh chỉ thuộc 1 mặt = BAO NGOÀI (nét liền). Tự phân loại theo trùng lặp toạ độ.
        to_mat: dict {chỉ_số_mặt: màu} → tô nhạt mặt đó (tuỳ chọn)."""
        from collections import defaultdict
        dem = defaultdict(list)
        for poly in faces:
            k = len(poly)
            for i in range(k):
                A, B = poly[i], poly[(i + 1) % k]
                (xa, ya), (xb, yb) = self.V[A], self.V[B]
                key = tuple(sorted([(round(xa, 3), round(ya, 3)), (round(xb, 3), round(yb, 3))]))
                dem[key].append((A, B))
        if to_mat:
            for idx, mau in to_mat.items():
                self.to_mien(*faces[idx], mau=mau)
        for segs in dem.values():
            A, B = segs[0]
            self.doan(A, B, net=('dut' if len(segs) >= 2 else 'lien'))
        return self

    def khai_trien_hop(self, dai, rong, cao, nhan=None, so_mat=False,
                       goc_o=(0.0, 0.0), ten='KT'):
        """KHAI TRIỂN (net) HÌNH HỘP CHỮ NHẬT dạng CHỮ THẬP (H10.4 · H10.6):
        4 mặt bên thành DẢI ngang (rộng dai·rong·dai·rong, cao=cao) + mặt TRÊN & DƯỚI gắn vào
        mặt thứ 2. Nếp gấp (cạnh trong) NÉT ĐỨT, bao ngoài nét liền — máy tự phân loại.

        dai,rong,cao : 3 kích thước hộp (độ dài VẼ) > 0.
        nhan   : dict {'dai':.., 'rong':.., 'cao':..} ghi số đo (string/biểu thức, tự bọc $…$).
        so_mat : True → đánh số (1)…(6) vào giữa 6 mặt (như H10.6 HD4).
        goc_o,ten : dời net + tiền tố tên đỉnh (ẩn).
        Máy tự tính toạ độ (Đ5.9).
        """
        if not (dai > 0 and rong > 0 and cao > 0):
            raise ValueError("[khai_trien_hop] dai, rong, cao đều phải > 0")
        self._nen_luoi = False
        ox, oy = goc_o
        p = ten
        xs = [0, dai, dai + rong, 2 * dai + rong, 2 * dai + 2 * rong]

        def R(nm, x0, y0, x1, y1):
            b = f'{p}{nm}'
            self._diem(b + 'a', ox + x0, oy + y0, nhan=None, moc=False)
            self._diem(b + 'b', ox + x1, oy + y0, nhan=None, moc=False)
            self._diem(b + 'c', ox + x1, oy + y1, nhan=None, moc=False)
            self._diem(b + 'd', ox + x0, oy + y1, nhan=None, moc=False)
            return [b + 'a', b + 'b', b + 'c', b + 'd']
        # dải 4 mặt bên (1)(2)(3)(4) + mặt trên (5) & dưới (6) gắn mặt (2)
        F = [R('f1', xs[0], 0, xs[1], cao),
             R('f2', xs[1], 0, xs[2], cao),
             R('f3', xs[2], 0, xs[3], cao),
             R('f4', xs[3], 0, xs[4], cao),
             R('f5', xs[1], cao, xs[2], cao + dai),
             R('f6', xs[1], -dai, xs[2], 0)]
        self._ve_net(F)

        # nhãn số đo (a=dai dưới mặt1, b=rong dưới mặt2, c=cao trái mặt1)
        nhan = nhan or {}
        if nhan.get('dai'):
            self.ghi_chu(ox + dai / 2, oy - 0.32, _mathwrap(nhan['dai']))
        if nhan.get('rong'):
            self.ghi_chu(ox + dai + rong / 2, oy - 0.32, _mathwrap(nhan['rong']))
        if nhan.get('cao'):
            self.ghi_chu(ox - 0.34, oy + cao / 2, _mathwrap(nhan['cao']))
        # đánh số mặt (1)…(6)
        if so_mat:
            tam = [(dai / 2, cao / 2), (dai + rong / 2, cao / 2),
                   (dai + rong + dai / 2, cao / 2), (2 * dai + rong + rong / 2, cao / 2),
                   (dai + rong / 2, cao + dai / 2), (dai + rong / 2, -dai / 2)]
            for i, (cx, cy) in enumerate(tam, 1):
                self.ghi_chu(ox + cx, oy + cy, f'({i})')
        return self

    def khai_trien_lang_tru(self, day, cao, nhan_cao=None, so_mat=False,
                            goc_o=(0.0, 0.0), ten='KL'):
        """KHAI TRIỂN (net) LĂNG TRỤ ĐỨNG đáy đa giác (H10.22 · H10.24 · H10.32):
        DẢI n mặt bên hình chữ nhật (rộng = độ dài từng CẠNH ĐÁY, cao = chiều cao lăng trụ)
        + 2 ĐA GIÁC ĐÁY gắn TRÊN & DƯỚI mặt bên đầu. Nếp gấp NÉT ĐỨT, bao ngoài liền.

        day  : dict SPEC đáy — KHOÁ số đo GIỐNG lang_tru_dung (tam_giac{a,b,c} · thang_vuong ·
               thang_can · chu_nhat{a,b} · binh_hanh · ngu_giac_nha · da_giac). Đáy MANG 'nhan'
               → ghi số đo cạnh (trên các mặt bên tương ứng).
        cao  : chiều cao lăng trụ (rộng của dải = độ dài cạnh đáy; cao dải = cao). > 0.
        nhan_cao : nhãn ghi chiều cao (vd '12 cm') trên 1 mặt bên.
        so_mat   : True → đánh số (1)…(n) các mặt bên (như H10.24).
        goc_o,ten: dời net + tiền tố tên đỉnh (ẩn).
        Máy tự tính toạ độ + phân loại nếp gấp (Đ5.9).
        """
        pts, canh_nhan = _day_polygon(day)
        n = len(pts)
        if n < 3:
            raise ValueError("[khai_trien_lang_tru] đáy cần ≥ 3 đỉnh")
        if not (cao > 0):
            raise ValueError("[khai_trien_lang_tru] cao > 0")
        self._nen_luoi = False
        ox, oy = goc_o
        p = ten
        # độ dài từng cạnh đáy (rộng mỗi mặt bên trong dải)
        canh = [math.hypot(pts[(i + 1) % n][0] - pts[i][0], pts[(i + 1) % n][1] - pts[i][1])
                for i in range(n)]
        xcum = [0.0]
        for c in canh:
            xcum.append(xcum[-1] + c)

        def R(nm, x0, y0, x1, y1):
            b = f'{p}{nm}'
            self._diem(b + 'a', ox + x0, oy + y0, nhan=None, moc=False)
            self._diem(b + 'b', ox + x1, oy + y0, nhan=None, moc=False)
            self._diem(b + 'c', ox + x1, oy + y1, nhan=None, moc=False)
            self._diem(b + 'd', ox + x0, oy + y1, nhan=None, moc=False)
            return [b + 'a', b + 'b', b + 'c', b + 'd']
        faces = [R(f'r{i}', xcum[i], 0, xcum[i + 1], cao) for i in range(n)]
        # 2 đáy: gắn trên & dưới mặt bên ĐẦU (r0), chia sẻ cạnh [0, canh0]
        # đáy trên = pts dời lên (y += cao); đáy dưới = pts lật (y = -y)
        def DAY(nm, fn):
            names = []
            for i, (px, py) in enumerate(pts):
                a = f'{p}{nm}{i}'
                x, y = fn(px, py)
                self._diem(a, ox + x, oy + y, nhan=None, moc=False)
                names.append(a)
            return names
        day_tren = DAY('dt', lambda px, py: (px, cao + py))
        day_duoi = DAY('dd', lambda px, py: (px, -py))
        self._ve_net(faces + [day_tren, day_duoi])

        # nhãn số đo cạnh đáy (trên đỉnh mỗi mặt bên tương ứng) + chiều cao
        for i in range(n):
            if canh_nhan[i]:
                self.ghi_chu(ox + (xcum[i] + xcum[i + 1]) / 2, oy + cao + 0.30, canh_nhan[i])
        if nhan_cao:
            self.ghi_chu(ox + xcum[-1] + 0.36, oy + cao / 2, _mathwrap(nhan_cao))
        if so_mat:
            for i in range(n):
                self.ghi_chu(ox + (xcum[i] + xcum[i + 1]) / 2, oy + cao / 2, f'({i + 1})')
        return self

    def khoi_hop_chia_o(self, dai, rong, cao, o_roi=True, nhan_donvi='1 dm',
                        goc_o=(0.0, 0.0), ten='CO'):
        """KHỐI HỘP CHỮ NHẬT chia dai×rong×cao Ô ĐƠN VỊ (H10.8 — giới thiệu thể tích: hộp 5×2×4).
        dai = số ô ngang (mặt trước), rong = số ô sâu, cao = số ô đứng (đều nguyên ≥ 1).
        Kẻ lưới ô trên 3 mặt THẤY (trước·trên·phải); 3 cạnh khuất tại đỉnh sau-dưới nét đứt.
        o_roi=True → kèm 1 lập phương ĐƠN VỊ rời + nhãn 'nhan_donvi' (vd '1 dm').
        Máy tự tính toạ độ (Đ5.9). Góc phối cảnh ≡ khoi_hop_chu_nhat."""
        dai, rong, cao = int(dai), int(rong), int(cao)
        if not (dai >= 1 and rong >= 1 and cao >= 1):
            raise ValueError("[khoi_hop_chia_o] dai, rong, cao đều phải ≥ 1 (số ô nguyên)")
        self._nen_luoi = False
        ang = math.radians(_GOC_SAU); cs = _CO_SAU * math.cos(ang); sn = _CO_SAU * math.sin(ang)
        ox, oy = goc_o; p = ten
        A, B, C = dai, cao, rong        # i-ngang=dai · j-đứng=cao · k-sâu=rong
        def pt(i, j, k):
            nm = f'{p}_{i}_{j}_{k}'
            if nm not in self.V:
                self._diem(nm, ox + i + cs * k, oy + j + sn * k, nhan=None, moc=False)
            return nm
        def seg(a, b, net='lien'):
            self.doan(pt(*a), pt(*b), net=net)
        # 12 cạnh ngoài: 9 liền + 3 khuất tại (0,0,C)
        for a, b in [((0,0,0),(A,0,0)),((A,0,0),(A,B,0)),((A,B,0),(0,B,0)),((0,B,0),(0,0,0)),
                     ((A,0,0),(A,0,C)),((A,B,0),(A,B,C)),((0,B,0),(0,B,C)),
                     ((A,0,C),(A,B,C)),((A,B,C),(0,B,C))]:
            seg(a, b)
        for a, b in [((0,0,0),(0,0,C)),((0,0,C),(A,0,C)),((0,0,C),(0,B,C))]:
            seg(a, b, 'dut')
        # lưới ô trên 3 mặt thấy (liền)
        for t in range(1, A):
            seg((t,0,0),(t,B,0)); seg((t,B,0),(t,B,C))          # trước dọc · trên dọc
        for t in range(1, B):
            seg((0,t,0),(A,t,0)); seg((A,t,0),(A,t,C))          # trước ngang · phải dọc
        for t in range(1, C):
            seg((0,B,t),(A,B,t)); seg((A,0,t),(A,B,t))          # trên sâu · phải sâu
        # ô đơn vị rời + nhãn
        if o_roi:
            self.khoi_hop_chu_nhat(1, 1, 1, goc_o=(ox + A + 1.3, oy), ten=p + 'u')
            if nhan_donvi:
                self.ghi_chu(ox + A + 1.3 + 0.5 + 0.5 * cs, oy - 0.42, _mathwrap(nhan_donvi))
        return self

    def khoi_lap_phuong_chia_o(self, n, o_roi=True, nhan_donvi='1 dm',
                               goc_o=(0.0, 0.0), ten='CO'):
        """KHỐI LẬP PHƯƠNG chia n×n×n Ô ĐƠN VỊ (trường hợp riêng của khoi_hop_chia_o, dai=rong=cao=n)."""
        return self.khoi_hop_chia_o(n, n, n, o_roi=o_roi, nhan_donvi=nhan_donvi,
                                    goc_o=goc_o, ten=ten)

    def khoi_ghep_lapphuong(self, danh_sach_o, goc_o=(0.0, 0.0), ten='GL'):
        """KHỐI GHÉP từ các LẬP PHƯƠNG ĐƠN VỊ đặt theo Ô NGUYÊN (x,y,z) — gốc (0,0,0)
        (H10.11 bài 10.1 đếm khối · H10.18 khay đá). Che khuất đúng (khối gần che khối xa,
        painter xa→gần tô mặt trắng); vẽ CẠNH của MẶT LỘ để đếm được từng khối.
        danh_sach_o = [(x,y,z), ...] (x phải, y lên, z lùi sâu). Máy tự tính toạ độ (Đ5.9)."""
        if not danh_sach_o:
            raise ValueError("[khoi_ghep_lapphuong] danh_sach_o rỗng")
        self._nen_luoi = False
        ang = math.radians(_GOC_SAU); cs = _CO_SAU * math.cos(ang); sn = _CO_SAU * math.sin(ang)
        ox, oy = goc_o; p = ten
        cells = set((int(a), int(b), int(c)) for a, b, c in danh_sach_o)
        cache = {}
        def pt(i, j, k):
            key = (i, j, k)
            if key not in cache:
                nm = f'{p}_{i}_{j}_{k}'
                self._diem(nm, ox + i + cs * k, oy + j + sn * k, nhan=None, moc=False)
                cache[key] = nm
            return cache[key]
        def mat(x, y, z, loai):
            if loai == 'truoc':  return [(x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z)]
            if loai == 'tren':   return [(x,y+1,z),(x+1,y+1,z),(x+1,y+1,z+1),(x,y+1,z+1)]
            return [(x+1,y,z),(x+1,y+1,z),(x+1,y+1,z+1),(x+1,y,z+1)]   # phai
        # painter: XA trước (z lớn·y lớn·x lớn) → GẦN sau (tô trắng đè)
        for (x, y, z) in sorted(cells, key=lambda c: (c[2], c[1], c[0]), reverse=True):
            for loai in ('truoc', 'tren', 'phai'):
                self.to_mien(*[pt(*v) for v in mat(x, y, z, loai)], mau='white')
        # cạnh MẶT LỘ (không có khối kề phía đó)
        for (x, y, z) in cells:
            for loai, kề in (('truoc', (x,y,z-1)), ('tren', (x,y+1,z)), ('phai', (x+1,y,z))):
                if kề not in cells:
                    f = mat(x, y, z, loai)
                    for i in range(4):
                        self.doan(pt(*f[i]), pt(*f[(i+1) % 4]))
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
