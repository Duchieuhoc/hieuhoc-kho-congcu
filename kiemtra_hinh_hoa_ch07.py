#!/usr/bin/env python3
# kiemtra_hinh_hoa_ch07.py — self-test module hình chương VII (mốc 37a).
#   Render 2 hàm, kiểm có .CHU_GIAI, kiểm CUA_RENDER khớp. Chạy trong kho.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hinh_hoa_ch07 as H7

def main():
    fns = {'dot_butane': H7.dot_butane, 'dieu_che_ethylene': H7.dieu_che_ethylene}
    assert H7.CUA_RENDER == set(fns), f'CUA_RENDER lệch: {H7.CUA_RENDER}'
    for name, fn in fns.items():
        b = fn(tra_bytes=True)
        assert b and len(b) > 2000, f'{name} render FAIL'
        assert hasattr(fn, 'CHU_GIAI') and fn.CHU_GIAI, f'{name} thiếu CHU_GIAI'
        print(f'  ✓ {name}: {len(b)} bytes · chú giải {len(fn.CHU_GIAI)} mục')
    print('✓ self-test 2/2 OK (mốc 37a)')

if __name__ == '__main__':
    main()
