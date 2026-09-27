# -*- coding: utf-8 -*-
"""
bieudo_xstk.py — Lớp figure BIỂU ĐỒ & MÔ HÌNH XÁC SUẤT cho mạch Thống kê & Xác suất (XS-TK).
Kiến trúc: lớp figure Python (matplotlib) → PNG → nhúng Word qua H.hinhVe
(nhất quán hinh_khoihop.py). Dùng chung THCS 6·7·8·9 + THPT.
Font DejaVu Sans (đủ dấu tiếng Việt). Nền trắng, viền mảnh xám (CHUAN_TRINH_BAY).
Số thập phân IN dấu phẩy (VN); dấu trừ dùng "−" (U+2212).

HÀM CHÍNH:
  Thống kê:  bieu_do_cot · bieu_do_cot_kep · bieu_do_tranh
  Xác suất:  vong_quay · xuc_xac · dong_xu · tui_bi · truc_kha_nang
Mỗi hàm trả đường dẫn PNG (hoặc bytes nếu tra_bytes=True).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrow, Rectangle, FancyBboxPatch
import numpy as np

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.edgecolor"] = "#999999"
plt.rcParams["axes.linewidth"] = 0.8
_C1, _C2 = "#2F5C8F", "#E39A3B"
_BO = [_C1, _C2, "#5FA88C", "#B45C7E", "#8E7CC3"]
_GRID = "#D9D9D9"

def _fig_ax(w=6.2, h=4.0):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor("white"); ax.set_facecolor("white")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    return fig, ax

def _xuat(fig, out, tra_bytes):
    png = f"/tmp/{out}.png"
    fig.savefig(png, dpi=200, bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)
    return open(png, "rb").read() if tra_bytes else png

def _fmt(v):
    return f"{v:g}".replace("-", "−").replace(".", ",")

# ───────────────────────── BIỂU ĐỒ CỘT ─────────────────────────
def bieu_do_cot(danh_muc, gia_tri, nhan_truc_dung="", nhan_truc_ngang="",
                tieu_de="", huong="dung", hien_nhan=True, mau=None,
                so_nguyen=True, out="bd_cot", tra_bytes=False):
    """Biểu đồ cột. Tự xử lí CỘT ÂM (giá trị <0 dưới trục). huong='ngang' → thanh ngang."""
    mau = mau or _C1
    co_am = any(v < 0 for v in gia_tri)
    biendo = max(abs(v) for v in gia_tri) or 1
    n = len(danh_muc); pos = range(n)
    if huong == "ngang":
        fig, ax = _fig_ax(6.4, max(3.0, 0.6 * n + 1.4))
        ax.barh(pos, gia_tri, color=mau, height=0.6, edgecolor="#33475B", linewidth=0.5)
        ax.set_yticks(list(pos)); ax.set_yticklabels(danh_muc); ax.invert_yaxis()
        ax.set_xlabel(nhan_truc_dung); ax.set_ylabel(nhan_truc_ngang)
        ax.xaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
        if co_am: ax.axvline(0, color="#333", linewidth=0.9)
        if hien_nhan:
            for y, v in zip(pos, gia_tri):
                ax.text(v + (0.012 if v >= 0 else -0.012) * biendo, y, _fmt(v),
                        va="center", ha="left" if v >= 0 else "right", fontsize=9)
    else:
        fig, ax = _fig_ax(max(5.2, 0.95 * n + 2.2), 4.0)
        ax.bar(pos, gia_tri, color=mau, width=0.6, edgecolor="#33475B", linewidth=0.5)
        ax.set_xticks(list(pos)); ax.set_xticklabels(danh_muc)
        ax.set_ylabel(nhan_truc_dung); ax.set_xlabel(nhan_truc_ngang)
        ax.yaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
        if co_am: ax.axhline(0, color="#333", linewidth=0.9)
        if so_nguyen and all(float(v).is_integer() for v in gia_tri):
            ax.yaxis.get_major_locator().set_params(integer=True)
        if hien_nhan:
            for x, v in zip(pos, gia_tri):
                ax.text(x, v + (0.02 if v >= 0 else -0.02) * biendo, _fmt(v),
                        ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)

# ─────────────────────── BIỂU ĐỒ CỘT KÉP ───────────────────────
def bieu_do_cot_kep(danh_muc, nhom, nhan_truc_dung="", nhan_truc_ngang="",
                    tieu_de="", huong="dung", hien_nhan=True, so_nguyen=True,
                    out="bd_cot_kep", tra_bytes=False):
    """Cột kép/đa nhóm + chú giải. nhom=[{'ten','gia_tri':[...]}]. Tự xử cột âm; huong='ngang'."""
    n = len(danh_muc); k = len(nhom)
    tat_ca = [v for g in nhom for v in g["gia_tri"]]
    co_am = any(v < 0 for v in tat_ca); biendo = max(abs(v) for v in tat_ca) or 1
    w = 0.8 / k; base = [i - 0.4 + w / 2 for i in range(n)]
    if huong == "ngang":
        fig, ax = _fig_ax(6.6, max(3.2, 0.75 * n + 1.6))
        for j, g in enumerate(nhom):
            ys = [b + j * w for b in base]
            ax.barh(ys, g["gia_tri"], height=w, color=_BO[j % len(_BO)],
                    edgecolor="#33475B", linewidth=0.4, label=g["ten"])
            if hien_nhan:
                for y, v in zip(ys, g["gia_tri"]):
                    ax.text(v + (0.012 if v >= 0 else -0.012) * biendo, y, _fmt(v),
                            va="center", ha="left" if v >= 0 else "right", fontsize=8)
        ax.set_yticks(range(n)); ax.set_yticklabels(danh_muc); ax.invert_yaxis()
        ax.set_xlabel(nhan_truc_dung); ax.set_ylabel(nhan_truc_ngang)
        ax.xaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
        if co_am: ax.axvline(0, color="#333", linewidth=0.9)
    else:
        fig, ax = _fig_ax(max(6.0, 1.15 * n + 2.4), 4.2)
        for j, g in enumerate(nhom):
            xs = [b + j * w for b in base]
            ax.bar(xs, g["gia_tri"], width=w, color=_BO[j % len(_BO)],
                   edgecolor="#33475B", linewidth=0.4, label=g["ten"])
            if hien_nhan:
                for x, v in zip(xs, g["gia_tri"]):
                    ax.text(x, v + (0.02 if v >= 0 else -0.02) * biendo, _fmt(v),
                            ha="center", va="bottom" if v >= 0 else "top", fontsize=8)
        ax.set_xticks(range(n)); ax.set_xticklabels(danh_muc)
        ax.set_ylabel(nhan_truc_dung); ax.set_xlabel(nhan_truc_ngang)
        ax.yaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
        if co_am: ax.axhline(0, color="#333", linewidth=0.9)
        if so_nguyen and all(float(v).is_integer() for v in tat_ca):
            ax.yaxis.get_major_locator().set_params(integer=True)
    ax.legend(frameon=False, fontsize=9, loc="best")
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)

# ──────────────────────── BIỂU ĐỒ TRANH ────────────────────────
def bieu_do_tranh(hang, moi_icon, bieu_tuong="●", mau_icon=_C1,
                  cho_phep_le=True, tieu_de="", chu_thich_khoa=None,
                  out="bd_tranh", tra_bytes=False):
    """Biểu đồ tranh. hang=[{'nhan','so_luong'}]. Vẽ so_luong/moi_icon biểu tượng, lẻ ½.
       chu_thich_khoa mặc định 'Mỗi <bt> ứng với <k> đơn vị'."""
    n = len(hang)
    so_icon_max = max((h["so_luong"] / moi_icon) for h in hang)
    fig, ax = _fig_ax(max(6.0, 0.55 * so_icon_max + 3.0), 0.62 * n + 1.4)
    ax.axis("off")
    for i, h in enumerate(hang):
        y = n - 1 - i
        ax.text(-0.3, y, h["nhan"], ha="right", va="center", fontsize=10)
        full = int(h["so_luong"] // moi_icon)
        le = (h["so_luong"] - full * moi_icon) / moi_icon  # phần lẻ [0,1)
        for j in range(full):
            ax.text(j, y, bieu_tuong, ha="center", va="center",
                    fontsize=16, color=mau_icon)
        if cho_phep_le and le >= 0.25:
            # nửa biểu tượng: vẽ biểu tượng rồi che nửa phải bằng nền trắng
            ax.text(full, y, bieu_tuong, ha="center", va="center",
                    fontsize=16, color=mau_icon)
            ax.add_patch(Rectangle((full + 0.02, y - 0.35), 0.5, 0.7,
                                   facecolor="white", edgecolor="none", zorder=5))
    ax.set_xlim(-3.2, so_icon_max + 0.6); ax.set_ylim(-0.8, n - 0.2)
    khoa = chu_thich_khoa or f"Mỗi {bieu_tuong} ứng với {_fmt(moi_icon)} đơn vị"
    ax.text(so_icon_max / 2, -0.7, f"({khoa})", ha="center", va="center",
            fontsize=9, style="italic", color="#444")
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=8)
    return _xuat(fig, out, tra_bytes)

# ───────────────────── MÔ HÌNH XÁC SUẤT ─────────────────────
def vong_quay(o, mui_ten_chi_vao=None, tieu_de="", out="vong_quay", tra_bytes=False):
    """Vòng quay/tấm bìa. o=[{'nhan','mau'?,'ti_le'?}]. mui_ten_chi_vao = nhãn ô mũi tên chỉ."""
    n = len(o)
    ti_le = [x.get("ti_le", 1) for x in o]; tong = sum(ti_le)
    goc = [t / tong * 360 for t in ti_le]
    fig, ax = _fig_ax(4.6, 4.6); ax.set_aspect("equal"); ax.axis("off")
    start = 90.0; tam_chi = None
    for i, (x, g) in enumerate(zip(o, goc)):
        mau = x.get("mau") or _BO[i % len(_BO)]
        ax.add_patch(Wedge((0, 0), 1.0, start - g, start, facecolor=mau,
                           edgecolor="white", linewidth=1.4))
        mid = np.radians(start - g / 2)
        ax.text(0.62 * np.cos(mid), 0.62 * np.sin(mid), str(x["nhan"]),
                ha="center", va="center", fontsize=11, fontweight="bold", color="white")
        if mui_ten_chi_vao is not None and str(x["nhan"]) == str(mui_ten_chi_vao):
            tam_chi = mid
        start -= g
    if tam_chi is None: tam_chi = np.radians(60)
    ax.add_patch(FancyArrow(0, 0, 0.7 * np.cos(tam_chi), 0.7 * np.sin(tam_chi),
                            width=0.02, head_width=0.09, head_length=0.12,
                            length_includes_head=True, color="#222", zorder=6))
    ax.add_patch(Circle((0, 0), 0.05, color="#222", zorder=7))
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15)
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=6)
    return _xuat(fig, out, tra_bytes)

def _cham_xucxac(ax, cx, cy, n, s=1.0):
    r = s / 2
    ax.add_patch(FancyBboxPatch((cx - r, cy - r), s, s,
                boxstyle="round,pad=0.02,rounding_size=0.12",
                facecolor="white", edgecolor="#222", linewidth=1.5))
    d = s * 0.22
    pos = {1: [(0, 0)], 2: [(-d, d), (d, -d)],
           3: [(-d, d), (0, 0), (d, -d)],
           4: [(-d, d), (d, d), (-d, -d), (d, -d)],
           5: [(-d, d), (d, d), (0, 0), (-d, -d), (d, -d)],
           6: [(-d, d), (d, d), (-d, 0), (d, 0), (-d, -d), (d, -d)]}
    for dx, dy in pos[n]:
        ax.add_patch(Circle((cx + dx, cy + dy), s * 0.07, color="#222"))

def xuc_xac(mat, kieu="don", out="xuc_xac", tra_bytes=False):
    """Xúc xắc. mat=[n] (đơn) hoặc [n1,n2] (đôi). n = số chấm 1..6."""
    ns = mat if isinstance(mat, (list, tuple)) else [mat]
    k = len(ns)
    fig, ax = _fig_ax(1.6 * k + 0.6, 2.0); ax.set_aspect("equal"); ax.axis("off")
    for i, n in enumerate(ns):
        _cham_xucxac(ax, i * 1.5, 0, n, 1.1)
    ax.set_xlim(-0.9, 1.5 * (k - 1) + 0.9); ax.set_ylim(-0.9, 0.9)
    return _xuat(fig, out, tra_bytes)

def dong_xu(mat="sap", out="dong_xu", tra_bytes=False):
    """Đồng xu. mat='sap'|'ngua' → in chữ S/N."""
    fig, ax = _fig_ax(1.8, 1.8); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0, 0), 0.9, facecolor="#F2D06B", edgecolor="#B8912E", linewidth=2))
    ax.text(0, 0, "S" if mat == "sap" else "N", ha="center", va="center",
            fontsize=26, fontweight="bold", color="#6B4E12")
    ax.text(0, -1.15, "Mặt sấp" if mat == "sap" else "Mặt ngửa",
            ha="center", fontsize=9, color="#444")
    ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.4, 1.1)
    return _xuat(fig, out, tra_bytes)

def tui_bi(bi, tieu_de="", out="tui_bi", tra_bytes=False):
    """Túi bi. bi=[{'mau','so_luong'}] (mau: tên VN 'đỏ/xanh/vàng/đen/tím/trắng' hoặc hex)."""
    _MAU = {"đỏ": "#D64545", "xanh": "#3E7CB1", "vàng": "#E7B84B", "đen": "#333333",
            "tím": "#8E5DA8", "trắng": "#EEEEEE", "xanh lá": "#5FA85F"}
    diem = []
    for b in bi:
        mau = _MAU.get(b["mau"], b["mau"])
        diem += [mau] * b["so_luong"]
    fig, ax = _fig_ax(3.2, 3.4); ax.set_aspect("equal"); ax.axis("off")
    # túi
    ax.add_patch(FancyBboxPatch((-1.1, -1.3), 2.2, 2.3,
                boxstyle="round,pad=0.02,rounding_size=0.35",
                facecolor="#F5F7FA", edgecolor="#9AA6B2", linewidth=1.6))
    ax.plot([-0.45, 0.45], [1.0, 1.0], color="#9AA6B2", linewidth=2)  # miệng túi
    rng = np.random.default_rng(len(diem))
    pts = []
    for _ in range(len(diem)):
        for _try in range(200):
            x, y = rng.uniform(-0.75, 0.75), rng.uniform(-1.05, 0.55)
            if all((x - px) ** 2 + (y - py) ** 2 > 0.09 for px, py in pts):
                pts.append((x, y)); break
    for (x, y), c in zip(pts, diem):
        ax.add_patch(Circle((x, y), 0.16, facecolor=c, edgecolor="#555", linewidth=0.6))
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.5, 1.3)
    if tieu_de: ax.set_title(tieu_de, fontsize=10, pad=4)
    return _xuat(fig, out, tra_bytes)

def truc_kha_nang(out="truc_kha_nang", tra_bytes=False):
    """Trục khả năng 0 — ½ — 1 (Không xảy ra / Có thể / Luôn xảy ra) — H.9.28."""
    fig, ax = _fig_ax(6.2, 1.6); ax.axis("off")
    ax.annotate("", xy=(1.05, 0), xytext=(-0.05, 0),
                arrowprops=dict(arrowstyle="-", color="#333", linewidth=1.5))
    for x, top, bot in [(0, "0", "Không\nxảy ra"), (0.5, r"$\frac{1}{2}$", "Có thể\nxảy ra"),
                        (1, "1", "Luôn\nxảy ra")]:
        ax.plot([x, x], [-0.05, 0.05], color="#333", linewidth=1.5)
        ax.text(x, 0.16, top, ha="center", fontsize=13)
        ax.text(x, -0.28, bot, ha="center", va="top", fontsize=9, color="#444")
    ax.set_xlim(-0.15, 1.15); ax.set_ylim(-0.6, 0.4)
    return _xuat(fig, out, tra_bytes)
