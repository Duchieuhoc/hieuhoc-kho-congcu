#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_daiso.py — ENTRY MẠCH ĐẠI SỐ (tia số / trục số) — DS THCS lớp 6→9
#   class Hinh(HinhCoBan): thêm primitive `tia_so`. COMPOSE THUẦN từ base
#   (đoạn/ghi_chu/chấm/tia) — KHÔNG mổ lõi, KHÔNG thêm renderer op mới.
#   Đặt nền cho tia số (DS6) → trục số âm/dương, trục toạ độ (lớp 7→9).
# [28p] +tia_so (Ông Bụt 2026-09-04, Pha B DS6_CH01_B03 — bài Đại số đầu cần hình;
#        kho 28o toàn Hình học, không có tia số → khe hở lộ khi soạn B03).
#   Triết lý giữ nguyên base: AI Soạn khai GIÁ TRỊ ngữ nghĩa (gia_tri_max/buoc/diem),
#   máy TỰ TÍNH toạ độ. Không lộ toạ độ thô → qua cổng AST cua_quet_hinh (Đ5.9).
# CS2627.
# ═══════════════════════════════════════════════════════════════════
from hinh_coban import HinhCoBan


class Hinh(HinhCoBan):
    """Entry Đại số — tia số & trục số tự nhiên. Kế thừa toàn bộ base HinhCoBan."""

    def tia_so(self, gia_tri_max=None, buoc=1, diem=None, hien_nhan_diem=True,
               moc_nhan=None, ti_le=True, mui_ten=True, goc_ten='O', nhay=None):
        """TIA SỐ tự nhiên — gốc bên trái, mũi tên sang phải; vạch chia + nhãn số + điểm đánh dấu.

        gia_tri_max    : giá trị lớn nhất hiển thị (bỏ qua khi ti_le=False).
        buoc           : mỗi VẠCH ứng bao nhiêu đơn vị (1, 5, …).
        diem           : list [(gia_tri, ten)] — điểm đánh dấu; ten=None → chỉ chấm (bài xác định điểm).
        hien_nhan_diem : True ghi giá trị dưới điểm; False chỉ hiện tên — bài ĐỌC ĐIỂM, Đ35 (cấm lộ đáp án).
        moc_nhan       : list giá trị được ghi nhãn số dưới vạch; None → ghi MỌI vạch.
        ti_le          : True khoảng cách đúng tỉ lệ; False khoảng danh nghĩa đều nhau ("không theo tỉ lệ").
        mui_ten        : True vẽ mũi tên đầu phải (ký hiệu tia).
        goc_ten        : nhãn gốc (mặc định 'O'; 'km0' cho tia cột mốc).

        Máy tự tính toạ độ từ GIÁ TRỊ — AI Soạn chỉ khai nghĩa (không đụng toạ độ, Đ5.9).
        """
        self._nen_luoi = False                       # tia số: nền sạch, không ô lưới vuông
        diem = list(diem or [])

        if ti_le:
            if gia_tri_max is None or gia_tri_max <= 0:
                raise ValueError("[tia_so] cần gia_tri_max > 0 khi ti_le=True")
            if buoc <= 0:
                raise ValueError("[tia_so] buoc phải > 0")
            so_vach = int(gia_tri_max // buoc)
            for k in range(so_vach + 1):
                gt = k * buoc
                self._vach(k, k)
                if (moc_nhan is None) or (gt in moc_nhan):
                    self.ghi_chu(k, -0.44, self._so(gt))
            for j, (gt, ten) in enumerate(diem):
                if gt < 0 or gt > gia_tri_max:
                    raise ValueError(f"[tia_so] điểm {gt} ngoài đoạn [0, {gia_tri_max}]")
                if gt % buoc != 0:
                    raise ValueError(f"[tia_so] điểm {gt} không rơi vạch (bước {buoc})")
                da_ghi = (moc_nhan is None) or (gt in moc_nhan)
                self._danh_dau(j, gt / buoc, gt, ten,
                               hien_gt=(hien_nhan_diem and not da_ghi))
            x_end = so_vach + 0.7
        else:
            if not diem:
                raise ValueError("[tia_so] ti_le=False cần danh sách 'diem'")
            KHOANG = 2.4                                  # giãn để nhãn dài không chồng
            self._vach(0, 0)
            for i, (gt, ten) in enumerate(diem, start=1):
                self._vach(i * KHOANG, i)
                self._danh_dau(i - 1, i * KHOANG, gt, ten, hien_gt=False)
            x_end = len(diem) * KHOANG + 0.7

        # bước nhảy cộng/trừ (Hình 1.6–1.8): cung + mũi tên tu→den (giá trị), nhãn ở đỉnh
        for (tu, den, nh) in (nhay or []):
            self.tikz.append(('nhay', tu / buoc, den / buoc, str(nh) if nh else ''))

        self.ghi_chu(-0.30, 0.30, goc_ten)           # nhãn gốc
        # trục + mũi tên: renderer 'tia' kéo dài 1.25× từ gốc → đặt mút để mũi tới đúng x_end
        self._diem('_tsO', 0, 0, nhan=None, moc=False)
        self._diem('_tsE', x_end * 0.8, 0, nhan=None, moc=False)
        self.tikz.append(('tia', '_tsO', '_tsE', mui_ten, None, 'lien'))
        return self

    # ═══════════════════════════════════════════════════════════════
    # [28r] TRỤC SỐ HỮU TỈ — DS7 Chương I "Số hữu tỉ".
    #   KHE HỞ: tia_so (DS6) là TIA tự nhiên — gốc trái, chỉ dương, điểm rơi
    #   vạch NGUYÊN, nhãn thập phân. DS7 cần: phần ÂM/DƯƠNG (gốc O giữa), CHIA
    #   đoạn đơn vị thành n phần, điểm tại toạ độ PHÂN SỐ (cả âm), nhãn phân số.
    #   COMPOSE THUẦN base (tia/đoạn/so_o) — KHÔNG mổ lõi, KHÔNG op renderer mới.
    #   Trục 2 phía = tia dương (có mũi) + tia âm (kéo dài) — pattern base tia_diem.
    #   Nhãn phân số qua $\frac{a}{b}$ (renderer TikZ math mode) — chỉ số, an toàn
    #   font (không đụng lỗi horn-glyph ơ/ư của Computer Modern).
    #   AI Soạn khai GIÁ TRỊ (tu/den/chia/diem) — máy TỰ TÍNH toạ độ (Đ5.9).
    # ═══════════════════════════════════════════════════════════════
    def truc_so_huu_ti(self, tu=-1, den=4, chia=1, diem=None,
                       hien_nhan_diem=True, moc_nhan=None,
                       mui_ten_am=False, goc_ten='0',
                       khoang_to=None, vach_dut=None):
        """TRỤC SỐ biểu diễn số hữu tỉ — gốc O ở giá trị 0, có phần âm & dương.

        tu, den        : biên NGUYÊN trái/phải của trục (tu có thể < 0). Cần tu < den.
        chia           : chia MỖI đoạn đơn vị thành `chia` phần bằng nhau (1,2,3,4,6,12…);
                         chia>1 → vẽ vạch PHỤ (ngắn) để đặt phân số 1/chia, 2/chia…
        diem           : list điểm. Mỗi phần tử (gt, ten) hoặc (gt, ten, nhan):
                           · gt  = giá trị điểm — Fraction | (tử,mẫu) | int | float | "a/b";
                           · ten = nhãn TRÊN điểm (A,B,C — bài đọc) hoặc None → chỉ chấm;
                           · nhan= nhãn DƯỚI điểm; bỏ trống → TỰ sinh phân số của gt;
                                   None (khai rõ) → KHÔNG ghi nhãn dưới.
        hien_nhan_diem : False → không ghi giá trị dưới điểm (bài ĐỌC ĐIỂM, Đ35 cấm lộ đáp án).
        moc_nhan       : list số NGUYÊN được ghi nhãn dưới vạch chính; None → ghi MỌI số nguyên.
        mui_ten_am     : True → phía âm cũng có mũi tên (mặc định False: chỉ kéo dài, chuẩn SGK).
        goc_ten        : nhãn tại vị trí 0 (mặc định '0').
        khoang_to      : list (x1, x2, nhan) — tô DẢI + mũi tên 2 đầu giữa hai giá trị trên trục,
                         ghi `nhan` (nhãn độ dài, vd "0,5") NGAY TRÊN dải. Biểu diễn "độ chính xác"
                         (khoảng làm tròn). x1, x2 nhận Fraction|(tử,mẫu)|int|float|"a/b".
        vach_dut       : list giá trị — vẽ VẠCH ĐỨNG NÉT ĐỨT tại các giá trị (kể cả giá trị lẻ
                         không rơi vạch phụ), vd trung điểm 46,5. Nhận cùng kiểu giá trị như trên.

        Máy tự tính toạ độ từ GIÁ TRỊ — AI Soạn không đụng toạ độ thô (Đ5.9).
        """
        from fractions import Fraction
        if not (isinstance(tu, int) and isinstance(den, int)) or tu >= den:
            raise ValueError("[truc_so_huu_ti] cần tu, den NGUYÊN và tu < den")
        if chia < 1:
            raise ValueError("[truc_so_huu_ti] chia phải ≥ 1")
        self._nen_luoi = False
        SCALE = 1.4                      # mỗi đơn vị = 1,4 đơn vị vẽ (thoáng vạch phụ)

        def _toFrac(gt):
            if isinstance(gt, Fraction): return gt
            if isinstance(gt, tuple):    return Fraction(gt[0], gt[1])
            if isinstance(gt, int):      return Fraction(gt)
            if isinstance(gt, float):    return Fraction(gt).limit_denominator(10000)
            if isinstance(gt, str):
                s = gt.strip().replace(',', '.')
                return Fraction(s) if '/' in s else Fraction(s).limit_denominator(10000)
            return Fraction(gt)

        def _nhan_frac(q):               # Fraction → nhãn hiển thị (số nguyên hoặc $\frac{}{}$)
            if q.denominator == 1:
                return self._so(float(q))            # "-1","0","2"
            dau = '-' if q < 0 else ''
            return r'$%s\frac{%d}{%d}$' % (dau, abs(q.numerator), q.denominator)

        # ── TRỤC: gốc 0 ở giữa, tia dương (mũi) + tia âm (kéo dài) ──
        x_R = den * SCALE + 0.6
        x_L = tu  * SCALE - 0.6
        self._diem('_htO', 0.0, 0.0, nhan=None, moc=False)
        self._diem('_htR', x_R / 1.25, 0.0, nhan=None, moc=False)     # mũi (keo 1.25) → tới x_R
        keoL = 1.25 if mui_ten_am else 1.15
        self._diem('_htL', x_L / keoL, 0.0, nhan=None, moc=False)
        self.tikz.append(('tia', '_htO', '_htR', True, None, 'lien'))
        self.tikz.append(('tia', '_htO', '_htL', mui_ten_am, None, 'lien'))

        # ── VẠCH CHÍNH (số nguyên) + nhãn ──
        for n in range(tu, den + 1):
            x = n * SCALE
            self._vach_ht(x, f'n{n - tu}', chinh=True)
            if (moc_nhan is None) or (n in moc_nhan):
                self.ghi_chu(x, -0.44, goc_ten if n == 0 else self._so(n))

        # ── VẠCH PHỤ (chia đoạn đơn vị) ──
        if chia > 1:
            vid = 0
            for n in range(tu, den):
                for j in range(1, chia):
                    self._vach_ht((n + j / chia) * SCALE, f'p{vid}', chinh=False)
                    vid += 1

        # ── ĐIỂM đánh dấu (toạ độ phân số/âm) ──
        for idx, spec in enumerate(diem or []):
            gt, ten = spec[0], spec[1]
            nhan = spec[2] if len(spec) > 2 else 'auto'
            q = _toFrac(gt)
            if q < tu or q > den:
                raise ValueError(f"[truc_so_huu_ti] điểm {gt} ngoài đoạn [{tu}, {den}]")
            x = float(q) * SCALE
            self._diem(f'_hp{idx}', x, 0.0, nhan=None, moc=True)     # chấm đậm
            if ten:
                self.ghi_chu(x, 0.34, str(ten))                     # nhãn tên (trên)
            if hien_nhan_diem and nhan is not None:
                self.ghi_chu(x, -0.44, _nhan_frac(q) if nhan == 'auto' else str(nhan))

        # ── VẠCH ĐỨT (giá trị lẻ, vd trung điểm 46,5) ──
        for vi, gt in enumerate(vach_dut or []):
            q = _toFrac(gt)
            if q < tu or q > den:
                raise ValueError(f"[truc_so_huu_ti] vach_dut {gt} ngoài đoạn [{tu}, {den}]")
            x = float(q) * SCALE
            a, b = f'_vda{vi}', f'_vdb{vi}'
            self._diem(a, x, 0.16, nhan=None, moc=False)
            self._diem(b, x, -0.16, nhan=None, moc=False)
            self.tikz.append(('doan', a, b, None, 'dut', 'manh'))

        # ── KHOẢNG TÔ (dải "độ chính xác" + mũi tên 2 đầu + nhãn độ dài) ──
        for ki, spec in enumerate(khoang_to or []):
            x1, x2, nhanKC = spec[0], spec[1], spec[2]
            q1, q2 = _toFrac(x1), _toFrac(x2)
            for qq in (q1, q2):
                if qq < tu or qq > den:
                    raise ValueError(f"[truc_so_huu_ti] khoang_to {qq} ngoài đoạn [{tu}, {den}]")
            xa, xb = float(q1) * SCALE, float(q2) * SCALE
            ya, yb = f'_kca{ki}', f'_kcb{ki}'
            YKC = 0.30                                   # dải nằm TRÊN trục
            self._diem(ya, xa, YKC, nhan=None, moc=False)
            self._diem(yb, xb, YKC, nhan=None, moc=False)
            self.tikz.append(('khoang', ya, yb, str(nhanKC)))

        self.ghi_chu(-0.30, 0.30, '')   # giữ khoảng trên gốc (nhãn 0 nằm dưới)
        return self

    def truc_do_chinh_xac(self, trai, phai, a, do_chinh_xac=None, nhan_a='a'):
        """TRỤC SỐ 'ĐỘ CHÍNH XÁC LÀM TRÒN' — đoạn cục bộ [trai; phai] (KHÔNG cần gốc 0).

        Dựng trọn cảnh minh họa làm tròn (SGK Toán 7 Hình 2.1):
          · trục ngang chỉ trong đoạn [trai; phai] (hai mốc nguyên liền kề), mũi tên 2 đầu;
          · điểm a nằm giữa, nhãn `nhan_a` phía trên; vạch đứt tại trung điểm (trai+phai)/2;
          · dải "độ chính xác" từ mốc GẦN a nhất tới trung điểm, nhãn = do_chinh_xac (vd "0,5").

        trai, phai     : hai mốc NGUYÊN liền kề (phai = trai + 1). Vd 46, 47.
        a              : giá trị điểm cần làm tròn (trai < a < phai) — float | "a/b" | (tử,mẫu) | Fraction.
        do_chinh_xac   : nhãn độ dài dải (vd "0,5"); None → tự ghi "0,5" (một nửa đơn vị).
        nhan_a         : nhãn trên điểm a (mặc định 'a').

        Máy tự tính toạ độ — AI Soạn chỉ khai GIÁ TRỊ (Đ5.9). Nền sạch, không lưới.
        """
        from fractions import Fraction
        if not (isinstance(trai, int) and isinstance(phai, int)) or phai != trai + 1:
            raise ValueError("[truc_do_chinh_xac] cần trai, phai NGUYÊN liền kề (phai = trai+1)")

        def _toF(v):
            if isinstance(v, Fraction): return v
            if isinstance(v, tuple):    return Fraction(v[0], v[1])
            if isinstance(v, int):      return Fraction(v)
            if isinstance(v, float):    return Fraction(v).limit_denominator(10000)
            if isinstance(v, str):
                s = v.strip().replace(',', '.')
                return Fraction(s) if '/' in s else Fraction(s).limit_denominator(10000)
            return Fraction(v)

        qa = _toF(a)
        if not (trai < qa < phai):
            raise ValueError(f"[truc_do_chinh_xac] a={a} phải nằm trong ({trai}; {phai})")
        self._nen_luoi = False
        SCALE = 4.2                          # đoạn 1 đơn vị kéo rộng cho thoáng
        mid = Fraction(trai + phai, 2)       # trung điểm
        moc_gan = trai if abs(qa - trai) <= abs(qa - phai) else phai  # mốc gần a nhất

        def _X(q): return (float(q) - trai) * SCALE   # gốc vẽ đặt tại `trai`

        xL, xR = _X(Fraction(trai)), _X(Fraction(phai))
        # trục: 1 đường mũi tên 2 đầu, thò nhẹ ngoài 2 mốc
        self._diem('_dcL', xL - 0.5, 0.0, nhan=None, moc=False)
        self._diem('_dcR', xR + 0.5, 0.0, nhan=None, moc=False)
        self.tikz.append(('truc2dau', '_dcL', '_dcR'))
        # hai mốc nguyên + nhãn
        for n in (trai, phai):
            x = _X(Fraction(n))
            self._vach_ht(x, f'dc{n}', chinh=True)
            self.ghi_chu(x, -0.46, self._so(n))
        # vạch đứt trung điểm
        xm = _X(mid)
        self._diem('_dcma', xm, 0.18, nhan=None, moc=False)
        self._diem('_dcmb', xm, -0.18, nhan=None, moc=False)
        self.tikz.append(('doan', '_dcma', '_dcmb', None, 'dut', 'manh'))
        # điểm a + nhãn trên
        xa = _X(qa)
        self._diem('_dcA', xa, 0.0, nhan=None, moc=True)
        self.ghi_chu(xa, 0.34, str(nhan_a))
        # dải độ chính xác: từ mốc gần a → trung điểm
        xg = _X(Fraction(moc_gan))
        self._diem('_dckA', xg, 0.34, nhan=None, moc=False)
        self._diem('_dckB', xm, 0.34, nhan=None, moc=False)
        self.tikz.append(('khoang', '_dckA', '_dckB', do_chinh_xac or '0,5'))
        return self

    def dung_can_hai(self, canh=2, nhan_diem='A', nhan_can=None):
        """DỰNG √2 (hoặc √(canh²/2)) TRÊN TRỤC SỐ bằng compa — SGK Toán 7 Hình 2.3.

        Compose ngữ nghĩa: máy tự dựng hình vuông cạnh `canh` + hai đường chéo cắt tại tâm E,
        rồi trục Ox (gốc O), đường tròn tâm O bán kính OE, cắt tia Ox tại điểm A = nửa đường chéo
        = canh·√2/2. Với canh=2 → A = √2 (đúng SGK).

        AI Soạn CHỈ khai giá trị `canh` — KHÔNG đụng toạ độ/bán kính thô (Đ5.9).

        canh       : cạnh hình vuông dựng (mặc định 2 → ra √2).
        nhan_diem  : nhãn điểm giao trên trục (mặc định 'A').
        nhan_can   : nhãn giá trị dưới điểm A (vd '√2'); None → không ghi (đúng SGK, để HS nhận).
        """
        import math as _m
        self._nen_luoi = False
        c = float(canh)
        nua_cheo = c * _m.sqrt(2) / 2         # OE = A trên trục
        # ── Hình vuông MNPQ cạnh c, đặt phía trên-trái, tách khỏi trục ──
        oy = 1.9                               # nâng hình vuông cao hơn (tách khỏi đường tròn)
        ox = -c - 1.4                          # đặt lệch trái gốc O nhiều hơn
        M=(ox, oy+c); N=(ox+c, oy+c); P=(ox+c, oy); Q=(ox, oy)
        for tn,(px,py) in [('M',M),('N',N),('P',P),('Q',Q)]:
            self._diem(tn, px, py, nhan='above' if py>oy else 'below', moc=True)
        for a,b in [('M','N'),('N','P'),('P','Q'),('Q','M')]:
            self.tikz.append(('doan', a, b, None, 'lien', None))
        # hai đường chéo + tâm E
        self.tikz.append(('doan','M','P',None,'lien',None))
        self.tikz.append(('doan','N','Q',None,'lien',None))
        ex,ey = (ox+c/2, oy+c/2)
        self._diem('E', ex, ey, nhan='above right', moc=True)
        self.ghi_chu((M[0]+N[0])/2, M[1]+0.12, self._so(int(c)) if c==int(c) else str(c))
        # ── Trục Ox: gốc O tại (0,0), mũi tên 2 đầu ──
        SC = 1.0
        xO = 0.0
        self._diem('O', xO, 0.0, nhan=None, moc=True)
        xR = nua_cheo*SC + 1.2
        self._diem('_ox_L', -0.6, 0.0, nhan=None, moc=False)
        self._diem('_ox_R', xR, 0.0, nhan=None, moc=False)
        self.tikz.append(('truc2dau','_ox_L','_ox_R'))
        self.ghi_chu(xO, -0.44, '0')
        self.ghi_chu(xR-0.05, 0.22, 'x')
        # ── Đường tròn tâm O bán kính OE (=nua_cheo) → điểm A trên tia Ox ──
        self.tikz.append(('tron','O', nua_cheo*SC, None, 'dut'))
        xA = nua_cheo*SC
        self._diem(nhan_diem, xA, 0.0, nhan='above', moc=True)
        if nhan_can:
            self.ghi_chu(xA, -0.34, str(nhan_can))
        return self

    def truc_doan_doc_diem(self, trai, phai, chia=10, diem=None,
                           hien_nhan_diem=False, moc_nhan=None):
        """TRỤC SỐ ĐOẠN PHÓNG TO để ĐỌC ĐIỂM — biên THẬP PHÂN, chia nhỏ, kéo rộng.

        Dùng cho bài "quan sát hình, đọc số biểu diễn bởi điểm" (SGK 2.15, 2.22):
        đoạn [trai; phai] (biên thập phân được), chia `chia` vạch nhỏ, hiển thị rộng đủ
        để các điểm không chồng. Điểm KHÔNG ghi đáp số (Đ35) trừ khi hien_nhan_diem=True.

        trai, phai      : biên đoạn — nhận float | "a/b" | (tử,mẫu) | Fraction (THẬP PHÂN OK).
        chia            : số vạch nhỏ chia đều đoạn (mặc định 10).
        diem            : list (gt, ten) hoặc (gt, ten, nhan) — gt trong [trai; phai].
        hien_nhan_diem  : False (mặc định) → KHÔNG ghi giá trị dưới điểm (bài đọc điểm).
        moc_nhan        : list giá trị được ghi nhãn ở vạch (mặc định: chỉ 2 biên trai, phai).

        Máy tự tính toạ độ — AI Soạn khai GIÁ TRỊ (Đ5.9). Nền sạch.
        """
        from fractions import Fraction
        def _toF(v):
            if isinstance(v, Fraction): return v
            if isinstance(v, tuple):    return Fraction(v[0], v[1])
            if isinstance(v, int):      return Fraction(v)
            if isinstance(v, float):    return Fraction(v).limit_denominator(100000)
            if isinstance(v, str):
                s=v.strip().replace(',', '.'); return Fraction(s) if '/' in s else Fraction(s).limit_denominator(100000)
            return Fraction(v)
        self._nen_luoi = False
        qt, qp = _toF(trai), _toF(phai)
        if qt >= qp:
            raise ValueError("[truc_doan_doc_diem] cần trai < phai")
        RONG = 10.0                            # bề rộng vẽ (đơn vị vẽ) — kéo rộng để đọc điểm
        span = float(qp - qt)
        def _X(q): return (float(q) - float(qt)) / span * RONG
        # trục mũi 2 đầu
        self._diem('_dL', -0.5, 0.0, nhan=None, moc=False)
        self._diem('_dR', RONG+0.5, 0.0, nhan=None, moc=False)
        self.tikz.append(('truc2dau','_dL','_dR'))
        # vạch chia nhỏ
        for i in range(chia+1):
            q = qt + (qp-qt)*Fraction(i, chia)
            x = _X(q)
            chinh = (i==0 or i==chia)
            self._vach_ht(x, f'_dv{i}', chinh=chinh)
        # nhãn biên (chỉ 2 đầu, hoặc moc_nhan)
        show = moc_nhan if moc_nhan is not None else [trai, phai]
        for gt in show:
            q=_toF(gt); x=_X(q)
            s=str(gt).replace('.', ',') if not isinstance(gt,str) else gt.replace('.', ',')
            self.ghi_chu(x, -0.42, s)
        # điểm đọc
        for spec in (diem or []):
            gt, ten = spec[0], spec[1]
            nhan = spec[2] if len(spec)>2 else None
            q=_toF(gt)
            if q<qt or q>qp:
                raise ValueError(f"[truc_doan_doc_diem] điểm {gt} ngoài [{trai};{phai}]")
            x=_X(q)
            self._diem(ten, x, 0.0, nhan='above', moc=True)
            if hien_nhan_diem and nhan is not None:
                self.ghi_chu(x, -0.42, str(nhan))
        return self

    def _vach_ht(self, x, tag, chinh=True):
        """Vạch chia dọc trục hữu tỉ: chính (dài) cho số nguyên, phụ (ngắn) cho phần chia."""
        h = 0.13 if chinh else 0.08
        a, b = f'_wa{tag}', f'_wb{tag}'
        self._diem(a, x, h, nhan=None, moc=False)
        self._diem(b, x, -h, nhan=None, moc=False)
        self.tikz.append(('doan', a, b, None, 'lien', 'manh'))

    # ─────────── phụ trợ nội bộ (prefix _ → KHÔNG phơi cho AI Soạn) ───────────
    def _vach(self, x, tag):
        """Vạch chia dọc (nét mảnh) tại hoành độ x; tag = số nguyên đặt tên an toàn."""
        a, b = f'_va{tag}', f'_vb{tag}'
        self._diem(a, x, 0.13, nhan=None, moc=False)
        self._diem(b, x, -0.13, nhan=None, moc=False)
        self.tikz.append(('doan', a, b, None, 'lien', 'manh'))

    def _danh_dau(self, idx, x, gt, ten, hien_gt=False):
        """Chấm điểm tại x + nhãn tên (trên) + giá trị (dưới, nếu hien_gt)."""
        self._diem(f'_pd{idx}', x, 0, nhan=None, moc=True)        # chấm đậm, không nhãn tự động
        if ten:
            self.ghi_chu(x, 0.34, str(ten))                      # nhãn tên — text mode (an toàn dấu/space)
        if hien_gt:
            self.ghi_chu(x, -0.44, self._so(gt))

    @staticmethod
    def _so(v):
        return ('%g' % v).replace('.', ',')


# ═══ [29c] Ông Bụt 2026-09-16 · DS8 Chương 2 (Hằng đẳng thức) ═══
import hinh_core as _HC   # helper render_tikz_doc / _m (generator độc lập)
def hinhDienTichDaiSo(kieu='catghep', nhan=None, chuThich=None,
                      out='dientich_daiso', tra_bytes=False):
    """HÌNH DIỆN TÍCH đại số (nhãn BIẾN, giấu toạ độ). 3 biến thể:
       • 'catghep' : vuông a khoét ô b² → hình L, mũi tên cong → chữ nhật (a+b)(a-b).
                     nhan = {a, b, a_tru_b, a_cong_b}
       • 'chia4'   : vuông (a+b) chia 4 phần P/Q/R/S, đỉnh ABCD. nhan = {a, b, a_cong_b, P,Q,R,S,A,B,C,D}
       • 'vien'    : vuông ngoài x, vuông trong đồng tâm, vành tô, 4 mũi tên bề rộng y.
                     nhan = {ngoai, vien}
       chuThich : caption "Hình N" căn giữa dưới (tuỳ chọn).
    """
    nhan = nhan or {}
    cap = ''
    if chuThich:
        cap = (r'\node[below,font=\itshape] at (CAPX,CAPY) {CAPT};'
               .replace('CAPT', chuThich))

    if kieu == 'catghep':
        a   = _HC._m(nhan.get('a'), 'a')
        b   = _HC._m(nhan.get('b'), 'b')
        amb = _HC._m(nhan.get('a_tru_b'), 'a-b')
        apb = _HC._m(nhan.get('a_cong_b'), 'a+b')
        # a=4, b=1.5 (toạ độ VẼ cố định — giấu trong kho, không lộ ra script AI Soạn)
        cap = cap.replace('CAPX', '5.3').replace('CAPY', '-0.9')
        body = r'''\documentclass[tikz,border=8pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[line join=round, every node/.style={font=\normalsize},
  cA/.style={fill=blue!16}, cB/.style={fill=orange!28}, edge/.style={very thick, black}]
% ---- Hình a: vuông a khoét ô b² góc TRÊN-TRÁI ----
\begin{scope}[shift={(0,0)}]
  \fill[cA] (0,0) rectangle (4,2.5);
  \fill[cA] (1.5,2.5) rectangle (4,4);
  \fill[cB] (0,2.5) rectangle (1.5,4);
  \draw[dashed, thick, black!55] (0,2.5) rectangle (1.5,4);
  \node[black!55] at (0.75,3.25) {$@@B@@$};
  \draw[edge] (0,0) rectangle (4,4);
  \draw[edge] (0,2.5) -- (4,2.5);
  \draw[edge] (1.5,2.5) -- (1.5,4);
  \node[left]  at (0,2)    {$@@A@@$};
  \node[below] at (2,0)    {$@@A@@$};
  \node[above] at (0.75,4) {$@@B@@$};
  \node[above] at (2.75,4) {$@@AMB@@$};
  \node[right] at (4,1.25) {$@@AMB@@$};
\end{scope}
% ---- mũi tên cong ----
\draw[-{Stealth[length=4mm]}, very thick, black!70] (4.55,2.6) to[bend left=28] (6.35,1.9);
% ---- Hình b: chữ nhật (a+b)×(a-b) ----
\begin{scope}[shift={(7,0.75)}]
  \fill[cA] (0,0) rectangle (5.5,2.5);
  \draw[edge] (0,0) rectangle (5.5,2.5);
  \draw[edge] (4,0) -- (4,2.5);
  \node[below] at (2,0)     {$@@A@@$};
  \node[below] at (4.75,0)  {$@@B@@$};
  \node[right] at (5.5,1.25){$@@AMB@@$};
  \node[above] at (2.75,2.5){$@@APB@@$};
\end{scope}
@@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@AMB@@', amb).replace('@@APB@@', apb)
                    .replace('@@A@@', a).replace('@@B@@', b).replace('@@CAP@@', cap))

    elif kieu == 'vien':
        ngoai = _HC._m(nhan.get('ngoai'), 'x')
        vien  = _HC._m(nhan.get('vien'), 'y')
        cap = cap.replace('CAPX', r'\O/2').replace('CAPY', '-0.9')
        body = r'''\documentclass[border=4pt]{standalone}
\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.4mm]},line width=0.5pt,font=\normalsize]
  \def\O{8}\def\w{1.5}
  \fill[green!22, even odd rule] (0,0) rectangle (\O,\O) (\w,\w) rectangle (\O-\w,\O-\w);
  \draw[line width=0.8pt] (0,0) rectangle (\O,\O);
  \draw[line width=0.8pt] (\w,\w) rectangle (\O-\w,\O-\w);
  \draw[<->] (0,\O+0.7) -- (\O,\O+0.7);
  \node[above] at (\O/2,\O+0.7) {$@@NGOAI@@$};
  \draw[<->] (\O/2,\O-\w) -- (\O/2,\O); \node[right] at (\O/2,\O-\w/2) {$@@VIEN@@$};
  \draw[<->] (\O/2,0) -- (\O/2,\w);     \node[right] at (\O/2,\w/2) {$@@VIEN@@$};
  \draw[<->] (0,\O/2) -- (\w,\O/2);     \node[above] at (\w/2,\O/2) {$@@VIEN@@$};
  \draw[<->] (\O-\w,\O/2) -- (\O,\O/2); \node[above] at (\O-\w/2,\O/2) {$@@VIEN@@$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@NGOAI@@', ngoai).replace('@@VIEN@@', vien)
                    .replace('@@CAP@@', cap))

    elif kieu == 'chia4':
        a   = _HC._m(nhan.get('a'), 'a')
        b   = _HC._m(nhan.get('b'), 'b')
        apb = _HC._m(nhan.get('a_cong_b'), 'a+b')
        A = _HC._m(nhan.get('A'), 'A'); B = _HC._m(nhan.get('B'), 'B')
        Cc = _HC._m(nhan.get('C'), 'C'); D = _HC._m(nhan.get('D'), 'D')
        P = _HC._m(nhan.get('P'), 'P'); Q = _HC._m(nhan.get('Q'), 'Q')
        Rr = _HC._m(nhan.get('R'), 'R'); S = _HC._m(nhan.get('S'), 'S')
        # a=3.2, b=1.8 (a+b=5). Đỉnh: A trên-trái, B trên-phải, C dưới-phải, D dưới-trái.
        cap = cap.replace('CAPX', '2.5').replace('CAPY', '-1.35')
        body = r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.6mm]}, every node/.style={font=\normalsize},
  cM/.style={fill=green!20}, edge/.style={very thick, black}]
  \def\a{3.2}\def\b{1.8}\def\s{5}   % s=a+b
  % tô Q (trên-phải) và R (dưới-trái)
  \fill[cM] (\a,\b) rectangle (\s,\s);   % Q: trên-phải  (x>a, y>b)
  \fill[cM] (0,0)  rectangle (\a,\b);    % R: dưới-trái  (x<a, y<b)
  % viền + 2 đường chia
  \draw[edge] (0,0) rectangle (\s,\s);
  \draw[edge] (\a,0) -- (\a,\s);         % đường dọc tại x=a
  \draw[edge] (0,\b) -- (\s,\b);         % đường ngang tại y=b
  % nhãn 4 vùng (P trên-trái, Q trên-phải, R dưới-trái, S dưới-phải)
  \node at ({\a/2},{(\b+\s)/2})      {$@@P@@$};
  \node at ({(\a+\s)/2},{(\b+\s)/2}){$@@Q@@$};
  \node at ({\a/2},{\b/2})            {$@@R@@$};
  \node at ({(\a+\s)/2},{\b/2})      {$@@S@@$};
  % nhãn đỉnh ABCD (ngoài góc)
  \node[above left]  at (0,\s)  {$@@AA@@$};
  \node[above right] at (\s,\s) {$@@BB@@$};
  \node[below right] at (\s,0)  {$@@CC@@$};
  \node[below left]  at (0,0)   {$@@DD@@$};
  % nhãn cạnh trên (a | b) + cạnh trái (a | b)
  \node[above] at ({\a/2},\s)       {$@@a@@$};
  \node[above] at ({(\a+\s)/2},\s) {$@@b@@$};
  \node[left]  at (0,{(\b+\s)/2})  {$@@a@@$};
  \node[left]  at (0,{\b/2})        {$@@b@@$};
  % a+b: mũi tên 2 đầu ngoài cạnh trên & cạnh trái
  \draw[<->] (0,\s+0.7) -- (\s,\s+0.7); \node[above] at ({\s/2},\s+0.7) {$@@APB@@$};
  \draw[<->] (-1.05,0) -- (-1.05,\s);   \node[left] at (-1.05,{\s/2}) [rotate=90,anchor=south] {$@@APB@@$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@APB@@', apb)
                    .replace('@@AA@@', A).replace('@@BB@@', B).replace('@@CC@@', Cc).replace('@@DD@@', D)
                    .replace('@@P@@', P).replace('@@Q@@', Q).replace('@@R@@', Rr).replace('@@S@@', S)
                    .replace('@@a@@', a).replace('@@b@@', b).replace('@@CAP@@', cap))
    else:
        raise ValueError(f"[hinhDienTichDaiSo] kieu='{kieu}' không hợp lệ (catghep|chia4|vien)")

    return _HC.render_tikz_doc(body, out, tra_bytes)

# [29c] gắn làm staticmethod class entry → vào bản trích (sinh_bantrich) + gọi qua instance
Hinh.hinhDienTichDaiSo = staticmethod(hinhDienTichDaiSo)


# ═══ [29y] Ông Bụt 2026-09-21 · DS9 Chương I (Phương trình & hệ hai ẩn) ═══
# MẶT PHẲNG TOẠ ĐỘ Oxy + ĐỒ THỊ ĐƯỜNG THẲNG — generator ĐỘC LẬP (khuôn hinhDienTichDaiSo).
#   KHE HỞ: module đã "đặt nền trục toạ độ (lớp 7→9)" nhưng mới có tia số/trục số 1 chiều;
#   CH1 Toán 9 cần mặt phẳng Oxy + đồ thị đường thẳng (theo PT ax+by=c / 2 điểm) + điểm có
#   nhãn + đường gióng. TikZ dựng gọn, clip trong khung; 0 rủi ro base renderer (Đ như 29c).
#   Toạ độ điểm/PT là GIÁ TRỊ toán học (nội dung bài), không phải toạ độ vẽ thô.
def _mptd_fmt(v):
    return ('%g' % v).replace('.', ',')

def _mptd_abc(d):
    """Chuẩn hoá 1 khai báo đường thẳng về (a,b,c) của a*x+b*y=c."""
    if 'pt' in d:      a, b, c = d['pt']
    elif 'hs' in d:    m, k = d['hs']; a, b, c = -m, 1, k
    elif 'dung' in d:  a, b, c = 1, 0, d['dung']
    elif 'ngang' in d: a, b, c = 0, 1, d['ngang']
    elif 'qua' in d:
        (x1, y1), (x2, y2) = d['qua']
        a, b, c = (y2 - y1), -(x2 - x1), (y2 - y1) * x1 - (x2 - x1) * y1
    else:
        raise ValueError("[hinhMatPhangToaDo] đường thẳng cần 1 trong: pt/hs/dung/ngang/qua")
    return float(a), float(b), float(c)

def _mptd_pts(a, b, c, xr, yr):
    xmin, xmax = xr; ymin, ymax = yr
    if abs(b) < 1e-9:
        x = c / a
        return (x, ymin - 1), (x, ymax + 1), (x, ymax * 0.62)
    f = lambda x: (c - a * x) / b
    xa = xmax * 0.58
    return (xmin - 1, f(xmin - 1)), (xmax + 1, f(xmax + 1)), (xa, f(xa))

def hinhMatPhangToaDo(xRange=(-5, 5), yRange=(-5, 5), buoc=1, luoi=True,
                      duongThang=None, diem=None, chuThich=None,
                      scale=0.72, out='mp_toado', tra_bytes=False):
    """MẶT PHẲNG TOẠ ĐỘ Oxy — trục có mũi tên + nhãn O,x,y; lưới mờ tuỳ chọn; đồ thị ĐƯỜNG
       THẲNG (theo phương trình / 2 điểm) + ĐIỂM có nhãn + đường gióng nét đứt.

       xRange, yRange : (min,max) miền vẽ 2 trục (số nguyên).
       buoc  : bước chia vạch/lưới (mặc định 1).   luoi : True → lưới ô mờ.
       duongThang : list dict, mỗi đường khai 1 trong —
                      pt=(a,b,c) → a x + b y = c  ·  hs=(m,k) → y = m x + k  ·
                      dung=k → x=k  ·  ngang=k → y=k  ·  qua=((x1,y1),(x2,y2)) —
                    kèm nhan (chuỗi, vd 'd_1'), net ('lien'|'dut'), mau (vd 'blue!75'),
                    viTriNhan (anchor TikZ, mặc định 'above right').
       diem  : list dict toa=(x,y) + nhan (vd 'M(1;\\,2)') + viTri (anchor, mặc định
                'above right') + giong (True → gióng nét đứt xuống 2 trục) + mau.
       chuThich : caption 'Hình N' căn giữa dưới.
    """
    duongThang = duongThang or []; diem = diem or []
    xmin, xmax = xRange; ymin, ymax = yRange
    L = [r'\documentclass[tikz,border=6pt]{standalone}',
         r'\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}',
         r'\begin{document}',
         r'\begin{tikzpicture}[scale=%g,>={Stealth[length=2.4mm]},'
         r'line join=round,every node/.style={font=\normalsize}]' % scale]
    if luoi:
        L.append(r'\draw[help lines,gray!35,step=%g] (%g,%g) grid (%g,%g);'
                 % (buoc, xmin, ymin, xmax, ymax))
    L.append(r'\draw[->,thick] (%g,0) -- (%g,0) node[right] {$x$};' % (xmin - 0.4, xmax + 0.7))
    L.append(r'\draw[->,thick] (0,%g) -- (0,%g) node[above] {$y$};' % (ymin - 0.4, ymax + 0.7))
    L.append(r'\node[below left] at (0,0) {$O$};')
    n = xmin
    while n <= xmax + 1e-9:
        if abs(n) > 1e-9:
            L.append(r'\draw (%g,-0.08) -- (%g,0.08);' % (n, n))
            L.append(r'\node[below,font=\footnotesize] at (%g,-0.06) {$%s$};' % (n, _mptd_fmt(n)))
        n += buoc
    n = ymin
    while n <= ymax + 1e-9:
        if abs(n) > 1e-9:
            L.append(r'\draw (-0.08,%g) -- (0.08,%g);' % (n, n))
            L.append(r'\node[left,font=\footnotesize] at (-0.08,%g) {$%s$};' % (n, _mptd_fmt(n)))
        n += buoc
    for d in duongThang:
        a, b, c = _mptd_abc(d)
        (px1, py1), (px2, py2), (lx, ly) = _mptd_pts(a, b, c, xRange, yRange)
        net = 'dashed' if d.get('net') == 'dut' else 'solid'
        mau = d.get('mau', 'blue!75')
        L.append(r'\begin{scope}\clip (%g,%g) rectangle (%g,%g);' % (xmin, ymin, xmax, ymax))
        L.append(r'\draw[very thick,%s,%s] (%g,%g) -- (%g,%g);' % (mau, net, px1, py1, px2, py2))
        L.append(r'\end{scope}')
        if d.get('nhan'):
            L.append(r'\node[%s,%s,font=\small] at (%g,%g) {$%s$};'
                     % (d.get('viTriNhan', 'above right'), mau, lx, ly, d['nhan']))
    for p in diem:
        x, y = p['toa']; mau = p.get('mau', 'black')
        if p.get('giong'):
            L.append(r'\draw[dashed,gray!70] (%g,%g) -- (%g,0);' % (x, y, x))
            L.append(r'\draw[dashed,gray!70] (%g,%g) -- (0,%g);' % (x, y, y))
        L.append(r'\fill[%s] (%g,%g) circle (2.2pt);' % (mau, x, y))
        if p.get('nhan'):
            L.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};'
                     % (p.get('viTri', 'above right'), x, y, p['nhan']))
    if chuThich:
        L.append(r'\node[below,font=\itshape] at (%g,%g) {%s};'
                 % ((xmin + xmax) / 2.0, ymin - 1.0, chuThich))
    L.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(L), out, tra_bytes)

# [29y] gắn làm staticmethod class entry → vào bản trích (sinh_bantrich) + gọi qua instance
Hinh.hinhMatPhangToaDo = staticmethod(hinhMatPhangToaDo)
