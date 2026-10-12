#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_toado.py — PRIMITIVE TOẠ ĐỘ (DÙNG CHUNG Hình ↔ Đại số)
#   Tách từ hinh_daiso.py [B1, 30a] để primitive cross-cutting (tia số, trục số,
#   mặt phẳng toạ độ, cắm điểm) không bị giam trong silo "daiso".
#   class Hinh(HinhCoBan): compose thuần từ base. Đại số/Hình đều KẾ THỪA lại,
#   GỌI LẠI — cấm viết mới vùng này (Quy ước sửa kho §1-2).
#   Triết lý Đ5.9: khai GIÁ TRỊ ngữ nghĩa → máy tự tính toạ độ → PHANH kiểm. CS2627.
# ═══════════════════════════════════════════════════════════════════
from hinh_coban import HinhCoBan
import hinh_core as _HC   # render_tikz_doc cho generator độc lập


class Hinh(HinhCoBan):
    """Primitive toạ độ dùng chung — tia số, trục số, mặt phẳng toạ độ. Kế thừa base HinhCoBan."""

    def tia_diem(self, *args, **kwargs):
        """[Đại số] sơ đồ điểm trên đường thẳng — NỀN SẠCH (base hinh_coban mặc định có lưới)."""
        self._nen_luoi = False
        return super().tia_diem(*args, **kwargs)

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

    def truc_so_huu_ti(self, tu=-1, den=4, chia=1, diem=None,
                       hien_nhan_diem=True, moc_nhan=None,
                       mui_ten_am=False, goc_ten='0',
                       khoang_to=None, vach_dut=None, mui_ten_dc=None, ti_le=True):
        """TRỤC SỐ biểu diễn số hữu tỉ — gốc O ở giá trị 0, có phần âm & dương.

        ti_le          : True (mặc định) khoảng cách ĐÚNG tỉ lệ (hành vi cũ, 0 regression).
                         False → các ĐIỂM trong `diem` xếp cách đều DANH NGHĨA theo thứ tự
                         giá trị (giữ gốc 0 + mốc tu/den định hướng) — dùng cho dãy/giá trị
                         HỘI TỤ (vd uₙ=(-1)ⁿ/2ⁿ) để nhãn không chồng. Chỉ nhận `diem`
                         (bỏ khoang_to/vach_dut/mui_ten_dc). Caption ghi "(không theo tỉ lệ)".

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

        # ══ CHẾ ĐỘ GIÃN ĐỀU (ti_le=False) — minh họa dãy/giá trị HỘI TỤ, nhãn không chồng ══
        if not ti_le:
            if not diem:
                raise ValueError("[truc_so_huu_ti] ti_le=False cần danh sách 'diem'")
            if khoang_to or vach_dut or mui_ten_dc:
                raise ValueError("[truc_so_huu_ti] ti_le=False chỉ hỗ trợ 'diem' "
                                 "(bỏ khoang_to/vach_dut/mui_ten_dc)")
            KHOANG = 1.7
            anchors = []                               # (q, loai, idx, ten, nhan)
            for idx, spec in enumerate(diem):
                gt, ten = spec[0], spec[1]
                nhan = spec[2] if len(spec) > 2 else 'auto'
                q = _toFrac(gt)
                if q < tu or q > den:
                    raise ValueError(f"[truc_so_huu_ti] điểm {gt} ngoài đoạn [{tu}, {den}]")
                anchors.append((q, 'diem', idx, ten, nhan))
            co = {a[0] for a in anchors}
            for mv in (tu, 0, den):                    # mốc nguyên định hướng (gốc 0 + ±biên)
                qv = _toFrac(mv)
                if qv not in co:
                    anchors.append((qv, 'moc', None, None, None))
                    co.add(qv)
            anchors.sort(key=lambda t: t[0])
            xs = [i * KHOANG for i in range(len(anchors))]
            xL, xR = xs[0] - 0.7, xs[-1] + 0.7
            self._diem('_haL', xL, 0.0, nhan=None, moc=False)
            self._diem('_haR', xR, 0.0, nhan=None, moc=False)
            self.tikz.append(('tia', '_haL', '_haR', True, None, 'lien'))   # mũi phải
            if mui_ten_am:
                self.tikz.append(('tia', '_haR', '_haL', True, None, 'lien'))
            for (q, loai, idx, ten, nhan), x in zip(anchors, xs):
                if loai == 'moc':
                    self._vach_ht(x, f'm{int(q) - tu}', chinh=True)
                    self.ghi_chu(x, -0.44, goc_ten if q == 0 else self._so(int(q)))
                else:
                    self._diem(f'hp{idx}', x, 0.0, nhan=None, moc=True)      # chấm đậm
                    if ten:
                        self.ghi_chu(x, 0.34, str(ten))                      # nhãn tên (trên)
                    if hien_nhan_diem and nhan is not None:
                        self.ghi_chu(x, -0.44, _nhan_frac(q) if nhan == 'auto' else str(nhan))
            self.ghi_chu(xs[0] - 0.30, 0.30, '')
            return self

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
            self._diem(f'hp{idx}', x, 0.0, nhan=None, moc=True)     # chấm đậm
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

        # ── MŨI TÊN DI CHUYỂN (mô phỏng cộng/trừ: chuỗi cung có hướng, KHÔNG ghi kết quả — Đ35) ──
        for seg in (mui_ten_dc or []):
            a_v, b_v = _toFrac(seg[0]), _toFrac(seg[1])
            for qq in (a_v, b_v):
                if qq < tu or qq > den:
                    raise ValueError(f"[truc_so_huu_ti] mui_ten_dc {seg} ngoài đoạn [{tu}, {den}]")
            self.tikz.append(('nhay', float(a_v) * SCALE, float(b_v) * SCALE, None))

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

    def nhiet_ke_cot(self, cot, thang=(-20, 50), buoc=10, don_vi='\u00b0C',
                     hien_muc_so=False):
        """NHIET KE COT \u2014 nhieu thang do DUNG canh nhau, doc muc thuy ngan.

        cot         : list (ten, muc) \u2014 moi nhiet ke: ten = nhan duoi cot (rong \u2192 khong ghi);
                      muc = muc thuy ngan (nguyen, theo don vi thang).
        thang       : (min, max) bien thang chia (nguyen), min < max.
        buoc        : moi vach chinh ung bao nhieu don vi; chia het (max-min).
        don_vi      : chuoi don vi ghi o dau moi thang ('\u00b0C').
        hien_muc_so : False (mac dinh) \u2192 KHONG ghi so tai dinh cot (muc la cai HS doc, \u110435);
                      True \u2192 ghi (dung cho loi giai).

        May tu tinh toa do tu GIA TRI \u2014 AI Soan chi khai cot/thang/buoc (\u11045.9).
        """
        tmin, tmax = thang
        # \u2500\u2500 PHANH kiem (\u11045.9) \u2500\u2500
        if not (isinstance(tmin, int) and isinstance(tmax, int)) or tmin >= tmax:
            raise ValueError("[nhiet_ke_cot] thang can (min,max) NGUYEN va min < max")
        if not isinstance(buoc, int) or buoc < 1:
            raise ValueError("[nhiet_ke_cot] buoc phai NGUYEN >= 1")
        if (tmax - tmin) % buoc != 0:
            raise ValueError(f"[nhiet_ke_cot] buoc {buoc} khong chia het khoang [{tmin},{tmax}]")
        cot = list(cot or [])
        if not cot:
            raise ValueError("[nhiet_ke_cot] can it nhat mot cot (ten, muc)")
        self._nen_luoi = False

        VY = 0.55 / buoc          # don vi ve tren moi 1 don vi thang
        W = 0.40                  # be rong ong
        PITCH = 1.55              # khoang cach tam hai nhiet ke
        INSET = 0.06              # thuy ngan thut vao so voi thanh ong
        y0 = 0.0
        yTop = (tmax - tmin) * VY
        dv = str(don_vi).replace('\u00b0', r'$^\circ$')   # \u00b0 \u2192 math cho TikZ

        for i, spec in enumerate(cot):
            ten, muc = spec[0], spec[1]
            if not isinstance(muc, int):
                raise ValueError(f"[nhiet_ke_cot] muc cot {i+1} phai NGUYEN")
            if muc < tmin or muc > tmax:
                raise ValueError(f"[nhiet_ke_cot] muc {muc} ngoai thang [{tmin},{tmax}]")
            xL = i * PITCH; xR = xL + W; xC = (xL + xR) / 2
            ymuc = (muc - tmin) * VY
            p = f'nk{i}_'
            # ong: hai thanh + nap tren
            self._diem(p+'bl', xL, y0, nhan=None, moc=False)
            self._diem(p+'tl', xL, yTop + 0.14, nhan=None, moc=False)
            self._diem(p+'br', xR, y0, nhan=None, moc=False)
            self._diem(p+'tr', xR, yTop + 0.14, nhan=None, moc=False)
            self.tikz.append(('doan', p+'bl', p+'tl', None, 'lien', 'manh'))
            self.tikz.append(('doan', p+'br', p+'tr', None, 'lien', 'manh'))
            self.tikz.append(('doan', p+'tl', p+'tr', None, 'lien', 'manh'))
            # bau chua (day) + cot thuy ngan do
            self._diem(p+'gbl', xL - 0.12, y0 - 0.34, nhan=None, moc=False)
            self._diem(p+'gbr', xR + 0.12, y0 - 0.34, nhan=None, moc=False)
            self._diem(p+'gtr', xR + 0.12, y0, nhan=None, moc=False)
            self._diem(p+'gtl', xL - 0.12, y0, nhan=None, moc=False)
            self.to_mien(p+'gbl', p+'gbr', p+'gtr', p+'gtl', mau='red!85')
            self._diem(p+'mbl', xL + INSET, y0, nhan=None, moc=False)
            self._diem(p+'mbr', xR - INSET, y0, nhan=None, moc=False)
            self._diem(p+'mtr', xR - INSET, ymuc, nhan=None, moc=False)
            self._diem(p+'mtl', xL + INSET, ymuc, nhan=None, moc=False)
            self.to_mien(p+'mbl', p+'mbr', p+'mtr', p+'mtl', mau='red!85')
            # vach chinh + so (trai ong), max o tren xuong min
            v = tmin
            while v <= tmax:
                yv = (v - tmin) * VY
                a, b = f'{p}wa{v-tmin}', f'{p}wb{v-tmin}'
                self._diem(a, xL - 0.14, yv, nhan=None, moc=False)
                self._diem(b, xL, yv, nhan=None, moc=False)
                self.tikz.append(('doan', a, b, None, 'lien', 'manh'))
                self.ghi_chu(xL - 0.42, yv, self._so(v))
                v += buoc
            # don vi dau thang + nhan cot + so muc (tuy chon)
            self.ghi_chu(xR + 0.26, yTop + 0.12, dv)
            if ten:
                self.ghi_chu(xC, y0 - 0.60, str(ten))
            if hien_muc_so:
                self.ghi_chu(xR + 0.32, ymuc, self._so(muc))
        return self

    def kim_tu_thap(self, hang, o_canh=0.95):
        """KIM TỰ THÁP SỐ (2D) — tháp ô vuông, ô trên gối lệch nửa ô giữa 2 ô dưới.
        Dùng cho bài "điền tháp" (ô trên = tích/tổng 2 ô dưới). CHỈ VẼ tháp + số/ô-trống;
        KHÔNG tự tính (HS điền). Đây KHÔNG phải hình chóp không gian 3D (đó là hàm khác).

        hang    : list các hàng TỪ ĐỈNH XUỐNG ĐÁY. Hàng k có k+1 ô (đỉnh 1 ô → đáy nhiều ô nhất).
                  Mỗi ô: số | chuỗi (vd '?' cho ô cần điền) | '' (ô rỗng). Ví dụ B16:
                  [['?'], ['?','?'], [-1,'?',1], [-1,'?','?',-1]].
        o_canh  : cạnh ô vuông (đơn vị vẽ).
        """
        hang = [list(r) for r in (hang or [])]
        # ── PHANH kiểm ──
        if not hang:
            raise ValueError("[kim_tu_thap] cần ít nhất 1 hàng")
        for k, r in enumerate(hang):
            if len(r) != k + 1:
                raise ValueError(f"[kim_tu_thap] hàng {k+1} phải có {k+1} ô (từ đỉnh xuống: 1,2,3,…), đang có {len(r)}")
        self._nen_luoi = False
        C = float(o_canh)
        for k, row in enumerate(hang):
            n = len(row)
            yT = -k * C
            yB = yT - C
            xL0 = -(n * C) / 2.0
            for j, val in enumerate(row):
                xL = xL0 + j * C
                xR = xL + C
                p = f'kt{k}_{j}_'
                self._diem(p+'tl', xL, yT, nhan=None, moc=False)
                self._diem(p+'tr', xR, yT, nhan=None, moc=False)
                self._diem(p+'br', xR, yB, nhan=None, moc=False)
                self._diem(p+'bl', xL, yB, nhan=None, moc=False)
                self.tikz.append(('doan', p+'tl', p+'tr', None, 'lien', 'manh'))
                self.tikz.append(('doan', p+'tr', p+'br', None, 'lien', 'manh'))
                self.tikz.append(('doan', p+'br', p+'bl', None, 'lien', 'manh'))
                self.tikz.append(('doan', p+'bl', p+'tl', None, 'lien', 'manh'))
                s = '' if val is None else (self._so(val) if isinstance(val, (int, float)) else str(val))
                if s != '':
                    self.ghi_chu((xL + xR) / 2.0, (yT + yB) / 2.0, s)
        return self

    def _vach_ht(self, x, tag, chinh=True):
        """Vạch chia dọc trục hữu tỉ: chính (dài) cho số nguyên, phụ (ngắn) cho phần chia."""
        h = 0.13 if chinh else 0.08
        a, b = f'_wa{tag}', f'_wb{tag}'
        self._diem(a, x, h, nhan=None, moc=False)
        self._diem(b, x, -h, nhan=None, moc=False)
        self.tikz.append(('doan', a, b, None, 'lien', 'manh'))

    def _vach(self, x, tag):
        """Vạch chia dọc (nét mảnh) tại hoành độ x; tag = số nguyên đặt tên an toàn."""
        a, b = f'_va{tag}', f'_vb{tag}'
        self._diem(a, x, 0.13, nhan=None, moc=False)
        self._diem(b, x, -0.13, nhan=None, moc=False)
        self.tikz.append(('doan', a, b, None, 'lien', 'manh'))

    def _danh_dau(self, idx, x, gt, ten, hien_gt=False):
        """Chấm điểm tại x + nhãn tên (trên) + giá trị (dưới, nếu hien_gt)."""
        self._diem(f'pd{idx}', x, 0, nhan=None, moc=True)        # chấm đậm, không nhãn tự động
        if ten:
            self.ghi_chu(x, 0.34, str(ten))                      # nhãn tên — text mode (an toàn dấu/space)
        if hien_gt:
            self.ghi_chu(x, -0.44, self._so(gt))

    @staticmethod
    def _so(v):
        return ('%g' % v).replace('.', ',')


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


# ── [32t] G1 cungGoc + G2 chanVuongGoc — primitive góc & khoảng cách trên Oxy (HH10 CH7 B20) ──
import math as _math

def _mptd_giao2dt(d1, d2):
    """Giao điểm 2 đường thẳng (a*x+b*y=c). None nếu song song/trùng."""
    a1, b1, c1 = _mptd_abc(d1); a2, b2, c2 = _mptd_abc(d2)
    det = a1 * b2 - a2 * b1
    if abs(det) < 1e-9:
        return None
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)

def _mptd_huong_dt(d):
    """Vectơ chỉ phương (đã chuẩn hoá) của đường thẳng a*x+b*y=c → (b,-a)."""
    a, b, c = _mptd_abc(d)
    ux, uy = b, -a
    n = _math.hypot(ux, uy) or 1.0
    return ux / n, uy / n

def _mptd_goc_deg(ux, uy):
    return _math.degrees(_math.atan2(uy, ux))

def _mptd_cung_tikz(vx, vy, ang1, ang2, r, mau, nhan=None, ang_nhan=None, r_nhan=None):
    """Sinh lệnh TikZ: cung từ ang1→ang2 (độ) bán kính r quanh (vx,vy) + nhãn (tuỳ)."""
    out = []
    sx = vx + r * _math.cos(_math.radians(ang1)); sy = vy + r * _math.sin(_math.radians(ang1))
    out.append(r'\draw[%s,thick] (%g,%g) arc[start angle=%g, end angle=%g, radius=%g];'
               % (mau, sx, sy, ang1, ang2, r))
    if nhan:
        am = ang_nhan if ang_nhan is not None else (ang1 + ang2) / 2.0
        rn = r_nhan if r_nhan is not None else r + 0.33
        lx = vx + rn * _math.cos(_math.radians(am)); ly = vy + rn * _math.sin(_math.radians(am))
        out.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};' % (mau, lx, ly, nhan))
    return out

def _mptd_cung_goc(cg, duongThang, vecto):
    """Cung góc giữa 2 phương (dt↔dt hoặc vt↔vt). Trả list lệnh TikZ.
       cg: {giua:[('dt',i),('dt',j)] | [('vt',i),('vt',j)], nhan?, boSung4Goc?, mau?, banKinh?}
    """
    giua = cg['giua']
    if len(giua) != 2:
        raise ValueError("[cungGoc] 'giua' cần đúng 2 phương (dt hoặc vt).")
    (k1, i1), (k2, i2) = giua
    mau = cg.get('mau', 'black'); r = cg.get('banKinh', 0.7); nhan = cg.get('nhan')
    if k1 == 'dt' and k2 == 'dt':
        v = _mptd_giao2dt(duongThang[i1], duongThang[i2])
        if v is None:
            raise ValueError("[cungGoc] hai đường thẳng song song/trùng — không có góc để vẽ.")
        vx, vy = v
        a1 = _mptd_goc_deg(*_mptd_huong_dt(duongThang[i1]))
        a2 = _mptd_goc_deg(*_mptd_huong_dt(duongThang[i2]))
        if cg.get('boSung4Goc'):
            # 4 tia biên: a1, a2, a1+180, a2+180 → 4 cung TÁCH RỜI (chừa khe) để đọc ra 4 góc
            rays = sorted((x % 360) for x in (a1, a2, a1 + 180, a2 + 180))
            out = []
            rr = cg.get('banKinh', 0.42); khe = cg.get('khe', 15)
            for t in range(4):
                s = rays[t]; e = rays[(t + 1) % 4]
                if e <= s:
                    e += 360
                out += _mptd_cung_tikz(vx, vy, s + khe, e - khe, rr, mau)
            return out
        # 1 cung góc KHÔNG tù: trong 4 tia (2 của mỗi đt), chọn cặp có góc nhỏ nhất,
        # vẽ theo hướng ngắn (signed) → đúng góc nhọn giữa 2 đường thẳng (SGK: góc không tù).
        cands = []
        for r1 in (a1 % 360, (a1 + 180) % 360):
            for r2 in (a2 % 360, (a2 + 180) % 360):
                dsw = (r2 - r1) % 360
                if dsw > 180:
                    dsw -= 360
                cands.append((abs(dsw), r1, dsw))
        cands.sort()
        _, r1, dsw = cands[0]
        mid = r1 + dsw / 2.0
        return _mptd_cung_tikz(vx, vy, r1, r1 + dsw, r, mau, nhan, ang_nhan=mid)
    elif k1 == 'vt' and k2 == 'vt':
        v1 = vecto[i1]; v2 = vecto[i2]
        vx, vy = v1['tu']
        d1 = (v1['den'][0] - v1['tu'][0], v1['den'][1] - v1['tu'][1])
        d2 = (v2['den'][0] - v2['tu'][0], v2['den'][1] - v2['tu'][1])
        a1 = _mptd_goc_deg(*d1); a2 = _mptd_goc_deg(*d2)
        sweep = (a2 - a1) % 360
        if sweep > 180:
            sweep -= 360          # vẽ cung ≤180 (góc giữa 2 vectơ)
        return _mptd_cung_tikz(vx, vy, a1, a1 + sweep, r, mau, nhan)
    else:
        raise ValueError("[cungGoc] chỉ hỗ trợ dt↔dt hoặc vt↔vt (không trộn).")

def _mptd_chan_vuong(cv, diem, duongThang):
    """Chân vuông góc H = hình chiếu điểm lên đường thẳng + ô vuông + đoạn. List lệnh TikZ.
       cv: {tuDiem:i, denDuong:j, nhanChan?, oVuong?, veDoan?, net?, mau?}
    """
    M = diem[cv['tuDiem']]['toa']; a, b, c = _mptd_abc(duongThang[cv['denDuong']])
    mx, my = M
    t = (a * mx + b * my - c) / (a * a + b * b)
    hx, hy = mx - a * t, my - b * t
    dist = abs(t) * _math.hypot(a, b)
    if dist < 1e-9:
        raise ValueError("[chanVuongGoc] điểm nằm TRÊN đường thẳng — không có đoạn khoảng cách.")
    mau = cv.get('mau', 'gray!75')
    net = 'dashed' if cv.get('net', 'dut') == 'dut' else 'solid'
    out = []
    if cv.get('veDoan', True):
        out.append(r'\draw[%s,%s,thick] (%g,%g) -- (%g,%g);' % (mau, net, mx, my, hx, hy))
    if cv.get('oVuong', True):
        s = 0.3
        e1x, e1y = b / _math.hypot(a, b), -a / _math.hypot(a, b)     # phương đt
        e2x, e2y = (mx - hx) / dist, (my - hy) / dist                 # phương H→M
        p1 = (hx + s * e1x, hy + s * e1y)
        p2 = (hx + s * e2x, hy + s * e2y)
        pc = (hx + s * e1x + s * e2x, hy + s * e1y + s * e2y)
        out.append(r'\draw[%s] (%g,%g) -- (%g,%g) -- (%g,%g);'
                   % (mau, p1[0], p1[1], pc[0], pc[1], p2[0], p2[1]))
    out.append(r'\fill[black] (%g,%g) circle (2.2pt);' % (hx, hy))
    if cv.get('nhanChan'):
        out.append(r'\node[below right,font=\small] at (%g,%g) {$%s$};'
                   % (hx, hy, cv['nhanChan']))
    return out


# ── [32u] V1 ĐƯỜNG TRÒN trên Oxy (HH10 CH7 B21) — duongTron + tiepTuyen + doan ──
def _mptd_duong_tron(dt):
    """Đường tròn tâm (a,b) bán kính R trên Oxy (+ tâm, nhãn). List lệnh TikZ.
       dt: {tam:(a,b), R, nhan?:'(C)', mau?, net?, veTam?, nhanTam?:'I', viTriNhan?}
    """
    (a, b) = dt['tam']; R = dt['R']
    if R <= 0:
        raise ValueError("[duongTron] bán kính R phải > 0.")
    mau = dt.get('mau', 'blue!70')
    net = 'dashed' if dt.get('net') == 'dut' else 'solid'
    out = [r'\draw[very thick,%s,%s] (%g,%g) circle (%g);' % (mau, net, a, b, R)]
    if dt.get('veTam', True):
        out.append(r'\fill[%s] (%g,%g) circle (2.2pt);' % (mau, a, b))
        if dt.get('nhanTam'):
            out.append(r'\node[below left,font=\small] at (%g,%g) {$%s$};'
                       % (a, b, dt['nhanTam']))
    if dt.get('nhan'):
        # nhãn (C) đặt trên rìa trên-phải đường tròn
        lx = a + R * 0.707; ly = b + R * 0.707
        out.append(r'\node[%s,%s,font=\small] at (%g,%g) {$%s$};'
                   % (dt.get('viTriNhan', 'above right'), mau, lx, ly, dt['nhan']))
    return out

def _mptd_tiep_tuyen(tt, duongTron):
    """Tiếp tuyến tại điểm M THUỘC đường tròn (idx trong duongTron): máy tự tính
       đường ⊥ bán kính IM tại M + (tuỳ) vẽ bán kính + ô vuông. Đ5.9. List lệnh TikZ.
       tt: {tron:idx, diem:(x0,y0), nhanDiem?:'M', veBanKinh?:True, oVuong?:True,
            nhan?:'\\Delta', mau?, daiNua?:2.6}
    """
    dt = duongTron[tt['tron']]; (a, b) = dt['tam']; R = dt['R']
    (mx, my) = tt['diem']
    d = _math.hypot(mx - a, my - b)
    if abs(d - R) > 1e-6 * max(1.0, R):
        raise ValueError("[tiepTuyen] điểm không thuộc đường tròn (|IM| ≠ R).")
    mau = tt.get('mau', 'red!75')
    # phương bán kính IM (đơn vị) + phương tiếp tuyến (vuông góc)
    rx, ry = (mx - a) / d, (my - b) / d
    tx, ty = -ry, rx
    L = tt.get('daiNua', 2.6)
    out = []
    # tiếp tuyến: đoạn qua M theo phương (tx,ty)
    out.append(r'\draw[very thick,%s] (%g,%g) -- (%g,%g);'
               % (mau, mx - L * tx, my - L * ty, mx + L * tx, my + L * ty))
    if tt.get('veBanKinh', True):
        out.append(r'\draw[thick,gray!80] (%g,%g) -- (%g,%g);' % (a, b, mx, my))
    if tt.get('oVuong', True):
        s = 0.3
        p1 = (mx + s * tx, my + s * ty)            # dọc tiếp tuyến
        p2 = (mx - s * rx, my - s * ry)            # dọc bán kính (M→I)
        pc = (mx + s * tx - s * rx, my + s * ty - s * ry)
        out.append(r'\draw[%s] (%g,%g) -- (%g,%g) -- (%g,%g);'
                   % (mau, p1[0], p1[1], pc[0], pc[1], p2[0], p2[1]))
    out.append(r'\fill[black] (%g,%g) circle (2.2pt);' % (mx, my))
    if tt.get('nhanDiem'):
        out.append(r'\node[above right,font=\small] at (%g,%g) {$%s$};' % (mx, my, tt['nhanDiem']))
    if tt.get('nhan'):
        out.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};'
                   % (mau, mx + L * tx * 0.8, my + L * ty * 0.8, tt['nhan']))
    return out

def _mptd_doan(dn):
    """Đoạn thẳng tu→den + nhãn (không mũi tên). dn: {tu,den,nhan?,net?,mau?,viTriNhan?}"""
    (x1, y1) = dn['tu']; (x2, y2) = dn['den']
    mau = dn.get('mau', 'black'); net = 'dashed' if dn.get('net') == 'dut' else 'solid'
    out = [r'\draw[thick,%s,%s] (%g,%g) -- (%g,%g);' % (mau, net, x1, y1, x2, y2)]
    if dn.get('nhan'):
        out.append(r'\node[%s,%s,font=\small] at (%g,%g) {$%s$};'
                   % (dn.get('viTriNhan', 'above'), mau, (x1 + x2) / 2.0, (y1 + y2) / 2.0, dn['nhan']))
    return out


# ── [32v] V2–V4 BA CONIC trên Oxy (HH10 CH7 B22) — elip + hypebol + parabol ──
def _mptd_tieu_diem(out, c, nhanTD, mau):
    """Chấm 2 tiêu điểm (±c;0) + nhãn (nhanTD = (nhãn trái, nhãn phải))."""
    for sx, nh in ((-c, nhanTD[0] if nhanTD else None), (c, nhanTD[1] if nhanTD else None)):
        out.append(r'\fill[%s] (%g,0) circle (2.2pt);' % (mau, sx))
        if nh:
            out.append(r'\node[below,font=\small] at (%g,-0.08) {$%s$};' % (sx, nh))

def _mptd_elip(el, xRange, yRange):
    """Elip x²/a² + y²/b² = 1 (tâm mặc định O). PT chính tắc a>b>0 (tiêu điểm trên Ox).
       el: {a, b, tam?:(0,0), veTieuDiem?, nhanTieuDiem?:('F_1','F_2'), nua?:'tren'|'duoi',
            nhan?:'(E)', mau?, net?, veTruc?}
    """
    a = el['a']; b = el['b']
    if a <= 0 or b <= 0:
        raise ValueError("[elip] a, b phải > 0.")
    cx, cy = el.get('tam', (0, 0))
    mau = el.get('mau', 'blue!70'); net = 'dashed' if el.get('net') == 'dut' else 'solid'
    out = []
    nua = el.get('nua')
    if nua == 'tren':
        out.append(r'\draw[very thick,%s,%s] (%g,%g) arc[start angle=0, end angle=180, x radius=%g, y radius=%g];'
                   % (mau, net, cx + a, cy, a, b))
    elif nua == 'duoi':
        out.append(r'\draw[very thick,%s,%s] (%g,%g) arc[start angle=0, end angle=-180, x radius=%g, y radius=%g];'
                   % (mau, net, cx + a, cy, a, b))
    else:
        out.append(r'\draw[very thick,%s,%s] (%g,%g) ellipse (%g and %g);' % (mau, net, cx, cy, a, b))
    if el.get('veTieuDiem') and cx == 0 and cy == 0 and a > b:
        import math as _m
        c = _m.sqrt(a * a - b * b)
        _mptd_tieu_diem(out, c, el.get('nhanTieuDiem'), mau)
    if el.get('nhan'):
        out.append(r'\node[%s,%s,font=\small] at (%g,%g) {$%s$};'
                   % (el.get('viTriNhan', 'above right'), mau, cx + a * 0.72, cy + b * 0.72, el['nhan']))
    return out

def _mptd_hypebol(hy, xRange, yRange):
    """Hypebol x²/a² − y²/b² = 1 (2 nhánh trái/phải, tiêu điểm trên Ox).
       hy: {a, b, veTieuDiem?, nhanTieuDiem?, nhan?:'(H)', mau?, net?, samples?}
    """
    a = hy['a']; b = hy['b']
    if a <= 0 or b <= 0:
        raise ValueError("[hypebol] a, b phải > 0.")
    xmin, xmax = xRange; ymin, ymax = yRange
    mau = hy.get('mau', 'blue!70'); net = 'dashed' if hy.get('net') == 'dut' else 'solid'
    xr = max(abs(xmin), abs(xmax))
    out = [r'\begin{scope}\clip (%g,%g) rectangle (%g,%g);' % (xmin, ymin, xmax, ymax)]
    # mỗi nhánh: y = ± b·√(x²/a² − 1); nhánh phải x∈[a, xr], nhánh trái x∈[−xr, −a]
    for dom in ('%g:%g' % (a, xr + 0.5), '%g:%g' % (-(xr + 0.5), -a)):
        out.append(r'\draw[very thick,%s,%s,samples=60,domain=%s] plot ({\x},{%g*sqrt((\x*\x)/(%g)-1)});'
                   % (mau, net, dom, b, a * a))
        out.append(r'\draw[very thick,%s,%s,samples=60,domain=%s] plot ({\x},{-%g*sqrt((\x*\x)/(%g)-1)});'
                   % (mau, net, dom, b, a * a))
    out.append(r'\end{scope}')
    if hy.get('veTieuDiem'):
        import math as _m
        c = _m.sqrt(a * a + b * b)
        _mptd_tieu_diem(out, c, hy.get('nhanTieuDiem'), mau)
    if hy.get('nhan'):
        out.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};'
                   % (mau, a + 0.5, b * 0.9 + 0.3, hy['nhan']))
    return out

def _mptd_parabol(pr, xRange, yRange):
    """Parabol y² = 2px (p>0, mở sang phải), tiêu điểm F(p/2;0), đường chuẩn x=−p/2.
       pr: {p, veTieuDiem?, nhanTieuDiem?:'F', veDuongChuan?, nhanChuan?:'\\Delta',
            nhan?:'(P)', mau?, net?}
    """
    p = pr['p']
    if p <= 0:
        raise ValueError("[parabol] p phải > 0.")
    xmin, xmax = xRange; ymin, ymax = yRange
    mau = pr.get('mau', 'blue!70'); net = 'dashed' if pr.get('net') == 'dut' else 'solid'
    ym = max(abs(ymin), abs(ymax))
    out = [r'\begin{scope}\clip (%g,%g) rectangle (%g,%g);' % (xmin, ymin, xmax, ymax)]
    out.append(r'\draw[very thick,%s,%s,samples=80,domain=%g:%g] plot ({(\x*\x)/(%g)},{\x});'
               % (mau, net, -(ym + 0.5), ym + 0.5, 2.0 * p))
    out.append(r'\end{scope}')
    if pr.get('veTieuDiem'):
        out.append(r'\fill[%s] (%g,0) circle (2.2pt);' % (mau, p / 2.0))
        out.append(r'\node[below right,font=\small] at (%g,0) {$%s$};' % (p / 2.0, pr.get('nhanTieuDiem', 'F')))
    if pr.get('veDuongChuan'):
        out.append(r'\draw[very thick,red!70,%s] (%g,%g) -- (%g,%g);' % (net, -p / 2.0, ymin, -p / 2.0, ymax))
        out.append(r'\node[red!70,above,font=\small] at (%g,%g) {$%s$};'
                   % (-p / 2.0, ymax - 0.5, pr.get('nhanChuan', '\\Delta')))
    if pr.get('nhan'):
        out.append(r'\node[%s,font=\small] at (%g,%g) {$%s$};'
                   % (mau, (ym * ym) / (2.0 * p) * 0.6, ym * 0.75, pr['nhan']))
    return out


def hinhMatPhangToaDo(xRange=(-5, 5), yRange=(-5, 5), buoc=1, luoi=True,
                      duongThang=None, diem=None, vecto=None, chuThich=None,
                      cungGoc=None, chanVuongGoc=None,
                      duongTron=None, tiepTuyen=None, doan=None,
                      elip=None, hypebol=None, parabol=None,
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
       vecto : [CH04] list dict tu=(x,y) + den=(x,y) + nhan ('\\vec a' | '\\overrightarrow{OM}')
                + mau (mặc định 'red!80') + net ('lien'|'dut') + viTriNhan (anchor, 'above left').
                Mũi tên ĐÚNG tu→den (vectơ trong hệ trục — B10/B11 tọa độ).
       cungGoc : [32t] list dict — cung góc giữa 2 PHƯƠNG trên Oxy. Mỗi dict:
                 {giua:[('dt',i),('dt',j)]  (góc giữa 2 đường thẳng, index trong duongThang)
                   | [('vt',i),('vt',j)]    (góc giữa 2 vectơ, index trong vecto),
                  nhan?:'\\varphi' (nhãn góc), boSung4Goc?:False (True → đánh dấu cả 4 góc,
                  cho H7.6), mau?:'black', banKinh?:0.7}. Máy TỰ tính giao điểm (dt↔dt)
                  hoặc gốc chung (vt↔vt) + vẽ cung không-tù (dt) / góc thực (vt). Đ5.9.
       chanVuongGoc : [32t] list dict — chân vuông góc (hình chiếu điểm lên đt) + ô vuông +
                  đoạn khoảng cách. Mỗi dict: {tuDiem:i (index trong diem),
                  denDuong:j (index trong duongThang), nhanChan?:'H', oVuong?:True,
                  veDoan?:True, net?:'dut'|'lien', mau?:'gray!75'}. Máy TỰ tính H = hình
                  chiếu (Đ5.9 — người/AI KHÔNG cấp toạ độ H). Phục vụ d(M,Δ) H7.9, H7.10.
       duongTron : [32u] list dict — đường tròn trên Oxy. Mỗi dict: {tam:(a,b), R,
                  nhan?:'(C)', mau?:'blue!70', net?:'dut'|'lien', veTam?:True,
                  nhanTam?:'I', viTriNhan?}. Phục vụ H7.13 (định nghĩa), H7.15b, H7.16.
       tiepTuyen : [32u] list dict — tiếp tuyến tại điểm M THUỘC đường tròn (idx trong
                  duongTron). Mỗi dict: {tron:idx, diem:(x0,y0), nhanDiem?:'M',
                  veBanKinh?:True, oVuong?:True, nhan?:'\\Delta', mau?, daiNua?:2.6}.
                  Máy TỰ tính đường ⊥ bán kính IM tại M (Đ5.9) + vẽ bán kính + ô vuông.
                  PHANH kiểm |IM| = R. Phục vụ H7.16 (tiếp tuyến tại điểm).
       doan : [32u] list dict — đoạn thẳng phụ (không mũi tên): {tu, den, nhan?, net?,
                  mau?, viTriNhan?}. Dùng vẽ bán kính R, dây cung… (H7.13).
       elip : [32v] list dict — elip x²/a²+y²/b²=1 (tâm O): {a, b, tam?:(0,0),
                  veTieuDiem?, nhanTieuDiem?:('F_1','F_2'), nua?:'tren'|'duoi' (nửa elip),
                  nhan?:'(E)', mau?, net?}. Tiêu điểm (±√(a²−b²);0) khi a>b, tâm O. H7.21/H7.22.
       hypebol : [32v] list dict — hypebol x²/a²−y²/b²=1 (2 nhánh): {a, b, veTieuDiem?,
                  nhanTieuDiem?, nhan?:'(H)', mau?, net?}. Tiêu điểm (±√(a²+b²);0). H7.23/H7.26.
       parabol : [32v] list dict — parabol y²=2px (p>0, mở phải): {p, veTieuDiem?,
                  nhanTieuDiem?:'F', veDuongChuan?, nhanChuan?:'\\Delta', nhan?:'(P)', mau?,
                  net?}. Tiêu điểm F(p/2;0), đường chuẩn x=−p/2. H7.27/H7.34.
       chuThich : caption 'Hình N' căn giữa dưới.
    """
    duongThang = duongThang or []; diem = diem or []; vecto = vecto or []
    cungGoc = cungGoc or []; chanVuongGoc = chanVuongGoc or []
    duongTron = duongTron or []; tiepTuyen = tiepTuyen or []; doan = doan or []
    elip = elip or []; hypebol = hypebol or []; parabol = parabol or []
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
    # [32u] V1 — đường tròn vẽ TRƯỚC (nền) để đường thẳng/điểm/tiếp tuyến nằm trên
    for dt in duongTron:
        L += _mptd_duong_tron(dt)
    # [32v] V2–V4 — ba conic vẽ nền (cùng lớp với đường tròn)
    for el in elip:
        L += _mptd_elip(el, xRange, yRange)
    for hy in hypebol:
        L += _mptd_hypebol(hy, xRange, yRange)
    for pr in parabol:
        L += _mptd_parabol(pr, xRange, yRange)
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
    # [CH04 Vectơ, 2026-10-04] VECTƠ trên hệ trục — mũi tên tu→den (không kéo dài).
    #   v: dict {tu:(x,y), den:(x,y), nhan?:'\\vec a', mau?:'red!80', net?:'lien'|'dut',
    #            viTriNhan?: anchor TikZ (mặc định 'above left')}.
    for v in vecto:
        (vx1, vy1) = v['tu']; (vx2, vy2) = v['den']
        mau = v.get('mau', 'red!80')
        net = 'dashed' if v.get('net') == 'dut' else 'solid'
        L.append(r'\draw[->,very thick,%s,%s] (%g,%g) -- (%g,%g);'
                 % (mau, net, vx1, vy1, vx2, vy2))
        if v.get('nhan'):
            mx, my = (vx1 + vx2) / 2.0, (vy1 + vy2) / 2.0
            L.append(r'\node[%s,%s,font=\small] at (%g,%g) {$%s$};'
                     % (v.get('viTriNhan', 'above left'), mau, mx, my, v['nhan']))
    # [32t] G1 — cung góc giữa 2 phương (dt↔dt: H7.6, H7.7 | vt↔vt: H7.7 VTPT)
    for cg in cungGoc:
        L += _mptd_cung_goc(cg, duongThang, vecto)
    # [32t] G2 — chân vuông góc (hình chiếu) + ô vuông + đoạn khoảng cách (H7.9, H7.10)
    for cv in chanVuongGoc:
        L += _mptd_chan_vuong(cv, diem, duongThang)
    # [32u] V1 — đoạn phụ (bán kính…) + tiếp tuyến tại điểm trên đường tròn
    for dn in doan:
        L += _mptd_doan(dn)
    for tt in tiepTuyen:
        L += _mptd_tiep_tuyen(tt, duongTron)
    if chuThich:
        L.append(r'\node[below,font=\itshape] at (%g,%g) {%s};'
                 % ((xmin + xmax) / 2.0, ymin - 1.0, chuThich))
    L.append(r'\end{tikzpicture}\end{document}')
    return _HC.render_tikz_doc('\n'.join(L), out, tra_bytes)

Hinh.hinhMatPhangToaDo = staticmethod(hinhMatPhangToaDo)
