#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh12_ch02.py — MẠCH HÌNH KHÔNG GIAN TỔNG HỢP (phối cảnh xiên) cho
#   Hình học 12, Chương II (Vectơ trong không gian).
#   class HinhHH12CH02(HinhKhoiHop): thêm 2 primitive KHỐI NỀN còn thiếu —
#     tu_dien (K1) · chop (K2) — nét khuất tự tính.
#   Hộp/lập phương (khoi_hop_chu_nhat) + lăng trụ (lang_tru_dung) kế thừa
#   nguyên từ hinh_khoihop. Trung điểm/điểm-trên-đoạn/giao/VECTƠ dùng base
#   (hinh_coban: trung_diem, diem_giua, giao, vecto, doan) — phép chiếu
#   xiên là AFFINE nên mọi op 2D chạy thẳng trên đỉnh đã chiếu.
#   Triết lý Đ5.9: AI khai NGHĨA (tên khối, đỉnh nào, điểm phụ gì) — máy
#   tự tính toạ độ phối cảnh; AI KHÔNG cấp toạ độ.
#   Căn cứ: DE_XUAT_CHUAN_PHOI_CANH_3D §2–§3 (duyệt 2026-10-12). CS2627.
# ═══════════════════════════════════════════════════════════════════
import math
from hinh_khoihop import HinhKhoiHop, _day_polygon, _hull
import hinh_netkhuat as _NK          # [33s] engine nét khuất tự tính

_GOC_SAU = 40.0
_CO_SAU  = 0.5


class HinhHH12CH02(HinhKhoiHop):
    """Mạch hình không gian tổng hợp lớp 12. Kế thừa khối hộp/lăng trụ + base."""

    # ══════════ [33s] ENGINE NÉT KHUẤT TỰ TÍNH (hidden-line) ══════════
    # Bật qua cờ net_khuat=True ở tu_dien/chop. Mỗi đỉnh khối lưu toạ độ 3D
    # (giữ NGUYÊN vị trí màn), engine tính đoạn nào bị MẶT khối che → đứt.
    # Mặc định TẮT ⇒ bài cũ 0 đổi. Đ5.9: nét khuất = hình học, máy tự tính.
    def _kh_bat(self):
        self._net_khuat = True
        if not hasattr(self, '_kh_V'):     self._kh_V = {}
        if not hasattr(self, '_kh_faces'): self._kh_faces = []

    def _kh_put(self, name, x, y, v):
        """Lưu toạ độ 3D của đỉnh từ vị trí màn (x,y) + độ sâu v (giữ y vị trí)."""
        self._kh_V[name] = _NK.recon3d(x, y, v)

    def _kh_aff(self, name, cha):
        """Điểm dẫn xuất (trung điểm/giao/trọng tâm): toạ độ 3D = tổ hợp affine
        cha = [(ten_cha, trong_so)...] (tổng trọng số = 1). Chiếu xiên affine nên
        tổ hợp trên màn ⟺ tổ hợp trên 3D."""
        if not getattr(self, '_net_khuat', False):
            return
        if not all(p in self._kh_V for p, _ in cha):
            return
        u = v = w = 0.0
        for p, wt in cha:
            pu, pv, pw = self._kh_V[p]
            u += wt * pu; v += wt * pv; w += wt * pw
        self._kh_V[name] = (u, v, w)

    def _kh_doan(self, A, B):
        """Trả list khúc [((xa,ya),(xb,yb),khuat)] của đoạn A-B theo che; None nếu
        không áp được (thiếu toạ độ 3D / chưa có mặt khối)."""
        if not getattr(self, '_net_khuat', False):
            return None
        if A not in self._kh_V or B not in self._kh_V or not self._kh_faces:
            return None
        P0, P1 = self._kh_V[A], self._kh_V[B]
        faces3 = []
        for f in self._kh_faces:
            pts = [self._kh_V[n] for n in f if n in self._kh_V]
            if len(pts) >= 3:
                faces3.append(pts)
        if not faces3:
            return None
        out = []
        for t0, t1, hid in _NK.che_khuat(P0, P1, faces3):
            def at(t):
                return _NK.proj((P0[0] + (P1[0] - P0[0]) * t,
                                 P0[1] + (P1[1] - P0[1]) * t,
                                 P0[2] + (P1[2] - P0[2]) * t))
            out.append((at(t0), at(t1), hid))
        return out

    # ── propagate toạ độ 3D qua các phép đặt điểm dẫn xuất (override base) ──
    def trung_diem(self, M, A, B, mau=None):
        super().trung_diem(M, A, B, mau=mau)
        self._kh_aff(M, [(A, 0.5), (B, 0.5)])
        return self

    def diem_giua(self, ten, A, B, ti_le=0.5, mau=None, nhan='above'):
        super().diem_giua(ten, A, B, ti_le=ti_le, mau=mau, nhan=nhan)
        self._kh_aff(ten, [(A, 1.0 - ti_le), (B, ti_le)])
        return self

    def giao(self, ten, dt1, dt2, mau=None):
        super().giao(ten, dt1, dt2, mau=mau)
        # nội suy độ sâu theo tham số chiếu dọc dt1 (P→Q), affine nên khớp 3D
        if getattr(self, '_net_khuat', False) and isinstance(dt1, (tuple, list)) \
           and len(dt1) == 2 and dt1[0] in self._kh_V and dt1[1] in self._kh_V \
           and ten in self.V:
            P, Q = dt1
            (px, py), (qx, qy) = self.V[P], self.V[Q]
            (gx, gy) = self.V[ten]
            dx, dy = qx - px, qy - py
            den = dx * dx + dy * dy
            if den > 1e-12:
                t = ((gx - px) * dx + (gy - py) * dy) / den
                self._kh_aff(ten, [(P, 1.0 - t), (Q, t)])
        return self

    def keo_dai(self, ten, A, B, dai=None, nhan='below right', ve_doan=True, mau=None):
        super().keo_dai(ten, A, B, dai=dai, nhan=nhan, ve_doan=ve_doan, mau=mau)
        if getattr(self, '_net_khuat', False) and A in self._kh_V and B in self._kh_V \
           and ten in self.V:
            (ax, ay), (bx, by) = self.V[A], self.V[B]
            (tx, ty) = self.V[ten]
            dx, dy = bx - ax, by - ay
            den = dx * dx + dy * dy
            if den > 1e-12:
                t = ((tx - ax) * dx + (ty - ay) * dy) / den
                self._kh_aff(ten, [(A, 1.0 - t), (B, t)])
        return self

    # ─────────────────────────────────────────────────────────────
    def tu_dien(self, nhan='ABCD', dinh_tren=None, canh=3.0,
                goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=False):
        """TỨ DIỆN phối cảnh chuẩn — 4 đỉnh, 6 cạnh (1 cạnh đáy sau KHUẤT nét đứt).

        nhan      : 4 ký tự tên đỉnh, ký tự ĐẦU = đỉnh trên (apex), 3 ký tự sau = đáy.
                    Vd 'ABCD' → A apex; đáy B,C,D. Chấp nhận tên nhiều ký tự qua list.
        dinh_tren : tên đỉnh làm apex (mặc định = phần tử đầu của nhan).
        canh      : cỡ vẽ (bề rộng đáy, đơn vị ô). >0.
        Bố cục chuẩn (kho quyết góc nhìn): đáy có 1 đỉnh TRƯỚC + 2 đỉnh SAU; cạnh
          nối 2 đỉnh sau = cạnh KHUẤT (nét đứt). apex nối cả 3 đỉnh đáy (nét liền).

        Máy tự tính toạ độ — AI không đụng toạ độ (Đ5.9).
        """
        names = list(nhan)
        if len(names) != 4:
            raise ValueError("[tu_dien] cần đúng 4 tên đỉnh (vd 'ABCD')")
        if dinh_tren is not None and dinh_tren in names:
            names.remove(dinh_tren); names.insert(0, dinh_tren)
        if not (canh > 0):
            raise ValueError("[tu_dien] canh phải > 0")
        self._nen_luoi = False
        ox, oy = goc_o
        s = canh / 3.0                       # hệ số tỉ lệ theo 'canh'
        A, B, C, D = names                   # A = apex; B,C,D = đáy
        # bố cục chuẩn: C TRƯỚC (dưới), B SAU-TRÁI, D SAU-PHẢI, A apex trên
        P = {
            C: (ox + 1.5 * s, oy + 0.0 * s),       # trước, dưới
            B: (ox + 0.0 * s, oy + 1.0 * s),       # sau, trái
            D: (ox + 3.0 * s, oy + 1.0 * s),       # sau, phải
            A: (ox + 1.5 * s, oy + 2.6 * s),       # apex trên
        }
        pos = {C: 'below', B: 'left', D: 'right', A: 'above'}
        for nm in (A, B, C, D):
            self._diem(nm, P[nm][0], P[nm][1],
                       nhan=(pos[nm] if hien_nhan else None), moc=hien_nhan)
        # [33s] bật engine nét khuất: lưu toạ độ 3D (giữ vị trí màn) + 4 mặt
        if net_khuat:
            self._kh_bat()
            VB = 2.0                                  # độ sâu 2 đỉnh đáy sau
            dep = {C: 0.0, B: VB, D: VB, A: VB * 2.0 / 3.0}   # C trước · B,D sau · A apex (sâu = trọng tâm đáy)
            for nm in (A, B, C, D):
                self._kh_put(nm, P[nm][0], P[nm][1], dep[nm])
            # 4 mặt: 3 mặt bên quanh apex A + mặt đáy BCD
            self._kh_faces = [[A, B, C], [A, C, D], [A, D, B], [B, C, D]]
        # 6 cạnh: đáy BC, CD liền · đáy sau BD khuất (nét đứt) · bên AB, AC, AD liền
        for u, v in [(B, C), (C, D), (A, B), (A, C), (A, D)]:
            self.doan(u, v)
        self.doan(B, D, net='dut')
        return self

    # ─────────────────────────────────────────────────────────────
    def trong_tam(self, ten, *dinh, nhan='right', moc=True, mau=None):
        """Đặt TRỌNG TÂM của các đỉnh đã có (trung bình toạ độ — chiếu affine nên
        trùng trọng tâm hình học). Vd trọng tâm mặt BCD: trong_tam('G','B','C','D').
        AI chỉ nêu các đỉnh; máy tính vị trí (Đ5.9)."""
        if len(dinh) < 2:
            raise ValueError("[trong_tam] cần ≥ 2 đỉnh")
        xs = [self.V[d][0] for d in dinh]; ys = [self.V[d][1] for d in dinh]
        self._diem(ten, sum(xs) / len(xs), sum(ys) / len(ys),
                   nhan=nhan, moc=moc, mau=mau)
        self._kh_aff(ten, [(d, 1.0 / len(dinh)) for d in dinh])   # [33s] độ sâu = trung bình
        return self

    # ─────────────────────────────────────────────────────────────
    def chop(self, day, dinh='S', cao=2.6, ten_day=None,
             goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=False):
        """CHÓP đáy ĐA GIÁC bất kỳ + 1 đỉnh (apex) trên tâm đáy — phối cảnh xiên,
        NÉT KHUẤT tự tính theo che.

        day     : dict SPEC đáy như lang_tru_dung (loai + số đo + nhan) HOẶC list điểm.
                  Loại dùng nhiều: 'tam_giac'{a,b,c} · 'chu_nhat'{a,b} ·
                  'binh_hanh'{canh_day,canh_ben,goc} · 'da_giac'{diem:[...]}.
        dinh    : tên đỉnh chóp (apex), vd 'S'.
        cao     : chiều cao chóp (độ dài VẼ apex trên tâm đáy). >0.
        ten_day : list tên đỉnh đáy (vd ['A','B','C','D']). None → đỉnh đáy ẩn.

        Máy tự tính toạ độ + nét khuất — AI không đụng toạ độ (Đ5.9).
        """
        pts, canh_nhan = _day_polygon(day)
        n = len(pts)
        if n < 3:
            raise ValueError("[chop] đáy cần ≥ 3 đỉnh")
        if not (cao > 0):
            raise ValueError("[chop] cao phải > 0")
        self._nen_luoi = False
        ox, oy = goc_o
        c = math.cos(math.radians(_GOC_SAU)); s = math.sin(math.radians(_GOC_SAU))
        # đáy nằm NGANG (floor), chiếu xiên; apex trên tâm đáy + cao
        floor = [(ox + u + _CO_SAU * v * c, oy + _CO_SAU * v * s) for (u, v) in pts]
        gx = sum(x for x, _ in floor) / n
        gy = sum(y for _, y in floor) / n
        apex = (gx, gy + cao)
        # nét khuất: đỉnh đáy KHUẤT ⇔ nằm TRONG bao lồi của (đáy ∪ apex)
        hull = _hull(floor + [apex])
        an = [(round(floor[i][0], 4), round(floor[i][1], 4)) not in hull for i in range(n)]

        # tên đỉnh
        if ten_day:
            if len(ten_day) != n:
                raise ValueError(f"[chop] ten_day cần đủ {n} tên")
            dnames = list(ten_day)
        else:
            dnames = [f'_d{i}' for i in range(n)]
        show = bool(ten_day)
        # vị trí nhãn đáy: đẩy ra ngoài tâm
        for i in range(n):
            x, y = floor[i]
            dx, dy = x - gx, y - gy
            if abs(dx) >= abs(dy):
                pos = 'right' if dx >= 0 else 'left'
            else:
                pos = 'above' if dy >= 0 else 'below'
            self._diem(dnames[i], x, y, nhan=(pos if show else None), moc=show)
        self._diem(dinh, apex[0], apex[1], nhan=('above' if (show or True) else None),
                   moc=True)

        # [33s] bật engine nét khuất: toạ độ 3D (đáy w=0, apex w=cao) + mặt
        if net_khuat:
            self._kh_bat()
            for i in range(n):
                self._kh_put(dnames[i], floor[i][0], floor[i][1], pts[i][1])
            vS = sum(p[1] for p in pts) / n                 # độ sâu apex = trọng tâm đáy
            self._kh_put(dinh, apex[0], apex[1], vS)
            self._kh_faces = [list(dnames)]                 # mặt đáy
            for i in range(n):                              # n mặt bên
                self._kh_faces.append([dinh, dnames[i], dnames[(i + 1) % n]])

        # cạnh đáy: liền/đứt theo che
        for i in range(n):
            j = (i + 1) % n
            self.doan(dnames[i], dnames[j], net=('dut' if (an[i] or an[j]) else 'lien'))
        # cạnh bên (apex→đỉnh đáy): đứt nếu đỉnh đáy khuất
        for i in range(n):
            self.doan(dinh, dnames[i], net=('dut' if an[i] else 'lien'))

        # nhãn cạnh đáy (nếu khai)
        for i in range(n):
            if canh_nhan[i]:
                (x1, y1), (x2, y2) = floor[i], floor[(i + 1) % n]
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                vx, vy = mx - gx, my - gy; L = math.hypot(vx, vy) or 1.0
                self.ghi_chu(mx + vx / L * 0.34, my + vy / L * 0.34, canh_nhan[i])
        return self
