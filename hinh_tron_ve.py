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
