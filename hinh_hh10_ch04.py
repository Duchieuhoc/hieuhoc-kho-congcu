#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════
# hinh_hh10_ch04.py — ENTRY chương: Hình học 10 Chương IV (Vectơ)
#   Bộ KNTT · HH10_CH04 · Ông Bụt Hình 2026-10-04.
#   COMPOSE: HinhDaGiac (hình vuông/thoi/thang-cân/lục giác/tam giác + coban)
#            + HinhToaDo (trục số, mặt phẳng Oxy — hinhMatPhangToaDo)
#            + VECTƠ (mũi tên A→B — HinhCoBan.vecto, mới vá 2026-10-04).
#   `import hinh_hh10_ch04 as H; h = H.Hinh()` cho AI Soạn (mạch khai nghĩa),
#    HOẶC H.Hinh.hinhMatPhangToaDo(... vecto=[...]) cho hình trên hệ trục (static).
#   MRO: Hinh → HinhDaGiac → HinhToaDo(=hinh_toado.Hinh) → HinhCoBan.
#
#   PRIMITIVE VECTƠ (vá [CH04], additive, 0 regression):
#     • h.vecto(A, B, nhan='\\vec a'|'\\overrightarrow{AB}', mau, net, vi_tri_nhan, rong)
#       — vectơ trên nền đa giác/lưới (đỉnh đã đặt). Mũi tên ĐÚNG A→B (khác tia/doan).
#     • hinhMatPhangToaDo(..., vecto=[{tu,den,nhan,mau,net,viTriNhan}])
#       — vectơ trong hệ trục Oxy (B10/B11 tọa độ).
#   Hình vuông/thoi/thang/lục giác/tam giác + trục/hệ trục: DÙNG HÀM KHO SẴN CÓ,
#   chỉ phủ thêm mũi tên vectơ lên trên.
# ═══════════════════════════════════════════════════════════════════
import hinh_dagiac
import hinh_toado

# ── METADATA PHÂN TẦNG cho bản trích (mô hình X) ──
LOP_MODULE = [10]
CUA_RENDER = {'ve'}
# Hàm prefix '_' = HẠ TẦNG (ẩn khỏi bản phát — Đ5.9). Còn lại = KHAI NGHĨA.


class Hinh(hinh_dagiac.HinhDaGiac, hinh_toado.Hinh):
    """Kho Chương IV (Hình 10, Vectơ) = đa giác (hình vuông/thoi/thang-cân/lục giác/
    tam giác) + toạ độ (trục số, mặt phẳng Oxy) + VECTƠ (mũi tên A→B, kế thừa
    HinhCoBan.vecto). Chỉ compose — primitive vectơ nằm ở HinhCoBan (dùng chung)."""
    
    # ═══ [CH04 · vá 32f] 2 BUILDER HÌNH VẬT-LÍ VECTƠ (OB cấp — hình cố định SGK) ═══
    #   Vectơ KHÔNG neo đỉnh đa giác → AI Soạn CẤM tự tính toạ độ (Đ5.9).
    #   OB cấp builder: khai THAM SỐ NGỮ NGHĨA (góc, nhãn), máy đặt mọi điểm + vẽ.
    #   AI Soạn chỉ gọi 1 hàm/hình rồi h.ve(...). Additive, 0 regression.

    def ban_song(self, alpha=35, L_rieng=2.2, L_nuoc=1.6, cao=3.0,
                 nhan_r=r'\vec{v}_r', nhan_n=r'\vec{v}_n', nhan_v=r'\vec{v}'):
        """H4.17 — thuyền sang sông: hai bờ SONG SONG (d_1 dưới, d_2 trên) + tổng hợp
        vận tốc. v_r = AM (vận tốc riêng, hợp góc alpha° với bờ), v_n = MN (dòng nước,
        // bờ), v = AN (tổng). B = AN∩d_2, C = AM∩d_2 (nét đứt kéo dài).
        Máy đặt A,M,N,B,C + d_1,d_2 + cung góc alpha tại A. AI Soạn chỉ truyền alpha + nhãn."""
        import math as _m
        a = _m.radians(alpha)
        self._diem('A', 0.0, 0.0, 'below left')
        Mx, My = L_rieng*_m.cos(a), L_rieng*_m.sin(a)
        self._diem('M', Mx, My, 'above left', moc=False)
        Nx, Ny = Mx + L_nuoc, My
        self._diem('N', Nx, Ny, 'above right', moc=False)
        # B = A + t*(N-A) với y = cao ; C = A + s*(M-A) với y = cao
        tB = cao / Ny; Bx = Nx*tB
        self._diem('B', Bx, cao, 'above', moc=False)
        sC = cao / My; Cx = Mx*sC
        self._diem('C', Cx, cao, 'above', moc=False)
        # hai bờ (đường ngang) — mốc ẩn để kéo dài 2 đầu
        xl = min(-0.6, Cx-0.6); xr = max(Nx+0.8, Bx+0.8)
        self._diem('_d1l', xl, 0.0, moc=False); self._diem('_d1r', xr, 0.0, moc=False)
        self._diem('_d2l', xl, cao, moc=False); self._diem('_d2r', xr, cao, moc=False)
        self._duong_thang('_d1l', '_d1r'); self._duong_thang('_d2l', '_d2r')
        self.tikz.append(('nhan_mut', '_d1r', 'd_1')); self.tikz.append(('nhan_mut', '_d2r', 'd_2'))
        # nét đứt kéo dài AN→B và AM→C
        self.doan('N', 'B', net='dut'); self.doan('M', 'C', net='dut')
        # vectơ
        self.vecto('A', 'M', nhan=nhan_r, vi_tri_nhan='above left')
        self.vecto('M', 'N', nhan=nhan_n, vi_tri_nhan='above')
        self.vecto('A', 'N', nhan=nhan_v, vi_tri_nhan='below right', mau='blue')
        # cung góc alpha tại A (giữa bờ d1 ngang và AM)
        self.so_do_goc(('_d1r', 'A', 'M'), do=alpha)
        return self

    def mat_nghieng_luc(self, goc=30, day=6.0, ti_le_C=0.58,
                        L_P=1.9, L_w=1.25, L_F=1.6,
                        nhan_P=r'\vec{P}', nhan_w=r'\vec{w}', nhan_F=r'\vec{F}'):
        """H4.18 — kéo vật lên mặt dốc nghiêng góc 'goc'° so phương ngang. Tam giác vuông
        O(chân dốc) — Q(chân phải, góc vuông) — T(đỉnh); mặt dốc = OT. C = điểm đặt vật
        trên OT. Ba lực đồng quy tại C: P (thẳng đứng xuống), w (⊥ mặt dốc, hướng lên),
        F (dọc mặt dốc, hướng lên đỉnh). Máy đặt O,Q,T,C + cung góc tại O + ô vuông tại Q."""
        import math as _m
        a = _m.radians(goc)
        self._diem('O', 0.0, 0.0, 'below left')
        self._diem('Q', day, 0.0, 'below right', moc=False)
        Ty = day*_m.tan(a)
        self._diem('T', day, Ty, 'above right', moc=False)
        Cx, Cy = ti_le_C*day, ti_le_C*Ty
        self._diem('C', Cx, Cy, 'above left')
        # tam giác dốc (đáy ngang, cạnh đứng, mặt dốc dày hơn)
        self.doan('O', 'Q'); self.doan('Q', 'T'); self.doan('O', 'T', rong='dam')
        # đơn vị hướng
        ux, uy = _m.cos(a), _m.sin(a)          # dọc mặt dốc (lên đỉnh)
        nx, ny = -_m.sin(a), _m.cos(a)         # pháp tuyến mặt dốc (hướng lên-trái)
        self._diem('_P', Cx, Cy - L_P, moc=False)
        self._diem('_w', Cx + L_w*nx, Cy + L_w*ny, moc=False)
        self._diem('_F', Cx + L_F*ux, Cy + L_F*uy, moc=False)
        self.vecto('C', '_P', nhan=nhan_P, vi_tri_nhan='right')
        self.vecto('C', '_w', nhan=nhan_w, vi_tri_nhan='above left')
        self.vecto('C', '_F', nhan=nhan_F, vi_tri_nhan='above', mau='blue')
        # góc dốc tại O + ô vuông tại Q
        self.so_do_goc(('Q', 'O', 'T'), do=goc)
        self.goc_vuong(('O', 'Q', 'T'))
        return self
