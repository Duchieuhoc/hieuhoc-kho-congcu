#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# sinh_bantrich.py — TỰ SINH "bản trích hàm vẽ" cho AI Soạn
#   (song sinh với sinh_apiref.js: introspect KHO → bản trích, chống lệch code)
#
# Mô hình (X): OB giữ KHO (hinh_core + hinh_chNN), AI Soạn chỉ đọc BẢN TRÍCH.
# Bản trích = *CÁCH vẽ* (chữ ký hàm + tham số + mô tả). KHÔNG chứa code triển khai.
# Nguồn sự thật là chính file .py — vá kho → chạy lại script → bản trích khớp.
#
# PHÂN TẦNG: đọc metadata Ở KHO (HA_TANG / CUA_RENDER / LOP_MODULE). Kho chưa khai
#   → fallback heuristic (param x/y = hạ tầng) + cảnh báo. Nhóm HẠ TẦNG bị ẨN khỏi
#   bản phát cho AI Soạn (Đ5.9: người không cho tọa độ) — chỉ hiện với cờ --noi-bo.
#
#   Bản phát AI Soạn:  python3 sinh_bantrich.py hinh_ch8 HH6_CH08 > BAN_TRICH_HAM_HH6_CH08.md
#   Bản nội bộ (OB):   python3 sinh_bantrich.py hinh_ch8 HH6_CH08 --noi-bo
# ═══════════════════════════════════════════════════════════════════
import inspect, ast, sys, importlib, datetime

def _mo_ta_tu_comment(src_lines, def_lineno):
    """Gộp các dòng comment '#' liền ngay TRÊN dòng def (mô tả nằm ở comment)."""
    out = []
    i = def_lineno - 2
    while i >= 0 and src_lines[i].strip().startswith('#'):
        t = src_lines[i].strip().lstrip('#').strip().strip('─').strip()
        if t and not t.startswith('='):
            out.append(t)
        i -= 1
    return ' '.join(reversed(out))

def _mo_ta_tu_docstring(func):
    d = inspect.getdoc(func)
    return ' '.join(d.split()) if d else ''

def _chu_ky(name, func):
    sig = inspect.signature(func)
    params = [p for p in sig.parameters.values() if p.name != 'self']
    return f"{name}(" + ", ".join(str(p) for p in params) + ")"

def _co_toa_do(func):
    ps = inspect.signature(func).parameters
    return ('x' in ps) or ('y' in ps)

def sinh(ten_module, ma_chuong=None, noi_bo=False):
    mod = importlib.import_module(ten_module)
    Hinh = mod.Hinh
    src_lines = inspect.getsource(mod).splitlines()

    # metadata phân tầng — đọc Ở KHO (nguồn sự thật)
    HA_TANG = getattr(mod, 'HA_TANG', None)
    CUA = getattr(mod, 'CUA_RENDER', {'ve'})
    LOP = getattr(mod, 'LOP_MODULE', None)
    canh_bao = []
    # Phân tầng: ưu tiên prefix '_' (chuẩn mới); nếu kho còn khai HA_TANG tay thì tôn trọng.
    dung_prefix = HA_TANG is None

    tree = ast.parse(inspect.getsource(mod))
    lineno = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == 'Hinh':
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef):
                    lineno[sub.name] = sub.lineno

    khai, hatang, cua = [], [], []
    for name, func in inspect.getmembers(Hinh, inspect.isfunction):
        if name.startswith('__'):
            continue
        mota = _mo_ta_tu_docstring(func) or _mo_ta_tu_comment(src_lines, lineno.get(name, 2))
        rec = (_chu_ky(name, func), mota)
        if name in CUA:
            cua.append(rec)
        elif ((name.startswith('_')) if dung_prefix else (name in HA_TANG)):
            hatang.append(rec)
        else:
            khai.append(rec)

    ngay = datetime.date.today().strftime('%d/%m/%Y')
    td_chuong = f" — {ma_chuong}" if ma_chuong else ""
    td_lop = f" (Hình học lớp {', '.join(map(str, LOP))})" if LOP else ""
    L = []
    L.append(f"# BẢN TRÍCH HÀM VẼ{td_chuong}{td_lop} — tự sinh từ `{ten_module}.py`")
    L.append("")
    L.append(f"> **Cho AI Soạn.** Đây là *CÁCH vẽ* (chữ ký hàm + tham số). "
             f"*VẼ CÁI GÌ* nằm ở **phiếu khai nghĩa** Ông Bụt giao kèm nguồn.")
    L.append(f"> Tự sinh bằng introspect `{ten_module}.py` qua `sinh_bantrich.py` — "
             f"vá kho → chạy lại → khớp. KHÔNG sửa tay file này.")
    L.append(f"> Sinh ngày {ngay}. Mô hình (X): OB khai nghĩa → AI Soạn GỌI HÀM theo phiếu → PHANH kiểm.")
    L.append("")
    L.append(f"Import trong script bài: `import {ten_module} as H8` rồi `h = H8.Hinh()`.")
    L.append("Gọi các method KHAI NGHĨA (mục 1) theo phiếu; cuối cùng `png = h.ve(out=..., tra_bytes=True)`.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 1. HÀM KHAI NGHĨA — AI Soạn GỌI theo phiếu")
    L.append("")
    L.append("Mỗi hàm nhận NGHĨA (tên đỉnh/tia, số đo, loại quan hệ). Máy tự tính tọa độ + PHANH kiểm.")
    L.append("")
    L.append("| Hàm (chữ ký) | Dùng khi |")
    L.append("|---|---|")
    for ck, mota in sorted(khai):
        L.append(f"| `{ck}` | {mota or '—'} |")
    L.append("")
    L.append("## 2. CỬA RENDER")
    L.append("")
    L.append("| Hàm (chữ ký) | Dùng khi |")
    L.append("|---|---|")
    for ck, mota in cua:
        L.append(f"| `{ck}` | {mota or 'Chạy PHANH toàn bộ ràng buộc rồi render TikZ→PNG. Sai là raise.'} |")
    L.append("")
    L.append("## 3. HÀM HẠ TẦNG — máy dùng nội bộ, **AI Soạn KHÔNG gọi**")
    L.append("")
    L.append("Các hàm hạ tầng (nhận tọa độ thô hoặc cần điểm đặt trước) do các hàm khai nghĩa ở mục 1 "
             "tự gọi bên trong. Theo Đ5.9, người không cho tọa độ → **AI Soạn không gọi trực tiếp "
             "nhóm này**. Danh sách đã ẩn khỏi bản trích. Gặp hình mà mục 1 chưa phủ (vd đa giác "
             "thường) → **DỪNG báo Ông Bụt bổ sung hàm thuần-nghĩa** (khép vòng A↔C), KHÔNG tự dùng "
             "hàm hạ tầng.")

    if noi_bo:
        L.append("")
        L.append("### (Nội bộ OB — nhóm hạ tầng đã ẩn khỏi bản phát)")
        L.append("")
        L.append("| Hàm (chữ ký) | Ghi chú |")
        L.append("|---|---|")
        for ck, mota in sorted(hatang):
            L.append(f"| `{ck}` | {mota or '—'} |")

    L.append("")
    L.append("---")
    L.append("")
    L.append(f"**Thống kê:** {len(khai)} hàm khai nghĩa (phơi) · {len(cua)} cửa render · "
             f"{len(hatang)} hàm hạ tầng (ẩn khỏi bản phát).")
    if LOP is None:
        L.append("")
        L.append("> **Nợ:** kho chưa khai `LOP_MODULE` → bản trích chưa ghi lớp áp dụng.")
    for cb in canh_bao:
        L.append("")
        L.append(f"> ⚠️ {cb}")
    return "\n".join(L)

if __name__ == '__main__':
    raw = sys.argv[1:]
    noi_bo = '--noi-bo' in raw
    args = [a for a in raw if a != '--noi-bo']
    if not args:
        print("Dùng: python3 sinh_bantrich.py <ten_module> [ma_chuong] [--noi-bo]", file=sys.stderr)
        sys.exit(1)
    module = args[0]
    ma = args[1] if len(args) > 1 else None
    print(sinh(module, ma, noi_bo=noi_bo))
