#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# cua_quet_hinh.py — CỬA QUÉT script vẽ hình (tiền kiểm AST, chạy TRƯỚC khi build)
#   Song sinh với cua_quet_soan.js. Đóng kín van Đ5.9 ở TẦNG CỨNG thứ 2
#   (tầng 1 = bản trích đã ẩn hàm hạ tầng; tầng này chặn nếu AI Soạn vẫn gọi lén).
#
#   WHITELIST ĐỒNG NGUỒN: introspect chính kho `hinh_ch8.py` bằng cùng quy tắc
#   prefix '_' như sinh_bantrich.py — KHÔNG hard-code danh sách, không lệch bản trích.
#
#   Chặn cứng 4 loại vi phạm:
#     (1) Gọi HÀM HẠ TẦNG  (method prefix '_')            — vi phạm Đ5.9
#     (2) Gọi HÀM KHÔNG CÓ trong kho                       — typo / OB kê thiếu (A↔C)
#     (3) VƯỢT CỬA lõi     (import hinh_core, đụng .V/.rb/.tikz, tự dựng TikZ thô)
#     (4) KHÔNG qua .ve()  (khai hình mà thiếu cửa PHANH+render)
#
#   Dùng:  python3 cua_quet_hinh.py <script_bai.py> [--kho hinh_ch8]
#   Mã thoát: 0 = sạch, 1 = có vi phạm (in danh sách), 2 = lỗi dùng.
# ═══════════════════════════════════════════════════════════════════
import ast, sys, inspect, importlib

def _tap_ham_kho(ten_kho):
    """Introspect kho → (phơi, hạ tầng). Cùng quy tắc prefix '_' với sinh_bantrich."""
    mod = importlib.import_module(ten_kho)
    Hinh = mod.Hinh
    phoi, hatang = set(), set()
    for name, _ in inspect.getmembers(Hinh, inspect.isfunction):
        if name.startswith('__'):
            continue
        (hatang if name.startswith('_') else phoi).add(name)
    return phoi, hatang     # 've' nằm trong phơi (không '_') → hợp lệ để gọi

# thuộc tính nội bộ của Hinh — script bài KHÔNG được đụng thẳng (phải qua hàm khai nghĩa)
_THUOC_TINH_CAM = {'V', 'rb', 'tikz', 'nhan', 'moc'}
_LOI_CAM = {'phanh', '_render', '_o_vuong', '_do_goc', '_thu_tu'}  # lõi — không gọi trực tiếp

def quet(duong_dan, ten_kho='hinh_ch8'):
    phoi, hatang = _tap_ham_kho(ten_kho)
    src = open(duong_dan, encoding='utf-8').read()
    try:
        cay = ast.parse(src)
    except SyntaxError as e:
        return [f"[LỖI CÚ PHÁP] {e}"]

    vp = []                       # danh sách vi phạm
    bien_hinh = set()             # tên biến là instance Hinh
    co_tao_hinh = False
    co_goi_ve = False

    # vòng 1: tìm biến gán từ *.Hinh() hoặc Hinh()
    for node in ast.walk(cay):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            f = node.value.func
            ten_goi = (f.attr if isinstance(f, ast.Attribute)
                       else f.id if isinstance(f, ast.Name) else None)
            if ten_goi == 'Hinh':
                co_tao_hinh = True
                for t in node.targets:
                    if isinstance(t, ast.Name):
                        bien_hinh.add(t.id)

    # vòng 2: quét lời gọi / truy cập
    for node in ast.walk(cay):
        # (3a) cấm import hinh_core trong script bài
        if isinstance(node, ast.Import):
            for n in node.names:
                if n.name in ('hinh_core','hinh_phang') or n.name.endswith(('.hinh_core','.hinh_phang')):
                    vp.append(f"[3-VƯỢT CỬA] dòng {node.lineno}: import `{n.name}` — "
                              f"lõi do kho tự gọi, script bài KHÔNG import trực tiếp.")
        if isinstance(node, ast.ImportFrom) and (node.module or '').endswith(('hinh_core','hinh_phang')):
            vp.append(f"[3-VƯỢT CỬA] dòng {node.lineno}: from `{node.module}` — cấm.")

        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            owner = node.func.value
            owner_ten = owner.id if isinstance(owner, ast.Name) else None
            ln = node.func.lineno

            # (3b) gọi lõi trực tiếp qua bí danh module (vd C.phanh, C._render)
            if attr in _LOI_CAM and owner_ten and owner_ten not in bien_hinh:
                vp.append(f"[3-VƯỢT CỬA] dòng {ln}: gọi lõi `{owner_ten}.{attr}(...)` — "
                          f"chỉ `.ve()` được chạy PHANH/render.")
                continue

            # các lời gọi trên instance Hinh
            if owner_ten in bien_hinh:
                if attr == 've':
                    co_goi_ve = True
                elif attr in hatang or (attr.startswith('_') and not attr.startswith('__')):
                    vp.append(f"[1-HẠ TẦNG] dòng {ln}: gọi `{owner_ten}.{attr}(...)` — "
                              f"hàm hạ tầng, AI Soạn KHÔNG gọi (Đ5.9). Dùng hàm khai nghĩa phơi.")
                elif attr not in phoi:
                    vp.append(f"[2-KHÔNG CÓ] dòng {ln}: `{owner_ten}.{attr}(...)` không có trong "
                              f"kho `{ten_kho}` — typo hoặc OB kê thiếu hàm (DỪNG báo OB, khép A↔C).")

        # (3c) đụng thuộc tính nội bộ: h.V[...], h.rb.append(...), h.tikz...
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id in bien_hinh and node.attr in _THUOC_TINH_CAM:
                vp.append(f"[3-VƯỢT CỬA] dòng {node.lineno}: đụng thẳng "
                          f"`{node.value.id}.{node.attr}` — nội bộ máy, phải qua hàm khai nghĩa.")

    # (4) có tạo Hinh mà không qua cửa .ve()
    if co_tao_hinh and not co_goi_ve:
        vp.append("[4-THIẾU CỬA] có `Hinh()` nhưng KHÔNG gọi `.ve()` — hình chưa chạy PHANH/render.")

    # khử trùng lặp, giữ thứ tự
    thay = set(); sach = []
    for v in vp:
        if v not in thay:
            thay.add(v); sach.append(v)
    return sach

if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    kho = 'hinh_ch8'
    if '--kho' in sys.argv:
        kho = sys.argv[sys.argv.index('--kho') + 1]
    if not args:
        print("Dùng: python3 cua_quet_hinh.py <script_bai.py> [--kho hinh_ch8]", file=sys.stderr)
        sys.exit(2)
    loi = quet(args[0], kho)
    if not loi:
        print(f"✅ SẠCH — {args[0]} không có vi phạm (whitelist đồng nguồn từ `{kho}`).")
        sys.exit(0)
    print(f"❌ CHẶN — {args[0]} có {len(loi)} vi phạm:")
    for v in loi:
        print("  •", v)
    sys.exit(1)
