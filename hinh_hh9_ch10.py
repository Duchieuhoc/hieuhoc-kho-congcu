#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh9_ch10.py — MẠCH HÌNH KHỐI TRÒN XOAY (hình trụ · hình nón · hình cầu)
#   Toán 9 · Chương X "Một số hình khối trong thực tiễn" (Hình học TRỰC QUAN).
#
#   [33zl→] Ông Bụt 2026-11-19, Pha A HH9_CH10. Soi kho THẬT trước khi dựng:
#     • mat_cau có trong hinh_hh12_ch05.py NHƯNG buộc Oxyz (lớp 12, có hệ trục +
#       vectơ) → KHÔNG hợp bản lớp 9 (chỉ cần O, A, B, R, đường tròn lớn).
#     • khoi_hop/khai_trien_hop/lang_tru có trong hinh_khoihop.py — là KHỐI ĐA DIỆN
#       (cạnh thẳng), KHÔNG dùng được cho mặt cong tròn xoay.
#     • khai_trien_tru / khai_trien_non CHƯA có.
#   → mạch khối TRÒN XOAY (elip + mặt cong + nét khuất nửa sau) CHƯA có hàm nào.
#
#   TRIẾT LÝ ENGINE (theo tiền lệ khoiLapPhuongKhoetGoc trong hinh_khoihop.py,
#   được hinh_core.py cho phép: "generator ĐỘC LẬP, KHÔNG qua PHANH" cho hình
#   MINH HOẠ nhãn — không có quan hệ toạ-độ-SỐ để verify):
#     • generator matplotlib độc lập — elip/cung/mặt cong dựng trực tiếp (gọn hơn
#       TikZ-xấp-xỉ-đoạn rất nhiều), nền trong suốt, nét khuất = đường đứt.
#     • AI Soạn khai NGHĨA (R, h, l, nhãn) — máy tự tính toạ độ phối cảnh, KHÔNG
#       lộ toạ độ thô (Đ5.9).
#     • Quy ước SGK: đáy = elip (nửa TRƯỚC liền, nửa SAU đứt); trục/đường cao
#       bên trong = nét đứt; đường sinh biên = nét liền.
# CS2627 / HH2627.
# ═══════════════════════════════════════════════════════════════════
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# ─────────── Hằng phong cách (đồng bộ look SGK KNTT) ───────────
_MAU_NET   = "#1a1a1a"      # màu đường chính (gần đen)
_LW        = 1.7            # bề rộng nét liền
_LW_KHUAT  = 1.15           # bề rộng nét khuất (đứt)
_DUT       = (0, (4, 3))    # kiểu nét đứt
_FS        = 18             # cỡ chữ nhãn
_DEP       = 0.32           # hệ số dẹt elip đáy (b/a) — chuẩn phối cảnh SGK
_MAU_PHU   = "#c62828"      # màu đỏ cho kích thước nhấn (R, l) khi cần


def _mt(s):
    """Nhãn → mathtext: None giữ None; có '$' giữ nguyên; ngược lại bọc $...$ in nghiêng."""
    if s is None:
        return None
    s = str(s)
    return s if "$" in s else f"${s}$"


def _cung_elip(ax, cx, cy, a, b, t0, t1, net="lien", mau=_MAU_NET, lw=None, n=120):
    """Vẽ CUNG elip tâm (cx,cy), bán trục ngang a, bán trục dọc b, từ góc t0→t1 (độ).
       net='lien'|'dut'. Góc 0°=hướng +x (phải), 90°=lên, 180°=trái, 270°=xuống."""
    ts = [math.radians(t0 + (t1 - t0) * k / n) for k in range(n + 1)]
    xs = [cx + a * math.cos(t) for t in ts]
    ys = [cy + b * math.sin(t) for t in ts]
    ax.plot(xs, ys, linestyle=(_DUT if net == "dut" else "-"),
            linewidth=lw or (_LW_KHUAT if net == "dut" else _LW),
            color=mau, solid_capstyle="round", zorder=5)


def _elip_day(ax, cx, cy, a, b, mau=_MAU_NET):
    """ĐÁY hình khối = elip: nửa TRƯỚC (cung dưới 180°→360°) nét LIỀN,
       nửa SAU (cung trên 0°→180°) nét ĐỨT (khuất)."""
    _cung_elip(ax, cx, cy, a, b, 180, 360, net="lien", mau=mau)
    _cung_elip(ax, cx, cy, a, b, 0, 180, net="dut", mau=mau)


def _doan(ax, p1, p2, net="lien", mau=_MAU_NET, lw=None):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]],
            linestyle=(_DUT if net == "dut" else "-"),
            linewidth=lw or (_LW_KHUAT if net == "dut" else _LW),
            color=mau, solid_capstyle="round", zorder=5)


def _nhan(ax, x, y, chu, dx=0.0, dy=0.0, ha="center", va="center", mau="#111", fs=_FS):
    t = _mt(chu)
    if t is None:
        return
    ax.text(x + dx, y + dy, t, fontsize=fs, ha=ha, va=va, color=mau, zorder=9)


def _cham(ax, x, y, mau=_MAU_NET):
    ax.plot([x], [y], marker="o", markersize=2.6, color=mau, zorder=7)


def _ovuong(ax, dinh, u, v, canh=0.28, mau=_MAU_NET):
    """Ô vuông đánh dấu góc vuông tại 'dinh', hai cạnh theo hướng đơn vị u, v."""
    (dx, dy) = dinh
    p1 = (dx + u[0] * canh, dy + u[1] * canh)
    p3 = (dx + v[0] * canh, dy + v[1] * canh)
    p2 = (p1[0] + v[0] * canh, p1[1] + v[1] * canh)
    _doan(ax, p1, p2, mau=mau, lw=1.1)
    _doan(ax, p2, p3, mau=mau, lw=1.1)


def _khung(ax, xs, ys, m=0.7):
    ax.set_xlim(min(xs) - m, max(xs) + m)
    ax.set_ylim(min(ys) - m, max(ys) + m)


def _xuat(fig, out, tra_bytes):
    png = f"/tmp/{out}.png"
    fig.savefig(png, dpi=200, bbox_inches="tight", pad_inches=0.08, transparent=True)
    plt.close(fig)
    return open(png, "rb").read() if tra_bytes else png


# ═══════════════════════════════════════════════════════════════════
# 1) HÌNH TRỤ
# ═══════════════════════════════════════════════════════════════════
def hinh_tru(R=1.4, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None,
             tam_tren="O'", tam_duoi="O", dinh_tren=None, dinh_duoi=None,
             hien_truc=True, out="tru", tra_bytes=False):
    """HÌNH TRỤ phối cảnh đứng (2 đáy elip + 2 đường sinh biên).

    R, h      : bán kính đáy, chiều cao (độ dài VẼ, đơn vị ô). >0.
    nhan_R    : nhãn bán kính đáy (vẽ đoạn O→mép phải đáy dưới). None=ẩn.
    nhan_h    : nhãn chiều cao (trục O'O). None=ẩn nhãn (trục vẫn vẽ nếu hien_truc).
    nhan_l    : nhãn 1 đường sinh (cạnh biên phải). None=ẩn.
    tam_tren/tam_duoi : tên 2 tâm đáy (mặc định O', O). '' = không ghi.
    dinh_tren/dinh_duoi : tên điểm mép phải đáy trên/dưới (vd 'A'/'B' khi cần l=AB).
    hien_truc : vẽ trục O'O (nét đứt) hay không.
    """
    fig, ax = plt.subplots(figsize=(3.2, 4.0))
    ax.set_aspect("equal"); ax.axis("off")
    b = R * _DEP
    Ot = (0.0, h); Od = (0.0, 0.0)
    # thân: 2 đường sinh biên
    _doan(ax, (-R, 0), (-R, h))
    _doan(ax, (R, 0), (R, h))
    # đáy trên (rim nhìn thấy đủ → liền cả vòng) & đáy dưới (nửa sau đứt)
    _cung_elip(ax, Ot[0], Ot[1], R, b, 0, 360, net="lien")
    _elip_day(ax, Od[0], Od[1], R, b)
    # trục + chiều cao
    if hien_truc:
        _doan(ax, Ot, Od, net="dut")
    if tam_tren:
        _cham(ax, *Ot); _nhan(ax, Ot[0], Ot[1], tam_tren, dx=-0.16, dy=0.12, ha="right")
    if tam_duoi:
        _cham(ax, *Od); _nhan(ax, Od[0], Od[1], tam_duoi, dx=-0.16, dy=-0.14, ha="right", va="top")
    if nhan_h is not None:
        _nhan(ax, 0.0, h / 2, nhan_h, dx=0.14, ha="left")
    # bán kính đáy dưới: O → mép phải (R,0)
    if nhan_R is not None:
        Bp = (R, 0.0)
        _doan(ax, Od, Bp, mau=_MAU_NET)
        _cham(ax, *Bp)
        _nhan(ax, R / 2, 0.0, nhan_R, dy=-0.20, va="top")
        if dinh_duoi:
            _nhan(ax, R, 0.0, dinh_duoi, dx=0.16, dy=-0.12, ha="left", va="top")
    # đường sinh l = cạnh biên phải; đặt tên 2 mép phải nếu yêu cầu
    if nhan_l is not None:
        _nhan(ax, R, h / 2, nhan_l, dx=0.16, ha="left")
    if dinh_tren:
        _cham(ax, R, h); _nhan(ax, R, h, dinh_tren, dx=0.16, dy=0.10, ha="left")
    if dinh_duoi and nhan_R is None:
        _cham(ax, R, 0); _nhan(ax, R, 0, dinh_duoi, dx=0.16, dy=-0.12, ha="left", va="top")
    _khung(ax, [-R, R], [-b, h + b])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 2) HÌNH NÓN
# ═══════════════════════════════════════════════════════════════════
def hinh_non(R=1.6, h=3.0, nhan_R=None, nhan_h=None, nhan_l=None,
             dinh="S", tam="O", trai="A", phai="B",
             hien_dinh_ten=True, hien_tam=True, hien_trai_phai=False,
             o_vuong=True, out="non", tra_bytes=False):
    """HÌNH NÓN phối cảnh đứng (đỉnh trên, đáy elip, 2 đường sinh biên).

    R, h    : bán kính đáy, chiều cao. >0.
    nhan_R  : nhãn bán kính (O→mép phải đáy). None=ẩn.
    nhan_h  : nhãn chiều cao (trục SO, nét đứt). None=ẩn.
    nhan_l  : nhãn đường sinh (cạnh biên phải S→B). None=ẩn.
    dinh,tam,trai,phai : tên đỉnh S, tâm đáy O, mép trái A, mép phải B.
    o_vuong : đánh dấu góc vuông tại O (SO ⊥ đáy).
    """
    fig, ax = plt.subplots(figsize=(3.4, 4.0))
    ax.set_aspect("equal"); ax.axis("off")
    b = R * _DEP
    S = (0.0, h); O = (0.0, 0.0)
    A = (-R, 0.0); B = (R, 0.0)
    # đáy
    _elip_day(ax, O[0], O[1], R, b)
    # 2 đường sinh biên
    _doan(ax, S, A); _doan(ax, S, B)
    # trục/chiều cao SO
    _doan(ax, S, O, net="dut")
    if o_vuong:
        _ovuong(ax, O, (1, 0), (0, 1), canh=0.26)
    # nhãn
    if hien_dinh_ten and dinh:
        _cham(ax, *S); _nhan(ax, S[0], S[1], dinh, dy=0.20, va="bottom")
    if hien_tam and tam:
        _cham(ax, *O); _nhan(ax, O[0], O[1], tam, dx=0.0, dy=-0.20, va="top")
    if nhan_h is not None:
        _nhan(ax, 0.0, h / 2, nhan_h, dx=0.14, ha="left")
    if nhan_l is not None:
        _nhan(ax, R / 2, h / 2, nhan_l, dx=0.18, dy=0.10, ha="left")
    if nhan_R is not None:
        _doan(ax, O, B)
        _nhan(ax, R / 2, 0.0, nhan_R, dy=-0.20, va="top")
    if hien_trai_phai:
        _cham(ax, *A); _nhan(ax, A[0], A[1], trai, dx=-0.16, dy=-0.10, ha="right", va="top")
        _cham(ax, *B); _nhan(ax, B[0], B[1], phai, dx=0.16, dy=-0.10, ha="left", va="top")
    _khung(ax, [-R, R], [-b, h])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 3) HÌNH CẦU (bản lớp 9 — không hệ trục Oxyz)
# ═══════════════════════════════════════════════════════════════════
def hinh_cau(R=1.6, nhan_R=None, tam="O", hien_tam=True, hien_xichdao=True,
             duong_kinh=None, diem=None, out="cau", tra_bytes=False):
    """HÌNH CẦU / MẶT CẦU phối cảnh (viền tròn + xích đạo elip).

    R        : bán kính (độ dài VẼ). >0.
    nhan_R   : nhãn bán kính — vẽ O→mép phải, ghi nhãn. None=ẩn.
    tam      : tên tâm (mặc định O). hien_tam: ghi tâm + chấm.
    hien_xichdao : vẽ đường tròn lớn nằm ngang (xích đạo): nửa trước liền, sau đứt.
    duong_kinh=('A','B') : vẽ đường kính ngang AB (mép trái–phải) + ghi 2 tên.
    diem=('M', goc_do)   : điểm M trên mặt cầu ở góc 'goc_do' (độ) + bán kính OM.
    """
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    ax.set_aspect("equal"); ax.axis("off")
    O = (0.0, 0.0)
    # viền cầu = đường tròn
    _cung_elip(ax, 0, 0, R, R, 0, 360, net="lien", mau="#15407a")
    # xích đạo (đường tròn lớn nằm ngang)
    if hien_xichdao:
        be = R * _DEP
        _cung_elip(ax, 0, 0, R, be, 180, 360, net="lien", mau="#15407a")
        _cung_elip(ax, 0, 0, R, be, 0, 180, net="dut", mau="#15407a")
    if hien_tam and tam:
        _cham(ax, *O); _nhan(ax, 0, 0, tam, dx=0.0, dy=-0.22, va="top")
    # đường kính ngang
    if duong_kinh is not None:
        An, Bn = duong_kinh
        _doan(ax, (-R, 0), (R, 0))
        _cham(ax, -R, 0); _cham(ax, R, 0)
        _nhan(ax, -R, 0, An, dx=-0.16, ha="right")
        _nhan(ax, R, 0, Bn, dx=0.16, ha="left")
    # bán kính tới điểm M
    if diem is not None:
        Mn, gd = diem
        g = math.radians(gd)
        Mx, My = R * math.cos(g), R * math.sin(g)
        _doan(ax, O, (Mx, My), mau=_MAU_PHU)
        _cham(ax, Mx, My, mau=_MAU_PHU)
        _nhan(ax, Mx, My, Mn, dx=0.14 * math.copysign(1, Mx or 1), dy=0.14, ha="left")
        if nhan_R is not None:
            _nhan(ax, Mx / 2, My / 2, nhan_R, dx=0.10, dy=0.12, mau=_MAU_PHU)
    elif nhan_R is not None:
        _doan(ax, O, (R, 0), mau=_MAU_PHU)
        _cham(ax, R, 0, mau=_MAU_PHU)
        _nhan(ax, R / 2, 0, nhan_R, dy=0.16)
    _khung(ax, [-R, R], [-R, R])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 4) MẶT CẮT HÌNH CẦU bởi mặt phẳng (H10.23)
# ═══════════════════════════════════════════════════════════════════
def cat_cau(R=1.7, cao=0.0, nhan_mc="R", qua_tam=True, tam="O",
            nhan_mp="(P)", out="cat_cau", tra_bytes=False):
    """MẶT CẦU cắt bởi mặt phẳng → mặt cắt là hình tròn.

    cao      : độ cao mặt cắt so tâm (0 = qua tâm → đường tròn lớn).
    qua_tam  : True ghi "đường tròn lớn" (bán kính R); False → đường tròn nhỏ.
    nhan_mc  : nhãn bán kính mặt cắt.
    """
    fig, ax = plt.subplots(figsize=(3.8, 3.8))
    ax.set_aspect("equal"); ax.axis("off")
    _cung_elip(ax, 0, 0, R, R, 0, 360, net="lien", mau="#15407a")
    # bán kính hình tròn mặt cắt tại độ cao 'cao'
    rc = math.sqrt(max(R * R - cao * cao, 1e-6))
    bc = rc * _DEP
    # mặt phẳng cắt (hình bình hành mỏng)
    w = rc * 1.45
    yc = cao
    plan = [(-w, yc - 0.12), (w, yc - 0.12), (w + 0.5, yc + 0.22), (-w + 0.5, yc + 0.22)]
    ax.add_patch(plt.Polygon(plan, closed=True, facecolor="#9ab7e0",
                             edgecolor="#15407a", alpha=0.35, lw=1.0, zorder=2))
    _nhan(ax, w + 0.5, yc + 0.22, nhan_mp, dx=0.12, ha="left")
    # đường tròn mặt cắt (elip): trước liền, sau đứt
    _cung_elip(ax, 0, yc, rc, bc, 180, 360, net="lien", mau="#c62828")
    _cung_elip(ax, 0, yc, rc, bc, 0, 180, net="dut", mau="#c62828")
    _cham(ax, 0, yc)
    _nhan(ax, 0, yc, tam, dx=-0.16, dy=-0.04, ha="right")
    _doan(ax, (0, yc), (rc, yc), mau="#c62828")
    _nhan(ax, rc / 2, yc, nhan_mc, dy=0.16, mau="#c62828")
    _khung(ax, [-R, R + 0.5], [-R, R])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 5) HÌNH CHỮ NHẬT QUAY → trụ · 6) TAM GIÁC VUÔNG QUAY → nón  (H10.3 / H10.9a)
# ═══════════════════════════════════════════════════════════════════
def hcn_quay(R=1.3, h=2.8, ten=("O'", "A", "B", "O"), hien_tru=True,
             out="hcn_quay", tra_bytes=False):
    """HÌNH CHỮ NHẬT quay quanh một CẠNH (trục đứng) sinh HÌNH TRỤ (H10.3).
    ten=(trên-trục, trên-ngoài, dưới-ngoài, dưới-trục)."""
    fig, ax = plt.subplots(figsize=(3.4, 3.8)); ax.set_aspect("equal"); ax.axis("off")
    Ot, A, B, Od = (0, h), (R, h), (R, 0), (0, 0)
    # trục quay (dọc, nét đứt kéo dài)
    _doan(ax, (0, -0.5), (0, h + 0.5), net="dut")
    # hình chữ nhật (nền tô nhạt)
    ax.add_patch(plt.Polygon([Od, B, A, Ot], closed=True, facecolor="#f3d9e4",
                             edgecolor=_MAU_NET, lw=_LW, zorder=3))
    for p, t, dx, dy, ha in ((Ot, ten[0], -0.14, 0.12, "right"), (A, ten[1], 0.14, 0.12, "left"),
                             (B, ten[2], 0.14, -0.10, "left"), (Od, ten[3], -0.14, -0.12, "right")):
        _cham(ax, *p); _nhan(ax, p[0], p[1], t, dx=dx, dy=dy, ha=ha)
    # mũi tên quay quanh trục
    ax.annotate("", xy=(0.42, h + 0.18), xytext=(-0.42, h + 0.18),
                arrowprops=dict(arrowstyle="->", color=_MAU_NET, lw=1.3,
                                connectionstyle="arc3,rad=-0.5"))
    # hình trụ sinh ra (mờ, bên phải)
    if hien_tru:
        dx = 2.9
        _cung_elip(ax, dx, h, R, R * _DEP, 0, 360, net="lien", mau="#9aa7b5")
        _elip_day(ax, dx, 0, R, R * _DEP, mau="#9aa7b5")
        _doan(ax, (dx - R, 0), (dx - R, h), mau="#9aa7b5")
        _doan(ax, (dx + R, 0), (dx + R, h), mau="#9aa7b5")
        ax.annotate("", xy=(dx - 1.0, h / 2), xytext=(R + 0.25, h / 2),
                    arrowprops=dict(arrowstyle="->", color=_MAU_NET, lw=1.2))
    _khung(ax, [-R - 0.3, (3.9 + R) if hien_tru else R + 0.3], [-0.6, h + 0.6])
    return _xuat(fig, out, tra_bytes)


def tamgiac_quay(R=1.5, h=2.8, ten=("S", "O", "A"), hien_non=True,
                 o_vuong=True, out="tg_quay", tra_bytes=False):
    """TAM GIÁC VUÔNG quay quanh CẠNH GÓC VUÔNG (trục đứng) sinh HÌNH NÓN (H10.9a).
    ten=(đỉnh trên S, chân vuông O, đỉnh ngoài A)."""
    fig, ax = plt.subplots(figsize=(3.4, 3.8)); ax.set_aspect("equal"); ax.axis("off")
    S, O, A = (0, h), (0, 0), (R, 0)
    _doan(ax, (0, -0.5), (0, h + 0.5), net="dut")
    ax.add_patch(plt.Polygon([S, O, A], closed=True, facecolor="#f3d9e4",
                             edgecolor=_MAU_NET, lw=_LW, zorder=3))
    if o_vuong:
        _ovuong(ax, O, (1, 0), (0, 1), canh=0.24)
    for p, t, dx, dy, ha, va in ((S, ten[0], 0.0, 0.20, "center", "bottom"),
                                 (O, ten[1], -0.16, -0.10, "right", "top"),
                                 (A, ten[2], 0.16, -0.10, "left", "top")):
        _cham(ax, *p); _nhan(ax, p[0], p[1], t, dx=dx, dy=dy, ha=ha, va=va)
    ax.annotate("", xy=(0.42, h + 0.18), xytext=(-0.42, h + 0.18),
                arrowprops=dict(arrowstyle="->", color=_MAU_NET, lw=1.3,
                                connectionstyle="arc3,rad=-0.5"))
    if hien_non:
        dx = 3.0
        _elip_day(ax, dx, 0, R, R * _DEP, mau="#9aa7b5")
        _doan(ax, (dx, h), (dx - R, 0), mau="#9aa7b5")
        _doan(ax, (dx, h), (dx + R, 0), mau="#9aa7b5")
        ax.annotate("", xy=(dx - 1.1, h / 2), xytext=(R + 0.25, h / 2),
                    arrowprops=dict(arrowstyle="->", color=_MAU_NET, lw=1.2))
    _khung(ax, [-R - 0.3, (4.0 + R) if hien_non else R + 0.3], [-0.6, h + 0.6])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 7) KHAI TRIỂN HÌNH TRỤ (H10.5) · 8) KHAI TRIỂN HÌNH NÓN (H10.11)
# ═══════════════════════════════════════════════════════════════════
def khai_trien_tru(R=0.9, h=2.4, nhan_cv=None, nhan_h=None, nhan_R=None,
                   out="kt_tru", tra_bytes=False):
    """KHAI TRIỂN hình trụ = hình chữ nhật (rộng = chu vi 2πR, cao = h) + 2 hình tròn đáy."""
    fig, ax = plt.subplots(figsize=(4.6, 3.4)); ax.set_aspect("equal"); ax.axis("off")
    W = 2 * math.pi * R          # chu vi (độ dài VẼ thật = 2πR)
    # hình chữ nhật
    ax.add_patch(plt.Rectangle((0, 0), W, h, fill=False, edgecolor=_MAU_NET, lw=_LW))
    # 2 hình tròn đáy: trên-trái và dưới-trái, tiếp xúc cạnh ngang
    cx = R + 0.3
    _cung_elip(ax, cx, h + R + 0.25, R, R, 0, 360, net="lien")
    _cung_elip(ax, cx, -R - 0.25, R, R, 0, 360, net="lien")
    if nhan_R is not None:
        _doan(ax, (cx, h + R + 0.25), (cx + R, h + R + 0.25))
        _nhan(ax, cx + R / 2, h + R + 0.25, nhan_R, dy=0.16)
    if nhan_cv is not None:
        ax.annotate("", xy=(W, -0.0), xytext=(0, -0.0), arrowprops=dict(arrowstyle="<->", color="#777", lw=1.0))
        _nhan(ax, W / 2, 0, nhan_cv, dy=-0.28, va="top")
    if nhan_h is not None:
        _nhan(ax, W, h / 2, nhan_h, dx=0.18, ha="left")
    _khung(ax, [0, W], [-2 * R - 0.4, h + 2 * R + 0.5])
    return _xuat(fig, out, tra_bytes)


def khai_trien_non(R=1.0, l=2.6, nhan_l=None, nhan_R=None, dinh="S",
                   out="kt_non", tra_bytes=False):
    """KHAI TRIỂN hình nón = hình quạt tròn (bán kính l, cung = 2πR) + hình tròn đáy (bán kính R)."""
    fig, ax = plt.subplots(figsize=(4.0, 4.0)); ax.set_aspect("equal"); ax.axis("off")
    # góc quạt n = (R/l)*360
    n = (R / l) * 360.0
    a0 = 90 - n / 2
    a1 = 90 + n / 2
    S = (0.0, 0.0)
    A = (l * math.cos(math.radians(a1)), l * math.sin(math.radians(a1)))  # trái
    B = (l * math.cos(math.radians(a0)), l * math.sin(math.radians(a0)))  # phải
    _doan(ax, S, A); _doan(ax, S, B)
    _cung_elip(ax, 0, 0, l, l, a0, a1, net="lien")
    _cham(ax, *S); _nhan(ax, 0, 0, dinh, dy=-0.22, va="top")
    _nhan(ax, A[0], A[1], "A", dx=-0.12, dy=0.12, ha="right")
    _nhan(ax, B[0], B[1], "B", dx=0.12, dy=0.12, ha="left")
    if nhan_l is not None:
        _nhan(ax, B[0] / 2, B[1] / 2, nhan_l, dx=0.16, ha="left")
    # hình tròn đáy, đặt dưới cung
    cy = l + R + 0.35
    _cung_elip(ax, 0, cy, R, R, 0, 360, net="lien")
    if nhan_R is not None:
        _doan(ax, (0, cy), (R, cy)); _nhan(ax, R / 2, cy, nhan_R, dy=0.16)
    _khung(ax, [-l * 0.75, l * 0.75], [0, cy + R])
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════
# 9–14) HÌNH GHÉP KHỐI
# ═══════════════════════════════════════════════════════════════════
def _than_tru(ax, R, y0, y1, mau=_MAU_NET):
    _doan(ax, (-R, y0), (-R, y1), mau=mau)
    _doan(ax, (R, y0), (R, y1), mau=mau)


def tru_non(R=1.3, h_tru=2.0, h_non=1.8, nhan=None, out="tru_non", tra_bytes=False):
    """GHÉP: hình TRỤ (dưới) + hình NÓN (trên, chung đáy) — H10.16 dụng cụ.
    nhan=dict {'R','h_tru','h_non'} nhãn kích thước (tùy chọn)."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(3.2, 4.4)); ax.set_aspect("equal"); ax.axis("off")
    _elip_day(ax, 0, 0, R, R * _DEP)                      # đáy trụ
    _than_tru(ax, R, 0, h_tru)
    # mặt tiếp giáp trụ–nón tại h_tru
    _cung_elip(ax, 0, h_tru, R, R * _DEP, 180, 360, net="lien")
    _cung_elip(ax, 0, h_tru, R, R * _DEP, 0, 180, net="dut")
    # nón trên
    S = (0, h_tru + h_non)
    _doan(ax, S, (-R, h_tru)); _doan(ax, S, (R, h_tru))
    if "h_tru" in nhan:
        _doan(ax, (-R - 0.35, 0), (-R - 0.35, h_tru), net="dut", mau="#888", lw=1.0)
        _nhan(ax, -R - 0.35, h_tru / 2, nhan["h_tru"], dx=-0.14, ha="right")
    if "h_non" in nhan:
        _doan(ax, (R + 0.35, h_tru), (R + 0.35, h_tru + h_non), net="dut", mau="#888", lw=1.0)
        _nhan(ax, R + 0.35, h_tru + h_non / 2, nhan["h_non"], dx=0.14, ha="left")
    if "R" in nhan:
        _doan(ax, (0, 0), (R, 0)); _nhan(ax, R / 2, 0, nhan["R"], dy=-0.20, va="top")
    _khung(ax, [-R, R], [-R * _DEP, h_tru + h_non])
    return _xuat(fig, out, tra_bytes)


def nua_cau_tru(R=1.3, h=2.2, nhan=None, out="nuacau_tru", tra_bytes=False):
    """GHÉP: hình TRỤ (dưới) + NỬA HÌNH CẦU (vòm trên) — H10.37a."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(3.0, 4.2)); ax.set_aspect("equal"); ax.axis("off")
    _elip_day(ax, 0, 0, R, R * _DEP)
    _than_tru(ax, R, 0, h)
    # vòm nửa cầu bán kính R tâm (0,h)
    _cung_elip(ax, 0, h, R, R, 0, 180, net="lien")
    # vành tiếp giáp
    _cung_elip(ax, 0, h, R, R * _DEP, 180, 360, net="lien")
    _cung_elip(ax, 0, h, R, R * _DEP, 0, 180, net="dut")
    if "h" in nhan:
        _doan(ax, (-R - 0.35, 0), (-R - 0.35, h), net="dut", mau="#888", lw=1.0)
        _nhan(ax, -R - 0.35, h / 2, nhan["h"], dx=-0.14, ha="right")
    if "R" in nhan:
        _doan(ax, (0, 0), (R, 0)); _nhan(ax, R / 2, 0, nhan["R"], dy=-0.20, va="top")
    _khung(ax, [-R, R], [-R * _DEP, h + R])
    return _xuat(fig, out, tra_bytes)


def nua_cau_non(R=1.2, h_non=2.4, nhan=None, up=True, out="nuacau_non", tra_bytes=False):
    """GHÉP: NÓN + NỬA CẦU chung đáy — ốc quế kem (H10.39): nón chúc XUỐNG, vòm cầu trên.
    up=True: nón đỉnh dưới, nửa cầu vòm trên (kem). up=False: nón trên."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(3.0, 4.2)); ax.set_aspect("equal"); ax.axis("off")
    # giao diện nón–cầu ở y = h_non (đỉnh nón ở 0 dưới)
    yj = h_non
    S = (0, 0)
    _doan(ax, S, (-R, yj)); _doan(ax, S, (R, yj))
    # vành
    _cung_elip(ax, 0, yj, R, R * _DEP, 180, 360, net="lien")
    _cung_elip(ax, 0, yj, R, R * _DEP, 0, 180, net="dut")
    # nửa cầu vòm trên
    _cung_elip(ax, 0, yj, R, R, 0, 180, net="lien")
    if "h_non" in nhan:
        _doan(ax, (R + 0.35, 0), (R + 0.35, yj), net="dut", mau="#888", lw=1.0)
        _nhan(ax, R + 0.35, yj / 2, nhan["h_non"], dx=0.14, ha="left")
    if "R" in nhan:
        _doan(ax, (0, yj), (R, yj)); _nhan(ax, R / 2, yj, nhan["R"], dy=0.14)
    _khung(ax, [-R, R], [0, yj + R])
    return _xuat(fig, out, tra_bytes)


def vong_bi(R=1.6, r=0.9, h=1.3, nhan=None, out="vong_bi", tra_bytes=False):
    """VÒNG BI / ỐNG TRỤ RỖNG — trụ ngoài R khoét trụ trong r, cao h (H10.30)."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(3.6, 3.2)); ax.set_aspect("equal"); ax.axis("off")
    b, br = R * _DEP, r * _DEP
    # mặt trên: vành khăn (elip ngoài + elip trong)
    _cung_elip(ax, 0, h, R, b, 0, 360, net="lien")
    _cung_elip(ax, 0, h, r, br, 0, 360, net="lien")
    # thành ngoài
    _than_tru(ax, R, 0, h)
    # đáy ngoài (nửa trước)
    _cung_elip(ax, 0, 0, R, b, 180, 360, net="lien")
    _cung_elip(ax, 0, 0, R, b, 0, 180, net="dut")
    # lỗ trong: thành trong nhìn qua lỗ (nét đứt) + đáy trong
    _doan(ax, (-r, h), (-r, 0), net="dut", lw=1.1)
    _doan(ax, (r, h), (r, 0), net="dut", lw=1.1)
    _cung_elip(ax, 0, 0, r, br, 0, 180, net="dut")       # đáy trong (cung sau, khuất)
    if "R" in nhan:
        _doan(ax, (0, h), (R, h)); _nhan(ax, R * 0.72, h, nhan["R"], dy=0.14)
    if "r" in nhan:
        _nhan(ax, r / 2, h, nhan["r"], dy=0.14)
    if "h" in nhan:
        _doan(ax, (R + 0.3, 0), (R + 0.3, h), net="dut", mau="#888", lw=1.0)
        _nhan(ax, R + 0.3, h / 2, nhan["h"], dx=0.14, ha="left")
    _khung(ax, [-R, R + 0.3], [-b, h + b])
    return _xuat(fig, out, tra_bytes)


def bon_xang(R=1.0, L=3.2, nhan=None, out="bon_xang", tra_bytes=False):
    """BỒN NẰM NGANG — trụ nằm ngang dài L + 2 NỬA CẦU hai đầu (H10.32)."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(5.0, 2.6)); ax.set_aspect("equal"); ax.axis("off")
    bx = R * _DEP                 # bán trục ngang của elip đầu (thu ngắn do nhìn ngang)
    # thân trụ: 2 đường sinh ngang
    _doan(ax, (0, R), (L, R)); _doan(ax, (0, -R), (L, -R))
    # vành nối thân–nắp tại 2 đầu (elip đứng): đầu phải nhìn thấy, đầu trái khuất 1 phần
    _cung_elip(ax, L, 0, bx, R, 90, 270, net="dut")     # nửa sau vành phải
    _cung_elip(ax, L, 0, bx, R, -90, 90, net="lien")    # nửa trước vành phải
    _cung_elip(ax, 0, 0, bx, R, 90, 270, net="lien")    # vành trái (thấy)
    # nắp nửa cầu 2 đầu: nửa elip bán kính R bung ra ngoài
    _cung_elip(ax, L, 0, R, R, -90, 90, net="lien")     # nắp phải bung phải
    _cung_elip(ax, 0, 0, R, R, 90, 270, net="lien")     # nắp trái bung trái
    if "L" in nhan:
        ax.annotate("", xy=(L, R + 0.35), xytext=(0, R + 0.35),
                    arrowprops=dict(arrowstyle="<->", color="#777", lw=1.0))
        _nhan(ax, L / 2, R + 0.35, nhan["L"], dy=0.16)
    if "D" in nhan:
        ax.annotate("", xy=(L + R + 0.35, R), xytext=(L + R + 0.35, -R),
                    arrowprops=dict(arrowstyle="<->", color="#777", lw=1.0))
        _nhan(ax, L + R + 0.35, 0, nhan["D"], dx=0.14, ha="left")
    _khung(ax, [-R, L + R], [-R, R])
    return _xuat(fig, out, tra_bytes)


def tru_khoan_non(R=1.3, h=2.4, nhan=None, out="tru_khoan_non", tra_bytes=False):
    """HÌNH TRỤ bị KHOAN mất phần hình NÓN (đáy nón = đáy trên trụ, đỉnh ở tâm đáy dưới) — H10.28."""
    nhan = nhan or {}
    fig, ax = plt.subplots(figsize=(3.0, 4.0)); ax.set_aspect("equal"); ax.axis("off")
    b = R * _DEP
    _elip_day(ax, 0, 0, R, b)
    _than_tru(ax, R, 0, h)
    _cung_elip(ax, 0, h, R, b, 0, 360, net="lien")       # miệng trụ trên
    # nón khoét: đỉnh ở tâm đáy dưới (0,0), miệng = mép trên — nét đứt (khuất trong)
    _doan(ax, (0, 0), (-R, h), net="dut", lw=1.15)
    _doan(ax, (0, 0), (R, h), net="dut", lw=1.15)
    _cham(ax, 0, 0)
    if "R" in nhan:
        _doan(ax, (0, h), (R, h)); _nhan(ax, R / 2, h, nhan["R"], dy=0.14)
    if "h" in nhan:
        _doan(ax, (R + 0.35, 0), (R + 0.35, h), net="dut", mau="#888", lw=1.0)
        _nhan(ax, R + 0.35, h / 2, nhan["h"], dx=0.14, ha="left")
    _khung(ax, [-R, R + 0.35], [-b, h + b])
    return _xuat(fig, out, tra_bytes)


# ─────────── smoke test khi chạy trực tiếp ───────────
if __name__ == "__main__":
    R = {}
    R["tru"] = hinh_tru(nhan_R="R", nhan_h="h", nhan_l="l", dinh_tren="A", dinh_duoi="B", out="t_tru")
    R["non"] = hinh_non(nhan_R="R", nhan_h="h", nhan_l="l", out="t_non")
    R["cau"] = hinh_cau(nhan_R="R", duong_kinh=("A", "B"), out="t_cau")
    R["cat_cau"] = cat_cau(nhan_mc="R", out="t_catcau")
    R["hcn_quay"] = hcn_quay(out="t_hcnquay")
    R["tg_quay"] = tamgiac_quay(out="t_tgquay")
    R["kt_tru"] = khai_trien_tru(nhan_cv=r"2\pi R", nhan_h="h", nhan_R="R", out="t_kttru")
    R["kt_non"] = khai_trien_non(nhan_l="l", nhan_R="R", out="t_ktnon")
    R["tru_non"] = tru_non(nhan={"R": "R", "h_tru": "h_1", "h_non": "h_2"}, out="t_trunon")
    R["nuacau_tru"] = nua_cau_tru(nhan={"R": "R", "h": "h"}, out="t_ncautru")
    R["nuacau_non"] = nua_cau_non(nhan={"R": "R", "h_non": "h"}, out="t_ncaunon")
    R["vong_bi"] = vong_bi(nhan={"R": "R", "r": "r", "h": "h"}, out="t_vongbi")
    R["bon_xang"] = bon_xang(nhan={"L": "3.6 m", "D": "1.8 m"}, out="t_bonxang")
    R["tru_khoan_non"] = tru_khoan_non(nhan={"R": "R", "h": "h"}, out="t_trukhoannon")
    for k, v in R.items():
        print(f"{k:16s} {v}")
