// HIEUHOC_TEMPLATE — CHÍNH THỨC | VERSION: v10.11 (2026-08-13) | GUARD "Ví dụ rỗng": viDuLyThuyet chỉ có hình (không đề & không câu hỏi) → CHẶN, buộc chèn HÌNH MINH HOẠ thẳng qua hinhVe (bỏ nhãn "Ví dụ:" thừa cho hình 8.X đi kèm định nghĩa). | v10.10 (2026-08-13) | LAYOUT CÂU HỎI a,b,c ĐỒNG BỘ ②④⑤: (1) layoutCauHoi dồn 1 dòng CHỈ KHI vừa cột, không thì mỗi câu xuống hàng; (2) bài CÓ hình bên phải (viDu mục③ / baiTapTaiLop / tuLuanBTVN) → ÉP xuống hàng (cột hẹp, không dồn ngang); (3) viDu/viDuLyThuyet nhận `dapAn` → in "Trả lời:" cho bản đầy đủ. | v10.9: sửa THẬT regex nhãn nhân đôi (split \t). | v10.7: hình tự đọc tỉ lệ PNG. | v10.6: cửa trùng-byte hình TỰ BỎ. | v10.3: +GUARD KHUNG A.1.
// File DUY NHẤT. Scripts require("./hieuhoc_template.js").
/**
 * ═══════════════════════════════════════════════════════════════
 * THƯ VIỆN TEMPLATE CHUẨN — HỆ THỐNG HIẾU HỌC — CS2627/PT2627
 * Phiên bản: v10.0 — 2026-08-09 (xem stamp CHÍNH THỨC dòng 1; changelog chi tiết bên dưới)
 * ═══════════════════════════════════════════════════════════════
 *
 * CHANGELOG v10.1 (Ông Bụt — dọn tham số hình, 09/08/2026):
 *   [DỌN] Đảo tham số CHÍNH về hinhBenPhai (khớp hành vi neo PHẢI của hinhVeTextBox);
 *         hinhBenTrai còn NHẬN làm bí danh (code cũ không vỡ). Biến nội bộ _hinhTrai → _hinh.
 *         Sửa GỐC lỗi tài liệu "neo trái": tên hinhBenTrai (v9.4) gây các phiên trước hiểu
 *         nhầm hành vi. HÀNH VI KHÔNG ĐỔI — vẫn neo phải, chữ wrap trái (HP V11.2 Điều 18.3).
 *
 * CHANGELOG v10.0 (Ông Bụt — BẢN SAU CHUẨN HÓA đồng bộ HP CS2627 V11.1, 09/08/2026):
 *   [HP18.1] viDuLyThuyet() guard: mục ② CẤM neo hình bên phải — hình lý thuyết luôn
 *            dòng riêng căn giữa. Truyền hinhBenTrai/hinhBenPhai vào là CHẶN.
 *   [HP72/76] trangCuoiChuong() GỠ bangNguonGoc — HP V11 bỏ hẳn bảng nguồn gốc gom cuối
 *            chương, nguồn kiểm ở cấp bài. bangNguonGoc() giữ định nghĩa (code cũ không vỡ)
 *            nhưng KHÔNG còn gộp; đừng truyền dsNguon vào trangCuoiChuong.
 *   [MỐC] Bump v9.9 → v10.0 cắt mớ stamp cũ (thầy chốt 09/08). Từ đây MỘT số duy nhất cho
 *         template + API_REFERENCE (v10.0). Chữ ký hàm sinh tự động qua sinh_apiref.js.
 *   [ĐỒNG BỘ HP] Cấu trúc Dạng toán (A.1: Bài toán mẫu→Phân tích→Lời giải→Phương pháp chung
 *         →Sai lầm→Ghi nhớ) nay ĐÃ khớp HP V11.1 Điều 23.2 (V11 gốc còn tả khung cũ — đã sửa).
 *
 * CHANGELOG v9.6 (Ông Bụt — vá Nhóm A+B sau phiên nghiệm thu B04, 05/08/2026):
 *   [A.1] dangToanDayDu() DỰNG LẠI theo Chuẩn trình bày A.1: đề mẫu TRƯỚC → phân tích
 *         → lời giải → PHƯƠNG PHÁP CHUNG đặt SAU → sai lầm/ghi nhớ. Bỏ mục "Nhận dạng"
 *         riêng (Phân tích gánh). Trước v9.6 dựng nhận dạng+phương pháp TRƯỚC ví dụ (sai A.1).
 *   [A.1] tieuDeDang() BỎ ép "(mứcĐộ)" khỏi tên Dạng (A.1: tên không gắn nhãn mức độ);
 *         thêm keepNext chống mồ côi. Tham số `mucDo` không còn dùng (truyền dư vẫn chạy).
 *   [A.1] THÊM phanTich(noiDung) — mục Phân tích 1–2 câu giữa đề mẫu và lời giải; nhận
 *         string/mảng trộn. phuongPhapGiai() thêm opts.nhan (dangToanDayDu gọi "Phương pháp chung").
 *   [TN] cauTracNghiem() guard trùng đáp án BỎ QUA khi đáp án chứa công thức OMML — trước
 *        đây 4 đáp án phân số ["x = ", phanSo] đều rút còn "x =" → chặn build NHẦM.
 *   [SAI/GHI] saiLamThuongGap() & ghiNhoNhanh() nay nhận MẢNG TRỘN (chèn phanSo/luyThua)
 *        qua toInline; guard 2 dòng đếm qua _extractText. Trước chỉ nhận string.
 *   [ĐÁP ÁN] bangDapAnPhanI() ép 1 DÒNG cho 8 câu: bỏ nhãn "Đáp án:", "Câu 1-B" sát,
 *        phân tách "; ". Trước "Đáp án: Câu 1 - B;  …" tràn 2 dòng ở 8 câu.
 *
 * CHANGELOG v9.5 (Ông Bụt — phiên chuẩn trình bày 05/08/2026):
 *   [KHOẢNG THỞ] Thêm 3 hằng THO_RONG(280)/THO_VUA(130)/THO_HEP(60) — áp đồng bộ
 *            mọi hàm sinh-khối để phân tầng khoảng cách RỘNG>VỪA>HẸP, trị "chữ sát
 *            chữ". Căn cứ: HP V10.5 Điều 13.4; chi tiết ở CHUAN_TRINH_BAY Nhóm A.
 *   [CỬA KÝ HIỆU] xuatFile() quét thêm − (U+2212), – (en), — (em), ÷, · — build FAIL
 *            kèm thông báo cách thay. Căn cứ: HP V10.5 Điều 16.2; CHUAN_TRINH_BAY C5.
 *   [HIỆU ĐÍNH CĂN LỀ] Sửa comment [C6] lỗi thời (ghi nhầm "loiGiai căn trái") cho
 *            khớp code — loiGiai/gopDongTuDo/paraHePhuongTrinh vốn đã justify:true
 *            đúng HP V10.5 Điều 14. Code không đổi, chỉ sửa chú thích.
 *
 * CHANGELOG v9.4 (Ông Bụt — theo quyết định của thầy ngày 24/07/2026):
 *   [CĂN LỀ] HP V10.4 Điều 14 viết lại: căn đều MỌI đoạn văn xuôi. Đã thêm justify
 *            cho loiGiai (các bước + kết luận), nhanDang, phuongPhapGiai,
 *            saiLamThuongGap, ghiNhoNhanh. Căn trái nay chỉ còn: dòng xếp tab,
 *            ô bảng, tiêu đề & mã.
 *   [VÁ BUG] paraCoHinhPhai() NUỐT MẤT opts.justify — hàm chỉ đọc opts.align, trong
 *            khi viDu/baiTapTaiLop/tuLuanBTVN đều truyền justify:true. Hậu quả: mọi
 *            đề bài kèm hình bị căn trái suốt bao lâu nay, trái HP Điều 14.
 *   [NEO TRÁI] HP V10.4 Điều 18: hình neo TRÁI, chữ wrap PHẢI, áp mọi vị trí trong
 *            bài. Bỏ Điều 18.1 cũ → viDuLyThuyet() gỡ guard, nay chỉ là bí danh của
 *            viDu(). Tham số đổi tên hinhBenPhai → hinhBenTrai (giữ tên cũ làm bí danh).
 *   [TAB STOP] tabLine() nhận opts.hinhTraiCm để tính mốc cột theo bề ngang THẬT.
 *            Không có nó, cột đầu của dãy a) b) c) d) rơi vào vùng hình neo trái.
 *   [NGƯỠNG] hinhVeTextBox() phát biểu lại theo "cột chữ còn ≥ 9cm" thay vì "hình < 9cm".
 *   [GUARD] para() chặn Paragraph lồng Paragraph — Word từ chối mở file, mọi trình
 *            kiểm XML đều báo hợp lệ (sự cố B09, mất 2 giờ ngày 24/07).
 *   [LỘT NHÃN] layoutCauHoi() và cauTracNghiem() tự bỏ nhãn "a)" / "A." mà AI Soạn
 *            gõ sẵn — trước đây in ra "a) a) Tìm một cặp góc...".
 *   [SỬA] nhanDang() dùng ▸ (U+25B8, nhỏ hơn ►) thay vì "|" — HP Điều 16.1 và 23.2 quy định nút tam giác.
 *   [BỎ 12pt] SZ_MISTAKE 24 (12pt) → = SZ_CONTENT (13pt). Toàn hệ thống nay
 *             chỉ còn 2 cỡ chữ: 13pt nội dung, 11pt mã & tham chiếu.
 *             Áp cho: Sai lầm thường gặp, Ghi nhớ, Ghi nhớ nhanh, bảng đáp án
 *             Phần I, bảng Đúng/Sai. Căn cứ: HP V10.4 Điều 13.2.
 *   [GUARD 2 DÒNG] saiLamThuongGap() và ghiNhoNhanh() nay CHẶN BUILD nếu khối
 *             in ra quá 2 dòng (ước lượng 88 ký tự/dòng ở 13pt trên 18.4cm).
 *             Trước v9.4 dùng slice(0,3) — âm thầm cắt mất mục thứ 4, AI Soạn
 *             không hề biết mình bị mất nội dung. Nay báo lỗi rõ kèm số ký tự
 *             từng mục và cách sửa. Căn cứ: HP V10.4 Điều 22.7 & 23.2.
 *   [MỚI] ghiNhoNhanh(dongArr, {nhan}) — tham số `nhan` để đổi nhãn thành
 *             "Ghi nhớ" khi dùng ở cuối mục ② (HP Điều 22.7).
 *
 * GHI CHÚ: dòng khai báo [MÔN|CẤP|LỚP|BÀI] đã BỎ HẲN khỏi hệ thống
 *          (quyết định 24/07/2026) — mã định danh Phần IX thay thế hoàn toàn.
 *
 * ───────────────────────────────────────────────────────────────
 *
 * CHANGELOG v8.1 (Ông Bụt — đúc kết từ 3 lần trượt QC bài HH_CH03_B08):
 *   [FIX 1] tuLuanBTVN(): thiếu dòng push coHinh → hình truyền vào bị mất
 *           hoàn toàn, không xuất hiện trong docx. Đã thêm, đồng bộ với
 *           baiTapTaiLop().
 *   [FIX 2] hinhVe(): tiLeGoc chỉ nhận số; nếu truyền {width,height}
 *           (theo code mẫu SAI ở Instructions v2 Mục 12.3) → pxHeight = NaN
 *           → hình méo/hỏng. Nay nhận CẢ HAI dạng, đồng bộ với
 *           viDuCoHinhBenCanh().
 *   [FIX 3] bangDungSai(): menhDe render bằng nối string trực tiếp nên
 *           KHÔNG nhúng được kyHieuGoc() → không viết được mệnh đề bẫy có
 *           tên góc. Nay dùng toInline() → nhận string HOẶC mảng trộn.
 *   [FIX 4] _guardKyHieuGoc(): sửa CẢ HAI loại lỗi —
 *           • Chặn nhầm câu văn hợp lệ ("góc phản xạ", "góc lệch",
 *             "góc phụ", "chia góc thành hai phần") → tắc việc, phá cả
 *             Vật Lý vì template dùng chung.
 *           • Lọt lỗi thật: "Góc xOy" viết hoa đầu câu không bị bắt.
 *           Logic mới: tên góc = chữ La-tinh không dấu + có chữ HOA + ≤6 ký tự.
 *   [FIX 5] _guardND() — LỖ HỔNG LỚN NHẤT: các hàm chỉ guard khi tham số là
 *           string thuần (`if (typeof deBai === "string")`). Truyền deBai/
 *           cauHoi/cacBuoc/ketLuan dạng ARRAY thì KHÔNG hàm nào kiểm tra
 *           → ký hiệu góc sai lọt thẳng ra file. Đây là lý do B08 v3/v6/v9
 *           build trót lọt mà QC vẫn bắt lỗi ký hiệu góc.
 *           Nay guard quét được: string, mảng trộn, và cả TextRun đã dựng sẵn.
 *   [NEW 1] baiTapTaiLopCoHinhBenCanh() — layout 2 cột (chữ 62% / hình 38%).
 *   [NEW 2] tuLuanBTVNCoHinhBenCanh()   — layout 2 cột.
 *           → Dùng khi hình nhỏ (rongCm ≤ 7); hình lớn vẫn dùng hàm thường
 *             với tham số coHinh.
 *
 * (changelog cũ v9.0–v9.3 — giữ để truy vết)
 *
 * CHANGELOG v9.3 (Ông Bụt — đồng bộ HP V10.3 bản cập nhật Điều 14 & 18):
 *   [C1] phuongPhapGiai(): en-dash U+2013 -> hyphen U+002D (AI Soạn báo T1).
 *   [C2] tieuDePhanI/II/III(): en-dash trong tiêu đề -> hyphen (T2).
 *   [C3] headerFooterBaiHoc(): header thiếu "PHÁT TRIỂN" -> đã thêm (T3).
 *   [C4] hinhVeTextBox(): ngưỡng chặn 10cm -> 9cm (Điều 18.2). Lý do: vùng chữ
 *        A4 = 18.4cm; hình 9cm + khe -> chữ còn 9.1cm, hẹp hơn thì justify giãn xấu.
 *   [C5] THÊM viDuLyThuyet() cho mục ② — CỐ Ý không nhận hinhBenPhai
 *        (Điều 18.1: hình mục ② luôn dòng riêng căn giữa). Dùng đúng hàm là
 *        tự đúng chuẩn, AI Soạn không thể lỡ đặt text box ở mục ②.
 *   [C6] Căn lề theo Điều 14 (HP V10.4/V10.5): CĂN ĐỀU = MỌI đoạn văn xuôi, KỂ CẢ
 *        các bước lời giải (mẫu đối chứng 24/07 đã bác lập luận "OMML giãn xấu" cũ).
 *        CĂN TRÁI chỉ còn: dòng xếp tab (đề trắc nghiệm, đáp án A/B/C/D, câu a/b/c),
 *        ô bảng, tiêu đề & mã. loiGiai()/gopDongTuDo()/paraHePhuongTrinh() đều
 *        justify:true (đã đúng).  [hiệu đính 05/08: comment cũ ghi nhầm "căn trái".]
 *
 * CHANGELOG v9.2 (Ông Bụt — đồng bộ HP V10.3):
 *   [B1] para() thêm opt justify; lyThuyet() căn đều hai bên mặc định (HP Điều 14).
 *   [B2] bangDungSai() CÓ viền mảnh xám #999999 (HP V10.3 Điều 17.2 — trước ẩn viền).
 *   [B3] viDu/baiTapTaiLop/tuLuanBTVN + dangToanDayDu nhận hinhBenPhai:{imageBuffer,
 *        rongCm,tiLeGoc} → tự đặt hình neo PHẢI, chữ wrap TRÁI (text box), căn đều.
 *        Đây là cách đặt hình MẶC ĐỊNH cho hình nhỏ (HP Điều 18) — AI Soạn chỉ cần
 *        truyền hinhBenPhai, không phải tự chọn hinhVe/hinhVeTextBox.
 *
 * CHANGELOG v9.1 (Ông Bụt):
 *   [A10] dangToanDayDu() nhận thêm viDuCoHinh — ví dụ trong dạng toán có thể
 *        kèm hình (trước đây bị chặn bởi guard "cần hình vẽ"). Cần cho Hình học.
 *   [A8] Thêm hinhVeTextBox() + paraCoHinhPhai() — hình neo PHẢI, chữ wrap TRÁI
 *        bằng floating ImageRun (wp:anchor + wrapSquare), KHÔNG dùng bảng 2 cột.
 *        Thay thế đúng chuẩn cho *CoHinhBenCanh đã xóa (HP V10 Điều 18).
 *        Chặn rongCm ≥ 9 → hướng dùng hinhVe(). Export: hinhVeTextBox, paraCoHinhPhai.
 *   [A9] Thêm chiSoDuoi() (chỉ số dưới phức tạp x_{n+1}) + triTuyetDoi() (gạch đứng
 *        |…| giãn theo chiều cao) — OMML chuẩn. Bổ nốt 2 ký hiệu Loại B còn thiếu
 *        (HP V10 Điều 16.4). Chỉ số/trị tuyệt đối đơn giản vẫn gõ Unicode/thẳng.
 *        Export: chiSoDuoi, triTuyetDoi.
 *
 * CHANGELOG v9.0 (Ông Bụt — đồng bộ HP V10 + bàn giao 2026-07-21):
 *   [A1] bangDapAnPhanI() + bangDungSai(): bỏ toàn bộ viền (HP V10 Điều 17.2 —
 *        bảng nội dung ngắn = ẨN VIỀN, chữ ĐẬM ĐEN, thẳng cột).
 *   [A2] tabLine(): thay khoảng trắng giả bằng tab stop thật chia đều TOTAL_W
 *        theo số cột — căn đều bất kể font/zoom, đúng HP V10 Điều 24.2.
 *   [A3] gopDongTuDo(): không ngắt dòng ngay trước ⇒ (U+21D2).
 *        canBac(): hàm OMML căn bậc 2/3/n chuẩn SGK — BẮT BUỘC trước Toán 9
 *        (HP V10 Điều 16.4). Export: canBac.
 *   [A4] hinhVe(): thêm guard imageBuffer rỗng. type:'png' BẮT BUỘC — comment rõ.
 *   [A5] para(): thêm keepLines/keepNext — chống nhảy trang 2 tầng (HP V10 Điều 32).
 *   [A6] toPhanChuong(): thêm 1 dòng trống trước tên chương (HP V10 Điều 51 mục 8).
 *   [XÓA] viDuCoHinhBenCanh / baiTapTaiLopCoHinhBenCanh / tuLuanBTVNCoHinhBenCanh
 *          / _khoiBaiTapCoHinh / _oHinhBenCanh / _NOBORDER / _noBorders:
 *          HP V10 Điều 18 CẤM bảng 2 cột cho khối đề-hình.
 *          Thay bằng hinhVe() dòng riêng (≥10cm) hoặc text box (chờ quyết định).
 *
 * MỤC ĐÍCH: AI Soạn KHÔNG tự viết code định dạng Word.
 * AI Soạn CHỈ ĐƯỢC gọi các hàm dưới đây, truyền nội dung vào,
 * KHÔNG được sửa bất kỳ thông số font/màu/spacing nào bên trong.
 *
 * CÁCH DÙNG:
 *   const H = require('./hieuhoc_template.js');
 *   const children = [];
 *   children.push(...H.tenBaiHoc({ soBai:1, tenBai:"Tập hợp", tiet:2,
 *     sgkTr:"5–8", sbtTr:"5–6", ma:"GT_CH01_B01" }));
 *   children.push(...H.mucTieu({ kienThuc:"...", kyNang:"...", nangLuc:"..." }));
 *   ... rồi Packer.toBuffer(new Document({ sections:[{ children }] }))
 *
 * NGHIÊM CẤM: sửa các hằng số màu/size ở đầu file. Nếu thấy cần khác
 * đi so với thực tế bài học → DỪNG LẠI, báo thầy/cô, không tự sửa.
 * ═══════════════════════════════════════════════════════════════
 */

// ════════ NHẬT KÝ v9.4 → v9.5 (phiên 05/08/2026, thầy duyệt) ════════
// 1) BA CẤP KHOẢNG THỞ (THO_RONG/VUA/HEP) áp ĐỒNG BỘ mọi hàm sinh-khối —
//    trị "chữ sát chữ": mục lớn/Dạng/khối TN = RỘNG; mục con/bài/câu = VỪA;
//    kết luận rời bước giải = HẸP; dòng nội dung trong khối = liền (0).
// 2) Nhãn câu a) b) c) d) IN ĐẬM (layoutCauHoi) — phân biệt với nội dung.
// 3) Cửa xuatFile quét thêm ký hiệu sai chuẩn: − (U+2212), – , — , ÷ , ·
//    (HP Điều 16.1/16.2) — chặn tại chỗ, không đợi AI QC.
const fs = require("fs");
const path = require("path");
const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, VerticalAlign, ShadingType, UnderlineType,
  Header, Footer, PageNumber, ImageRun,
  Math: DMath, MathRun, MathSuperScript, MathFraction, MathSubScript, RunProperties,
  BuilderElement, createMathBase, createMathAccentCharacter,
  HorizontalPositionAlign, HorizontalPositionRelativeFrom,
  VerticalPositionRelativeFrom, TextWrappingType, TextWrappingSide,
} = require("docx");

const AdmZip = require('adm-zip');

/**
 * Patch docPr id trong file docx — mỗi hình có id DUY NHẤT.
 * Word báo "unreadable content" khi nhiều hình có id=1 (lỗi A2).
 *
 * Cách dùng trong script AI Soạn:
 *   const buf = H.patchDocPrIds(await Packer.toBuffer(doc));
 *   fs.writeFileSync('output.docx', buf);
 *
 * @param {Buffer} docBuffer — kết quả từ Packer.toBuffer(doc)
 * @returns {Buffer} — docx đã patch, sẵn sàng ghi file
 */
function patchDocPrIds(docBuffer) {
  const zip = new AdmZip(docBuffer);
  let xml = zip.readAsText('word/document.xml');
  let counter = 0;
  xml = xml.replace(/(<wp:docPr\s+id=")[^"]*(")/g, (m, pre, post) => pre + (++counter) + post);
  zip.updateFile('word/document.xml', Buffer.from(xml, 'utf8'));
  return zip.toBuffer();
}

// [v9.4] Kiểm TỈ LỆ CHỮ CÓ DẤU trong văn bản tiếng Việt.
// Sự cố B09 v2: AI Soạn gõ tiếng Việt KHÔNG DẤU toàn bài ("Cac goc tao boi...").
// Template không sinh lỗi này (lỗi nội dung), nhưng CHẶN được: văn bản tiếng Việt
// thật luôn có tỉ lệ ký tự-có-dấu đáng kể; thấp bất thường = mất dấu.
const _CO_DAU = /[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]/i;
function _kiemDauTiengViet(xml) {
  const texts = (xml.match(/<w:t[^>]*>(.*?)<\/w:t>/g) || [])
    .map(m => m.replace(/<[^>]+>/g, ''));
  // chỉ xét đoạn văn xuôi dài (>25 ký tự, có ít nhất 4 chữ cái liền)
  const vanXuoi = texts.filter(t => t.length > 25 && /[a-zàâăêôơư]{4}/i.test(t));
  if (vanXuoi.length < 5) return null;             // quá ít văn xuôi, bỏ qua
  const coDau = vanXuoi.filter(t => _CO_DAU.test(t)).length;
  const tiLe = coDau / vanXuoi.length;
  if (tiLe < 0.5) {
    const vd = vanXuoi.find(t => !_CO_DAU.test(t)) || '';
    return `[MẤT DẤU TIẾNG VIỆT] Chỉ ${(tiLe*100).toFixed(0)}% đoạn văn xuôi có dấu ` +
      `(bình thường > 90%). AI Soạn nhiều khả năng gõ tiếng Việt KHÔNG DẤU.\n` +
      `   Ví dụ đoạn mất dấu: "${vd.slice(0, 60)}…"\n` +
      `   Sửa: gõ lại có dấu đầy đủ. Đây là lỗi nghiêm trọng, KHÔNG được xuất bản.`;
  }
  return null;
}

// [v9.4] CỬA VÀO DUY NHẤT — dựng sẵn TOÀN BỘ KHUNG (khổ giấy, lề, header, footer).
// AI Soạn CHỈ đưa nội dung + thông tin bài; hàm lo hết định dạng trang.
// KHÔNG để AI tự viết new Document / tự set lề / tự gắn header — mỗi lần tự làm là
// một lần quên hoặc set sai (lề lệch, thiếu footer, khổ giấy sai).
//
//   const doc = H.taoTaiLieu({ soBai: 8, tenBai: "...", lop: "Lớp 7", children });
//   await H.xuatFile(doc, "/mnt/user-data/outputs/HH7_CH03_B08.docx");
//
function taoTaiLieu({ soBai, tenBai, lop, children }) {
  const { Document } = require("docx");
  if (!Array.isArray(children)) throw new Error("[taoTaiLieu] 'children' phải là mảng Paragraph/Table đã dựng sẵn.");
  const { header, footer } = headerFooterBaiHoc({ soBai, tenBai, lop });
  return new Document({
    sections: [{
      properties: {
        page: { size: PAGE_SIZE, margin: PAGE_MARGIN },
      },
      headers: { default: header },
      footers: { default: footer },
      children,
    }],
    // mặc định font & cỡ toàn tài liệu — AI không cần set từng run
    styles: {
      default: {
        document: { run: { font: TNR, size: SZ_CONTENT } },
      },
    },
  });
}

// ─────────────────────────────────────────────────────────────
// taoTaiLieuDeKT — dựng Document cho ĐỀ KIỂM TRA (thay khối Document
//   tự dựng trong build script mỗi đề). Header/footer đề KT tự gắn
//   (ĐÚNG MẪU headerFooterBaiHoc).
//   Dùng: const doc = H.taoTaiLieuDeKT({ tenDe: 'Đề kiểm tra ... (Đề A)', children: C });
//   · tenDe        — hiện ở header chạy mỗi trang (dạng thường, nhận diện đề/tránh lẫn A/B).
//   · headerFooter=false — tắt header/footer trang (nếu muốn tờ trắng).
//   Khối "ĐỀ KIỂM TRA…/họ tên/điểm" đầu trang vẫn do headerDeKiemTra() đẩy vào children.
// ─────────────────────────────────────────────────────────────
function taoTaiLieuDeKT({ tenDe, children, headerFooter = true }) {
  const { Document } = require("docx");
  if (!Array.isArray(children)) throw new Error("[taoTaiLieuDeKT] 'children' phải là mảng Paragraph/Table đã dựng sẵn.");
  const sec = {
    properties: { page: { size: PAGE_SIZE, margin: PAGE_MARGIN } },
    children,
  };
  if (headerFooter) {
    const { header, footer } = headerFooterDeKT({ tenDe });
    sec.headers = { default: header };
    sec.footers = { default: footer };
  }
  return new Document({
    sections: [sec],
    styles: { default: { document: { run: { font: TNR, size: SZ_CONTENT } } } },
  });
}

// [v9.4] CỬA RA DUY NHẤT — gộp mọi kiểm tra + vá id.
// AI Soạn CHỈ gọi hàm này để xuất file, KHÔNG tự Packer.toBuffer + ghi file.
// [v9.4] BỘ KIỂM TRÌNH BÀY — quét document.xml tìm lỗi trình bày CHUNG.
// Chỉ kiểm cái ĐO ĐƯỢC CHẮC CHẮN (không báo oan). Trả mảng lỗi (rỗng = sạch).
// Mở rộng dần: mỗi khi gặp loại lỗi trình bày mới, thêm một mục ở đây.
function _kiemTrinhBay(xml) {
  const loi = [];

  // (a) Đoạn lồng đoạn — Word từ chối mở file
  if (/<w:p\b[^>]*>(?:(?!<\/w:p>)[\s\S])*?<w:p\b/.test(xml))
    loi.push("Đoạn văn lồng trong đoạn văn (<w:p> trong <w:p>) — Word sẽ từ chối mở. Quên spread mảng: dùng ...H.loiGiai() thay vì H.para(H.loiGiai()).");

  // (b) Cỡ 12pt — đã bỏ khỏi hệ thống (HP Điều 13.2)
  if (xml.includes('w:val="24"'))
    loi.push('Còn cỡ chữ 12pt (w:val="24") — đã bỏ (HP Điều 13.2).');

  // (c) Mất dấu tiếng Việt
  const loiDau = _kiemDauTiengViet(xml);
  if (loiDau) loi.push(loiDau);

  // texts/full — dùng cho các mục (e)(f)… bên dưới
  const texts = (xml.match(/<w:t[^>]*>([^<]*)<\/w:t>/g) || []).map(m => m.replace(/<[^>]+>/g, ""));
  const full = texts.join(" ");

  // (d) Nhãn nhân đôi "a) a)" / "A. A." — template tự đánh nhãn, AI gõ thêm là lặp.
  //   [v10.9] Kiểm TỪNG đoạn <w:p>, TỪNG cột. LƯU Ý: tabLine() sinh TAB là ký tự "\t" LITERAL
  //   trong <w:t> (KHÔNG phải element <w:tab/>) → gộp text trong đoạn rồi split theo "\t".
  //   Tránh false-positive khi tên điểm cuối câu ("…B.") đứng trước nhãn đáp án "B." ở cột kế.
  for (const p of xml.split(/<\/w:p>/)) {
    const pText = (p.match(/<w:t[^>]*>([^<]*)<\/w:t>/g) || [])
      .map(m => m.replace(/<[^>]+>/g, "")).join("");
    let found = false;
    for (const seg of pText.split("\t")) {
      const nhanDoi = seg.match(/([a-h])\)\s*\1\)|([A-H])\.\s*\2\./);
      if (nhanDoi) { loi.push(`Nhãn nhân đôi "${nhanDoi[0]}" — template tự đánh nhãn, không gõ thêm.`); found = true; break; }
    }
    if (found) break;
  }

  // (e) Ký hiệu góc sai ∠ (HP Điều 16 — phải dùng kyHieuGoc/mũ cong)
  if (/∠/.test(full))
    loi.push('Ký hiệu góc "∠" — dùng H.kyHieuGoc() (mũ cong chuẩn SGK), không gõ ∠.');

  // [v9.5] (e2) Dấu trừ/chia/nhân SAI CHUẨN trong văn bản (HP Điều 16.1/16.2).
  // Quét text run — KHÔNG đụng OMML. Cửa tự chặn, không đợi AI QC.
  const _kySai = [
    ["\u2212", 'dấu trừ dài U+2212 (−) — thay bằng "-" (U+002D)'],
    ["\u2013", 'en dash U+2013 (–) — thay bằng "-" (U+002D)'],
    ["\u2014", 'em dash U+2014 (—) — thay bằng "-" (U+002D)'],
    ["\u00f7", 'dấu chia ÷ (Anh–Mỹ) — thay bằng " : "'],
    ["\u00b7", 'dấu nhân · (giữa dòng) — nhân số dùng "×", nhân ẩn viết liền'],
  ];
  for (const [ch, mo] of _kySai) {
    if (full.includes(ch)) loi.push("Ký hiệu sai chuẩn: " + mo + " (HP Điều 16.1/16.2).");
  }

  // (f) Dòng khai báo [MÔN|CẤP|LỚP|BÀI] — đã bỏ (HP Điều 57.1)
  if (/\[\s*MÔN\s*[:|]/i.test(full))
    loi.push('Còn dòng khai báo [MÔN|CẤP|LỚP|BÀI] — đã bỏ (HP Điều 57.1). Nhận diện bài qua mã trong tenBaiHoc({ma}).');

  // (g) Nguồn ngoài lọt lưới — nếu có "(... tr...)" mà KHÔNG phải SGK/SBT/Tự soạn
  const nguon = full.match(/\([^)]*(?:tr(?:ang|\.)|bài\s*\d)[^)]*\)/gi) || [];
  for (const n of nguon) {
    if (!/SGK|SBT|tự\s*soạn/i.test(n)) {
      loi.push(`Nguồn ngoài lộ tên: "${n}" — chỉ SGK/SBT được ghi, còn lại "(Tự soạn)" (HP Điều 5.7.1). Dùng thamChieu qua hàm để tự lọc.`);
      break;
    }
  }

  // (h) Căn lề: văn xuôi phải justify. Nếu 'left' NHIỀU HƠN HẲN 'both' → nghi dùng
  //     template cũ chưa áp justify (HP Điều 14). Ngưỡng rộng để không báo oan.
  const nLeft = (xml.match(/w:val="left"/g) || []).length;
  const nBoth = (xml.match(/w:val="both"/g) || []).length;
  if (nBoth > 0 && nLeft > nBoth * 3 + 10)
    loi.push(`Căn lề nghi sai: ${nLeft} đoạn căn trái so với ${nBoth} căn đều — văn xuôi phải justify (HP Điều 14). Có thể dùng template cũ chưa áp justify.`);

  return loi;
}

// ═══════════════════════════════════════════════════════════════
// [v9.7] CỬA KIỂM MÁY CHUNG — kiemMay(bufOrPath, opts)
//   Code hóa checklist máy (HP Điều 61). AI Soạn (qua xuatFile) và AI QC
//   (gọi trực tiếp trên file nhận) dùng CHUNG một cửa. Bắt cả failure IM LẶNG.
// ═══════════════════════════════════════════════════════════════
function kiemMay(bufOrPath, opts = {}) {
  const AdmZipL = require("adm-zip");
  const buf = Buffer.isBuffer(bufOrPath) ? bufOrPath : require("fs").readFileSync(bufOrPath);
  const zip = new AdmZipL(buf);
  const xml = zip.readAsText("word/document.xml");
  const loi = _kiemTrinhBay(xml);

  if (xml.includes("[object Object]"))
    loi.push('Có "[object Object]" — đối tượng lọt vào chỗ cần string (kiểm tham số hàm).');
  // Chỉ bắt shading MÀU — trắng (FFFFFF) và auto là "không shading", hợp lệ (Điều 17.2 bảng nền trắng).
  const shdFills = (xml.match(/<w:shd\b[^>]*w:fill="([0-9A-Fa-f]{6})"/g) || [])
    .map(x => x.match(/w:fill="([0-9A-Fa-f]{6})"/)[1].toUpperCase())
    .filter(c => c !== "FFFFFF");
  if (shdFills.length) loi.push(`Có ${shdFills.length} chỗ tô nền MÀU (${[...new Set(shdFills)].join(", ")}) — HP Điều 17.1 CẤM shading màu.`);
  const hl = xml.match(/<w:highlight\b/g) || [];
  if (hl.length) loi.push(`Có ${hl.length} chỗ highlight (HP Điều 17.3 CẤM — đánh dấu bằng in đậm/màu chữ).`);
  const empty = (xml.match(/<w:p\/>/g) || []).length + (xml.match(/<w:p>\s*<\/w:p>/g) || []).length;
  if (empty) loi.push(`Có ${empty} đoạn rỗng <w:p/> (HP Điều 17.4 — dùng spacing).`);
  const nHinh = (xml.match(/<w:drawing>/g) || []).length;
  if (opts.soHinh != null && nHinh !== opts.soHinh)
    loi.push(`Số hình nhúng = ${nHinh} nhưng khai báo soHinh = ${opts.soHinh}. Nghi coHinh nuốt hình (thiếu spread "...H.hinhVe()") hoặc lệch thiết kế. [FAILURE IM LẶNG]`);
  let sxml = ""; try { sxml = zip.readAsText("word/settings.xml"); } catch (e) {}
  if (!sxml || !sxml.includes("compatibilityMode"))
    loi.push('Thiếu compatibilityMode (settings.xml) → Word desktop có thể từ chối mở.');
  const ids = (xml.match(/docPr[^>]+id="(\d+)"/g) || []).map(x => x.match(/id="(\d+)"/)[1]);
  const dup = [...new Set(ids.filter((x, i) => ids.indexOf(x) !== i))];
  if (dup.length) loi.push(`docPr id trùng: ${dup.join(", ")} → Word "unreadable content" (cần patchDocPrIds).`);
  const badMedia = zip.getEntries()
    .filter(e => e.entryName.startsWith("word/media/") && e.entryName !== "word/media/")
    .filter(e => !/\.(png|jpe?g|gif|svg|emf|wmf)$/i.test(e.entryName));
  if (badMedia.length) loi.push(`Media sai đuôi: ${badMedia.map(e => e.entryName).join(", ")} → hình mất trong Word.`);
  // [v9.8·B5] Quét footer/header cho ký hiệu sai (Điều 16.2) — trước đây chỉ soi document.xml
  const _badSym = [["\u2013","en dash –"],["\u2014","em dash —"],["\u2212","minus −"],["\u00f7","÷"],["\u2220","∠"],["[object Object]","[object Object]"]];
  zip.getEntries().filter(e => /word\/(footer|header)\d*\.xml$/.test(e.entryName)).forEach(e => {
    const t = zip.readAsText(e.entryName);
    _badSym.forEach(([ch, ten]) => { if (t.includes(ch)) loi.push(`${e.entryName.split("/").pop()}: có ${ten} (Điều 16.2).`); });
  });
  return loi;
}

// [v9.7] Guard chống NUỐT HÌNH IM LẶNG: hinhVe() trả MẢNG [hình, chú thích];
// quên spread → coHinh thành [[..]] → docx bỏ qua không báo. Tự làm phẳng + cảnh báo.
function _appendHinh(out, coHinh, ctx) {
  if (!coHinh || !Array.isArray(coHinh)) return;
  for (const item of coHinh) {
    if (Array.isArray(item)) {
      console.warn(`[CẢNH BÁO ${ctx}] coHinh có MẢNG LỒNG — thiếu spread "...". Đã tự làm phẳng để không mất hình; hãy sửa: coHinh: [ ...H.hinhVe(...) ].`);
      item.flat(Infinity).forEach(x => x && out.push(x));
    } else if (item) out.push(item);
  }
}

// Chặn tại chỗ các lỗi trình bày — CỬA CHUNG kiemMay (v9.7).
async function xuatFile(doc, duongDan, opts = {}) {
  const { Packer } = require("docx");
  const buf0 = await Packer.toBuffer(doc);
  const buf = patchDocPrIds(buf0);              // vá id TRƯỚC → kiểm đúng bytes sẽ ghi
  const loi = kiemMay(buf, opts);               // CỬA MÁY CHUNG (AI QC gọi cùng hàm)
  if (loi.length)
    throw new Error("[CHẶN XUẤT] Bài có " + loi.length + " lỗi (cửa kiểm máy):\n" +
      loi.map((l, i) => `   ${i + 1}. ${l}`).join("\n") +
      "\n(Sửa hết rồi xuất lại. AI QC sẽ chạy lại CHÍNH cửa này để kiểm chéo.)");
  require("fs").writeFileSync(duongDan, buf);
  return duongDan;
}

// ─────────────────────────────────────────────────────────────
// HẰNG SỐ CHUẨN — KHÔNG ĐƯỢC SỬA
// ─────────────────────────────────────────────────────────────
const TNR = "Times New Roman";
const C_BLACK = "000000";
const C_RED = "C00000";
const C_RED_ANSWER = "DC2626";
const C_GRAY = "555555";
const C_WHITE = "FFFFFF";

const SZ_CONTENT = 26;   // 13pt — nội dung chính
const SZ_TITLE_BAI = 28; // 14pt — tên bài
const SZ_SMALL = 22;     // 11pt — tham chiếu, thông tin dòng 2
// [v9.4] 12pt ĐÃ BỊ XOÁ KHỎI HỆ THỐNG (HP V10.4 Điều 13.2).
// Giữ lại tên hằng để code cũ không vỡ, nhưng giá trị = SZ_CONTENT (13pt).
// KHÔNG dùng hằng này trong code mới — dùng thẳng SZ_CONTENT.
const SZ_MISTAKE = SZ_CONTENT;   // 13pt (trước v9.4 là 12pt)

// [v9.5] BA CẤP KHOẢNG THỞ (spacing before, đơn vị twip; 20 twip = 1pt) — HP Điều 13.4.
// Trị bệnh "chữ sát chữ": mọi ranh giới khối phải PHÂN TẦNG, không cách đều nhau.
const THO_RONG = 280;  // ranh giới MỤC LỚN (①②③④⑤) và trước mỗi DẠNG / KHỐI TN mới (~14pt)
const THO_VUA  = 130;  // giữa các MỤC CON, giữa các BÀI / VÍ DỤ / CÂU              (~6.5pt)
const THO_HEP  = 60;   // tách nhẹ trong cùng khối (vd. kết luận rời khỏi bước giải) (~3pt)

// [v9.4] LỌC NGUỒN THAM CHIẾU — chỉ SGK/SBT được ghi tên thật; mọi nguồn khác
// (sách luyện thi, tham khảo, "Toán Bút Phá"…) → "Tự soạn" (giấu nguồn ngoài,
// bảo vệ uy tín Hiếu Học). Áp cho MỌI thamChieu qua hàm này — AI Soạn không cần nhớ.
function _locNguon(tc) {
  if (!tc) return tc;
  const s = String(tc).trim();
  // đã là "Tự soạn" → giữ
  if (/^tự\s*soạn$/i.test(s)) return "Tự soạn";
  // có nhắc SGK hoặc SBT (sách giáo khoa / bài tập chính thống) → giữ nguyên
  if (/\b(SGK|SBT)\b/i.test(s)) return s;
  // còn lại: mọi nguồn ngoài → Tự soạn
  return "Tự soạn";
}

// Ước lượng số dòng in ra của một đoạn văn ở 13pt trên vùng chữ 18.4cm.
// Times New Roman 13pt: bề rộng ký tự trung bình ~0.21cm → ~88 ký tự/dòng.
// Dùng cho guard "tối đa 2 dòng" của Sai lầm / Ghi nhớ (HP V10.4 Điều 23.2).
const CHARS_PER_LINE = 88;
function _soDongUocTinh(text) {
  const s = String(text ?? "").trim();
  if (!s) return 0;
  return Math.max(1, Math.ceil(s.length / CHARS_PER_LINE));
}

const TOTAL_W = 10432; // A4, lề 1.3cm mỗi bên

// Thông số trang chuẩn — BẮT BUỘC dùng đúng 2 hằng số này khi khai báo
// `sections[].properties.page` trong Document, nếu không TOTAL_W ở trên
// (dùng để tính độ rộng bảng) sẽ không khớp với lề thực tế của trang.
const PAGE_SIZE = { width: 11906, height: 16838 }; // A4
const PAGE_MARGIN = { top: 567, bottom: 567, left: 737, right: 737 }; // 1cm/1cm/1.3cm/1.3cm


// ═════════════════════════════════════════════════════════════
// GUARD — PHÁT HIỆN KÝ HIỆU GÓC SAI VÀ THIẾU HÌNH
// Throw lỗi ngay khi AI Soạn dùng sai — file không build được
// ═════════════════════════════════════════════════════════════
const KY_HIEU_GOC_SAI = /[∠]/u;

// v8.1 — SỬA GUARD (Ông Bụt 2026-07-18):
//   Bản cũ có CẢ HAI loại lỗi:
//   [FP] Chặn nhầm câu văn hợp lệ: "góc phản xạ", "góc lệch", "góc phụ",
//        "góc quay", "chia góc thành hai phần"... → tắc việc, phá cả Vật Lý
//        (template dùng chung, VL có "góc tới", "góc phản xạ", "góc lệch").
//   [FN] Lọt lỗi thật: "Góc xOy = 60°" viết hoa đầu câu → regex cũ chỉ
//        match "góc" thường nên không bắt được.
//
//   Logic mới — tên góc thật có 3 đặc điểm bắt buộc:
//     1. Chỉ gồm chữ La-tinh không dấu + chỉ số dưới (xOy, AOB, mOt, O₁, A)
//     2. Có ít nhất 1 chữ HOA (đỉnh góc luôn viết hoa)
//     3. Không nằm trong danh sách ngoại lệ
//   → Từ tiếng Việt ("thành", "phản", "lệch", "phụ") có dấu hoặc không có
//     chữ hoa → tự động bỏ qua, không cần liệt kê hết.
const NGOAI_LE_GOC = /^(A|B|C|D|Sai|Dung|Do|La|Va|Neu|Khi)$/;

function _laTenGoc(tu) {
  if (!/^[A-Za-z][A-Za-z0-9\u2080-\u2089]*$/.test(tu)) return false;  // có dấu tiếng Việt → không phải
  if (!/[A-Z]/.test(tu)) return false;                                 // không có chữ hoa → không phải
  if (tu.length > 6) return false;                                     // tên góc không dài quá 6 ký tự
  return true;
}

function _guardKyHieuGoc(text, tenHam) {
  if (typeof text !== "string") return;
  if (KY_HIEU_GOC_SAI.test(text)) {
    throw new Error(
      "\n[LỖI KÝ HIỆU GÓC] Hàm " + tenHam + "() chứa ký hiệu ∠ text thuần:\n" +
      '  "' + text.substring(0,80) + (text.length>80?"...":"") + '"\n' +
      "→ Thay bằng H.kyHieuGoc() inline. KHÔNG được xuất file."
    );
  }
  // Bắt cả "góc" thường lẫn "Góc" hoa đầu câu
  const matchGoc = text.match(/[Gg]óc\s+([A-Za-zÀ-ỹ][A-Za-zÀ-ỹ0-9\u2080-\u2089]*)/u);
  if (matchGoc && _laTenGoc(matchGoc[1]) && !NGOAI_LE_GOC.test(matchGoc[1])) {
    throw new Error(
      "\n[LỖI KÝ HIỆU GÓC] Hàm " + tenHam + '() chứa "góc ' + matchGoc[1] + '" text thuần:\n' +
      '  "' + text.substring(0,80) + (text.length>80?"...":"") + '"\n' +
      '→ Thay bằng: para([..., H.kyHieuGoc("' + matchGoc[1] + '"), ...])'
    );
  }
}

// v8.1 — Trích text từ TextRun đã dựng sẵn để guard quét được.
// Trước đây guard chỉ thấy string thô: khi AI Soạn viết run("Ta có góc xOy")
// thì text bị bọc trong object → guard mù, lỗi lọt ra file.
// Hàm này đọc các node w:t trong JSON của TextRun. Math object (kyHieuGoc)
// không có w:t nên tự động được bỏ qua — đúng ý đồ.
function _textTuRun(obj) {
  try {
    const j = JSON.stringify(obj);
    if (!j || j.indexOf('"w:t"') === -1) return [];
    const out = [];
    const re = /"rootKey":"w:t","root":\[(?:[^\[\]]*?)"((?:[^"\\]|\\.)*)"\]/g;
    let m;
    while ((m = re.exec(j)) !== null) {
      try { out.push(JSON.parse('"' + m[1] + '"')); } catch (e) { /* bỏ qua */ }
    }
    return out;
  } catch (e) { return []; }
}

function _guardArr(arr, tenHam) {
  if (!Array.isArray(arr)) return;
  arr.forEach(item => {
    if (typeof item === "string") _guardKyHieuGoc(item, tenHam);
    else if (Array.isArray(item)) _guardArr(item, tenHam);
    else if (item && typeof item === "object") {
      _textTuRun(item).forEach(t => _guardKyHieuGoc(t, tenHam));
    }
  });
}

// v8.1 — Guard hợp nhất: nhận string, array trộn, hoặc TextRun đơn lẻ.
// Trước đây các hàm chỉ guard khi tham số là string thuần:
//     if (typeof deBai === "string") _guardKyHieuGoc(deBai, ...)
// → truyền deBai dạng ARRAY thì KHÔNG hàm nào kiểm tra, lỗi lọt thẳng ra file.
// Đây chính là lỗ hổng làm ký hiệu góc sai lọt qua build ở B08 v3/v6/v9.
function _guardND(val, tenHam) {
  if (typeof val === "string") _guardKyHieuGoc(val, tenHam);
  else if (Array.isArray(val)) _guardArr(val, tenHam);
  else if (val && typeof val === "object") _textTuRun(val).forEach(t => _guardKyHieuGoc(t, tenHam));
}

function _extractText(val) {
  if (typeof val === "string") return val;
  if (Array.isArray(val)) return val.map(_extractText).join(" ");
  return "";
}

function _canHinh(deBai, cacCau) {
  const deStr = _extractText(deBai) + " " + _extractText(cacCau);
  return (
    /quan sát hình|hình bên|hình vẽ|hình dưới|cho hình|xem hình|hình \d+\.\d+/i.test(deStr) ||
    /ba tia|tia nằm giữa|các tia|từ đỉnh/i.test(deStr) ||
    (/chứng minh/i.test(deStr) && /tia phân giác/i.test(deStr)) ||
    (/cắt nhau tại|hai đường thẳng cắt/i.test(deStr) &&
      /kể tên|gọi tên|các cặp góc|đối đỉnh|kề bù/i.test(deStr))
  );
}

// ── Counter toàn cục cho docPr id — mỗi ImageRun phải có id DUY NHẤT
// Word báo lỗi "unreadable content" nếu nhiều hình có cùng id
let _imgIdCounter = 0;
function _nextImgId() { return ++_imgIdCounter; }

// ─────────────────────────────────────────────────────────────
// HÀM CƠ SỞ (không gọi trực tiếp từ AI Soạn, dùng nội bộ)
// ─────────────────────────────────────────────────────────────
function run(text, opts = {}) {
  return new TextRun({
    text, font: TNR,
    bold: opts.bold || false,
    italics: opts.italic || false,
    underline: opts.underline ? { type: UnderlineType.SINGLE } : undefined,
    color: opts.color || C_BLACK,
    size: opts.size || SZ_CONTENT,
  });
}

// A5 v9.0: hỗ trợ keepLines / keepNext — chống nhảy trang 2 tầng
// keepLines: giữ toàn bộ đoạn trên cùng 1 trang (không bị bẻ đôi giữa chừng)
// keepNext:  giữ đoạn này cùng trang với đoạn kế tiếp (tiêu đề không bị mồ côi)
function para(children, opts = {}) {
  // [v9.4] GUARD CHỐNG ĐOẠN LỒNG ĐOẠN — sự cố B09 ngày 24/07/2026.
  // Schema OOXML CẤM <w:p> chứa <w:p>. Trình kiểm XML thấy hợp lệ (thẻ cân đối)
  // nên mọi checklist đều báo OK, nhưng Word từ chối mở file. Bài B09 dính 75 chỗ,
  // mất 2 giờ dò không ra.
  // Nguyên nhân luôn là quên spread khi hàm trả về MẢNG Paragraph:
  //     children.push(H.para(H.loiGiai({...})))     ← SAI
  //     children.push(...H.loiGiai({...}))          ← ĐÚNG
  const ds = Array.isArray(children) ? children : [children];
  const viTri = [];
  ds.forEach((c, i) => { if (c instanceof Paragraph) viTri.push(i); });
  if (viTri.length) {
    throw new Error(
      `[LỖI CẤU TRÚC] para(): phần tử thứ ${viTri.join(", ")} là Paragraph — ` +
      `schema OOXML CẤM đoạn văn lồng trong đoạn văn, Word sẽ TỪ CHỐI MỞ FILE.\n` +
      `   Nguyên nhân thường gặp: quên dấu ... khi hàm trả về mảng Paragraph.\n` +
      `   SAI:   children.push(H.para(H.loiGiai({...})))\n` +
      `   ĐÚNG:  children.push(...H.loiGiai({...}))\n` +
      `   Các hàm trả về MẢNG (phải spread): loiGiai, viDu, viDuLyThuyet, mucTieu,\n` +
      `   baiTapTaiLop, tuLuanBTVN, saiLamThuongGap, ghiNhoNhanh, nhanDang,\n` +
      `   phuongPhapGiai, dangToanDayDu, tenBaiHoc, cauTracNghiem, traLoiNgan, hinhVe.`
    );
  }
  return new Paragraph({
    alignment: opts.justify ? AlignmentType.JUSTIFIED : (opts.align || AlignmentType.LEFT),
    spacing: { before: opts.before ?? 0, after: opts.after ?? 0, line: 260 },
    indent: opts.indent || {},
    keepLines: opts.keepLines || false,
    keepNext: opts.keepNext || false,
    children: Array.isArray(children) ? children : [children],
  });
}

/**
 * Chuẩn hóa cách viết hoa/thường của 1 chuỗi về dạng "Sentence case":
 * chỉ viết hoa chữ cái đầu mỗi câu (câu phân cách bằng dấu "."), phần
 * còn lại viết thường — bất kể chuỗi gốc là IN HOA, chữ thường hay hỗn hợp.
 * Dùng cho header (không dùng cho tiêu đề bài học — tiêu đề vẫn IN HOA
 * toàn bộ theo Hiến Pháp Phần II, mục Hệ thống Tiêu đề).
 * @param {string} str
 * @returns {string}
 */
function chuanHoaCauChu(str) {
  if (!str) return str;
  return str
    .toLowerCase()
    .split(".")
    .map(cau => cau.trim())
    .filter(cau => cau.length > 0)
    .map(cau => cau.charAt(0).toUpperCase() + cau.slice(1))
    .join(". ");
}

// ─────────────────────────────────────────────────────────────
// HÀM CHUYỂN ĐỔI NỘI BỘ DÙNG CHUNG — cho phép mọi tham số nội dung
// (cauHoi, dapAn, deBai, cacCau, loiGiaiND...) nhận CẢ string (như cũ)
// LẪN mảng trộn text/công thức, ví dụ: ["Tính ", H.luyThua(2,3), " ="]
// KHÔNG cần đổi cách gọi cũ — string vẫn hoạt động y hệt trước giờ.
// ─────────────────────────────────────────────────────────────
/**
 * @param {string|Array} input - string thường, hoặc mảng gồm string xen
 *   TextRun/Math (kết quả của run()/luyThua()/phanSo()...)
 * @returns {TextRun[]|Math[]} mảng inline sẵn sàng đưa vào children của Paragraph
 */
function toInline(input, opts = {}) {
  if (input === undefined || input === null) return [];
  if (Array.isArray(input)) {
    return input.map(item => (typeof item === "string" ? run(item, opts) : item));
  }
  if (typeof input === "string") return [run(input, opts)];
  return [input]; // đã là 1 TextRun/Math object sẵn
}

// Ước lượng độ dài hiển thị — dùng để quyết định xếp cột/xuống hàng
// (công thức Math không có .length nên tính tượng trưng 3 ký tự)
function approxLen(item) {
  if (typeof item === "string") return item.length;
  if (Array.isArray(item)) return item.reduce((acc, x) => acc + approxLen(x), 0);
  return 3;
}

// Dựng nhanh 1 Paragraph từ nội dung string|mảng trộn — dùng nội bộ
function paraInline(input, opts = {}) {
  return para(toInline(input, { size: opts.size || SZ_CONTENT }), opts);
}

// Ngưỡng ước lượng ký tự/dòng để tự động gộp các "ý" ngắn lại 1 dòng
// (cỡ 13pt, A4, lề 1.3cm — dùng cho loiGiai() phần cacBuoc).
const NGUONG_GOP_DONG_BUOC = 72;

function toParts(item) {
  return Array.isArray(item) ? item : [item];
}

/**
 * Tự động gộp mảng các "ý" lý luận ngắn (đã có sẵn từ nối ⟺/nên/suy ra do
 * AI Soạn tự viết trong từng ý) thành các dòng vừa khít trang — gộp liền
 * nếu còn dưới ngưỡng, tự ngắt dòng mới nếu vượt. Không tự chèn từ nối
 * (đó là việc của AI Soạn, tùy ngữ nghĩa) — hàm chỉ quyết định NGẮT Ở ĐÂU.
 * @param {Array<string|Array>} items
 * @param {number} [nguong=NGUONG_GOP_DONG_BUOC]
 * @returns {Array<Array>} mảng các "dòng", mỗi dòng là mảng-trộn sẵn sàng cho paraInline
 */
// A3 v9.0: nhận ⇒ (U+21D2) như từ nối — không ngắt dòng ngay TRƯỚC ⇒
// (ký hiệu suy ra/tương đương thường đứng đầu ý tiếp theo, ngắt trước nó
//  tạo dòng kết thúc bằng khoảng trắng → xấu. Ngắt SAU ⇒ thì hợp lý hơn.)
function gopDongTuDo(items, nguong = NGUONG_GOP_DONG_BUOC) {
  const dong = [];
  let cur = [];
  let curLen = 0;
  items.forEach((item, idx) => {
    const len = approxLen(item);
    // Không ngắt dòng ngay trước ký hiệu ⇒ — để nó dính với ý trước
    const isArrow = typeof item === "string" && item.trimStart().startsWith("\u21D2");
    if (cur.length > 0 && !isArrow && curLen + len + 1 > nguong) {
      dong.push(cur);
      cur = [];
      curLen = 0;
    }
    if (cur.length > 0) { cur.push(" "); curLen += 1; }
    cur.push(...toParts(item));
    curLen += len;
  });
  if (cur.length > 0) dong.push(cur);
  return dong;
}

// A2 v9.0: tab stop thật chia đều 18.4cm (TOTAL_W tính theo twip = 10432 ≈ 18.4cm)
// Thay khoảng trắng giả bằng \t + tabStops chuẩn — căn đều bất kể font/zoom
function tabLine(parts, opts = {}) {
  // parts: mảng string HOẶC mảng-trộn-inline, cách đều bằng tab stop thật
  // — dùng cho A,B,C,D hoặc a) b) c)... (hỗ trợ cả công thức toán)
  const n = parts.length;
  // [v9.4] Bề ngang khả dụng: mặc định cả vùng chữ 18.4cm; nếu dòng nằm cạnh
  // hình neo trái thì phải trừ đi bề rộng hình + khe, nếu không cột đầu của
  // dãy a) b) c) d) sẽ rơi vào vùng hình (HP V10.4 Điều 18.3, ghi chú kỹ thuật).
  // Người gọi truyền opts.hinhTraiCm; template tự tính, AI Soạn không phải biết.
  const truCm = opts.hinhTraiCm ? opts.hinhTraiCm + 0.3 : 0;
  const beNgang = Math.max(
    Math.round(TOTAL_W * 0.35),                       // sàn an toàn
    Math.round(TOTAL_W * (1 - truCm / 18.4))
  );
  const lech = TOTAL_W - beNgang;                     // dịch phải khi né hình
  const tabStops = [];
  for (let i = 1; i < n; i++) {
    tabStops.push({ type: "left", position: lech + Math.round(beNgang * i / n) });
  }
  const children = [];
  parts.forEach((p, i) => {
    if (i > 0) children.push(new TextRun({ text: "\t", font: TNR, size: opts.size || SZ_CONTENT }));
    children.push(...toInline(p, { size: opts.size || SZ_CONTENT }));
  });
  return new Paragraph({
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { before: opts.before ?? 0, after: opts.after ?? 0, line: 260 },
    indent: opts.indent || {},
    tabStops,
    children,
  });
}

// ═════════════════════════════════════════════════════════════
// 1. TÊN BÀI HỌC (không đánh số mục)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soBai   - số thứ tự bài
 * @param {string} p.tenBai  - tên bài (KHÔNG cần viết hoa, hàm tự IN HOA)
 * @param {number} p.tiet    - số tiết
 * @param {string} p.sgkTr   - "5–8"
 * @param {string} p.sbtTr   - "5–6"
 * @param {string} p.ma      - mã định danh, ví dụ "GT_CH01_B01"
 */
function tenBaiHoc({ soBai, tenBai, tiet, sgkTr, sbtTr, ma }) {
  return [
    para([run(`BÀI ${soBai}. ${tenBai.toUpperCase()}`, { bold: true, size: SZ_TITLE_BAI })],
      { align: AlignmentType.CENTER, before: 40, after: 0 }),
    para([
      run(`Thời lượng: ${tiet} tiết  |  SGK trang ${sgkTr}  |  SBT trang ${sbtTr}  |  Mã: `,
        { italic: true, size: SZ_SMALL }),
      run(ma, { italic: true, bold: true, size: SZ_SMALL }),
    ], { align: AlignmentType.CENTER, before: 0, after: 20 }),
  ];
}

// ═════════════════════════════════════════════════════════════
// 2. MỤC TIÊU (mục ①)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {string} p.kienThuc
 * @param {string} p.kyNang
 * @param {string} p.nangLuc
 */
function mucTieu({ kienThuc, kyNang, nangLuc }) {
  return [
    tieuDeMucChinh("①", "Mục tiêu"),
    para([run("• Kiến thức: ", { bold: true, size: SZ_CONTENT }), run(kienThuc, { size: SZ_CONTENT })],
      { before: 0, after: 0, justify: true }),
    para([run("• Kỹ năng: ", { bold: true, size: SZ_CONTENT }), run(kyNang, { size: SZ_CONTENT })],
      { before: 0, after: 0, justify: true }),
    para([run("• Năng lực: ", { bold: true, size: SZ_CONTENT }), run(nangLuc, { size: SZ_CONTENT })],
      { before: 0, after: 20, justify: true }),
  ];
}

// ═════════════════════════════════════════════════════════════
// 3. TIÊU ĐỀ MỤC LÝ THUYẾT (dùng trong Kiến thức trọng tâm)
// ═════════════════════════════════════════════════════════════
function tieuDeMuc(stt, ten) {
  return para([run(`${stt}. ${ten}`, { bold: true, underline: true, size: SZ_CONTENT })],
    { before: THO_RONG, after: 40, keepNext: true });
}

// ═════════════════════════════════════════════════════════════
// 3b. TIÊU ĐỀ MỤC CẤP 1 (①–⑤) — chuẩn CHUNG mọi môn (Chuẩn trình bày)
//   Kiểu chốt 12/08/2026: số + TÊN IN HOA + đậm + gạch chân + KHÔNG dấu chấm.
//   Dùng cho 5 mục xương sống của bài: ① Mục tiêu · ② Kiến thức trọng tâm ·
//   ③ Các dạng toán · ④ Bài tập tại lớp · ⑤ Bài tập về nhà.
//   (tieuDeMuc — có chấm, title-case — HẠ VAI xuống tiêu đề CON trong một mục.)
// ═════════════════════════════════════════════════════════════
function tieuDeMucChinh(stt, ten) {
  return para([run(`${stt} ${String(ten).toUpperCase()}`, { bold: true, underline: true, size: SZ_CONTENT })],
    { before: THO_RONG, after: 40, keepNext: true });
}

// ═════════════════════════════════════════════════════════════
// 4. LÝ THUYẾT — 1 dòng nội dung thường
// ═════════════════════════════════════════════════════════════
function lyThuyet(text) {
  _guardKyHieuGoc(text, "lyThuyet");
  return para([run(text, { size: SZ_CONTENT })], { before: 0, after: 0, justify: true });
}

// ═════════════════════════════════════════════════════════════
// 5. VÍ DỤ / VÍ DỤ MINH HỌA
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {string} p.nhan       - "Ví dụ" hoặc "Ví dụ minh họa"
 * @param {string|Array} p.deBai - nội dung đề (nếu 1 câu). String hoặc mảng
 *   trộn text/công thức, ví dụ: ["Tính ", H.luyThua(2,3), " = ?"]. Bỏ trống nếu dùng cacCau.
 * @param {Array<string|Array>} [p.cacCau] - mảng câu a), b), c)... — mỗi phần tử
 *   là string HOẶC mảng trộn text/công thức
 * @param {string} [p.thamChieu]- "SGK tr.5 — Ví dụ 1" (để trống nếu tự soạn)
 */
// [v10.10] Đáp án cho Ví dụ mục ② (bản đầy đủ). dapAn: string | mảng (khớp a,b,c).
function _dapAnViDu(dapAn) {
  if (!dapAn) return [];
  const nhan = "abcdefgh".split("");
  let noi;
  if (Array.isArray(dapAn)) {
    noi = [];
    dapAn.forEach((d, i) => {
      if (i) noi.push(run("   ", { size: SZ_CONTENT }));
      noi.push(run(`${nhan[i]}) `, { bold: true, size: SZ_CONTENT }));
      noi.push(...toInline(d, { size: SZ_CONTENT }));
    });
  } else {
    noi = toInline(dapAn, { size: SZ_CONTENT });
  }
  return [ paraInline([ run("Trả lời: ", { bold: true, italic: true, size: SZ_CONTENT }), ...noi ],
    { before: 0, after: 0 }) ];
}

function viDu({ nhan = "Ví dụ", deBai, cacCau, dapAn, thamChieu, coHinh, hinhBenTrai, hinhBenPhai }) {
  thamChieu = _locNguon(thamChieu);
  _guardND(deBai, "viDu");
  _guardArr(cacCau, "viDu");
  const _hinh = hinhBenPhai || hinhBenTrai;   // hinhBenPhai = tên CHÍNH (neo phải); hinhBenTrai = bí danh cũ (v9.4)
  if (_canHinh(deBai, cacCau) && !coHinh && !_hinh) {
    const ds = _extractText(deBai) + " " + _extractText(cacCau);
    throw new Error(`\n[LỖI THIẾU HÌNH] viDu "${nhan}" cần hình vẽ.\n  Đề: "${ds.substring(0,80)}..."\n→ Mục ③ trở xuống: hinhBenPhai:{imageBuffer,...} (NEO PHẢI, chữ wrap TRÁI), hình nướng nhãn qua ve(nhan="Hình N"). Mục ② & Phần II: coHinh:[...H.hinhVe(...,chuThich:"Hình N. ...")] (dòng riêng căn giữa)`);
  }
  const out = [];
  // HP V10.3 Điều 18: hình nhỏ (<10cm) + nội dung dài → TEXT BOX neo phải, chữ wrap trái.
  // hinhBenPhai tự đặt hình vào ĐẦU paragraph đề bài (mặc định trình bày đúng chuẩn).
  if (_hinh && _hinh.imageBuffer) {
    const anh = hinhVeTextBox(_hinh);   // tự chặn nếu cột chữ còn < 9cm
    const deInline = deBai
      ? [run(`${nhan}: `, { bold: true, size: SZ_CONTENT }), ...toInline(deBai, { size: SZ_CONTENT })]
      : [run(`${nhan}:`, { bold: true, size: SZ_CONTENT })];
    out.push(paraCoHinhPhai(anh, deInline, { before: THO_VUA, after: 0, justify: true }));
    if (thamChieu) {
      out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })], { before: 0, after: 6 }));
    }
    if (cacCau && cacCau.length) out.push(...layoutCauHoi(cacCau, { dai: true }));
    out.push(..._dapAnViDu(dapAn));
    return out;
  }
  if (deBai) {
    out.push(para([run(`${nhan}: `, { bold: true, size: SZ_CONTENT }), ...toInline(deBai, { size: SZ_CONTENT })],
      { before: THO_VUA, after: 0, justify: true }));
  } else {
    out.push(para([run(`${nhan}:`, { bold: true, size: SZ_CONTENT })], { before: THO_VUA, after: 0 }));
  }
  if (thamChieu) {
    out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { before: 0, after: 6 }));
  }
  _appendHinh(out, coHinh, "coHinh");
  if (cacCau && cacCau.length) {
    out.push(...layoutCauHoi(cacCau));
  }
  out.push(..._dapAnViDu(dapAn));
  return out;
}

/**
 * viDuLyThuyet() — VÍ DỤ TRONG MỤC ② KIẾN THỨC TRỌNG TÂM
 *
 * HP V10.3 Điều 18.1: mọi hình trong mục ② LUÔN đặt DÒNG RIÊNG CĂN GIỮA,
 * không phụ thuộc kích thước. Lý do: hình lý thuyết là hình mẫu GV chỉ trên
 * lớp, HS xem lại nhiều lần — cần đứng độc lập, không chen chữ bên cạnh.
 *
 * Hàm này CỐ Ý không nhận hinhBenPhai — dùng đúng hàm là tự đúng chuẩn,
 * AI Soạn không thể lỡ đặt text box ở mục ②.
 *
 * Ở mục ③ trở xuống → dùng viDu() với hinhBenPhai (Điều 18.2).
 */
/**
 * [v9.9→HP V11] viDuLyThuyet() — VÍ DỤ MỤC ② KIẾN THỨC TRỌNG TÂM.
 *
 * HP V11 Điều 18.1 KHÔI PHỤC: mọi hình trong mục ② LUÔN đặt DÒNG RIÊNG CĂN GIỮA,
 * không phụ thuộc kích thước (hình lý thuyết là hình mẫu, HS xem lại nhiều lần).
 * Vì vậy hàm CỐ Ý KHÔNG nhận hinhBenPhai/hinhBenTrai — truyền vào là CHẶN, buộc
 * dùng coHinh:[...H.hinhVe(...)] (dòng riêng căn giữa). Dùng đúng hàm là tự đúng chuẩn.
 * (Bí danh-viDu của v9.4 đã bị thu hồi khi HP V11 khôi phục Điều 18.1.)
 */
function viDuLyThuyet(p = {}) {
  if (p.hinhBenPhai || p.hinhBenTrai)
    throw new Error('[viDuLyThuyet] Mục ② KHÔNG được neo hình bên phải (HP V11 Điều 18.1). '
      + 'Hình mục ② phải dòng riêng căn giữa — dùng coHinh:[...H.hinhVe(...)].');
  // [v10.11] Chặn "Ví dụ" RỖNG: chỉ có hình, không đề & không câu hỏi → đó là HÌNH MINH HOẠ
  //   lý thuyết (Hình 8.X đi kèm định nghĩa), KHÔNG phải Ví dụ. Nhãn "Ví dụ:" khi đó là THỪA.
  const _coCau = p.cacCau && p.cacCau.length;
  if (!p.deBai && !_coCau)
    throw new Error('[viDuLyThuyet] "Ví dụ" chỉ có HÌNH, không đề & không câu hỏi → đây là HÌNH '
      + 'MINH HOẠ lý thuyết, không phải Ví dụ (nhãn "Ví dụ:" thừa). Chèn THẲNG hình căn giữa: '
      + 'P(...H.hinhVe({ imageBuffer, chuThich:"Hình 8.X" })) — KHÔNG bọc viDuLyThuyet. '
      + 'Chỉ dùng viDuLyThuyet khi có đề/câu hỏi "?" (kèm dapAn).');
  return viDu({ nhan: p.nhan || "Ví dụ", deBai: p.deBai, cacCau: p.cacCau, dapAn: p.dapAn,
                thamChieu: p.thamChieu, coHinh: p.coHinh });
}

// ═════════════════════════════════════════════════════════════
// 5b. ĐÃ XÓA (v9.0) — viDuCoHinhBenCanh / baiTapTaiLopCoHinhBenCanh /
//     tuLuanBTVNCoHinhBenCanh / _khoiBaiTapCoHinh / _oHinhBenCanh / _NOBORDER
//     HP V10 Điều 18: CẤM dùng bảng 2 cột cho khối đề-hình.
//     Dùng hinhVe() dòng riêng căn giữa thay thế.
// ═════════════════════════════════════════════════════════════
//     Cột trái: đề bài + lời giải  |  Cột phải: hình + chú thích
//     Dùng khi hình cần nằm bên phải, không chiếm dòng riêng.
//
//  Cách dùng:
//    ...H.viDuCoHinhBenCanh({
// (đã xóa — xem ghi chú mục 5b ở trên)

// ═════════════════════════════════════════════════════════════
// 6. LAYOUT CÂU HỎI a) b) c) d)... — tự động chọn cách xếp cột
//    theo đúng quy tắc CS2627 (không kẻ bảng, dùng tab)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Array<string|Array>} cauArr - mảng nội dung từng câu — mỗi phần tử
 *   là string (như cũ) HOẶC mảng trộn text/công thức, ví dụ:
 *   ["4 □ M", ["Tính ", H.luyThua(2,3), " = ?"]]
 *   Hàm tự thêm nhãn a) b) c)... theo thứ tự.
 * @param {Object} [opts]
 * @param {boolean} [opts.dai] - true nếu câu dài (>1 dòng) → luôn xuống hàng riêng
 */
/**
 * [v9.4] Lột nhãn thứ tự mà AI Soạn đã gõ sẵn ở đầu nội dung.
 *
 * Sự cố B09 (24/07/2026): file in ra "a) a) Tìm một cặp góc so le trong."
 * Nguyên nhân: layoutCauHoi() và cauTracNghiem() TỰ đánh nhãn, nhưng AI Soạn
 * cũng gõ nhãn trong nội dung — hai bên cùng làm một việc nên nhãn nhân đôi.
 *
 * Template tự lột thay vì chặn build: ý định rõ ràng, không có gì mơ hồ để hỏi.
 * Có cảnh báo ra console để AI Soạn biết mà bỏ thói quen gõ tay.
 *
 * @param {string|Array} item  nội dung 1 câu (string hoặc mảng trộn)
 * @param {RegExp} mau         mẫu nhãn cần lột
 * @param {string} ten         tên hàm gọi, dùng cho thông báo
 */
function _lotNhanTrung(item, mau, ten) {
  const lot = (s) => {
    if (typeof s !== "string") return s;
    const sach = s.replace(mau, "");
    if (sach !== s) {
      console.warn(
        `[${ten}] Đã tự bỏ nhãn gõ tay ở đầu câu: "${s.slice(0, 28)}…" — ` +
        `template tự đánh nhãn, AI Soạn KHÔNG cần gõ.`
      );
    }
    return sach;
  };
  if (Array.isArray(item)) {
    const ra = item.slice();
    for (let i = 0; i < ra.length; i++) {
      if (typeof ra[i] === "string") {
        if (ra[i].trim() === "") continue;   // bỏ qua phần tử rỗng, xét phần tử sau
        ra[i] = lot(ra[i]);
        break;
      }
      break;                                  // gặp công thức trước chữ → không có nhãn
    }
    return ra;
  }
  return lot(item);
}

// Nhãn câu hỏi phụ: "a)" "b." "c )" — chữ thường a..h
const _MAU_NHAN_CAU = /^\s*[a-h]\s*[).．.]\s*/;
// Nhãn đáp án trắc nghiệm: "A." "B)" "C ." — chữ HOA A..D
const _MAU_NHAN_DAPAN = /^\s*[A-D]\s*[).．.]\s*/;

function layoutCauHoi(cauArr, opts = {}) {
  const nhan = "abcdefgh".split("");
  // Mỗi item vẫn là string (nếu c là string) hoặc mảng [nhãn, ...nội dung trộn]
  const items = cauArr.map((c, i) => {
    const label = run(`${nhan[i]}) `, { bold: true, size: SZ_CONTENT });
    const sach = _lotNhanTrung(c, _MAU_NHAN_CAU, "layoutCauHoi");
    return Array.isArray(sach) ? [label, ...sach] : [label, sach];
  });
  const out = [];
  const lens = items.map(it => approxLen(it));
  const max = lens.length ? Math.max(...lens) : 0;
  const COT2 = 44, COT3 = 29;   // [v10.10] ước lượng ký tự vừa 1 cột khi chia 2 / 3 cột
  const xuongHang = () => items.forEach(it => out.push(paraInline(it, { before: 0, after: 0 })));

  if (opts.dai) { xuongHang(); return out; }              // ép dài → mỗi câu 1 dòng
  if (items.length === 1) { out.push(paraInline(items[0], { before: 0, after: 0 })); return out; }
  // 1 DÒNG DUY NHẤT nếu mọi câu vừa cột; không thì xuống hàng (thầy: "một dòng nếu được, còn không thì…")
  if (items.length === 2 && max <= COT2) { out.push(tabLine(items)); return out; }
  if (items.length === 3 && max <= COT3) { out.push(tabLine(items)); return out; }
  if (items.length === 4 && max <= COT2) {
    out.push(tabLine([items[0], items[1]]));
    out.push(tabLine([items[2], items[3]]));
    return out;
  }
  xuongHang();
  return out;
}

// ═════════════════════════════════════════════════════════════
// 7. LỜI GIẢI
// ═════════════════════════════════════════════════════════════
/**
 * @param {string|Array|Object} noiDung
 *
 * CHẾ ĐỘ CŨ (vẫn hoạt động y hệt trước giờ — KHÔNG phá bài đã soạn):
 *   loiGiai("126 = 2×63 = ... Vậy 126 = 2×3²×7.")
 *   loiGiai(["a) ...", "b) ..."])
 *
 * CHẾ ĐỘ MỚI (khuyến khích dùng từ nay — chuẩn đồng nhất kết luận):
 *   loiGiai({ cacBuoc: "126 = 2×63 = 2×3×21 = 2×3×3×7", ketLuan: "126 = 2×3²×7." })
 *   loiGiai({ cacBuoc: ["5x + 6y = 4", "⟺ 20x + 24y = 16", "⟺ 24y − (−45y) = 16 − 85"], ketLuan: "y = −1." })
 *
 *   - cacBuoc dạng STRING: AI Soạn tự viết liền 1 chuỗi (chuỗi đẳng thức cho
 *     Số học/Đại số) — dùng khi cả bài ngắn, viết 1 mạch tự nhiên hơn.
 *   - cacBuoc dạng MẢNG: mỗi phần tử là 1 "ý" lý luận NGẮN, AI Soạn tự chèn
 *     từ nối phù hợp ở ĐẦU mỗi ý (trừ ý đầu tiên) — dùng "⟺" khi nối 2 biểu
 *     thức/phương trình tương đương nhau, dùng "nên"/"suy ra" khi nối 2 sự
 *     kiện/kết luận khác bản chất (thường gặp ở Hình học, chứng minh).
 *     Hàm TỰ ĐỘNG gộp các ý liền nhau nếu vừa 1 dòng, TỰ NGẮT dòng mới nếu
 *     vượt ngưỡng ~72 ký tự — AI Soạn KHÔNG cần tự đoán độ dài/ngắt dòng.
 *     Nếu bài có HỆ PHƯƠNG TRÌNH, chèn thẳng paraHePhuongTrinh([...]) làm
 *     1 phần tử trong mảng — hàm tự nhận diện, KHÔNG gộp nó vào dòng khác.
 *   - ketLuan: BẮT BUỘC nên có — hàm TỰ ĐỘNG in đậm, tách dòng riêng, và tự
 *     thêm chữ "Vậy " ở đầu nếu AI Soạn quên gõ. Đây là phần học sinh nhìn
 *     lên TV phải thấy NGAY, không cần đọc lại từ đầu.
 */
function loiGiai(noiDung) {
  if (typeof noiDung === "string") _guardKyHieuGoc(noiDung, "loiGiai");
  if (noiDung && typeof noiDung === "object" && !Array.isArray(noiDung)) {
    _guardND(noiDung.cacBuoc, "loiGiai");
    _guardArr(Array.isArray(noiDung.cacBuoc) ? noiDung.cacBuoc : [], "loiGiai");
    _guardND(noiDung.ketLuan, "loiGiai");
    // Guard chuThich hình lời giải
    if (noiDung.hinhLoiGiai?.chuThich) _guardKyHieuGoc(noiDung.hinhLoiGiai.chuThich, "loiGiai hinhLoiGiai.chuThich");
  }
  // [v9.9] Hình lời giải cũng NEO PHẢI, chữ wrap trái — như hình đề (yêu cầu 08/08).
  //   AI Soạn nướng "Hình N" vào ảnh qua ve(nhan="Hình N"); template KHÔNG in chú thích text.
  let _anhLGFloat = null;
  if (noiDung && typeof noiDung === "object" && !Array.isArray(noiDung) && noiDung.hinhLoiGiai) {
    const hlg = noiDung.hinhLoiGiai;
    _anhLGFloat = hinhVeTextBox({ imageBuffer: hlg.imageBuffer, rongCm: hlg.rongCm ?? 6, tiLeGoc: hlg.tiLeGoc });
  }
  const _lgHeader = [run("Lời giải:", { bold: true, italic: true, size: SZ_CONTENT })];
  if (_anhLGFloat) _lgHeader.unshift(_anhLGFloat);   // float neo phải, chữ lời giải wrap trái
  const out = [para(_lgHeader, { before: THO_VUA, after: 0, keepNext: true })];

  // ── Chế độ MỚI: object { cacBuoc, ketLuan, hinhLoiGiai } ──
  if (noiDung && typeof noiDung === "object" && !Array.isArray(noiDung)
      && ("cacBuoc" in noiDung || "ketLuan" in noiDung)) {
    const { cacBuoc, ketLuan } = noiDung;   // hinhLoiGiai đã dựng float ở trên
    if (cacBuoc !== undefined && cacBuoc !== null && cacBuoc !== "") {
      if (Array.isArray(cacBuoc)) {
        // Tách riêng các khối đã dựng sẵn (Paragraph — vd. paraHePhuongTrinh())
        // khỏi các "ý" ngắn cần tự gộp/ngắt dòng bằng gopDongTuDo.
        let buffer = [];
        const flushBuffer = () => {
          if (buffer.length) {
            gopDongTuDo(buffer).forEach(dong => out.push(paraInline(dong, { before: 0, after: 0, justify: true })));
            buffer = [];
          }
        };
        cacBuoc.forEach(item => {
          if (item instanceof Paragraph) {
            flushBuffer();
            out.push(item);
          } else {
            buffer.push(item);
          }
        });
        flushBuffer();
      } else {
        out.push(paraInline(cacBuoc, { before: 0, after: 0, justify: true }));
      }
    }
    if (ketLuan !== undefined && ketLuan !== null && ketLuan !== "") {
      const firstStr = typeof ketLuan === "string" ? ketLuan
        : (Array.isArray(ketLuan) && typeof ketLuan[0] === "string" ? ketLuan[0] : "");
      const daCoVay = /^vậy\b/i.test(firstStr.trim());
      const noiDungKetLuan = toInline(ketLuan, { bold: true, size: SZ_CONTENT });
      const children = daCoVay ? noiDungKetLuan : [run("Vậy ", { bold: true, size: SZ_CONTENT }), ...noiDungKetLuan];
      out.push(para(children, { before: THO_HEP, after: 0, justify: true }));
    }
    return out;
  }

  // ── Chế độ CŨ — giữ nguyên 100%, không đổi hành vi ──
  if (Array.isArray(noiDung)) {
    if (noiDung.length === 2) {
      out.push(tabLine(noiDung));
    } else {
      noiDung.forEach(nd => out.push(paraInline(nd, { before: 0, after: 0 })));
    }
  } else {
    out.push(paraInline(noiDung, { before: 0, after: 0 }));
  }
  return out;
}

// ═════════════════════════════════════════════════════════════
// 8. SAI LẦM THƯỜNG GẶP
// ═════════════════════════════════════════════════════════════
/**
 * @param {Array<{sai:string, dung:string}>} loiArr - tối đa 3 lỗi
 */
function saiLamThuongGap(loiArr, opts = {}) {
  if (!Array.isArray(loiArr) || loiArr.length === 0)
    throw new Error("saiLamThuongGap(): cần mảng ít nhất 1 lỗi dạng {sai, dung}.");

  // [v9.4] GUARD 2 DÒNG — HP V10.4 Điều 23.2
  // Trước v9.4: slice(0,3) âm thầm cắt lỗi thứ 4 → AI Soạn không hề biết.
  // Nay: đếm số dòng THỰC SỰ in ra, vượt 2 thì chặn build.
  // [v9.6] sai/dung nhận string HOẶC mảng trộn (chèn phanSo/luyThua). Đếm dòng qua _extractText.
  const dongMoiLoi = loiArr.map(l =>
    _soDongUocTinh(`✗ Sai: ${_extractText(l.sai)}  →  ✓ Đúng: ${_extractText(l.dung)}`));
  const tongDong = dongMoiLoi.reduce((a, b) => a + b, 0);
  if (tongDong > 2) {
    const chiTiet = loiArr.map((l, i) =>
      `   ${i + 1}. ${dongMoiLoi[i]} dòng (${`✗ Sai: ${_extractText(l.sai)}  →  ✓ Đúng: ${_extractText(l.dung)}`.length} ký tự)`
    ).join("\n");
    throw new Error(
      `saiLamThuongGap(): khối này in ra ${tongDong} dòng, TỐI ĐA cho phép 2 (HP V10.4 Điều 23.2).\n${chiTiet}\n` +
      `   Cách sửa: rút gọn chữ đệm, hoặc gộp 2 lỗi cùng bản chất vào 1 mục, ` +
      `hoặc bỏ lỗi ít gặp nhất. Mỗi mục nên dưới ${CHARS_PER_LINE} ký tự.`
    );
  }

  const out = [para([run("Sai lầm thường gặp:", { bold: true, size: SZ_CONTENT })],
    { before: opts.beforeFirst ?? THO_VUA, after: 0 })];
  loiArr.forEach(l => {
    out.push(para([
      run("✗ Sai: ", { size: SZ_CONTENT }), ...toInline(l.sai, { size: SZ_CONTENT }),
      run("  →  ✓ Đúng: ", { size: SZ_CONTENT }), ...toInline(l.dung, { size: SZ_CONTENT }),
    ], { before: 0, after: 4, justify: true }));
  });
  return out;
}

// ═════════════════════════════════════════════════════════════
// 9. GHI NHỚ NHANH
// ═════════════════════════════════════════════════════════════
/**
 * @param {string[]} dongArr - tối đa 3 dòng
 */
function ghiNhoNhanh(dongArr, opts = {}) {
  if (!Array.isArray(dongArr) || dongArr.length === 0)
    throw new Error("ghiNhoNhanh(): cần mảng ít nhất 1 ý.");

  // [v9.4] GUARD 2 DÒNG — HP V10.4 Điều 23.2 (và Điều 22.7 cho "Ghi nhớ" mục ②)
  // [v9.6] mỗi ý nhận string HOẶC mảng trộn. Đếm dòng qua _extractText.
  const dongMoiY = dongArr.map(d => _soDongUocTinh(`• ${_extractText(d)}`));
  const tongDong = dongMoiY.reduce((a, b) => a + b, 0);
  const nhan = opts.nhan || "Ghi nhớ nhanh";
  if (tongDong > 2) {
    const chiTiet = dongArr.map((d, i) =>
      `   ${i + 1}. ${dongMoiY[i]} dòng (${_extractText(d).length} ký tự)`).join("\n");
    throw new Error(
      `ghiNhoNhanh(): khối này in ra ${tongDong} dòng, TỐI ĐA cho phép 2 (HP V10.4 Điều 23.2).\n${chiTiet}\n` +
      `   Cách sửa: gộp các ý ngắn vào cùng 1 dòng, ngăn bằng dấu chấm phẩy. ` +
      `Mỗi dòng nên dưới ${CHARS_PER_LINE} ký tự.`
    );
  }

  const out = [para([run(`${nhan}:`, { bold: true, size: SZ_CONTENT })], { before: THO_VUA, after: 0, keepNext: true })];
  dongArr.forEach((d, i, arr) => {
    const isLast = i === arr.length - 1;
    out.push(para([run("• ", { size: SZ_CONTENT }), ...toInline(d, { size: SZ_CONTENT })], { before: 0, after: isLast ? 16 : 0, justify: true }));
  });
  return out;
}

// ═════════════════════════════════════════════════════════════
// 10. DẠNG TOÁN — tiêu đề + Nhận dạng + Phương pháp giải
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soDang
 * @param {string} p.tenDang
 * @param {string} p.mucDo   - "NB"|"TH"|"VD"|"VDC"|"NC"
 * @param {string} p.ma      - mã định danh, ví dụ "GT_CH01_B01_D1"
 * @param {string[]} p.nhanDang - mảng ý (mỗi phần tử 1 dòng, hàm tự thêm dấu |)
 * @param {string[]} p.phuongPhap - mảng bước (mỗi phần tử 1 dòng, hàm tự thêm dấu –)
 */
function tieuDeDang({ soDang, tenDang, ma }) {
  // [v9.6] A.1: tên Dạng KHÔNG gắn nhãn mức độ; mã định vị in xám cuối tên. keepNext chống mồ côi.
  return [
    new Paragraph({
      spacing: { before: THO_RONG, after: 40, line: 220 },
      keepNext: true,
      children: [
        new TextRun({ text: `Dạng ${soDang}. ${tenDang}`, font: TNR,
          bold: true, underline: { type: UnderlineType.SINGLE }, size: SZ_CONTENT }),
        new TextRun({ text: `  ${ma}`, font: TNR, italic: true, color: C_GRAY, size: SZ_SMALL - 2 }),
      ],
    }),
  ];
}

function nhanDang(yArr) {
  const out = [para([run("Nhận dạng:", { bold: true, size: SZ_CONTENT })], { before: THO_VUA, after: 0 })];
  yArr.forEach(y => out.push(para([run(`▸ ${y}`, { size: SZ_CONTENT })],
    { before: 0, after: 0, indent: { left: 200 }, justify: true })));
  return out;
}

function phuongPhapGiai(buocArr, opts = {}) {
  // [v9.6] opts.nhan để đổi nhãn — A.1 dùng "Phương pháp chung" (đặt SAU lời giải).
  const nhan = opts.nhan || "Phương pháp giải";
  const out = [para([run(`${nhan}:`, { bold: true, size: SZ_CONTENT })], { before: THO_VUA, after: 0, keepNext: true })];
  buocArr.forEach((b, i) => out.push(para([run(`- ${b}`, { size: SZ_CONTENT })],
    { before: 0, after: i === buocArr.length - 1 ? 4 : 0, indent: { left: 200 }, justify: true })));
  return out;
}

// [v9.6] Phân tích — mục A.1 giữa "Bài toán mẫu" và "Lời giải"; gánh luôn việc nhận dạng.
// Nhận string hoặc mảng trộn (chèn phanSo/luyThua). Trả mảng — dùng spread.
function phanTich(noiDung) {
  return [para(
    [run("Phân tích: ", { bold: true, size: SZ_CONTENT }), ...toInline(noiDung, { size: SZ_CONTENT })],
    { before: THO_HEP, after: 0, justify: true }
  )];
}

// [v10.6 Nhóm A] CỬA TỰ BỎ (+cảnh báo) — hình lời giải TRÙNG BYTE hình đề.
//   Quy ước 4 vế (CHUAN_TRINH_BAY §Vị trí hình): hình lời giải CHỈ tách khi KHÁC hình đề
//   (thêm đường phụ/đánh dấu/dựng — style phân biệt: đường phụ đỏ nét đứt, kết quả đỏ liền đậm,
//   chấm đỏ điểm dựng). Trùng byte = không thêm gì → lặp thừa. Máy TỰ BỎ hinhLoiGiai, giữ hình đề
//   (HP Điều 36.1) + cảnh báo để OB dọn nguồn. Máy CHỈ bắt ca TRÙNG HỆT; "khi nào PHẢI tách" là
//   phán đoán OB-QC. Trả về p.viDuLoiGiai đã lọc (bỏ hinhLoiGiai nếu trùng).
function _xuLyTrungHinhLoiGiai(p) {
  const bufDe = p.viDuHinhBenPhai?.imageBuffer || p.viDuHinhBenTrai?.imageBuffer;
  const isObj = p.viDuLoiGiai && typeof p.viDuLoiGiai === "object" && !Array.isArray(p.viDuLoiGiai);
  const bufLG = isObj ? p.viDuLoiGiai.hinhLoiGiai?.imageBuffer : undefined;
  if (Buffer.isBuffer(bufDe) && Buffer.isBuffer(bufLG) && bufDe.equals(bufLG)) {
    console.warn(`[CẢNH BÁO trùng hình] Dạng ${p.soDang ?? "?"}: hình lời giải TRÙNG BYTE hình đề `
      + `— ĐÃ TỰ BỎ hình lời giải, giữ hình đề (HP Điều 36.1). Nếu lời giải CẦN hình riêng, `
      + `thêm yếu tố dựng (đường phụ đỏ nét đứt / kết quả đỏ liền đậm / chấm đỏ) cho khác hình đề.`);
    const { hinhLoiGiai, ...conLai } = p.viDuLoiGiai;   // tự bỏ hinhLoiGiai
    return conLai;
  }
  return p.viDuLoiGiai;
}

// Gộp toàn bộ 1 Dạng toán thành 1 lệnh gọi duy nhất — khuyến khích AI Soạn dùng hàm này
function dangToanDayDu(p) {
  // [v9.6] Dựng theo Chuẩn trình bày A.1: đề mẫu TRƯỚC → phân tích → lời giải →
  // phương pháp chung ĐẶT SAU → sai lầm/ghi nhớ. Bỏ mục "Nhận dạng" riêng (Phân tích gánh).
  // tieuDeDang KHÔNG còn nhận mucDo (tên Dạng không gắn nhãn mức độ).
  // [v10.3] CỬA CHẶN KHUNG A.1 (HP Điều 23.2): mỗi Dạng BẮT BUỘC đủ Sai lầm + Ghi nhớ —
  //   hệ thống hoá, không để soạn viên tự ý bỏ mục ở bài này mà giữ ở bài khác.
  if (!p.saiLamArr || !p.saiLamArr.length)
    throw new Error(`\n[LỖI KHUNG A.1] Dạng ${p.soDang ?? "?"} THIẾU "Sai lầm thường gặp" (saiLamArr).\n`
      + `  HP Điều 23.2 — mỗi Dạng phải ĐỦ khung: Bài toán mẫu → Phân tích → Lời giải → Phương pháp chung → SAI LẦM → GHI NHỚ.\n`
      + `→ Bổ saiLamArr:[{sai,dung}] — lỗi HS THẬT, cốt lõi, ≤ 2 dòng; KHÔNG nhồi cho đủ.`);
  if (!p.ghiNhoArr || !p.ghiNhoArr.length)
    throw new Error(`\n[LỖI KHUNG A.1] Dạng ${p.soDang ?? "?"} THIẾU "Ghi nhớ nhanh" (ghiNhoArr).\n`
      + `  HP Điều 23.2 — mỗi Dạng phải ĐỦ khung (… → Sai lầm → GHI NHỚ).\n`
      + `→ Bổ ghiNhoArr:[...] — ý cốt lõi cần nhớ, ≤ 2 dòng.`);
  let out = [];
  out.push(...tieuDeDang({ soDang: p.soDang, tenDang: p.tenDang, ma: p.ma }));
  out.push(...viDu({ nhan: "Bài toán mẫu", deBai: p.viDuDeBai, cacCau: p.viDuCacCau,
    thamChieu: p.viDuThamChieu, coHinh: p.viDuCoHinh, hinhBenPhai: p.viDuHinhBenPhai || p.viDuHinhBenTrai }));
  if (p.phanTich) out.push(...phanTich(p.phanTich));
  const _viDuLoiGiai = _xuLyTrungHinhLoiGiai(p);   // [v10.6] tự bỏ hình lời giải nếu trùng byte hình đề
  out.push(...loiGiai(_viDuLoiGiai));
  if (p.phuongPhapArr && p.phuongPhapArr.length)
    out.push(...phuongPhapGiai(p.phuongPhapArr, { nhan: "Phương pháp chung" }));
  if (p.saiLamArr && p.saiLamArr.length) out.push(...saiLamThuongGap(p.saiLamArr, { beforeFirst: THO_VUA }));
  if (p.ghiNhoArr && p.ghiNhoArr.length) out.push(...ghiNhoNhanh(p.ghiNhoArr));
  return out;
}

// ═════════════════════════════════════════════════════════════
// 11. BÀI TẬP TẠI LỚP (mục ④, tối đa 4 bài)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soBai
 * @param {string} p.mucDo    - "NB"|"TH"|"VD"|"VDC"
 * @param {string|Array} [p.deBai] - string (như cũ) hoặc mảng trộn text/công thức
 * @param {Array<string|Array>} [p.cacCau] - mảng câu, mỗi phần tử string hoặc mảng trộn
 * @param {string} [p.thamChieu]
 * @param {string|Array} p.loiGiaiND
 */
function baiTapTaiLop({ soBai, mucDo, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai }) {
  thamChieu = _locNguon(thamChieu);
  _guardND(deBai, "baiTapTaiLop");
  _guardArr(cacCau, "baiTapTaiLop");
  const _hinh = hinhBenPhai || hinhBenTrai;   // hinhBenPhai = tên CHÍNH (neo phải); hinhBenTrai = bí danh cũ (v9.4)
  if (_canHinh(deBai, cacCau) && !coHinh && !_hinh) {
    const ds = _extractText(deBai) + " " + _extractText(cacCau);
    throw new Error(`\n[LỖI THIẾU HÌNH] BT tại lớp Bài ${soBai} cần hình.\n  Đề: "${ds.substring(0,100)}..."\n→ Mục ③ trở xuống: hinhBenPhai:{imageBuffer,...} (NEO PHẢI, chữ wrap TRÁI), hình nướng nhãn qua ve(nhan="Hình N"). Mục ② & Phần II: coHinh:[...H.hinhVe(...,chuThich:"Hình N. ...")] (dòng riêng căn giữa)`);
  }
  const out = [];
  const nhanBai = `Bài ${soBai}. (${mucDo}) `;
  // HP V10.3 Điều 18: hình nhỏ + nội dung dài → text box neo phải, chữ wrap trái
  if (_hinh && _hinh.imageBuffer) {
    const anh = hinhVeTextBox(_hinh);
    const deInline = deBai
      ? [run(nhanBai, { bold: true, size: SZ_CONTENT }), ...toInline(deBai, { size: SZ_CONTENT })]
      : [run(`Bài ${soBai}. (${mucDo})`, { bold: true, size: SZ_CONTENT })];
    out.push(paraCoHinhPhai(anh, deInline, { before: THO_VUA, after: 0, justify: true }));
    if (thamChieu) out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })], { before: 0, after: 6 }));
    if (cacCau && cacCau.length) out.push(...layoutCauHoi(cacCau, { dai: true }));
    out.push(...loiGiai(loiGiaiND));
    return out;
  }
  if (deBai) {
    out.push(para([run(nhanBai, { bold: true, size: SZ_CONTENT }),
      ...toInline(deBai, { size: SZ_CONTENT })], { before: THO_VUA, after: 0, justify: true }));
  } else {
    out.push(para([run(`Bài ${soBai}. (${mucDo})`, { bold: true, size: SZ_CONTENT })],
      { before: THO_VUA, after: 0 }));
  }
  if (thamChieu) {
    out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { before: 0, after: 6 }));
  }
  _appendHinh(out, coHinh, "coHinh");
  if (cacCau && cacCau.length) out.push(...layoutCauHoi(cacCau));
  out.push(...loiGiai(loiGiaiND));
  return out;
}

// 11.1. ĐÃ XÓA (v9.0) — baiTapTaiLopCoHinhBenCanh / tuLuanBTVNCoHinhBenCanh
//        HP V10 Điều 18: CẤM bảng 2 cột cho khối đề-hình.
//        Dùng baiTapTaiLop() + coHinh: [...H.hinhVe(...)] thay thế.

// ═════════════════════════════════════════════════════════════
// 12. TRẮC NGHIỆM CHỌN ĐÁP ÁN (dùng chung BTVN Phần I & Đề kiểm tra)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soCau
 * @param {string|Array} p.cauHoi - string (như cũ) hoặc mảng trộn text/công thức
 * @param {Array<string|Array>} p.dapAn - đúng 4 phần tử [A,B,C,D], mỗi phần tử
 *   là string (như cũ) HOẶC mảng trộn text/công thức
 * @param {string} [p.thamChieu] - VD: "SBT Bài 2 câu 2.1" / "Phát triển từ SBT câu 2.1" / "Tự soạn"
 *   (tùy chọn — nếu không truyền, không hiển thị dòng nguồn, giữ nguyên hành vi cũ)
 */
function cauTracNghiem({ soCau, cauHoi, dapAn, thamChieu }) {
  thamChieu = _locNguon(thamChieu);
  if (!Array.isArray(dapAn) || dapAn.length !== 4) {
    throw new Error(`\n[LỖI CÂU TN] Câu ${soCau}: cần đúng 4 đáp án [A,B,C,D]. Hiện có: ${dapAn?.length ?? 0}.`);
  }
  // [v9.6] Chỉ so trùng khi đáp án là STRING THUẦN. Nếu chứa công thức OMML (phanSo/luyThua…),
  // phần chữ rút ra sẽ giống nhau ("x =") gây chặn NHẦM — bỏ guard, để AI QC kiểm tay.
  const coOMML = dapAn.some(d => Array.isArray(d) ? d.some(x => typeof x !== "string") : (typeof d !== "string"));
  const dapAnStr = dapAn.map(d => Array.isArray(d) ? d.filter(x=>typeof x==="string").join("").trim().toLowerCase() : String(d).trim().toLowerCase());
  const textEntries = dapAnStr.filter(s => s.length > 2);
  if (!coOMML && textEntries.length >= 2 && new Set(textEntries).size < textEntries.length) {
    throw new Error(`\n[LỖI CÂU TN] Câu ${soCau}: có đáp án trùng nhau! A="${dapAnStr[0]}" B="${dapAnStr[1]}" C="${dapAnStr[2]}" D="${dapAnStr[3]}"`);
  }
  _guardND(cauHoi, "cauTracNghiem");
  const out = [para([run(`Câu ${soCau}. `, { bold: true, size: SZ_CONTENT }),
    ...toInline(cauHoi, { size: SZ_CONTENT })], { before: THO_VUA, after: thamChieu ? 0 : 4, justify: true })];

  if (thamChieu) {
    out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { before: 0, after: 4 }));
  }

  const labeled = ["A", "B", "C", "D"].map((k, i) => {
    const d = _lotNhanTrung(dapAn[i], _MAU_NHAN_DAPAN, "cauTracNghiem");
    return Array.isArray(d) ? [`${k}. `, ...d] : `${k}. ${d}`;
  });
  // [v9.9] Xếp cột theo ĐỘ DÀI đáp án dài nhất (kể cả nhãn "A. "):
  //  ≤18 kt → 4 cột 1 hàng (4,6cm/cột đủ chỗ); ≤40 kt → 2×2 (9,2cm/cột);
  //  >40 kt → mỗi đáp án 1 dòng. Trước đây ngưỡng 30 cho 4-cột nên đáp án
  //  ~20 kt vẫn nhồi 4 cột → tràn/wrap xấu (câu 4, câu 5 B32).
  const maxLen = Math.max(...labeled.map(approxLen));
  if (maxLen > 40) {
    labeled.forEach(it => out.push(paraInline(it, { before: 0, after: 0 })));
  } else if (maxLen > 18) {
    out.push(tabLine([labeled[0], labeled[1]]));
    out.push(tabLine([labeled[2], labeled[3]]));
  } else {
    out.push(tabLine(labeled));
  }
  return out;
}

// ═════════════════════════════════════════════════════════════
// 13. BẢNG ĐÁP ÁN PHẦN I (2 hàng × N cột, N=8 THCS, N=12 THPT)
// ═════════════════════════════════════════════════════════════
// [v9.4] Đáp án Phần I trình bày MỘT DÒNG: "Câu 1 - B; Câu 2 - A; ..."
// (thay dạng bảng 2 hàng cũ — gọn hơn, đúng yêu cầu 25/07). Nhận mảng đáp án
// ['B','A','C',...]. Trả 1 Paragraph.
function bangDapAnPhanI(dapAnArr) {
  // [v9.6] Ép 1 DÒNG cho 8 câu (yêu cầu 05/08): bỏ nhãn "Đáp án:", bỏ dấu cách quanh gạch
  // ("Câu 1-B" thay "Câu 1 - B"), phân tách gọn "; ". Nhãn "Câu N-" đen đậm, đáp án đỏ đậm.
  const runs = [];
  dapAnArr.forEach((da, i) => {
    runs.push(run(`Câu ${i + 1}-`, { bold: true, size: SZ_CONTENT }));
    runs.push(run(String(da), { bold: true, color: C_RED_ANSWER, size: SZ_CONTENT }));
    if (i < dapAnArr.length - 1) runs.push(run("; ", { bold: true, size: SZ_CONTENT }));
  });
  return para(runs, { before: 6, after: 6 });
}

// ═════════════════════════════════════════════════════════════
// 14. BẢNG ĐÚNG/SAI — tỉ lệ CỐ ĐỊNH 80%-10%-10%, nền trắng chữ đen
// ═════════════════════════════════════════════════════════════
function bangDungSai(menhDeArr) {
  if (!Array.isArray(menhDeArr) || menhDeArr.length !== 4) {
    throw new Error(`\n[LỖI BẢNG DS]: Cần đúng 4 mệnh đề (a,b,c,d). Hiện có: ${menhDeArr?.length ?? 0}.`);
  }
  const soSai = menhDeArr.filter(m => !m.dung).length;
  if (soSai === 0) {
    throw new Error("\n[LỖI BẢNG DS]: Tất cả 4 mệnh đề đều ĐÚNG — phải có ít nhất 1 mệnh đề SAI mang bẫy kiến thức.");
  }
  menhDeArr.forEach((m,i) => _guardND(m.menhDe, `bangDungSai mệnh đề ${"abcd"[i]}`));
  // HP V10.3 Điều 17.2: bảng Đúng/Sai CÓ viền mảnh xám (size 4, #999999)
  // để học sinh đọc rõ từng mệnh đề và cột Đúng/Sai.
  const bc = { style: BorderStyle.SINGLE, size: 4, color: "999999" };
  const borders = { top: bc, bottom: bc, left: bc, right: bc, insideH: bc, insideV: bc };
  const wMenhDe = Math.round(TOTAL_W * 0.80);
  const wDung = Math.round(TOTAL_W * 0.10);
  const wSai = TOTAL_W - wMenhDe - wDung;

  const shd = { type: ShadingType.CLEAR, fill: C_WHITE }; // BẮT BUỘC trắng — không đổi

  const headerRow = new TableRow({
    children: [
      new TableCell({ width: { size: wMenhDe, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: [para([run("Mệnh đề", { bold: true, size: SZ_CONTENT })], { before: 0, after: 0 })] }),
      new TableCell({ width: { size: wDung, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: [para([run("Đúng", { bold: true, size: SZ_CONTENT })],
          { align: AlignmentType.CENTER, before: 0, after: 0 })] }),
      new TableCell({ width: { size: wSai, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: [para([run("Sai", { bold: true, size: SZ_CONTENT })],
          { align: AlignmentType.CENTER, before: 0, after: 0 })] }),
    ],
  });

  const nhan = "abcd".split("");
  const rows = menhDeArr.map((m, i) => new TableRow({
    children: [
      new TableCell({ width: { size: wMenhDe, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 100, right: 100 },
        children: [para([run(`${nhan[i]}) `, { size: SZ_CONTENT }),
          ...toInline(m.menhDe, { size: SZ_CONTENT })], { before: 0, after: 0 })] }),
      new TableCell({ width: { size: wDung, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: [para([m.dung ? run("●", { size: SZ_CONTENT }) : run("", {})],
          { align: AlignmentType.CENTER, before: 0, after: 0 })] }),
      new TableCell({ width: { size: wSai, type: WidthType.DXA }, borders, shading: shd,
        margins: { top: 60, bottom: 60, left: 60, right: 60 },
        children: [para([!m.dung ? run("●", { size: SZ_CONTENT }) : run("", {})],
          { align: AlignmentType.CENTER, before: 0, after: 0 })] }),
    ],
  }));

  return new Table({
    width: { size: TOTAL_W, type: WidthType.DXA },
    columnWidths: [wMenhDe, wDung, wSai],
    rows: [headerRow, ...rows],
  });
}

// ═════════════════════════════════════════════════════════════
// 15. TRẢ LỜI NGẮN
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soCau
 * @param {string|Array} p.cauHoi - string (như cũ) hoặc mảng trộn text/công thức
 * @param {string|Array} p.dapAn  - string (như cũ) hoặc mảng trộn text/công thức
 */
function traLoiNgan({ soCau, cauHoi, dapAn }) {
  return [
    para([run(`Câu ${soCau}. `, { bold: true, size: SZ_CONTENT }), ...toInline(cauHoi, { size: SZ_CONTENT })],
      { before: THO_VUA, after: 6 }),
    para([run("Đáp án: ", { bold: true, size: SZ_CONTENT }), ...toInline(dapAn, { size: SZ_CONTENT })],
      { before: 0, after: 20 }),
  ];
}

// ═════════════════════════════════════════════════════════════
// 16. HEADER ĐỀ KIỂM TRA (tên đề + thời gian + bảng Họ tên/Điểm/NX)
// ═════════════════════════════════════════════════════════════
function headerDeKiemTra({ tenDe, phut }) {
  const wTrai = Math.round(TOTAL_W * 0.40);
  const wPhai = TOTAL_W - wTrai;
  const bc = { style: BorderStyle.SINGLE, size: 6, color: C_BLACK };
  const borders = { top: bc, bottom: bc, left: bc, right: bc };

  const table = new Table({
    width: { size: TOTAL_W, type: WidthType.DXA },
    columnWidths: [wTrai, wPhai],
    rows: [new TableRow({
      children: [
        new TableCell({
          width: { size: wTrai, type: WidthType.DXA }, borders,
          margins: { top: 80, bottom: 60, left: 160, right: 160 },
          children: [
            para([run("Họ và tên: ", { bold: true, size: SZ_CONTENT })], { before: 0, after: 40 }),
            para([run("Điểm: ", { bold: true, size: SZ_CONTENT })], { before: 0, after: 40 }),
          ],
        }),
        new TableCell({
          width: { size: wPhai, type: WidthType.DXA }, borders,
          margins: { top: 80, bottom: 60, left: 160, right: 160 },
          children: [
            para([run("Nhận xét của GV:", { bold: true, size: SZ_CONTENT })], { before: 0, after: 100 }),
          ],
        }),
      ],
    })],
  });

  return [
    para([run(tenDe, { bold: true, size: SZ_CONTENT })],
      { align: AlignmentType.CENTER, before: 20, after: 0 }),
    para([run(`THỜI GIAN: ${phut} PHÚT `, { bold: true, color: C_RED, size: SZ_CONTENT }),
      run("(không kể thời gian phát đề)", { bold: true, color: C_RED, size: SZ_CONTENT })],
      { align: AlignmentType.CENTER, before: 0, after: 10 }),
    table,
    para([], { before: 10, after: 10 }),
  ];
}

// ═════════════════════════════════════════════════════════════
// 17. HEADER & FOOTER CHUẨN CHO FILE BÀI HỌC (Bản GV)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soBai  - số thứ tự bài (GIỐNG object truyền vào tenBaiHoc)
 * @param {string} p.tenBai - tên bài THÔ, không cần viết hoa/thường chuẩn
 *   (KHÔNG cần gõ "BÀI n." — hàm tự dựng; KHÔNG cần tự IN HOA/viết thường —
 *   hàm tự chuẩn hóa về Sentence case, chỉ viết hoa chữ cái đầu mỗi câu)
 * @param {string} p.lop    - ví dụ "Lớp 6"
 * Trả về { header, footer } — object Header/Footer của docx-js,
 * dùng trực tiếp trong sections[0].headers / .footers.
 *
 * ⚠️ Dùng CÙNG object { soBai, tenBai, ... } đã truyền cho tenBaiHoc() —
 * gõ tenBai MỘT LẦN DUY NHẤT, tránh lệch tên bài giữa tiêu đề và header
 * (sự cố đã xảy ra ở Bài 10).
 */
function headerFooterBaiHoc({ soBai, tenBai, lop }) {
  const headerText = `Bài ${soBai}. ${chuanHoaCauChu(tenBai)}`;
  const header = new Header({
    children: [
      new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C_GRAY, space: 2 } },
        spacing: { before: 0, after: 60 },
        tabStops: [{ type: "right", position: TOTAL_W }],
        children: [
          new TextRun({ text: "HỆ THỐNG PHÁT TRIỂN NGUỒN LỰC HIẾU HỌC", font: TNR, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: `${headerText} | ${lop}`, font: TNR, size: SZ_SMALL - 2, color: C_GRAY }),
        ],
      }),
    ],
  });

  const footer = new Footer({
    children: [
      new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: C_GRAY, space: 2 } },
        spacing: { before: 60, after: 0 },
        tabStops: [
          { type: "center", position: Math.round(TOTAL_W / 2) },
          { type: "right", position: TOTAL_W },
        ],
        children: [
          new TextRun({ text: "© Hiếu Học - TL nội bộ", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: "Tập trung - Tự Tin - Chiến thắng", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: "Trang ", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ children: [PageNumber.CURRENT], font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
        ],
      }),
    ],
  });

  return { header, footer };
}

// ─────────────────────────────────────────────────────────────
// header/footer trang Word cho ĐỀ KIỂM TRA — ĐÚNG MẪU headerFooterBaiHoc,
//   KHÔNG làm khác. Chỉ thay định danh: "Bài n. Tên | Lớp" → tên đề (dạng
//   thường, truyền sẵn). Footer y hệt mẫu: © Hiếu Học - TL nội bộ + slogan
//   + số trang (PageNumber.CURRENT — tự chạy theo vị trí khi gộp file).
// ─────────────────────────────────────────────────────────────
function headerFooterDeKT({ tenDe }) {
  const header = new Header({
    children: [
      new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: C_GRAY, space: 2 } },
        spacing: { before: 0, after: 60 },
        tabStops: [{ type: "right", position: TOTAL_W }],
        children: [
          new TextRun({ text: "HỆ THỐNG PHÁT TRIỂN NGUỒN LỰC HIẾU HỌC", font: TNR, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: tenDe, font: TNR, size: SZ_SMALL - 2, color: C_GRAY }),
        ],
      }),
    ],
  });
  const footer = new Footer({
    children: [
      new Paragraph({
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: C_GRAY, space: 2 } },
        spacing: { before: 60, after: 0 },
        tabStops: [
          { type: "center", position: Math.round(TOTAL_W / 2) },
          { type: "right", position: TOTAL_W },
        ],
        children: [
          new TextRun({ text: "© Hiếu Học - TL nội bộ", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: "Tập trung - Tự Tin - Chiến thắng", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ text: "\t", font: TNR, size: SZ_SMALL - 2 }),
          new TextRun({ text: "Trang ", font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
          new TextRun({ children: [PageNumber.CURRENT], font: TNR, italic: true, size: SZ_SMALL - 2, color: C_GRAY }),
        ],
      }),
    ],
  });
  return { header, footer };
}

// ═════════════════════════════════════════════════════════════
// 18. TỜ PHÂN CHƯƠNG (dành cho AI QC — sau khi gộp file tổng)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {Buffer} p.logoBuffer   - fs.readFileSync(đường dẫn logo .png)
 * @param {string}  p.lop         - ví dụ "TOÁN 8"
 * @param {string}  p.tenChuong   - ví dụ "CHƯƠNG I. ĐA THỨC"
 * @param {Array<{soBai:number, ten:string}>} p.danhSachBai
 * @param {boolean} [p.co45=true] - có đề 45 phút không
 * @param {boolean} [p.co90=true] - có đề 90 phút không
 * @param {string}  [p.capCho=""] - để trống, GV tự điền tay
 * Trả về mảng children — dùng riêng 1 section KHÔNG có header/footer, KHÔNG số trang.
 */
function toPhanChuong({ logoBuffer, lop, tenChuong, danhSachBai, coTongKet = false, co45 = true, co90 = true }) {
  const { ImageRun } = require("docx");
  const logoWidth = 2880000;
  const logoHeight = Math.round(logoWidth * 1024 / 1280); // tỉ lệ logo gốc 1280×1024

  const out = [];

  // Logo
  out.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 80, after: 20 },
    children: [new ImageRun({
      data: logoBuffer,
      transformation: { width: Math.round(logoWidth / 9144), height: Math.round(logoHeight / 9144) },
      type: "png",
    })],
  }));

  // Tên hệ thống — 20pt (line height rộng hơn để không chồng chữ)
  out.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 60, line: 320 },
    children: [run("HỆ THỐNG PHÁT TRIỂN NGUỒN LỰC HIẾU HỌC", { bold: true, color: "1F3864", size: 40 })],
  }));

  // Tên trung tâm — 16pt
  out.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 20, line: 280 },
    children: [run("TRUNG TÂM BỒI DƯỠNG VĂN HÓA VÀ LUYỆN THI HIẾU HỌC", { bold: true, color: "1F3864", size: 32 })],
  }));

  // Đường kẻ kép
  out.push(new Paragraph({ spacing: { before: 20, after: 20 },
    border: { bottom: { style: BorderStyle.DOUBLE, size: 6, color: "1565C0", space: 1 } }, children: [] }));

  // Dòng trắng
  out.push(new Paragraph({ spacing: { before: 0, after: 0, line: 220 }, children: [] }));

  // TOÁN [lớp] — 48pt (line height rộng để không chồng chữ)
  out.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 60, line: 400 },
    children: [run(lop, { bold: true, color: "1565C0", size: 48 })],
  }));
  out.push(para([run("KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", { bold: true, color: C_GRAY, size: 28 })],
    { align: AlignmentType.CENTER, before: 0, after: 10 }));
  out.push(para([run("BẢN GIÁO VIÊN", { bold: true, italic: true, color: "D84315", size: 28 })],
    { align: AlignmentType.CENTER, before: 0, after: 20 }));

  // Đường kẻ đơn
  out.push(new Paragraph({ spacing: { before: 20, after: 20 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "1565C0", space: 1 } }, children: [] }));

  // A6 v9.0: 1 dòng trống trước tên chương (HP V10 Điều 51, mục 8)
  out.push(new Paragraph({ spacing: { before: 0, after: 0, line: 220 }, children: [] }));

  // Tên chương
  out.push(para([run(tenChuong, { bold: true, color: "1F3864", size: 28 })],
    { align: AlignmentType.CENTER, before: 0, after: 20 }));

  // Danh sách bài — KHÔNG ghi số tiết, KHÔNG ghi mã định danh
  danhSachBai.forEach(b => {
    out.push(new Paragraph({
      spacing: { before: 10, after: 10, line: 220 }, indent: { left: 400 },
      children: [
        new TextRun({ text: "✦  ", font: TNR, color: "1565C0", size: 28 }),
        new TextRun({ text: `Bài ${b.soBai}. ${b.ten}`, font: TNR, bold: true, size: 28 }),
      ],
    }));
  });

  // Tổng kết chương (sơ đồ hệ thống hoá) — sau các bài, trước đề
  if (coTongKet) {
    out.push(new Paragraph({
      spacing: { before: 10, after: 10, line: 220 }, indent: { left: 400 },
      children: [
        new TextRun({ text: "✦  ", font: TNR, color: "1565C0", size: 28 }),
        new TextRun({ text: "Tổng kết chương", font: TNR, bold: true, size: 28 }),
      ],
    }));
  }

  // Đề kiểm tra — 1 đề 45' + 1 đề 90' / chương, KHÔNG ghi mã
  if (co45) {
    out.push(new Paragraph({
      spacing: { before: 10, after: 10, line: 220 }, indent: { left: 400 },
      children: [
        new TextRun({ text: "✦  ", font: TNR, color: "1565C0", size: 28 }),
        new TextRun({ text: "Đề kiểm tra 45 phút", font: TNR, bold: true, size: 28 }),
      ],
    }));
  }
  if (co90) {
    out.push(new Paragraph({
      spacing: { before: 10, after: 30, line: 220 }, indent: { left: 400 },
      children: [
        new TextRun({ text: "✦  ", font: TNR, color: "1565C0", size: 28 }),
        new TextRun({ text: "Đề kiểm tra 90 phút", font: TNR, bold: true, size: 28 }),
      ],
    }));
  }

  // Đường kẻ đơn
  out.push(new Paragraph({ spacing: { before: 20, after: 20 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "1565C0", space: 1 } }, children: [] }));

  // Dòng trắng
  out.push(new Paragraph({ spacing: { before: 0, after: 0, line: 220 }, children: [] }));

  // Cấp cho — thụt 1 tab
  out.push(new Paragraph({
    spacing: { before: 0, after: 30, line: 220 },
    tabStops: [{ type: "left", position: 700 }],
    children: [
      new TextRun({ text: "\t", font: TNR }),
      new TextRun({ text: "Cấp cho: ", font: TNR, bold: true, size: 28 }),
      new TextRun({ text: "…………………………………………………………………", font: TNR, size: 28 }),
    ],
  }));

  return out;
}

// Footer riêng cho tờ phân chương (khác footer file bài học — không số trang)
function footerTPC() {
  return new Footer({
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 0 },
        children: [new TextRun({
          text: "✦  Hiếu Học © 2026  │  Phiên bản CS2627  │  Lưu hành nội bộ  ✦",
          font: TNR, italic: true, color: C_GRAY, size: SZ_SMALL,
        })],
      }),
    ],
  });
}

// ═════════════════════════════════════════════════════════════
// 19. TỰ LUẬN BTVN — mục D, dùng chung cho THCS (5 bài) & THPT (3 bài)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {number} p.soBai
 * @param {string} p.mucDo     - "NB"|"TH"|"VD"|"VDC"|"NC"
 * @param {number} p.diem      - điểm số bài này, ví dụ 1 (THCS) hoặc theo THPT
 * @param {string} [p.deBai]   - nếu 1 câu
 * @param {string[]} [p.cacCau]- nếu nhiều câu (a,b,c...)
 * @param {string} [p.thamChieu] - để trống nếu tự soạn
 * @param {string|string[]} p.loiGiaiND
 */
/**
 * @param {Object} p
 * @param {number} p.soBai
 * @param {string} p.mucDo     - "NB"|"TH"|"VD"|"VDC"|"NC"
 * @param {number} p.diem      - điểm số bài này, ví dụ 1 (THCS) hoặc theo THPT
 * @param {string|Array} [p.deBai] - string (như cũ) hoặc mảng trộn text/công thức
 * @param {Array<string|Array>} [p.cacCau]- mảng câu, mỗi phần tử string hoặc mảng trộn
 * @param {string} [p.thamChieu] - để trống nếu tự soạn
 * @param {string|Array} p.loiGiaiND
 */
function tuLuanBTVN({ soBai, mucDo, diem, deBai, cacCau, thamChieu, loiGiaiND, coHinh, hinhBenTrai, hinhBenPhai }) {
  thamChieu = _locNguon(thamChieu);
  _guardND(deBai, "tuLuanBTVN");
  _guardArr(cacCau, "tuLuanBTVN");
  const _hinh = hinhBenPhai || hinhBenTrai;   // hinhBenPhai = tên CHÍNH (neo phải); hinhBenTrai = bí danh cũ (v9.4)
  if (_canHinh(deBai, cacCau) && !coHinh && !_hinh) {
    const ds = _extractText(deBai) + " " + _extractText(cacCau);
    throw new Error(`\n[LỖI THIẾU HÌNH] BTVN TL Bài ${soBai} cần hình.\n  Đề: "${ds.substring(0,100)}..."\n→ Mục ③ trở xuống: hinhBenPhai:{imageBuffer,...} (NEO PHẢI, chữ wrap TRÁI), hình nướng nhãn qua ve(nhan="Hình N"). Mục ② & Phần II: coHinh:[...H.hinhVe(...,chuThich:"Hình N. ...")] (dòng riêng căn giữa)`);
  }
  const out = [];
  const nhanDiem = diem ? ` (${diem}đ)` : "";
  const nhanBai = `Bài ${soBai}. (${mucDo})${nhanDiem} `;
  // HP V10.3 Điều 18: hình nhỏ + nội dung dài → text box neo phải, chữ wrap trái
  if (_hinh && _hinh.imageBuffer) {
    const anh = hinhVeTextBox(_hinh);
    const deInline = deBai
      ? [run(nhanBai, { bold: true, size: SZ_CONTENT }), ...toInline(deBai, { size: SZ_CONTENT })]
      : [run(`Bài ${soBai}. (${mucDo})${nhanDiem}`, { bold: true, size: SZ_CONTENT })];
    out.push(paraCoHinhPhai(anh, deInline, { before: THO_VUA, after: 0, justify: true }));
    if (thamChieu) out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })], { before: 0, after: 6 }));
    if (cacCau && cacCau.length) out.push(...layoutCauHoi(cacCau, { dai: true }));
    out.push(...loiGiai(loiGiaiND));
    return out;
  }
  if (deBai) {
    out.push(para([run(nhanBai, { bold: true, size: SZ_CONTENT }),
      ...toInline(deBai, { size: SZ_CONTENT })], { before: THO_VUA, after: 0, justify: true }));
  } else {
    out.push(para([run(`Bài ${soBai}. (${mucDo})${nhanDiem}`, { bold: true, size: SZ_CONTENT })],
      { before: THO_VUA, after: 0 }));
  }
  if (thamChieu) {
    out.push(para([run(`(${thamChieu})`, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { before: 0, after: 6 }));
  }
  _appendHinh(out, coHinh, "coHinh");
  if (cacCau && cacCau.length) out.push(...layoutCauHoi(cacCau));
  out.push(...loiGiai(loiGiaiND));
  return out;
}

// Tiêu đề khối "D. TỰ LUẬN (n bài = Xđ)"
function tieuDeTuLuan(soBai, tongDiem) {
  return para([run(`D. TỰ LUẬN  (${soBai} bài = ${tongDiem}đ)`, { bold: true, size: SZ_CONTENT })],
    { before: THO_RONG, after: 10 });
}

// Định dạng đơn giá mỗi câu (điểm/câu) theo chuẩn số thập phân dấu phẩy
// của Hiến Pháp — ví dụ 0.25 → "0,25", 0.5 → "0,5", 1 → "1".
function formatDonGia(tongDiem, soCau) {
  const donGia = Math.round((tongDiem / soCau) * 100) / 100; // tránh sai số dấu phẩy động
  return donGia.toString().replace(".", ",");
}

// Tiêu đề khối "A. PHẦN I - CHỌN ĐÁP ÁN (...)"
function tieuDePhanI(soCau, tongDiem) {
  const donGia = formatDonGia(tongDiem, soCau);
  return para([run(`A. PHẦN I - CHỌN ĐÁP ÁN  (${soCau} câu × ${donGia}đ = ${tongDiem}đ)`,
    { bold: true, size: SZ_CONTENT })], { before: THO_RONG, after: 10 });
}

function tieuDePhanII(soCau, soMenhDe, tongDiem) {
  return para([run(`B. PHẦN II - ĐÚNG / SAI  (${soCau} câu × ${soMenhDe} mệnh đề = ${tongDiem}đ)`,
    { bold: true, size: SZ_CONTENT })], { before: THO_RONG, after: 10 });
}

function tieuDePhanIII(soCau, tongDiem) {
  const donGia = formatDonGia(tongDiem, soCau);
  return para([run(`C. PHẦN III - TRẢ LỜI NGẮN  (${soCau} câu × ${donGia}đ = ${tongDiem}đ)`,
    { bold: true, size: SZ_CONTENT })], { before: THO_RONG, after: 10 });
}

// ═════════════════════════════════════════════════════════════
// 20. TRANG CUỐI CHƯƠNG — mục ⑧ Ghi chú giảng dạy + ⑨ Nhật ký cải tiến
//     (đặt CUỐI CHƯƠNG, không đánh số trang, chỉ soạn 1 lần)
// ═════════════════════════════════════════════════════════════
/**
 * @param {Array<{lop:string, bai:string}>} [p.dsLopBai] - danh sách cặp Lớp/Bài để GV tự điền,
 *   mỗi phần tử tạo sẵn 1 dòng "Lớp ...: " + "Bài ...: " trống để GV viết tay.
 *   Nếu không truyền, mặc định tạo sẵn 2 cặp trống.
 */
function ghiChuGiangDay({ dsLopBai } = {}) {
  const out = [];
  out.push(para([run("⑧ GHI CHÚ GIẢNG DẠY", { bold: true, size: SZ_CONTENT })], { before: 10, after: 10 }));

  out.push(para([run("1. Thời lượng thực tế", { bold: true, size: SZ_CONTENT })], { before: 0, after: 4 }));
  out.push(para([run("Lý thuyết: .......... tiết  /  Dự kiến: .......... tiết", { size: SZ_CONTENT, color: C_GRAY })],
    { before: 0, after: 0, indent: { left: 300 } }));
  out.push(para([run("Bài tập: .......... tiết  /  Dự kiến: .......... tiết", { size: SZ_CONTENT, color: C_GRAY })],
    { before: 0, after: 10, indent: { left: 300 } }));

  out.push(para([run("2. Nội dung HS tiếp thu tốt", { bold: true, size: SZ_CONTENT })], { before: 0, after: 4 }));
  out.push(para([run(".................................................................................",
    { size: SZ_CONTENT, color: "CCCCCC" })], { before: 0, after: 10, indent: { left: 300 } }));

  out.push(para([run("3. Nội dung HS còn yếu / hay sai", { bold: true, size: SZ_CONTENT })], { before: 0, after: 4 }));
  out.push(para([run(".................................................................................",
    { size: SZ_CONTENT, color: "CCCCCC" })], { before: 0, after: 10, indent: { left: 300 } }));

  out.push(para([run("4. Điều chỉnh cho lần dạy tiếp theo", { bold: true, size: SZ_CONTENT })], { before: 0, after: 4 }));
  out.push(para([run(".................................................................................",
    { size: SZ_CONTENT, color: "CCCCCC" })], { before: 0, after: 10, indent: { left: 300 } }));

  out.push(para([run("5. Ghi chú riêng theo từng lớp từng bài", { bold: true, size: SZ_CONTENT })],
    { before: 0, after: 4 }));
  const cap = (dsLopBai && dsLopBai.length) ? dsLopBai : [{}, {}];
  cap.forEach((_, i) => {
    const isLast = i === cap.length - 1;
    out.push(para([run("Lớp .........: .................................................................",
      { size: SZ_CONTENT, color: C_GRAY })], { before: 0, after: 0, indent: { left: 300 } }));
    out.push(para([run("Bài  .........: .................................................................",
      { size: SZ_CONTENT, color: C_GRAY })], { before: 0, after: isLast ? 20 : 0, indent: { left: 300 } }));
  });

  return out;
}

/**
 * @param {Array<{phienBan:string, ngay:string, noiDung:string, nguoiCapNhat:string}>} [p.dsPhienBan]
 */
function nhatKyCaiTien({ dsPhienBan } = {}) {
  const rows = (dsPhienBan && dsPhienBan.length) ? dsPhienBan : [{ phienBan: "v1.0", ngay: "", noiDung: "Bản gốc", nguoiCapNhat: "" }];
  const bc = { style: BorderStyle.SINGLE, size: 4, color: C_BLACK };
  const borders = { top: bc, bottom: bc, left: bc, right: bc };
  const colW = [1500, 1500, 5500, 1932];
  const headerCells = ["Phiên bản", "Ngày", "Nội dung cập nhật", "Người cập nhật"];

  const headerRow = new TableRow({
    children: headerCells.map((h, i) => new TableCell({
      width: { size: colW[i], type: WidthType.DXA }, borders,
      shading: { type: ShadingType.CLEAR, fill: "F5F7FA" },
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [para([run(h, { bold: true, size: SZ_CONTENT })], { before: 0, after: 0 })],
    })),
  });
  const bodyRows = rows.map(r => new TableRow({
    children: [r.phienBan, r.ngay, r.noiDung, r.nguoiCapNhat].map((v, i) => new TableCell({
      width: { size: colW[i], type: WidthType.DXA }, borders,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [para([run(v || "", { size: SZ_CONTENT })], { before: 0, after: 0 })],
    })),
  }));

  return [
    para([run("⑨ NHẬT KÝ CẢI TIẾN TÀI LIỆU", { bold: true, size: SZ_CONTENT })], { before: 10, after: 10 }),
    new Table({ width: { size: TOTAL_W, type: WidthType.DXA }, columnWidths: colW, rows: [headerRow, ...bodyRows] }),
  ];
}

/**
 * BẢNG NGUỒN GỐC BÀI TẬP — CUỐI CHƯƠNG (4 cột: Bài | STT | Vị trí | Nguồn gốc)
 * @param {number|string} p.soChuong
 * @param {Array<{bai:string, stt:number, viTri:string, nguon:string}>} p.dsNguon
 */
function bangNguonGoc({ soChuong, dsNguon }) {
  const bc = { style: BorderStyle.SINGLE, size: 4, color: C_BLACK };
  const borders = { top: bc, bottom: bc, left: bc, right: bc };
  const colW = [1200, 800, 4500, 3932];
  const headerCells = ["Bài", "STT", "Vị trí trong bài", "Nguồn gốc"];

  const headerRow = new TableRow({
    children: headerCells.map((h, i) => new TableCell({
      width: { size: colW[i], type: WidthType.DXA }, borders,
      shading: { type: ShadingType.CLEAR, fill: "F5F7FA" },
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [para([run(h, { bold: true, size: SZ_CONTENT })], { before: 0, after: 0 })],
    })),
  });
  const bodyRows = dsNguon.map(r => new TableRow({
    children: [r.bai, String(r.stt), r.viTri, r.nguon].map((v, i) => new TableCell({
      width: { size: colW[i], type: WidthType.DXA }, borders,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [para([run(v, { size: SZ_CONTENT })], { before: 0, after: 0 })],
    })),
  }));

  return [
    para([], { before: 20, after: 0 }),
    para([run(`BẢNG NGUỒN GỐC BÀI TẬP — CHƯƠNG ${soChuong}`, { bold: true, size: SZ_CONTENT })],
      { before: 20, after: 10 }),
    new Table({ width: { size: TOTAL_W, type: WidthType.DXA }, columnWidths: colW, rows: [headerRow, ...bodyRows] }),
  ];
}

// Gộp cả trang cuối chương thành 1 lệnh gọi — khuyến khích dùng
/**
 * @param {Object} p
 * @param {Array} [p.dsLopBai]
 * @param {Array} [p.dsPhienBan]
 */
function trangCuoiChuong({ dsLopBai, dsPhienBan }) {
  // [v10.0] HP V11 Điều 72/76: BỎ HẲN bảng nguồn gốc gom cuối chương — nguồn kiểm ở
  // CẤP BÀI (metadata kiểm soát, không phải nội dung học liệu). bangNguonGoc() giữ định
  // nghĩa để code cũ không vỡ nhưng KHÔNG còn được gộp vào trang cuối chương.
  return [
    ...ghiChuGiangDay({ dsLopBai }),
    ...nhatKyCaiTien({ dsPhienBan }),
  ];
}

// Header rỗng — dùng để NGẮT KẾ THỪA header khi tạo section riêng cho Trang cuối chương
// (OOXML mặc định section sau kế thừa header/footer section trước nếu không khai báo lại)
function headerRong() {
  return new Header({ children: [] });
}

// ═════════════════════════════════════════════════════════════
// 21. CÔNG THỨC TOÁN THẬT — OMML (hiển thị đúng trong Microsoft Word;
//     LibreOffice preview có thể không render đẹp, nhưng XML chuẩn OOXML)
// ═════════════════════════════════════════════════════════════
/**
 * MathRunSized — thay thế MathRun mặc định của docx (không hỗ trợ size).
 * Kế thừa MathRun gốc rồi chèn thêm <w:rPr><w:sz .../></w:rPr> làm con
 * đầu tiên của <m:r>, đúng chuẩn OOXML thật (w:rPr nằm TRỰC TIẾP trong
 * m:r, KHÔNG bọc trong m:rPr — m:rPr chỉ dành cho thuộc tính riêng của
 * Math như literal/nor, không phải font size).
 * Đã kiểm tra: XML sinh ra khớp 100% với cách Word tự xuất khi Insert Equation.
 */
class MathRunSized extends MathRun {
  constructor(text, size = SZ_CONTENT) {
    super(text);
    this.root.unshift(new RunProperties({ size }));
  }
}

/**
 * Lũy thừa — dùng CHÈN TRỰC TIẾP vào mảng children của 1 TextRun/Paragraph,
 * xen giữa các run text bình thường.
 * @param {string|number} coSo
 * @param {string|number} soMu
 * @returns {Math} — object chèn thẳng vào children của Paragraph
 *
 * Ví dụ: para([run("Ta có "), luyThua(2,3), run(" · "), luyThua(3,2), run(" = 72")])
 *
 * ⚠️ LƯU Ý: hàm này tạo công thức OMML chuẩn (giống Word tự tạo khi bấm
 * Insert Equation). Cấu trúc XML đã kiểm tra hợp lệ 100% theo chuẩn OOXML.
 * Cỡ chữ đã khớp SZ_CONTENT (13pt) với văn bản xung quanh — không còn lệch dòng.
 */
function luyThua(coSo, soMu) {
  return new DMath({
    children: [new MathSuperScript({
      children: [new MathRunSized(String(coSo))],
      superScript: [new MathRunSized(String(soMu))],
    })],
  });
}

// Bảng chuyển số thường → ký tự Unicode superscript
const UNICODE_SUP = { "0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹","-":"⁻" };

/**
 * PHƯƠNG ÁN DỰ PHÒNG — lũy thừa bằng ký tự Unicode (², ³...), đảm bảo
 * hiển thị đúng ở MỌI nơi (Word, LibreOffice, PDF, web...) dù không phải
 * object công thức thật. Dùng khi luyThua() không hiển thị đúng trong Word.
 * @returns {TextRun} — chèn thẳng vào children của Paragraph như run() bình thường
 */
function luyThuaUnicode(coSo, soMu) {
  const supStr = String(soMu).split("").map(c => UNICODE_SUP[c] || c).join("");
  return run(`${coSo}${supStr}`, { size: SZ_CONTENT });
}

/**
 * Phân số — dùng CHÈN TRỰC TIẾP vào mảng children của Paragraph.
 * @param {string|number} tuSo
 * @param {string|number} mauSo
 * @returns {Math}
 *
 * Ví dụ: para([run("Kết quả: "), phanSo(1,2), run(" + "), phanSo(1,3)])
 */
function phanSo(tuSo, mauSo) {
  return new DMath({
    children: [new MathFraction({
      numerator: [new MathRunSized(String(tuSo))],
      denominator: [new MathRunSized(String(mauSo))],
    })],
  });
}

/**
 * A3 v9.0 — Căn bậc — OMML chuẩn SGK KNTT Việt Nam.
 * Dùng CHÈN TRỰC TIẾP vào mảng children của Paragraph, xen giữa các run text.
 * @param {string|number} soHang  - số/biểu thức dưới dấu căn
 * @param {string|number} [bacCan=2] - bậc của căn (2=căn bậc hai, 3=căn bậc ba...)
 * @returns {Math}
 *
 * Ví dụ:
 *   para([run("Tính "), H.canBac(2), run(" = ?")])           // √2
 *   para([run("x = "), H.canBac("a+b")])                     // √(a+b)
 *   para([run("Kết quả: "), H.canBac(8, 3), run(" = 2")])    // ∛8
 */
function canBac(soHang, bacCan = 2) {
  const rad = new BuilderElement({
    name: "m:rad",
    children: [
      new BuilderElement({
        name: "m:radPr",
        children: [
          new BuilderElement({
            name: "m:degHide",
            attributes: { val: { key: "m:val", value: bacCan == 2 ? "1" : "0" } },
          }),
        ],
      }),
      // Bậc căn (ẩn nếu bậc 2)
      new BuilderElement({
        name: "m:deg",
        children: bacCan == 2 ? [] : [new MathRunSized(String(bacCan))],
      }),
      createMathBase({ children: [new MathRunSized(String(soHang))] }),
    ],
  });
  return new DMath({ children: [rad] });
}

/**
 * A9 v9.1 — Chỉ số dưới (subscript) — OMML. Dùng cho biến có chỉ số:
 * x₁, aₙ, u_{n+1}... Chèn thẳng vào children của Paragraph.
 * @param {string|number} coSo   - phần gốc (x, a, u...)
 * @param {string|number} chiSo  - phần chỉ số dưới (1, n, n+1...)
 * @returns {Math}
 *
 * LƯU Ý: chỉ số dưới ĐƠN GIẢN 1 chữ số (x₁, a₂) nên gõ Unicode ₀–₉ trực
 * tiếp (đủ cho THCS — HP V10 Điều 16.4). Chỉ dùng hàm này khi chỉ số PHỨC
 * TẠP (n+1, i-1, 2k...) mà Unicode không có sẵn.
 *
 * Ví dụ: para([run("Số hạng "), chiSoDuoi("u", "n+1"), run(" = ...")])
 */
function chiSoDuoi(coSo, chiSo) {
  return new DMath({
    children: [new MathSubScript({
      children: [new MathRunSized(String(coSo))],
      subScript: [new MathRunSized(String(chiSo))],
    })],
  });
}

/**
 * A9 v9.1 — Trị tuyệt đối — OMML, cặp gạch đứng |…| bao biểu thức (delimiter
 * chuẩn, giãn theo chiều cao nội dung — khác gõ "|" thẳng bị cứng). Chèn
 * thẳng vào children của Paragraph.
 * @param {string} bieuThuc - nội dung bên trong, ví dụ "x - 3", "2a + b"
 * @returns {Math}
 *
 * LƯU Ý: trị tuyệt đối 1 dòng ĐƠN GIẢN (|x|, |a-b| gọn) nên gõ "|x|" thẳng
 * (HP V10 Điều 16.1). Chỉ dùng hàm này khi bên trong có phân số dọc hoặc
 * biểu thức cao cần gạch đứng giãn theo — thường gặp ở cấp 3.
 *
 * Ví dụ: para([run("Ta có "), triTuyetDoi("x - 3"), run(" = 5")])
 */
function triTuyetDoi(bieuThuc) {
  const dPr = new BuilderElement({
    name: "m:dPr",
    children: [
      new BuilderElement({ name: "m:begChr", attributes: { val: { key: "m:val", value: "|" } } }),
      new BuilderElement({ name: "m:endChr", attributes: { val: { key: "m:val", value: "|" } } }),
    ],
  });
  const e = new BuilderElement({ name: "m:e", children: [new MathRunSized(String(bieuThuc))] });
  const base = createMathBase({ children: [e] });
  const d = new BuilderElement({ name: "m:d", children: [dPr, base] });
  return new DMath({ children: [d] });
}

/**
 * Hệ phương trình — vẽ dấu ngoặc nhọn "{" chỉ mở, các phương trình xếp
 * dọc bên phải (đúng chuẩn OOXML, giống Word tự vẽ khi Insert Equation
 * → Cases). Trả về object Math CHÈN TRỰC TIẾP vào children của Paragraph
 * (thường dùng riêng 1 dòng, căn giữa — xem paraHePhuongTrinh bên dưới).
 * @param {Array<string>} danhSachPT - mỗi phần tử là 1 phương trình,
 *   AI Soạn tự gõ kèm nhãn nếu cần, ví dụ: "5x + 6y = 4     (1)"
 * @returns {Math}
 *
 * Ví dụ: hePhuongTrinh(["5x + 6y = 4     (1)", "4x − 9y = 17     (2)"])
 */
function hePhuongTrinh(danhSachPT) {
  const hangArr = danhSachPT.map(pt => new BuilderElement({
    name: "m:e", children: [new MathRunSized(String(pt))],
  }));
  const eqArr = new BuilderElement({ name: "m:eqArr", children: hangArr });
  const dPr = new BuilderElement({
    name: "m:dPr",
    children: [
      new BuilderElement({ name: "m:begChr", attributes: { val: { key: "m:val", value: "{" } } }),
      new BuilderElement({ name: "m:endChr", attributes: { val: { key: "m:val", value: "" } } }),
    ],
  });
  const base = createMathBase({ children: [eqArr] });
  const d = new BuilderElement({ name: "m:d", children: [dPr, base] });
  return new DMath({ children: [d] });
}

/**
 * Bản tiện dụng — trả thẳng 1 Paragraph căn giữa chứa hệ phương trình,
 * dùng CHÈN TRỰC TIẾP vào mảng nội dung bài học hoặc vào cacBuoc của
 * loiGiai() (hàm loiGiai tự nhận diện Paragraph và không gộp dòng nó).
 * @param {Array<string>} danhSachPT
 * @param {Object} [opts]
 */
function paraHePhuongTrinh(danhSachPT, opts = {}) {
  return para([hePhuongTrinh(danhSachPT)],
    { align: AlignmentType.CENTER, before: opts.before ?? 4, after: opts.after ?? 4 });
}

// ═════════════════════════════════════════════════════════════
// 21.4. KÝ HIỆU GÓC — OMML chuẩn SGK KNTT Việt Nam
// ═════════════════════════════════════════════════════════════
function kyHieuGoc(tenGoc) {
  const t = String(tenGoc);
  // Chặn cách viết bịa thay cho dấu phẩy: "xPrimOyPrim", "xphayOyphay"...
  if (/prim|phay|dash|apos/i.test(t)) {
    throw new Error(
      `[LỖI TÊN GÓC] kyHieuGoc("${t}") — chứa chữ thay cho dấu phẩy.\n` +
      `  Dấu phẩy phải dùng KÝ TỰ THẬT U+2032 (′), viết thẳng trong chuỗi.\n` +
      `  SAI:  kyHieuGoc("xPrimOyPrim")   → hiện ra "xPrimOyPrim"\n` +
      `  ĐÚNG: kyHieuGoc("x\u2032Oy\u2032")  → hiện ra x′Oy′ có mũ cong\n` +
      `  Trong script .js viết: H.kyHieuGoc("x\u2032Oy\u2032") hoặc dán thẳng ký tự ′.`
    );
  }
  // Chặn nháy đơn thẳng ' (U+0027) và nháy cong ' (U+2019) — phải là ′ (U+2032)
  if (/['\u2019]/.test(t)) {
    throw new Error(
      `[LỖI TÊN GÓC] kyHieuGoc("${t}") — dùng sai loại dấu phẩy.\n` +
      `  Phải dùng U+2032 (′ - prime), KHÔNG dùng ' (U+0027) hay ' (U+2019).\n` +
      `  ĐÚNG: kyHieuGoc("x\u2032Oy\u2032")`
    );
  }
  const acc = new BuilderElement({
    name: "m:acc",
    children: [
      new BuilderElement({
        name: "m:accPr",
        children: [createMathAccentCharacter({ accent: "\u0302" })],
      }),
      createMathBase({ children: [new MathRunSized(String(tenGoc))] }),
    ],
  });
  return new DMath({ children: [acc] });
}


// ═════════════════════════════════════════════════════════════
// 22. HÌNH VẼ MINH HỌA — chèn ảnh PNG đã dựng sẵn (sơ đồ cây, tia số,
//     sơ đồ cột phân tích thừa số...). AI Soạn tự vẽ ảnh bằng công cụ
//     riêng (matplotlib/PIL/canvas...) rồi gọi hàm này để chèn vào bài.
// ═════════════════════════════════════════════════════════════
/**
 * @param {Object} p
 * @param {Buffer} p.imageBuffer - fs.readFileSync(đường dẫn ảnh .png)
 * @param {number} [p.rongCm=8]  - chiều rộng hình theo cm, chiều cao tự tính theo tỉ lệ gốc
 * @param {number} [p.tiLeGoc] - tỉ lệ width/height gốc. [v10.7] TÙY CHỌN — bỏ trống thì template TỰ đọc tỉ lệ từ ảnh PNG (không méo). Truyền tay chỉ để ép khác.
 * @param {string} [p.chuThich]  - chú thích dưới hình, ví dụ "Hình 1. Sơ đồ cây phân tích 60"
 */
// A4 v9.0: ngưỡng đặt ảnh —
//   ≥ 10cm → dòng riêng căn giữa (đã là hành vi cũ, giữ nguyên)
//   < 10cm → vẫn dòng riêng căn giữa (bố cục text box TREO — chờ thầy quyết,
//             tạm thời AI Soạn dùng hàng riêng cho mọi hình theo quyết định hiện tại)
// type:'png' BẮT BUỘC — thiếu → Word thật báo "unreadable content"
// [v10.7] Đọc tỉ lệ rộng/cao THẬT từ ảnh PNG (IHDR: width@16, height@20, big-endian).
//   → hết méo khi quên truyền tiLeGoc; tiLeGoc truyền tay vẫn ưu tiên (ghi đè).
function _tiLeAnh(buf) {
  try {
    if (Buffer.isBuffer(buf) && buf.length > 24 &&
        buf[0] === 0x89 && buf[1] === 0x50 && buf[2] === 0x4e && buf[3] === 0x47) {
      const w = buf.readUInt32BE(16), h = buf.readUInt32BE(20);
      if (w > 0 && h > 0) return w / h;
    }
  } catch (e) { /* đọc lỗi → trả null, dùng mặc định cũ */ }
  return null;
}

function hinhVe({ imageBuffer, rongCm = 8, tiLeGoc, chuThich }) {
  if (!imageBuffer) throw new Error("[LỖI HÌNH] hinhVe(): imageBuffer không được để trống.");
  if (typeof chuThich === "string") _guardKyHieuGoc(chuThich, "hinhVe chuThich");
  const pxWidth = Math.round(rongCm * 37.795);
  const _ratio = tiLeGoc
    ? (typeof tiLeGoc === 'number' ? tiLeGoc : tiLeGoc.width / tiLeGoc.height)
    : (_tiLeAnh(imageBuffer) || 1);  // [v10.7] tự đọc tỉ lệ ảnh (cũ FIX v8.1): nhận cả số lẫn {width,height} như viDuCoHinhBenCanh
  const pxHeight = Math.round(pxWidth / _ratio);
  const out = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 60, after: chuThich ? 10 : 60 },
      children: [new ImageRun({
        data: imageBuffer,
        transformation: { width: pxWidth, height: pxHeight },
        type: "png",   // BẮT BUỘC — không được xóa, xem A4 v9.0
        docId: _nextImgId(),
      })],
    }),
  ];
  if (chuThich) {
    out.push(para([run(chuThich, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { align: AlignmentType.CENTER, before: 0, after: 60 }));
  }
  return out;
}

// ═════════════════════════════════════════════════════════════
// 22a2. HÀNG NHIỀU HÌNH (mục ② lý thuyết) — [v10.4]
//   HP Điều 18.1 (sửa 12/08): 2–3 hình NHỎ liên quan xếp 1 hàng, cả cụm căn giữa.
//   `hangHinh`: 1 hàng ≤3 hình, KHÔNG viền, ô căn dọc giữa, CHUẨN HOÁ cùng chiều cao (caoCm).
//   `luoiHinh`: tự chia hàng theo số lượng đã chốt — 1–3→1 hàng · 4→2+2 · 5→3+2 · 6→3+3.
//   Chỉ dùng cho hình nhỏ + bộ liên quan; hình đơn/lớn/Phần II → vẫn hinhVe (dòng riêng).
// ═════════════════════════════════════════════════════════════
function hangHinh(items, { caoCm = 3.2 } = {}) {
  if (!Array.isArray(items) || !items.length) throw new Error("[LỖI HÌNH] hangHinh(): cần mảng ≥ 1 hình.");
  if (items.length > 3) throw new Error(`[LỖI HÌNH] hangHinh(): 1 hàng tối đa 3 hình (đang ${items.length}). Dùng luoiHinh() để tự chia hàng (4→2+2, 5→3+2, 6→3+3).`);
  const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  const noB = { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE };
  const DXA = cm => Math.round(cm * 567);
  const phH = Math.round(caoCm * 37.795);            // chiều cao chung (px) — CHUẨN HOÁ
  const ws = [];                                     // bề rộng ô (dxa)
  const cells = items.map(it => {
    if (!it.imageBuffer) throw new Error("[LỖI HÌNH] hangHinh(): một phần tử thiếu imageBuffer.");
    if (typeof it.chuThich === "string") _guardKyHieuGoc(it.chuThich, "hangHinh chuThich");
    const ratio = it.tiLeGoc ? (typeof it.tiLeGoc === 'number' ? it.tiLeGoc : it.tiLeGoc.width / it.tiLeGoc.height) : (_tiLeAnh(it.imageBuffer) || 1);  // [v10.7] tự đọc tỉ lệ
    const phW = Math.round(phH * ratio);
    const oCm = phW / 37.795 + 0.5;                  // + lề trái/phải ô
    ws.push(DXA(oCm));
    const kids = [ new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60, after: it.chuThich ? 10 : 60 },
      children: [ new ImageRun({ data: it.imageBuffer, transformation: { width: phW, height: phH }, type: "png", docId: _nextImgId() }) ] }) ];
    if (it.chuThich) kids.push(para([run(it.chuThich, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { align: AlignmentType.CENTER, before: 0, after: 60 }));
    return new TableCell({ borders: noB, verticalAlign: VerticalAlign.CENTER, width: { size: DXA(oCm), type: WidthType.DXA },
      margins: { left: DXA(0.25), right: DXA(0.25) }, children: kids });
  });
  const tongDxa = ws.reduce((s, w) => s + w, 0);
  if (tongDxa > DXA(18.4)) throw new Error(`[LỖI HÌNH] hangHinh(): hàng rộng ${(tongDxa / 567).toFixed(1)}cm > 18.4cm (vùng chữ A4). Giảm caoCm hoặc bớt hình.`);
  return [ new Table({ alignment: AlignmentType.CENTER, borders: noB, width: { size: tongDxa, type: WidthType.DXA },
    columnWidths: ws, rows: [ new TableRow({ children: cells }) ] }) ];
}

function luoiHinh(items, opts = {}) {
  if (!Array.isArray(items) || !items.length) throw new Error("[LỖI HÌNH] luoiHinh(): cần mảng ≥ 1 hình.");
  const n = items.length;
  let chia;
  if (n <= 3) chia = [n];
  else if (n === 4) chia = [2, 2];
  else if (n === 5) chia = [3, 2];
  else if (n === 6) chia = [3, 3];
  else throw new Error(`[LỖI HÌNH] luoiHinh(): ${n} hình — bố cục > 6 chưa chốt. Tách thủ công bằng nhiều hangHinh().`);
  const out = [];
  let i = 0;
  for (const c of chia) { out.push(...hangHinh(items.slice(i, i + c), opts)); i += c; }
  return out;
}

// ═════════════════════════════════════════════════════════════
// 22b. HÌNH BÊN PHẢI — CHỮ WRAP TRÁI (A8 v9.1)
//      HP V10 Điều 18: hình < 10cm + nội dung đủ dài → hình neo bên PHẢI,
//      văn bản (đề bài/lời giải) tự wrap xuống bên TRÁI hình.
//      Dùng FLOATING ImageRun (wp:anchor + wrapSquare) — KHÔNG dùng bảng 2 cột
//      (bảng 2 cột bị CẤM, Điều 18). Đây là hàm thay thế *CoHinhBenCanh đã xóa.
//
//  CÁCH DÙNG — hình phải nằm TRONG paragraph đầu tiên của khối chữ:
//    const anhPhai = H.hinhVeTextBox({ imageBuffer, rongCm:6, tiLeGoc:{width,height}, chuThich:"Hình 1" });
//    children.push(H.paraCoHinhPhai(anhPhai, [
//      run("Bài 1. (VD) ", {bold:true}), run("Cho tam giác ABC..."),
//    ]));
//    // các đoạn chữ tiếp theo push bình thường — vẫn wrap quanh hình
//
//  Hoặc dùng trực tiếp ImageRun trả về, tự chèn vào children của 1 Paragraph.
//
//  LƯU Ý:
//  - CHỈ dùng khi rongCm < 9 VÀ nội dung đủ dài lấp cạnh ảnh (Điều 18.2).
//  - Hình ≥ 10cm hoặc nội dung quá ngắn (1–2 dòng) → dùng H.hinhVe() (dòng riêng).
// ═════════════════════════════════════════════════════════════
/**
 * Trả về 1 ImageRun FLOATING (neo phải, wrap trái) để chèn vào đầu children
 * của Paragraph chứa văn bản.
 * @param {Object} p
 * @param {Buffer} p.imageBuffer
 * @param {number} [p.rongCm=6] - BẮT BUỘC < 9 (Điều 18.2)
 * @param {number|{width,height}} p.tiLeGoc
 * @param {string} [p.chuThich] - hiện chưa gắn trực tiếp lên hình floating;
 *   nếu cần chú thích, đặt dòng nghiêng căn phải ngay sau khối (AI Soạn tự thêm)
 * @returns {ImageRun}
 */
function hinhVeTextBox({ imageBuffer, rongCm = 6, tiLeGoc, chuThich }) {
  if (!imageBuffer) throw new Error("[LỖI HÌNH] hinhVeTextBox(): imageBuffer không được để trống.");
  if (rongCm > 9.1) {
    const cotChu = (18.1 - rongCm).toFixed(1);
    throw new Error(
      `[LỖI HÌNH] hinhVeTextBox(): hình rộng ${rongCm}cm → cột chữ chỉ còn ${cotChu}cm, dưới ngưỡng 9cm.\n` +
      `   HP V10.4 Điều 18.2: cột chữ còn < 9cm thì hình phải để DÒNG RIÊNG CĂN GIỮA → dùng H.hinhVe().\n` +
      `   (Vùng chữ A4 = 18.4cm; ở cột 9cm một dòng chứa ~44 ký tự — ngưỡng dưới để đọc trôi.)`
    );
  }
  if (typeof chuThich === "string") _guardKyHieuGoc(chuThich, "hinhVeTextBox chuThich");
  const pxWidth = Math.round(rongCm * 37.795);
  const _ratio = tiLeGoc
    ? (typeof tiLeGoc === 'number' ? tiLeGoc : tiLeGoc.width / tiLeGoc.height)
    : (_tiLeAnh(imageBuffer) || 1.5);  // [v10.7] tự đọc tỉ lệ ảnh
  const pxHeight = Math.round(pxWidth / _ratio);
  return new ImageRun({
    data: imageBuffer,
    transformation: { width: pxWidth, height: pxHeight },
    type: "png",   // BẮT BUỘC
    docId: _nextImgId(),
    floating: {
      allowOverlap: false,   // [22e] Word TỰ chống đè: 2 hình neo phải không leo lên nhau, tự đẩy xuống
      horizontalPosition: {
        relative: HorizontalPositionRelativeFrom.MARGIN,
        align: HorizontalPositionAlign.RIGHT,   // hình neo PHẢI, chữ wrap trái (HP Điều 18)
      },
      verticalPosition: {
        relative: VerticalPositionRelativeFrom.LINE,
        offset: 0,
      },
      wrap: { type: TextWrappingType.SQUARE, side: TextWrappingSide.LEFT }, // hình neo PHẢI → chữ chảy bên TRÁI
      margins: { left: 90000, bottom: 90000 }, // khe ~0.25cm TRÁI & dưới (chữ nằm bên trái)
    },
  });
}

/**
 * Dựng 1 Paragraph có hình neo phải + văn bản wrap trái.
 * @param {ImageRun} anhFloating - kết quả của hinhVeTextBox()
 * @param {Array} noiDungInline  - mảng run()/toInline() nội dung chữ
 * @param {Object} [opts]        - before/after/align như para()
 * @returns {Paragraph}
 */
function paraCoHinhPhai(anhFloating, noiDungInline, opts = {}) {
  // [v9.4] VÁ BUG: hàm cũ chỉ đọc opts.align nên NUỐT MẤT opts.justify — trong khi
  // viDu/baiTapTaiLop/tuLuanBTVN đều truyền justify:true. Hậu quả: mọi đề bài kèm
  // hình bị căn trái, trái HP Điều 14. Nay đọc justify như para().
  const children = [anhFloating, ...toInline(noiDungInline)];
  return new Paragraph({
    alignment: opts.justify ? AlignmentType.JUSTIFIED : (opts.align || AlignmentType.LEFT),
    spacing: { before: opts.before ?? 6, after: opts.after ?? 0, line: 260 },
    children,
  });
}
//       (khác hinhVe ở trên: hinhVe nhận ảnh AI Soạn tự vẽ/tự dựng theo bài;
//       hinhIcon lấy từ thư mục icons/ có sẵn — dùng cho ký hiệu an toàn/
//       cảnh báo cần chuẩn hóa, hiện phủ Bài 2 và Bài 50, xem Mục 2.2
//       Instructions_AI_Soan_VatLy). AI Soạn KHÔNG được tự vẽ thay thế —
//       nếu thiếu icon cần dùng, DỪNG LẠI báo Ông Bụt bổ sung thư viện.
// ═════════════════════════════════════════════════════════════
const ICON_DIR = path.join(__dirname, "icons");

const ICON_LIBRARY = {
  // Bài 2 — An toàn phòng thực hành
  chat_de_chay:          { file: "chat_de_chay.png",          label: "Chất dễ cháy" },
  chat_doc:              { file: "chat_doc.png",              label: "Chất độc" },
  nguon_dien_nguy_hiem:  { file: "nguon_dien_nguy_hiem.png",  label: "Nguồn điện nguy hiểm" },
  dung_cu_sac_nhon:      { file: "dung_cu_sac_nhon.png",      label: "Dụng cụ sắc nhọn" },
  thuy_tinh_de_vo:       { file: "thuy_tinh_de_vo.png",       label: "Thuỷ tinh dễ vỡ" },
  nhiet_do_cao:          { file: "nhiet_do_cao.png",          label: "Nhiệt độ cao" },
  binh_chua_chay:        { file: "binh_chua_chay.png",        label: "Bình chữa cháy" },
  cam_uong_nuoc:         { file: "cam_uong_nuoc.png",         label: "Cấm uống nước" },
  cam_cham_so:           { file: "cam_cham_so.png",           label: "Cấm chạm/sờ" },
  cam_an_uong:           { file: "cam_an_uong.png",           label: "Cấm ăn uống" },
  // Bài 50 — Năng lượng tái tạo / không tái tạo
  mat_troi:              { file: "mat_troi.png",              label: "Năng lượng Mặt Trời" },
  gio:                   { file: "gio.png",                   label: "Năng lượng gió" },
  nuoc_nang_luong:       { file: "nuoc_nang_luong.png",       label: "Năng lượng nước" },
  dia_nhiet:             { file: "dia_nhiet.png",             label: "Năng lượng địa nhiệt" },
  sinh_khoi:             { file: "sinh_khoi.png",             label: "Năng lượng sinh khối" },
  dau_mo:                { file: "dau_mo.png",                label: "Dầu mỏ" },
  than_da:               { file: "than_da.png",               label: "Than đá" },
  khi_tu_nhien:          { file: "khi_tu_nhien.png",          label: "Khí tự nhiên" },
  urani:                 { file: "urani.png",                 label: "Urani" },
};

/**
 * hinhIcon(tenIcon, opts) — chèn 1 pictogram chuẩn từ ICON_LIBRARY, canh giữa,
 * kèm chú thích nhỏ bên dưới (tùy chọn tắt qua opts.chuThich = false).
 * @param {string} tenIcon - khoá trong ICON_LIBRARY, xem danh sách ở trên hoặc API_REFERENCE.md
 * @param {Object} [opts]
 * @param {number} [opts.size=60]      - kích thước icon (px vuông)
 * @param {boolean} [opts.chuThich=true] - có hiện dòng chú thích tên icon bên dưới không
 * @returns {Paragraph[]} — dùng ...hinhIcon(...) khi push vào children
 */
function hinhIcon(tenIcon, opts = {}) {
  const entry = ICON_LIBRARY[tenIcon];
  if (!entry) {
    throw new Error(
      `hinhIcon(): không tìm thấy icon "${tenIcon}" trong ICON_LIBRARY. ` +
      `DỪNG LẠI và báo Ông Bụt bổ sung thư viện — KHÔNG tự vẽ tay thay thế. ` +
      `Icon hiện có: ${Object.keys(ICON_LIBRARY).join(", ")}`
    );
  }
  const size = opts.size || 60;
  const chuThich = opts.chuThich !== false;
  const imgBuffer = fs.readFileSync(path.join(ICON_DIR, entry.file));

  const out = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 40, after: chuThich ? 4 : 40 },
      children: [new ImageRun({ data: imgBuffer, transformation: { width: size, height: size }, type: "png" })],
    }),
  ];
  if (chuThich) {
    out.push(para([run(entry.label, { italic: true, color: C_GRAY, size: SZ_SMALL })],
      { align: AlignmentType.CENTER, before: 0, after: 40 }));
  }
  return out;
}

/**
 * hinhIconHang(danhSachTen, opts) — chèn nhiều icon nằm ngang trong 1 hàng bảng
 * (dùng cho câu kiểu "biển báo sau có ý nghĩa gì" — SBT Bài 2 câu 2.1/2.2/2.3).
 * @param {string[]} danhSachTen - mảng tên icon trong ICON_LIBRARY
 * @param {Object} [opts]
 * @param {number} [opts.size=55]
 * @returns {Table[]}
 */
function hinhIconHang(danhSachTen, opts = {}) {
  const size = opts.size || 55;
  const bc = { style: BorderStyle.SINGLE, size: 4, color: C_BLACK };
  const borders = { top: bc, bottom: bc, left: bc, right: bc };
  const colW = Math.round(TOTAL_W / danhSachTen.length);

  const cells = danhSachTen.map((ten) => {
    const entry = ICON_LIBRARY[ten];
    if (!entry) {
      throw new Error(`hinhIconHang(): không tìm thấy icon "${ten}" — báo Ông Bụt bổ sung thư viện.`);
    }
    const imgBuffer = fs.readFileSync(path.join(ICON_DIR, entry.file));
    return new TableCell({
      width: { size: colW, type: WidthType.DXA }, borders,
      margins: { top: 100, bottom: 100, left: 60, right: 60 },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new ImageRun({ data: imgBuffer, transformation: { width: size, height: size }, type: "png" })],
        }),
        para([run(entry.label, { italic: true, color: C_GRAY, size: SZ_SMALL - 2 })],
          { align: AlignmentType.CENTER, before: 20, after: 0 }),
      ],
    });
  });

  return [new Table({
    width: { size: TOTAL_W, type: WidthType.DXA },
    columnWidths: danhSachTen.map(() => colW),
    rows: [new TableRow({ children: cells })],
  })];
}

// ═════════════════════════════════════════════════════════════
// 23. TIÊU ĐỀ CÁC PHẦN ĐỀ KIỂM TRA (I/II/III/IV — khác BTVN dùng A/B/C/D)
// ═════════════════════════════════════════════════════════════
function tieuDePhanI_DeKT(soCau, tongDiem) {
  return para([run(`PHẦN I. TRẮC NGHIỆM CHỌN ĐÁP ÁN (${tongDiem} điểm)`,
    { bold: true, underline: true, size: SZ_CONTENT })], { before: THO_RONG, after: 6 });
}
function tieuDePhanII_DeKT(soCau, soMenhDe, tongDiem) {
  return para([run(`PHẦN II. TRẮC NGHIỆM ĐÚNG/SAI (${tongDiem} điểm)`,
    { bold: true, underline: true, size: SZ_CONTENT })], { before: THO_RONG, after: 6 });
}
function tieuDePhanIII_DeKT(soCau, tongDiem) {
  return para([run(`PHẦN III. TRẢ LỜI NGẮN (${tongDiem} điểm)`,
    { bold: true, underline: true, size: SZ_CONTENT })], { before: THO_RONG, after: 6 });
}
function tieuDePhanIV_DeKT(soBai, tongDiem) {
  return para([run(`PHẦN IV. TỰ LUẬN (${tongDiem} điểm)`,
    { bold: true, underline: true, size: SZ_CONTENT })], { before: THO_RONG, after: 6 });
}

module.exports = {
  kiemMay,
  viDuLyThuyet,
  // hằng số (chỉ đọc, KHÔNG sửa)
  TNR, C_BLACK, C_RED, C_RED_ANSWER, C_GRAY, C_WHITE,
  SZ_CONTENT, SZ_TITLE_BAI, SZ_SMALL, SZ_MISTAKE, TOTAL_W,
  THO_RONG, THO_VUA, THO_HEP,
  PAGE_SIZE, PAGE_MARGIN,
  // patch docPr id — gọi sau Packer.toBuffer()
  patchDocPrIds, xuatFile, taoTaiLieu, taoTaiLieuDeKT,
  // helpers cơ sở
  run, para, tabLine, toInline, paraInline, approxLen,
  // phần 1 — bài học
  tenBaiHoc, mucTieu, tieuDeMuc, tieuDeMucChinh, lyThuyet, viDu, layoutCauHoi, loiGiai,
  saiLamThuongGap, ghiNhoNhanh,
  // phần 2 — dạng toán, BT, BTVN, đề kiểm tra
  tieuDeDang, nhanDang, phuongPhapGiai, phanTich, dangToanDayDu,
  baiTapTaiLop, cauTracNghiem, bangDapAnPhanI, bangDungSai, traLoiNgan,
  headerDeKiemTra,
  // phần 3 — header/footer file bài học + đề kiểm tra
  headerFooterBaiHoc, headerFooterDeKT,
  // phần 4 — tờ phân chương (AI QC dùng)
  toPhanChuong, footerTPC, headerRong,
  // phần 5 — tự luận BTVN + tiêu đề các khối
  tuLuanBTVN, tieuDeTuLuan, tieuDePhanI, tieuDePhanII, tieuDePhanIII,
  // phần 6 — trang cuối chương
  ghiChuGiangDay, nhatKyCaiTien, bangNguonGoc, trangCuoiChuong,
  // phần 7 — công thức toán thật (OMML), hình vẽ, tiêu đề phần đề kiểm tra
  luyThua, luyThuaUnicode, phanSo, canBac, chiSoDuoi, triTuyetDoi, kyHieuGoc, hinhVe, hangHinh, luoiHinh, hinhVeTextBox, paraCoHinhPhai, hePhuongTrinh, paraHePhuongTrinh,
  tieuDePhanI_DeKT, tieuDePhanII_DeKT, tieuDePhanIII_DeKT, tieuDePhanIV_DeKT,
  // phần 8 — thư viện pictogram an toàn chuẩn hóa (Bài 2, Bài 50)
  hinhIcon, hinhIconHang, ICON_LIBRARY,
};
