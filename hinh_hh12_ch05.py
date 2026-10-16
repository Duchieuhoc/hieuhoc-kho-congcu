#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh12_ch05.py — ĐỐI TƯỢNG GIẢI TÍCH trong Oxyz (Chương V lớp 12):
#   MẶT PHẲNG · HAI MẶT PHẲNG · MẶT CẦU · ĐƯỜNG THẲNG · HAI ĐƯỜNG THẲNG ·
#   MẶT PHẲNG THEO ĐOẠN CHẮN.
#   class HinhCh05(HinhOxyz): nối tiếp phép chiếu xiên [32y] (Oz↑/Oy→/Ox 218°).
#
#   ADDITIVE — module ĐỘC LẬP (import HinhOxyz), KHÔNG đụng hinh_core/hinh_coban/
#     hinh_hh12_oxyz. Chỉ dùng op renderer sẵn có (tron/doan/vecto/to_mien/ghi_chu)
#     ⇒ 0 regression. Căn cứ: DE_XUAT_CHUAN_PHOI_CANH__HH12_CH05 (OB 2026-10-14, đã duyệt).
#
#   Đ5.9 hai chế độ (đã duyệt §3):
#     • coordinate-tied (mặt cầu · đoạn chắn · đt cho toạ độ): truyền toạ-độ-toán
#       từ ĐỀ, máy chiếu.
#     • schematic (mp α tổng quát · cặp VTCP · 2 đt minh hoạ): không toạ độ đề → kho
#       đặt phối cảnh canonical; OB khai PHẦN TỬ + QUAN HỆ.
# ═══════════════════════════════════════════════════════════════════
import math
from hinh_hh12_oxyz import HinhOxyz


class HinhCh05(HinhOxyz):
    """Đối tượng giải tích Oxyz lớp 12 (CH05). Nối tiếp HinhOxyz."""

    # ───────────────────────── tiện ích nội bộ ─────────────────────────
    def _goc_vuong_man(self, tenP, u, v, canh=0.26, mau=None):
        """Dấu GÓC VUÔNG tại điểm (màn hình) tenP, giữa hai hướng màn hình u, v (đã chuẩn hoá)."""
        px, py = self.V[tenP]
        def _n(w):
            L = math.hypot(*w) or 1.0
            return (w[0] / L * canh, w[1] / L * canh)
        ux, uy = _n(u); vx, vy = _n(v)
        a = (px + ux, py + uy); b = (px + ux + vx, py + uy + vy); c = (px + vx, py + vy)
        na, nb, nc = f'_gv{len(self.V)}a', f'_gv{len(self.V)}b', f'_gv{len(self.V)}c'
        self._diem(na, *a, nhan=None, moc=False)
        self._diem(nb, *b, nhan=None, moc=False)
        self._diem(nc, *c, nhan=None, moc=False)
        self.doan(na, nb, mau=mau); self.doan(nb, nc, mau=mau)
        return self

    # ═══════════════════ (a) MẶT PHẲNG (schematic) ═══════════════════
    def mat_phang(self, nhan=r'(\alpha)', vtpt=False, nhan_n=r'\vec n',
                  cap_vtcp=False, nhan_uv=(r'\vec u', r'\vec v'),
                  diem_ngoai=False, mau='blue!9', pos=(0.0, 0.0),
                  rw=1.75, rd=1.15):
        """MẶT PHẲNG schematic = hình bình hành phối cảnh (hình bình hành trên nền z=0).

        vtpt       : True → vectơ pháp tuyến hướng lên + dấu góc vuông với mp.
        cap_vtcp   : True → cặp vectơ chỉ phương u, v nằm trong mp (từ tâm).
        diem_ngoai : True → điểm M ngoài mp + chân vuông góc N + đoạn MN (H5.13).
        pos        : (x0,y0) dời tâm hình bình hành theo (Oy,Oz-man) để đặt nhiều hình.
        Schematic (Đ5.9 chế độ 2): toạ độ canonical do kho đặt; OB khai phần tử."""
        x0, y0 = pos
        # 4 đỉnh hình bình hành trên nền z=0 (rectangle math → parallelogram phối cảnh)
        C = [(-rw, -rd, 0), (rw, -rd, 0), (rw, rd, 0), (-rw, rd, 0)]
        nm = []
        for i, (a, b, c) in enumerate(C):
            t = f'_mp{len(self.V)}_{i}'
            # dời theo mặt phẳng vẽ: cộng offset màn hình sau khi chiếu
            sx, sy = self._P(a, b, c); sx += x0; sy += y0
            self._diem(t, sx, sy, nhan=None, moc=False); nm.append(t)
        self.to_mien(*nm, mau=mau)
        for i in range(4):
            self.doan(nm[i], nm[(i + 1) % 4])
        # nhãn mp ở góc phải-dưới hình bình hành
        gx, gy = self.V[nm[1]]
        self.ghi_chu(gx + 0.12, gy - 0.30, _m(nhan))
        # tâm (màn hình)
        cx = sum(self.V[t][0] for t in nm) / 4
        cy = sum(self.V[t][1] for t in nm) / 4
        tam = f'_mpO{len(self.V)}'; self._diem(tam, cx, cy, nhan=None, moc=False)
        if vtpt:
            top = f'_mpn{len(self.V)}'; self._diem(top, cx, cy + 2.2, nhan=None, moc=False)
            self.vecto(tam, top, nhan=None, mau='red', rong='dam')
            self.ghi_chu(cx + 0.12, cy + 2.2, _m(nhan_n), mau='red')
            # dấu góc vuông giữa pháp tuyến (lên) và một hướng trong mp (sang phải)
            din = (self.V[nm[1]][0] - cx, self.V[nm[1]][1] - cy)
            self._goc_vuong_man(tam, (0, 1), din, mau='red')
            self.moc.discard(tam)
        if cap_vtcp:
            pu = f'_mpu{len(self.V)}'; pv = f'_mpv{len(self.V)}'
            ux, uy = self.V[nm[1]]; vx, vy = self.V[nm[3]]
            self._diem(pu, cx + (ux - cx) * 0.6, cy + (uy - cy) * 0.6, nhan=None, moc=False)
            self._diem(pv, cx + (vx - cx) * 0.6, cy + (vy - cy) * 0.6, nhan=None, moc=False)
            self.vecto(tam, pu, nhan=None, mau='red', rong='dam')
            self.vecto(tam, pv, nhan=None, mau='red', rong='dam')
            self.ghi_chu(*self.V[pu], _m(nhan_uv[0]), mau='red')
            self.ghi_chu(self.V[pv][0] - 0.3, self.V[pv][1] + 0.05, _m(nhan_uv[1]), mau='red')
            self.moc.discard(tam)
        if diem_ngoai:
            M = f'_mpM{len(self.V)}'; N = tam
            self._diem(M, cx + 0.25, cy + 1.9, nhan=None, moc=True)
            self.ghi_chu(cx + 0.33, cy + 1.95, 'M')
            self.doan(M, N, net='lien')
            self.ghi_chu(cx - 0.32, cy + 0.9, 'd', mau=None)
            self._goc_vuong_man(N, (0, 1), (self.V[nm[1]][0] - cx, self.V[nm[1]][1] - cy))
            self.ghi_chu(cx - 0.05, cy - 0.34, 'N')
            self.moc.add(N)
        return self

    # ═══════════════════ (a′) HAI MẶT PHẲNG (quan hệ) ═══════════════════
    def hai_mat_phang(self, quan_he='cat', nhan=(r'(P)', r'(Q)'), vtpt=True):
        """HAI MẶT PHẲNG ở quan hệ: 'song_song' | 'vuong_goc' | 'cat'.
        vtpt=True → vẽ VTPT n, n'. Schematic (Đ5.9 chế độ 2)."""
        if quan_he == 'song_song':
            self.mat_phang(nhan=nhan[0], vtpt=vtpt, nhan_n=r'\vec n', pos=(0.0, 0.0),
                           rw=1.7, rd=1.05, mau='blue!9')
            self.mat_phang(nhan=nhan[1], vtpt=vtpt, nhan_n=r"\vec{n'}", pos=(0.9, 1.9),
                           rw=1.7, rd=1.05, mau='green!10')
        elif quan_he == 'vuong_goc':
            # mp ngang (P) + mp đứng (Q) cắt nhau vuông góc
            self.mat_phang(nhan=nhan[0], vtpt=False, pos=(0.0, 0.0), rw=1.9, rd=1.15, mau='blue!9')
            # mp đứng: hình bình hành trong mặt phẳng chứa Oz (dùng toạ độ y-z)
            C = [(-0.1, -1.2, 0), (-0.1, 1.2, 0), (-0.1, 1.2, 2.3), (-0.1, -1.2, 2.3)]
            nm = []
            for i, (a, b, c) in enumerate(C):
                t = f'_q{len(self.V)}_{i}'; sx, sy = self._P(a, b, c)
                self._diem(t, sx, sy, nhan=None, moc=False); nm.append(t)
            self.to_mien(*nm, mau='green!10')
            for i in range(4):
                self.doan(nm[i], nm[(i + 1) % 4])
            self.ghi_chu(self.V[nm[2]][0] + 0.1, self.V[nm[2]][1], _m(nhan[1]))
            # dấu góc vuông tại giao tuyến
            self._goc_vuong_man(nm[0], (1, 0), (0, 1))
            if vtpt:
                cx = sum(self.V[t][0] for t in nm) / 4; cy = sum(self.V[t][1] for t in nm) / 4
                p = f'_qn{len(self.V)}'; self._diem(p, cx - 1.6, cy, nhan=None, moc=False)
                tam = f'_qc{len(self.V)}'; self._diem(tam, cx, cy, nhan=None, moc=False)
                self.vecto(tam, p, nhan=None, mau='red', rong='dam')
                self.ghi_chu(cx - 1.95, cy + 0.05, r"$\vec{n'}$", mau='red')
        else:  # cat
            self.mat_phang(nhan=nhan[0], vtpt=False, pos=(0.0, 0.0), rw=1.9, rd=1.1, mau='blue!9')
            C = [(-1.0, 0.0, -1.1), (1.6, 0.0, -0.5), (1.6, 0.0, 1.9), (-1.0, 0.0, 1.3)]
            nm = []
            for i, (a, b, c) in enumerate(C):
                t = f'_q{len(self.V)}_{i}'; sx, sy = self._P(a, b, c)
                self._diem(t, sx, sy, nhan=None, moc=False); nm.append(t)
            self.to_mien(*nm, mau='green!10')
            for i in range(4):
                self.doan(nm[i], nm[(i + 1) % 4])
            self.ghi_chu(self.V[nm[2]][0] + 0.1, self.V[nm[2]][1], _m(nhan[1]))
            if vtpt:
                for (cxn, cyn, lb, dx) in [(-1.3, 1.3, r'$\vec n$', 0.0),
                                           (1.5, 1.3, r"$\vec{n'}$", 0.1)]:
                    tam = f'_c{len(self.V)}'; p = f'_cp{len(self.V)}'
                    self._diem(tam, cxn, cyn, nhan=None, moc=False)
                    self._diem(p, cxn, cyn + 1.3, nhan=None, moc=False)
                    self.vecto(tam, p, nhan=None, mau='red', rong='dam')
                    self.ghi_chu(cxn + dx, cyn + 1.35, lb, mau='red')
        return self

    # ═══════════════════ (d) MẶT PHẲNG THEO ĐOẠN CHẮN ═══════════════════
    def mat_phang_doan_chan(self, a, b, c, nhan=r'(\alpha)', to=True,
                            ten=('A', 'B', 'C')):
        """MẶT PHẲNG cắt 3 trục tại A(a;0;0), B(0;b;0), C(0;0;c) — coordinate-tied.
        GỌI he_truc() TRƯỚC. a,b,c > 0 (toạ độ đề)."""
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("[mat_phang_doan_chan] a, b, c > 0")
        A, B, Cc = ten
        self._dat(A, a, 0, 0, nhan='below', moc=True)
        self._dat(B, 0, b, 0, nhan='right', moc=True)
        self._dat(Cc, 0, 0, c, nhan='above', moc=True)
        if to:
            self.to_mien(A, B, Cc, mau='blue!10')
        self.doan(A, B); self.doan(B, Cc); self.doan(Cc, A)
        # nhãn mp ở tâm tam giác vết
        cx = (self.V[A][0] + self.V[B][0] + self.V[Cc][0]) / 3
        cy = (self.V[A][1] + self.V[B][1] + self.V[Cc][1]) / 3
        self.ghi_chu(cx - 0.1, cy, _m(nhan))
        return self

    # ═══════════════════ (b) MẶT CẦU ═══════════════════
    def mat_cau(self, tam=(0.0, 0.0, 0.0), R=1.3, nhan=r'(S)', tam_ten='I',
                ban_kinh=True, diem=None, duong_kinh=None, rb_ti=0.34):
        """MẶT CẦU tâm I(tam) bán kính R — coordinate-tied (toạ độ + R từ đề).
        Viền = đường tròn (quy ước SGK); xích đạo = ellipse ngang (nửa sau nét đứt).
        diem=('M',x,y,z) điểm trên/ngoài mặt + bán kính tới M. duong_kinh=('A','B').
        rb_ti : tỉ lệ bán trục phụ ellipse xích đạo (mặc định 0,34·R — chuẩn mock)."""
        ix, iy, iz = tam
        Icx, Icy = self._P(ix, iy, iz)
        self._diem(tam_ten, Icx, Icy, nhan='below', moc=True)
        # viền cầu = đường tròn bán kính R (màn hình)
        self.tikz.append(('tron', tam_ten, float(R), 'blue!65!black', 'lien'))
        # xích đạo = ellipse ngang: nửa dưới (gần) liền, nửa trên (xa) đứt
        rb = rb_ti * R
        def _pts(a0, a1, n=28):
            out = []
            for k in range(n + 1):
                ang = math.radians(a0 + (a1 - a0) * k / n)
                out.append((Icx + R * math.cos(ang), Icy + rb * math.sin(ang)))
            return out
        for seg, net in ((_pts(180, 360), 'lien'), (_pts(0, 180), 'dut')):
            nmprev = None
            for j, (sx, sy) in enumerate(seg):
                t = f'_eq{len(self.V)}'
                self._diem(t, sx, sy, nhan=None, moc=False)
                if nmprev is not None:
                    self.doan(nmprev, t, net=net, mau='blue!65!black')
                nmprev = t
        # nhãn mặt cầu (góc trên phải)
        self.ghi_chu(Icx + R * 0.72, Icy + R * 0.72, _m(nhan))
        # điểm M + bán kính
        if diem is not None:
            Mn, mx, my, mz = diem
            Msx, Msy = self._P(mx, my, mz)
            self._diem(Mn, Msx, Msy, nhan='above right', moc=True, mau='red')
            if ban_kinh:
                self.doan(tam_ten, Mn, mau='red')
                midx = (Icx + Msx) / 2; midy = (Icy + Msy) / 2
                self.ghi_chu(midx + 0.06, midy + 0.06, '$R$', mau='red')
        if duong_kinh is not None:
            (An, ax, ay, az), (Bn, bx, by, bz) = duong_kinh
            Asx, Asy = self._P(ax, ay, az); Bsx, Bsy = self._P(bx, by, bz)
            self._diem(An, Asx, Asy, nhan='above left', moc=True)
            self._diem(Bn, Bsx, Bsy, nhan='below right', moc=True)
            self.doan(An, Bn)
        return self

    # ═══════════════════ (c) ĐƯỜNG THẲNG ═══════════════════
    def duong_thang(self, qua=None, vtcp=None, ten=r'\Delta', nhan_u=r'\vec u',
                    diem_qua=None, pos=(0.0, 0.0), huong=(2.6, 1.3)):
        """ĐƯỜNG THẲNG + VTCP. Coordinate-tied nếu truyền qua=(x,y,z)+vtcp=(a,b,c)
        (cần he_truc); schematic nếu để None (đặt phối cảnh canonical theo huong)."""
        if qua is not None and vtcp is not None:
            qx, qy, qz = qua; vx, vy, vz = vtcp
            L = 2.0
            A = self._P(qx - vx * L, qy - vy * L, qz - vz * L)
            B = self._P(qx + vx * L, qy + vy * L, qz + vz * L)
            Qp = self._P(qx, qy, qz)
            mid = self._P(qx + vx * 0.9, qy + vy * 0.9, qz + vz * 0.9)
        else:
            hx, hy = huong; ox, oy = pos
            A = (ox - hx, oy - hy); B = (ox + hx, oy + hy)
            Qp = (ox, oy); mid = (ox + hx * 0.55, oy + hy * 0.55)
        na, nb = f'_dA{len(self.V)}', f'_dB{len(self.V)}'
        self._diem(na, *A, nhan=None, moc=False); self._diem(nb, *B, nhan=None, moc=False)
        self.doan(na, nb)
        self.ghi_chu(B[0] + 0.1, B[1] + 0.02, _m(ten))
        # VTCP từ giữa
        nm, nq = f'_dM{len(self.V)}', f'_dQ{len(self.V)}'
        self._diem(nm, *Qp, nhan=None, moc=False); self._diem(nq, *mid, nhan=None, moc=False)
        self.vecto(nm, nq, nhan=None, mau='red', rong='dam')
        self.ghi_chu(mid[0] + 0.06, mid[1] - 0.22, _m(nhan_u), mau='red')
        return self

    # ═══════════════════ (c′) HAI ĐƯỜNG THẲNG ═══════════════════
    def hai_duong_thang(self, quan_he='cheo', ten=(r'\Delta_1', r'\Delta_2'),
                        vtcp=True):
        """HAI ĐƯỜNG THẲNG schematic: 'cat' | 'song_song' | 'cheo' | 'vuong_goc'.
        'cheo' → đoạn giao của đt sau vẽ NÉT ĐỨT (biểu thị đi sau). Đ5.9 chế độ 2."""
        # d1
        a1, b1 = (-2.0, -1.0), (2.3, 1.1)
        na, nb = '_l1a', '_l1b'
        self._diem(na, *a1, nhan=None, moc=False); self._diem(nb, *b1, nhan=None, moc=False)
        self.doan(na, nb)
        self.ghi_chu(b1[0] + 0.12, b1[1], _m(ten[0]))
        if vtcp:
            m1, q1 = '_l1m', '_l1q'
            self._diem(m1, (a1[0]+b1[0])/2, (a1[1]+b1[1])/2, nhan=None, moc=False)
            self._diem(q1, (a1[0]+b1[0])/2 + 0.95, (a1[1]+b1[1])/2 + 0.44, nhan=None, moc=False)
            self.vecto(m1, q1, nhan=None, mau='red', rong='dam')
            self.ghi_chu(self.V[q1][0] + 0.05, self.V[q1][1] - 0.2, r'$\vec{u_1}$', mau='red')
        if quan_he == 'song_song':
            a2, b2 = (-2.0, 0.2), (2.3, 2.3)
        elif quan_he == 'cat':
            a2, b2 = (-1.6, 1.6), (2.0, -1.3)
        else:  # cheo / vuong_goc
            a2, b2 = (-1.4, 1.7), (2.0, -1.2)
        # d2 với đoạn giữa đứt nếu chéo
        if quan_he == 'cheo':
            pa = (a2[0] + 0.40*(b2[0]-a2[0]), a2[1] + 0.40*(b2[1]-a2[1]))
            pb = (a2[0] + 0.60*(b2[0]-a2[0]), a2[1] + 0.60*(b2[1]-a2[1]))
            for (p, q, net) in ((a2, pa, 'lien'), (pa, pb, 'dut'), (pb, b2, 'lien')):
                np_, nq_ = f'_l2{len(self.V)}a', f'_l2{len(self.V)}b'
                self._diem(np_, *p, nhan=None, moc=False); self._diem(nq_, *q, nhan=None, moc=False)
                self.doan(np_, nq_, net=net)
        else:
            na2, nb2 = '_l2a', '_l2b'
            self._diem(na2, *a2, nhan=None, moc=False); self._diem(nb2, *b2, nhan=None, moc=False)
            self.doan(na2, nb2)
        self.ghi_chu(b2[0] + 0.08, b2[1] - 0.15, _m(ten[1]))
        if vtcp:
            m2, q2 = '_l2m', '_l2q'
            self._diem(m2, a2[0] + 0.22*(b2[0]-a2[0]), a2[1] + 0.22*(b2[1]-a2[1]), nhan=None, moc=False)
            self._diem(q2, a2[0] + 0.22*(b2[0]-a2[0]) + 0.7, a2[1] + 0.22*(b2[1]-a2[1]) - 0.6, nhan=None, moc=False)
            self.vecto(m2, q2, nhan=None, mau='green!55!black', rong='dam')
            self.ghi_chu(self.V[q2][0] - 0.5, self.V[q2][1] + 0.02, r'$\vec{u_2}$', mau='green!55!black')
        return self


def _m(s):
    """Nhãn toán: bọc $...$ nếu chưa có."""
    s = str(s)
    return s if '$' in s else ('$' + s + '$')
