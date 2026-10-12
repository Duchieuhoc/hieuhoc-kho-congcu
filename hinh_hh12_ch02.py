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

_GOC_SAU = 40.0
_CO_SAU  = 0.5


class HinhHH12CH02(HinhKhoiHop):
    """Mạch hình không gian tổng hợp lớp 12. Kế thừa khối hộp/lăng trụ + base."""

    # ─────────────────────────────────────────────────────────────
    def tu_dien(self, nhan='ABCD', dinh_tren=None, canh=3.0,
                goc_o=(0.0, 0.0), hien_nhan=True):
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
        return self

    # ─────────────────────────────────────────────────────────────
    def chop(self, day, dinh='S', cao=2.6, ten_day=None,
             goc_o=(0.0, 0.0), hien_nhan=True):
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
