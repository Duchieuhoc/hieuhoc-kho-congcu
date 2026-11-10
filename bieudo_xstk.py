# -*- coding: utf-8 -*-
"""
bieudo_xstk.py — Lớp figure BIỂU ĐỒ & MÔ HÌNH XÁC SUẤT cho mạch Thống kê & Xác suất (XS-TK).
Kiến trúc: lớp figure Python (matplotlib) → PNG → nhúng Word qua H.hinhVe
(nhất quán hinh_khoihop.py). Dùng chung THCS 6·7·8·9 + THPT.
Font DejaVu Sans (đủ dấu tiếng Việt). Nền trắng, viền mảnh xám (CHUAN_TRINH_BAY).
Số thập phân IN dấu phẩy (VN); dấu trừ dùng "−" (U+2212).

HÀM CHÍNH:
  Thống kê:  bieu_do_cot · bieu_do_cot_kep · bieu_do_tranh · bieu_do_hop · bieu_do_cham · bieu_do_tan_so_tuong_doi
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

from matplotlib.ticker import FuncFormatter as _FuncFormatter
def _ap_truc_phay(ax, huong="dung"):
    """[33 OB 07/11] Áp dấu PHẨY cho NHÃN VẠCH trục giá trị (chuẩn trình bày VN).
    Trước đây chỉ nhãn giá trị trên cột dùng phẩy; vạch trục để matplotlib mặc định → '17.5'.
    huong='dung' → trục đứng (y); huong='ngang' → trục ngang (x). Số nguyên không đổi."""
    truc = ax.xaxis if huong == "ngang" else ax.yaxis
    truc.set_major_formatter(_FuncFormatter(lambda v, _pos: _fmt(v)))

# ── Bộ BIỂU TƯỢNG AN TOÀN (có glyph trong DejaVu Sans) cho bieu_do_tranh ──
#   Emoji plane (🚗📕⚽👦…) CHƯA có font đen trong môi trường → sẽ ra ô vuông.
#   Ánh xạ icon SGK → biểu tượng an toàn; khoá luôn ghi TÊN VẬT THẬT nên nghĩa không mất.
ICON_AN_TOAN = "☺ ☹ ● ★ ✿ ✉ ☎ ◐".split()
def _has_glyph(c):
    """True nếu font DejaVu Sans có glyph cho ký tự c. Dùng FT2Font (không thêm phụ thuộc)."""
    global _FT
    try:
        _FT
    except NameError:
        try:
            from matplotlib.ft2font import FT2Font
            from matplotlib.font_manager import findfont, FontProperties
            _FT = FT2Font(findfont(FontProperties(family="DejaVu Sans")))
        except Exception:
            _FT = None
    if _FT is None:
        return True  # không kiểm được → không chặn
    return _FT.get_char_index(ord(c)) != 0
def _kiem_glyph(bt):
    thieu = [c for c in bt if not _has_glyph(c)]
    if thieu:
        raise ValueError(
            f"bieu_do_tranh: biểu tượng {thieu!r} KHÔNG có glyph trong font "
            f"(sẽ vẽ ra ô vuông ▯). Dùng biểu tượng trong BỘ AN TOÀN: "
            f"{' '.join(ICON_AN_TOAN)}. Icon emoji (🚗📕⚽👦…) chưa có font đen — "
            f"tạm dùng ● và ghi tên vật ở khoá, hoặc báo Ông Bụt bổ font.")

# ───────────────────────── BIỂU ĐỒ CỘT ─────────────────────────
def bieu_do_cot(danh_muc, gia_tri, nhan_truc_dung="", nhan_truc_ngang="",
                tieu_de="", huong="dung", hien_nhan=True, mau=None,
                so_nguyen=True, goc_truc_dung=None, out="bd_cot", tra_bytes=False):
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
        if goc_truc_dung is not None:
            ax.set_ylim(bottom=goc_truc_dung)  # gốc trục ≠ 0 (minh họa bẫy đọc)
        if hien_nhan:
            for x, v in zip(pos, gia_tri):
                ax.text(x, v + (0.02 if v >= 0 else -0.02) * biendo, _fmt(v),
                        ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    _ap_truc_phay(ax, huong)
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
    _ap_truc_phay(ax, huong)
    ax.legend(frameon=False, fontsize=9, loc="best")
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)

# ──────────────────────── BIỂU ĐỒ TRANH ────────────────────────
def bieu_do_tranh(hang, moi_icon, bieu_tuong="●", mau_icon=_C1,
                  cho_phep_le=True, tieu_de="", chu_thich_khoa=None,
                  out="bd_tranh", tra_bytes=False):
    """Biểu đồ tranh. hang=[{'nhan','so_luong'}]. Vẽ so_luong/moi_icon biểu tượng, lẻ ½.
       chu_thich_khoa mặc định 'Mỗi <bt> ứng với <k> đơn vị'.
       CHẶN TOFU: biểu tượng thiếu glyph → raise (không vẽ ô vuông câm)."""
    _kiem_glyph(bieu_tuong)
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
def _mau_chu_tuong_phan(mau):
    """[33zo 09/11] Chọn màu chữ nhãn (đen/trắng) theo độ sáng nền ô vòng quay.
    Nền sáng (trắng/vàng nhạt) → chữ ĐEN; nền đậm → chữ TRẮNG. Dùng cho vong_quay."""
    import matplotlib.colors as _mc
    r, g, b = _mc.to_rgb(mau)
    lum = 0.299 * r + 0.587 * g + 0.114 * b   # độ sáng cảm thụ
    return "#222222" if lum > 0.6 else "white"

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
                ha="center", va="center", fontsize=11, fontweight="bold",
                color=_mau_chu_tuong_phan(mau))
        if mui_ten_chi_vao is not None and str(x["nhan"]) == str(mui_ten_chi_vao):
            tam_chi = mid
        start -= g
    if tam_chi is None: tam_chi = np.radians(60)
    # [33zm 07/11] Rút mũi tên về 0,55R (trước nhãn ô 0,62R) để KHÔNG trùm nhãn ô đích
    #   (lỗi lộ khi QC B42: ô "3"/"Nai" bị đầu mũi tên che). Vẫn chỉ rõ hướng vào ô.
    ax.add_patch(FancyArrow(0, 0, 0.55 * np.cos(tam_chi), 0.55 * np.sin(tam_chi),
                            width=0.02, head_width=0.09, head_length=0.10,
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

# ═════════════════ BIỂU ĐỒ HỘP (box plot) — DS10_CH05_B14 ═════════════════
def bieu_do_hop(q1=None, q2=None, q3=None, rau_trai=None, rau_phai=None,
                bat_thuong=None, moc_truc=None, nhan_truc="",
                so_do=False, tieu_de="", out="box", tra_bytes=False):
    """Biểu đồ hộp (box plot) nằm ngang — mạch Thống kê THPT (độ phân tán, giá trị bất thường).
    • Dạng SỐ LIỆU (mặc định): q1≤q2≤q3; rau_trai≤q1; q3≤rau_phai;
      bat_thuong=[...] các giá trị NẰM NGOÀI [rau_trai; rau_phai]; moc_truc=[...] mốc ghi trên trục.
      PHANH: sai thứ tự / bất thường nằm trong râu → raise (không ra hình sai).
    • Dạng SƠ ĐỒ (so_do=True): KHUNG CHÚ THÍCH tổng quát (H5.5) — nhãn Q₁/Q₂/Q₃, ngoặc ΔQ,
      hai mốc (Q₁−1,5·ΔQ)/(Q₃+1,5·ΔQ), vùng giá trị bất thường. KHÔNG số liệu, KHÔNG lộ đáp án (Đ41.4).
    Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe."""
    bat_thuong = bat_thuong or []
    OUT = "#2E8B57"  # chấm bất thường (xanh lá)
    if so_do:
        q1v, q2v, q3v, rt, rp = 3.4, 4.9, 6.4, 1.3, 8.5
        fig, ax = _fig_ax(6.8, 2.7); ax.axis("off")
        ax.annotate("", xy=(9.7, 0), xytext=(0.2, 0),
                    arrowprops=dict(arrowstyle="-", color="#333", lw=1.3))
        ax.add_patch(Rectangle((q1v, -0.5), (q3v - q1v), 1.0,
                     facecolor="#EAF1F8", edgecolor=_C1, linewidth=1.6))
        ax.plot([q2v, q2v], [-0.5, 0.5], color=_C1, lw=1.8)
        ax.plot([rt, q1v], [0, 0], color="#333", lw=1.2)
        ax.plot([q3v, rp], [0, 0], color="#333", lw=1.2)
        for x in (rt, rp):
            ax.plot([x, x], [-0.22, 0.22], color="#333", lw=1.2)
        for x in (0.55, 9.25):
            ax.plot(x, 0, "o", color=OUT, ms=7)
        for x, t in [(q1v, "Q₁"), (q2v, "Q₂"), (q3v, "Q₃")]:
            ax.text(x, -0.72, t, ha="center", va="top", fontsize=12)
        ax.annotate("", xy=(q3v, 0.9), xytext=(q1v, 0.9),
                    arrowprops=dict(arrowstyle="<->", color="#555", lw=1.0))
        ax.text((q1v + q3v) / 2, 1.05, "ΔQ", ha="center", fontsize=11)
        ax.text(rt, -0.72, "Q₁ − 1,5·ΔQ", ha="center", va="top", fontsize=8.5)
        ax.text(rp, -0.72, "Q₃ + 1,5·ΔQ", ha="center", va="top", fontsize=8.5)
        ax.text(0.55, 0.5, "Giá trị\nbất thường", ha="center", va="bottom", fontsize=8, color=OUT)
        ax.text(9.25, 0.5, "Giá trị\nbất thường", ha="center", va="bottom", fontsize=8, color=OUT)
        ax.set_xlim(-0.3, 10.1); ax.set_ylim(-1.5, 1.6)
        if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=6)
        return _xuat(fig, out, tra_bytes)
    # ── DẠNG SỐ LIỆU + PHANH ──
    if None in (q1, q2, q3, rau_trai, rau_phai):
        raise ValueError("bieu_do_hop: cần q1,q2,q3,rau_trai,rau_phai (hoặc so_do=True).")
    if not (rau_trai <= q1 <= q2 <= q3 <= rau_phai):
        raise ValueError(f"bieu_do_hop PHANH: cần rau_trai≤q1≤q2≤q3≤rau_phai, "
                         f"nhận rau_trai={rau_trai}, q1={q1}, q2={q2}, q3={q3}, rau_phai={rau_phai}.")
    for b in bat_thuong:
        if rau_trai <= b <= rau_phai:
            raise ValueError(f"bieu_do_hop PHANH: giá trị bất thường {b} phải NẰM NGOÀI "
                             f"[{rau_trai}; {rau_phai}].")
    allx = [rau_trai, rau_phai] + list(bat_thuong)
    lo, hi = min(allx), max(allx); pad = (hi - lo) * 0.06 or 1
    fig, ax = _fig_ax(6.8, 2.2)
    ax.spines["left"].set_visible(False); ax.set_yticks([])
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color("#333")
    ax.add_patch(Rectangle((q1, -0.5), (q3 - q1), 1.0,
                 facecolor="#EAF1F8", edgecolor=_C1, linewidth=1.6, zorder=3))
    ax.plot([q2, q2], [-0.5, 0.5], color=_C1, lw=1.9, zorder=4)
    ax.plot([rau_trai, q1], [0, 0], color="#333", lw=1.2, zorder=2)
    ax.plot([q3, rau_phai], [0, 0], color="#333", lw=1.2, zorder=2)
    for x in (rau_trai, rau_phai):
        ax.plot([x, x], [-0.22, 0.22], color="#333", lw=1.2, zorder=2)
    for b in bat_thuong:
        ax.plot(b, 0, "o", color=OUT, ms=7, zorder=5)
    ticks = moc_truc if moc_truc else sorted(set([rau_trai, q1, q2, q3, rau_phai] + list(bat_thuong)))
    ax.set_xticks(ticks); ax.set_xticklabels([_fmt(t) for t in ticks], fontsize=9)
    ax.set_xlim(lo - pad, hi + pad); ax.set_ylim(-1.1, 1.1)
    if nhan_truc: ax.set_xlabel(nhan_truc, fontsize=9)
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=8)
    return _xuat(fig, out, tra_bytes)

# ═════════════════ BIỂU ĐỒ CHẤM ĐIỂM (dot plot) — DS10_CH05_B14 ═════════════════
def bieu_do_cham(tan_so, truc=None, nhan_truc="", tieu_de="", out="dot", tra_bytes=False):
    """Biểu đồ chấm điểm (dot plot). tan_so: dict {gia_tri(int): so_cham}. Trên mỗi giá trị
    xếp CHỒNG các chấm tròn, số chấm = tần số của giá trị đó.
    truc=(min,max): ép chung thang để so sánh cặp A/B (2 biểu đồ cùng trục).
    Ghép cặp: gọi 2 lần cùng truc rồi H.luoiHinh([pngA, pngB]).
    Trả PNG (hoặc bytes nếu tra_bytes=True)."""
    if not tan_so:
        raise ValueError("bieu_do_cham: tan_so rỗng.")
    keys = sorted(tan_so.keys())
    lo, hi = (truc if truc else (min(keys), max(keys)))
    lo, hi = int(lo), int(hi)
    maxf = max(tan_so.values()) or 1
    fig, ax = _fig_ax(max(3.6, 0.7 * (hi - lo + 1) + 0.8), 0.40 * maxf + 1.2)
    ax.spines["left"].set_visible(False); ax.set_yticks([])
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_color("#333")
    for x in range(lo, hi + 1):
        for j in range(int(tan_so.get(x, 0))):
            ax.plot(x, j + 1, "o", color=_C1, ms=9, zorder=3)
    ax.set_xticks(range(lo, hi + 1))
    ax.set_xticklabels([_fmt(t) for t in range(lo, hi + 1)], fontsize=10)
    ax.set_xlim(lo - 0.6, hi + 0.6); ax.set_ylim(0.3, maxf + 0.8)
    if nhan_truc: ax.set_xlabel(nhan_truc, fontsize=9)
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=8)
    return _xuat(fig, out, tra_bytes)

# ═════ HISTOGRAM TẦN SỐ TƯƠNG ĐỐI GHÉP NHÓM — DS12_CH03 (Cuối chương, SBT 3.18) [33g] ═════
def _buoc_dep(cao):
    """Chọn bước chia trục tung 'đẹp' sao cho ~5–9 vạch."""
    import math
    tho = cao / 7.0
    bac = 10 ** math.floor(math.log10(tho)) if tho > 0 else 1
    for m in (1, 2, 2.5, 5, 10):
        if m * bac >= tho:
            return m * bac
    return 10 * bac

def bieu_do_tan_so_tuong_doi(mocs, tan_so_tuong_doi, nhan_truc_dung="Tần số tương đối",
                             nhan_truc_ngang="", tieu_de="", don_vi="%",
                             hien_nhan=True, buoc_truc_dung=None,
                             out="bd_tstd", tra_bytes=False):
    """
    HISTOGRAM tần số tương đối cho mẫu số liệu GHÉP NHÓM (cột LIỀN KỀ — chuẩn SGK/SBT 12).
      mocs             : list MỐC nhóm (n+1 số) — vd [48.5,49,49.5,50,50.5,51] → 5 nhóm liền kề.
      tan_so_tuong_doi : list chiều cao n cột theo don_vi (mặc định %) — vd [5,10,35,40,10].
      don_vi           : hậu tố nhãn trục tung + nhãn cột ("%" mặc định; "" nếu tần số tương đối thập phân).
      buoc_truc_dung   : bước chia trục tung (vd 5 → 0,5,10,…); None = tự chọn vạch đẹp.
    Cột span [mocs[i]; mocs[i+1]] → XỬ ĐƯỢC nhóm KHÔNG đều rộng. Số thập phân IN dấu phẩy (VN).
    """
    import numpy as _np, math as _math
    assert len(mocs) == len(tan_so_tuong_doi) + 1, \
        "mocs phải nhiều hơn tần số đúng 1 (n+1 mốc cho n nhóm)."
    n = len(tan_so_tuong_doi)
    rong = [mocs[i + 1] - mocs[i] for i in range(n)]
    tong_rong = mocs[-1] - mocs[0]
    fig, ax = _fig_ax(max(5.6, 0.9 * n + 2.4), 4.2)
    ax.bar(mocs[:-1], tan_so_tuong_doi, width=rong, align="edge",
           color=_C1, edgecolor="#33475B", linewidth=0.7)
    ax.set_xlim(mocs[0] - 0.04 * tong_rong, mocs[-1] + 0.04 * tong_rong)
    ax.set_xticks(mocs); ax.set_xticklabels([_fmt(m) for m in mocs])
    ax.set_ylabel(nhan_truc_dung); ax.set_xlabel(nhan_truc_ngang)
    ax.yaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
    cao = max(tan_so_tuong_doi) or 1
    buoc = buoc_truc_dung or _buoc_dep(cao)
    top = (_math.floor(cao / buoc) + 1) * buoc
    vach = _np.arange(0, top + buoc * 0.5, buoc)
    ax.set_yticks(vach)
    ax.set_yticklabels([f"{_fmt(t)}{don_vi}" for t in vach])
    ax.set_ylim(0, top)
    if hien_nhan:
        for i in range(n):
            xc = (mocs[i] + mocs[i + 1]) / 2
            ax.text(xc, tan_so_tuong_doi[i] + 0.018 * top,
                    f"{_fmt(tan_so_tuong_doi[i])}{don_vi}",
                    ha="center", va="bottom", fontsize=9)
    if tieu_de:
        ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)


# ════════════════════ BỔ SUNG 2026-11-03 (DS8_CH05 Thống kê) ════════════════════
# ADDITIVE: hai hàm biểu đồ còn thiếu cho mạch Thống kê lớp 7·8 (dự phóng THPT).
# Dùng chung helper sẵn có (_fig_ax, _xuat, _fmt, _C1, _BO, _GRID, Wedge, np).

# ──────────────────────── BIỂU ĐỒ HÌNH QUẠT TRÒN ────────────────────────
def bieu_do_quat(nhan, phan_tram, tieu_de="", mau=None, out="bd_quat", tra_bytes=False):
    """Biểu đồ hình quạt tròn (%). nhan=[...], phan_tram=[...] (tổng ~100).
    % in trên mỗi hình quạt (dấu phẩy VN), chú giải bên phải.
    Nan đầu bắt đầu từ đỉnh (12 giờ), đi THEO chiều kim đồng hồ (như SGK).
    Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe."""
    mau = mau or _BO
    tong = float(sum(phan_tram)) or 1.0
    fig, ax = _fig_ax(6.4, 4.2)
    ax.set_aspect("equal")
    goc0 = 90.0
    NGUONG_NGOAI = 5.0  # [33zn] quạt < 5% -> nhãn ra NGOÀI vành (tránh chồng nhãn quạt nhỏ)
    nhan_ngoai = []     # (goc_giua_rad, "x%")
    for i, p in enumerate(phan_tram):
        goc1 = goc0 - p / tong * 360.0
        ax.add_patch(Wedge((0, 0), 1.0, goc1, goc0,
                           facecolor=mau[i % len(mau)], edgecolor="white", linewidth=1.3))
        gm = np.radians((goc0 + goc1) / 2.0)
        if p / tong * 100.0 >= NGUONG_NGOAI:
            ax.text(0.60 * np.cos(gm), 0.60 * np.sin(gm), f"{_fmt(p)}%",
                    ha="center", va="center", fontsize=10, color="white", fontweight="bold")
        else:
            nhan_ngoai.append((gm, f"{_fmt(p)}%"))
        goc0 = goc1
    # [33zn] nhãn quạt nhỏ: đặt NGOÀI vành, màu đen, có đường dẫn mảnh; tách y chống chồng
    if nhan_ngoai:
        for ben in (1, -1):  # 1 = phải, -1 = trái
            nhom = [(gm, t) for gm, t in nhan_ngoai if (np.cos(gm) >= 0) == (ben == 1)]
            nhom.sort(key=lambda it: np.sin(it[0]), reverse=True)
            ys = [np.sin(gm) for gm, _ in nhom]
            dymin = 0.17  # khoảng cách y tối thiểu giữa 2 nhãn ngoài cùng bên
            for k in range(1, len(ys)):
                if ys[k - 1] - ys[k] < dymin:
                    ys[k] = ys[k - 1] - dymin
            for (gm, t), yT in zip(nhom, ys):
                ax.annotate(t, xy=(np.cos(gm), np.sin(gm)), xytext=(ben * 1.33, yT),
                            ha=("left" if ben == 1 else "right"), va="center",
                            fontsize=9, color="#222222", fontweight="bold",
                            arrowprops=dict(arrowstyle="-", color="#999999",
                                            lw=0.8, shrinkA=0, shrinkB=2))
    ax.set_xlim(-1.65, 1.65); ax.set_ylim(-1.3, 1.4); ax.axis("off")
    from matplotlib.patches import Patch
    handles = [Patch(facecolor=mau[i % len(mau)], label=nhan[i]) for i in range(len(nhan))]
    ax.legend(handles=handles, frameon=False, fontsize=9,
              loc="center left", bbox_to_anchor=(1.0, 0.5))
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)

# ──────────────────────── BIỂU ĐỒ ĐOẠN THẲNG ────────────────────────
_MARKERS = ["o", "s", "D", "^", "v"]
def bieu_do_doan_thang(truc, gia_tri=None, duong=None, nhan_truc_dung="", nhan_truc_ngang="",
                       tieu_de="", hien_nhan=True, so_nguyen=True, bat_dau_0=True, cach_deu=True, vi_tri=None, dao_truc_dung=False,
                       gioi_han_dung=None, out="bd_doan_thang", tra_bytes=False):
    """Biểu đồ đoạn thẳng (biểu diễn thay đổi theo thời gian). truc=[nhãn trục ngang].
    MỘT đường: gia_tri=[...]. NHIỀU đường: duong=[{'ten','gia_tri':[...]}, ...] (có chú giải).
    bat_dau_0=True → trục đứng từ 0 (đúng chuẩn, tránh bẫy gốc≠0).
    Trả PNG (hoặc bytes nếu tra_bytes=True). Nhúng Word qua H.hinhVe."""
    if duong is None:
        duong = [{"ten": "", "gia_tri": gia_tri}]
    nhieu = len(duong) > 1 or bool(duong and duong[0].get("ten"))
    n = len(truc)
    if vi_tri is not None:    # vị trí x tùy chọn (nhãn ngày/tháng không đều — H5.12)
        pos = list(vi_tri)
    elif not cach_deu:        # trục ngang theo GIÁ TRỊ THẬT → khoảng cách không đều (bẫy đọc)
        try: pos = [float(t) for t in truc]
        except (TypeError, ValueError): pos = list(range(n))
    else:
        pos = list(range(n))
    tat_ca = [v for d in duong for v in d["gia_tri"]]
    vmax = max(tat_ca) or 1
    fig, ax = _fig_ax(max(5.8, 0.7 * n + 2.2), 4.2)
    for j, d in enumerate(duong):
        ax.plot(pos, d["gia_tri"], marker=_MARKERS[j % len(_MARKERS)], markersize=6,
                linewidth=1.8, color=_BO[j % len(_BO)], label=d.get("ten", ""))
        if hien_nhan:
            for x, v in zip(pos, d["gia_tri"]):
                ax.text(x, v + 0.022 * vmax, _fmt(v), ha="center", va="bottom",
                        fontsize=8, color=_BO[j % len(_BO)])
    ax.set_xticks(pos); ax.set_xticklabels([str(t) for t in truc])
    ax.set_ylabel(nhan_truc_dung); ax.set_xlabel(nhan_truc_ngang)
    ax.yaxis.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
    if gioi_han_dung is not None:   # đặt (min,max) trục đứng tùy ý — cho bài "cùng dữ liệu khác trục" (5.24)
        ax.set_ylim(gioi_han_dung[0], gioi_han_dung[1])
    elif bat_dau_0:
        ax.set_ylim(0, vmax * 1.14)
    if so_nguyen and all(float(v).is_integer() for v in tat_ca):
        ax.yaxis.get_major_locator().set_params(integer=True)
    if dao_truc_dung:         # đảo trục đứng (vd xếp hạng: hạng nhỏ ở trên) — H5.13
        ax.invert_yaxis()
    _ap_truc_phay(ax, "dung")
    if nhieu:
        ax.legend(frameon=False, fontsize=9, loc="best")
    if tieu_de: ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)


# ═══════════════════════════════════════════════════════════════════════════
# [33zp] ĐỌC ĐỒ THỊ THỰC TẾ — đường cong mượt + điểm rời rạc 2 trục lệch tỉ lệ
#   OB Đại số THCS, 2026-11-09. Bổ cho DS8_CH07_B27 (hoãn SGK 7.22/7.23 → ⑤/LTC).
#   ADDITIVE: 2 HÀM MỚI (không đụng hàm cũ) → tương thích ngược hoàn toàn.
# ═══════════════════════════════════════════════════════════════════════════
def _ve_truc_oxy(ax, xlo, xhi, ylo, yhi, buoc_ngang, buoc_dung,
                 nhan_ngang, nhan_dung):
    """Khung Oxy kiểu SGK: lưới mờ, vạch + nhãn (dấu phẩy VN), mũi tên 2 đầu, chữ O."""
    ax.set_xlim(xlo, xhi); ax.set_ylim(ylo, yhi)
    xt = np.arange(0, xhi + 1e-9, buoc_ngang)
    yt = np.arange(0, yhi + 1e-9, buoc_dung)
    ax.set_xticks(xt[xt > 1e-9]); ax.set_yticks(yt[yt > 1e-9])
    ax.grid(True, color=_GRID, linewidth=0.7); ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    _ap_truc_phay(ax, "ngang"); _ap_truc_phay(ax, "dung")
    ax.tick_params(labelsize=8)
    # mũi tên đầu trục
    ax.plot(xhi, 0, ">k", clip_on=False, markersize=6)
    ax.plot(0, yhi, "^k", clip_on=False, markersize=6)
    ax.text(-0.02 * xhi, -0.03 * yhi, "O", ha="right", va="top", fontsize=10)
    # tên trục ĐẶT TRÊN đường trục (không lẫn với nhãn vạch bên dưới/bên trái)
    if nhan_ngang:
        ax.text(xhi, 0.03 * yhi, nhan_ngang, ha="right", va="bottom", fontsize=9)
    if nhan_dung:
        ax.text(0.02 * xhi, yhi, nhan_dung, ha="left", va="top", fontsize=9)


from scipy.interpolate import PchipInterpolator as _Pchip
def do_thi_duong_cong(moc, nhan_truc_ngang="", nhan_truc_dung="", tieu_de="",
                      giong=None, mau=None, x_max=None, y_max=None,
                      buoc_ngang=1, buoc_dung=1, out="dt_cong", tra_bytes=False):
    """ĐỒ THỊ HÀM SỐ dạng ĐƯỜNG CONG MƯỢT LIỀN đi qua các mốc (đọc đồ thị thực tế:
    nhiệt độ theo giờ SGK 7.23, …). moc=[(x,y),…] đọc từ đồ thị (x TĂNG DẦN).
    Nội suy PCHIP: giữ đơn điệu từng đoạn → lên đỉnh rồi xuống MƯỢT, KHÔNG vọt lố
    (không bướu giả như spline bậc 3). giong=[(x,y),…] vẽ nét đứt gióng + chấm mốc
    chốt (vd (4;5) SGK). buoc_ngang/buoc_dung bước vạch. Trả PNG/bytes."""
    xs = np.array([p[0] for p in moc], float)
    ys = np.array([p[1] for p in moc], float)
    mau = mau or _C1
    f = _Pchip(xs, ys)
    xx = np.linspace(xs[0], xs[-1], 400)
    fig, ax = _fig_ax(6.0, 4.3)
    xhi = x_max if x_max is not None else xs[-1] + buoc_ngang
    yhi = y_max if y_max is not None else float(max(ys)) + buoc_dung
    _ve_truc_oxy(ax, -0.03 * xhi, xhi * 1.06, -0.03 * yhi, yhi * 1.06,
                 buoc_ngang, buoc_dung, nhan_truc_ngang, nhan_truc_dung)
    ax.plot(xx, f(xx), color=mau, linewidth=2.1, zorder=4)
    for gx, gy in (giong or []):
        ax.plot([gx, gx], [0, gy], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
        ax.plot([0, gx], [gy, gy], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
        ax.plot(gx, gy, "o", color=mau, markersize=5, zorder=5)
    if tieu_de:
        ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)


def mp_toado_diem(diem, nhan_truc_ngang="", nhan_truc_dung="", tieu_de="",
                  x_max=None, y_max=None, buoc_ngang=1, buoc_dung=1,
                  giong=False, mau=None, out="mp_diem", tra_bytes=False):
    """ĐIỂM RỜI RẠC CÓ NHÃN TÊN trên mặt phẳng toạ độ — HAI TRỤC LỆCH TỈ LỆ.
    matplotlib tự scale 2 trục độc lập → 'một đơn vị trục tung = k lần trục hoành'
    hiện ra TỰ NHIÊN khi buoc_dung ≠ buoc_ngang (vd SGK 7.22 tuổi–cân nặng:
    buoc_ngang=1 (tuổi), buoc_dung=5 (kg) → mỗi ô lưới = 1 tuổi × 5 kg).
    diem=[{'x','y','ten','mau'?,'lech'?:(dx,dy) lệch nhãn}]. giong=True → mỗi điểm
    gióng nét đứt xuống 2 trục (đọc toạ độ). Trả PNG/bytes."""
    xs = [d["x"] for d in diem]; ys = [d["y"] for d in diem]
    fig, ax = _fig_ax(6.0, 4.6)
    xhi = x_max if x_max is not None else max(xs) + buoc_ngang
    yhi = y_max if y_max is not None else max(ys) + buoc_dung
    _ve_truc_oxy(ax, -0.03 * xhi, xhi * 1.06, -0.03 * yhi, yhi * 1.06,
                 buoc_ngang, buoc_dung, nhan_truc_ngang, nhan_truc_dung)
    for d in diem:
        c = d.get("mau") or _C1
        if giong:
            ax.plot([d["x"], d["x"]], [0, d["y"]], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
            ax.plot([0, d["x"]], [d["y"], d["y"]], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
        ax.plot(d["x"], d["y"], "o", color=c, markersize=6, zorder=5)
        dx, dy = d.get("lech", (0.10 * buoc_ngang, 0.10 * buoc_dung))
        ax.annotate(d.get("ten", ""), (d["x"], d["y"]), xytext=(d["x"] + dx, d["y"] + dy),
                    fontsize=9, color=c, fontweight="bold", zorder=6)
    if tieu_de:
        ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)


def do_thi_gap_khuc(moc, nhan_truc_ngang="", nhan_truc_dung="", tieu_de="",
                    giong=None, cham_dinh=True, mau=None, x_max=None, y_max=None,
                    buoc_ngang=1, buoc_dung=1, out="dt_gapkhuc", tra_bytes=False):
    """ĐỒ THỊ ĐƯỜNG GẤP KHÚC LIỀN trên lưới Oxy (đọc đồ thị thực tế liên tục:
    cân nặng cả đời SBT Vd2, vận tốc–thời gian SBT 7.24, …). moc=[(x,y),…] các ĐỈNH
    theo thứ tự (nối thẳng liền). Khác bieu_do_doan_thang (biểu đồ THỐNG KÊ, vạch
    theo mục): hàm này vẽ TRỤC SỐ ĐỀU (vạch nguyên cách buoc_ngang) nên ĐỈNH THẬP
    PHÂN (4,2 · 7,4 · 9,1) ĐỌC ÁP LƯỚI, KHÔNG gắn nhãn lên đỉnh → không chồng chữ.
    cham_dinh=True chấm đỉnh; giong=[(x,y),…] nét đứt gióng mốc chốt. Trả PNG/bytes."""
    xs = [p[0] for p in moc]; ys = [p[1] for p in moc]
    mau = mau or _C1
    fig, ax = _fig_ax(6.4, 4.3)
    xhi = x_max if x_max is not None else max(xs) + buoc_ngang
    yhi = y_max if y_max is not None else max(ys) + buoc_dung
    _ve_truc_oxy(ax, -0.03 * xhi, xhi * 1.06, -0.03 * yhi, yhi * 1.06,
                 buoc_ngang, buoc_dung, nhan_truc_ngang, nhan_truc_dung)
    ax.plot(xs, ys, color=mau, linewidth=2.0, zorder=4,
            marker="o" if cham_dinh else None, markersize=5)
    for gx, gy in (giong or []):
        ax.plot([gx, gx], [0, gy], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
        ax.plot([0, gx], [gy, gy], color="#8A8A8A", ls="--", lw=0.9, zorder=2)
    if tieu_de:
        ax.set_title(tieu_de, fontsize=11, fontweight="bold", pad=10)
    return _xuat(fig, out, tra_bytes)
