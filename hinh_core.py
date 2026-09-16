#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_core.py — LÕI VẼ HÌNH Hiếu Học (KHUNG dùng chung mọi lớp/chiều)
#   Triết lý VERIFY: hàm khai NGHĨA → máy tính tọa độ → PHANH ĐỐI CHIẾU
#   quan hệ khai báo → sai thì DỪNG (raise), không ra hình sai.
#
# [12/08/2026] TÁCH KHUNG ↔ LUẬT (đón HHKG lớp 8 — BAN_GIAO mục 2):
#   • Lõi = KHUNG PHANH (lặp ràng buộc, tra registry, raise) + render pipeline
#     (biên dịch .tex, KHÔNG hard-code 2D) + `dang_ky(loai, ham)`.
#   • LUẬT KIỂM (2D) dời sang `hinh_phang.py`, tự đăng ký khi import.
#   • Lõi nạp `hinh_phang` ở CUỐI file làm GÓI MẶC ĐỊNH ⟹ Toán 7 chạy y nguyên
#     (cầu tương thích — bỏ được khi mọi kho chương tự nạp gói luật của mình).
#   • HHKG lớp 8: thêm `hinh_kg.py` `dang_ky` luật 3D + render phối cảnh —
#     KHÔNG mổ lại lõi.
# Trích & nâng cấp từ vehinh_tikz.py (Toán 7 CH3, 28/07). CS2627.
# ═══════════════════════════════════════════════════════════════════
import subprocess, os

# ═══════════ REGISTRY LUẬT — khung tra cứu, không biết 2D/3D ═══════════
LUAT = {}                      # loai(str) → ham_kiem(V, rb) : raise nếu sai

def dang_ky(loai, ham_kiem):
    """Đăng ký 1 luật kiểm cho PHANH. Kho phẳng/không-gian gọi hàm này khi import.
    ham_kiem(V, rb): đọc rb (dict có 'loai' + tham số), raise ValueError nếu vi phạm."""
    LUAT[loai] = ham_kiem

# ═══════════ PHANH TỔNG QUÁT — máy tự báo khai sai ═══════════
def phanh(V, rang_buoc):
    """rang_buoc: list dict, mỗi cái có 'loai' + tham số riêng (xem hinh_phang).
    Tra registry LUAT theo 'loai' → gọi luật kiểm. Sai vượt dung sai → raise,
    KHÔNG ra hình sai. 'loai' chưa đăng ký → raise (nhắc nạp gói luật)."""
    for rb in rang_buoc:
        loai = rb.get('loai')
        ham = LUAT.get(loai)
        if ham is None:
            raise ValueError(f"[PHANH] Loại ràng buộc '{loai}' chưa đăng ký "
                             f"— thiếu gói luật (import hinh_phang / hinh_kg)?")
        ham(V, rb)

# ─────────── TƯƠNG THÍCH NGƯỢC: PHANH góc kiểu cũ ───────────
def _phanh(V, goc_de):
    """Bản cũ (chỉ góc) — để 4 hàm Toán 7 cũ chạy không cần sửa."""
    phanh(V, [{'loai':'goc','ten':g['ten'],'do':g['do']} for g in goc_de])

# ─────────── tên coordinate an toàn cho TikZ ───────────
def _san(t): return t.replace("'","p")

# ─────────── RENDER TikZ → PNG (biên dịch thuần, KHÔNG hard-code 2D) ───────────
def _render(tikz, out, tra_bytes=False):
    tex=(r'\documentclass[border=4pt]{standalone}'
         r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}'
         r'\usepackage{tikz}\usepackage{amsmath}'
         r'\usepackage{newunicodechar}'
         r'\newunicodechar{′}{\ensuremath{{}^{\prime}}}'      # U+2032 prime  → x′
         r'\newunicodechar{″}{\ensuremath{{}^{\prime\prime}}}' # U+2033 dprime → x″
         r'\usetikzlibrary{angles,quotes,intersections,calc}\begin{document}'
         +tikz+r'\end{document}')
    open(f'/tmp/{out}.tex','w').write(tex)
    subprocess.run(['pdflatex','-interaction=nonstopmode',f'{out}.tex'],cwd='/tmp',capture_output=True)
    subprocess.run(['pdftoppm','-png','-r','150',f'{out}.pdf',out],cwd='/tmp',capture_output=True)
    png=f'/tmp/{out}-1.png'
    if not os.path.exists(png): return None
    return open(png,'rb').read() if tra_bytes else png

# ═══════════ GÓI LUẬT MẶC ĐỊNH (cầu tương thích) ═══════════
# Nạp luật 2D + helper đo (để mọi kho import hinh_core có sẵn luật phẳng, Toán 7 nguyên vẹn).
# Đặt CUỐI file: các tên khung ở trên đã định nghĩa xong trước khi hinh_phang cần chúng.
import hinh_phang as _phang          # noqa: E402  (import cuối là chủ ý — cầu tương thích)
# re-export vài helper 2D cho kho phẳng gọi qua C.* (tương thích chữ ký cũ)
_o_vuong = _phang._o_vuong
_thu_tu  = _phang._thu_tu
_do_goc  = _phang._do_goc


# ═══ [29c] Ông Bụt 2026-09-16 · DS8 Chương 2 (Hằng đẳng thức) ═══
# HÌNH ĐẠI SỐ MINH HOẠ (nhãn BIẾN) — generator ĐỘC LẬP, KHÔNG qua PHANH/HinhCoBan.
#   Lý do tách engine: hình cắt-ghép/vành-khăn/khối-khoét là minh hoạ nhãn-biến
#   (a, b, x-2y…) — KHÔNG có quan hệ toạ-độ-số để PHANH verify. Ép vào .ve() phải
#   mổ render loop (rủi ro 20+ hàm cũ). Generator độc lập: tái dùng bản .tex/.py
#   ĐÃ ĐẠT (QC pass), giấu toạ độ (Đ5.9), 0 rủi ro regression.
def render_tikz_doc(tex_full, out, tra_bytes=False, dpi=200):
    """Biên dịch MỘT tài liệu TikZ standalone ĐẦY ĐỦ (documentclass→end) → PNG.
       Khác _render (nhận thân tikz + preamble cố định): hàm hình đại số cần preamble
       riêng (arrows.meta, even odd rule, style tô) nên tự cấp trọn tài liệu."""
    open(f'/tmp/{out}.tex', 'w').write(tex_full)
    subprocess.run(['pdflatex', '-interaction=nonstopmode', f'{out}.tex'],
                   cwd='/tmp', capture_output=True)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), f'{out}.pdf', out],
                   cwd='/tmp', capture_output=True)
    png = f'/tmp/{out}-1.png'
    if not os.path.exists(png):
        return None
    return open(png, 'rb').read() if tra_bytes else png

def _m(s, macdinh):
    """Nhãn: None → mặc định (biến); có $ → giữ; ngược lại bọc để in toán."""
    if s is None:
        return macdinh
    return str(s)
