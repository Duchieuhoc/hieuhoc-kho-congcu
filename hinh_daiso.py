#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_daiso.py — ENTRY MẠCH ĐẠI SỐ — DS THCS lớp 6→9
#   [B1, 30a] Primitive toạ độ (tia số/trục số/mặt phẳng toạ độ) ĐÃ TÁCH sang
#   hinh_toado.py (dùng chung). Module này KẾ THỪA lại + giữ phần THUẦN đại số
#   (dựng căn hai, diện tích đại số). Backward-compatible: Hinh() vẫn đủ mọi method cũ.
#   Lịch sử: [28p] +tia_so · [29c] +hinhDienTichDaiSo · [29y] +hinhMatPhangToaDo.
#   Triết lý Đ5.9 giữ nguyên. CS2627.
# ═══════════════════════════════════════════════════════════════════
import hinh_toado
import hinh_core as _HC   # helper render_tikz_doc (generator độc lập)


class Hinh(hinh_toado.Hinh):
    """Entry Đại số — kế thừa primitive toạ độ (hinh_toado.Hinh) + phần thuần đại số."""

    def dung_can_hai(self, canh=2, nhan_diem='A', nhan_can=None):
        """DỰNG √2 (hoặc √(canh²/2)) TRÊN TRỤC SỐ bằng compa — SGK Toán 7 Hình 2.3.

        Compose ngữ nghĩa: máy tự dựng hình vuông cạnh `canh` + hai đường chéo cắt tại tâm E,
        rồi trục Ox (gốc O), đường tròn tâm O bán kính OE, cắt tia Ox tại điểm A = nửa đường chéo
        = canh·√2/2. Với canh=2 → A = √2 (đúng SGK).

        AI Soạn CHỈ khai giá trị `canh` — KHÔNG đụng toạ độ/bán kính thô (Đ5.9).

        canh       : cạnh hình vuông dựng (mặc định 2 → ra √2).
        nhan_diem  : nhãn điểm giao trên trục (mặc định 'A').
        nhan_can   : nhãn giá trị dưới điểm A (vd '√2'); None → không ghi (đúng SGK, để HS nhận).
        """
        import math as _m
        self._nen_luoi = False
        c = float(canh)
        nua_cheo = c * _m.sqrt(2) / 2         # OE = A trên trục
        # ── Hình vuông MNPQ cạnh c, đặt phía trên-trái, tách khỏi trục ──
        oy = 1.9                               # nâng hình vuông cao hơn (tách khỏi đường tròn)
        ox = -c - 1.4                          # đặt lệch trái gốc O nhiều hơn
        M=(ox, oy+c); N=(ox+c, oy+c); P=(ox+c, oy); Q=(ox, oy)
        for tn,(px,py) in [('M',M),('N',N),('P',P),('Q',Q)]:
            self._diem(tn, px, py, nhan='above' if py>oy else 'below', moc=True)
        for a,b in [('M','N'),('N','P'),('P','Q'),('Q','M')]:
            self.tikz.append(('doan', a, b, None, 'lien', None))
        # hai đường chéo + tâm E
        self.tikz.append(('doan','M','P',None,'lien',None))
        self.tikz.append(('doan','N','Q',None,'lien',None))
        ex,ey = (ox+c/2, oy+c/2)
        self._diem('E', ex, ey, nhan='above right', moc=True)
        self.ghi_chu((M[0]+N[0])/2, M[1]+0.12, self._so(int(c)) if c==int(c) else str(c))
        # ── Trục Ox: gốc O tại (0,0), mũi tên 2 đầu ──
        SC = 1.0
        xO = 0.0
        self._diem('O', xO, 0.0, nhan=None, moc=True)
        xR = nua_cheo*SC + 1.2
        self._diem('_ox_L', -0.6, 0.0, nhan=None, moc=False)
        self._diem('_ox_R', xR, 0.0, nhan=None, moc=False)
        self.tikz.append(('truc2dau','_ox_L','_ox_R'))
        self.ghi_chu(xO, -0.44, '0')
        self.ghi_chu(xR-0.05, 0.22, 'x')
        # ── Đường tròn tâm O bán kính OE (=nua_cheo) → điểm A trên tia Ox ──
        self.tikz.append(('tron','O', nua_cheo*SC, None, 'dut'))
        xA = nua_cheo*SC
        self._diem(nhan_diem, xA, 0.0, nhan='above', moc=True)
        if nhan_can:
            self.ghi_chu(xA, -0.34, str(nhan_can))
        return self


def hinhDienTichDaiSo(kieu='catghep', nhan=None, chuThich=None,
                      out='dientich_daiso', tra_bytes=False):
    """HÌNH DIỆN TÍCH đại số (nhãn BIẾN, giấu toạ độ). 3 biến thể:
       • 'catghep' : vuông a khoét ô b² → hình L, mũi tên cong → chữ nhật (a+b)(a-b).
                     nhan = {a, b, a_tru_b, a_cong_b}
       • 'chia4'   : vuông (a+b) chia 4 phần P/Q/R/S, đỉnh ABCD. nhan = {a, b, a_cong_b, P,Q,R,S,A,B,C,D}
       • 'vien'    : vuông ngoài x, vuông trong đồng tâm, vành tô, 4 mũi tên bề rộng y.
                     nhan = {ngoai, vien}
       chuThich : caption "Hình N" căn giữa dưới (tuỳ chọn).
    """
    nhan = nhan or {}
    cap = ''
    if chuThich:
        cap = (r'\node[below,font=\itshape] at (CAPX,CAPY) {CAPT};'
               .replace('CAPT', chuThich))

    if kieu == 'catghep':
        a   = _HC._m(nhan.get('a'), 'a')
        b   = _HC._m(nhan.get('b'), 'b')
        amb = _HC._m(nhan.get('a_tru_b'), 'a-b')
        apb = _HC._m(nhan.get('a_cong_b'), 'a+b')
        # a=4, b=1.5 (toạ độ VẼ cố định — giấu trong kho, không lộ ra script AI Soạn)
        cap = cap.replace('CAPX', '5.3').replace('CAPY', '-0.9')
        body = r'''\documentclass[tikz,border=8pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[line join=round, every node/.style={font=\normalsize},
  cA/.style={fill=blue!16}, cB/.style={fill=orange!28}, edge/.style={very thick, black}]
% ---- Hình a: vuông a khoét ô b² góc TRÊN-TRÁI ----
\begin{scope}[shift={(0,0)}]
  \fill[cA] (0,0) rectangle (4,2.5);
  \fill[cA] (1.5,2.5) rectangle (4,4);
  \fill[cB] (0,2.5) rectangle (1.5,4);
  \draw[dashed, thick, black!55] (0,2.5) rectangle (1.5,4);
  \node[black!55] at (0.75,3.25) {$@@B@@$};
  \draw[edge] (0,0) rectangle (4,4);
  \draw[edge] (0,2.5) -- (4,2.5);
  \draw[edge] (1.5,2.5) -- (1.5,4);
  \node[left]  at (0,2)    {$@@A@@$};
  \node[below] at (2,0)    {$@@A@@$};
  \node[above] at (0.75,4) {$@@B@@$};
  \node[above] at (2.75,4) {$@@AMB@@$};
  \node[right] at (4,1.25) {$@@AMB@@$};
\end{scope}
% ---- mũi tên cong ----
\draw[-{Stealth[length=4mm]}, very thick, black!70] (4.55,2.6) to[bend left=28] (6.35,1.9);
% ---- Hình b: chữ nhật (a+b)×(a-b) ----
\begin{scope}[shift={(7,0.75)}]
  \fill[cA] (0,0) rectangle (5.5,2.5);
  \draw[edge] (0,0) rectangle (5.5,2.5);
  \draw[edge] (4,0) -- (4,2.5);
  \node[below] at (2,0)     {$@@A@@$};
  \node[below] at (4.75,0)  {$@@B@@$};
  \node[right] at (5.5,1.25){$@@AMB@@$};
  \node[above] at (2.75,2.5){$@@APB@@$};
\end{scope}
@@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@AMB@@', amb).replace('@@APB@@', apb)
                    .replace('@@A@@', a).replace('@@B@@', b).replace('@@CAP@@', cap))

    elif kieu == 'vien':
        ngoai = _HC._m(nhan.get('ngoai'), 'x')
        vien  = _HC._m(nhan.get('vien'), 'y')
        cap = cap.replace('CAPX', r'\O/2').replace('CAPY', '-0.9')
        body = r'''\documentclass[border=4pt]{standalone}
\usepackage{tikz}\usepackage{amsmath}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.4mm]},line width=0.5pt,font=\normalsize]
  \def\O{8}\def\w{1.5}
  \fill[green!22, even odd rule] (0,0) rectangle (\O,\O) (\w,\w) rectangle (\O-\w,\O-\w);
  \draw[line width=0.8pt] (0,0) rectangle (\O,\O);
  \draw[line width=0.8pt] (\w,\w) rectangle (\O-\w,\O-\w);
  \draw[<->] (0,\O+0.7) -- (\O,\O+0.7);
  \node[above] at (\O/2,\O+0.7) {$@@NGOAI@@$};
  \draw[<->] (\O/2,\O-\w) -- (\O/2,\O); \node[right] at (\O/2,\O-\w/2) {$@@VIEN@@$};
  \draw[<->] (\O/2,0) -- (\O/2,\w);     \node[right] at (\O/2,\w/2) {$@@VIEN@@$};
  \draw[<->] (0,\O/2) -- (\w,\O/2);     \node[above] at (\w/2,\O/2) {$@@VIEN@@$};
  \draw[<->] (\O-\w,\O/2) -- (\O,\O/2); \node[above] at (\O-\w/2,\O/2) {$@@VIEN@@$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@NGOAI@@', ngoai).replace('@@VIEN@@', vien)
                    .replace('@@CAP@@', cap))

    elif kieu == 'chia4':
        a   = _HC._m(nhan.get('a'), 'a')
        b   = _HC._m(nhan.get('b'), 'b')
        apb = _HC._m(nhan.get('a_cong_b'), 'a+b')
        A = _HC._m(nhan.get('A'), 'A'); B = _HC._m(nhan.get('B'), 'B')
        Cc = _HC._m(nhan.get('C'), 'C'); D = _HC._m(nhan.get('D'), 'D')
        P = _HC._m(nhan.get('P'), 'P'); Q = _HC._m(nhan.get('Q'), 'Q')
        Rr = _HC._m(nhan.get('R'), 'R'); S = _HC._m(nhan.get('S'), 'S')
        # a=3.2, b=1.8 (a+b=5). Đỉnh: A trên-trái, B trên-phải, C dưới-phải, D dưới-trái.
        cap = cap.replace('CAPX', '2.5').replace('CAPY', '-1.35')
        body = r'''\documentclass[border=6pt]{standalone}
\usepackage{tikz}\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>={Stealth[length=2.6mm]}, every node/.style={font=\normalsize},
  cM/.style={fill=green!20}, edge/.style={very thick, black}]
  \def\a{3.2}\def\b{1.8}\def\s{5}   % s=a+b
  % tô Q (trên-phải) và R (dưới-trái)
  \fill[cM] (\a,\b) rectangle (\s,\s);   % Q: trên-phải  (x>a, y>b)
  \fill[cM] (0,0)  rectangle (\a,\b);    % R: dưới-trái  (x<a, y<b)
  % viền + 2 đường chia
  \draw[edge] (0,0) rectangle (\s,\s);
  \draw[edge] (\a,0) -- (\a,\s);         % đường dọc tại x=a
  \draw[edge] (0,\b) -- (\s,\b);         % đường ngang tại y=b
  % nhãn 4 vùng (P trên-trái, Q trên-phải, R dưới-trái, S dưới-phải)
  \node at ({\a/2},{(\b+\s)/2})      {$@@P@@$};
  \node at ({(\a+\s)/2},{(\b+\s)/2}){$@@Q@@$};
  \node at ({\a/2},{\b/2})            {$@@R@@$};
  \node at ({(\a+\s)/2},{\b/2})      {$@@S@@$};
  % nhãn đỉnh ABCD (ngoài góc)
  \node[above left]  at (0,\s)  {$@@AA@@$};
  \node[above right] at (\s,\s) {$@@BB@@$};
  \node[below right] at (\s,0)  {$@@CC@@$};
  \node[below left]  at (0,0)   {$@@DD@@$};
  % nhãn cạnh trên (a | b) + cạnh trái (a | b)
  \node[above] at ({\a/2},\s)       {$@@a@@$};
  \node[above] at ({(\a+\s)/2},\s) {$@@b@@$};
  \node[left]  at (0,{(\b+\s)/2})  {$@@a@@$};
  \node[left]  at (0,{\b/2})        {$@@b@@$};
  % a+b: mũi tên 2 đầu ngoài cạnh trên & cạnh trái
  \draw[<->] (0,\s+0.7) -- (\s,\s+0.7); \node[above] at ({\s/2},\s+0.7) {$@@APB@@$};
  \draw[<->] (-1.05,0) -- (-1.05,\s);   \node[left] at (-1.05,{\s/2}) [rotate=90,anchor=south] {$@@APB@@$};
  @@CAP@@
\end{tikzpicture}
\end{document}'''
        body = (body.replace('@@APB@@', apb)
                    .replace('@@AA@@', A).replace('@@BB@@', B).replace('@@CC@@', Cc).replace('@@DD@@', D)
                    .replace('@@P@@', P).replace('@@Q@@', Q).replace('@@R@@', Rr).replace('@@S@@', S)
                    .replace('@@a@@', a).replace('@@b@@', b).replace('@@CAP@@', cap))
    else:
        raise ValueError(f"[hinhDienTichDaiSo] kieu='{kieu}' không hợp lệ (catghep|chia4|vien)")

    return _HC.render_tikz_doc(body, out, tra_bytes)

Hinh.hinhDienTichDaiSo = staticmethod(hinhDienTichDaiSo)
