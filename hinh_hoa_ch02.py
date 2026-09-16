#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hoa_ch02.py — ENTRY chương: Hóa (KHTN) lớp 7 Chương II
#   "Phân tử · Liên kết hoá học". Dựng: mô hình phân tử (quả cầu-que),
#   mô hình hạt/mẫu chất, hộp hạt (SBT phân loại), sơ đồ liên kết ion,
#   sơ đồ liên kết cộng hoá trị. Generator ĐỘC LẬP, NGHĨA-THUẦN: hàm nhận
#   công thức / cấu hình, MÁY tự bố trí (layout ẩn trong kho, Đ5.9); PHANH
#   ngữ nghĩa → sai thì DỪNG. Xuất PNG buffer (hinhVe/hinhBenPhai).
#   [29f] Ông Bụt (Hóa) 2026-09-16.
# ═══════════════════════════════════════════════════════════════════
import math
import hinh_core as _HC

LOP_MODULE = [7]
CUA_RENDER = {'phan_tu', 'mo_hinh_hat', 'hop_hat', 'lien_ket_ion', 'lien_ket_cht'}

# Màu & bán kính quả cầu theo nguyên tố (quy ước dựng-lại, Đ42; gần CPK + SGK)
MAU_NT = {'H':'white','C':'gray!65!black','O':'red!80!black','N':'blue!65!white',
          'Cl':'green!60!black','Na':'magenta!70!black','Mg':'teal!70!black',
          'S':'yellow!80!black','P':'orange!80!black','F':'green!55!yellow','K':'violet'}
BK_NT  = {'H':0.26,'C':0.42,'O':0.40,'N':0.40,'Cl':0.50,'Na':0.55,'Mg':0.52,'default':0.40}
def _mau(s): return MAU_NT.get(s,'gray!55!black')
def _bk(s):  return BK_NT.get(s, BK_NT['default'])
def _txt(s): return 'black' if s in ('H','F') else 'white'   # chữ trên cầu sáng/tối

_PRE = (r'\documentclass[border=5pt]{standalone}'
        r'\usepackage{tikz}\usepackage{amsmath}'
        r'\usetikzlibrary{arrows.meta}\begin{document}')

# ── Layout phân tử (toạ độ ẩn trong kho = nghĩa-thuần) ──
# (ký hiệu, x, y) + liên kết (i, j, bậc)
_PT = {
 'H2': (['H','H'], [(-0.55,0),(0.55,0)], [(0,1,1)]),
 'Cl2':(['Cl','Cl'], [(-0.75,0),(0.75,0)], [(0,1,1)]),
 'O2': (['O','O'], [(-0.62,0),(0.62,0)], [(0,1,2)]),
 'N2': (['N','N'], [(-0.62,0),(0.62,0)], [(0,1,3)]),
 'HCl':(['H','Cl'], [(-0.62,0),(0.62,0)], [(0,1,1)]),
 'CO2':(['O','C','O'], [(-1.15,0),(0,0),(1.15,0)], [(0,1,2),(1,2,2)]),
 'H2O':(['O','H','H'], [(0,0.15),(-0.78,-0.55),(0.78,-0.55)], [(0,1,1),(0,2,1)]),
 'CH4':(['C','H','H','H','H'], [(0,0),(0,1.0),(0,-1.0),(-1.0,0),(1.0,0)],
        [(0,1,1),(0,2,1),(0,3,1),(0,4,1)]),
 'NH3':(['N','H','H','H'], [(0,0.25),(-0.85,-0.5),(0,-0.8),(0.85,-0.5)],
        [(0,1,1),(0,2,1),(0,3,1)]),
}
def _ball(sym,x,y,s=1.0):
    r=_bk(sym)*s
    return (f"  \\shade[ball color={_mau(sym)}] ({x*s:.3f},{y*s:.3f}) circle ({r:.3f});\n"
            f"  \\node[font=\\footnotesize\\bfseries,{_txt(sym)}] at ({x*s:.3f},{y*s:.3f}) {{{sym}}};")

# ═══════════ Hàm 1 — phan_tu(cong_thuc) : mô hình 1 phân tử ═══════════
def phan_tu(cong_thuc, out='hoa2_pt', tra_bytes=False):
    """Mô hình quả cầu-que của 1 phân tử (lớp 7): H2,Cl2,O2,N2,HCl,CO2,H2O,CH4,NH3.
       Quả cầu = nguyên tử (màu theo nguyên tố); que = liên kết (đơn/đôi/ba). NGHĨA-THUẦN."""
    if cong_thuc not in _PT:
        raise ValueError(f"[PHANH hoa2] chưa có layout phân tử '{cong_thuc}' (có: {sorted(_PT)}).")
    syms, pos, bonds = _PT[cong_thuc]
    s=1.0; sticks=[]
    for i,j,bac in bonds:
        (x1,y1),(x2,y2)=pos[i],pos[j]
        dx,dy=x2-x1,y2-y1; L=math.hypot(dx,dy); ox,oy=-dy/L,dx/L  # pháp tuyến
        offs={1:[0],2:[-0.09,0.09],3:[-0.14,0,0.14]}[bac]
        for o in offs:
            sticks.append(f"  \\draw[line width=2.6pt,gray!55!black] "
                          f"({x1+ox*o:.3f},{y1+oy*o:.3f})--({x2+ox*o:.3f},{y2+oy*o:.3f});")
    balls="\n".join(_ball(sy,x,y,s) for sy,(x,y) in zip(syms,pos))
    body=(_PRE+r'''
\begin{tikzpicture}[line join=round]
@@STICK@@
@@BALL@@
\end{tikzpicture}\end{document}''').replace('@@STICK@@',"\n".join(sticks)).replace('@@BALL@@',balls)
    return _HC.render_tikz_doc(body,out,tra_bytes)

# ═══════════ Hàm 2 — mo_hinh_hat : mẫu chất nhiều hạt ═══════════
def mo_hinh_hat(loai, nguyen_to=None, cong_thuc=None, ion_duong=None, ion_am=None,
                out='hoa2_hat', tra_bytes=False):
    """Mô hình HẠT của một mẫu chất. loai:
       'kim_loai' (nguyen_to): lưới quả cầu cùng màu xếp khít (vd Cu rắn);
       'khi_don'  (nguyen_to): các quả cầu đơn lẻ rời (khí hiếm, vd He);
       'phan_tu'  (cong_thuc): nhiều phân tử rời cùng loại (vd O2, CO2);
       'mang_ion' (ion_duong,ion_am): mạng 2 màu xen kẽ (vd Na+ / Cl-)."""
    el=[]
    if loai=='kim_loai':
        c=_mau(nguyen_to)
        for r in range(4):
            for q in range(5):
                x=q*0.62+(0.31 if r%2 else 0); y=r*0.54
                el.append(f"  \\shade[ball color={c}] ({x:.3f},{y:.3f}) circle (0.3);")
    elif loai=='khi_don':
        c=_mau(nguyen_to)
        import random; random.seed(7)
        for _ in range(9):
            x=random.uniform(0,3.2); y=random.uniform(0,2.4)
            el.append(f"  \\shade[ball color={c}] ({x:.3f},{y:.3f}) circle (0.28);")
    elif loai=='phan_tu':
        syms,pos,bonds=_PT[cong_thuc]
        import random; random.seed(3)
        for cx,cy in [(0.4,0.4),(1.9,0.9),(0.9,1.9),(2.6,2.1),(0.3,2.6)]:
            for i,j,_b in bonds:
                (x1,y1),(x2,y2)=pos[i],pos[j]
                el.append(f"  \\draw[line width=1.8pt,gray!55!black] ({cx+x1*0.5:.3f},{cy+y1*0.5:.3f})--({cx+x2*0.5:.3f},{cy+y2*0.5:.3f});")
            for sy,(x,y) in zip(syms,pos):
                el.append(f"  \\shade[ball color={_mau(sy)}] ({cx+x*0.5:.3f},{cy+y*0.5:.3f}) circle ({_bk(sy)*0.55:.3f});")
    elif loai=='mang_ion':
        for r in range(4):
            for q in range(4):
                x=q*0.7; y=r*0.7; pos_dup=(r+q)%2==0
                c=_mau(ion_duong) if pos_dup else _mau(ion_am)
                rr=0.24 if pos_dup else 0.32
                el.append(f"  \\shade[ball color={c}] ({x:.3f},{y:.3f}) circle ({rr:.3f});")
    else:
        raise ValueError(f"[PHANH hoa2] loai mô hình hạt lạ: {loai}")
    body=(_PRE+r'''
\begin{tikzpicture}[line join=round]
@@E@@
\end{tikzpicture}\end{document}''').replace('@@E@@',"\n".join(el))
    return _HC.render_tikz_doc(body,out,tra_bytes)

# ═══════════ Hàm 3 — hop_hat : hộp hạt trừu tượng (SBT phân loại) ═══════════
def hop_hat(items, nhan=None, out='hoa2_hop', tra_bytes=False):
    """Hộp chữ nhật chứa 'hạt' trừu tượng để phân loại đơn/hợp chất/hỗn hợp.
       items: list mô tả — mỗi phần tử là:
         ('don', mau)                → 1 nguyên tử lẻ;
         ('cap', mau1, mau2)         → 1 phân tử 2 nguyên tử (mau1==mau2: đơn chất; khác: hợp chất).
       Máy tự rải trong hộp. nhan: nhãn hộp (vd 'A')."""
    import random; random.seed(11)
    W,Hh=3.6,2.6; el=[f"  \\draw[thick,rounded corners=2pt] (0,0) rectangle ({W},{Hh});"]
    spots=[(0.7,0.6),(2.0,0.6),(3.0,1.0),(0.7,1.8),(1.9,1.9),(3.0,2.1),(1.3,1.2)]
    for k,it in enumerate(items[:len(spots)]):
        cx,cy=spots[k]
        if it[0]=='don':
            el.append(f"  \\shade[ball color={it[1]}] ({cx:.2f},{cy:.2f}) circle (0.26);")
        else:
            el.append(f"  \\draw[line width=1.6pt,gray!55!black] ({cx-0.28:.2f},{cy:.2f})--({cx+0.28:.2f},{cy:.2f});")
            el.append(f"  \\shade[ball color={it[1]}] ({cx-0.28:.2f},{cy:.2f}) circle (0.22);")
            el.append(f"  \\shade[ball color={it[2]}] ({cx+0.28:.2f},{cy:.2f}) circle (0.22);")
    if nhan: el.append(f"  \\node[above,font=\\bfseries] at ({W/2:.2f},{Hh+0.05}) {{{nhan}}};")
    body=(_PRE+r'''
\begin{tikzpicture}[line join=round]
@@E@@
\end{tikzpicture}\end{document}''').replace('@@E@@',"\n".join(el))
    return _HC.render_tikz_doc(body,out,tra_bytes)

# ── Bohr fragment (tái dùng cho sơ đồ liên kết ion) ──
def _bohr_frag(cx,cy,Z,cau_hinh,ten,s=0.62):
    if sum(cau_hinh)!=Z: raise ValueError(f"[PHANH hoa2] {ten}: sum{cau_hinh}≠Z={Z}")
    out=[]; r0,dr=0.5*s,0.42*s
    for i,ne in enumerate(cau_hinh):
        r=r0+i*dr
        out.append(f"  \\draw[black!70,very thin] ({cx:.3f},{cy:.3f}) circle ({r:.3f});")
        for k in range(ne):
            a=90+i*14+k*360.0/ne
            x=cx+r*math.cos(math.radians(a)); y=cy+r*math.sin(math.radians(a))
            out.append(f"  \\fill[blue!70!black] ({x:.3f},{y:.3f}) circle (0.05);")
    out.append(f"  \\fill[red!75!black] ({cx:.3f},{cy:.3f}) circle ({0.16*s:.3f});")
    out.append(f"  \\node[below,font=\\footnotesize\\bfseries] at ({cx:.3f},{cy-r0-len(cau_hinh)*dr-0.12:.3f}) {{{ten}\\,($+{Z}$)}};")
    return "\n".join(out)

# ═══════════ Hàm 4 — lien_ket_ion : sơ đồ hình thành liên kết ion ═══════════
def lien_ket_ion(cho_Z, cho_ch, cho_ten, nhan_Z, nhan_ch, nhan_ten, so_e,
                 ion_duong, ion_am, out='hoa2_ion', tra_bytes=False):
    """Sơ đồ: nguyên tử KIM LOẠI (cho) nhường so_e electron cho nguyên tử PHI KIM (nhan)
       → ion dương + ion âm. Vẽ 2 nguyên tử Bohr + mũi tên chuyển e + kết quả ion.
       vd NaCl: (11,[2,8,1],'Na',17,[2,8,7],'Cl',1,'Na^+','Cl^-')."""
    L=_bohr_frag(0,0,cho_Z,cho_ch,cho_ten)
    R=_bohr_frag(4.2,0,nhan_Z,nhan_ch,nhan_ten)
    arrow=(f"  \\draw[-{{Stealth[length=3mm]}},thick,red!70!black] (1.3,0.35) to[bend left=20] (2.9,0.35);\n"
           f"  \\node[font=\\scriptsize,red!70!black] at (2.1,1.05) {{cho {so_e}e}};")
    res=(f"  \\node[font=\\small\\bfseries] at (2.1,-2.1) {{${ion_duong}\\ \\ {ion_am}$}};")
    body=(_PRE+r'''
\begin{tikzpicture}[line join=round]
@@L@@
@@R@@
@@A@@
@@RES@@
\end{tikzpicture}\end{document}''').replace('@@L@@',L).replace('@@R@@',R).replace('@@A@@',arrow).replace('@@RES@@',res)
    return _HC.render_tikz_doc(body,out,tra_bytes)

# ═══════════ Hàm 5 — lien_ket_cht : sơ đồ liên kết cộng hoá trị ═══════════
# registry: (atoms[(sym,x,y)], bonds[(i,j,so_cap_dung_chung)], lone[(atom_idx, so_e_rieng)])
_CHT = {
 'H2': ([('H',-0.9,0),('H',0.9,0)], [(0,1,1)], []),
 'Cl2':([('Cl',-1.1,0),('Cl',1.1,0)], [(0,1,1)], [(0,6),(1,6)]),
 'N2': ([('N',-1.0,0),('N',1.0,0)], [(0,1,3)], [(0,2),(1,2)]),
 'O2': ([('O',-1.0,0),('O',1.0,0)], [(0,1,2)], [(0,4),(1,4)]),
 'HCl':([('H',-0.9,0),('Cl',0.9,0)], [(0,1,1)], [(1,6)]),
 'H2O':([('O',0,0.1),('H',-1.15,-0.55),('H',1.15,-0.55)], [(0,1,1),(0,2,1)], [(0,4)]),
}
def lien_ket_cht(cong_thuc, out='hoa2_cht', tra_bytes=False):
    """Sơ đồ liên kết cộng hoá trị (dùng chung cặp electron): H2,Cl2,N2,O2,HCl,H2O.
       Mỗi nguyên tử = vòng tròn có ký hiệu; cặp electron DÙNG CHUNG = 2 chấm giữa 2 nguyên tử
       (mỗi liên kết có so_cap cặp); electron riêng = chấm quanh nguyên tử. NGHĨA-THUẦN."""
    if cong_thuc not in _CHT:
        raise ValueError(f"[PHANH hoa2] chưa có sơ đồ CHT '{cong_thuc}' (có: {sorted(_CHT)}).")
    atoms,bonds,lone=_CHT[cong_thuc]; el=[]
    R=0.62
    for sym,x,y in atoms:
        el.append(f"  \\draw[thick,fill={_mau(sym)}!25] ({x:.3f},{y:.3f}) circle ({R:.3f});")
        el.append(f"  \\node[font=\\small\\bfseries] at ({x:.3f},{y:.3f}) {{{sym}}};")
    def dot(x,y,c='black'): return f"  \\fill[{c}] ({x:.3f},{y:.3f}) circle (0.055);"
    # cặp dùng chung: đặt trên đoạn nối, lệch nhau theo số cặp
    for i,j,ncap in bonds:
        _,x1,y1=atoms[i]; _,x2,y2=atoms[j]
        mx,my=(x1+x2)/2,(y1+y2)/2; dx,dy=x2-x1,y2-y1; Ln=math.hypot(dx,dy); ux,uy=-dy/Ln,dx/Ln
        # ncap cặp, mỗi cặp = 2 chấm sát nhau dọc trục nối
        for ci in range(ncap):
            off=(ci-(ncap-1)/2)*0.24
            bx,by=mx+ux*off,my+uy*off
            tx,ty=dx/Ln*0.07,dy/Ln*0.07
            el.append(dot(bx-tx,by-ty,'red!75!black')); el.append(dot(bx+tx,by+ty,'red!75!black'))
    # electron riêng: rải trên cung ngoài phía "xa" của mỗi nguyên tử
    for idx,ne in lone:
        sym,x,y=atoms[idx]
        # hướng xa tâm phân tử
        cxm=sum(a[1] for a in atoms)/len(atoms); cym=sum(a[2] for a in atoms)/len(atoms)
        base=math.degrees(math.atan2(y-cym,x-cxm)) if (x!=cxm or y!=cym) else 0
        for k in range(ne):
            a=base-60+k*(120.0/max(ne-1,1))
            ex=x+(R+0.14)*math.cos(math.radians(a)); ey=y+(R+0.14)*math.sin(math.radians(a))
            el.append(dot(ex,ey,'blue!70!black'))
    body=(_PRE+r'''
\begin{tikzpicture}[line join=round]
@@E@@
\end{tikzpicture}\end{document}''').replace('@@E@@',"\n".join(el))
    return _HC.render_tikz_doc(body,out,tra_bytes)

# ═══════════ CLASS ENTRY cho sinh_bantrich ═══════════
class Hinh:
    """Entry bản trích — thư viện hình Chương II Hóa 7 (hàm-độc-lập)."""
    phan_tu       = staticmethod(phan_tu)
    mo_hinh_hat   = staticmethod(mo_hinh_hat)
    hop_hat       = staticmethod(hop_hat)
    lien_ket_ion  = staticmethod(lien_ket_ion)
    lien_ket_cht  = staticmethod(lien_ket_cht)
