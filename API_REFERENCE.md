# API_REFERENCE.md — Tham chiếu nhanh `hieuhoc_template.js` (v10.15)
> **Tự sinh** bởi `sinh_apiref.js` từ template v10.15 (2026-09-05) — KHÔNG sửa tay (sửa sẽ mất khi regen). Cập nhật: chạy lại `node sinh_apiref.js hieuhoc_template.js > API_REFERENCE.md`.
> Bản rút gọn thay template đầy đủ trong Project (tiết kiệm token). AI Soạn GỌI HÀM theo chữ ký dưới; không tự viết OOXML.

### `kiemMay(bufOrPath, opts = {})`
[v9.7] CỬA KIỂM MÁY CHUNG — kiemMay(bufOrPath, opts) Code hóa checklist máy (HP Điều 61). AI Soạn (qua xuatFile) và AI QC (gọi trực tiếp trên file nhận) dùng CHUNG một cửa. Bắt cả failure IM LẶNG.
### `viDuLyThuyet({ hinhBenPhai, hinhBenTrai, cacCau, deBai, nhan, dapAn, thamChieu, coHinh })`

## patch docPr id — gọi sau Packer.toBuffer()
### `patchDocPrIds(docBuffer)`
### `taoTaiLieu({ soBai, tenBai, lop, children })`
[v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer). AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang. KHÔNG để AI tự viết new Document / tự set lề / tự gắn header — mỗi lần tự làm là một lần quên hoặc set sai (lề lệch, thiếu footer, khổ giấy sai). const doc = H.taoTaiLieu({ soBai: 8, tenBai: "...", lop: "Lớp 7", children }); await H.xuatFile(doc, "/mnt/user-data/outputs/HH7_CH03_B08.docx");
### `taoTaiLieuDeKT({ tenDe, children, headerFooter = true })`
taoTaiLieuDeKT — dựng Document cho ĐỀ KIỂM TRA (thay khối Document tự dựng trong build script mỗi đề). Header/footer đề KT tự gắn (ĐÚNG MẪU headerFooterBaiHoc). Dùng: const doc = H.taoTaiLieuDeKT({ tenDe: 'Đề kiểm tra ... (Đề A)', children: C }); · tenDe — hiện ở header chạy mỗi trang (dạng thường, nhận diện đề/tránh lẫn A/B). · headerFooter=false — tắt header/footer trang (nếu muốn tờ trắng). Khối "ĐỀ KIỂM TRA…/họ tên/điểm" đầu trang vẫn do headerDeKiemTra() đẩy vào children.

## helpers cơ sở
### `run(text, opts = {})`
### `para(children, opts = {})`
A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng) keepNext: giữ đoạn này cùng trang với đoạn kế tiếp (tiêu đề không bị mồ côi)
### `tabLine(parts, opts = {})`
A2 v9.0: tab stop thật chia đều 18.4cm (TOTAL_W tính theo twip = 10432 ≈ 18.4cm) Thay khoảng trắng giả bằng \t + tabStops chuẩn — căn đều bất kể font/zoom
### `toInline(input, opts = {})`
### `paraInline(input, opts = {})`
Dựng nhanh 1 Paragraph từ nội dung string|mảng trộn — dùng nội bộ
### `approxLen(item)`
Ước lượng độ dài hiển thị — dùng để quyết định xếp cột/xuống hàng (công thức Math không có .length nên tính tượng trưng 3 ký tự)

## phần 1 — bài học
### `tenBaiHoc({ soBai, tenBai, tiet, sgkTr, sbtTr, ma })`
### `mucTieu({ kienThuc, kyNang, nangLuc })`
### `tieuDeMuc(stt, ten)`
3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm)
### `tieuDeMucChinh(stt, ten)`
### `lyThuyet(text)`
4. LÝ THUYẾT — 1 dòng nội dung thường
### `viDu({ nhan = "Ví dụ", deBai, cacCau, dapAn, thamChieu, coHinh, hinhBenTrai, hinhBenPhai })`
### `layoutCauHoi(cauArr, opts = {})`
### `loiGiai(noiDung)`
### `saiLamThuongGap(loiArr, opts = {})`
### `ghiNhoNhanh(dongArr, opts = {})`

## phần 2 — dạng toán, BT, BTVN, đề kiểm tra
### `tieuDeDang({ soDang, tenDang, ma })`
### `nhanDang(yArr)`
### `phuongPhapGiai(buocArr, opts = {})`
### `phanTich(noiDung)`
[v9.6] Phân tích — mục A.1 giữa "Bài toán mẫu" và "Lời giải"; gánh luôn việc nhận dạng. Nhận string hoặc mảng trộn (chèn phanSo/luyThua). Trả mảng — dùng spread.
### `dangToanDayDu({ saiLamArr, soDang, ghiNhoArr, tenDang, ma, viDuDeBai, viDuCacCau, viDuThamChieu, viDuCoHinh, viDuHinhBenPhai, viDuHinhBenTrai, phanTich, phuongPhapArr, soBai, mucDo, deBai, cacCau, thamChieu, loiGiaiND })`
Gộp toàn bộ 1 Dạng toán thành 1 lệnh gọi duy nhất — khuyến khích AI Soạn dùng hàm này
### `baiTapTaiLop({ soBai, mucDo, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai })`
### `cauTracNghiem({ soCau, cauHoi, dapAn, thamChieu })`
### `bangDapAnPhanI(dapAnArr)`
13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT) [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..." (thay dạng bảng 2 hàng cũ — gọn hơn, đúng yêu cầu 25/07). Nhận mảng đáp án ['B','A','C',...]. Trả 1 Paragraph.
### `bangDungSai(menhDeArr)`
14. BẢNG ĐÚNG/SAI — tỉ lệ CỐ ĐỊNH 80%-10%-10%, nền trắng chữ đen
### `bangSoLieu(duLieu, opts = {})`
[28r] 14b. BẢNG SỐ LIỆU TỔNG QUÁT — dữ liệu thực tiễn nhiều cột (dân số, tuổi thọ, hồ, hành tinh, khí hiếm, pizza…) — DS7 dày bảng. GỐC: kho chỉ có bảng CHUYÊN DỤNG (đáp án/đúng-sai/nhật ký); bảng số liệu thực tiễn chưa có hàm → AI Soạn buộc viết new Table() thô (phạm nguyên tắc). Ô nhận string|number|OMML|mảng trộn qua toInline → nhúng thẳng luỹ thừa/phân số OMML trong ô (số khoa học a·10ⁿ, ma phương 2ᵏ). QC ô bảng PHẢI bằng lxml (python-docx cũ nuốt paragraph chứa OMML). Viền mảnh xám #999999, nền TRẮNG (HP Đ17.2). Hàng tiêu đề đậm. duLieu: { tieuDe?: [ô…], hang: [[ô…],…] } HOẶC [[ô…],…] (không tiêu đề). opts.rongCot: mảng tỉ lệ cột (vd [0.4,0.3,0.3]); thiếu → chia đều. opts.canLe: mảng 'trai'|'giua'|'phai' theo cột; thiếu → cột 0 trái, còn lại giữa. Ví dụ: bangSoLieu({ tieuDe:["Hành tinh","Khoảng cách (km)"], hang:[ ["Trái Đất", ["1,50 · ", luyThua(10,8)] ], ["Sao Mộc", ["7,78 · ", luyThua(10,8)] ] ] })
### `danDungSai(soCau, moTa)`
[28m] DÒNG DẪN Đúng/Sai — nhãn "Câu N." TỰ ĐẬM (khớp nhãn câu template tự sinh ở cauTracNghiem/traLoiNgan/tự luận). GỐC: dòng dẫn Đ/S trước đây dựng TAY bằng para thường → quên đậm (mục ⑥ HH7-CH04). Nay bắt buộc qua hàm này: không thể quên đậm. moTa = phần mô tả (thường), nhận cả chuỗi lẫn OMML. Đặt NGAY TRƯỚC bangDungSai (chèn hinhVe căn giữa vào giữa nếu câu có hình).
### `traLoiNgan({ soCau, cauHoi, dapAn, thamChieu })`
### `headerDeKiemTra({ tenDe, phut })`
16. HEADER ĐỀ KIỂM TRA (tên đề + thời gian + bảng Họ tên/Điểm/NX)

## phần 3 — header/footer file bài học + đề kiểm tra
### `headerFooterBaiHoc({ soBai, tenBai, lop })`
### `headerFooterDeKT({ tenDe })`
header/footer trang Word cho ĐỀ KIỂM TRA — ĐÚNG MẪU headerFooterBaiHoc, KHÔNG làm khác. Chỉ thay định danh: "Bài n. Tên | Lớp" → tên đề (dạng thường, truyền sẵn). Footer y hệt mẫu: © Hiếu Học - TL nội bộ + slogan + số trang (PageNumber.CURRENT — tự chạy theo vị trí khi gộp file).

## phần 4 — tờ phân chương (AI QC dùng)
### `toPhanChuong({ logoBuffer, lop, tenChuong, danhSachBai, coTongKet = false, co45 = true, co90 = true })`
### `footerTPC()`
Footer riêng cho tờ phân chương (khác footer file bài học — không số trang)
### `headerRong()`
Header rỗng — dùng để NGẮT KẾ THỪA header khi tạo section riêng cho Trang cuối chương (OOXML mặc định section sau kế thừa header/footer section trước nếu không khai báo lại)

## phần 5 — tự luận BTVN + tiêu đề các khối
### `tuLuanBTVN({ soBai, mucDo, diem, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai })`
### `tieuDeTuLuan(soBai, tongDiem)`
Tiêu đề khối "D. TỰ LUẬN (n bài = Xđ)"
### `tieuDePhanI(soCau, tongDiem)`
Tiêu đề khối "A. PHẦN I - CHỌN ĐÁP ÁN (...)"
### `tieuDePhanII(soCau, soMenhDe, tongDiem)`
### `tieuDePhanIII(soCau, tongDiem)`

## phần 6 — trang cuối chương
### `ghiChuGiangDay({ dsLopBai } = {})`
### `nhatKyCaiTien({ dsPhienBan } = {})`
### `bangNguonGoc({ soChuong, dsNguon })`
### `trangCuoiChuong({ dsLopBai, dsPhienBan })`

## phần 7 — công thức toán thật (OMML), hình vẽ, tiêu đề phần đề kiểm tra
### `luyThua(coSo, soMu)`
### `luyThuaUnicode(coSo, soMu)`
### `phanSo(tuSo, mauSo)`
### `ngoac(bieuThuc)`
### `canBac(soHang, bacCan = 2)`
### `chiSoDuoi(coSo, chiSo)`
### `triTuyetDoi(bieuThuc)`
### `kyHieuGoc(tenGoc)`
21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam
### `hinhVe({ imageBuffer, rongCm = 8, tiLeGoc, chuThich })`
### `hangHinh(items, { caoCm = 3.2, _tuLuoi = false } = {})`
22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4] HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa. `hangHinh`: 1 hàng ≤3 hình, KHÔNG viền, ô căn dọc giữa, CHUẨN HOÁ cùng chiều cao (caoCm). `luoiHinh`: tự chia hàng theo số lượng đã chốt — 1–3→1 hàng · 4→2+2 · 5→3+2 · 6→3+3. Chỉ dùng cho hình nhỏ + bộ liên quan; hình đơn/lớn/Phần II → vẫn hinhVe (dòng riêng).
### `luoiHinh(items, opts = {})`
### `hinhVeTextBox({ imageBuffer, rongCm = 6, tiLeGoc, chuThich })`
### `paraCoHinhPhai(anhFloating, noiDungInline, opts = {})`
### `hePhuongTrinh(danhSachPT)`
### `paraHePhuongTrinh(danhSachPT, opts = {})`
### `tieuDePhanI_DeKT(soCau, tongDiem)`
23. TIÊU ĐỀ CÁC PHẦN ĐỀ KIỂM TRA (I/II/III/IV — khác BTVN dùng A/B/C/D)
### `tieuDePhanII_DeKT(soCau, soMenhDe, tongDiem)`
### `tieuDePhanIII_DeKT(soCau, tongDiem)`
### `tieuDePhanIV_DeKT(soBai, tongDiem)`

## phần 8 — thư viện pictogram an toàn chuẩn hóa (Bài 2, Bài 50)
### `hinhIcon(tenIcon, opts = {})`
### `hinhIconHang(danhSachTen, opts = {})`

## Hằng số & tham chiếu (chỉ đọc)
`TNR` · `C_BLACK` · `C_RED` · `C_RED_ANSWER` · `C_GRAY` · `C_WHITE` · `SZ_CONTENT` · `SZ_TITLE_BAI` · `SZ_SMALL` · `SZ_MISTAKE` · `TOTAL_W` · `THO_RONG` · `THO_VUA` · `THO_HEP` · `PAGE_SIZE` · `PAGE_MARGIN` · `xuatFile` · `ICON_LIBRARY`

---
*Tự sinh: 69 hàm + 18 hằng/tham chiếu · template v10.15 (2026-09-05) · sinh_apiref.js.*
[sinh_apiref] 69 hàm, 18 hằng — template v10.15
