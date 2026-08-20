#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# quet_stamp.py — GATE chống lệch banner version (đầu phiên, sau bụng kho).
#   python3 quet_stamp.py <thư_mục_luật> [--chuan V11.6]
#   Chuẩn tự suy từ tên file HIEN_PHAP_CS2627_V11_X.md nếu không truyền.
#   Quét CHỈ HEADER (6 dòng đầu) — nhật ký/inline lịch sử KHÔNG tính là lệch.
#   Thoát mã 1 nếu có lệch (để chèn vào quy trình gate).
# Lý do tồn tại: mỗi lần bump HP phải sweep banner nhiều file → dễ sót;
#   công cụ này phát hiện ngay, không để AI Soạn báo [SỬA] về sau.
# ═══════════════════════════════════════════════════════════════════
import sys, os, re, glob

PAT = [                                    # các dạng banner version ở HEADER
    r'CS2627 \*\*(V11\.\d+)\*\*',
    r'HP CS2627 (V11\.\d+)',
    r'CS2627 (V11\.\d+)',
    r'Hiến Pháp CS2627 \*\*(V11\.\d+)\*\*',
    r'Đồng bộ CS2627 (V11\.\d+)',
]

def suy_chuan(folder):
    for p in glob.glob(os.path.join(folder, 'HIEN_PHAP_CS2627_V11_*.md')):
        m = re.search(r'V11_(\d+)', os.path.basename(p))
        if m:
            return f"V11.{m.group(1)}"
    return None

def quet(folder, chuan):
    print(f"QUÉT STAMP — chuẩn: {chuan}\n" + "=" * 52)
    lech = []
    for p in sorted(glob.glob(os.path.join(folder, '*.md'))):
        name = os.path.basename(p)
        if name.startswith(('NHAT_KY', 'BAN_GIAO_LUONG', '00_DANH_MUC')):
            continue                       # file snapshot/nhật ký — version cũ là lịch sử
        head = '\n'.join(open(p, encoding='utf-8').read().split('\n')[:6])
        vers = set()
        for pat in PAT:
            vers |= set(re.findall(pat, head))
        if not vers:
            continue                       # file không mang banner → bỏ qua
        bad = sorted(v for v in vers if v != chuan)
        if bad:
            lech.append((name, bad)); print(f"  ✗ {name}: header {bad} ≠ {chuan}")
        else:
            print(f"  ✓ {name}: {chuan}")
    print("=" * 52)
    print(f"⚠ LỆCH: {len(lech)} file — sweep banner header về {chuan}." if lech
          else f"✅ SẠCH — mọi banner header khớp {chuan}.")
    return len(lech)

if __name__ == '__main__':
    folder = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '.'
    chuan = None
    if '--chuan' in sys.argv:
        chuan = sys.argv[sys.argv.index('--chuan') + 1]
    chuan = chuan or suy_chuan(folder) or 'V11.6'
    sys.exit(1 if quet(folder, chuan) else 0)
