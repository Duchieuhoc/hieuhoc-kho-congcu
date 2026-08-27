# -*- coding: utf-8 -*-
# Render toàn bộ hình HH6_CH05_B22 — AI Soạn gọi hàm theo PHIEU_KHAI_NGHIA + BAN_TRICH.
# Xuất PNG ra /tmp/figs_b22/<token>-1.png ; in bytes + so_o_ngang cho build.
import os, json, shutil
import hinh_ch5 as H5

OUT = "/tmp/figs_b22"
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)

meta = {}   # token -> so_o_ngang

def R(token, fn):
    h = H5.Hinh()
    fn(h)
    b = h.ve(out=token, tra_bytes=True)
    src = f"/tmp/{token}-1.png"
    dst = f"{OUT}/{token}.png"
    shutil.copy(src, dst)
    meta[token] = h.so_o_ngang
    flag = "  <<<500B?" if len(b) < 500 else ""
    print(f"OK {token:16s} bytes={len(b):5d} o_ngang={h.so_o_ngang}{flag}")

# ---------- helpers lưới (vẽ-thêm qua tâm O) ----------
def grid_de(pts, order, Ocr):
    def fn(h):
        for n,(c,r) in pts.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
        h.noi(*order, kin=True)
        h.diem_luoi('O',Ocr[0],Ocr[1],nhan='O',cham=True)
    return fn

def grid_lg(pts, order, Ocr):
    def fn(h):
        for n,(c,r) in pts.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
        h.noi(*order, kin=True)
        h.diem_luoi('O',Ocr[0],Ocr[1],nhan='O',cham=True)
        Ox,Oy = Ocr
        for n,(c,r) in pts.items():
            h.diem_luoi(n+'x', 2*Ox-c, 2*Oy-r, nhan=None, cham=False, mau='red')
        h.noi(*[n+'x' for n in order], kin=True, mau='red')
    return fn

# ---------- ② KIẾN THỨC ----------
R('f02_dn',    lambda h: h.ngoi_sao('O', so_canh=6, ban_kinh=1.8, cham_tam=True))
def _bh(h): h.tu_giac('A','B','C','D',loai='binh_hanh'); h.tam_doi_xung('O',('A','C'),('B','D'))
R('f02_bh', _bh)
def _cn(h): h.tu_giac('A','B','C','D',loai='chu_nhat'); h.tam_doi_xung('O',('A','C'),('B','D'))
R('f02_cn', _cn)
def _vuong(h): h.hinh_vuong('M','N','P','Q',canh=4); h.tam_doi_xung('O',('M','P'),('N','Q'))
R('f02_vuong', _vuong)
R('f02_lgd',   lambda h: h.luc_giac_deu('A','B','C','D','E','F',canh=2.0,cheo='chinh',tam='O'))

# ---------- ③ D1 NHẬN BIẾT ----------
R('f_d1_sao5', lambda h: h.ngoi_sao('O', so_canh=5, ban_kinh=1.6))
R('f_d1_sao6', lambda h: h.ngoi_sao('O', so_canh=6, ban_kinh=1.6))
R('f_d1_sao4', lambda h: h.ngoi_sao('O', so_canh=4, ban_kinh=1.6))

# ---------- ③ D2 XÁC ĐỊNH TÂM ----------
R('f_d2_de', lambda h: h.luc_giac_deu('A','B','C','D','E','F',canh=2.0))          # plain (đề)
# lời giải D2 dùng lại f02_lgd (lục giác + 3 chéo chính + O)

# ---------- ③ D3 VẼ THÊM (VD: bậc thang A-F, O(4,2)) ----------
_d3_pts = {'a':(0,0),'b':(2,0),'c':(2,1),'d':(1,1),'e':(1,2),'f':(0,2)}
_d3_ord = ['a','b','c','d','e','f']
R('f_d3_de', grid_de(_d3_pts, _d3_ord, (2,2)))
R('f_d3_lg', grid_lg(_d3_pts, _d3_ord, (2,2)))

# ---------- ③ D4 GẤP-CẮT (sơ đồ hình học thuần) ----------
def _d4(h):
    for n,(c,r) in {'p':(0,0),'q':(4,0),'r':(4,4),'s':(0,4)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.noi('p','q','r','s',kin=True)
    for n,(c,r) in {'gt':(2,0),'gb':(2,4),'gl':(0,2),'gr':(4,2)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.doan('gt','gb',net='dut'); h.doan('gl','gr',net='dut')
    for n,(c,r) in {'k1':(1,4),'k2':(1,3),'k3':(3,3),'k4':(3,4)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.noi('k1','k2','k3','k4',mau='red')
    h.diem_luoi('O',2,2,nhan='O',cham=True)
R('f_d4_schema', _d4)

# ---------- ③ D5 TÍNH (thoi THGT B7: OA=4, OB=3, cạnh 5) ----------
def _d5(h):
    h.hinh_thoi('A','B','C','D',a=2,b=1,cheo=True,tam='O')
    h.doan('O','A',dodai='4 cm'); h.doan('O','B',dodai='3 cm'); h.doan('A','B',dodai='5 cm')
R('f_d5_de', _d5)

# ---------- ④ BT TẠI LỚP ----------
# BT1 (D1): 4 hình plain
R('f_bt1_thoi',     lambda h: h.hinh_thoi('A','B','C','D',a=2,b=1,cheo=False,tam=None))
R('f_bt1_tgd',      lambda h: h.tam_giac_deu('A','B','C',canh=3.0))
R('f_bt1_tron',     lambda h: h.duong_tron('O',ban_kinh=1.6,hien_tam=False))
R('f_bt1_thangcan', lambda h: h.hinh_thang_can('A','B','C','D',day_nho=2.0,day_lon=3.6,cao=2.0))
# BT2 (D2): đề plain (lời giải dùng lại f02_cn, f02_lgd)
R('f_bt2_cn_de', lambda h: h.tu_giac('A','B','C','D',loai='chu_nhat'))
R('f_bt2_lg_de', lambda h: h.luc_giac_deu('M','N','P','Q','R','S',canh=2.0))
# BT3 (D3): L khác VD, O(3,2)
_bt3_pts = {'a':(0,0),'b':(2,0),'c':(2,2),'d':(1,2),'e':(1,1),'f':(0,1)}
_bt3_ord = ['a','b','c','d','e','f']
R('f_bt3_de', grid_de(_bt3_pts, _bt3_ord, (2,2)))
R('f_bt3_lg', grid_lg(_bt3_pts, _bt3_ord, (2,2)))
# BT4 (D4): sơ đồ gấp tư (không nét cắt — HS tự nêu cách cắt chữ N)
def _bt4(h):
    for n,(c,r) in {'p':(0,0),'q':(4,0),'r':(4,4),'s':(0,4)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.noi('p','q','r','s',kin=True)
    for n,(c,r) in {'gt':(2,0),'gb':(2,4),'gl':(0,2),'gr':(4,2)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.doan('gt','gb',net='dut'); h.doan('gl','gr',net='dut')
    h.diem_luoi('O',2,2,nhan='O',cham=True)
R('f_bt4_gap', _bt4)

# ---------- ⑤ BTVN ----------
# Phần II Câu 2: dùng lại f02_bh (bình hành + chéo + O)
# Phần III Câu 1 (VD): đoạn AB=4, O trung điểm
def _p3c1(h):
    h.doan_le('A','B',dai=4.0,dodai='4 cm')
    h.diem_giua('O','A','B',0.5,nhan='below')     # O xuống dưới, tránh đè "4 cm"
R('f_p3c1_doan', _p3c1)
# Phần III Câu 2 (VDC): thoi 2 chéo 6 & 8 → S. Số đưa vào ĐỀ (nhãn chéo rơi vào O → bỏ).
def _p3c2(h):
    h.hinh_thoi('A','B','C','D',a=2,b=1,cheo=True,tam='O')
R('f_p3c2_thoi', _p3c2)

# Tự luận BT1 (D3 grid #1): bậc thang, O(4,2)
_tl1_pts = {'a':(0,0),'b':(2,0),'c':(2,1),'d':(1,1),'e':(1,2),'f':(0,2)}
_tl1_ord = ['a','b','c','d','e','f']
R('f_tl1_de', grid_de(_tl1_pts, _tl1_ord, (2,2)))
R('f_tl1_lg', grid_lg(_tl1_pts, _tl1_ord, (2,2)))
# Tự luận BT2 (D3 grid #2): chữ L đứng, O(4,2)
_tl2_pts = {'a':(0,0),'b':(2,0),'c':(2,1),'d':(1,1),'e':(1,2),'f':(0,2)}
_tl2_ord = ['a','b','c','d','e','f']
R('f_tl2_de', grid_de(_tl2_pts, _tl2_ord, (2,2)))
R('f_tl2_lg', grid_lg(_tl2_pts, _tl2_ord, (2,2)))
# Tự luận BT3 (D4 gấp-cắt): sơ đồ có nét cắt khác
def _tl3(h):
    for n,(c,r) in {'p':(0,0),'q':(4,0),'r':(4,4),'s':(0,4)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.noi('p','q','r','s',kin=True)
    for n,(c,r) in {'gt':(2,0),'gb':(2,4),'gl':(0,2),'gr':(4,2)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.doan('gt','gb',net='dut'); h.doan('gl','gr',net='dut')
    for n,(c,r) in {'k1':(0,3),'k2':(1,3),'k3':(1,4)}.items(): h.diem_luoi(n,c,r,nhan=None,cham=False)
    h.noi('k1','k2','k3',mau='red')
    h.diem_luoi('O',2,2,nhan='O',cham=True)
R('f_tl3_gap', _tl3)
# Tự luận BT4 (D5 lục giác mặt bàn 5.14): dùng lại f02_lgd (nhãn "1,2 m" ở AD rơi vào O → số vào ĐỀ)
# Tự luận BT5 (D5 thoi biến thể): AC=12, BD=8 → số vào ĐỀ (nhãn chéo rơi vào O → bỏ)
def _tl5(h):
    h.hinh_thoi('A','B','C','D',a=2,b=1,cheo=True,tam='O')
R('f_tl5_thoi', _tl5)

json.dump(meta, open(f"{OUT}/_meta.json","w"))
print("\nTOTAL:", len(meta), "figures ->", OUT)
