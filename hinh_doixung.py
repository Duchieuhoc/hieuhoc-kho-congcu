#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_doixung.py — MẠCH "TÍNH ĐỐI XỨNG" (semantic — L6 Chương V) · 25/08/2026
#   Kế thừa HinhDaGiac → có sẵn hình phẳng quen (thoi/vuông/cn/tam giác đều/lục giác
#   đều/thang cân) + nền coban (luoi·diem_luoi·noi·diem_giua·doan·giao).
#   PHẠM VI L6 (SGK Chương V — Bài 21 trục, Bài 22 tâm): chỉ NHẬN BIẾT / ĐÁNH DẤU
#   trục–tâm / vẽ-thêm-để-có-đối-xứng. KHÔNG dựng ảnh qua phép đối xứng (đó là LỚP 8).
#   → Chỉ 2 tiện ích CHUẨN HOÁ trình bày; mọi thứ khác tái dùng hàm sẵn có.
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac


class HinhDoiXung(hinh_dagiac.HinhDaGiac):
    def truc_doi_xung(self, diem1, diem2, nhan=None, net='dut'):
        """TRỤC ĐỐI XỨNG: đường thẳng NÉT ĐỨT màu ĐEN, tự kéo dài đều ~15% ra ngoài mỗi
        đầu (thò ra như SGK). KHÔNG đỏ, KHÔNG tick trung điểm.
        diem1, diem2 — mỗi cái là:
          · TÊN điểm đã đặt (trục đi qua điểm đó: đỉnh, nút lưới…), HOẶC
          · tuple ('A','B') → trục đi qua TRUNG ĐIỂM cạnh AB (điểm giữa ẩn: không chấm,
            không nhãn — tránh dây bẩn trục).
        Ví dụ: chữ nhật ABCD 2 trục → truc_doi_xung(('A','B'),('D','C')) và
        truc_doi_xung(('A','D'),('B','C')); thoi → truc_doi_xung('A','C') (trùng đường
        chéo); tam giác cân đỉnh A đáy BC → truc_doi_xung('A',('B','C')).
        nhan='d' → ghi tên trục ở đầu. A,B đã kín nghĩa qua con đường đặt → KHÔNG thêm
        ràng buộc (Đ5.9)."""
        def _moc(d):
            if isinstance(d, (tuple, list)):
                A, B = d
                ten = f'_tdx{A}{B}'
                if ten not in self.V:
                    (ax, ay), (bx, by) = self.V[A], self.V[B]
                    self._diem(ten, (ax + bx) / 2.0, (ay + by) / 2.0, nhan=None, moc=False)
                return ten
            if d not in self.V:
                raise ValueError(f"truc_doi_xung: điểm '{d}' chưa đặt.")
            return d
        P, Q = _moc(diem1), _moc(diem2)
        self.tikz.append(('duong', P, Q, None, net))     # mau=None → ĐEN; renderer tự thò 15%
        if nhan:
            self.tikz.append(('nhan_mut', Q, nhan))
        return self

    def tam_doi_xung(self, O, *cap_doi_dinh, nhan='O', ve_cheo=True, net='dut'):
        """TÂM ĐỐI XỨNG O = giao các đường chéo (chấm + nhãn O). cap_doi_dinh = các CẶP
        đỉnh ĐỐI đã đặt:
          · tứ giác (bình hành/thoi/vuông/cn) → ('A','C'), ('B','D')
          · lục giác đều → ('A','D'), ('B','E'), ('C','F')
        ve_cheo=True → vẽ mỗi cặp thành ĐƯỜNG CHÉO nét đứt đen (đoạn ĐÚNG 2 đỉnh, không
        thò). O đặt tại trung điểm cặp chéo đầu (các chéo đồng quy — Đ5.9). Đoạn thẳng có
        tâm đối xứng là trung điểm: tam_doi_xung('I', ('A','B')) với ve_cheo=False."""
        if not cap_doi_dinh:
            raise ValueError("tam_doi_xung: cần ít nhất 1 cặp đỉnh đối, vd ('A','C').")
        if ve_cheo:
            for A, B in cap_doi_dinh:
                self.doan(A, B, net=net)                 # đoạn: KHÔNG kéo dài ngoài đỉnh
        A0, B0 = cap_doi_dinh[0]
        (ax, ay), (bx, by) = self.V[A0], self.V[B0]
        self._diem(O, (ax + bx) / 2.0, (ay + by) / 2.0, nhan='above right', moc=True)
        return self
