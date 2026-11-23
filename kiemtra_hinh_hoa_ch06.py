#!/usr/bin/env python3
# kiemtra_hinh_hoa_ch06.py — OB kiểm module TRƯỚC KHI push GitHub (§7 checklist kho).
# Chạy TRONG ~/kho sau khi đặt hinh_hoa_ch06.py vào kho:
#   python3 kiemtra_hinh_hoa_ch06.py
# Kiểm: import OK + render 5/5 hình (3 TN bình khí + mạch điện + thìa nhiệt) ra PNG hợp lệ.
import os, sys
sys.path.insert(0, os.getcwd())
import hinh_hoa_ch06 as H6

OUT = '/tmp/kiemtra_hoa6'; os.makedirs(OUT, exist_ok=True)
jobs = {
    'Fe_O2':  lambda: H6.phan_ung_phi_kim('Fe_O2',  tra_bytes=True),
    'Na_Cl2': lambda: H6.phan_ung_phi_kim('Na_Cl2', tra_bytes=True),
    'Fe_Cl2': lambda: H6.phan_ung_phi_kim('Fe_Cl2', tra_bytes=True),
    'mach':   lambda: H6.mach_thu_dan_dien(tra_bytes=True),
    'nhiet':  lambda: H6.thi_nghiem_dan_nhiet(tra_bytes=True),
}
ok = 0
for name, fn in jobs.items():
    try:
        b = fn()
        assert b and b[:8] == b'\x89PNG\r\n\x1a\n', 'không phải PNG hợp lệ'
        open(f'{OUT}/{name}.png', 'wb').write(b)
        print(f'  ✓ {name}: {len(b)} bytes'); ok += 1
    except Exception as e:
        print(f'  ✗ {name}: {type(e).__name__}: {e}')
# PHANH test (phải raise)
try:
    H6.phan_ung_phi_kim('XX'); print('  ✗ PHANH không bắt tên lạ')
except ValueError:
    print('  ✓ PHANH bắt tên lạ')
print(f'\n{"ĐẠT" if ok == 5 else "LỖI"} — render {ok}/5. PNG ở {OUT}')
sys.exit(0 if ok == 5 else 1)
