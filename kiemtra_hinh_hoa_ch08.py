#!/usr/bin/env python3
# kiemtra_hinh_hoa_ch08.py — self-test module hình chương VIII (mốc 38a).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hinh_hoa_ch08 as H8
def main():
    fns = {n: getattr(H8, n) for n in ['na_ethylic','chay_ethylic','ester_hoa','so_sanh_hcl_acetic']}
    assert H8.CUA_RENDER == set(fns), f'CUA_RENDER lệch: {H8.CUA_RENDER}'
    for name, fn in fns.items():
        b = fn(tra_bytes=True)
        assert b and len(b) > 2000, f'{name} render FAIL'
        assert hasattr(fn,'CHU_GIAI') and fn.CHU_GIAI, f'{name} thiếu CHU_GIAI'
        print(f'  ✓ {name}: {len(b)}B · chú giải {len(fn.CHU_GIAI)} mục')
    print('✓ self-test 4/4 OK (mốc 38a)')
if __name__ == '__main__':
    main()
