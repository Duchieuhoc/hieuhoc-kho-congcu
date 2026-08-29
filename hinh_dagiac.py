#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_dagiac.py — MẠCH "ĐA GIÁC & HÌNH PHẲNG" (tam giác·tứ giác·đa giác đều·hình phẳng đặc biệt)
#   Kế thừa HinhCoBan. Dùng chung Lớp 6→8 (L7 thêm dấu bằng, L8 thêm đồng dạng — cùng hàm).
#   LOP_MODULE gợi ý: [6,7,8]. Tách 13/08/2026 từ hinh_ch8 (MO_HINH_KHO_HINH_THCS).
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_coban

class HinhDaGiac(hinh_coban.HinhCoBan):
    def tam_giac_deu(self, A, B, Cc, canh=3.0, xoay=0, goc_o=(0.0, 0.0)):
        """Tam giác ĐỀU 3 đỉnh: B dưới-trái, C dưới-phải, A đỉnh trên. canh = độ dài cạnh
        (mặc định 3.0). Ba cạnh bằng nhau (PHANH canh_bang). Dùng nhận dạng / hình nền.
        goc_o=(dx,dy): DỜI cả tam giác đi (dx,dy) đơn vị vẽ — đặt NHIỀU tam giác cạnh nhau
        trong 1 hình (hình nhận dạng cặp/bộ tam giác bằng nhau); mặc định (0,0) = gốc."""
        ox, oy = goc_o
        self._diem(B, ox+0, oy+0, 'below left')
        self._diem(Cc, ox+canh, oy+0, 'below right')
        self._diem(A, ox+canh/2, oy+canh*math.sqrt(3)/2, 'above')
        self._da_giac(A, B, Cc)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(B,Cc),(Cc,A)]}); return self
    def hinh_vuong(self, M, N, P_, Q, canh=4):
        """Hình VUÔNG: M dưới-trái, N trên-trái, P trên-phải, Q dưới-phải. canh = độ dài cạnh (dùng CHẴN ô để tâm rơi NÚT lưới).
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
    def tam_giac(self, A, B, Cc, noi=True, goc_o=(0.0, 0.0)):
        """Tam giác 3 đỉnh (không thẳng hàng). Thứ tự A→B→C chiều kim đồng hồ.
        noi=False → chỉ ĐẶT 3 điểm (không nối cạnh) — dùng cho 'ba điểm không thẳng hàng'.
        goc_o=(dx,dy): DỜI cả tam giác đi (dx,dy) đơn vị vẽ — đặt NHIỀU tam giác cạnh nhau
        trong 1 hình (hình nhận dạng cặp/bộ tam giác bằng nhau); mặc định (0,0) = gốc."""
        ox, oy = goc_o
        self._diem(A, ox+1.4, oy+2.2, 'above'); self._diem(B, ox+2.8, oy+0, 'below right')
        self._diem(Cc, ox+0, oy+0, 'below left')
        if noi: self._da_giac(A, B, Cc)
        self.rb.append({'loai':'khong_thang_hang','diem':[A,B,Cc]}); return self
    def tam_giac_can(self, A, B, Cc, canh_ben=3.0, day=2.4, danh_dau=True, goc_o=(0.0, 0.0)):
        """Tam giác CÂN tại đỉnh A (A đỉnh trên; B–C đáy nằm ngang, B trái–C phải).
        canh_ben = AB = AC (cạnh bên); day = BC (đáy). PHANH canh_bang (AB, AC).
        danh_dau=True → tự vạch 1 gạch lên AB và AC (ký hiệu 2 cạnh bên bằng nhau);
        đặt False khi hình chỉ ghi số đo, không hiện vạch. Yêu cầu canh_ben > day/2.
        Cân tại đỉnh KHÁC → truyền đỉnh cân vào vị trí A (A luôn là đỉnh cân).
        goc_o=(dx,dy): DỜI cả tam giác đi (dx,dy) đơn vị vẽ — đặt NHIỀU tam giác cạnh nhau
        trong 1 hình (hình nhận dạng cặp/bộ tam giác bằng nhau); mặc định (0,0) = gốc."""
        h2 = canh_ben**2 - (day/2.0)**2
        if h2 <= 0:
            raise ValueError(f"[tam_giac_can] canh_ben={canh_ben} phải > day/2={day/2.0} để có tam giác thật.")
        h = math.sqrt(h2)
        ox, oy = goc_o
        self._diem(B, ox+0, oy+0, 'below left')
        self._diem(Cc, ox+day, oy+0, 'below right')
        self._diem(A, ox+day/2.0, oy+h, 'above')
        self._da_giac(A, B, Cc)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(A,Cc)]})
        if danh_dau:
            self.dau_bang(A, B, 1); self.dau_bang(A, Cc, 1)
        return self
    def tam_giac_goc(self, A, B, Cc, goc_B, goc_C, day=4.0, goc_o=(0.0, 0.0)):
        """Tam giác ABC với GÓC cho sẵn: góc tại B = goc_B, góc tại C = goc_C
        (góc A tự = 180 − goc_B − goc_C). Đáy BC nằm ngang: B dưới-trái (0,0),
        C dưới-phải (day,0); A đỉnh trên = giao hai tia BA, CA. VẼ SẠCH 3 cạnh
        (KHÔNG tia thừa, KHÔNG nhãn phụ). PHANH kiểm CẢ BA góc (±0,5°).
        Yêu cầu goc_B, goc_C > 0 và goc_B + goc_C < 180 để có tam giác thật.
        Số đo hiện qua so_do_goc((cạnh1,đỉnh,cạnh2)) gọi SAU — tuỳ hình lộ góc nào;
        góc vuông đánh bằng goc_vuong((cạnh1,đỉnh,cạnh2)). Xương sống mạch tính-góc
        tam giác (HH7-CH04 → tam giác thường theo góc mọi lớp).
        goc_o=(dx,dy): DỜI cả tam giác đi (dx,dy) đơn vị vẽ — đặt NHIỀU tam giác cạnh nhau
        trong 1 hình (hình nhận dạng cặp/bộ tam giác bằng nhau); mặc định (0,0) = gốc."""
        goc_A = 180.0 - goc_B - goc_C
        if goc_B <= 0 or goc_C <= 0 or goc_A <= 0:
            raise ValueError(f"[tam_giac_goc] góc B={goc_B}°, C={goc_C}° ⇒ A={goc_A}°: "
                f"mỗi góc phải > 0 và goc_B + goc_C < 180 để có tam giác thật.")
        if day <= 0:
            raise ValueError(f"[tam_giac_goc] day={day} phải > 0.")
        bR = math.radians(goc_B); cR = math.radians(goc_C)
        ba = day * math.sin(cR) / math.sin(bR + cR)   # BA = day·sinC / sin(B+C)
        xA = ba * math.cos(bR); yA = ba * math.sin(bR)
        ox, oy = goc_o
        self._diem(B, ox+0.0, oy+0.0, 'below left')
        self._diem(Cc, ox+day, oy+0.0, 'below right')
        self._diem(A, ox+xA, oy+yA, 'above')
        self._da_giac(A, B, Cc)
        # PHANH: đối chiếu CẢ BA góc (đỉnh Ở GIỮA: ten=[cạnh1, đỉnh, cạnh2])
        self.rb.append({'loai':'goc','ten':[A, B, Cc],'do': round(goc_B, 6)})
        self.rb.append({'loai':'goc','ten':[A, Cc, B],'do': round(goc_C, 6)})
        self.rb.append({'loai':'goc','ten':[B, A, Cc],'do': round(goc_A, 6)})
        self.rb.append({'loai':'khong_thang_hang','diem':[A, B, Cc]})
        return self
    def diem_doi_xung_truc(self, new, P, A, B, nhan='above right', mau=None):
        """Đặt điểm 'new' = ẢNH của điểm P qua TRỤC (đường thẳng) AB — phản chiếu.
        P, A, B phải ĐÃ đặt trước. Máy tự tính ảnh (KHÔNG cho toạ độ). Dùng dựng
        điểm đối xứng: điểm thứ 4 hình cánh diều (AC=AD, BC=BD), ảnh qua trục,
        đỉnh tam giác cân... dau_bang/so_do_goc gọi SAU để đánh dấu/kiểm."""
        for t in (P, A, B):
            if t not in self.V:
                raise ValueError(f"[diem_doi_xung_truc] điểm '{t}' chưa đặt.")
        px, py = self.V[P]; ax, ay = self.V[A]; bx, by = self.V[B]
        dx, dy = bx - ax, by - ay
        d2 = dx*dx + dy*dy
        if d2 < 1e-12:
            raise ValueError("[diem_doi_xung_truc] A≡B: trục không xác định.")
        t = ((px - ax)*dx + (py - ay)*dy) / d2      # chiếu P lên AB
        fx, fy = ax + t*dx, ay + t*dy                # chân vuông góc
        self._diem(new, 2*fx - px, 2*fy - py, nhan, mau=mau)   # P' = 2F − P
        return self
    def tam_giac_canh(self, A, B, Cc, AB, BC, CA, goc_o=(0.0, 0.0)):
        """Tam giác ABC dựng từ 3 CẠNH cho sẵn (SSS): |AB|, |BC|, |CA| (đơn vị bất kỳ,
        giữ ĐÚNG TỈ LỆ). Đáy BC nằm ngang: B dưới-trái (0,0), C dưới-phải (BC,0);
        A đỉnh trên = giao hai đường tròn (tâm B bk AB) ∩ (tâm C bk CA). VẼ SẠCH 3 cạnh.
        Dùng cho 'dựng tam giác biết ba cạnh' bằng compa (đề 4-5-6…) — A đặt ĐÚNG chỗ
        giao, hai cung sau đó có bán kính AB, CA khớp. PHANH kiểm 3 điểm không thẳng hàng.
        Bất đẳng thức tam giác phải thoả (tổng 2 cạnh > cạnh còn lại).
        goc_o=(dx,dy): DỜI cả tam giác đi (dx,dy) đơn vị vẽ — đặt NHIỀU tam giác cạnh nhau
        trong 1 hình (hình nhận dạng cặp/bộ tam giác bằng nhau); mặc định (0,0) = gốc."""
        AB, BC, CA = float(AB), float(BC), float(CA)
        for a, b, c, ten in [(AB,CA,BC,'AB+CA'),(AB,BC,CA,'AB+BC'),(BC,CA,AB,'BC+CA')]:
            if a + b <= c + 1e-9:
                raise ValueError(f"[tam_giac_canh] {ten} ≤ cạnh còn lại — không thành tam giác "
                    f"(AB={AB}, BC={BC}, CA={CA}).")
        xA = (AB*AB - CA*CA + BC*BC) / (2.0 * BC)
        yA2 = AB*AB - xA*xA
        if yA2 <= 0:
            raise ValueError(f"[tam_giac_canh] bộ cạnh suy biến (AB={AB}, BC={BC}, CA={CA}).")
        import math as _m
        yA = _m.sqrt(yA2)
        ox, oy = goc_o
        self._diem(B, ox+0.0, oy+0.0, 'below left')
        self._diem(Cc, ox+BC, oy+0.0, 'below right')
        self._diem(A, ox+xA, oy+yA, 'above')
        self._da_giac(A, B, Cc)
        self.rb.append({'loai':'khong_thang_hang','diem':[A, B, Cc]})
        return self
    def tu_giac(self, A, B, Cc, D, loai=None):
        """Tứ giác 4 đỉnh lồi, chiều kim đồng hồ. loai∈{None,'binh_hanh','chu_nhat'}."""
        if loai == 'binh_hanh':
            self._diem(A,1,2,'above left'); self._diem(B,4,2,'above right')
            self._diem(Cc,3,0,'below right'); self._diem(D,0,0,'below left')  # tâm (2,1) NÚT
            self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})
            self.rb.append({'loai':'song_song','doan1':(A,D),'doan2':(B,Cc)})
        elif loai == 'chu_nhat':
            self._diem(A,0,2,'above left'); self._diem(B,4,2,'above right')
            self._diem(Cc,4,0,'below right'); self._diem(D,0,0,'below left')  # tâm (2,1) NÚT
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
    def chu_so_7doan(self, so, x0=0.0, y0=0.0, rong=1.0, cao=2.0, mau=None, rong_net='dam'):
        """CHỮ SỐ kiểu 7-ĐOẠN (0..9) — cho bài TÂM đối xứng (lật nửa vòng 6↔9, giữ 0/1/2/5/8).
        Vẽ tại góc dưới-trái (x0,y0); rộng 'rong', cao 'cao' (đơn vị vẽ, mặc định 1×2 ô).
        Mỗi đoạn = nét ĐẬM. Gọi NHIỀU lần (đổi x0) để đặt các thẻ số cạnh nhau.
        rong_net ∈ {'vua','dam','rat_dam'}. mau=None → đen."""
        so = str(so)
        SEG = {'0':'abcdef','1':'bc','2':'abged','3':'abgcd','4':'fgbc',
               '5':'afgcd','6':'afgecd','7':'abc','8':'abcdefg','9':'abcdfg'}
        if so not in SEG:
            raise ValueError(f'chu_so_7doan chỉ nhận 0..9, nhận: {so!r}')
        # 6 nút của khung số
        TL=(x0,      y0+cao);   TR=(x0+rong, y0+cao)
        ML=(x0,      y0+cao/2); MR=(x0+rong, y0+cao/2)
        BL=(x0,      y0);       BR=(x0+rong, y0)
        DOAN = {'a':(TL,TR),'b':(TR,MR),'c':(MR,BR),
                'd':(BL,BR),'e':(BL,ML),'f':(TL,ML),'g':(ML,MR)}
        if not hasattr(self,'_so7_id'): self._so7_id = 0
        self._so7_id += 1; tag = self._so7_id
        for s in SEG[so]:
            p1,p2 = DOAN[s]
            n1=f'_s7_{tag}_{s}1'; n2=f'_s7_{tag}_{s}2'
            self._diem(n1,p1[0],p1[1],nhan=None,moc=False)
            self._diem(n2,p2[0],p2[1],nhan=None,moc=False)
            self.tikz.append(('doan', n1, n2, mau, 'lien', rong_net))
        return self

    def hinh_thoi(self, A, B, Cc, D, a=4, b=3, cheo=True, tam='O'):
        """Hình thoi "kim cương" dựng theo 2 nửa chéo NGUYÊN ô → tâm + 4 đỉnh rơi NÚT lưới.
        a = nửa chéo NGANG (ô; OA = OC);  b = nửa chéo DỌC (ô; OB = OD).
        A trái, B trên, C phải, D dưới. cheo=True vẽ 2 chéo (AC ngang, BD dọc).
        tam = tên tâm O (chấm; None để bỏ). (Đổi từ cạnh+góc → chéo-lưới, mốc 26g.)"""
        a = int(round(a)); b = int(round(b))
        ox, oy = a, b                                          # đặt O tại nút (a,b) → mọi toạ độ ≥ 0
        self._diem(A, ox-a, oy, 'left');    self._diem(B, ox, oy+b, 'above')
        self._diem(Cc, ox+a, oy, 'right');  self._diem(D, ox, oy-b, 'below')
        self._da_giac(A, B, Cc, D)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(B,Cc),(Cc,D),(D,A)]})
        self.rb.append({'loai':'song_song','doan1':(A,B),'doan2':(D,Cc)})
        self.rb.append({'loai':'song_song','doan1':(A,D),'doan2':(B,Cc)})
        if cheo:
            self.tikz.append(('noi', [A, Cc], False, None))
            self.tikz.append(('noi', [B, D],  False, None))
        if tam:
            self._diem(tam, ox, oy, 'below right')             # tâm cho sẵn → ĐEN (Đ40)
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
