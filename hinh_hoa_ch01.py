#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hoa_ch01.py — ENTRY chương: Hóa (KHTN) lớp 7 Chương I
#   "Nguyên tử · Sơ lược bảng tuần hoàn". Thư viện DỰNG HÌNH NGUYÊN TỬ
#   (mô hình Bohr / hạt nhân p·n / hành tinh Rutherford) cho HOA7_CH01.
#   Generator ĐỘC LẬP (như hình đại số minh hoạ): NGHĨA-THUẦN — hàm nhận
#   số hạt / cấu hình e, MÁY tự bố trí vòng + chấm e (KHÔNG toạ độ tay,
#   Đ5.9). PHANH ngữ nghĩa (sum(cau_hinh)==Z, giới hạn lớp) → sai thì
#   DỪNG (raise), không ra hình sai. Xuất PNG buffer khớp
#   hinhVe/hinhBenPhai của template.
#   [29e] Ông Bụt (Hóa) 2026-09-16 — theo YEUCAU_KHO__HINH_NGUYENTU__HOA_CH01.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_core as _HC

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [7]
CUA_RENDER = {'nguyen_tu_bo', 'nguyen_tu_hat_nhan', 'mo_hinh_hanh_tinh'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.

# 3 màu PHÂN BIỆT RÕ, nhất quán toàn bài (Phiếu Khai Nghĩa)
MAU_EPN = {"e": "blue!70!black", "p": "red!75!black", "n": "gray!45!black"}

_PRE = (r'\documentclass[border=4pt]{standalone}'
        r'\usepackage{tikz}\usepackage{amsmath}'
        r'\usetikzlibrary{arrows.meta}'
        r'\begin{document}')

# ─────────── PHANH ngữ nghĩa ───────────
def _phanh(Z, cau_hinh):
    """Nguyên tử trung hòa + giới hạn lớp. Sai → raise (DỪNG, không ra hình sai)."""
    if not cau_hinh or any((not isinstance(x, int)) or x <= 0 for x in cau_hinh):
        raise ValueError(f"[PHANH hoa] cấu hình không hợp lệ: {cau_hinh}")
    tong = sum(cau_hinh)
    if tong != Z:
        raise ValueError(f"[PHANH hoa] sum(cau_hinh)={tong} ≠ Z={Z} — nguyên tử phải trung hòa.")
    if cau_hinh[0] > 2:
        raise ValueError(f"[PHANH hoa] lớp 1 = {cau_hinh[0]} > 2 (tối đa 2 e).")
    if len(cau_hinh) >= 2 and cau_hinh[1] > 8:
        raise ValueError(f"[PHANH hoa] lớp 2 = {cau_hinh[1]} > 8 (tối đa 8 e).")

# ─────────── helper: chấm e đều trên vòng bán kính r ───────────
def _cham_e(r, n, lech=0.0):
    out = []
    for k in range(n):
        ang = 90 + lech + k * 360.0 / n
        x = r * math.cos(math.radians(ang)); y = r * math.sin(math.radians(ang))
        out.append(f"  \\fill[{MAU_EPN['e']}] ({x:.3f},{y:.3f}) circle (0.10);")
    return "\n".join(out)

# ─────────── helper: cụm hạt nhân p/n (phyllotaxis, gọn) ───────────
def _cum_hat_nhan(so_p, so_n):
    thu_tu = []
    i = j = 0
    while i < so_p or j < so_n:      # xen kẽ p,n cho lẫn màu
        if i < so_p: thu_tu.append('p'); i += 1
        if j < so_n: thu_tu.append('n'); j += 1
    out = []
    for k, loai in enumerate(thu_tu):
        r = 0.17 * math.sqrt(k)
        ang = k * 137.5
        x = r * math.cos(math.radians(ang)); y = r * math.sin(math.radians(ang))
        out.append(f"  \\fill[{MAU_EPN[loai]}] ({x:.3f},{y:.3f}) circle (0.125);")
    return "\n".join(out)

def _nhan(nhan, y):
    if not nhan: return ""
    return f"  \\node[below, font=\\bfseries] at (0,{y:.3f}) {{{nhan}}};"

# ═══════════ Hàm 1 — nguyen_tu_bo (⭐ gánh ~80% hình chương) ═══════════
def nguyen_tu_bo(Z, cau_hinh, nhan=None, hien_e=True, out='hoa_ntbo', tra_bytes=False):
    """Mô hình Bohr: hạt nhân tâm ghi +Z; vòng đồng tâm = số lớp trong cau_hinh;
       e là chấm phân bố đều trên mỗi vòng (từ trong ra ngoài).
       cau_hinh: list số e mỗi lớp, vd [2,8,7].
       hien_e=False → sơ đồ 'CHƯA HOÀN THIỆN' (vòng trống, KHÔNG chấm e) cho đề
                      'hoàn thiện Hình' (oxygen 2.11, silicon 2.20); đáp án gọi hien_e=True.
       nhan → nhãn nguyên tố tùy chọn (vd 'Cl').
       PHANH: sum(cau_hinh)==Z; lớp1≤2; lớp2≤8."""
    _phanh(Z, cau_hinh)
    r0, dr = 0.85, 0.6
    rings, dots = [], []
    for i, ne in enumerate(cau_hinh):
        r = r0 + i * dr
        rings.append(f"  \\draw[black!70, thin] (0,0) circle ({r:.3f});")
        if hien_e:
            dots.append(_cham_e(r, ne, lech=i * 15))
    rmax = r0 + (len(cau_hinh) - 1) * dr
    body = (_PRE + r'''
\begin{tikzpicture}[line join=round]
@@RINGS@@
  \fill[@@P@@] (0,0) circle (0.33);
  \node[white, font=\footnotesize\bfseries] at (0,0) {$+@@Z@@$};
@@DOTS@@
@@NHAN@@
\end{tikzpicture}
\end{document}''')
    body = (body.replace('@@RINGS@@', "\n".join(rings))
                .replace('@@DOTS@@', "\n".join(dots))
                .replace('@@P@@', MAU_EPN['p'])
                .replace('@@Z@@', str(Z))
                .replace('@@NHAN@@', _nhan(nhan, -(rmax + 0.5))))
    return _HC.render_tikz_doc(body, out, tra_bytes)

# ═══════════ Hàm 2 — nguyen_tu_hat_nhan (hạt nhân vẽ rõ p·n) ═══════════
def nguyen_tu_hat_nhan(so_p, so_n, cau_hinh_vo, nhan=None, out='hoa_nthn', tra_bytes=False):
    """Mô hình chi tiết: hạt nhân vẽ RÕ các quả cầu proton (màu p) + neutron (màu n)
       + vỏ electron (chấm màu e) trên vòng theo cau_hinh_vo.
       PHANH: sum(cau_hinh_vo)==so_p (trung hòa)."""
    _phanh(so_p, cau_hinh_vo)
    r0, dr = 1.0, 0.6
    rings, dots = [], []
    for i, ne in enumerate(cau_hinh_vo):
        r = r0 + i * dr
        rings.append(f"  \\draw[black!70, thin] (0,0) circle ({r:.3f});")
        dots.append(_cham_e(r, ne, lech=i * 15))
    rmax = r0 + (len(cau_hinh_vo) - 1) * dr
    body = (_PRE + r'''
\begin{tikzpicture}[line join=round]
@@RINGS@@
@@NHANHAN@@
@@DOTS@@
@@NHAN@@
\end{tikzpicture}
\end{document}''')
    body = (body.replace('@@RINGS@@', "\n".join(rings))
                .replace('@@NHANHAN@@', _cum_hat_nhan(so_p, so_n))
                .replace('@@DOTS@@', "\n".join(dots))
                .replace('@@NHAN@@', _nhan(nhan, -(rmax + 0.5))))
    return _HC.render_tikz_doc(body, out, tra_bytes)

# ═══════════ Hàm 3 — mo_hinh_hanh_tinh (Rutherford, định tính) ═══════════
def mo_hinh_hanh_tinh(out='hoa_hanhtinh', tra_bytes=False):
    """Mô hình hành tinh Rutherford: hạt nhân dương ở tâm, electron trên NHIỀU
       quỹ đạo elip nghiêng. Không tham số (hình định tính, một-lần)."""
    orbits = []
    for ang in (0, 60, 120):
        orbits.append(f"  \\draw[black!60, thin, rotate={ang}] (0,0) ellipse (1.7 and 0.62);")
    # mỗi quỹ đạo 1 electron, đặt lệch nhau
    epos = [(0, 1.7, 0.0), (60, 1.7, 0.0), (120, -1.7, 0.0)]
    edots = []
    for ang, a, _b in epos:
        x = a * math.cos(math.radians(ang)); y = a * math.sin(math.radians(ang)) * (0.62/1.7)
        edots.append(f"  \\fill[{MAU_EPN['e']}] ({x:.3f},{y:.3f}) circle (0.11);")
    body = (_PRE + r'''
\begin{tikzpicture}[line join=round]
@@ORBITS@@
  \fill[@@P@@] (0,0) circle (0.32);
  \node[white, font=\footnotesize\bfseries] at (0,0) {$+$};
@@EDOTS@@
\end{tikzpicture}
\end{document}''')
    body = (body.replace('@@ORBITS@@', "\n".join(orbits))
                .replace('@@P@@', MAU_EPN['p'])
                .replace('@@EDOTS@@', "\n".join(edots)))
    return _HC.render_tikz_doc(body, out, tra_bytes)

# ═══════════ CLASS ENTRY cho sinh_bantrich (module hàm-độc-lập) ═══════════
# Theo tiền lệ [29c] (hinh_daiso: hàm minh hoạ gắn @staticmethod vào class entry
# để vào bản trích). Gọi được CẢ H.nguyen_tu_bo(...) LẪN H.Hinh.nguyen_tu_bo(...).
class Hinh:
    """Entry bản trích — thư viện hình nguyên tử HOA7_CH01 (hàm-độc-lập)."""
    nguyen_tu_bo       = staticmethod(nguyen_tu_bo)
    nguyen_tu_hat_nhan = staticmethod(nguyen_tu_hat_nhan)
    mo_hinh_hanh_tinh  = staticmethod(mo_hinh_hanh_tinh)
