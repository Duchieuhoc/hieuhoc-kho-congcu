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

    def cung(self, tam, goc_dau, goc_cuoi, mau='red', net='lien'):
        """CUNG của đường tròn tâm 'tam', quét từ 'goc_dau' đến 'goc_cuoi' (độ, góc ở tâm).
        Mặc định đỏ (yếu tố nhấn ở lời giải). Dùng đánh dấu 1 phần đường tròn / cung tròn."""
        if tam not in self.tron:
            raise ValueError(f"cung: chưa khai đường tròn tâm '{tam}'.")
        r = self.tron[tam]
        self.tikz.append(('cung', tam, r, float(goc_dau), float(goc_cuoi), mau, net))
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
