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
