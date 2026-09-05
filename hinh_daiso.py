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
                       mui_ten_am=False, goc_ten='0'):
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

        self.ghi_chu(-0.30, 0.30, '')   # giữ khoảng trên gốc (nhãn 0 nằm dưới)
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
