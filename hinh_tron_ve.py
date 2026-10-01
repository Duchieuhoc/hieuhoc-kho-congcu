#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_tron_ve.py — MẠCH "ĐƯỜNG TRÒN" (semantic — hàm khai nghĩa)
#   Kế thừa HinhCoBan (dùng chung ve()/PHANH/style 2D). Xây 15/08/2026.
#   L6 DÙNG THẬT: đồng hồ (ghép primitive), vòng quay, compa (8.10).
#   Chữ ký MỞ để L9 kế thừa + thêm ràng buộc (dây·tiếp tuyến·góc nội tiếp — MO_HINH §3).
#   Nạp gói luật `hinh_tron` ở đầu → luật PHANH đường tròn sẵn sàng.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_coban
import hinh_tron          # nạp gói luật (tự đăng ký 'diem_tren_tron','goc_o_tam')

# Hướng nhãn 12 số mặt đồng hồ (hạ tầng — prefix _, cửa quét bỏ qua): số toả RA NGOÀI vành.
_NHAN_DONGHO = {12:'above',    1:'above right', 2:'right',      3:'right',
                4:'right',     5:'below right', 6:'below',      7:'below left',
                8:'left',      9:'left',        10:'left',      11:'above left'}

class HinhTron(hinh_coban.HinhCoBan):
    def duong_tron(self, tam, ban_kinh=2.0, mau=None, net='lien', hien_tam=True):
        """ĐƯỜNG TRÒN tâm 'tam', bán kính 'ban_kinh' (đơn vị vẽ). Nếu 'tam' chưa đặt →
        đặt tại gốc (0,0) — KHÔNG nhận tọa độ (Đ5.9). hien_tam=False → không chấm tâm.
        Các điểm trên đường tròn khai bằng diem_tren_tron (định vị bằng GÓC Ở TÂM)."""
        if tam not in self.V:
            self._diem(tam, 0.0, 0.0, 'below' if hien_tam else None, moc=hien_tam)
        elif not hien_tam:
            self.moc.discard(tam); self.nhan[tam] = None
        self.tron[tam] = float(ban_kinh)
        self.tikz.append(('tron', tam, float(ban_kinh), mau, net))
        return self

    def duong_tron_qua(self, tam, qua, mau=None, net='lien', hien_tam=True):
        """ĐƯỜNG TRÒN tâm 'tam' đi QUA điểm 'qua' (cả hai ĐÃ đặt). Bán kính = |tam→qua|,
        máy tự tính — KHÔNG cho số (Đ5.9). Dùng vẽ ĐƯỜNG TRÒN NGOẠI TIẾP (tâm O cách đều
        3 đỉnh: duong_tron_qua(O, A) → tự đi qua B, C nếu OA=OB=OC) hoặc nội tiếp
        (tâm I, qua chân vuông góc). PHANH kiểm 'qua' nằm trên đường tròn."""
        import math as _m
        if tam not in self.V:
            raise ValueError(f"duong_tron_qua: chưa đặt tâm '{tam}'.")
        if qua not in self.V:
            raise ValueError(f"duong_tron_qua: chưa đặt điểm 'qua'='{qua}'.")
        (ox, oy) = self.V[tam]; (qx, qy) = self.V[qua]
        r = _m.hypot(qx - ox, qy - oy)
        if not hien_tam:
            self.moc.discard(tam); self.nhan[tam] = None
        self.tron[tam] = r
        self.tikz.append(('tron', tam, r, mau, net))
        self.rb.append({'loai': 'diem_tren_tron', 'diem': qua, 'tam': tam, 'ban_kinh': r})
        return self

    def diem_tren_tron(self, ten, tam, goc_o_tam, nhan='above right', mau=None):
        """Điểm 'ten' NẰM TRÊN đường tròn tâm 'tam', định vị bằng GÓC Ở TÂM 'goc_o_tam'
        (độ, đo ngược chiều kim đồng hồ từ hướng ngang) — KHÔNG tọa độ. PHANH kiểm
        khoảng cách tới tâm = bán kính. mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        if tam not in self.tron:
            raise ValueError(f"diem_tren_tron: chưa khai đường tròn tâm '{tam}' "
                             f"(gọi duong_tron trước).")
        r = self.tron[tam]; ox, oy = self.V[tam]
        a = math.radians(goc_o_tam)
        self._diem(ten, ox + r*math.cos(a), oy + r*math.sin(a), nhan, moc=True, mau=mau)
        self.rb.append({'loai':'diem_tren_tron','diem':ten,'tam':tam,'ban_kinh':r})
        return self

    def diem_ban_kinh(self, ten, tam, goc, ban_kinh, nhan='above right', mau=None, hien=True):
        """Điểm 'ten' cách tâm 'tam' đúng 'ban_kinh' (đơn vị vẽ) theo hướng 'goc' (độ, ngược
        chiều kim từ ngang) — KHÔNG tọa độ. Dùng đặt mút hướng-tâm: KIM đồng hồ (kim giờ
        bán_kinh nhỏ = ngắn, kim phút lớn = dài), nan quạt, mốc trên bán kính. hien=False →
        không chấm/không nhãn (chỉ làm mút để nối kim)."""
        if tam not in self.V:
            self._diem(tam, 0.0, 0.0, 'below', moc=hien)
        ox, oy = self.V[tam]; a = math.radians(goc)
        self._diem(ten, ox + ban_kinh*math.cos(a), oy + ban_kinh*math.sin(a),
                   nhan if hien else None, moc=hien, mau=mau)
        return self

    def so_quanh_tam(self, tam, ban_kinh, danh_sach, goc_dau=90, chieu=-1):
        """Rải các nhãn 'danh_sach' ĐỀU quanh tâm 'tam' trên vòng bán kính 'ban_kinh',
        bắt đầu ở hướng 'goc_dau'° (mặc định 90 = trên đỉnh), bước 'chieu'*360/n (chieu=-1
        = thuận chiều kim). Dùng ghi SỐ 1–12 mặt đồng hồ, mặt số công-tơ-mét, xúc xắc quanh."""
        if tam not in self.V:
            self._diem(tam, 0.0, 0.0, 'below', moc=True)
        ox, oy = self.V[tam]; n = len(danh_sach); buoc = 360.0/n
        for i, nhan in enumerate(danh_sach):
            a = math.radians(goc_dau + chieu*i*buoc)
            self.tikz.append(('so_o', ox + ban_kinh*math.cos(a), oy + ban_kinh*math.sin(a), str(nhan)))
        return self

    def cung(self, tam, goc_dau, goc_cuoi, mau='red', net='lien', ban_kinh=None):
        """CUNG của đường tròn tâm 'tam', quét từ 'goc_dau' đến 'goc_cuoi' (độ, góc ở tâm).
        Mặc định đỏ (yếu tố nhấn ở lời giải). Dùng đánh dấu 1 phần đường tròn / cung tròn.
        ban_kinh=None → lấy bán kính đường tròn ĐÃ khai (cần duong_tron trước).
        ban_kinh=<số> → vẽ CHỈ CUNG bán kính đó, KHÔNG cần vẽ trọn đường tròn."""
        if ban_kinh is not None:
            r = float(ban_kinh)
        else:
            if tam not in self.tron:
                raise ValueError(f"cung: chưa khai đường tròn tâm '{tam}' (hoặc truyền ban_kinh=).")
            r = self.tron[tam]
        self.tikz.append(('cung', tam, r, float(goc_dau), float(goc_cuoi), mau, net))
        return self

    def cung_qua(self, tam, qua, ban_kinh=None, mo=28, mau='black', net='dut'):
        """Vẽ CUNG NGẮN của đường tròn tâm 'tam' ĐI QUA điểm 'qua' — đánh dấu chỗ giao compa,
        KHÔNG vẽ trọn đường tròn. Bán kính = ban_kinh (nếu cho) hoặc |tam→qua|; quét ±'mo'°
        quanh hướng tâm→qua. Dựng tam giác/điểm bằng compa: cung_qua(B,A)+cung_qua(C,A) cắt tại A."""
        if tam not in self.V or qua not in self.V:
            raise ValueError(f"cung_qua: cần đặt trước tâm '{tam}' và điểm '{qua}'.")
        ox, oy = self.V[tam]; qx, qy = self.V[qua]
        r = float(ban_kinh) if ban_kinh is not None else math.hypot(qx - ox, qy - oy)
        ang = math.degrees(math.atan2(qy - oy, qx - ox))
        self.tikz.append(('cung', tam, r, ang - mo, ang + mo, mau, net))
        return self

    def goc_o_tam(self, tam, A, B, do=None, danh_dau=True):
        """Góc ở tâm chắn bởi 2 bán kính 'tam'A, 'tam'B (A,B đã đặt trên đường tròn).
        Vẽ 2 bán kính + đánh dấu cung góc. do=số đo → PHANH kiểm góc ở tâm đúng số đo.
        (Nền cho L9: góc nội tiếp = ½ góc ở tâm.)"""
        self.tikz.append(('doan', tam, A, None, 'lien'))
        self.tikz.append(('doan', tam, B, None, 'lien'))
        if do is not None:
            self.rb.append({'loai':'goc_o_tam','tam':tam,'ban_kinh_2':(A,B),'do':do})
        if danh_dau:
            self.tikz.append(('goc', [A, tam, B], do, do is not None))
        return self

    def kim(self, R, vi_tri, loai='gio', tam='O'):
        """Vẽ MỘT kim đồng hồ từ tâm 'tam' ra hướng 'vi_tri' (thang 12 giờ, cho phép LẺ:
        vd 3.5 = giữa số 3 và 4). Tham số 'loai' chọn kiểu kim:
          · 'gio'  → kim GIỜ  ngắn + đậm  (R*0.52, đen)
          · 'phut' → kim PHÚT dài + mảnh  (R*0.86, đen)
          · 'giay' → kim GIÂY dài nhất + mảnh + ĐỎ (R*0.92, red)   [thêm 25/08 — bài thật Hình 5]
        Mút kim là điểm ẩn (hien=False, không nhãn). Thường gọi qua mat_dong_ho(); tách phơi
        để dựng kim lẻ. Phân biệt các kim = ĐỘ DÀI + BỀ DÀY (+ MÀU cho giây) — chuẩn hoá tại
        đây để mọi bài đồng hồ ra ĐỒNG NHẤT, AI Soạn KHÔNG tự ghép primitive. KHÔNG đặt tên
        mút, KHÔNG cung góc."""
        _CHUAN = {                       # loai → (tên_mút_ẩn, tỉ_lệ_R, bề_dày, màu)
            'gio':  ('_kimG', 0.52, 'dam',  None),
            'phut': ('_kimP', 0.86, 'manh', None),
            'giay': ('_kimS', 0.92, 'manh', 'red'),
        }
        if loai not in _CHUAN:
            raise ValueError(f"kim: loai='{loai}' không hợp lệ — chọn 'gio' | 'phut' | 'giay'.")
        ten, ti_le, rong, mau = _CHUAN[loai]
        goc = 90 - 30*vi_tri
        self.diem_ban_kinh(ten, tam, goc, R*ti_le, hien=False)
        self.doan(tam, ten, mau=mau, rong=rong)
        return self

    def mat_dong_ho(self, gio=None, phut=0, giay=None, R=2.4, tam='O'):
        """ĐỒNG HỒ chuẩn HH6 — MỘT hàm ra đồng hồ hoàn chỉnh: vành tròn tâm 'tam' + 12 số
        (đặt bằng diem_tren_tron, nhãn toả ra ngoài) + tuỳ chọn các kim.
          · gio=None              → chỉ vẽ MẶT (vành + số), không kim.
          · gio∈1..12, phut∈0..59 → vẽ kèm kim GIỜ (ngắn+đậm, tự dịch theo phút)
                                      + kim PHÚT (dài+mảnh).
          · giay∈0..59 (tuỳ chọn) → thêm kim GIÂY (dài nhất + ĐỎ).  [thêm 25/08 — bài thật Hình 5]
        Bài thường hỏi = GÓC giữa hai kim tại một thời điểm. KHÔNG đặt tên điểm A/B/C trên mặt,
        KHÔNG vẽ cung góc trên mặt đồng hồ (chỉ hỏi số đo, không đánh dấu cung).
        Trả về R để gọi kim() thủ công nếu cần. (Số đặt qua diem_tren_tron — KHÔNG so_quanh_tam.)"""
        self.duong_tron(tam, ban_kinh=R, hien_tam=True)
        for k in range(1, 13):
            self.diem_tren_tron(str(k), tam, goc_o_tam=90-30*k, nhan=_NHAN_DONGHO[k])
        if gio is not None:
            self.kim(R, (gio % 12) + phut/60.0, loai='gio',  tam=tam)   # kim giờ
            self.kim(R, phut/5.0,               loai='phut', tam=tam)   # kim phút
        if giay is not None:
            self.kim(R, giay/5.0,               loai='giay', tam=tam)   # kim giây (đỏ)
        return R

    # ═══════════ [30i] LỚP 9 — TIẾP TUYẾN · QUẠT · VIÊN PHÂN (Ông Bụt Hình 2026-09-25) ═══════════
    #   Xây nền hình đường tròn lớp 9 (CH5 Đường tròn). MO_HINH_KHO §3. Nền cũ (L6): đồng hồ/vòng quay.

    def _don_vi(self, tam, diem):
        """Trả (u_perp, u_ban_kinh): vectơ đơn vị VUÔNG GÓC bán kính & DỌC bán kính (tam→diem)."""
        import math as _mm
        ox, oy = self.V[tam]; px, py = self.V[diem]
        dx, dy = px - ox, py - oy; L = _mm.hypot(dx, dy) or 1.0
        return (-dy/L, dx/L), (dx/L, dy/L)

    def _goc_polar(self, tam, diem):
        """Góc cực (độ) của 'diem' quanh 'tam' (đo từ hướng ngang, ngược chiều kim)."""
        import math as _mm
        ox, oy = self.V[tam]; px, py = self.V[diem]
        return _mm.degrees(_mm.atan2(py - oy, px - ox))

    def tiep_tuyen(self, tam, tiep_diem, dai=1.7, mau=None, net='lien', o_vuong=False):
        """TIẾP TUYẾN của đường tròn 'tam' tại 'tiep_diem' (đã đặt TRÊN đường tròn) — đoạn
        thẳng qua tiếp điểm, VUÔNG GÓC bán kính, nửa dài 'dai' mỗi phía. o_vuong=True → vẽ
        ô vuông góc (dấu ⊥ giữa bán kính và tiếp tuyến). KHÔNG tọa độ (Đ5.9)."""
        if tam not in self.tron:
            raise ValueError(f"tiep_tuyen: chưa khai đường tròn tâm '{tam}' (gọi duong_tron trước).")
        if tiep_diem not in self.V:
            raise ValueError(f"tiep_tuyen: chưa đặt tiếp điểm '{tiep_diem}'.")
        (ux, uy), _ = self._don_vi(tam, tiep_diem)
        px, py = self.V[tiep_diem]
        t1, t2 = f'_tt{tiep_diem}A', f'_tt{tiep_diem}B'
        self._diem(t1, px - dai*ux, py - dai*uy, None, moc=False)
        self._diem(t2, px + dai*ux, py + dai*uy, None, moc=False)
        self.tikz.append(('doan', t1, t2, mau, net, None))
        if o_vuong:
            self.tikz.append(('goc_vuong', [t2, tiep_diem, tam]))
        return self

    def hai_tiep_tuyen(self, tam, M, A='A', B='B', mau=None, o_vuong=True, noi_tam=False):
        """HAI TIẾP TUYẾN kẻ từ điểm 'M' NẰM NGOÀI đường tròn 'tam': tạo hai tiếp điểm A, B
        trên đường tròn + vẽ hai đoạn MA, MB. M đặt trước & phải ngoài đường tròn. o_vuong=True
        → ô vuông tại A, B (bán kính ⊥ tiếp tuyến). noi_tam=True → nối đoạn OM. PHANH kiểm A,B
        thuộc đường tròn (qua diem_tren_tron)."""
        import math as _mm
        if tam not in self.tron:
            raise ValueError(f"hai_tiep_tuyen: chưa khai đường tròn tâm '{tam}'.")
        if M not in self.V:
            raise ValueError(f"hai_tiep_tuyen: chưa đặt điểm '{M}'.")
        r = self.tron[tam]; ox, oy = self.V[tam]; mx, my = self.V[M]
        d = _mm.hypot(mx - ox, my - oy)
        if d <= r:
            raise ValueError(f"hai_tiep_tuyen: '{M}' phải NẰM NGOÀI đường tròn (khoảng cách {d:.3f} ≤ R {r}).")
        base = _mm.degrees(_mm.atan2(my - oy, mx - ox)); phi = _mm.degrees(_mm.acos(r/d))
        self.diem_tren_tron(A, tam, base + phi, nhan='above left')
        self.diem_tren_tron(B, tam, base - phi, nhan='below left')
        if noi_tam:
            self.tikz.append(('doan', tam, M, None, 'lien', None))
        self.tikz.append(('doan', M, A, mau, 'lien', None))
        self.tikz.append(('doan', M, B, mau, 'lien', None))
        if o_vuong:
            self.tikz.append(('goc_vuong', [M, A, tam]))
            self.tikz.append(('goc_vuong', [M, B, tam]))
        return self

    def tiep_tuyen_chung(self, tam1, tam2, loai='ngoai', phia=1, mau=None, net='lien',
                         tiep1='T', tiep2='T2', dai=0.7):
        """TIẾP TUYẾN CHUNG NGOÀI của hai đường tròn 'tam1','tam2' (đã khai): tạo hai tiếp
        điểm tiep1∈(tam1), tiep2∈(tam2) + vẽ đường tiếp tuyến qua chúng (kéo dài 'dai' mỗi
        đầu). phia=±1 chọn 1 trong 2 tiếp tuyến chung ngoài. Điều kiện: hai đường tròn tách
        rời (ngoài nhau). PHANH kiểm hai tiếp điểm thuộc đường tròn tương ứng."""
        import math as _mm
        if tam1 not in self.tron or tam2 not in self.tron:
            raise ValueError("tiep_tuyen_chung: cần khai cả hai đường tròn trước.")
        if loai != 'ngoai':
            raise ValueError("tiep_tuyen_chung: hiện chỉ hỗ trợ loai='ngoai'.")
        o1 = self.V[tam1]; o2 = self.V[tam2]; r1 = self.tron[tam1]; r2 = self.tron[tam2]
        dx, dy = o2[0]-o1[0], o2[1]-o1[1]; d = _mm.hypot(dx, dy) or 1.0
        ux, uy = dx/d, dy/d
        c = max(-1.0, min(1.0, (r1 - r2)/d)); beta = _mm.acos(c) * phia
        cb, sb = _mm.cos(beta), _mm.sin(beta)
        nx, ny = ux*cb - uy*sb, ux*sb + uy*cb          # n = quay u góc beta
        p1 = (o1[0] + r1*nx, o1[1] + r1*ny); p2 = (o2[0] + r2*nx, o2[1] + r2*ny)
        self._diem(tiep1, p1[0], p1[1], 'above left', moc=True, mau=mau)
        self._diem(tiep2, p2[0], p2[1], 'above right', moc=True, mau=mau)
        self.rb.append({'loai':'diem_tren_tron','diem':tiep1,'tam':tam1,'ban_kinh':r1})
        self.rb.append({'loai':'diem_tren_tron','diem':tiep2,'tam':tam2,'ban_kinh':r2})
        tx, ty = p2[0]-p1[0], p2[1]-p1[1]; tl = _mm.hypot(tx, ty) or 1.0; tx, ty = tx/tl, ty/tl
        e1, e2 = '_ttcA', '_ttcB'
        self._diem(e1, p1[0]-dai*tx, p1[1]-dai*ty, None, moc=False)
        self._diem(e2, p2[0]+dai*tx, p2[1]+dai*ty, None, moc=False)
        self.tikz.append(('doan', e1, e2, mau, net, None))
        return self

    def hinh_quat(self, tam, A, B, mau='cyan!18', vien=True):
        """TÔ MÀU HÌNH QUẠT TRÒN giới hạn bởi cung nhỏ AB và hai bán kính (tam)A, (tam)B
        (A,B đã đặt trên đường tròn). Sweep A→B theo cung ≤180° (cung nhỏ). vien=True → vẽ
        viền hai bán kính + cung."""
        if tam not in self.tron:
            raise ValueError(f"hinh_quat: chưa khai đường tròn tâm '{tam}'.")
        r = self.tron[tam]; gA = self._goc_polar(tam, A); gB = self._goc_polar(tam, B)
        gB2 = gA + (((gB - gA + 180) % 360) - 180)     # sweep về cung nhỏ (-180,180]
        path = f'({_HC._san(tam)}) -- ({_HC._san(A)}) arc ({gA:.3f}:{gB2:.3f}:{r:.3f}) -- cycle'
        self.tikz.append(('fill_raw', path, mau))
        if vien:
            self.tikz.append(('doan', tam, A, None, 'lien', None))
            self.tikz.append(('doan', tam, B, None, 'lien', None))
            self.cung(tam, gA, gB2, mau='black', net='lien', ban_kinh=r)
        return self

    def vien_phan(self, tam, A, B, mau='cyan!18', vien=True):
        """TÔ MÀU HÌNH VIÊN PHÂN giới hạn bởi dây AB và cung nhỏ AB (A,B trên đường tròn
        'tam'). vien=True → vẽ dây AB + cung."""
        if tam not in self.tron:
            raise ValueError(f"vien_phan: chưa khai đường tròn tâm '{tam}'.")
        r = self.tron[tam]; gA = self._goc_polar(tam, A); gB = self._goc_polar(tam, B)
        gB2 = gA + (((gB - gA + 180) % 360) - 180)
        path = f'({_HC._san(A)}) arc ({gA:.3f}:{gB2:.3f}:{r:.3f}) -- cycle'
        self.tikz.append(('fill_raw', path, mau))
        if vien:
            self.tikz.append(('doan', A, B, None, 'lien', None))
            self.cung(tam, gA, gB2, mau='black', net='lien', ban_kinh=r)
        return self

    # ═══════ [31j] LỚP 10 CH3 — ĐƯỜNG TRÒN NGOẠI/NỘI TIẾP TAM GIÁC (Ông Bụt Hình 2026-10-01) ═══════
    #   Hệ thức lượng (HH10_CH03_B06): HĐ3 định lí sin (tam giác nội tiếp đường tròn, Hình 3),
    #   HĐ4 công thức diện tích (đường tròn nội tiếp tâm I bán kính r, Hình 7). Máy tính TÂM
    #   (Đ5.9 cho phép HÀM kho tính toạ độ; người/AI KHÔNG cho). PHANH: đỉnh/tiếp điểm nằm trên
    #   đường tròn; nội tiếp tự kiểm d(I,cạnh)=r. Chữ ký MỞ (kế thừa lớp trên).

    def duong_tron_ngoai_tiep(self, A, B, C, tam='O', mau=None, net='lien',
                              hien_tam=True, noi_tam=False):
        """ĐƯỜNG TRÒN NGOẠI TIẾP tam giác A,B,C (3 đỉnh ĐÃ đặt, không thẳng hàng). Máy tính
        TÂM (giao 3 trung trực) + bán kính R=|tâm→A| — KHÔNG nhận toạ độ (Đ5.9). Đặt điểm 'tam'
        tại tâm ngoại tiếp, vẽ đường tròn qua 3 đỉnh. noi_tam=True → nối 3 bán kính tâm→A,B,C.
        PHANH kiểm A,B,C cùng nằm trên đường tròn (cách đều tâm)."""
        import math as _mm
        for _P in (A, B, C):
            if _P not in self.V:
                raise ValueError(f"duong_tron_ngoai_tiep: chưa đặt đỉnh '{_P}'.")
        (xa, ya), (xb, yb), (xc, yc) = self.V[A], self.V[B], self.V[C]
        d = 2.0 * (xa*(yb - yc) + xb*(yc - ya) + xc*(ya - yb))
        if abs(d) < 1e-9:
            raise ValueError("duong_tron_ngoai_tiep: 3 đỉnh thẳng hàng — không có đường tròn ngoại tiếp.")
        a2, b2, c2 = xa*xa + ya*ya, xb*xb + yb*yb, xc*xc + yc*yc
        ox = (a2*(yb - yc) + b2*(yc - ya) + c2*(ya - yb)) / d
        oy = (a2*(xc - xb) + b2*(xa - xc) + c2*(xb - xa)) / d
        r = _mm.hypot(xa - ox, ya - oy)
        self._diem(tam, ox, oy, 'below' if hien_tam else None, moc=hien_tam)
        self.tron[tam] = r
        self.tikz.append(('tron', tam, r, mau, net))
        for _P in (A, B, C):
            self.rb.append({'loai': 'diem_tren_tron', 'diem': _P, 'tam': tam, 'ban_kinh': r})
        if noi_tam:
            for _P in (A, B, C):
                self.tikz.append(('doan', tam, _P, None, 'lien', None))
        return self

    def duong_tron_noi_tiep(self, A, B, C, tam='I', mau=None, net='lien',
                            hien_tam=True, chan_vuong=False):
        """ĐƯỜNG TRÒN NỘI TIẾP tam giác A,B,C (3 đỉnh ĐÃ đặt). Máy tính TÂM (giao 3 phân giác:
        I = (a·A + b·B + c·C)/(a+b+c), với a=BC, b=CA, c=AB) + bán kính r=S/p — KHÔNG nhận toạ
        độ (Đ5.9). Đặt điểm 'tam' tại tâm nội tiếp, vẽ đường tròn. chan_vuong=True → đặt 3 chân
        vuông góc (tiếp điểm) trên 3 cạnh + nối bán kính (chấm đỏ). PHANH tự kiểm d(I,BC)=r."""
        import math as _mm
        for _P in (A, B, C):
            if _P not in self.V:
                raise ValueError(f"duong_tron_noi_tiep: chưa đặt đỉnh '{_P}'.")
        (xa, ya), (xb, yb), (xc, yc) = self.V[A], self.V[B], self.V[C]
        a = _mm.hypot(xb - xc, yb - yc)   # cạnh đối A = BC
        b = _mm.hypot(xc - xa, yc - ya)   # cạnh đối B = CA
        c = _mm.hypot(xa - xb, ya - yb)   # cạnh đối C = AB
        per = a + b + c
        if per < 1e-9 or min(a, b, c) < 1e-9:
            raise ValueError("duong_tron_noi_tiep: tam giác suy biến.")
        ix = (a*xa + b*xb + c*xc) / per
        iy = (a*ya + b*yb + c*yc) / per
        S = abs((xb - xa)*(yc - ya) - (xc - xa)*(yb - ya)) / 2.0
        p = per / 2.0
        r = S / p
        # PHANH tự kiểm: khoảng cách I→cạnh BC phải = r (verify incenter)
        dBC = abs((xc - xb)*(iy - yb) - (ix - xb)*(yc - yb)) / (a or 1.0)
        if abs(dBC - r) > 1e-6 * max(1.0, r):
            raise ValueError(f"duong_tron_noi_tiep: PHANH lệch (d(I,BC)={dBC:.6f} ≠ r={r:.6f}).")
        self._diem(tam, ix, iy, 'below' if hien_tam else None, moc=hien_tam)
        self.tron[tam] = r
        self.tikz.append(('tron', tam, r, mau, net))
        if chan_vuong:
            def _chan(ten, Px, Py, Qx, Qy, nhan):
                vx, vy = Qx - Px, Qy - Py
                L2 = vx*vx + vy*vy or 1.0
                t = ((ix - Px)*vx + (iy - Py)*vy) / L2
                self._diem(ten, Px + t*vx, Py + t*vy, nhan, moc=True, mau='red')
                self.rb.append({'loai': 'diem_tren_tron', 'diem': ten, 'tam': tam, 'ban_kinh': r})
                self.tikz.append(('doan', tam, ten, 'red', 'lien', None))
            _chan('_tiepA', xb, yb, xc, yc, 'below')        # tiếp điểm trên BC
            _chan('_tiepB', xc, yc, xa, ya, 'above right')  # tiếp điểm trên CA
            _chan('_tiepC', xa, ya, xb, yb, 'above left')   # tiếp điểm trên AB
        return self


# ═══ [29c] Ông Bụt 2026-09-16 · DS8 Chương 2 (Hằng đẳng thức) ═══
import hinh_core as _HC
def vanhKhan(R='R', r='r', toVanh=True, chuThich=None, nua=False,
             out='vanh_khan', tra_bytes=False):
    """VÀNH KHĂN — hai đường tròn đồng tâm tâm O; bán kính ngoài R, trong r (r<R),
       mỗi bán kính có nhãn ĐẶT GIỮA đoạn; vành giữa tô nhạt (toVanh).
       nua=True → NỬA vành khuyên (quạt giấy xoè nửa hình tròn — SGK 5.13)."""
    R = _HC._m(R, 'R'); r = _HC._m(r, 'r')
    if nua:
        return _vanhKhan_nua(R, r, toVanh, chuThich, out, tra_bytes)
    to = (r'\fill[cyan!14, even odd rule] (O) circle (\R) (O) circle (\r);'
          if toVanh else '')
    cap = ''
    if chuThich:
        cap = (r'\node[below,font=\itshape] at (0,CAPY) {CAPT};'
               .replace('CAPT', chuThich).replace('CAPY', r'-\R-0.55'))
    body = r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\normalsize]
  \def\R{3.0}\def\r{1.7}
  \coordinate (O) at (0,0);
  @@TO@@
  \draw[line width=0.8pt] (O) circle (\R);
  \draw[line width=0.8pt] (O) circle (\r);
  % bán kính ngoài R (hướng 35°) + nhãn giữa đoạn
  \draw (O) -- (35:\R);
  \node[above,font=\small] at (35:{\R/2}) {$@@R@@$};
  % bán kính trong r (hướng -125°) + nhãn giữa đoạn
  \draw (O) -- (-125:\r);
  \node[below left,font=\small] at (-125:{\r/2}) {$@@r@@$};
  \fill (O) circle (1.6pt); \node[above right,font=\small] at (O) {$O$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
    body = (body.replace('@@TO@@', to).replace('@@R@@', R).replace('@@r@@', r)
                .replace('@@CAP@@', cap))
    return _HC.render_tikz_doc(body, out, tra_bytes)

def _vanhKhan_nua(R, r, toVanh, chuThich, out, tra_bytes):
    """[30i] NỬA vành khuyên (nửa trên) — quạt giấy xoè nửa hình tròn (SGK 5.13)."""
    to = (r'\fill[cyan!14] (\R,0) arc (0:180:\R) -- (-\r,0) arc (180:0:\r) -- cycle;'
          if toVanh else '')
    cap = ''
    if chuThich:
        cap = (r'\node[below,font=\itshape] at (0,-0.35) {CAPT};'.replace('CAPT', chuThich))
    body = r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[font=\normalsize]
  \def\R{3.0}\def\r{1.2}
  \coordinate (O) at (0,0);
  @@TO@@
  \draw[line width=0.8pt] (\R,0) arc (0:180:\R);
  \draw[line width=0.8pt] (\r,0) arc (0:180:\r);
  \draw[line width=0.8pt] (-\R,0)--(-\r,0);
  \draw[line width=0.8pt] (\r,0)--(\R,0);
  % bán kính ngoài R (hướng 60°) + nhãn giữa đoạn
  \draw (O) -- (60:\R);
  \node[above left,font=\small] at (60:{\R/2}) {$@@R@@$};
  % chiều rộng phần giấy (R - r) hướng 120°
  \draw[|<->|] (120:\r) -- (120:\R);
  \node[left,font=\small] at (120:{(\R+\r)/2}) {$@@W@@$};
  \fill (O) circle (1.6pt); \node[below,font=\small] at (O) {$O$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
    body = (body.replace('@@TO@@', to).replace('@@R@@', R)
                .replace('@@W@@', 'w').replace('@@CAP@@', cap))
    return _HC.render_tikz_doc(body, out, tra_bytes)

# [29c] gắn làm staticmethod class entry → vào bản trích + gọi qua instance
HinhTron.vanhKhan = staticmethod(vanhKhan)


# ═══════ [31l] NỬA ĐƯỜNG TRÒN ĐƠN VỊ — ĐỊNH NGHĨA GTLG GÓC 0°–180° (Ông Bụt Hình THPT 2026-10-01) ═══════
#   Bài HH10_CH03_B05: định nghĩa GTLG (H3.2) · VD 135°/120° (H3.3/3.4) · góc bù nhau (H3.5) · góc phụ nhau (H3.6).
#   Hệ Oxy + nửa đường tròn R=1 trên trục hoành + điểm M tại góc xOM=α (máy tính toạ độ cos/sin — Đ5.9, KHÔNG nhập tay).
def _ndtdv_lab(s):
    """Nhãn math: 'α'→$\\alpha$ ; '180°-α'→$180^\\circ-\\alpha$ ; 'x_0'/'M'→$...$ ; có sẵn $ → giữ."""
    s = str(s)
    if '$' in s:
        return s
    if _HC._has_greek(s):
        out = ''
        for ch in s:
            if ch in _HC._GREEK:
                out += _HC._GREEK[ch]
            elif ch == '°':
                out += r'^\circ '
            else:
                out += ch
        return '$%s$' % out
    return '$%s$' % s

def nua_duong_tron_don_vi(diem=None, R=3.0, scale=1.0, nhan_ABC=False,
                          out='nua_dt_don_vi', tra_bytes=False):
    """NỬA ĐƯỜNG TRÒN ĐƠN VỊ (định nghĩa GTLG góc 0°–180°, SGK H3.2–3.6).
    Hệ trục Oxy (mũi tên) + nửa đường tròn tâm O bán kính R=1 nằm TRÊN trục hoành
    (B(-1,0)→C(0,1)→A(1,0), đỏ) + nhãn -1,1. Mỗi 'điểm' M trên nửa đường tròn tại góc xOM=α;
    máy tính toạ độ (cosα,sinα)·R — nhận NGHĨA (góc), KHÔNG toạ độ (Đ5.9).
    diem: list dict, mỗi điểm:
      ten:'M'(bắt buộc) · goc:α độ 0–180(bắt buộc) · ban_kinh=True(vẽ OM) ·
      ox_ten/oy_ten: tên chân chiếu lên Ox/Oy (chấm+nhãn) · ox_nhan/oy_nhan: nhãn toạ độ chân
        (vd 'x_0','-x_0','y_0') · ve_chieu_ox/oy: ép vẽ gióng nét đứt (mặc định True nếu có ten/nhan) ·
      cung:'α'|số|None (vẽ cung xOM + nhãn) · cung_r: bán kính cung (mặc định 0.6, nest nhiều cung) ·
      cung_phu:(g1,g2,nhãn[,r]) cung phụ (vd góc MON 45° H3.3) · mau_diem:'blue'(mặc định).
    nhan_ABC=True → nhãn A(1,0),B(-1,0),C(0,1). PHANH nội sinh: góc ∈[0,180]; toạ độ cos/sin (dựng)."""
    diem = diem or []
    R = float(R)
    rac = R + 0.62        # mũi trục ngoài đường tròn
    L = [r'\documentclass[border=6pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.4mm]},font=\normalsize]' % scale]
    # trục Oxy (x hai đầu? SGK: x mũi phải + nhánh trái tới -rac; y mũi trên)
    L.append(r'\draw[<->,thick] (-%g,0) -- (%g,0) node[right] {$x$};' % (rac, rac))
    L.append(r'\draw[->,thick] (0,-0.45) -- (0,%g) node[above] {$y$};' % (R + 0.55))
    # nửa đường tròn đỏ R + nhãn mốc
    L.append(r'\draw[red,line width=0.9pt] (%g,0) arc (0:180:%g);' % (R, R))
    L.append(r'\node[below] at (%g,-0.05) {$-1$};' % (-R))
    L.append(r'\node[below] at (%g,-0.05) {$1$};' % (R))
    L.append(r'\node[left] at (0,%g) {$1$};' % R)
    L.append(r'\fill (0,0) circle (1.5pt); \node[below left,font=\small] at (0,0) {$O$};')
    if nhan_ABC:
        L.append(r'\fill[blue] (%g,0) circle (1.6pt); \node[below right,font=\small,blue] at (%g,0) {$A$};' % (R, R))
        L.append(r'\fill[blue] (%g,0) circle (1.6pt); \node[below left,font=\small,blue] at (%g,0) {$B$};' % (-R, -R))
        L.append(r'\fill[blue] (0,%g) circle (1.6pt); \node[above left,font=\small,blue] at (0,%g) {$C$};' % (R, R))
    for d in diem:
        ten = d['ten']; a = float(d['goc'])
        if not (0.0 <= a <= 180.0):
            raise ValueError("[nua_duong_tron_don_vi] góc %s='%s' ngoài [0,180] — điểm không trên nửa trên." % (ten, a))
        mau = d.get('mau_diem', 'blue')
        mx = R * math.cos(math.radians(a)); my = R * math.sin(math.radians(a))
        fx = (mx, 0.0); fy = (0.0, my)
        # gióng nét đứt
        ox_ten = d.get('ox_ten'); ox_nhan = d.get('ox_nhan')
        oy_ten = d.get('oy_ten'); oy_nhan = d.get('oy_nhan')
        ve_ox = d.get('ve_chieu_ox', (ox_ten is not None or ox_nhan is not None))
        ve_oy = d.get('ve_chieu_oy', (oy_ten is not None or oy_nhan is not None))
        if ve_ox:
            L.append(r'\draw[dashed,gray] (%g,%g) -- (%g,%g);' % (mx, my, fx[0], fx[1]))
        if ve_oy:
            L.append(r'\draw[dashed,gray] (%g,%g) -- (%g,%g);' % (mx, my, fy[0], fy[1]))
        # bán kính OM
        if d.get('ban_kinh', True):
            L.append(r'\draw[thick] (0,0) -- (%g,%g);' % (mx, my))
        # cung xOM + nhãn
        cg = d.get('cung')
        if cg is not None:
            cr = float(d.get('cung_r', 0.6))
            L.append(r'\draw[orange,thick] (%g:%g) arc (0:%g:%g);' % (0.0, cr, a, cr))
            mid = a / 2.0; lr = cr + 0.34
            lbl = ('$%g^\\circ$' % cg) if isinstance(cg, (int, float)) else _ndtdv_lab(cg)
            L.append(r'\node[orange,font=\small] at (%g:%g) {%s};' % (mid, lr, lbl))
        cp = d.get('cung_phu')
        if cp is not None:
            g1, g2, lbp = cp[0], cp[1], cp[2]; cpr = float(cp[3]) if len(cp) > 3 else 0.95
            L.append(r'\draw[orange,thick] (%g:%g) arc (%g:%g:%g);' % (g1, cpr, g1, g2, cpr))
            lbl = ('$%g^\\circ$' % lbp) if isinstance(lbp, (int, float)) else _ndtdv_lab(lbp)
            L.append(r'\node[orange,font=\small] at (%g:%g) {%s};' % ((g1 + g2) / 2.0, cpr + 0.3, lbl))
        # chấm chân chiếu + nhãn
        if ox_ten or ox_nhan:
            L.append(r'\fill (%g,0) circle (1.3pt);' % mx)
        if ox_ten:
            L.append(r'\node[below,font=\small] at (%g,-0.04) {%s};' % (mx, _ndtdv_lab(ox_ten)))
        if ox_nhan:
            dy2 = -0.04 if not ox_ten else -0.42
            L.append(r'\node[below,font=\small] at (%g,%g) {%s};' % (mx, dy2, _ndtdv_lab(ox_nhan)))
        if oy_ten:
            L.append(r'\fill (0,%g) circle (1.3pt); \node[left,font=\small] at (-0.06,%g) {%s};' % (my, my, _ndtdv_lab(oy_ten)))
        if oy_nhan:
            L.append(r'\node[%s,font=\small] at (0.08,%g) {%s};' % ('right' if mx < 0 else 'left', my, _ndtdv_lab(oy_nhan)))
        # điểm M + nhãn
        anc = 'above right' if mx >= -0.05 else 'above left'
        L.append(r'\fill[%s] (%g,%g) circle (1.7pt); \node[%s,font=\small,%s] at (%g,%g) {%s};'
                 % (mau, mx, my, anc, mau, mx, my, _ndtdv_lab(ten)))
    L.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(L), out, tra_bytes)

HinhTron.nua_duong_tron_don_vi = staticmethod(nua_duong_tron_don_vi)
