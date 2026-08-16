#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_tron.py — GÓI LUẬT KIỂM ĐƯỜNG TRÒN (tách khỏi lõi, 15/08/2026)
#   Song sinh với hinh_phang.py: mọi luật ở đây tự ĐĂNG KÝ vào lõi khi import
#   (C.dang_ky). Semantic `hinh_tron_ve.py` import file này → luật sẵn sàng.
#
#   PHẠM VI HIỆN TẠI (L6 dùng thật — đồng hồ, vòng quay, compa):
#     • điểm ∈ (O) ⇔ khoảng cách tới tâm = bán kính  [luật 'diem_tren_tron']
#     • vị trí điểm trên (O) do GÓC Ở TÂM quyết định (không tọa độ — Đ5.9),
#       kiểm gián tiếp qua khoảng cách + (tùy chọn) góc ở tâm  [luật 'goc_o_tam']
#   ĐỂ LỚP 9 (chưa xây — MO_HINH_KHO_HINH_THCS §3): dây · tiếp tuyến ·
#     góc nội tiếp = ½ góc ở tâm · tứ giác nội tiếp. Thêm luật vào ĐÂY, không mổ lõi.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_core as C

# ═══════════ ĐO QUAN HỆ ĐƯỜNG TRÒN ═══════════
def _kc_toi_tam(V, diem, tam):
    return math.hypot(V[diem][0]-V[tam][0], V[diem][1]-V[tam][1])

def _goc_o_tam(V, tam, A, B):
    """Góc ở tâm (độ, 0..360 rồi lấy ≤180) chắn bởi 2 bán kính OA, OB."""
    ax, ay = V[A][0]-V[tam][0], V[A][1]-V[tam][1]
    bx, by = V[B][0]-V[tam][0], V[B][1]-V[tam][1]
    d = math.degrees(math.acos(max(-1, min(1,
        (ax*bx+ay*by)/((math.hypot(ax,ay) or 1)*(math.hypot(bx,by) or 1))))))
    return d

# ═══════════ LUẬT KIỂM — đăng ký vào lõi ═══════════
def _kt_diem_tren_tron(V, rb):
    """Điểm khai NẰM TRÊN (O) → khoảng cách tới tâm phải = bán kính."""
    P = rb['diem']; tam = rb['tam']; r = rb['ban_kinh']
    ds = rb.get('dungsai', 0.02)
    kc = _kc_toi_tam(V, P, tam)
    if abs(kc - r) > ds:
        raise ValueError(f"[PHANH DỪNG] {P} khai THUỘC đường tròn tâm {tam} bán kính "
            f"{r} nhưng cách tâm {kc:.3f}. Sửa tọa độ, KHÔNG ra hình sai.")

def _kt_goc_o_tam(V, rb):
    """Kiểm góc ở tâm giữa 2 bán kính OA, OB đúng số đo khai."""
    tam = rb['tam']; A, B = rb['ban_kinh_2']; do = rb['do']
    ds = rb.get('dungsai', 0.5)
    thuc = _goc_o_tam(V, tam, A, B)
    if abs(thuc - do) > ds:
        raise ValueError(f"[PHANH DỪNG] Góc ở tâm {A}{tam}{B} khai {do}° nhưng dựng "
            f"{thuc:.1f}°. Sửa tọa độ, KHÔNG ra hình sai.")

for _loai, _ham in [
    ('diem_tren_tron', _kt_diem_tren_tron),
    ('goc_o_tam',      _kt_goc_o_tam),
]:
    C.dang_ky(_loai, _ham)
