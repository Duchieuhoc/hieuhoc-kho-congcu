#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_dagiac.py — MẠCH "ĐA GIÁC & HÌNH PHẲNG" (tam giác·tứ giác·đa giác đều·hình phẳng đặc biệt)
#   Kế thừa HinhCoBan. Dùng chung Lớp 6→8 (L7 thêm dấu bằng, L8 thêm đồng dạng — cùng hàm).
#   LOP_MODULE gợi ý: [6,7,8]. Tách 13/08/2026 từ hinh_ch8 (MO_HINH_KHO_HINH_THCS).
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_coban

class HinhDaGiac(hinh_coban.HinhCoBan):
    def tam_giac_deu(self, A, B, Cc, canh=3.0, xoay=0):
        """Tam giác ĐỀU 3 đỉnh: B dưới-trái, C dưới-phải, A đỉnh trên. canh = độ dài cạnh
        (mặc định 3.0). Ba cạnh bằng nhau (PHANH canh_bang). Dùng nhận dạng / hình nền."""
        self._diem(B, 0, 0, 'below left')
        self._diem(Cc, canh, 0, 'below right')
        self._diem(A, canh/2, canh*math.sqrt(3)/2, 'above')
        self._da_giac(A, B, Cc)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(B,Cc),(Cc,A)]}); return self
    def hinh_vuong(self, M, N, P_, Q, canh=3.0):
        """Hình VUÔNG: M dưới-trái, N trên-trái, P trên-phải, Q dưới-phải. canh = độ dài cạnh.
        PHANH: 4 cạnh bằng nhau + góc tại M vuông (90°)."""
        self._diem(M, 0, 0, 'below left'); self._diem(N, 0, canh, 'above left')
        self._diem(P_, canh, canh, 'above right'); self._diem(Q, canh, 0, 'below right')
        self._da_giac(M, N, P_, Q)
        self.rb.append({'loai':'canh_bang','cac_doan':[(M,N),(N,P_),(P_,Q),(Q,M)]})
        self.rb.append({'loai':'goc','ten':[Q,M,N],'do':90}); return self
    def hinh_thang(self, A, B, Cc, D, day_tren=3.0, day_duoi=5.0, cao=2.5, lech=0.8):
        """Hình THANG thường: A,B = đáy trên (day_tren); D,C = đáy dưới (day_duoi); AB ∥ DC
        (PHANH song_song). cao = chiều cao; lech = dời ngang đáy trên. Thang CÂN dùng hinh_thang_can."""
        self._diem(A, lech, cao, 'above left'); self._diem(B, lech+day_tren, cao, 'above right')
        self._diem(Cc, day_duoi, 0, 'below right'); self._diem(D, 0, 0, 'below left')
        self._da_giac(A, B, Cc, D)
        self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)}); return self
    def tam_giac(self, A, B, Cc, noi=True):
        """Tam giác 3 đỉnh (không thẳng hàng). Thứ tự A→B→C chiều kim đồng hồ.
        noi=False → chỉ ĐẶT 3 điểm (không nối cạnh) — dùng cho 'ba điểm không thẳng hàng'."""
        self._diem(A, 1.4, 2.2, 'above'); self._diem(B, 2.8, 0, 'below right')
        self._diem(Cc, 0, 0, 'below left')
        if noi: self._da_giac(A, B, Cc)
        self.rb.append({'loai':'khong_thang_hang','diem':[A,B,Cc]}); return self
    def tu_giac(self, A, B, Cc, D, loai=None):
        """Tứ giác 4 đỉnh lồi, chiều kim đồng hồ. loai∈{None,'binh_hanh','chu_nhat'}."""
        if loai == 'binh_hanh':
            self._diem(A,0.7,2,'above left'); self._diem(B,3.7,2,'above right')
            self._diem(Cc,3,0,'below right'); self._diem(D,0,0,'below left')
            self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})
            self.rb.append({'loai':'song_song','doan1':(A,D),'doan2':(B,Cc)})
        elif loai == 'chu_nhat':
            self._diem(A,0,2,'above left'); self._diem(B,3.5,2,'above right')
            self._diem(Cc,3.5,0,'below right'); self._diem(D,0,0,'below left')
            self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})
            self.rb.append({'loai':'song_song','doan1':(A,D),'doan2':(B,Cc)})
            self.rb.append({'loai':'goc','ten':[D,A,B],'do':90})
        else:
            self._diem(A,0.5,2,'above left'); self._diem(B,3.5,2,'above right')
            self._diem(Cc,4,0,'below right'); self._diem(D,0,0,'below left')
        self._da_giac(A, B, Cc, D); return self
    def luc_giac_deu(self, A, B, Cc, D, E, F, canh=2.0, xoay=0, cheo=None, tam=None):
        """Lục giác đều 6 đỉnh, thứ tự A→B→C→D→E→F theo chiều kim đồng hồ.
        Khi xoay=0: cạnh AB (trên) và ED (dưới) nằm ngang; C ở phải, F ở trái.
        canh   = độ dài cạnh (= bán kính đường tròn ngoại tiếp).
        xoay   = góc xoay cả hình (độ).
        cheo   = None | 'chinh' (AD,BE,CF) | 'phu' (AC,BD,CE,DF,EA,FB) | 'tatca'.
        tam    = tên tâm O (đặt → chấm tâm; 3 đường chéo chính đồng quy tại O)."""
        ten    = [A, B, Cc, D, E, F]
        goc0   = [120, 60, 0, -60, -120, 180]                  # A..F, cùng chiều kim đồng hồ
        anchor = ['above left','above right','right','below right','below left','left']
        cx, cy = canh, canh                                    # tâm (giữ toạ độ dương, gọn)
        for t, g, anc in zip(ten, goc0, anchor):
            th = math.radians(g + xoay)
            self._diem(t, cx + canh*math.cos(th), cy + canh*math.sin(th), anc)
        self._da_giac(*ten)
        self.rb.append({'loai':'canh_bang',
                        'cac_doan':[(ten[i], ten[(i+1)%6]) for i in range(6)]})
        for i in range(6):
            self.rb.append({'loai':'goc',
                            'ten':[ten[(i-1)%6], ten[i], ten[(i+1)%6]],
                            'do':120, 'dungsai':0.5})
        if tam:
            self._diem(tam, cx, cy, 'below')   # tâm = giao điểm cho sẵn → ĐEN (Đ40; đỏ chỉ cho yếu tố cần tìm)
        chinh = [(A,D),(B,E),(Cc,F)]
        phu   = [(A,Cc),(B,D),(Cc,E),(D,F),(E,A),(F,B)]
        ds = ([] if cheo is None else
              chinh if cheo=='chinh' else
              phu   if cheo=='phu'   else
              chinh+phu)
        for P_, Q in ds:
            self.tikz.append(('noi', [P_, Q], False, None))
        return self
    def da_giac_deu(self, *ten, canh=2.0, xoay=0, to=None):
        """Đa giác đều n cạnh (n = số tên truyền vào ≥ 3), đỉnh theo chiều kim đồng hồ,
        một cạnh nằm ngang phía trên khi xoay=0. Dùng cho hình NHẬN DẠNG / gây nhiễu
        (ngũ giác, bát giác,…) — KHÔNG vẽ đường chéo. to = màu tô miền (None = không tô).
        Lục giác đều dùng riêng luc_giac_deu (có đường chéo chính/phụ, tâm)."""
        n = len(ten)
        if n < 3:
            raise ValueError('da_giac_deu cần ≥ 3 đỉnh')
        R  = canh / (2*math.sin(math.pi/n))            # bán kính ngoại tiếp từ cạnh
        cx, cy = R, R
        g0 = 90 - 180.0/n                              # cạnh đầu nằm ngang phía trên
        for k, t in enumerate(ten):
            th = math.radians(g0 - k*360.0/n + xoay)   # chiều kim đồng hồ
            x, y = cx + R*math.cos(th), cy + R*math.sin(th)
            ax = 'right' if math.cos(th) > 0.30 else ('left' if math.cos(th) < -0.30 else '')
            ay = 'above' if math.sin(th) > 0.30 else ('below' if math.sin(th) < -0.30 else '')
            self._diem(t, x, y, (ay + ' ' + ax).strip() or 'above')
        self._da_giac(*ten)
        self.rb.append({'loai':'canh_bang',
                        'cac_doan':[(ten[i], ten[(i+1)%n]) for i in range(n)]})
        if to:
            self.tikz.append(('to_mien', list(ten), to))
        return self
    def ngoi_sao(self, tam, so_canh=5, ban_kinh=2.0, xoay=90, ti_le_trong=None, to=None, nhan=None, cham_tam=False):
        """NGÔI SAO so_canh cánh (mặc định 5 — cờ VN/Quốc kỳ; dùng cả 4/6/8 cánh cho Chương V).
        Đỉnh CÁNH trên đường tròn bán kính ban_kinh; đỉnh LÕM trên bán kính trong
        = ban_kinh*ti_le_trong. xoay=90 → một cánh chĩa thẳng LÊN (chuẩn cờ).
        ti_le_trong=None → tự chọn: 5 cánh = 0.382 (pentagram), khác = 0.5.
        tam = tên tâm (dùng làm gốc; cham_tam=True → CHẤM tâm cho bài TÂM đối xứng, mặc định KHÔNG chấm).
        to = màu tô (None = chỉ đường bao). Đỉnh sao đủ 2*so_canh."""
        if so_canh < 3:
            raise ValueError('ngoi_sao cần ≥ 3 cánh')
        if ti_le_trong is None:
            ti_le_trong = 0.382 if so_canh == 5 else 0.5
        R = ban_kinh; r = R*ti_le_trong; cx = cy = R
        if cham_tam:
            self._diem(tam, cx, cy, nhan or 'below')      # chấm tâm (chỉ khi bài TÂM đối xứng)
        dinh = []
        for k in range(so_canh):
            ao = math.radians(xoay + k*360.0/so_canh)         # đỉnh cánh
            ai = math.radians(xoay + (k + 0.5)*360.0/so_canh) # đỉnh lõm
            no = f'{tam}s{k}o'; ni = f'{tam}s{k}i'            # tên KHÔNG mở đầu '_' → khung tính vào
            self._diem(no, cx + R*math.cos(ao), cy + R*math.sin(ao), nhan=None, moc=False)
            self._diem(ni, cx + r*math.cos(ai), cy + r*math.sin(ai), nhan=None, moc=False)
            dinh += [no, ni]
        self._da_giac(*dinh)
        if to:
            self.tikz.append(('to_mien', dinh, to))
        return self
    def hinh_thoi(self, A, B, Cc, D, canh=3.0, goc=60, cheo=False, tam=None):
        """Hình thoi dạng "kim cương": A trái, B trên, C phải, D dưới.
        canh = độ dài cạnh; goc = góc tại đỉnh A (và C), độ (mặc định 60°).
        cheo=True → vẽ 2 đường chéo (AC ngang, BD dọc). tam = tên tâm (chấm)."""
        th = math.radians(goc/2.0)
        p, q = canh*math.cos(th), canh*math.sin(th)          # nửa chéo ngang / dọc
        self._diem(A, 0, q, 'left');    self._diem(B, p, 2*q, 'above')
        self._diem(Cc, 2*p, q, 'right'); self._diem(D, p, 0, 'below')
        self._da_giac(A, B, Cc, D)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(B,Cc),(Cc,D),(D,A)]})
        self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})
        self.rb.append({'loai':'song_song','doan1':(A,D),'doan2':(B,Cc)})
        if cheo:
            self.tikz.append(('noi', [A, Cc], False, None))
            self.tikz.append(('noi', [B, D],  False, None))
        if tam:
            self._diem(tam, p, q, 'below right')   # tâm = giao điểm cho sẵn → ĐEN (Đ40; đỏ chỉ cho yếu tố cần tìm)
        return self
    def hinh_thang_can(self, A, B, Cc, D, day_nho=3.0, day_lon=5.0, cao=2.5, cheo=False):
        """Hình thang cân đối xứng qua trục dọc: A,B = đáy nhỏ (trên); D,C = đáy lớn (dưới).
        A trên-trái, B trên-phải, C dưới-phải, D dưới-trái.
        cheo=True → vẽ 2 đường chéo (AC, BD — bằng nhau)."""
        lech = (day_lon - day_nho)/2.0
        self._diem(D, 0, 0, 'below left');   self._diem(Cc, day_lon, 0, 'below right')
        self._diem(A, lech, cao, 'above left'); self._diem(B, lech+day_nho, cao, 'above right')
        self._da_giac(A, B, Cc, D)
        self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})   # 2 đáy //
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,D),(B,Cc)]})      # 2 cạnh bên =
        if cheo:
            self.tikz.append(('noi', [A, Cc], False, None))
            self.tikz.append(('noi', [B, D],  False, None))
            self.rb.append({'loai':'canh_bang','cac_doan':[(A,Cc),(B,D)]})  # 2 đường chéo =
        return self
    def da_giac_vuong(self, ten, buoc, nhan='below right'):
        """Đa giác mọi cạnh song song trục (góc vuông) — hình chữ L, bậc thang, mặt bằng.
        ten  = list tên đỉnh (n đỉnh), đi quanh chu vi.
        buoc = list n (huong, dai) — huong ∈ {'phai','trai','len','xuong'}, dai>0.
               Đỉnh sinh cộng dồn từ ten[0]=(0,0); TỔNG vector phải = 0 (khép kín).
        (Nhãn cạnh/kích thước AI thêm bằng doan(..., dodai=...).)"""
        huong = {'phai':(1,0), 'trai':(-1,0), 'len':(0,1), 'xuong':(0,-1)}
        n = len(ten)
        if len(buoc) != n:
            raise ValueError('da_giac_vuong: số bước phải bằng số đỉnh (bước cuối khép về đỉnh đầu)')
        x = y = 0.0; toa_do = [(x, y)]
        for hg, dai in buoc[:-1]:
            ux, uy = huong[hg]; x += ux*dai; y += uy*dai; toa_do.append((x, y))
        # kiểm khép kín
        hgc, daic = buoc[-1]; ux, uy = huong[hgc]
        if abs(x + ux*daic) > 1e-6 or abs(y + uy*daic) > 1e-6:
            raise ValueError('da_giac_vuong: chuỗi bước KHÔNG khép kín (tổng vector ≠ 0)')
        for t, (px, py) in zip(ten, toa_do):
            self._diem(t, px, py, nhan)
        self._da_giac(*ten)
        return self
