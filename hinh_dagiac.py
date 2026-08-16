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
        self._diem(B, 0, 0, 'below left')
        self._diem(Cc, canh, 0, 'below right')
        self._diem(A, canh/2, canh*math.sqrt(3)/2, 'above')
        self._da_giac(A, B, Cc)
        self.rb.append({'loai':'canh_bang','cac_doan':[(A,B),(B,Cc),(Cc,A)]}); return self
    def hinh_vuong(self, M, N, P_, Q, canh=3.0):
        self._diem(M, 0, 0, 'below left'); self._diem(N, 0, canh, 'above left')
        self._diem(P_, canh, canh, 'above right'); self._diem(Q, canh, 0, 'below right')
        self._da_giac(M, N, P_, Q)
        self.rb.append({'loai':'canh_bang','cac_doan':[(M,N),(N,P_),(P_,Q),(Q,M)]})
        self.rb.append({'loai':'goc','ten':[Q,M,N],'do':90}); return self
    def hinh_thang(self, A, B, Cc, D, day_tren=3.0, day_duoi=5.0, cao=2.5, lech=0.8):
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
