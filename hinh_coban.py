#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_coban.py — MẠCH "HÌNH CƠ BẢN" (điểm·đường·tia·đoạn·góc·trung điểm)
#   Base class HinhCoBan: hạ tầng + khai nghĩa cơ bản + 13 hàm nền + ve().
#   Các mạch trên (đa giác, song song/cát tuyến, đường tròn…) KẾ THỪA class này.
#   Tách 13/08/2026 từ hinh_ch8 theo MO_HINH_KHO_HINH_THCS (tổ chức theo mạch, cấp=metadata).
# Xây trên hinh_core (khung PHANH) + hinh_phang (luật+đo 2D). CS2627.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_core as C
import hinh_phang as P

DAI_CHUAN = 3.0
BUOC_LUOI = 1.0    # cạnh 1 ô lưới (đơn vị vẽ) — nút (cột,hàng) → (cột·bước, hàng·bước)

def _kieu_net(mau=None, net='lien'):
    base = 'very thick' if (mau and net == 'lien') else 'thick'
    opt = [base]
    if mau: opt.append(f'draw={mau}')
    if net == 'dut': opt.append('dashed')
    return ','.join(opt)

class HinhCoBan:
    """Base mạch hình cơ bản. AI Soạn khai NGHĨA từng đối tượng, gọi .ve() cuối:
       máy chạy PHANH toàn bộ ràng buộc → sai thì raise, đúng thì render."""
    def __init__(self, scale=1.0):
        self.V = {}; self.nhan = {}; self.moc = set()
        self.rb = []; self.tikz = []; self.scale = scale
        self.DAI_TIA = 3.0
        # ── nền cho 13 hàm mới ──
        self.duong_data = {}   # ten_duong → (refA, refB) tên 2 điểm mốc (ẩn) trên đường
        self._nduong = 0       # đếm đường để xếp hướng/lệch tránh chồng
        self._tren = {}        # ten_duong → số điểm đã đặt trên đường (xếp thứ tự)
        self._luoi = None      # (cot, hang) nếu đã khai lưới
        self._nhom_bang = {}   # dấu bằng → [(A,B),...] để PHANH cạnh bằng
        self.mau_diem = {}     # [13/08 Nhóm A] ten_diem → màu chấm (điểm dựng ở lời giải = 'red')
        self._ndoanle = 0      # [14/08] đếm đoạn thẳng ĐƠN LẺ (doan_le) → xếp mỗi đoạn 1 dòng
        self.tron = {}         # [15/08] ten_tam → bán kính (đơn vị vẽ) — mạch hinh_tron_ve dùng
    def _diem(self, ten, x, y, nhan='above right', moc=True, mau=None):
        self.V[ten] = (x, y); self.nhan[ten] = nhan
        if moc: self.moc.add(ten)
        if mau: self.mau_diem[ten] = mau          # [13/08] chấm màu cho điểm dựng
        return self
    def _duong_thang(self, A, B, ten_duong=None):
        self.tikz.append(('duong', A, B, ten_duong)); return self
    def _nhan_dau_net(self, ten, huong='auto', xa=0.32):
        self.tikz.append(('nhan_net', ten, huong, xa))
        self.moc.discard(ten); return self
    def _tia(self, O, P_, mui_ten=False, chuan_hoa=True, mau=None, net='lien'):
        if chuan_hoa:
            Ox,Oy = self.V[O]; Px,Py = self.V[P_]
            vx,vy = Px-Ox, Py-Oy; Ln = math.hypot(vx,vy) or 1
            self.V[P_] = (Ox + vx/Ln*self.DAI_TIA, Oy + vy/Ln*self.DAI_TIA)
        self.tikz.append(('tia', O, P_, mui_ten, mau, net)); return self
    def _doan_thang(self, A, B, gach_bang=False):
        self.tikz.append(('doan', A, B, gach_bang)); return self
    def _da_giac(self, *dinh):
        self.tikz.append(('dagiac', list(dinh))); return self
    def _dat_duong(self, ten, goc_do, anchor):
        rA, rB = f'R{ten}0', f'R{ten}1'
        a = math.radians(goc_do); dx,dy = math.cos(a), math.sin(a)
        ax,ay = anchor
        self._diem(rA, ax-dx*3.0, ay-dy*3.0, nhan=None, moc=False)
        self._diem(rB, ax+dx*3.0, ay+dy*3.0, nhan=None, moc=False)
        self.duong_data[ten] = (rA, rB); self._tren[ten] = 0
        return rA, rB, (dx,dy), (ax,ay)
    def _mot_diem_duong(self, ten):     # 2 điểm mốc của 1 đường (để kiểm/giao)
        return self.duong_data[ten]
    def trung_diem(self, M, A, B, mau=None):
        """M = TRUNG ĐIỂM đoạn AB. M chưa đặt → tự đặt tại chính giữa A,B. Vẽ đoạn AB + gạch bằng
        2 nửa (A–M = M–B) + ràng buộc thẳng hàng A,M,B (PHANH). mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        if M not in self.V:            # [12/08 vá lỗi cũ] tự đặt M tại trung điểm nếu chưa đặt
            (ax,ay),(bx,by) = self.V[A], self.V[B]
            self._diem(M, (ax+bx)/2, (ay+by)/2, 'above', moc=True, mau=mau)
        elif mau:
            self.mau_diem[M] = mau
        self.rb.append({'loai':'trung_diem','M':M,'doan':(A,B)})
        self.rb.append({'loai':'thang_hang','diem':[A,M,B]})
        self.tikz.append(('doan', A, B, False))
        self.tikz.append(('gach_bang', A, M)); self.tikz.append(('gach_bang', M, B))
        return self
    def so_do_goc(self, ten, do=None, hien_so=True, mau='orange', ban_kinh=7):
        """mau/ban_kinh: khi 1 hình có ≥2 cung góc lồng nhau → dùng MÀU KHÁC +
        bán kính khác để phân biệt (Đ: cung trong nhỏ cam, cung ngoài lớn xanh).
        do=None → TỰ ĐO từ toạ độ (vẽ cung đánh dấu góc mà không assert số đo cho trước)."""
        if do is None:
            A, O, B = ten
            ox, oy = self.V[O]; ax, ay = self.V[A]; bx, by = self.V[B]
            a1 = math.atan2(ay - oy, ax - ox); a2 = math.atan2(by - oy, bx - ox)
            dd = (a2 - a1) % (2 * math.pi)
            do = round(math.degrees(dd if dd <= math.pi else 2 * math.pi - dd), 4)
        self.rb.append({'loai':'goc','ten':list(ten),'do':do})
        self.tikz.append(('goc', list(ten), do, hien_so, mau, ban_kinh)); return self
    def goc_vuong(self, ten):
        """Đánh dấu GÓC VUÔNG (90°) trên góc 'ten' = (cạnh1, đỉnh, cạnh2) đã khai — vẽ Ô VUÔNG nhỏ
        thay cung số. PHANH kiểm góc = 90°. Chỉ đánh dấu; 2 cạnh phải khai trước qua tia/chum_tia."""
        self.rb.append({'loai':'goc','ten':list(ten),'do':90})
        self.tikz.append(('goc_vuong', list(ten))); return self
    def tia(self, goc_O, ten_dau, xoay=0, mui_ten=False, nhan='auto', mau=None, net='lien'):
        """TIA gốc 'goc_O' hướng tới 'ten_dau', nghiêng 'xoay'° so ngang (0 = sang phải). Gốc chưa đặt
        → đặt tại (0,0). mui_ten=True → mũi tên đầu tia (ký hiệu tia). nhan: vị trí nhãn mút ('auto' tự chọn).
        mau/net: style phân biệt (đường phụ lời giải = 'red'/'dut'). Tia đơn: 1 gốc, 1 hướng."""
        if goc_O not in self.V: self._diem(goc_O, 0, 0, 'below left', moc=True)
        Ox, Oy = self.V[goc_O]; a = math.radians(xoay)
        self._diem(ten_dau, Ox+DAI_CHUAN*math.cos(a), Oy+DAI_CHUAN*math.sin(a), moc=False)
        self._tia(goc_O, ten_dau, mui_ten=mui_ten, mau=mau, net=net); self._nhan_dau_net(ten_dau, nhan)
        return self
    def tia_diem(self, goc_O, ds, xoay=0, ten_tia=None, hai_dau=False, nhan_dodai=False, mau=None, net='lien'):
        """TIA gốc 'goc_O' mang các điểm ĐO ĐƯỢC (metric). ds=[(tên, vị_trí), …] · vị_trí =
        khoảng cách từ gốc theo ĐƠN VỊ BÀI; vị_trí ÂM = điểm trên TIA ĐỐI. Máy chuẩn hoá tỉ lệ,
        đặt gốc O, vẽ mũi tên đầu dương (hai_dau=True → mũi tên cả hai đầu), ràng buộc thẳng hàng
        (PHANH). ten_tia: nhãn cạnh mũi tên (vd 'x' cho tia Ox). nhan_dodai=True → ghi khoảng cách
        từ gốc dưới mỗi điểm. (Song sinh với duong_diem, nhưng cho TIA + vị trí metric.)"""
        a = math.radians(xoay); dx, dy = math.cos(a), math.sin(a)
        if goc_O not in self.V: self._diem(goc_O, 0.0, 0.0, 'below left', moc=True)
        Ox, Oy = self.V[goc_O]
        vals = [float(v) for _, v in ds]
        vmax = max(abs(v) for v in vals) or 1.0
        k = 4.8 / vmax
        for ten, v in ds:
            self._diem(ten, Ox+dx*v*k, Oy+dy*v*k, 'above', moc=True)
            if nhan_dodai:
                self.tikz.append(('nhan_duoi', ten, ('%g' % abs(v)).replace('.', ',')))
        vpos, vneg = max(vals), min(vals)
        key = ten_tia or ('tia_'+goc_O)
        tip = '_tip_'+key
        self._diem(tip, Ox+dx*(vpos*k+0.8), Oy+dy*(vpos*k+0.8), nhan=None, moc=False)
        self.tikz.append(('tia', goc_O, tip, True, mau, net))
        if ten_tia: self.tikz.append(('nhan_mut', tip, ten_tia))
        if vneg < 0 or hai_dau:
            neg = '_tipn_'+key; d2 = min(vneg, 0.0)*k - 0.8
            self._diem(neg, Ox+dx*d2, Oy+dy*d2, nhan=None, moc=False)
            self.tikz.append(('tia', goc_O, neg, hai_dau, mau, net))
        self.duong_data[key] = (goc_O, tip); self._tren[key] = 0
        for t, _ in ds:
            self.rb.append({'loai':'diem_tren_duong','diem':t,'qua':(goc_O, tip)})
        self.rb.append({'loai':'thang_hang','diem':[goc_O]+[t for t,_ in ds]})
        return self
    def goc(self, dinh, canh1, canh2, do, xoay=0, vuong=False, hien_so=True):
        """AI Soạn chỉ khai: đỉnh, tên 2 cạnh, số đo. Máy đặt 2 cạnh BẰNG NHAU
        (DAI_CHUAN), cạnh1 nghiêng 'xoay'° so ngang, cạnh2 = cạnh1 + do.
        vuong=True → vẽ ô vuông thay cung số. hien_so=False → vẽ cung góc NHƯNG ẩn số đo
        (hình ĐỀ đo-góc / minh hoạ so sánh: chỉ hiện cung, không lộ đáp án — Đ35)."""
        if dinh not in self.V: self._diem(dinh, 0, 0, 'below left', moc=True)
        Ox, Oy = self.V[dinh]
        a1 = math.radians(xoay); a2 = math.radians(xoay + do)
        self._diem(canh1, Ox+DAI_CHUAN*math.cos(a1), Oy+DAI_CHUAN*math.sin(a1), moc=False)
        self._diem(canh2, Ox+DAI_CHUAN*math.cos(a2), Oy+DAI_CHUAN*math.sin(a2), moc=False)
        self._tia(dinh, canh1); self._tia(dinh, canh2)
        if vuong: self.goc_vuong((canh1, dinh, canh2))
        else:     self.so_do_goc((canh1, dinh, canh2), do, hien_so=hien_so)
        self._nhan_dau_net(canh1); self._nhan_dau_net(canh2); return self
    def thuoc_do_goc(self, dinh, tia0, tia_do, do, xoay=0, chieu=1, ban_kinh=2.5, thang='don'):
        """THƯỚC ĐO GÓC (nửa đường tròn chia độ) áp lên góc tia0-đỉnh-tia_do — minh hoạ/đọc số đo.
        tia0 = cạnh trùng vạch 0 (đặt nghiêng 'xoay'° so ngang); tia_do = cạnh chỉ 'do' độ.
        chieu=+1 quét ngược chiều kim (tia_do phía trên), -1 thuận chiều kim. thang='doi' hai
        thang 0–180 như SGK (dạy chọn thang), 'don' một thang. Máy đặt 2 tia + phủ thước
        (vạch chính 10° có số, vạch phụ 2°). PHANH kiểm góc tia0-đỉnh-tia_do = do."""
        if dinh not in self.V: self._diem(dinh, 0.0, 0.0, 'below', moc=True)
        Ox, Oy = self.V[dinh]
        a0 = math.radians(xoay); a1 = math.radians(xoay + chieu*do)
        self._diem(tia0, Ox+DAI_CHUAN*math.cos(a0), Oy+DAI_CHUAN*math.sin(a0), moc=False)
        self._diem(tia_do, Ox+DAI_CHUAN*math.cos(a1), Oy+DAI_CHUAN*math.sin(a1), moc=False)
        self._tia(dinh, tia0); self._tia(dinh, tia_do)
        self._nhan_dau_net(tia0); self._nhan_dau_net(tia_do)
        self.tikz.append(('thuoc', dinh, float(ban_kinh), float(xoay), int(chieu), thang))
        self.rb.append({'loai':'goc','ten':[tia0, dinh, tia_do],'do':do})  # PHANH kiểm, KHÔNG vẽ cung số
        return self
    def thang_hang(self, *diem):
        """KHAI các điểm THẲNG HÀNG → PHANH kiểm độ lệch, sai thì dừng."""
        self.rb.append({'loai':'thang_hang','diem':list(diem)}); return self
    def tia_doi(self, O, t1, t2, xoay=0):
        """HAI TIA ĐỐI chung gốc O: t1 và t2 hai phía đối nhau qua O, nghiêng 'xoay'° so ngang.
        Vẽ đoạn t1–t2 + PHANH kiểm góc t1-O-t2 = 180° và t1,O,t2 thẳng hàng. Dùng bài 'hai tia đối nhau'."""
        if O not in self.V: self._diem(O, 0, 0, 'below', moc=True)
        Ox, Oy = self.V[O]; a = math.radians(xoay)
        self._diem(t1, Ox+DAI_CHUAN*math.cos(a), Oy+DAI_CHUAN*math.sin(a), moc=False)
        self._diem(t2, Ox-DAI_CHUAN*math.cos(a), Oy-DAI_CHUAN*math.sin(a), moc=False)
        self.tikz.append(('doan', t1, t2, False))
        self.rb.append({'loai':'thang_hang','diem':[t1,O,t2]})
        self.rb.append({'loai':'goc','ten':[t1,O,t2],'do':180,'dungsai':0.5})
        self._nhan_dau_net(t1); self._nhan_dau_net(t2); return self
    def chum_tia(self, dinh, danh_sach, cung=None):
        """cung=[(canh1,canh2,số_đo), ...] để vẽ + kiểm góc giữa 2 tia."""
        if dinh not in self.V: self._diem(dinh, 0, 0, 'below left', moc=True)
        Ox, Oy = self.V[dinh]
        for ten, xoay in danh_sach:
            a = math.radians(xoay)
            self._diem(ten, Ox+DAI_CHUAN*math.cos(a), Oy+DAI_CHUAN*math.sin(a), moc=False)
            self._tia(dinh, ten); self._nhan_dau_net(ten)
        for c1, c2, do in (cung or []):
            self.so_do_goc((c1, dinh, c2), do)
        return self
    def chum_duong(self, tam, danh_sach, dai=3.0):
        """CHÙM ĐƯỜNG THẲNG đồng quy tại 'tam'. danh_sach=[(tên, xoay°), …] — mỗi đường qua tâm,
        nghiêng 'xoay'° so ngang, dài 'dai' về mỗi phía. Nhãn cạnh 1 đầu. Dùng nhiều đường cắt nhau tại 1 điểm."""
        if tam not in self.V: self._diem(tam, 0, 0, 'below', moc=True)
        Ox, Oy = self.V[tam]
        for ten, xoay in danh_sach:
            a = math.radians(xoay); e1, e2 = f'R{ten}A', f'R{ten}B'
            self._diem(e1, Ox+dai*math.cos(a), Oy+dai*math.sin(a), nhan=None, moc=False)
            self._diem(e2, Ox-dai*math.cos(a), Oy-dai*math.sin(a), nhan=None, moc=False)
            self.tikz.append(('doan', e1, e2, False))
            self.tikz.append(('nhan_duong', ten, e1, tam))
        return self
    def duong(self, ten, nhan2dau=None, mau=None, net='lien', an_nhan=False):
        """ĐƯỜNG THẲNG tên 'ten' (d,a,b,m…). nhan2dau=('x','y') → nhãn 2 đầu (đường xy).
        mau/net: style phân biệt (đường phụ lời giải = mau='red', net='dut').
        an_nhan=True → KHÔNG hiện nhãn đường (đường trần, vd bài 'lấy điểm')."""
        goc_do = [0, 68, 124, 40, 100, 156][self._nduong % 6]
        off    = [0, 0.4, -0.4, 0.8, -0.8, 1.2][self._nduong % 6]
        self._nduong += 1
        rA, rB, _, _ = self._dat_duong(ten, goc_do, (0, off))
        self.tikz.append(('duong', rA, rB, mau, net))
        if not an_nhan:
            if nhan2dau:
                self.tikz.append(('nhan_mut', rA, nhan2dau[0]))
                self.tikz.append(('nhan_mut', rB, nhan2dau[1]))
            else:
                self.tikz.append(('nhan_mut', rB, ten))
        return self
    def duong_qua(self, A, B, mau='red', net='dut'):
        """ĐƯỜNG THẲNG (kéo dài 2 phía) qua 2 điểm A,B đã đặt — dùng vẽ ĐƯỜNG PHỤ trong
        lời giải. Mặc định đỏ nét đứt (quy ước yếu tố dựng thêm). A,B đã được PHANH kiểm
        qua con đường nghĩa của chúng nên KHÔNG thêm ràng buộc (Đ5.9 vẫn kín)."""
        self.tikz.append(('duong', A, B, mau, net)); return self

    # ── [13/08] ĐƯỜNG + NHIỀU ĐIỂM rải ĐỀU, CĂN GIỮA (đường tự co vừa điểm — hết méo) ──
    def duong_diem(self, ten, ds_diem, nhan2dau=None, an_nhan=False, mau=None, net='lien', diem_do=()):
        """ĐƯỜNG THẲNG mang danh sách điểm ĐÃ SẮP THỨ TỰ (trái→phải): rải ĐỀU và CĂN GIỮA;
        đường TỰ CO vừa các điểm (thò 2 đầu một khoảng cố định). Thay cho duong+diem_tren khi
        bài là 'các điểm trên một đường' (nhận biết thẳng hàng, tia đối…). nhan2dau=('x','y')
        → nhãn 2 đầu; an_nhan=True → đường trần; diem_do=[…] → các điểm chấm ĐỎ (điểm dựng ở
        lời giải). Tự thêm ràng buộc thẳng hàng (PHANH)."""
        n = len(ds_diem)
        buoc, bien = 1.2, 0.7                      # khoảng giữa 2 điểm · đường thò mỗi đầu
        goc_do = [0, 68, 124, 40, 100, 156][self._nduong % 6]
        off    = [0, 0.4, -0.4, 0.8, -0.8, 1.2][self._nduong % 6]
        self._nduong += 1
        a = math.radians(goc_do); dx,dy = math.cos(a), math.sin(a)
        cx,cy = 0.0, off                            # tâm đường
        nua = (n-1)*buoc/2.0
        Lend = nua + bien
        rA, rB = f'R{ten}0', f'R{ten}1'
        self._diem(rA, cx-dx*Lend, cy-dy*Lend, nhan=None, moc=False)
        self._diem(rB, cx+dx*Lend, cy+dy*Lend, nhan=None, moc=False)
        self.duong_data[ten] = (rA, rB); self._tren[ten] = n
        self.tikz.append(('duong', rA, rB, mau, net))
        nghieng = abs(goc_do % 180)
        nhan = 'above' if (nghieng < 30 or nghieng > 150) else 'right'
        for i, P in enumerate(ds_diem):
            t = -nua + i*buoc
            self._diem(P, cx+dx*t, cy+dy*t, nhan, moc=True, mau=('red' if P in diem_do else None))
            self.rb.append({'loai':'diem_tren_duong','diem':P,'qua':(rA,rB)})
        if n >= 3:
            self.rb.append({'loai':'thang_hang','diem':list(ds_diem)})
        if not an_nhan:
            if nhan2dau:
                self.tikz.append(('nhan_mut', rA, nhan2dau[0]))
                self.tikz.append(('nhan_mut', rB, nhan2dau[1]))
            else:
                self.tikz.append(('nhan_mut', rB, ten))
        return self
    def hai_duong(self, ten1, ten2, quan_he):
        """quan_he ∈ {'cat','song_song','trung'}. Máy đặt thỏa quan hệ + PHANH kiểm."""
        self._nduong += 2
        if quan_he == 'cat':
            a1,b1,_,_ = self._dat_duong(ten1, 20, (0,0))
            a2,b2,_,_ = self._dat_duong(ten2, 108, (0,0))
            self.rb.append({'loai':'cat','doan1':(a1,b1),'doan2':(a2,b2)})
        elif quan_he == 'song_song':
            a1,b1,_,_ = self._dat_duong(ten1, 15, (0, 0.9))
            a2,b2,_,_ = self._dat_duong(ten2, 15, (0,-0.9))
            self.rb.append({'loai':'song_song','doan1':(a1,b1),'doan2':(a2,b2)})
        elif quan_he == 'trung':
            a1,b1,_,_ = self._dat_duong(ten1, 22, (0,0))
            # đường 2 trùng đường 1: dùng chung mốc, chỉ thêm nhãn
            self.duong_data[ten2] = (a1,b1); self._tren[ten2] = 0
            self.rb.append({'loai':'trung','diem':[a1, b1]})
        else:
            raise ValueError(f"hai_duong: quan_he '{quan_he}' không hợp lệ (cat/song_song/trung).")
        self.tikz.append(('duong', *self.duong_data[ten1], None))
        self.tikz.append(('nhan_mut', self.duong_data[ten1][1], ten1))
        if quan_he != 'trung':
            self.tikz.append(('duong', *self.duong_data[ten2], None))
        self.tikz.append(('nhan_mut', self.duong_data[ten2][1], ten2))
        return self
    def giao(self, ten, dt1, dt2, mau=None):
        """ĐIỂM 'ten' = giao của 2 đường (tên) HOẶC 2 đoạn (tuple mút). Song song → raise.
        mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        def mut(o):
            if isinstance(o, (tuple, list)): return o[0], o[1]
            return self.duong_data[o]
        A,B = mut(dt1); Cc,D = mut(dt2)
        (ax,ay),(bx,by) = self.V[A],self.V[B]; (cx,cy),(dx,dy) = self.V[Cc],self.V[D]
        r1x,r1y = bx-ax, by-ay; r2x,r2y = dx-cx, dy-cy
        den = r1x*r2y - r1y*r2x
        if abs(den) < 1e-9:
            raise ValueError(f"[PHANH DỪNG] giao '{ten}': 2 đường SONG SONG → không có giao.")
        t = ((cx-ax)*r2y - (cy-ay)*r2x)/den
        self._diem(ten, ax+t*r1x, ay+t*r1y, 'above right', moc=True, mau=mau)
        self.rb.append({'loai':'diem_tren_duong','diem':ten,'qua':(A,B)})
        self.rb.append({'loai':'diem_tren_duong','diem':ten,'qua':(Cc,D)})
        return self
    def diem_tren(self, ten, duong, thu_tu=None, mau=None):
        """Điểm 'ten' ∈ 'duong'. thu_tu=số nguyên xếp thứ tự nhiều điểm trên 1 đường.
        mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        rA, rB = self.duong_data[duong]
        (ax,ay),(bx,by) = self.V[rA], self.V[rB]
        ux,uy = bx-ax, by-ay
        k = thu_tu if thu_tu is not None else self._tren[duong]
        self._tren[duong] += 1
        t = 0.30 + k*0.18            # rải dọc đoạn mốc (0.30→) theo thứ tự
        nghieng = abs((math.degrees(math.atan2(uy,ux))) % 180)
        nhan = 'above' if (nghieng < 30 or nghieng > 150) else 'right'
        self._diem(ten, ax+t*ux, ay+t*uy, nhan, moc=True, mau=mau)
        self.rb.append({'loai':'diem_tren_duong','diem':ten,'qua':(rA,rB)})
        return self
    def diem_ngoai(self, ten, duong, phia=None, mau=None, doc=0.0):
        """Điểm 'ten' KHÔNG thuộc 'duong'. phia ∈ {'tren','duoi','trai','phai'}.
        doc: dời điểm DỌC theo đường (đơn vị vẽ) để đặt nhiều điểm ngoài phân biệt.
        mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        rA, rB = self.duong_data[duong]
        (ax,ay),(bx,by) = self.V[rA], self.V[rB]
        ux,uy = bx-ax, by-ay; L=math.hypot(ux,uy) or 1; ux,uy=ux/L,uy/L
        px,py = -uy, ux                      # pháp tuyến
        dau = { 'tren':1,'duoi':-1,'trai':-1,'phai':1 }.get(phia, 1)
        cx,cy = (ax+bx)/2, (ay+by)/2
        cx,cy = cx+ux*doc, cy+uy*doc         # dời dọc đường (đặt >1 điểm ngoài)
        self._diem(ten, cx+px*1.5*dau, cy+py*1.5*dau, 'above', moc=True, mau=mau)
        self.rb.append({'loai':'diem_ngoai_duong','diem':ten,'qua':(rA,rB)})
        return self
    def doan(self, A, B, dodai=None, danh_dau=None, mau=None, net='lien', rong=None):
        """Đoạn 2 mút A,B (đã đặt). dodai='4 cm' ghi độ dài. danh_dau='='|số → gạch bằng + kiểm.
        mau/net: style phân biệt (kết quả lời giải = mau='red', net='lien' → đỏ liền đậm).
        rong ∈ {'manh','vua','dam','rat_dam'}: bề dày nét — phân biệt vai đoạn (vd kim giờ
        'dam' vs kim phút 'manh' trong đồng hồ; None = mặc định theo mau/net)."""
        self.tikz.append(('doan', A, B, mau, net, rong))
        if dodai: self.tikz.append(('doan_nhan', A, B, str(dodai)))
        if danh_dau is not None:
            self.tikz.append(('gach_bang_don', A, B))
            self._nhom_bang.setdefault(danh_dau, []).append((A,B))
        return self
    def doan_le(self, A, B, dai=3.0, dodai=None, huong='ngang',
                danh_dau=None, mau=None, net='lien'):
        """ĐOẠN THẲNG ĐƠN LẺ — tự đặt 2 mút A,B rồi vẽ (KHÔNG cần đặt điểm trước).
        Mút cách nhau 'dai' (đơn vị vẽ) theo 'huong' ∈ {'ngang','doc','cheo'};
        'dodai'='4 cm' ghi độ dài; danh_dau/mau/net như doan(). Nhãn A,B ở 2 đầu.
        Gọi NHIỀU LẦN → mỗi đoạn tự xuống 1 DÒNG (không chồng), CĂN TRÁI cùng mốc
        (để mắt so độ dài). Dùng cho hình 'đoạn thẳng có ghi độ dài' (8.25/8.29/8.31).
        Đoạn đơn không khai quan hệ nào → PHANH không có gì để tái đo (đúng)."""
        k = self._ndoanle; self._ndoanle += 1
        LECH = 1.5                                   # khoảng cách giữa 2 dòng đoạn kề
        if huong == 'doc':
            ax, ay, bx, by = k*LECH, 0.0, k*LECH, dai
            nA, nB = 'below', 'above'
        elif huong == 'cheo':
            d = dai/math.sqrt(2)
            ax, ay, bx, by = 0.0, -k*LECH, d, -k*LECH + d
            nA, nB = 'below left', 'above right'
        else:                                        # 'ngang' (mặc định)
            ax, ay, bx, by = 0.0, -k*LECH, dai, -k*LECH
            nA, nB = 'below left', 'below right'
        self._diem(A, ax, ay, nA, moc=True)
        self._diem(B, bx, by, nB, moc=True)
        return self.doan(A, B, dodai=dodai, danh_dau=danh_dau, mau=mau, net=net)
    def diem_giua(self, ten, A, B, ti_le=0.5, mau=None, nhan='above'):
        """Điểm 'ten' nằm giữa A,B. ti_le∈(0,1) vị trí tương đối (KHÔNG phải tọa độ).
        mau='red' → chấm đỏ (điểm dựng ở lời giải). nhan='below' → tên điểm xuống dưới
        (tránh đè nhãn độ dài đặt phía trên, vd 8.30)."""
        (ax,ay),(bx,by) = self.V[A], self.V[B]
        self._diem(ten, ax+ti_le*(bx-ax), ay+ti_le*(by-ay), nhan, moc=True, mau=mau)
        self.rb.append({'loai':'thang_hang','diem':[A,ten,B]})
        self.rb.append({'loai':'nam_giua','diem':ten,'doan':(A,B)})
        return self
    def luoi(self, cot, hang):
        """Lưới nền cot×hang ô (xám nhạt)."""
        self._luoi = (cot, hang); self.tikz.append(('luoi', cot, hang)); return self
    def diem_luoi(self, ten, cot, hang, mau=None):
        """Điểm 'ten' tại NÚT (cột,hàng) — chỉ số nguyên, dữ kiện đề (như số đo góc).
        mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        self._diem(ten, cot*BUOC_LUOI, hang*BUOC_LUOI, 'above right', moc=True, mau=mau)
        rb = {'loai':'nut_luoi','diem':ten,'step':BUOC_LUOI}
        if self._luoi: rb['cot'], rb['hang'] = self._luoi
        self.rb.append(rb); return self
    def noi(self, *diem, kin=False, mau=None):
        """Nối các điểm ĐÃ ĐẶT thành đoạn/gấp khúc. kin=True→đa giác đóng. mau=màu đường."""
        self.tikz.append(('noi', list(diem), kin, mau)); return self
    def diem_trong(self, ten, goc, lech=0, xa=1.3, mau=None):
        """Điểm 'ten' nằm TRONG 'goc' (bộ 3 (cạnh1,đỉnh,cạnh2) đã khai qua goc/chum_tia).
        lech=số độ xoay quanh đỉnh so phân giác trong (đặt NHIỀU điểm trong phân biệt;
        xoay quá tay ra ngoài → PHANH dừng). xa=khoảng cách từ đỉnh. mau='red' → chấm đỏ."""
        c1, dinh, c2 = goc
        (ox,oy) = self.V[dinh]
        def u(P):
            vx,vy = self.V[P][0]-ox, self.V[P][1]-oy; L=math.hypot(vx,vy) or 1
            return vx/L, vy/L
        u1x,u1y = u(c1); u2x,u2y = u(c2)
        bx,by = u1x+u2x, u1y+u2y; L=math.hypot(bx,by) or 1
        dx,dy = bx/L, by/L                          # phân giác TRONG
        if lech:
            a = math.radians(lech); ca,sa = math.cos(a), math.sin(a)
            dx,dy = dx*ca - dy*sa, dx*sa + dy*ca
        self._diem(ten, ox+dx*xa, oy+dy*xa, 'above right', moc=True, mau=mau)
        self.rb.append({'loai':'diem_trong_goc','goc':(c1,dinh,c2),'diem':ten}); return self
    def diem_ngoai_goc(self, ten, goc, lech=0, xa=1.6, mau=None):
        """Điểm 'ten' nằm NGOÀI 'goc' (bộ 3 (cạnh1,đỉnh,cạnh2) đã khai qua goc/chum_tia).
        Đối xứng với diem_trong: đặt theo hướng PHÂN GIÁC NGOÀI (miền phản xạ) → chắc chắn
        ngoài góc. lech=số độ xoay hướng ngoài (đặt nhiều điểm ngoài phân biệt; PHANH vẫn
        kiểm phải nằm ngoài, xoay quá tay vào trong → dừng). xa=khoảng cách từ đỉnh.
        mau='red' → chấm đỏ (điểm dựng ở lời giải)."""
        c1, dinh, c2 = goc
        (ox,oy) = self.V[dinh]
        def u(P):
            vx,vy = self.V[P][0]-ox, self.V[P][1]-oy; L=math.hypot(vx,vy) or 1
            return vx/L, vy/L
        u1x,u1y = u(c1); u2x,u2y = u(c2)
        bx,by = u1x+u2x, u1y+u2y; L=math.hypot(bx,by) or 1
        dx,dy = -bx/L, -by/L                       # phân giác NGOÀI = ngược phân giác trong
        if lech:
            a = math.radians(lech); ca,sa = math.cos(a), math.sin(a)
            dx,dy = dx*ca - dy*sa, dx*sa + dy*ca   # xoay hướng ngoài quanh đỉnh
        anchor = 'above left' if dx <= 0 else 'above right'
        self._diem(ten, ox+dx*xa, oy+dy*xa, anchor, moc=True, mau=mau)
        self.rb.append({'loai':'diem_ngoai_goc','goc':(c1,dinh,c2),'diem':ten}); return self

    # ── [15/08] CỤM ĐÁNH DẤU (quan hệ = · // · tô miền) — palette ký hiệu SGK ──
    def dau_bang(self, A, B, so_vach=1, kiem_bang=None):
        """Đánh dấu CẠNH BẰNG NHAU trên đoạn A,B (đã đặt) bằng 'so_vach' vạch (1/2/3) —
        vạch khác nhau phân biệt các NHÓM cạnh bằng khác nhau (dấu ×/×× như SGK 8.33).
        kiem_bang=khóa nhóm (bất kỳ) → gom mọi đoạn cùng khóa vào PHANH cạnh-bằng
        (kiểm hình dựng đúng bằng nhau). Chỉ đánh dấu, không tự nối đoạn."""
        self.tikz.append(('dau_bang_n', A, B, int(so_vach)))
        if kiem_bang is not None:
            self._nhom_bang.setdefault(kiem_bang, []).append((A, B))
        return self
    def dau_song_song(self, A, B, so_mui=1):
        """Đánh dấu HƯỚNG SONG SONG trên đoạn A,B (đã đặt) bằng 'so_mui' mũi tên (1/2) —
        các đoạn cùng số mũi tên = cùng phương (ký hiệu >/>> như SGK). Chỉ đánh dấu."""
        self.tikz.append(('dau_ss', A, B, int(so_mui)))
        return self
    def to_mien(self, *diem, mau='cyan!18'):
        """TÔ MÀU một miền = đa giác qua các điểm ĐÃ ĐẶT (theo thứ tự). Dùng tô:
        • miền trong 1 góc: to_mien(P1, đỉnh, P2) — P1,P2 trên 2 cạnh;
        • giao/hợp nhiều góc (miền trong tam giác — 8.30): to_mien(A, B, C).
        Miền được tô NẰM DƯỚI mọi nét (không che hình). mau: màu tô nhạt."""
        self.tikz.append(('to_mien', list(diem), mau)); return self

    def ve(self, out='hinh', tra_bytes=False, nhan=None):
        """CỬA RENDER — gọi CUỐI cùng. Chạy PHANH verify (sai hình → DỪNG tại đây) rồi xuất TikZ→PNG.
        out = tên file (không đuôi). tra_bytes=True → trả bytes PNG (nhúng docx qua template); False → ghi file.
        nhan = caption "Hình N" nướng CĂN GIỮA DƯỚI ảnh (cho hình neo phải mục ③+). Mọi hàm khai nghĩa phải gọi TRƯỚC ve()."""
        # gom nhóm dấu-bằng → ràng buộc canh_bang trước khi PHANH
        for dau, segs in self._nhom_bang.items():
            if len(segs) >= 2:
                self.rb.append({'loai':'canh_bang','cac_doan':segs})
        C.phanh(self.V, self.rb)                 # ← CỬA VERIFY: sai là dừng ở đây
        s = self.scale
        L = [f'\\begin{{tikzpicture}}[scale={s},>=latex]']
        for tn,(x,y) in self.V.items():
            L.append(f'  \\coordinate ({C._san(tn)}) at ({x:.3f},{y:.3f});')
        # [15/08] TÔ MIỀN trước — nằm DƯỚI mọi nét (không che hình)
        for el in self.tikz:
            if el[0]=='to_mien':
                pts, mau = el[1], el[2]
                path='--'.join(f'({C._san(p)})' for p in pts)
                L.append(f'  \\fill[{mau}] {path}--cycle;')
        for el in self.tikz:
            k = el[0]
            if k=='to_mien':
                continue
            if k=='luoi':
                cot,hang = el[1],el[2]
                L.append(f'  \\draw[very thin,gray!35] (0,0) grid ({cot},{hang});')
            elif k=='dagiac':
                pts = el[1]; path='--'.join(f'({C._san(p)})' for p in pts)
                L.append(f'  \\draw[thick] {path}--cycle;')
            elif k=='noi':
                pts, kin, mau = el[1], el[2], el[3]
                path='--'.join(f'({C._san(p)})' for p in pts)
                opt = 'thick' + (f',draw={mau}' if mau else '')
                L.append(f'  \\draw[{opt}] {path}' + ('--cycle;' if kin else ';'))
            elif k=='tron':
                tam, r = el[1], el[2]
                mau = el[3] if len(el)>3 and isinstance(el[3],str) else None
                net = el[4] if len(el)>4 else 'lien'
                cx,cy = self.V[tam]
                L.append(f'  \\draw[{_kieu_net(mau,net)}] ({cx:.3f},{cy:.3f}) circle ({r:.3f});')
            elif k=='cung':
                tam, r, gA, gB = el[1], el[2], el[3], el[4]
                mau = el[5] if len(el)>5 and isinstance(el[5],str) else None
                net = el[6] if len(el)>6 else 'lien'
                cx,cy = self.V[tam]
                sx = cx + r*math.cos(math.radians(gA)); sy = cy + r*math.sin(math.radians(gA))
                L.append(f'  \\draw[{_kieu_net(mau,net)}] ({sx:.3f},{sy:.3f}) '
                         f'arc ({gA:.3f}:{gB:.3f}:{r:.3f});')
            elif k=='dau_bang_n':
                A,B,nv = el[1],el[2],el[3]; Ap,Bp = self.V[A],self.V[B]
                mx,my = (Ap[0]+Bp[0])/2,(Ap[1]+Bp[1])/2
                dx,dy = Bp[0]-Ap[0],Bp[1]-Ap[1]; Ln=math.hypot(dx,dy) or 1
                ux,uy = dx/Ln, dy/Ln
                px,py = -uy*0.12, ux*0.12          # nửa vạch (vuông góc đoạn)
                for i in range(nv):
                    off=(i-(nv-1)/2)*0.10
                    bx,by = mx+ux*off, my+uy*off
                    L.append(f'  \\draw[thick] ({bx-px:.3f},{by-py:.3f})--({bx+px:.3f},{by+py:.3f});')
            elif k=='dau_ss':
                A,B,nm = el[1],el[2],el[3]; Ap,Bp = self.V[A],self.V[B]
                mx,my = (Ap[0]+Bp[0])/2,(Ap[1]+Bp[1])/2
                dx,dy = Bp[0]-Ap[0],Bp[1]-Ap[1]; Ln=math.hypot(dx,dy) or 1
                ux,uy = dx/Ln, dy/Ln; sz,w = 0.13, 0.085
                for i in range(nm):
                    off=(i-(nm-1)/2)*0.16
                    tx,ty = mx+ux*off, my+uy*off        # đỉnh mũi (hướng B)
                    bxp,byp = tx-ux*sz, ty-uy*sz
                    L.append(f'  \\draw[thick] ({bxp+(-uy)*w:.3f},{byp+ux*w:.3f})--'
                             f'({tx:.3f},{ty:.3f})--({bxp-(-uy)*w:.3f},{byp-ux*w:.3f});')
            elif k=='duong':
                A,B = el[1],el[2]
                mau = el[3] if len(el)>3 and isinstance(el[3],str) else None
                net = el[4] if len(el)>4 else 'lien'
                L.append(f'  \\draw[{_kieu_net(mau,net)}] ($({C._san(A)})!-0.15!({C._san(B)})$)--'
                         f'($({C._san(A)})!1.15!({C._san(B)})$);')
            elif k=='nhan_mut':
                mut, ten = el[1], el[2]
                L.append(f'  \\node[above right] at ({C._san(mut)}) {{${ten}$}};')
            elif k=='nhan_duoi':
                mut, ten = el[1], el[2]
                L.append(f'  \\node[below] at ({C._san(mut)}) {{{ten}}};')
            elif k=='so_o':
                xx, yy, txt = el[1], el[2], el[3]
                L.append(f'  \\node[font=\\small] at ({xx:.3f},{yy:.3f}) {{{txt}}};')
            elif k=='tia':
                O,Pp = el[1],el[2]; mui = el[3] if len(el)>3 else False
                mau = el[4] if len(el)>4 and isinstance(el[4],str) else None
                net = el[5] if len(el)>5 else 'lien'
                kieu = _kieu_net(mau,net) + (',->' if mui else ''); keo = '1.15' if not mui else '1.25'
                L.append(f'  \\draw[{kieu}] ({C._san(O)})--($({C._san(O)})!{keo}!({C._san(Pp)})$);')
            elif k=='doan':
                A,B = el[1],el[2]
                mau = el[3] if len(el)>3 and isinstance(el[3],str) else None
                net = el[4] if len(el)>4 else 'lien'
                rong = el[5] if len(el)>5 else None
                kieu = _kieu_net(mau,net)
                if rong:
                    kieu += ',' + {'manh':'thin','vua':'thick',
                                   'dam':'very thick','rat_dam':'line width=1.6pt'}.get(rong,'')
                L.append(f'  \\draw[{kieu}] ({C._san(A)})--({C._san(B)});')
            elif k=='doan_nhan':
                A,B,txt = el[1],el[2],el[3]
                L.append(f'  \\node[above,font=\\small] at ($({C._san(A)})!0.5!({C._san(B)})$) {{{txt}}};')
            elif k in ('gach_bang','gach_bang_don'):
                A,B = el[1],el[2]; Ap,Bp = self.V[A],self.V[B]
                mx,my = (Ap[0]+Bp[0])/2,(Ap[1]+Bp[1])/2
                dx,dy = Bp[0]-Ap[0],Bp[1]-Ap[1]; Ln = math.hypot(dx,dy) or 1
                px,py = -dy/Ln*0.12, dx/Ln*0.12
                L.append(f'  \\draw[thick] ({mx-px:.3f},{my-py:.3f})--({mx+px:.3f},{my+py:.3f});')
            elif k=='goc_vuong':
                L.append(P._o_vuong(self.V, el[1]))
            elif k=='thuoc':
                O_, R = el[1], el[2]; base, chieu, thang = el[3], el[4], el[5]
                cx, cy = self.V[O_]
                s0 = base; s1 = base + chieu*180
                x0 = cx + R*math.cos(math.radians(s0)); y0 = cy + R*math.sin(math.radians(s0))
                L.append(f'  \\draw[thin] ({x0:.3f},{y0:.3f}) arc ({s0:.1f}:{s1:.1f}:{R:.3f});')
                xe = cx + R*math.cos(math.radians(s1)); ye = cy + R*math.sin(math.radians(s1))
                L.append(f'  \\draw[thin] ({x0:.3f},{y0:.3f})--({xe:.3f},{ye:.3f});')
                for kk in range(0, 181):
                    ang = base + chieu*kk; ar = math.radians(ang)
                    dx, dy = math.cos(ar), math.sin(ar)
                    if kk % 10 == 0: rin = R*0.85
                    elif kk % 2 == 0: rin = R*0.93
                    else: continue
                    L.append(f'  \\draw[thin] ({cx+rin*dx:.3f},{cy+rin*dy:.3f})--({cx+R*dx:.3f},{cy+R*dy:.3f});')
                    if kk % 10 == 0:
                        ro = R*0.80
                        L.append(f'  \\node[font=\\scriptsize] at ({cx+ro*dx:.3f},{cy+ro*dy:.3f}) {{{kk}}};')
                        if thang=='doi':
                            r2 = R*0.63
                            L.append(f'  \\node[font=\\scriptsize,gray] at ({cx+r2*dx:.3f},{cy+r2*dy:.3f}) {{{180-kk}}};')
                L.append(f'  \\fill ({cx:.3f},{cy:.3f}) circle(1.2pt);')
            elif k=='nhan_duong':
                ten, ep, tam = el[1], el[2], el[3]
                ex,ey = self.V[ep]; tx,ty = self.V[tam]
                dx,dy = ex-tx, ey-ty; Ln = math.hypot(dx,dy) or 1
                px,py = ex+dx/Ln*0.32, ey+dy/Ln*0.32
                L.append(f'  \\node at ({px:.3f},{py:.3f}) {{${ten}$}};')
            elif k=='goc':
                ten,do,hien = el[1],el[2],el[3]
                mau = el[4] if len(el)>4 else 'orange'
                br  = el[5] if len(el)>5 else 7
                tt = P._thu_tu(self.V, ten); srt='--'.join(C._san(z) for z in tt)
                lbl = f'"${do}^\\circ$",' if hien else ''
                L.append(f'  \\draw pic[{lbl}draw={mau},thick,angle radius={br}mm,'
                         f'angle eccentricity=1.35]{{angle={srt}}};')
        # nhãn đầu nét (tự hất ra ngoài)
        nhan_net_da = set()
        for el in self.tikz:
            if el[0]=='nhan_net':
                tn, huong, xa = el[1], el[2], el[3]; x,y = self.V[tn]
                if huong=='auto':
                    huong = 'phai' if abs(x)<1e-6 else 'tren'
                dx,dy = {'tren':(0,xa),'duoi':(0,-xa),'phai':(xa,0),'trai':(-xa,0)}[huong]
                L.append(f'  \\node at ({x+dx:.3f},{y+dy:.3f}) {{${tn}$}};')
                nhan_net_da.add(tn)
        for tn in self.V:
            if tn in nhan_net_da: continue
            pos = self.nhan.get(tn,'above right'); an_nhan = (pos is None)
            if tn in self.moc:
                lbl = '' if an_nhan else f'node[{pos}]{{${tn}$}}'
                mau_pt = self.mau_diem.get(tn)
                fill = f'\\fill[{mau_pt}]' if mau_pt else '\\fill'
                L.append(f'  {fill} ({C._san(tn)}) circle(1.6pt) {lbl};')
            elif not an_nhan:
                L.append(f'  \\node[{pos}] at ({C._san(tn)}) {{${tn}$}};')
        if nhan:
            # caption "Hình N" căn giữa dưới toàn hình (nhãn nhận biết hình trong bài)
            L.append(f'  \\node[below=3mm,font=\\itshape] at (current bounding box.south) {{{nhan}}};')
        L.append('\\end{tikzpicture}')
        return C._render('\n'.join(L), out, tra_bytes)
