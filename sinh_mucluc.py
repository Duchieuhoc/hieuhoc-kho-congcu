#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# sinh_mucluc.py — MỤC LỤC HÀM TỔNG (một chỗ tra "đã-có-chưa")
#   Vá gốc bệnh DS9: tra cứu rời rạc (API_REFERENCE ⟂ BAN_TRICH rải theo chương).
#   TÁI DÙNG, KHÔNG parse độc lập (điều kiện OB Hình):
#     • Python: import sinh_bantrich → dùng CHÍNH bộ trích của nó (_chu_ky, _mo_ta_*).
#     • JS:     đọc API_REFERENCE.md — đây LÀ output của sinh_apiref.js (nguồn sự thật JS).
#   ⟹ Không đẻ nguồn-sự-thật thứ ba.
#   Chạy:  python3 sinh_mucluc.py > 00_MUC_LUC_HAM.md
# CS2627 · [29z] OB Đại số 2026-09-21.
# ═══════════════════════════════════════════════════════════════════
import inspect, importlib, glob, os, re, datetime, sys
import sinh_bantrich as SB
import hinh_coban as _hcb

# ── Nhóm NGHĨA theo module (tra theo nghĩa, không theo file/chương) ──
NHOM = {
    'hinh_toado':   'Toạ độ & trục số (DÙNG CHUNG)',
    'hinh_daiso':   'Số & Đại số (tia số/trục số/toạ độ/diện tích đại số)',
    'hinh_coban':   'Hình phẳng — nền (điểm/đoạn/đường/góc)',
    'hinh_dagiac':  'Đa giác',
    'hinh_tron':    'Đường tròn', 'hinh_tron_ve': 'Đường tròn (dựng)',
    'hinh_gocdt':   'Góc & đường thẳng',
    'hinh_doixung': 'Đối xứng', 'hinh_tamgiac': 'Tam giác',
    'hinh_khoihop': 'Khối / không gian', 'hinh_phang': 'Hình phẳng (luật/đo)',
    'hinh_hoa_ch01':'Hoá học', 'hinh_hoa_ch02': 'Hoá học',
}
def _nhom(mod): return NHOM.get(mod, 'Theo chương / khác')

def _kieu(name):
    # generator standalone (tiền tố 'hinh…', gắn staticmethod) vs method-trên-Hinh
    return 'generator' if name.startswith('hinh') else 'method'

def _tang(mod):
    # tầng lớp tái dùng (best-effort theo module; '—' nếu chưa khai)
    if mod in ('hinh_toado', 'hinh_daiso'): return 'L6→9→THPT'
    if mod in ('hinh_coban', 'hinh_phang'): return 'mọi lớp (nền)'
    return '—'

# ═══ 1) PHÍA PYTHON — tái dùng bộ trích của sinh_bantrich ═══
def quet_python():
    rows = []
    for path in sorted(glob.glob('hinh_*.py')):
        mod_name = os.path.splitext(os.path.basename(path))[0]
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            continue
        Hinh = getattr(mod, 'Hinh', None)
        if Hinh is None:
            for _n, _c in inspect.getmembers(mod, inspect.isclass):
                if (issubclass(_c, _hcb.HinhCoBan) and _c is not _hcb.HinhCoBan
                        and _c.__module__ == mod.__name__):
                    Hinh = _c; break
        if Hinh is None:
            continue
        try:
            src = inspect.getsource(mod).splitlines()
        except OSError:
            src = []
        seen = set()
        def _add(name, func):
            # Liệt kê MỌI hàm figure công khai; chỉ bỏ cửa render chung 've' + hàm nội bộ '_…'.
            # (Module hoá dùng chính hàm figure làm cửa render → vẫn phải hiện ở mục lục.)
            if name.startswith('_') or name == 've' or name in seen:
                return
            if getattr(func, '__module__', None) != mod.__name__:   # khử trùng kế thừa
                return
            seen.add(name)
            mota = SB._mo_ta_tu_docstring(func)            # ← tái dùng bộ trích bantrich
            mota = (mota or '').split('. ')[0][:150]
            rows.append((_nhom(mod_name), SB._chu_ky(name, func), mota,
                         mod_name + '.py', _kieu(name), _tang(mod_name)))
        # (a) method KHAI NGHĨA trên class entry (ẩn hạ tầng/cửa render — Đ5.9)
        for name, func in inspect.getmembers(Hinh, inspect.isfunction):
            _add(name, func)
        # (b) hàm module-level công khai (generator độc lập chưa gắn class — vd hoá học)
        for name, func in inspect.getmembers(mod, inspect.isfunction):
            _add(name, func)
    return rows

# ═══ 2) PHÍA JS — đọc API_REFERENCE.md (output của sinh_apiref.js) ═══
def quet_js(apiref='API_REFERENCE.md'):
    rows = []
    if not os.path.exists(apiref):
        return rows
    ver = ''
    lines = open(apiref, encoding='utf-8').read().splitlines()
    for i, ln in enumerate(lines):
        if not ver:
            m = re.search(r'v\d+\.\d+', ln)
            if m: ver = m.group(0)
        m = re.match(r'^### `([^`]+)`', ln)
        if m:
            sig = m.group(1)
            mota = ''
            for j in range(i + 1, min(i + 4, len(lines))):
                t = lines[j].strip()
                if t and not t.startswith('#') and not t.startswith('`'):
                    mota = t[:150]; break
            rows.append(('Dựng Word (template JS %s)' % ver, sig, mota,
                         'hieuhoc_template.js', 'JS', '—'))
    return rows

def main():
    py, js = quet_python(), quet_js()
    ngay = datetime.date.today().strftime('%d/%m/%Y')
    L = []
    L.append('# 00_MUC_LUC_HAM — MỤC LỤC HÀM TỔNG (tra "đã-có-chưa" TRƯỚC khi viết)')
    L.append('')
    L.append('> **Tự sinh** bởi `sinh_mucluc.py` — TÁI DÙNG `sinh_bantrich.py` (Python) '
             '+ `API_REFERENCE.md` (output `sinh_apiref.js`, JS). KHÔNG sửa tay.')
    L.append('> Regen: `python3 sinh_mucluc.py > 00_MUC_LUC_HAM.md`. Sinh ngày %s.' % ngay)
    L.append('> **LUẬT VÀNG:** trước khi viết hàm mới → tra file này (Ctrl+F theo NGHĨA). '
             'Có hàm khớp → GỌI LẠI. Gần giống → MỞ RỘNG. Viết mới là bậc CUỐI.')
    L.append('')
    L.append('*Ẩn: hàm hạ tầng (`_…`) + cửa render (`ve`) theo Đ5.9. '
             'Base compose per-bài không vào kho → không liệt kê.*')
    L.append('')
    # gộp theo nhóm nghĩa
    allrows = py + js
    nhoms = []
    for r in allrows:
        if r[0] not in nhoms: nhoms.append(r[0])
    for nh in nhoms:
        rs = [r for r in allrows if r[0] == nh]
        L.append('## %s  · %d hàm' % (nh, len(rs)))
        L.append('')
        L.append('| Hàm | Nghĩa | File | Kiểu | Tầng |')
        L.append('|---|---|---|---|---|')
        for _, sig, mota, f, kieu, tang in sorted(rs, key=lambda x: x[1]):
            L.append('| `%s` | %s | `%s` | %s | %s |' % (sig, mota or '—', f, kieu, tang))
        L.append('')
    L.append('---')
    L.append('**Thống kê:** %d hàm Python (vẽ hình) + %d hàm JS (dựng Word) = %d.'
             % (len(py), len(js), len(py) + len(js)))
    print('\n'.join(L))

if __name__ == '__main__':
    main()
