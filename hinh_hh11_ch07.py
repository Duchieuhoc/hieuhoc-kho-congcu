#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh11_ch07.py — MẠCH HÌNH KHÔNG GIAN: QUAN HỆ VUÔNG GÓC
#   Hình học 11, Chương VII (Bộ KNTT). class HinhHH11CH07(HinhHH11CH04).
#   Thêm primitive ĐẶC THÙ chương vuông góc — KẾ THỪA nguyên khối/mp/đoạn
#   từ mạch ch04→hh12_ch02→khoihop→coban. ADDITIVE: bài cũ 0 đổi.
#   Triết lý Đ5.9: AI khai NGHĨA (khối/điểm/quan hệ) — MÁY giữ toạ độ
#   phối cảnh; AI KHÔNG cấp toạ độ.
#   Căn cứ: CHUẨN PHỐI CẢNH 3D (duyệt 2026-10-12) · DE_XUAT_VA_KHO__HH11_CH07.
# ═══════════════════════════════════════════════════════════════════
import math

def _nm(s):
    """Bọc nhãn mặt phẳng: chuỗi trần → $(...)$."""
    return s if (s.startswith("$") or s is None) else f"${s}$"
from hinh_hh11_ch04 import HinhHH11CH04


class HinhHH11CH07(HinhHH11CH04):
    """Mạch quan hệ vuông góc lớp 11. Kế thừa toàn bộ mạch không gian ch04."""

    # ══════ R-vuong3d · KÝ HIỆU GÓC VUÔNG SCHEMATIC (phối cảnh) ══════
    def o_vuong_3d(self, ten, mau=None):
        """Đánh Ô VUÔNG ⊥ cho hình PHỐI CẢNH — KHÔNG ràng PHANH do=90.
        Lý do: góc chiếu xiên ≠ 90° trên màn, nhưng ⊥ là THẬT trong không gian
        (Đ5.9: máy giữ toạ độ, nghĩa ⊥ do người khai). Ô vẽ theo HƯỚNG CHIẾU
        thật của 2 cạnh (reuse renderer _o_vuong). ten=(canh1, đỉnh, canh2) đã đặt.
        → Dùng cho MỌI ký hiệu vuông góc trong hình không gian (trụ cột CH07)."""
        for p in ten:
            if p not in self.V:
                raise ValueError(f"[o_vuong_3d] điểm '{p}' chưa đặt.")
        self.tikz.append(('goc_vuong', list(ten), mau))
        return self

    # ══════ R-cunggoc3d · CUNG GÓC SCHEMATIC (phối cảnh) ══════
    def cung_goc_3d(self, ten, nhan=None, mau='orange', br=6):
        """Vẽ CUNG đánh dấu GÓC cho hình PHỐI CẢNH — KHÔNG ràng PHANH số đo.
        Lý do: góc chiếu xiên ≠ góc thật (Đ5.9: máy giữ toạ độ, nghĩa góc do người khai);
        so_do_goc/goc cũ ràng PHANH số đo → DỪNG trong phối cảnh. Cung vẽ theo hướng
        CHIẾU thật của 2 cạnh. ten=(canh1, đỉnh, canh2) đã đặt. nhan: nhãn góc (vd 'α',
        '45°' — chuỗi LaTeX, hiện cạnh cung); None → chỉ cung trơn. br: bán kính cung (mm).
        → Góc đt–mp (chân hình chiếu), góc giữa 2 đường trong khối, góc cần tính (nhan=None
        ở hình ĐỀ — Đ35 không lộ số)."""
        for q in ten:
            if q not in self.V:
                raise ValueError(f"[cung_goc_3d] điểm '{q}' chưa đặt.")
        # cung trơn (hien=False → renderer KHÔNG tự thêm ^circ): (ten, do, hien, mau, br)
        self.tikz.append(('goc', list(ten), '', False, mau, br))
        # nhãn góc tự đặt tại phân giác (tránh renderer ép '^\\circ' cho tên góc như α)
        if nhan:
            import math as _m
            c1, d, c2 = ten
            (ox, oy) = self.V[d]
            def _u(P):
                vx, vy = self.V[P][0]-ox, self.V[P][1]-oy
                L = _m.hypot(vx, vy) or 1.0
                return vx/L, vy/L
            u1 = _u(c1); u2 = _u(c2)
            bx, by = u1[0]+u2[0], u1[1]+u2[1]
            L = _m.hypot(bx, by) or 1.0
            r = br/10.0 + 0.28
            self.ghi_chu(ox + bx/L*r, oy + by/L*r, f'${nhan}$' if not str(nhan).startswith('$') else str(nhan))
        return self

    # ══════ R-dtmp · ĐƯỜNG THẲNG VUÔNG GÓC MẶT PHẲNG ══════
    def duong_vuong_goc_mp(self, S='S', H='H', K='M', nhan_mp='(P)',
                           u=0.0, v=0.0, cao=2.3, rw=2.2, rd=1.4,
                           goc=(0.0, 0.0), net_SH='lien', o_vuong=True,
                           duong=None):
        """DỰNG mặt phẳng (P) + đường SH ⊥ (P) tại chân H.
        S = đỉnh NGOÀI mp; H = CHÂN vuông góc (trên mp); K = điểm phụ trên mp
        (lệch khỏi H) để đánh ô vuông ⊥. (u,v) = vị trí chân trên mp (canonical,
        Đ5.9 chế độ schematic). cao = độ cao S. net_SH='dut' nếu SH khuất.
        duong = list đường phụ ⊂ mp (truyền thẳng cho mat_phang).
        → Trụ cột: H.7.8/7.12/7.13 (đt⊥mp), định lý 3 đường vuông góc, chóp SA⊥đáy."""
        diem = [(H, u, v, 'below'), (K, u + 1.3, v, 'below right')]
        dngo = [(S, u, v, cao, 'above')]
        self.mat_phang(nhan=nhan_mp, goc=goc, rw=rw, rd=rd,
                       diem=diem, diem_ngoai=dngo, duong=duong)
        self.doan(S, H, net=net_SH)     # đường vuông góc
        self.doan(H, K)                 # vệt trong mp (mốc ⊥)
        if o_vuong:
            self.o_vuong_3d((S, H, K))
        return self

    # ══════ R-chop-canh-ben-vuong · CHÓP CÓ CẠNH BÊN ⊥ ĐÁY ══════
    def chop_canh_ben_vuong(self, day, dinh='S', tren='A', cao=2.6,
                            ten_day=None, goc_o=(0.0, 0.0), net_khuat=True,
                            o_vuong=True):
        """CHÓP có CẠNH BÊN ⊥ ĐÁY — apex 'dinh' nằm THẲNG TRÊN đỉnh đáy 'tren'
        (cạnh dinh–tren ⊥ mặt đáy; khác chop chuẩn: apex trên tâm đáy).
        day/ten_day như chop (bắt buộc ten_day để biết đỉnh 'tren'). o_vuong=True →
        đánh ô vuông ⊥ tại chân 'tren' giữa cạnh bên đứng và 1 cạnh đáy kề.
        Máy tự tính toạ độ + nét khuất (Đ5.9). → S.ABC/S.ABCD có SA⊥(đáy)."""
        from hinh_khoihop import _day_polygon, _hull
        import hinh_hh12_ch02 as _M
        _GS, _CS = _M._GOC_SAU, _M._CO_SAU
        pts, _ = _day_polygon(day)
        n = len(pts)
        if n < 3:
            raise ValueError("[chop_canh_ben_vuong] đáy cần ≥ 3 đỉnh")
        if not (cao > 0):
            raise ValueError("[chop_canh_ben_vuong] cao phải > 0")
        if not ten_day or len(ten_day) != n:
            raise ValueError(f"[chop_canh_ben_vuong] cần ten_day đủ {n} tên")
        if tren not in ten_day:
            raise ValueError(f"[chop_canh_ben_vuong] 'tren'='{tren}' không thuộc ten_day")
        idx = list(ten_day).index(tren)
        self._nen_luoi = False
        ox, oy = goc_o
        c = math.cos(math.radians(_GS)); s = math.sin(math.radians(_GS))
        floor = [(ox + u + _CS * v * c, oy + _CS * v * s) for (u, v) in pts]
        gx = sum(x for x, _ in floor) / n
        gy = sum(y for _, y in floor) / n
        apex = (floor[idx][0], floor[idx][1] + cao)     # apex THẲNG TRÊN đỉnh 'tren'
        hull = _hull(floor + [apex])
        an = [(round(floor[i][0], 4), round(floor[i][1], 4)) not in hull for i in range(n)]
        dnames = list(ten_day)
        for i in range(n):
            x, y = floor[i]
            dx, dy = x - gx, y - gy
            if abs(dx) >= abs(dy):
                pos = 'right' if dx >= 0 else 'left'
            else:
                pos = 'above' if dy >= 0 else 'below'
            self._diem(dnames[i], x, y, nhan=pos, moc=True)
        self._diem(dinh, apex[0], apex[1], nhan='above', moc=True)
        if net_khuat:
            self._kh_bat()
            for i in range(n):
                self._kh_put(dnames[i], floor[i][0], floor[i][1], pts[i][1])
            self._kh_put(dinh, apex[0], apex[1], pts[idx][1])   # apex sâu = đỉnh 'tren'
            self._kh_faces = [list(dnames)]
            for i in range(n):
                self._kh_faces.append([dinh, dnames[i], dnames[(i + 1) % n]])
        for i in range(n):
            j = (i + 1) % n
            self.doan(dnames[i], dnames[j], net=('dut' if (an[i] or an[j]) else 'lien'))
        for i in range(n):
            self.doan(dinh, dnames[i], net=('dut' if an[i] else 'lien'))
        if o_vuong:
            ke = dnames[(idx + 1) % n]      # 1 cạnh đáy kề đỉnh 'tren'
            self.o_vuong_3d((dinh, tren, ke))
        return self

    # ══════ R-nhidien · GÓC NHỊ DIỆN (2 nửa mp chung bờ) ══════
    def goc_nhi_dien(self, canh='a', O='O', x='x', y='y', goc_mo=62.0,
                     rw=2.3, rd=1.5, xr=1.5, nhan_mat=(None, None),
                     vuong=False, hien_cung=True, goc=(0.0, 0.0)):
        """GÓC NHỊ DIỆN cạnh 'canh' — 2 nửa mặt phẳng chung bờ (gấp như quyển sách).
        Mặt dưới NGANG; mặt trên nghiêng 'goc_mo'° (= số đo nhị diện). O = điểm trên bờ;
        Ox ⊥ bờ trong mặt dưới, Oy ⊥ bờ trong mặt trên → GÓC PHẲNG xOy. vuong=True →
        goc_mo=90 + ô vuông ⊥ thay cung. nhan_mat=(tên mặt dưới, tên mặt trên) ghi ở góc.
        Đ5.9: khai nghĩa (cạnh/mặt/góc mở) — máy giữ toạ độ phối cảnh."""
        import math
        if vuong:
            goc_mo = 90.0
        ph = math.radians(goc_mo)
        cs, sn = math.cos(ph), math.sin(ph)
        self._nen_luoi = False
        P3 = lambda u, v, w: self._p3(u, v, w, goc)
        # 2 đầu bờ a (chạy theo chiều sâu v)
        a0, a1 = f'_{canh}0', f'_{canh}1'
        self._diem(a0, *P3(0, -rd, 0), nhan=None, moc=False)
        self._diem(a1, *P3(0,  rd, 0), nhan=None, moc=False)
        # 4 góc mặt DƯỚI (ngang) + 4 góc mặt TRÊN (nghiêng)
        pd0, pd1 = f'_md{0}', f'_md{1}'
        self._diem(pd0, *P3(rw, -rd, 0), nhan=None, moc=False)
        self._diem(pd1, *P3(rw,  rd, 0), nhan=None, moc=False)
        pt0, pt1 = f'_mt{0}', f'_mt{1}'
        self._diem(pt0, *P3(rw * cs, -rd, rw * sn), nhan=None, moc=False)
        self._diem(pt1, *P3(rw * cs,  rd, rw * sn), nhan=None, moc=False)
        # tô 2 miền (dưới mọi nét)
        self.to_mien(a0, a1, pd1, pd0, mau='blue!7')
        self.to_mien(a0, a1, pt1, pt0, mau='cyan!12')
        # khung 2 mặt
        for u, v in [(a0, pd0), (pd0, pd1), (pd1, a1)]:
            self.doan(u, v)
        for u, v in [(a0, pt0), (pt0, pt1), (pt1, a1)]:
            self.doan(u, v)
        # BỜ a (đậm hơn — cạnh nhị diện)
        self.doan(a0, a1)
        # O trên bờ + tia Ox (mặt dưới), Oy (mặt trên) ⊥ bờ
        self._diem(O, *P3(0, 0, 0), nhan='below left', moc=True)
        self._diem(x, *P3(xr, 0, 0), nhan='right', moc=True)
        self._diem(y, *P3(xr * cs, 0, xr * sn), nhan='above right', moc=True)
        self.doan(O, x)
        self.doan(O, y)
        # góc phẳng xOy: cung schematic (KHÔNG ràng PHANH) hoặc ô vuông nếu vuông
        if vuong:
            self.o_vuong_3d((x, O, y))
        elif hien_cung:
            self.tikz.append(('goc', [x, O, y], '', False, 'orange', 6))
        # nhãn tên bờ + tên 2 mặt
        bx, by = self.V[a1]
        self.ghi_chu(bx - 0.05, by + 0.20, f'${canh}$')
        if nhan_mat[0]:
            gx, gy = self.V[pd0]
            self.ghi_chu(gx + 0.10, gy - 0.22, _nm(nhan_mat[0]))
        if nhan_mat[1]:
            gx, gy = self.V[pt0]
            self.ghi_chu(gx - 0.30, gy + 0.12, _nm(nhan_mat[1]))
        return self

    # ══════ R-chopcut · CHÓP CỤT ĐỀU (2 đáy đa giác đều ∥) ══════
    def chop_cut_deu(self, n=4, canh_lon=3.2, canh_nho=1.7, cao=2.4,
                     ten_duoi=None, ten_tren=None, goc_o=(0.0, 0.0),
                     duong_cao=False, O='O', Ou="O'"):
        """CHÓP CỤT ĐỀU n cạnh — đáy lớn (dưới) ∥ đáy nhỏ (trên), tâm thẳng trục;
        mặt bên hình thang cân; nét khuất tự tính (đỉnh sau = đứt).
        n=3 (tam giác đều) / 4 (tứ giác đều=vuông) / ... canh_lon>canh_nho>0, cao>0.
        ten_duoi/ten_tren = list tên đỉnh 2 đáy (vd ['A','B','C','D'] / ['A1',...]).
        duong_cao=True → nối tâm O (đáy lớn) – O' (đáy nhỏ) = đường cao + ô vuông đáy.
        Đ5.9: máy giữ toạ độ phối cảnh."""
        import math
        from hinh_khoihop import _hull
        if n < 3 or not (canh_lon > canh_nho > 0) or not (cao > 0):
            raise ValueError("[chop_cut_deu] cần n≥3, canh_lon>canh_nho>0, cao>0")
        self._nen_luoi = False
        ox, oy = goc_o
        Rb = canh_lon / (2 * math.sin(math.pi / n))
        Rt = canh_nho / (2 * math.sin(math.pi / n))
        off = math.pi / 2 + math.pi / n          # xoay để 1 cạnh nằm trước (đáy phẳng trước)
        def ngon(R, w):
            pts = []
            for k in range(n):
                th = off + 2 * math.pi * k / n
                u, v = R * math.cos(th), R * math.sin(th)
                pts.append(self._p3(u, v, w, (ox, oy)))
            return pts
        fb = ngon(Rb, 0.0)       # đáy dưới
        ft = ngon(Rt, cao)       # đáy trên (tâm thẳng trục → cùng off)
        # nét khuất: đỉnh đáy DƯỚI khuất ⇔ ngoài bao lồi toàn hình
        allpts = fb + ft
        hull = _hull(allpts)
        hid = [(round(fb[i][0], 4), round(fb[i][1], 4)) not in hull for i in range(n)]
        dn = list(ten_duoi) if ten_duoi else [f'_cd{i}' for i in range(n)]
        tn = list(ten_tren) if ten_tren else [f'_ct{i}' for i in range(n)]
        show_d, show_t = bool(ten_duoi), bool(ten_tren)
        gx = sum(p[0] for p in fb) / n; gy = sum(p[1] for p in fb) / n
        for i in range(n):
            x, yy = fb[i]; dx, dy = x - gx, yy - gy
            pos = ('right' if dx >= 0 else 'left') if abs(dx) >= abs(dy) else ('above' if dy >= 0 else 'below')
            self._diem(dn[i], x, yy, nhan=(pos if show_d else None), moc=show_d)
        gxt = sum(p[0] for p in ft) / n; gyt = sum(p[1] for p in ft) / n
        for i in range(n):
            x, yy = ft[i]; dx, dy = x - gxt, yy - gyt
            pos = ('right' if dx >= 0 else 'left') if abs(dx) >= abs(dy) else ('above' if dy >= 0 else 'below')
            self._diem(tn[i], x, yy, nhan=(pos if show_t else None), moc=show_t)
        # cạnh đáy dưới
        for i in range(n):
            j = (i + 1) % n
            self.doan(dn[i], dn[j], net=('dut' if (hid[i] or hid[j]) else 'lien'))
        # cạnh đáy trên (luôn thấy)
        for i in range(n):
            self.doan(tn[i], tn[(i + 1) % n])
        # cạnh bên
        for i in range(n):
            self.doan(dn[i], tn[i], net=('dut' if hid[i] else 'lien'))
        # đường cao nối 2 tâm
        if duong_cao:
            self._diem(O, gx, gy, nhan='below', moc=True)
            self._diem(Ou, gxt, gyt, nhan='above', moc=True)
            self.doan(O, Ou, net='dut')
        return self

    # ══════ R-khoi-xien · LĂNG TRỤ XIÊN (cạnh bên KHÔNG ⊥ đáy) ══════
    def lang_tru_xien(self, day, cao=2.4, lech=1.1, ten_duoi=None,
                      ten_tren=None, goc_o=(0.0, 0.0)):
        """LĂNG TRỤ/HỘP XIÊN — đáy trên = đáy dưới TỊNH TIẾN theo cạnh bên nghiêng
        (lệch 'lech' theo phương ngang + lên 'cao'); cạnh bên KHÔNG ⊥ đáy. day như
        chop ('chu_nhat'/'binh_hanh'/'tam_giac'/'da_giac'). ten_duoi/ten_tren = tên
        đỉnh 2 đáy. Nét khuất tự tính (đỉnh sau đứt). Đ5.9: máy giữ toạ độ."""
        import math
        from hinh_khoihop import _day_polygon, _hull
        pts, _ = _day_polygon(day)
        n = len(pts)
        if n < 3 or not (cao > 0):
            raise ValueError("[lang_tru_xien] đáy ≥3 đỉnh, cao>0")
        self._nen_luoi = False
        ox, oy = goc_o
        fb = [self._p3(u, v, 0.0, (ox, oy)) for (u, v) in pts]
        ft = [self._p3(u + lech, v, cao, (ox, oy)) for (u, v) in pts]   # tịnh tiến xiên
        hull = _hull(fb + ft)
        hid = [(round(fb[i][0], 4), round(fb[i][1], 4)) not in hull for i in range(n)]
        dn = list(ten_duoi) if ten_duoi else [f'_xd{i}' for i in range(n)]
        tn = list(ten_tren) if ten_tren else [f'_xt{i}' for i in range(n)]
        gx = sum(p[0] for p in fb) / n; gy = sum(p[1] for p in fb) / n
        gxt = sum(p[0] for p in ft) / n; gyt = sum(p[1] for p in ft) / n
        for i in range(n):
            x, yy = fb[i]; dx, dy = x - gx, yy - gy
            pos = ('right' if dx >= 0 else 'left') if abs(dx) >= abs(dy) else ('above' if dy >= 0 else 'below')
            self._diem(dn[i], x, yy, nhan=(pos if ten_duoi else None), moc=bool(ten_duoi))
        for i in range(n):
            x, yy = ft[i]; dx, dy = x - gxt, yy - gyt
            pos = ('right' if dx >= 0 else 'left') if abs(dx) >= abs(dy) else ('above' if dy >= 0 else 'below')
            self._diem(tn[i], x, yy, nhan=(pos if ten_tren else None), moc=bool(ten_tren))
        for i in range(n):
            j = (i + 1) % n
            self.doan(dn[i], dn[j], net=('dut' if (hid[i] or hid[j]) else 'lien'))
            self.doan(tn[i], tn[j])
            self.doan(dn[i], tn[i], net=('dut' if hid[i] else 'lien'))
        return self
