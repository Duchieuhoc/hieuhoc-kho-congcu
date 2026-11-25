#!/usr/bin/env python3
# OB kiểm module TRƯỚC KHI push. Chạy trong ~/kho: python3 kiemtra_hinh_hoa_ch06.py
import os, sys
sys.path.insert(0, os.getcwd())
import hinh_hoa_ch06 as H6
OUT='/tmp/kiemtra_hoa6'; os.makedirs(OUT, exist_ok=True)
jobs = {
 'Fe_O2': lambda: H6.phan_ung_phi_kim('Fe_O2', tra_bytes=True),
 'Na_Cl2': lambda: H6.phan_ung_phi_kim('Na_Cl2', tra_bytes=True),
 'Fe_Cl2': lambda: H6.phan_ung_phi_kim('Fe_Cl2', tra_bytes=True),
 'mach': lambda: H6.mach_thu_dan_dien(tra_bytes=True),
 'nhiet': lambda: H6.thi_nghiem_dan_nhiet(tra_bytes=True),
 'Fe_HCl': lambda: H6.thi_nghiem_day_hoat_dong('Fe_HCl', tra_bytes=True),
 'Cu_AgNO3': lambda: H6.thi_nghiem_day_hoat_dong('Cu_AgNO3', tra_bytes=True),
 'dienphan': lambda: H6.be_dien_phan_nhom(tra_bytes=True),
 'locao': lambda: H6.lo_cao_luyen_gang(tra_bytes=True),
 'lothoi': lambda: H6.lo_thoi_luyen_thep(tra_bytes=True),
 'cotthan': lambda: H6.cot_loc_than(tra_bytes=True),
}
ok = 0
for name, fn in jobs.items():
    try:
        b = fn(); assert b and b[:8] == b'\x89PNG\r\n\x1a\n'
        open(f'{OUT}/{name}.png','wb').write(b); print(f'  OK {name}: {len(b)}'); ok += 1
    except Exception as e:
        print(f'  FAIL {name}: {type(e).__name__}: {e}')
for bad, fn in [('XX', lambda: H6.phan_ung_phi_kim('XX')), ('ZZ', lambda: H6.thi_nghiem_day_hoat_dong('ZZ'))]:
    try: fn(); print(f'  PHANH miss ({bad})')
    except ValueError: print(f'  PHANH OK ({bad})')
print(f'\n{"ĐẠT" if ok==11 else "LỖI"} — render {ok}/11.')
sys.exit(0 if ok==11 else 1)
