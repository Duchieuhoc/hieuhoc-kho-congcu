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
