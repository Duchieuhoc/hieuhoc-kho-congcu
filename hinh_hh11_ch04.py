#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh11_ch04.py — KHÔNG GIAN TỔNG HỢP lớp 11, Chương IV
#   (Quan hệ song song: đường–mặt, mặt–mặt, phép chiếu song song).
#   class HinhHH11CH04(HinhHH12CH02): kế thừa TRỌN khối nền phối cảnh xiên
#     (tu_dien · chop · lang_tru_dung · khoi_hop_chu_nhat · trong_tam) + base
#     (doan · vecto · trung_diem · diem_giua · giao · to_mien · ghi_chu). Thêm
#     TẦNG QUAN HỆ (R) đặc thù HH11: mat_phang · ba_mp · hai_hbh_chung_canh ·
#     thiet_dien · phep_chieu_ss.
#
#   ADDITIVE — module ĐỘC LẬP (import HinhHH12CH02), KHÔNG sửa file kho cũ ⇒
#     0 regression. Phép chiếu xiên GOC_SAU=40°, CO_SAU=0.5 (KHỚP khối nền —
#     mp nền + khối đặt lên cùng hệ chiếu). Affine ⇒ op 2D chạy thẳng.
#   Triết lý Đ5.9: "máy giữ toạ độ, người giữ nghĩa". Hình tổng hợp = SCHEMATIC
#     (không toạ độ đề): kho đặt phối cảnh canonical; OB khai phần tử + quan hệ,
#     chọn vị trí minh hoạ (u,v) để bố trí đẹp — KHÔNG phải toạ độ toán của bài.
#   Căn cứ: DE_XUAT_CHUAN_PHOI_CANH_3D (duyệt 2026-10-12, cổng a+b);
#     6 phiếu khai nghĩa HH11_CH04 (2026-10-23). CS2627.
# ═══════════════════════════════════════════════════════════════════
import math
from hinh_hh12_ch02 import HinhHH12CH02

_GOC = 40.0          # độ nghiêng trục chiều sâu (KHỚP hinh_khoihop/hh12_ch02)
_CO  = 0.5           # hệ số co chiều sâu


def _m(s):
    """Nhãn toán: bọc $...$ nếu chưa có. None/'' → '' (không in)."""
    if s is None:
        return ''
    s = str(s)
    if s == '':
        return ''
    return s if '$' in s else ('$' + s + '$')


class HinhHH11CH04(HinhHH12CH02):
    """Không gian tổng hợp lớp 11 (quan hệ song song). Nối tiếp HinhHH12CH02."""

    # [33s] ENGINE NÉT KHUẤT mặc định BẬT cho chương quan hệ không gian lớp 11
    #        (hình biểu diễn chuẩn SGK: đường bị khối che = nét đứt, máy tự tính).
    #        Truyền net_khuat=False để tắt cho ca đặc biệt nếu cần.
    def tu_dien(self, nhan='ABCD', dinh_tren=None, canh=3.0,
                goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=True):
        return super().tu_dien(nhan, dinh_tren=dinh_tren, canh=canh,
                               goc_o=goc_o, hien_nhan=hien_nhan, net_khuat=net_khuat)

    def chop(self, day, dinh='S', cao=2.6, ten_day=None,
             goc_o=(0.0, 0.0), hien_nhan=True, net_khuat=True):
        return super().chop(day, dinh=dinh, cao=cao, ten_day=ten_day,
                            goc_o=goc_o, hien_nhan=hien_nhan, net_khuat=net_khuat)

    # ─────────────── phép chiếu xiên nội bộ (khớp khối nền) ───────────────
    def _p3(self, u, v, w=0.0, goc=(0.0, 0.0)):
        """Chiếu điểm (u=ngang, v=sâu, w=cao) → màn hình. Affine cố định."""
        ox, oy = goc
        c = math.cos(math.radians(_GOC)); s = math.sin(math.radians(_GOC))
        return (ox + u + _CO * v * c, oy + _CO * v * s + w)

    # ═══════════════════ R-mp · MẶT PHẲNG BIỂU DIỄN ═══════════════════
    def mat_phang(self, nhan='(P)', goc=(0.0, 0.0), rw=2.0, rd=1.3, mau='blue!8',
                  diem=None, duong=None, diem_ngoai=None, pre=None, to=True):
        """MẶT PHẲNG schematic = hình bình hành phối cảnh nghiêng (nền cao w=0).

        nhan       : nhãn mp ghi ở GÓC (vd '(P)', r'(\\alpha)').
        goc        : (ox,oy) dời cả mp (đặt nhiều mp).
        rw, rd     : nửa bề rộng (ngang) / nửa bề sâu của hình bình hành.
        diem       : list điểm NẰM TRÊN mp: (ten, u, v[, nhan_pos]). u∈[-rw,rw], v∈[-rd,rd].
        duong      : list đường ⊂ mp: (ten, (u1,v1), (u2,v2)[, net[, mau[, nhan]]]).
        diem_ngoai : list điểm NGOÀI mp (có cao): (ten, u, v, cao[, nhan_pos]).
        pre        : tiền tố tên nội bộ (tránh trùng khi nhiều mp); None → tự sinh.
        to         : True → tô nhạt miền mp.

        Schematic (Đ5.9 chế độ 2): vị trí (u,v) là minh hoạ canonical, KHÔNG phải
        toạ độ toán của đề. Điểm/đường đặt có TÊN → dùng được với doan/giao/... base.
        """
        self._nen_luoi = False
        tag = pre if pre is not None else f'mp{len(self.V)}'
        corners = [(-rw, -rd), (rw, -rd), (rw, rd), (-rw, rd)]
        cn = []
        for i, (u, v) in enumerate(corners):
            t = f'_{tag}c{i}'
            self._diem(t, *self._p3(u, v, 0, goc), nhan=None, moc=False)
            cn.append(t)
        if to:
            self.to_mien(*cn, mau=mau)
        for i in range(4):
            self.doan(cn[i], cn[(i + 1) % 4])
        # nhãn mp ở gần góc phải-dưới
        gx, gy = self.V[cn[1]]
        self.ghi_chu(gx + 0.14, gy - 0.26, _m(nhan))
        # điểm trên mp
        for it in (diem or []):
            ten, u, v = it[0], it[1], it[2]
            npos = it[3] if len(it) > 3 else 'above'
            self._diem(ten, *self._p3(u, v, 0, goc), nhan=npos, moc=True)
        # đường trên mp
        for it in (duong or []):
            ten, (u1, v1), (u2, v2) = it[0], it[1], it[2]
            net = it[3] if len(it) > 3 else 'lien'
            mu = it[4] if len(it) > 4 else None
            nh = it[5] if len(it) > 5 else None
            a, b = f'_{tag}{ten}a', f'_{tag}{ten}b'
            self._diem(a, *self._p3(u1, v1, 0, goc), nhan=None, moc=False)
            self._diem(b, *self._p3(u2, v2, 0, goc), nhan=None, moc=False)
            self.doan(a, b, net=net, mau=mu)
            if nh:
                bx, by = self.V[b]
                self.ghi_chu(bx + 0.10, by + 0.04, _m(nh), mau=mu)
        # điểm ngoài mp (có cao)
        for it in (diem_ngoai or []):
            ten, u, v, cao = it[0], it[1], it[2], it[3]
            npos = it[4] if len(it) > 4 else 'above'
            self._diem(ten, *self._p3(u, v, cao, goc), nhan=npos, moc=True)
        return self

    # ═══════════════════ R-3mp · BA MẶT PHẲNG ═══════════════════
    def ba_mp(self, quan_he='song_song', nhan=('(P)', '(Q)', '(R)'),
              cat_tuyen=False):
        """BA MẶT PHẲNG.
        quan_he='song_song' → 3 hbh chồng song song (Thalès H4.48); cat_tuyen=True
          thêm 2 cát tuyến xuyên 3 mp (đặt điểm A,B,C / A',B',C').
        quan_he='cat'        → 3 mp đôi một cắt nhau kiểu 'quyển sách' (H4.23/24).
        Trả về self. (Định lí 3 giao tuyến / Thalès — schematic.)"""
        self._nen_luoi = False
        if quan_he == 'song_song':
            dy = 1.9
            for k, lb in enumerate(nhan):
                self.mat_phang(nhan=lb, goc=(0.0, k * dy), rw=2.1, rd=1.1,
                               mau='blue!7', pre=f'bmp{k}', to=True)
            if cat_tuyen:
                # 2 cát tuyến d, d' xuyên 3 mp — các điểm cắt đặt tên
                # d: trái; d': phải. Điểm cắt tại cao 0 của mỗi mp (w = k*dy cộng sẵn qua goc)
                for (nmset, u0, du, nhd, xd) in [
                        (('A', 'B', 'C'), -1.0, 0.25, 'd', -1.4),
                        (("A'", "B'", "C'"), 1.0, -0.2, "d'", 1.5)]:
                    pts = []
                    for k, nm in enumerate(nmset):
                        sx, sy = self._p3(u0 + k * du, 0.2, k * 1.9)
                        self._diem(nm, sx, sy, nhan='left' if xd < 0 else 'right', moc=True)
                        pts.append(nm)
                    self.doan(pts[0], pts[2])   # cát tuyến thẳng
                    bx, by = self.V[pts[0]]     # nhãn d/d' ở ĐẦU DƯỚI (tránh chồng C/C')
                    self.ghi_chu(bx + (0.20 if xd > 0 else -0.30), by - 0.30, _m(nhd))
        else:  # cat — 3 mp qua 1 trục chung (quyển sách)
            specs = [((-2.0, 0.0), 'blue!8', nhan[0]),
                     ((2.0, 0.0), 'green!9', nhan[1]),
                     ((0.0, 1.0), 'orange!8', nhan[2])]
            # trục chung đứng
            self._diem('_trc0', *self._p3(0, 0, -1.2), nhan=None, moc=False)
            self._diem('_trc1', *self._p3(0, 0, 2.2), nhan=None, moc=False)
            for i, ((u, v), mu, lb) in enumerate(specs):
                a = f'_bk{i}a'; b = f'_bk{i}b'
                self._diem(a, *self._p3(u, v, -1.2), nhan=None, moc=False)
                self._diem(b, *self._p3(u, v, 2.2), nhan=None, moc=False)
                self.to_mien('_trc0', '_trc1', b, a, mau=mu)
                self.doan('_trc0', a); self.doan('_trc1', b); self.doan(a, b)
                bx, by = self.V[b]
                self.ghi_chu(bx, by + 0.12, _m(lb))
            self.doan('_trc0', '_trc1', net='lien')   # giao tuyến chung
        return self

    # ═══════════════════ R-3gt · ĐỊNH LÍ BA ĐƯỜNG GIAO TUYẾN ═══════════════════
    def ba_giao_tuyen(self, quan_he='dong_quy', nhan_mp=('(P)', '(Q)', '(R)'),
                      nhan_gt=('a', 'b', 'c'), goc=(0.0, 0.0)):
        """ĐỊNH LÍ BA ĐƯỜNG GIAO TUYẾN (H4.23/H4.24): ba mặt phẳng (P),(Q),(R)
        đôi một cắt nhau theo BA giao tuyến PHÂN BIỆT c=(P)∩(Q), a=(R)∩(P),
        b=(R)∩(Q).
          quan_he='dong_quy'  → ba giao tuyến ĐỒNG QUY tại M (góc tam diện, H4.23).
          quan_he='song_song' → ba giao tuyến ĐÔI MỘT SONG SONG (H4.24).
        nhan_mp: nhãn 3 mp; nhan_gt=(a,b,c): nhãn 3 giao tuyến. Schematic (Đ5.9):
        kho đặt phối cảnh canonical; giao tuyến vẽ ĐẬM, mặt phẳng tô nhạt.
        (Khác ba_mp('cat') = chùm 3 mp qua MỘT trục — chỉ 1 giao tuyến.)"""
        self._nen_luoi = False
        lp, lq, lr = nhan_mp
        la, lb, lc = nhan_gt

        def put(name, u, v, w):
            self._diem(name, *self._p3(u, v, w, goc), nhan=None, moc=False)

        def hbh(q, mau):
            self.to_mien(*q, mau=mau)
            for i in range(4):
                self.doan(q[i], q[(i + 1) % 4], mau='black!38')

        def nhan_tai(u, v, w, s, dx=0.0, dy=0.0, mau=None):
            x, y = self._p3(u, v, w, goc)
            self.ghi_chu(x + dx, y + dy, _m(s), mau=mau)

        if quan_he == 'dong_quy':
            # góc tam diện: đỉnh M, ba giao tuyến là ba cạnh toả từ M
            put('_M', 0.0, 0.0, 0.0)
            put('_Pa', -2.0, -0.15, 0.0)        # a (trên R và P)
            put('_Pb', 2.0, -0.15, 0.0)         # b (trên R và Q)
            put('_Pc', 0.0, 0.35, 2.15)         # c (trên P và Q)
            put('_Xr', 0.0, -1.05, 0.0)         # mũi sàn (R) đổ ra trước
            put('_Xp', -2.0, 0.15, 2.15)        # góc 4 của (P)
            put('_Xq', 2.0, 0.15, 2.15)         # góc 4 của (Q)
            hbh(('_M', '_Pa', '_Xp', '_Pc'), 'blue!7')    # (P)
            hbh(('_M', '_Pb', '_Xq', '_Pc'), 'green!8')   # (Q)
            hbh(('_M', '_Pa', '_Xr', '_Pb'), 'orange!7')  # (R)
            # ba giao tuyến ĐẬM
            self.doan('_M', '_Pa'); self.doan('_M', '_Pb'); self.doan('_M', '_Pc')
            self._diem('M', *self.V['_M'], nhan='above', moc=True)
            nhan_tai(-1.1, -0.08, 0.0, la, dy=0.17)       # a giữa M-Pa
            nhan_tai(1.1, -0.08, 0.0, lb, dy=0.17)        # b giữa M-Pb
            nhan_tai(0.0, 0.18, 1.2, lc, dx=0.14)         # c giữa M-Pc
            nhan_tai(-1.7, 0.12, 1.1, lp, dx=-0.34)       # (P) trong hbh trái
            nhan_tai(1.7, 0.12, 1.1, lq, dx=0.12)         # (Q) trong hbh phải
            nhan_tai(0.0, -0.62, 0.0, lr, dy=-0.04)       # (R) trong sàn (xa M)
        else:  # song_song — ba giao tuyến song song (phương sâu v)
            v0, v1 = -0.75, 1.15
            A = {'u': -1.65, 'w': 0.0}; B = {'u': 1.65, 'w': 0.0}; C = {'u': 0.0, 'w': 1.95}
            for nm, P in [('a', A), ('b', B), ('c', C)]:
                put(f'_{nm}0', P['u'], v0, P['w'])
                put(f'_{nm}1', P['u'], v1, P['w'])
            hbh(('_a0', '_a1', '_c1', '_c0'), 'blue!7')     # (P) chứa a,c
            hbh(('_b0', '_b1', '_c1', '_c0'), 'green!8')    # (Q) chứa b,c
            hbh(('_a0', '_a1', '_b1', '_b0'), 'orange!7')   # (R) chứa a,b
            for nm in ('a', 'b', 'c'):                      # ba giao tuyến ĐẬM //
                self.doan(f'_{nm}0', f'_{nm}1')
            nhan_tai(A['u'], v1, A['w'], la, dx=-0.28, dy=0.02)
            nhan_tai(B['u'], v1, B['w'], lb, dx=0.12, dy=0.02)
            nhan_tai(C['u'], v1, C['w'], lc, dx=0.10, dy=0.10)
            nhan_tai(-0.95, v0, 1.05, lp, dx=-0.26)
            nhan_tai(0.95, v0, 1.05, lq, dx=0.08)
            nhan_tai(0.0, v1, 0.0, lr, dy=-0.22)
        return self

    # ═══════════════════ R-2hbh · HAI HBH CHUNG CẠNH ═══════════════════
    def hai_hbh_chung_canh(self, ten1=('A', 'B', 'C', 'D'),
                           ten2=('A', 'B', 'E', 'F'), goc=(0.0, 0.0)):
        """HAI HÌNH BÌNH HÀNH chung cạnh AB, không đồng phẳng (H4.16/H4.42):
        hbh1 = ten1 (nằm ~ngang), hbh2 = ten2 (dựng ~đứng), chung cạnh đầu (A,B).
        ten1=[A,B,C,D] theo thứ tự chu vi; ten2=[A,B,E,F] chung A,B."""
        self._nen_luoi = False
        A, B, C, D = ten1
        _, _, E, F = ten2
        # hbh1 nằm ngang (nền): A trái-trước, B phải-trước, C phải-sau, D trái-sau
        P = {
            A: self._p3(-1.3, -0.6, 0.0, goc),
            B: self._p3(1.3, -0.6, 0.0, goc),
            C: self._p3(2.0, 1.1, 0.0, goc),
            D: self._p3(-0.6, 1.1, 0.0, goc),
        }
        # hbh2 dựng đứng chung AB: E trên B, F trên A (cao lên)
        ax, ay = P[A]; bx, by = P[B]
        P[E] = (bx + 0.5, by + 2.2)
        P[F] = (ax + 0.5, ay + 2.2)
        posmap = {A: 'below left', B: 'below right', C: 'right', D: 'left',
                  E: 'right', F: 'above left'}
        for nm in (A, B, C, D, E, F):
            self._diem(nm, *P[nm], nhan=posmap[nm], moc=True)
        # hbh1: A-B-C-D ; cạnh DA (sau) có thể khuất
        self.doan(A, B); self.doan(B, C); self.doan(C, D, net='dut'); self.doan(D, A, net='dut')
        # hbh2: A-B-E-F
        self.doan(B, E); self.doan(E, F); self.doan(F, A)
        return self

    # ═══════════════════ R-td · THIẾT DIỆN (helper) ═══════════════════
    def thiet_dien(self, *dinh, mau='cyan!16', net='lien', mau_vien=None):
        """Tô + viền đa giác THIẾT DIỆN theo các đỉnh (tên) đã đặt. Các đỉnh lấy từ
        điểm phụ (trung_diem/diem_giua/giao) đã dựng trên khối. = to_mien + doan khép."""
        if len(dinh) < 3:
            raise ValueError("[thiet_dien] cần ≥ 3 đỉnh")
        self.to_mien(*dinh, mau=mau)
        n = len(dinh)
        for i in range(n):
            self.doan(dinh[i], dinh[(i + 1) % n], net=net, mau=mau_vien)
        return self

    # ═══════════════════ R-chieu · PHÉP CHIẾU SONG SONG ═══════════════════
    def phep_chieu_ss(self, dinh_goc, canh, cao=2.6, phuong=(0.7, -0.35),
                      ten_goc=None, ten_bong=None, goc=(0.0, 0.0),
                      mp_chieu=True, nhan_mp=r'(\alpha)', elip=False):
        """PHÉP CHIẾU SONG SONG: hình GỐC (ở độ cao 'cao') đổ bóng xuống mặt phẳng
        chiếu (sàn, w=0) theo phương chiếu; vẽ tia chiếu đôi một song song.

        dinh_goc : list (u,v) đỉnh hình gốc (trong mặt phẳng ngang ở độ cao 'cao').
        canh     : list cạnh [(i,j),...] nối theo CHỈ SỐ đỉnh (vòng kín nếu đa giác).
        phuong   : (du,dv) độ dời ngang của bóng so với gốc (phương chiếu xiên).
        ten_goc  : list tên đỉnh gốc (vd ['A','B','C','D']); ten_bong tương ứng (["A'",...]).
        mp_chieu : True → vẽ mặt phẳng chiếu (sàn) nhạt.
        elip     : True → hình gốc là đường tròn (vẽ ellipse) thay cho đa giác.
        """
        self._nen_luoi = False
        n = len(dinh_goc)
        tg = ten_goc or [f'_g{i}' for i in range(n)]
        tb = ten_bong or [f"_b{i}" for i in range(n)]
        du, dv = phuong
        # mặt phẳng chiếu (sàn) bao quanh bóng
        if mp_chieu:
            self.mat_phang(nhan=nhan_mp, goc=(goc[0] + du + 0.5, goc[1] - 0.3),
                           rw=2.3, rd=1.3, mau='black!5', pre='mpc', to=True)
        # đỉnh gốc (cao) + bóng (sàn)
        for i, (u, v) in enumerate(dinh_goc):
            self._diem(tg[i], *self._p3(u, v, cao, goc),
                       nhan='above', moc=bool(ten_goc))
            self._diem(tb[i], *self._p3(u + du, v + dv, 0.0, goc),
                       nhan='below', moc=bool(ten_bong))
        # cạnh hình gốc (liền) + cạnh bóng (liền, nhạt)
        for (i, j) in canh:
            self.doan(tg[i], tg[j])
            self.doan(tb[i], tb[j], mau='black!55')
        # tia chiếu // (gốc → bóng), nét mảnh
        for i in range(n):
            self.doan(tg[i], tb[i], net='dut', mau='black!45')
        return self
