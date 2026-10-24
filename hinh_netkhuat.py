#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_netkhuat.py — ENGINE NÉT KHUẤT (hidden-line) cho KHỐI ĐA DIỆN LỒI.
#   Triết lý Đ5.9: nét khuất là THUỘC TÍNH HÌNH HỌC → MÁY tự tính, KHÔNG
#   để người khai net='dut' thủ công. Quy tắc (Giám đốc chốt 24/10):
#   "khối đa diện — phần nào BỊ CHE thì nét đứt".
#
#   Mô hình: mỗi điểm có toạ độ 3D (u=ngang, v=sâu, w=cao). Chiếu xiên:
#       x = u + KX·v ;  y = w + KY·v     (KX=CO·cosG, KY=CO·sinG, G=40°, CO=0.5)
#   Người xem ở phía v NHỎ → v lớn = XA (sau). Điểm P bị che ⇔ tồn tại MẶT
#   của khối nằm TRƯỚC P (độ sâu nhỏ hơn) mà hình chiếu phủ P, và P không
#   đồng phẳng mặt đó.
#
#   che_khuat(P0,P1,faces3) → danh sách khúc [(t0,t1,khuat_bool)] để vẽ
#   liền/đứt từng khúc. ADDITIVE, độc lập — không sửa file kho cũ.
# ═══════════════════════════════════════════════════════════════════
import math

_GOC = 40.0
_CO  = 0.5
KX = _CO * math.cos(math.radians(_GOC))
KY = _CO * math.sin(math.radians(_GOC))


def proj(p):
    """(u,v,w) → (x,y) màn."""
    u, v, w = p
    return (u + KX * v, w + KY * v)


def recon3d(x, y, v):
    """Dựng lại (u,v,w) từ vị trí màn (x,y) + độ sâu v đã gán (giữ NGUYÊN
    vị trí màn → layout bài cũ 0 lệch)."""
    return (x - KX * v, v, y - KY * v)


def _in_poly(pt, poly):
    """Điểm trong đa giác (ray-casting), biên tính là trong (nới nhẹ)."""
    x, y = pt
    n = len(poly)
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and \
           (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi):
            inside = not inside
        j = i
    return inside


def _plane(face3):
    """Mặt phẳng n·X = d từ đa giác 3D (lấy 3 đỉnh không cộng tuyến)."""
    p0 = face3[0]
    for i in range(1, len(face3) - 1):
        a, b = face3[i], face3[i + 1]
        e1 = (a[0] - p0[0], a[1] - p0[1], a[2] - p0[2])
        e2 = (b[0] - p0[0], b[1] - p0[1], b[2] - p0[2])
        n = (e1[1] * e2[2] - e1[2] * e2[1],
             e1[2] * e2[0] - e1[0] * e2[2],
             e1[0] * e2[1] - e1[1] * e2[0])
        if n[0] ** 2 + n[1] ** 2 + n[2] ** 2 > 1e-9:
            d = n[0] * p0[0] + n[1] * p0[1] + n[2] * p0[2]
            return n, d
    return None


def _depth_on_plane(x, y, n, d):
    """Độ sâu v của MẶT (n·X=d) tại điểm màn (x,y) dọc tia nhìn
    u=x-KX·v, w=y-KY·v. None nếu mặt song song tia (nhìn nghiêng)."""
    den = n[1] - KX * n[0] - KY * n[2]
    if abs(den) < 1e-9:
        return None
    return (d - n[0] * x - n[2] * y) / den


def che_khuat(P0, P1, faces3, nsamp=200, eps=6e-3, cop=5e-3):
    """Đoạn 3D P0→P1 bị các MẶT faces3 che tới đâu.
    Trả [(t0,t1,khuat)] gộp khúc. khuat=True ⇒ vẽ nét đứt.
      eps : ngưỡng 'mặt nằm trước' (sâu nhỏ hơn) mới tính che.
      cop : ngưỡng đồng phẳng (điểm NẰM TRÊN mặt → mặt đó không tự che)."""
    planes = []
    for f in faces3:
        pl = _plane(f)
        if pl is None:
            continue
        poly = [proj(p) for p in f]
        planes.append((pl[0], pl[1], poly))

    def lerp(t):
        return (P0[0] + (P1[0] - P0[0]) * t,
                P0[1] + (P1[1] - P0[1]) * t,
                P0[2] + (P1[2] - P0[2]) * t)

    def hidden_at(t):
        P = lerp(t)
        sx, sy = proj(P)
        dv = P[1]
        for n, d, poly in planes:
            # P nằm TRÊN mặt → mặt này không che chính nó
            if abs(n[0] * P[0] + n[1] * P[1] + n[2] * P[2] - d) < cop:
                continue
            if not _in_poly((sx, sy), poly):
                continue
            vf = _depth_on_plane(sx, sy, n, d)
            if vf is None:
                continue
            if dv > vf + eps:            # mặt ở TRƯỚC P (sâu nhỏ hơn) → che
                return True
        return False

    # lấy mẫu + gộp khúc, tinh biên bằng nhị phân
    xs = [i / nsamp for i in range(nsamp + 1)]
    flags = [hidden_at(t) for t in xs]
    segs = []
    t_start = 0.0
    cur = flags[0]
    for i in range(1, len(xs)):
        if flags[i] != cur:
            # tinh điểm chuyển giữa xs[i-1], xs[i]
            lo, hi = xs[i - 1], xs[i]
            for _ in range(24):
                mid = (lo + hi) / 2
                if hidden_at(mid) == cur:
                    lo = mid
                else:
                    hi = mid
            tb = (lo + hi) / 2
            segs.append((t_start, tb, cur))
            t_start = tb
            cur = flags[i]
    segs.append((t_start, 1.0, cur))
    # gộp khúc quá ngắn (nhiễu mẫu) vào khúc kề
    out = []
    for s in segs:
        if out and (s[1] - s[0]) < 8e-3 and out[-1][2] != s[2]:
            # khúc nhiễu cực ngắn: nối dài khúc trước
            out[-1] = (out[-1][0], s[1], out[-1][2])
        else:
            out.append(list(s))
    # hợp nhất 2 khúc kề cùng trạng thái
    merged = []
    for s in out:
        if merged and merged[-1][2] == s[2]:
            merged[-1][1] = s[1]
        else:
            merged.append(list(s))
    return [(a, b, h) for a, b, h in merged]
