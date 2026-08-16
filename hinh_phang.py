#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_phang.py — GÓI LUẬT KIỂM 2D + helper đo (tách khỏi lõi, 12/08/2026)
#   Mọi luật ở đây tự ĐĂNG KÝ vào lõi khi import (C.dang_ky).
#   HHKG lớp 8 sẽ có hinh_kg.py song song, đăng ký luật 3D — không đụng file này.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_core as C

# ─────────── QUY ƯỚC tên góc ⟺ tia ───────────
def _doc(ten):                       # [x,A,B] → (đỉnh A, cạnh x, cạnh B)
    return ten[1], ten[0], ten[2]

def _do_goc(V, ten):                 # đo góc thực từ tọa độ
    d,c1,c2 = _doc(ten); O,P,Q = V[d],V[c1],V[c2]
    v1=(P[0]-O[0],P[1]-O[1]); v2=(Q[0]-O[0],Q[1]-O[1])
    return math.degrees(math.acos(max(-1,min(1,
        (v1[0]*v2[0]+v1[1]*v2[1])/(math.hypot(*v1)*math.hypot(*v2))))))

def _thu_tu(V, ten):                 # thứ tự tia cho cung quét ≤180°
    d,c1,c2 = _doc(ten); O,P,Q = V[d],V[c1],V[c2]
    a1=math.degrees(math.atan2(P[1]-O[1],P[0]-O[0]))
    a2=math.degrees(math.atan2(Q[1]-O[1],Q[0]-O[0]))
    return [c2,d,c1] if (a2-a1)%360>180 else [c1,d,c2]

# ═══════════ ĐO CÁC QUAN HỆ ═══════════
def _lech_thang_hang(V, diem):
    """Độ lệch khỏi thẳng hàng (khoảng cách vuông góc lớn nhất)."""
    A,B = V[diem[0]], V[diem[1]]
    L = math.hypot(B[0]-A[0], B[1]-A[1]) or 1
    lech = 0
    for P in diem[2:]:
        Pp = V[P]
        cross = abs((B[0]-A[0])*(Pp[1]-A[1]) - (B[1]-A[1])*(Pp[0]-A[0]))
        lech = max(lech, cross/L)
    return lech

def _lech_trung_diem(V, M, A, B):
    Mp,Ap,Bp = V[M],V[A],V[B]
    mid = ((Ap[0]+Bp[0])/2,(Ap[1]+Bp[1])/2)
    lech = math.hypot(Mp[0]-mid[0], Mp[1]-mid[1])
    dAM = math.hypot(Mp[0]-Ap[0],Mp[1]-Ap[1])
    dMB = math.hypot(Mp[0]-Bp[0],Mp[1]-Bp[1])
    dAB = math.hypot(Bp[0]-Ap[0],Bp[1]-Ap[1])
    nam_giua = abs(dAM+dMB-dAB) < 1e-6
    return lech, nam_giua

def _khoang_cach(V, A, B):
    return math.hypot(V[A][0]-V[B][0], V[A][1]-V[B][1])

def _kc_diem_duong(V, P, A, B):
    """Khoảng cách vuông góc từ điểm P tới đường thẳng qua A,B."""
    Ap,Bp,Pp = V[A],V[B],V[P]
    L = math.hypot(Bp[0]-Ap[0], Bp[1]-Ap[1]) or 1
    return abs((Bp[0]-Ap[0])*(Pp[1]-Ap[1]) - (Bp[1]-Ap[1])*(Pp[0]-Ap[0]))/L

def _lech_song_song(V, A, B, Cc, D):
    v1=(V[B][0]-V[A][0], V[B][1]-V[A][1]); v2=(V[D][0]-V[Cc][0], V[D][1]-V[Cc][1])
    L1=math.hypot(*v1) or 1; L2=math.hypot(*v2) or 1
    return abs(v1[0]*v2[1]-v1[1]*v2[0])/(L1*L2)   # |sin góc lệch|

def _goc_huong(V, O, P):              # góc (độ) của tia OP so ngang, [0,360)
    return math.degrees(math.atan2(V[P][1]-V[O][1], V[P][0]-V[O][0])) % 360

# ═══════════ LUẬT KIỂM — đăng ký vào lõi ═══════════
def _kt_goc(V, rb):
    thuc = _do_goc(V, rb['ten']); ds = rb.get('dungsai', 0.5)
    if abs(thuc-rb['do']) > ds:
        raise ValueError(f"[PHANH DỪNG] Góc {''.join(rb['ten'])} đề ghi "
            f"{rb['do']}° nhưng hình dựng {thuc:.1f}°. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_thang_hang(V, rb):
    lech = _lech_thang_hang(V, rb['diem']); ds = rb.get('dungsai', 0.01)
    if lech > ds:
        raise ValueError(f"[PHANH DỪNG] Các điểm {','.join(rb['diem'])} khai THẲNG HÀNG "
            f"nhưng lệch {lech:.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_khong_thang_hang(V, rb):
    lech = _lech_thang_hang(V, rb['diem']); ds = rb.get('dungsai', 0.05)
    if lech <= ds:
        raise ValueError(f"[PHANH DỪNG] {','.join(rb['diem'])} khai KHÔNG thẳng hàng "
            f"nhưng gần thẳng hàng (lệch {lech:.3f}). Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_trung_diem(V, rb):
    M = rb['M']; A,B = rb['doan']
    lech, giua = _lech_trung_diem(V, M, A, B); ds = rb.get('dungsai', 0.01)
    if lech > ds:
        raise ValueError(f"[PHANH DỪNG] {M} khai TRUNG ĐIỂM {A}{B} nhưng lệch điểm giữa "
            f"{lech:.3f} ({M}{A}≠{M}{B}). Sửa tọa độ, KHÔNG ra hình sai.")
    if not giua:
        raise ValueError(f"[PHANH DỪNG] {M} khai TRUNG ĐIỂM {A}{B} nhưng KHÔNG nằm giữa "
            f"{A}-{B}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_nam_giua(V, rb):
    ten = rb['diem']; A,B = rb['doan']
    _, giua = _lech_trung_diem(V, ten, A, B)
    lech = _lech_thang_hang(V, [A, ten, B]); ds = rb.get('dungsai', 0.01)
    if lech > ds or not giua:
        raise ValueError(f"[PHANH DỪNG] {ten} khai NẰM GIỮA {A}-{B} nhưng không nằm trên "
            f"đoạn (lệch {lech:.3f}). Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_khoang_cach(V, rb):
    A,B = rb['doan']; thuc = _khoang_cach(V,A,B); ds = rb.get('dungsai', 0.01)
    if abs(thuc-rb['do']) > ds:
        raise ValueError(f"[PHANH DỪNG] Đoạn {A}{B} khai {rb['do']} nhưng dựng "
            f"{thuc:.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_song_song(V, rb):
    A,B = rb['doan1']; Cc,D = rb['doan2']; ds=rb.get('dungsai',0.02)
    lech=_lech_song_song(V,A,B,Cc,D)
    if lech>ds:
        raise ValueError(f"[PHANH DỪNG] {A}{B} và {Cc}{D} khai SONG SONG nhưng lệch "
            f"{lech:.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_cat(V, rb):
    """2 đường (mỗi đường = cặp điểm) khai CẮT → phải KHÔNG song song."""
    A,B = rb['doan1']; Cc,D = rb['doan2']; ds=rb.get('dungsai',0.02)
    lech=_lech_song_song(V,A,B,Cc,D)
    if lech<=ds:
        raise ValueError(f"[PHANH DỪNG] {A}{B} và {Cc}{D} khai CẮT NHAU nhưng song song "
            f"(lệch {lech:.3f}). Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_canh_bang(V, rb):
    ds=rb.get('dungsai',0.02); doan=rb['cac_doan']
    do_dai=[_khoang_cach(V,a,b) for a,b in doan]
    if max(do_dai)-min(do_dai) > ds:
        raise ValueError(f"[PHANH DỪNG] Các cạnh {doan} khai BẰNG NHAU nhưng lệch "
            f"{max(do_dai)-min(do_dai):.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_diem_tren_duong(V, rb):
    P = rb['diem']; A,B = rb['qua']; ds=rb.get('dungsai',0.02)
    kc=_kc_diem_duong(V,P,A,B)
    if kc>ds:
        raise ValueError(f"[PHANH DỪNG] {P} khai THUỘC đường {A}{B} nhưng cách "
            f"{kc:.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_diem_ngoai_duong(V, rb):
    P = rb['diem']; A,B = rb['qua']; ds=rb.get('dungsai',0.15)
    kc=_kc_diem_duong(V,P,A,B)
    if kc<ds:
        raise ValueError(f"[PHANH DỪNG] {P} khai NGOÀI đường {A}{B} nhưng nằm sát/trên "
            f"(cách {kc:.3f}). Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_nut_luoi(V, rb):
    P=rb['diem']; x,y=V[P]; step=rb.get('step',1.0)
    cx,cy=round(x/step),round(y/step)
    if abs(x-cx*step)>1e-6 or abs(y-cy*step)>1e-6:
        raise ValueError(f"[PHANH DỪNG] {P} khai tại NÚT LƯỚI nhưng lệch nút. KHÔNG ra hình sai.")
    if 'cot' in rb and 'hang' in rb and not (0<=cx<=rb['cot'] and 0<=cy<=rb['hang']):
        raise ValueError(f"[PHANH DỪNG] {P} ở nút ({cx},{cy}) NGOÀI lưới "
            f"{rb['cot']}×{rb['hang']}. KHÔNG ra hình sai.")

def _kt_diem_trong_goc(V, rb):
    c1,dinh,c2 = rb['goc']; P = rb['diem']
    a1=_goc_huong(V,dinh,c1); a2=_goc_huong(V,dinh,c2); ap=_goc_huong(V,dinh,P)
    # chuẩn hóa để c1 là mốc 0, quét ngược chiều kim tới c2
    span=(a2-a1)%360; off=(ap-a1)%360
    ds=rb.get('dungsai',0.5)
    ben_trong = ds < off < span-ds if span<=180 else False
    if span>180:  # lấy miền ≤180 (miền trong của góc hình học)
        span=360-span; off=(a1-ap)%360; ben_trong = ds < off < span-ds
    if not ben_trong:
        raise ValueError(f"[PHANH DỪNG] {P} khai NẰM TRONG góc {c1}{dinh}{c2} nhưng ở ngoài/"
            f"trên cạnh. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_diem_ngoai_goc(V, rb):
    """Đối xứng _kt_diem_trong_goc: điểm PHẢI nằm NGOÀI miền trong (≤180) của góc."""
    c1,dinh,c2 = rb['goc']; P = rb['diem']
    a1=_goc_huong(V,dinh,c1); a2=_goc_huong(V,dinh,c2); ap=_goc_huong(V,dinh,P)
    span=(a2-a1)%360; off=(ap-a1)%360
    ds=rb.get('dungsai',0.5)
    ben_trong = ds < off < span-ds if span<=180 else False
    if span>180:  # lấy miền ≤180 (miền trong của góc hình học)
        span=360-span; off=(a1-ap)%360; ben_trong = ds < off < span-ds
    if ben_trong:
        raise ValueError(f"[PHANH DỪNG] {P} khai NẰM NGOÀI góc {c1}{dinh}{c2} nhưng lại nằm "
            f"TRONG góc. Sửa tọa độ, KHÔNG ra hình sai.")

for _loai,_ham in [
    ('goc',_kt_goc),('thang_hang',_kt_thang_hang),('khong_thang_hang',_kt_khong_thang_hang),
    ('trung_diem',_kt_trung_diem),('nam_giua',_kt_nam_giua),('khoang_cach',_kt_khoang_cach),
    ('song_song',_kt_song_song),('cat',_kt_cat),('trung',_kt_thang_hang),  # trùng ⟺ thẳng hàng 4 mút
    ('canh_bang',_kt_canh_bang),('diem_tren_duong',_kt_diem_tren_duong),
    ('diem_ngoai_duong',_kt_diem_ngoai_duong),('nut_luoi',_kt_nut_luoi),
    ('diem_trong_goc',_kt_diem_trong_goc),
    ('diem_ngoai_goc',_kt_diem_ngoai_goc),
]:
    C.dang_ky(_loai,_ham)

# ─────────── Ô VUÔNG tự động cho góc 90° (2D render) ───────────
def _o_vuong(V, ten, mau="orange", d=0.32):
    tt = _thu_tu(V, ten); c1,dinh,c2 = tt; O = V[dinh]
    def diem_cach(P):
        vx,vy = V[P][0]-O[0], V[P][1]-O[1]; L = math.hypot(vx,vy) or 1
        return (O[0]+vx/L*d, O[1]+vy/L*d)
    p1=diem_cach(c1); p2=diem_cach(c2); p3=(p1[0]+p2[0]-O[0], p1[1]+p2[1]-O[1])
    return (f'  \\draw[draw={mau},thick] ({p1[0]:.3f},{p1[1]:.3f})--'
            f'({p3[0]:.3f},{p3[1]:.3f})--({p2[0]:.3f},{p2[1]:.3f});')
