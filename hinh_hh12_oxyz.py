#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh12_oxyz.py — MẠCH HỆ TRỤC TỌA ĐỘ Oxyz (phương pháp tọa độ không gian)
#   cho Hình học 12, Chương II, Bài 7–8 (Hệ trục Oxyz + biểu thức tọa độ).
#   class HinhOxyz(HinhCoBan): hệ trục Oxyz phối cảnh xiên + điểm/vectơ theo
#     TỌA ĐỘ (dữ liệu đề) + hộp chiếu + lưới đơn vị. Nét khuất khai tường minh.
#
#   Triết lý Đ5.9 (diễn giải cho Oxyz — DE_XUAT_CHUAN_PHOI_CANH_OXYZ §3):
#     "Máy giữ tọa độ MÀN HÌNH; người giữ nghĩa — tọa độ TOÁN từ đề."
#     AI/OB truyền tọa độ-toán (x;y;z) LẤY NGUYÊN TỪ NGUỒN (= dữ liệu đề bài,
#     không phải tự chế hình học); máy tự tính phép chiếu xiên ra màn hình.
#     AI KHÔNG tự tính điểm chiếu, không gõ tay vị trí màn hình.
#
#   Phép chiếu (quy ước SGK lớp 12): Oz thẳng-đứng-lên · Oy ngang-phải ·
#     Ox chếch xuống-trái (trục chiều sâu, rút gọn). Affine ⇒ mọi op nhất quán.
#   Căn cứ: DE_XUAT_CHUAN_PHOI_CANH_OXYZ (OB 2026-10-13). CS2627.
# ═══════════════════════════════════════════════════════════════════
import math
from hinh_coban import HinhCoBan
from hinh_khoihop import _hull, _in_poly

# ── phép chiếu xiên Oxyz: trục chiều sâu Ox hướng xuống-trái, rút gọn ──
_K_SAU = 0.62                    # hệ số rút gọn trục Ox (foreshortening)
_GOC_OX = 218.0                  # góc vẽ trục Ox (độ) — xuống-trái, về phía người xem


class HinhOxyz(HinhCoBan):
    """Mạch hệ trục Oxyz lớp 12. Điểm/vectơ đặt theo TỌA ĐỘ (dữ liệu đề), máy chiếu."""

    def __init__(self, scale=1.0, goc=(0.0, 0.0)):
        super().__init__(scale=scale)
        self._goc = goc                 # gốc O trên hệ vẽ
        self._nen_luoi = False          # hình Oxyz: nền sạch (không ô lưới nền 4mm)
        ca = math.cos(math.radians(_GOC_OX)); sa = math.sin(math.radians(_GOC_OX))
        self._ex = (_K_SAU * ca, _K_SAU * sa)   # vector trục Ox (chiều sâu)
        # Oy = (1,0) ngang-phải ; Oz = (0,1) thẳng-đứng-lên

    # ─────────────────────────────────────────────────────────────
    def _P(self, x, y, z):
        """Chiếu điểm TOÁN (x,y,z) → (màn hình). Affine cố định (máy giữ toạ độ màn hình)."""
        ox, oy = self._goc
        ex0, ex1 = self._ex
        return (ox + x * ex0 + y * 1.0 + z * 0.0,
                oy + x * ex1 + y * 0.0 + z * 1.0)

    def _dat(self, ten, x, y, z, nhan=None, moc=False, mau=None):
        """Đặt điểm theo toạ độ toán — lưu toạ độ màn hình đã chiếu vào self.V."""
        sx, sy = self._P(x, y, z)
        self._diem(ten, sx, sy, nhan=nhan, moc=moc, mau=mau)
        return self

    # ─────────────────────────────────────────────────────────────
    def he_truc(self, dai_x=3.2, dai_y=4.2, dai_z=4.2, mp_toado=False,
                vecto_dv=True, O='O', ten_truc=('x', 'y', 'z')):
        """HỆ TRỤC Oxyz: 3 trục đôi một vuông góc (mũi tên + nhãn) + vectơ đơn vị i,j,k.

        dai_x/y/z : độ dài VẼ dương của mỗi trục (đơn vị ô). >0.
        mp_toado  : True → tô nhạt 3 mặt phẳng toạ độ (Oxy),(Oyz),(Ozx) (H.2.35).
        vecto_dv  : True → vẽ 3 vectơ đơn vị i,j,k (bold) trên Ox,Oy,Oz gần gốc.
        ten_truc  : nhãn 3 trục (mặc định x,y,z).
        Máy tự tính phép chiếu — AI không đụng toạ độ màn hình (Đ5.9)."""
        if not (dai_x > 0 and dai_y > 0 and dai_z > 0):
            raise ValueError("[he_truc] dai_x, dai_y, dai_z đều phải > 0")
        tx, ty, tz = ten_truc
        # gốc O
        self._dat(O, 0, 0, 0, nhan='below right', moc=True)
        # tip 3 trục (ẩn chấm) — kéo dài nhẹ cho mũi tên
        self._dat('_Xt', dai_x, 0, 0, nhan=None, moc=False)
        self._dat('_Yt', 0, dai_y, 0, nhan=None, moc=False)
        self._dat('_Zt', 0, 0, dai_z, nhan=None, moc=False)
        # tô mặt phẳng toạ độ (dưới mọi nét)
        if mp_toado:
            for (nm, a, b, c, d, mau) in [
                ('xy', (dai_x, 0, 0), (dai_x, dai_y, 0), (0, dai_y, 0), None, 'blue!7'),
                ('yz', (0, dai_y, 0), (0, dai_y, dai_z), (0, 0, dai_z), None, 'green!8'),
                ('zx', (0, 0, dai_z), (dai_x, 0, dai_z), (dai_x, 0, 0), None, 'orange!8'),
            ]:
                P1 = f'_mp{nm}1'; P2 = f'_mp{nm}2'; P3 = f'_mp{nm}3'
                self._dat(P1, *a, nhan=None, moc=False)
                self._dat(P2, *b, nhan=None, moc=False)
                self._dat(P3, *c, nhan=None, moc=False)
                self.to_mien(O, P1, P2, P3, mau=mau)
        # 3 trục mũi tên (tia có mũi) — thứ tự: Ox (sau), Oy, Oz
        self.tikz.append(('tia', O, '_Xt', True, None, 'lien'))
        self.tikz.append(('tia', O, '_Yt', True, None, 'lien'))
        self.tikz.append(('tia', O, '_Zt', True, None, 'lien'))
        # nhãn trục ở đầu mũi tên (đặt PHÍA TRONG khung để không bị cắt)
        xx, xy = self.V['_Xt']; yx, yy = self.V['_Yt']; zx, zy = self.V['_Zt']
        self.ghi_chu(xx + 0.26, xy + 0.02, tx)     # Ox xuống-trái → nhãn lùi vào phải
        self.ghi_chu(yx + 0.24, yy - 0.08, ty)
        self.ghi_chu(zx + 0.24, zy - 0.02, tz)
        # vectơ đơn vị i, j, k (bold) trên 3 trục, gần gốc + nhãn tường minh
        if vecto_dv:
            self._dat('_i', 1, 0, 0, nhan=None, moc=False)
            self._dat('_j', 0, 1, 0, nhan=None, moc=False)
            self._dat('_k', 0, 0, 1, nhan=None, moc=False)
            self.vecto(O, '_i', nhan=None, mau='red', rong='dam')
            self.vecto(O, '_j', nhan=None, mau='red', rong='dam')
            self.vecto(O, '_k', nhan=None, mau='red', rong='dam')
            ix, iy = self.V['_i']; jx, jy = self.V['_j']; kx, ky = self.V['_k']
            self.ghi_chu(ix - 0.28, iy + 0.04, r'$\vec i$')
            self.ghi_chu(jx + 0.02, jy - 0.30, r'$\vec j$')
            self.ghi_chu(kx - 0.30, ky + 0.02, r'$\vec k$')
        return self

    # ─────────────────────────────────────────────────────────────
    def diem(self, ten, x, y, z, nhan='above right', mau=None, moc=True,
             hop_chieu=False, net_hop='dut', vecto_OM=False, O='O'):
        """ĐẶT ĐIỂM M theo TỌA ĐỘ (x;y;z) — dữ liệu đề; máy chiếu ra màn hình.

        hop_chieu : True → vẽ HÌNH HỘP CHỮ NHẬT chiếu từ O tới M (cạnh ∥ trục) +
                    3 chân chiếu trên trục (H.2.37/2.38). Nét hộp = net_hop ('dut').
        vecto_OM  : True → vẽ vectơ O→M.
        Toạ độ (x;y;z) lấy nguyên từ đề — AI không tính điểm chiếu (Đ5.9)."""
        self._dat(ten, x, y, z, nhan=nhan, moc=moc, mau=mau)
        if hop_chieu:
            # 8 đỉnh hộp O-A-?-B . C-...-M (cạnh song song trục)
            P = {}
            spec = {
                'A': (x, 0, 0), 'B': (0, y, 0), 'Cc': (0, 0, z),
                'xy': (x, y, 0), 'yz': (0, y, z), 'zx': (x, 0, z),
            }
            for nm, (a, b, c) in spec.items():
                pn = f'_{ten}{nm}'
                self._dat(pn, a, b, c, nhan=None, moc=False)
                P[nm] = pn
            # 12 cạnh hộp (nét đứt — hộp phụ trợ đọc toạ độ)
            A, B, Cc = P['A'], P['B'], P['Cc']
            xy, yz, zx = P['xy'], P['yz'], P['zx']
            for u, v in [(O, A), (O, B), (O, Cc),
                         (A, xy), (B, xy), (B, yz), (Cc, yz), (Cc, zx), (A, zx),
                         (xy, ten), (yz, ten), (zx, ten)]:
                self.doan(u, v, net=net_hop)
            # chấm + nhãn 3 chân trên trục
            for pn, lb in [(A, 'above'), (B, 'above'), (Cc, 'left')]:
                self.moc.add(pn)
        if vecto_OM:
            self.vecto(O, ten, nhan=None, mau='blue')
        return self

    # ─────────────────────────────────────────────────────────────
    def luoi_mp(self, nx, ny, nz=0, mau='black!18'):
        """LƯỚI Ô VUÔNG đơn vị trên MẶT PHẲNG (Oxy) (sàn) — nx×ny ô, để đọc toạ độ
        (H.2.38/2.39). nz>0 → thêm vạch dọc đơn vị tại các nút (gợi cao độ). Nét mảnh."""
        # lưới sàn (Oxy): các đường ∥ Oy (chạy theo y) tại x=0..nx, và ∥ Ox tại y=0..ny
        for i in range(nx + 1):
            a = f'_lxa{i}'; b = f'_lxb{i}'
            self._dat(a, i, 0, 0, nhan=None, moc=False)
            self._dat(b, i, ny, 0, nhan=None, moc=False)
            self.doan(a, b, mau=mau)
        for j in range(ny + 1):
            a = f'_lya{j}'; b = f'_lyb{j}'
            self._dat(a, 0, j, 0, nhan=None, moc=False)
            self._dat(b, nx, j, 0, nhan=None, moc=False)
            self.doan(a, b, mau=mau)
        return self

    # ─────────────────────────────────────────────────────────────
    def khoi_hop_oxyz(self, a, b, c, goc=(0.0, 0.0, 0.0), ten_dinh=None,
                      nhan=None, net_khuat='dut', hien_dinh=True):
        """KHỐI HỘP CHỮ NHẬT đặt trong Oxyz, cạnh song song 3 trục (nét khuất tự tính).

        a,b,c   : kích thước theo Ox, Oy, Oz (độ dài VẼ = đơn vị đề). >0.
        goc     : toạ độ (x0,y0,z0) của ĐỈNH gốc khối (mặc định ≡ O).
        ten_dinh: 8 tên đỉnh theo thứ tự [đáy: g, +x, +x+y, +y ; nắp: +z, +x+z, +x+y+z, +y+z].
                  Vd hộp ABCD.A'B'C'D' với A≡gốc: ['A','B','C','D','A','B','C','D'] + "'".
                  Gọn hơn: truyền list 8 tên tường minh.
        nhan    : dict {đỉnh_tên: vị_trí_nhãn} tuỳ chọn ghi đè vị trí nhãn.
        Máy tự tính 8 đỉnh chiếu + nét khuất (đỉnh nằm trong bao lồi = khuất). Đ5.9."""
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError("[khoi_hop_oxyz] a, b, c đều phải > 0")
        x0, y0, z0 = goc
        # 8 đỉnh theo toạ độ (thứ tự chuẩn)
        corners = [
            (x0,     y0,     z0),      # 0 gốc
            (x0 + a, y0,     z0),      # 1 +x
            (x0 + a, y0 + b, z0),      # 2 +x+y
            (x0,     y0 + b, z0),      # 3 +y
            (x0,     y0,     z0 + c),  # 4 +z
            (x0 + a, y0,     z0 + c),  # 5 +x+z
            (x0 + a, y0 + b, z0 + c),  # 6 +x+y+z
            (x0,     y0 + b, z0 + c),  # 7 +y+z
        ]
        if ten_dinh is None:
            ten_dinh = [f'_K{i}' for i in range(8)]
        if len(ten_dinh) != 8:
            raise ValueError("[khoi_hop_oxyz] ten_dinh cần đúng 8 tên")
        proj = [self._P(*cc) for cc in corners]
        hull = _hull(proj)
        khuat = [(round(proj[i][0], 4), round(proj[i][1], 4)) not in hull for i in range(8)]
        # vị trí nhãn mặc định (đẩy ra ngoài tâm khối)
        cx = sum(p[0] for p in proj) / 8; cy = sum(p[1] for p in proj) / 8
        nhan = nhan or {}
        for i, (cc, nm) in enumerate(zip(corners, ten_dinh)):
            px, py = proj[i]
            if nm in nhan:
                pos = nhan[nm]
            else:
                dx, dy = px - cx, py - cy
                if abs(dx) >= abs(dy):
                    pos = 'right' if dx >= 0 else 'left'
                else:
                    pos = 'above' if dy >= 0 else 'below'
            self._diem(nm, px, py, nhan=(pos if hien_dinh else None), moc=hien_dinh)
        # 12 cạnh: đáy(0-1-2-3), nắp(4-5-6-7), trụ(0-4,1-5,2-6,3-7)
        E = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]
        for u, v in E:
            net = net_khuat if (khuat[u] or khuat[v]) else 'lien'
            self.doan(ten_dinh[u], ten_dinh[v], net=net)
        return self

    # ─────────────────────────────────────────────────────────────
    def khoi_tu_dinh(self, dinh, canh, mat=None, to_mat=None, net_khuat='dut',
                     hien_dinh=True, mau_dinh=None):
        """KHỐI TỔNG QUÁT trong Oxyz từ TOẠ ĐỘ ĐỈNH (đề cho) + CẠNH (+ MẶT) —
        tự tính nét khuất. Dùng cho chóp/lăng trụ/khối 'thả' có nhãn toạ độ.

        dinh : dict {ten_đỉnh: (x,y,z)} — toạ độ TOÁN lấy từ đề (Đ5.9).
        canh : list [(u,v), …] các cạnh nối theo tên đỉnh.
        mat  : list các MẶT [(t1,t2,t3,…), …] — dùng TÍNH NÉT KHUẤT (che theo mặt).
               Nên khai đủ các mặt của khối đặc; thiếu mat → lùi heuristic bao lồi.
        to_mat : list mặt cần TÔ nhạt (tuỳ chọn) — nằm dưới nét.
        Nét khuất (có mat): cạnh bị CHE nếu trung điểm chiếu của nó nằm trong hình
          chiếu một mặt KHÁC ở GẦN người xem hơn (trục Ox hướng về người xem ⇒ x lớn
          = gần). Máy tự tính — AI chỉ cấp toạ độ đề + quan hệ cạnh/mặt (Đ5.9)."""
        names = list(dinh.keys())
        proj = {nm: self._P(*dinh[nm]) for nm in names}
        cx = sum(p[0] for p in proj.values()) / len(proj)
        cy = sum(p[1] for p in proj.values()) / len(proj)
        # tô mặt (dưới nét)
        for mt in (to_mat or []):
            self.to_mien(*mt, mau='cyan!12')
        # đặt đỉnh + nhãn đẩy ra ngoài tâm
        for nm in names:
            px, py = proj[nm]
            dx, dy = px - cx, py - cy
            if abs(dx) >= abs(dy):
                pos = 'right' if dx >= 0 else 'left'
            else:
                pos = 'above' if dy >= 0 else 'below'
            self._diem(nm, px, py, nhan=(pos if hien_dinh else None),
                       moc=hien_dinh, mau=mau_dinh)

        # ── tính khuất ──
        def _canh_khuat(u, v):
            if not mat:          # lùi: heuristic bao lồi (đỉnh nội = khuất)
                hull = _hull(list(proj.values()))
                ku = (round(proj[u][0], 4), round(proj[u][1], 4)) not in hull
                kv = (round(proj[v][0], 4), round(proj[v][1], 4)) not in hull
                return ku or kv
            # che theo mặt: trung điểm 3D của cạnh
            mx = (dinh[u][0] + dinh[v][0]) / 2
            my = (dinh[u][1] + dinh[v][1]) / 2
            mz = (dinh[u][2] + dinh[v][2]) / 2
            pm = self._P(mx, my, mz)
            depth_m = mx                       # x = độ sâu về phía người xem (Ox hướng tới)
            for f in mat:
                if u in f and v in f:
                    continue                   # cạnh thuộc mặt này → không tự che
                depth_f = sum(dinh[t][0] for t in f) / len(f)
                if depth_f <= depth_m + 1e-6:
                    continue                   # mặt KHÔNG gần hơn → không che
                poly = [proj[t] for t in f]
                if _in_poly(pm, poly):
                    return True
            return False

        for u, v in canh:
            self.doan(u, v, net=(net_khuat if _canh_khuat(u, v) else 'lien'))
        return self

    # ─────────────────────────────────────────────────────────────
    def nhan_toado(self, ten, x, y, z, nhan='above right', mau=None, moc=True):
        """Đặt + GHI NHÃN TOẠ ĐỘ cho đỉnh (khối 'thả' trong Oxyz — H.2.42).
        Toạ độ lấy từ đề; máy chiếu. Nhãn hiện tên đỉnh; toạ độ ghi kèm nếu cần ngoài."""
        self._dat(ten, x, y, z, nhan=nhan, moc=moc, mau=mau)
        return self

    # ─────────────────────────────────────────────────────────────
    def doan_oxyz(self, A, B, net='lien', mau=None):
        """Nối 2 điểm Oxyz đã đặt (tên) — tiện ích; = doan base."""
        self.doan(A, B, net=net, mau=mau)
        return self
