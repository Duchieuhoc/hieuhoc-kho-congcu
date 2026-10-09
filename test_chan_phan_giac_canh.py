import sys, math
sys.path.insert(0, '/home/claude/kho_b12')
import hinh_tamgiac as H3

h = H3.Hinh()
# HBH ABCD, AB > BC (dài ngang). A trên-trái, B trên-phải, C dưới-phải, D dưới-trái.
h.tu_giac('A', 'B', 'Cc', 'D', loai='binh_hanh')
V = h.V
print("Đỉnh:", {k: (round(v[0],3), round(v[1],3)) for k,v in V.items() if not k.startswith(('_','R'))})

# Phân giác góc D (hai tia DA, DC) cắt AB tại E
h.chan_phan_giac_canh('E', 'D', 'A', 'Cc', cat=('A', 'B'))
# Phân giác góc B (hai tia BA, BC) cắt CD tại F
h.chan_phan_giac_canh('F', 'B', 'A', 'Cc', cat=('Cc', 'D'))

def ang(V, c1, d, c2):
    O, P, Q = V[d], V[c1], V[c2]
    v1 = (P[0]-O[0], P[1]-O[1]); v2 = (Q[0]-O[0], Q[1]-O[1])
    return math.degrees(math.acos(max(-1,min(1,(v1[0]*v2[0]+v1[1]*v2[1])/(math.hypot(*v1)*math.hypot(*v2))))))

def dist(V,a,b): return math.hypot(V[a][0]-V[b][0], V[a][1]-V[b][1])

print("\n--- Kiểm bisector góc D ---")
aADE = ang(V,'A','D','E'); aEDC = ang(V,'E','D','Cc')
print(f"góc ADE = {aADE:.5f}°, góc EDC = {aEDC:.5f}°, lệch = {abs(aADE-aEDC):.6f}°")

print("--- Kiểm bisector góc B ---")
aABF = ang(V,'A','B','F'); aFBC = ang(V,'F','B','Cc')
print(f"góc ABF = {aABF:.5f}°, góc FBC = {aFBC:.5f}°, lệch = {abs(aABF-aFBC):.6f}°")

print("\n--- Kiểm tính chất tam giác cân (AE = AD) ---")
AE = dist(V,'A','E'); AD = dist(V,'A','D')
print(f"AE = {AE:.5f}, AD = {AD:.5f}, lệch = {abs(AE-AD):.6f}")
CF = dist(V,'Cc','F'); CB = dist(V,'Cc','B')
print(f"CF = {CF:.5f}, CB = {CB:.5f}, lệch = {abs(CF-CB):.6f}")

# E có nằm trên đoạn AB (giữa A,B)?
def tren_doan(V,P,A,B):
    d1=dist(V,A,P); d2=dist(V,P,B); d=dist(V,A,B)
    return abs(d1+d2-d) < 1e-6
print("\nE nằm trên đoạn AB:", tren_doan(V,'E','A','B'))
print("F nằm trên đoạn CD:", tren_doan(V,'F','Cc','D'))

# PHANH tổng
import hinh_core as C
C.phanh(h.V, h.rb)
print("\nPHANH: PASS (không raise)")

# Render thử ra PNG
try:
    png = h.ve('test_pgcanh')
    print("Render:", png)
except Exception as e:
    print("Render lỗi:", e)
