#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_gocdt.py — MẠCH "GÓC & ĐƯỜNG THẲNG" (hai đường cắt nhau · cát tuyến cắt hai đường)
#   Class HinhGocDT(HinhCoBan): gói 2 mô-típ xương sống của hình học góc–đường thẳng
#   (đối đỉnh/kề bù · so le trong/đồng vị/trong cùng phía). Dùng CHUNG lớp 7→9.
#   Kế thừa toàn bộ primitive + PHANH + ve() của HinhCoBan (không đụng file lõi).
#   ĐÁNH SỐ GÓC theo QUY ƯỚC PHẦN TƯ trục toạ độ: I=1 (trên-phải) · II=2 (trên-trái)
#   · III=3 (dưới-trái) · IV=4 (dưới-phải) — ngược chiều kim đồng hồ. Chuẩn SGK KNTT.
# CS2627. Tạo 2026-08-22 (Ông Bụt) cho HH7 Chương III, kế thừa cho các chương sau.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_dagiac
from hinh_dagiac import HinhDaGiac


class Hinh(HinhDaGiac):
    """Mạch góc & đường thẳng. Kế thừa HinhDaGiac (⊃ HinhCoBan) → có sẵn cả
       tam_giac/tu_giac/đa giác lẫn primitive điểm·đường·tia·góc. Hai hàm dựng chuyên:
       • hai_duong_cat_4goc  — hai đường thẳng cắt nhau tại 1 đỉnh, đánh số 4 góc.
       • cat_tuyen_2duong    — một cát tuyến cắt hai đường thẳng (song song hoặc cắt),
                               đánh số 4 góc tại mỗi đỉnh (A1–A4, B1–B4).
       • nhan_goc            — ghi nhãn số/ký hiệu (1,2,3…) tại phân giác trong 1 góc."""

    # ── nội bộ: tách tên đường thành nhãn 2 đầu ──
    #    "xx′"→['x',"x'"] · "yy′"→['y',"y'"] · "mn"→['m','n'] · "a"→['a'] (1 nhãn)
    @staticmethod
    def _tach_ten(ten):
        t = ten.replace('′', "'")
        # [VÁ 22/08f] tên 2 gốc ĐỀU prime: "x′y′" → ['x′','y′'] (H3.21/H3.23: xy // x′y′; góc ABy′)
        if len(t) == 4 and t[1] == "'" and t[3] == "'" and t[0].isalpha() and t[2].isalpha():
            return [t[0] + '′', t[2] + '′']
        if t.endswith("'") and len(t) >= 3:
            return [t[0], t[1:-1] + '′']   # gốc, gốc+prime (dùng ′ U+2032 khớp SGK, không apostrophe)
        if len(t) == 2 and not t.endswith("'") and t[1] not in ("'", '″'):
            return [t[0], t[1]]         # hai chữ khác nhau (mn, pq)
        return [t]                       # tên 1 phần (a, b, c, d″, x″…) — ″ gắn vào gốc

    # ── nội bộ: đặt nhãn tên đường ở 2 ĐẦU theo quy ước, RA NGOÀI đầu nét (không bị đường cắt) ──
    #    gốc (không prime) ở đầu TRÁI (đường ngang) / TRÊN (đường dọc);
    #    phần sau ở đầu PHẢI / DƯỚI. Tên 1 phần → 1 nhãn ở đầu dương.
    def _dat_nhan(self, txt, mut, tam, ra=1.18):
        """Đặt nhãn 'txt' ngoài mút 'mut' (theo hướng tam→mut), qua khỏi đoạn nét kéo dài."""
        mx, my = self.V[mut]; tx, ty = self.V[tam]
        dx, dy = mx - tx, my - ty; Ln = math.hypot(dx, dy) or 1
        ux, uy = dx / Ln, dy / Ln
        # nhãn = điểm ẩn (không chấm) mang KEY = txt, căn giữa tại vị trí ngoài nét
        self._diem(txt, mx + ux * ra, my + uy * ra, nhan='', moc=False)

    def _nhan_ten_duong(self, ten, e0, e1, tam, theta):
        parts = self._tach_ten(ten)
        if len(parts) == 1:
            self._dat_nhan(parts[0], e1, tam); return
        ngang = abs(math.cos(math.radians(theta))) >= abs(math.sin(math.radians(theta)))
        x0, y0 = self.V[e0]; x1, y1 = self.V[e1]
        if ngang:
            goc_mut = e0 if x0 < x1 else e1     # đầu trái = phần gốc
        else:
            goc_mut = e0 if y0 > y1 else e1     # đầu trên = phần gốc
        kia_mut = e1 if goc_mut == e0 else e0
        self._dat_nhan(parts[0], goc_mut, tam)
        self._dat_nhan(parts[1], kia_mut, tam)

    # ── nội bộ: vẽ 1 đường thẳng qua điểm 'O' theo góc 'theta' (độ) — NÉT THẲNG, KHÔNG mũi tên ──
    def _duong_qua_diem(self, ten, O, theta, dai=2.7, nhan_ten=True, mau=None, net='lien',
                        ti_duong=1.0, ti_am=1.0):
        # ti_duong: hệ số dài NHÁNH DƯƠNG (đầu e1, theo +theta); ti_am: nhánh ÂM (đầu e0).
        # Mặc định 1.0/1.0 = đối xứng như cũ. Rút 1 nhánh để bớt phần thò thừa (VD cát tuyến).
        Ox, Oy = self.V[O]
        a = math.radians(theta); dx, dy = math.cos(a), math.sin(a)
        dd, da = dai * ti_duong, dai * ti_am
        e0, e1 = f'_{ten}A', f'_{ten}B'
        self._diem(e0, Ox - dx * da, Oy - dy * da, nhan=None, moc=False)
        self._diem(e1, Ox + dx * dd, Oy + dy * dd, nhan=None, moc=False)
        self.tikz.append(('duong', e0, e1, mau, net))     # đường thẳng: 2 đầu KHÔNG mũi tên
        if nhan_ten:
            self._nhan_ten_duong(ten, e0, e1, O, theta)
        self.duong_data[ten] = (e0, e1)
        return e0, e1

    # ── nội bộ: đánh số 4 góc quanh đỉnh 'O' tạo bởi 2 hướng th1, th2 (độ) ──
    #    Gán số theo PHẦN TƯ mà tia phân giác của mỗi vùng rơi vào (I→1 … IV→4).
    def _so_4goc(self, O, th1, th2, r=0.60, prefix='', font=None):
        Ox, Oy = self.V[O]
        dirs = sorted(t % 360 for t in (th1, th2, th1 + 180, th2 + 180))
        for i in range(4):
            a = dirs[i]; b = dirs[(i + 1) % 4]
            if b <= a:
                b += 360
            mid = ((a + b) / 2) % 360
            quad = int(mid // 90)            # 0..3 → phần tư I..IV
            so = quad + 1                    # I→1, II→2, III→3, IV→4
            mr = math.radians(mid)
            x = Ox + r * math.cos(mr); y = Oy + r * math.sin(mr)
            self.tikz.append(('so_o', x, y, f'{prefix}{so}'))
        return self

    # ═══════════════════════════════════════════════════════════════
    # NHÃN SỐ THỨ TỰ GÓC (Ô₁, Ô₂, Ô₃…) — cho Tập suy luận / hình đối đỉnh đánh số riêng
    # ═══════════════════════════════════════════════════════════════
    def nhan_goc(self, goc, chu, r=0.44):
        """Ghi nhãn 'chu' (số thứ tự '1','2','3'… hoặc ký hiệu) tại phân giác TRONG của góc.
        goc = (canh1, dinh, canh2): tên 3 điểm ĐÃ đặt (qua tia/tia_doi…). Dùng cho các hình
        đánh số góc KHÔNG theo phần tư liên tục (vd H3.5: Ô₁–Ô₂ đối đỉnh). Không vẽ cung."""
        A, O, B = goc
        ox, oy = self.V[O]; ax, ay = self.V[A]; bx, by = self.V[B]
        a1 = math.atan2(ay - oy, ax - ox)
        a2 = math.atan2(by - oy, bx - ox)
        da = (a2 - a1) % (2 * math.pi)
        mid = a1 + da / 2 if da <= math.pi else a1 - (2 * math.pi - da) / 2   # phân giác trong
        x = ox + r * math.cos(mid); y = oy + r * math.sin(mid)
        self.tikz.append(('so_o', x, y, chu))
        return self

    def dau_goc_bang(self, goc, so_gach=1, ban_kinh=7, mau='orange', do=None):
        """Đánh dấu GÓC (cung + 'so_gach' gạch tick) → thể hiện HAI GÓC BẰNG NHAU.
        Các góc bằng nhau (vd 2 nửa của góc bị tia phân giác chia) dùng CÙNG so_gach.
        goc = (canh1, dinh, canh2) đã đặt. do: số đo thật (None → tự tính từ toạ độ). PHANH kiểm."""
        A, O, B = goc
        ox, oy = self.V[O]; ax, ay = self.V[A]; bx, by = self.V[B]
        a1 = math.atan2(ay - oy, ax - ox); a2 = math.atan2(by - oy, bx - ox)
        d = (a2 - a1) % (2 * math.pi)
        do_thuc = do if do is not None else round(math.degrees(d if d <= math.pi else 2 * math.pi - d), 4)
        self.so_do_goc(goc, do_thuc, hien_so=False, mau=mau, ban_kinh=ban_kinh)   # cung (PHANH kiểm)
        mid = a1 + d / 2 if d <= math.pi else a1 - (2 * math.pi - d) / 2           # phân giác trong
        R = ban_kinh / 10.0
        spread = math.radians(7)
        base = -(so_gach - 1) / 2.0
        for i in range(so_gach):
            ang = mid + (base + i) * spread
            ux, uy = math.cos(ang), math.sin(ang)
            t1, t2 = f'_gb{O}{A}{B}{i}a', f'_gb{O}{A}{B}{i}b'
            self._diem(t1, ox + (R - 0.09) * ux, oy + (R - 0.09) * uy, nhan=None, moc=False)
            self._diem(t2, ox + (R + 0.09) * ux, oy + (R + 0.09) * uy, nhan=None, moc=False)
            self.tikz.append(('doan', t1, t2, mau))
        return self

    # ═══════════════════════════════════════════════════════════════
    # MÔ-TÍP 1 — HAI ĐƯỜNG THẲNG CẮT NHAU (đối đỉnh · kề bù)
    # ═══════════════════════════════════════════════════════════════
    def hai_duong_cat_4goc(self, ten1='xx′', ten2='yy′', O='O',
                           xoay1=10, xoay2=105, danh_so=True,
                           nhan_dinh=True, prefix='', dai=2.2):
        """Hai đường thẳng ten1, ten2 cắt nhau tại đỉnh O.
        xoay1/xoay2: góc nghiêng (độ) của mỗi đường so phương ngang.
        danh_so=True → đánh số 4 góc theo phần tư I–IV (prefix để ghi 'O' nếu cần).
        PHANH: O ∈ cả hai đường (buộc 2 đường thực sự cắt tại O)."""
        if O not in self.V:
            self._diem(O, 0, 0, nhan=('below left' if nhan_dinh else None), moc=nhan_dinh)
        a1 = self._duong_qua_diem(ten1, O, xoay1, dai=dai)
        a2 = self._duong_qua_diem(ten2, O, xoay2, dai=dai)
        self.rb.append({'loai': 'diem_tren_duong', 'diem': O, 'qua': a1})
        self.rb.append({'loai': 'diem_tren_duong', 'diem': O, 'qua': a2})
        if danh_so:
            self._so_4goc(O, xoay1, xoay2, prefix=prefix)
        return self

    # ═══════════════════════════════════════════════════════════════
    # MÔ-TÍP 2 — CÁT TUYẾN CẮT HAI ĐƯỜNG THẲNG (so le trong · đồng vị · trong cùng phía)
    # ═══════════════════════════════════════════════════════════════
    def cat_tuyen_2duong(self, a='a', b='b', c='c', A='A', B='B',
                         song_song=True, xoay_ab=8, xoay_c=108,
                         khoang=1.9, danh_so=True, nhan_dinh=True,
                         danh_dau_ss=False, rut_c_tren=0.5, dai=2.2):
        """Cát tuyến c cắt đường a (trên) tại A và đường b (dưới) tại B.
        song_song=True → a // b (PHANH kiểm). xoay_ab: nghiêng chung a,b; xoay_c: nghiêng c.
        khoang: khoảng dọc giữa a và b. danh_so → A1–A4 tại A, B1–B4 tại B (phần tư).
        danh_dau_ss: mặc định TẮT (đường thẳng không đặt dấu trên đường); bật khi bài cần
        nhấn ký hiệu song song.
        rut_c_tren: tỉ lệ GIỮ LẠI của nhánh cát tuyến c PHÍA TRÊN A (mặc định 0.5 = cắt bỏ nửa
        phần thò lên trên A cho gọn; đặt 1.0 để giữ nhánh trên dài như nhánh dưới)."""
        # đỉnh A trên đường a (đặt gốc), B trên đường b — cùng nằm trên c
        self._diem(A, 0.0, khoang / 2, nhan=('above left' if nhan_dinh else None), moc=nhan_dinh)
        # B = giao của c với đường b: đi từ A theo hướng c xuống dưới quãng đủ để hạ 'khoang'
        ac = math.radians(xoay_c)
        # số bước theo c để tụt đúng 'khoang' theo phương dọc
        t = khoang / max(abs(math.sin(ac)), 1e-6)
        Bx = 0.0 - math.cos(ac) * t
        By = khoang / 2 - math.sin(ac) * t
        self._diem(B, Bx, By, nhan=('below left' if nhan_dinh else None), moc=nhan_dinh)
        # đường a qua A, đường b qua B — cùng nghiêng xoay_ab
        ea = self._duong_qua_diem(a, A, xoay_ab, dai=dai)
        eb = self._duong_qua_diem(b, B, xoay_ab, dai=dai)
        # cát tuyến c qua A và B (nhãn ở đầu trên). Rút nhánh PHÍA TRÊN A cho gọn:
        # nhánh dương (e1 = A + hướng) hướng lên khi sin(xoay_c) > 0 → rút đầu dương; ngược lại rút đầu âm.
        # cát tuyến c qua A và B: nhánh QUA B phải đủ dài để CHẠM B rồi thò lề đặt nhãn z′
        # (khoảng A→B dọc theo c = khoang/|sin(xoay_c)| — nghiêng càng nhiều càng dài).
        # Nhánh TRÊN A rút gọn theo rut_c_tren. Sửa 22h: trước đây để dai cố định → nghiêng
        # nhiều thì vẽ hụt, chưa tới B (lỗi H3.35 khoang lớn/góc thoải).
        t_AB = khoang / max(abs(math.sin(math.radians(xoay_c))), 1e-6)
        len_qua_B = t_AB + 0.7                  # chạm B rồi thò 0.7 đặt nhãn z′
        len_tren  = 0.55 + 0.9 * rut_c_tren     # nhánh phía trên A (gọn)
        if math.sin(math.radians(xoay_c)) >= 0:       # +theta hướng LÊN  → trên A = ti_duong
            ec = self._duong_qua_diem(c, A, xoay_c, dai=1.0, ti_duong=len_tren, ti_am=len_qua_B)
        else:                                         # +theta hướng XUỐNG → qua B = ti_duong
            ec = self._duong_qua_diem(c, A, xoay_c, dai=1.0, ti_duong=len_qua_B, ti_am=len_tren)
        # ── ràng buộc PHANH ──
        self.rb.append({'loai': 'diem_tren_duong', 'diem': A, 'qua': ea})
        self.rb.append({'loai': 'diem_tren_duong', 'diem': B, 'qua': eb})
        self.rb.append({'loai': 'diem_tren_duong', 'diem': A, 'qua': ec})
        self.rb.append({'loai': 'diem_tren_duong', 'diem': B, 'qua': ec})
        self.rb.append({'loai': 'thang_hang', 'diem': [A, B]})
        if song_song:
            self.rb.append({'loai': 'song_song', 'doan1': ea, 'doan2': eb})
            if danh_dau_ss:
                # đặt dấu // trên NỬA đoạn (đỉnh → đầu dương) để không trùng giao điểm
                self.tikz.append(('dau_ss', A, ea[1], 1))
                self.tikz.append(('dau_ss', B, eb[1], 1))
        if danh_so:
            self._so_4goc(A, xoay_ab, xoay_c, prefix='', r=0.66)
            self._so_4goc(B, xoay_ab, xoay_c, prefix='', r=0.66)
        return self
