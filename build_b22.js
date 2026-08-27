// ═══════════════════════════════════════════════════════════════════
// BUILD — HH6_CH05_B22 · Hình có tâm đối xứng · Bản Giáo viên (L1)
// AI Soạn · khung ①→⑤ (⑥⑦ để GỘP CHƯƠNG) · template v10.11 · kho 26f
// ═══════════════════════════════════════════════════════════════════
const fs = require("fs");
const H = require("./hieuhoc_template.js");

const FIG = "/tmp/figs_b22";
const img = t => fs.readFileSync(`${FIG}/${t}.png`);
const META = JSON.parse(fs.readFileSync(`${FIG}/_meta.json`, "utf8"));  // token -> so_o_ngang
const CO_O = 0.8;   // ô lưới = 8mm CỐ ĐỊNH (chỉ đạo Giám đốc)
const RG = t => +Math.min(4.0, Math.max(1.6, CO_O * META[t])).toFixed(3);   // rộng = 0,8×số ô, kẹp 1,6–4cm (hình gói trong 2–5 ô)

// Cỡ hình: hình lưới/phẳng neo-phải 5,5cm · đoạn thẳng 6cm · hình ② căn giữa
// dùng caoCm (luoiHinh/hangHinh chuẩn hoá chiều cao). (0,4×số ô cho B22 ra
// 1,6–3,2cm — vỡ chuẩn đọc 5–6cm mục ③④⑤; đã floor lên 5,5cm, ghi 🟡 OB.)
const W = 5.5;      // neo-phải mặc định
const WD = 6.0;     // đoạn thẳng (tỉ lệ dẹt)
const CAO = 3.0;    // caoCm cho hàng/lưới hình mục ②/④

const rp = (t) => ({ imageBuffer: img(t), rongCm: RG(t) });   // hinhBenPhai / hinhLoiGiai (ô 4mm)

const C = [];   // children

// ─────────────────────────────────────────────────────────────
// TÊN BÀI + ① MỤC TIÊU
// ─────────────────────────────────────────────────────────────
C.push(...H.tenBaiHoc({
  soBai: 22, tenBai: "Hình có tâm đối xứng", tiet: 2,
  sgkTr: "103-107", sbtTr: "84-89", ma: "HH6_CH05_B22",
}));

C.push(...H.mucTieu({
  kienThuc: "hiểu khái niệm hình có tâm đối xứng (quay nửa vòng thì chồng khít); biết tâm đối xứng của một số hình phẳng quen thuộc.",
  kyNang: "nhận biết hình và tâm đối xứng; vẽ thêm để được hình có tâm; gấp - cắt hình có tâm; tính toán đơn giản dựa vào tâm đối xứng.",
  nangLuc: "tư duy trực quan, thẩm mĩ (đối xứng trong tự nhiên và nghệ thuật), giải quyết vấn đề.",
}));

// ─────────────────────────────────────────────────────────────
// ② KIẾN THỨC TRỌNG TÂM
// ─────────────────────────────────────────────────────────────
C.push(H.tieuDeMucChinh("②", "Kiến thức trọng tâm"));
C.push(H.lyThuyet("Nối tiếp Bài 21 (trục đối xứng). Ở Bài 21, hình \"chồng khít\" khi gấp theo một trục; ở Bài 22, hình \"chồng khít\" khi quay nửa vòng quanh một điểm."));
C.push(H.lyThuyet("Định nghĩa. Một hình được gọi là có tâm đối xứng nếu có điểm O sao cho khi quay hình đúng một nửa vòng (180°) quanh O thì hình thu được chồng khít với hình ban đầu. Điểm O gọi là tâm đối xứng của hình."));
C.push(...H.hinhVe({ imageBuffer: img("f02_dn"), rongCm: RG("f02_dn"), chuThich: "Hình 1. Một hình có tâm đối xứng O" }));

C.push(H.lyThuyet("Tâm đối xứng của một số hình phẳng quen thuộc:"));
C.push(H.lyThuyet("• Hình bình hành, hình thoi, hình vuông, hình chữ nhật: tâm đối xứng là giao điểm hai đường chéo."));
C.push(H.lyThuyet("• Hình lục giác đều: tâm đối xứng là giao điểm các đường chéo chính."));
C.push(H.lyThuyet("• Đường tròn: tâm đối xứng là tâm của đường tròn. Đoạn thẳng: tâm đối xứng là trung điểm của đoạn thẳng."));
C.push(H.lyThuyet("• Tam giác đều: không có tâm đối xứng."));
C.push(...H.luoiHinh([
  { imageBuffer: img("f02_bh"), rongCm: RG("f02_bh"), chuThich: "Hình bình hành" },
  { imageBuffer: img("f02_cn"), rongCm: RG("f02_cn"), chuThich: "Hình chữ nhật" },
  { imageBuffer: img("f02_vuong"), rongCm: RG("f02_vuong"), chuThich: "Hình vuông" },
  { imageBuffer: img("f02_lgd"), rongCm: RG("f02_lgd"), chuThich: "Lục giác đều" },
]));

C.push(...H.ghiNhoNhanh([
  "Đa giác đều chẵn cạnh, đường tròn, hình bình hành: CÓ tâm đối xứng.",
  "Tam giác đều và đa giác đều lẻ cạnh: KHÔNG có tâm đối xứng.",
]));

// ─────────────────────────────────────────────────────────────
// ③ CÁC DẠNG TOÁN
// ─────────────────────────────────────────────────────────────
C.push(H.tieuDeMucChinh("③", "Các dạng toán"));

// DẠNG 1 — Nhận biết hình có tâm đối xứng
C.push(...H.dangToanDayDu({
  soDang: 1, tenDang: "Nhận biết hình có tâm đối xứng", ma: "HH6_CH05_B22_D1",
  viDuDeBai: "Xét xem hình (hoặc chữ cái) khi quay nửa vòng có chồng khít với chính nó không.",
  viDuCacCau: [
    "Trong các chữ cái in hoa H, K, M, N, X, những chữ nào có tâm đối xứng?",
    "Trong các hình ngôi sao dưới đây, hình nào có tâm đối xứng?",
  ],
  viDuCoHinh: H.hangHinh([
    { imageBuffer: img("f_d1_sao4"), rongCm: RG("f_d1_sao4"), chuThich: "4 cánh" },
    { imageBuffer: img("f_d1_sao5"), rongCm: RG("f_d1_sao5"), chuThich: "5 cánh" },
    { imageBuffer: img("f_d1_sao6"), rongCm: RG("f_d1_sao6"), chuThich: "6 cánh" },
  ]),
  phanTich: "Chỉ cần hình dung phép quay nửa vòng: chữ cái hoặc hình có số cánh chẵn thường chồng khít, số cánh lẻ thì không.",
  viDuLoiGiai: {
    cacBuoc: [
      "a) Quay nửa vòng: H, N, X chồng khít với chính nó; K, M thì không.",
      "b) Ngôi sao 4 cánh và 6 cánh (chẵn cánh) có tâm đối xứng; ngôi sao 5 cánh (lẻ cánh) không có.",
    ],
    ketLuan: "chữ có tâm đối xứng là H, N, X; hình sao có tâm đối xứng là sao 4 cánh và sao 6 cánh.",
  },
  phuongPhapArr: [
    "Hình dung phép quay nửa vòng quanh tâm dự kiến; nếu hình chồng khít chính nó thì có tâm đối xứng.",
    "Chữ cái in hoa thường có tâm đối xứng: H, I, N, O, S, X, Z.",
  ],
  saiLamArr: [{
    sai: "Cho rằng có trục đối xứng thì có tâm đối xứng.",
    dung: "Trục và tâm là hai tính chất khác nhau; tam giác đều có trục nhưng không có tâm.",
  }],
  ghiNhoArr: ["Chẵn cạnh (hoặc chẵn cánh): thường có tâm; lẻ cạnh: không có tâm."],
}));

// DẠNG 2 — Xác định tâm đối xứng
C.push(...H.dangToanDayDu({
  soDang: 2, tenDang: "Xác định tâm đối xứng của hình phẳng quen thuộc", ma: "HH6_CH05_B22_D2",
  viDuDeBai: "Cho hình lục giác đều ABCDEF. Xác định tâm đối xứng của nó.",
  viDuHinhBenPhai: rp("f_d2_de"),
  phanTich: "Với các hình phẳng quen thuộc, tâm đối xứng là giao điểm các đường chéo (theo bảng ở mục ②).",
  viDuLoiGiai: {
    cacBuoc: [
      "Lục giác đều ABCDEF có ba đường chéo chính là AD, BE, CF.",
      "Ba đường chéo chính cắt nhau tại một điểm O.",
    ],
    ketLuan: "tâm đối xứng của lục giác đều là O, giao điểm ba đường chéo chính AD, BE, CF.",
  },
  phuongPhapArr: [
    "Hình bình hành, hình thoi, hình vuông, hình chữ nhật: tâm là giao hai đường chéo.",
    "Lục giác đều: tâm là giao ba đường chéo chính.",
  ],
  saiLamArr: [{
    sai: "Vẽ nhầm đường chéo phụ của lục giác đều rồi lấy giao làm tâm.",
    dung: "Tâm lục giác đều là giao ba đường chéo chính AD, BE, CF.",
  }],
  ghiNhoArr: ["Tâm hình phẳng quen thuộc = giao các đường chéo (lục giác đều: 3 chéo chính)."],
}));

// DẠNG 3 — Vẽ thêm để được hình nhận O làm tâm
C.push(...H.dangToanDayDu({
  soDang: 3, tenDang: "Vẽ thêm để được hình nhận điểm O làm tâm đối xứng", ma: "HH6_CH05_B22_D3",
  viDuDeBai: "Trên lưới ô vuông, cho phần hình đã tô đậm và điểm O (hình bên). Hãy vẽ thêm để được một hình nhận O làm tâm đối xứng.",
  viDuHinhBenPhai: rp("f_d3_de"),
  phanTich: "Mỗi đỉnh X của phần đã cho được thay bằng điểm X' sao cho O là trung điểm của XX' (đếm ô để xác định X'), rồi nối các điểm X' lại.",
  viDuLoiGiai: {
    cacBuoc: [
      "Với mỗi đỉnh X, lấy X' nằm trên tia đối của tia OX sao cho OX' = OX (đếm số ô: X' đối xứng với X qua O).",
      "Nối các điểm X' vừa dựng theo đúng thứ tự để được phần hình mới (vẽ màu đỏ).",
    ],
    ketLuan: "hình gồm phần đã cho và phần vừa vẽ thêm nhận O làm tâm đối xứng.",
    hinhLoiGiai: rp("f_d3_lg"),
  },
  phuongPhapArr: [
    "Xác định ảnh X' của mỗi đỉnh: X, O, X' thẳng hàng và O là trung điểm XX' (đếm ô).",
    "Nối các ảnh X' theo thứ tự tương ứng để hoàn thành hình.",
  ],
  saiLamArr: [{
    sai: "Lấy đối xứng qua một trục (lật hình) thay vì qua tâm O.",
    dung: "Đối xứng qua tâm: X, O, X' thẳng hàng và O là trung điểm XX'.",
  }],
  ghiNhoArr: ["Đối xứng qua tâm O: O là trung điểm của mỗi đoạn nối một điểm với ảnh của nó."],
}));

// DẠNG 4 — Gấp giấy - cắt hình có tâm
C.push(...H.dangToanDayDu({
  soDang: 4, tenDang: "Gấp giấy - cắt hình có tâm đối xứng", ma: "HH6_CH05_B22_D4",
  viDuDeBai: "Nêu cách gấp một tờ giấy hình chữ nhật rồi cắt để mở ra được chữ H (một hình có tâm đối xứng).",
  viDuHinhBenPhai: rp("f_d4_schema"),
  phanTich: "Gấp đôi hai lần (theo chiều ngang rồi chiều dọc) thì hai nếp gấp cắt nhau tại một điểm O; O sẽ là tâm đối xứng của hình mở ra.",
  viDuLoiGiai: {
    cacBuoc: [
      "Gấp đôi tờ giấy theo chiều ngang, rồi gấp đôi tiếp theo chiều dọc; giao của hai nếp gấp là điểm O.",
      "Trên tờ giấy đã gấp tư, vẽ rồi cắt theo nửa nét của chữ H; mở tờ giấy ra.",
    ],
    ketLuan: "ta được chữ H nhận O làm tâm đối xứng, chỉ với một nhát cắt trên tờ gấp tư.",
  },
  phuongPhapArr: [
    "Gấp tư tờ giấy để tạo tâm O tại giao hai nếp gấp.",
    "Vì hình cần cắt có tâm đối xứng nên chỉ cần cắt một nét trên tờ gấp tư.",
  ],
  saiLamArr: [{
    sai: "Cắt khi giấy chưa gấp đủ hai lần nên hình mở ra không có tâm.",
    dung: "Phải gấp tư (giao hai nếp gấp là O) rồi mới cắt.",
  }],
  ghiNhoArr: ["Gấp tư giấy ⇒ tâm O nằm ở giao hai nếp gấp; hình có tâm chỉ cần một nhát cắt."],
}));

// DẠNG 5 — Tính toán trên hình có tâm đối xứng
C.push(...H.dangToanDayDu({
  soDang: 5, tenDang: "Tính toán trên hình có tâm đối xứng", ma: "HH6_CH05_B22_D5",
  viDuDeBai: "Hình thoi ABCD có cạnh 5 cm, tâm đối xứng O, biết OA = 4 cm và OB = 3 cm (hình bên).",
  viDuCacCau: [
    "Tính diện tích hình thoi ABCD.",
    "So sánh chu vi và diện tích của hai tam giác OAB và OCD.",
  ],
  viDuHinhBenPhai: rp("f_d5_de"),
  phanTich: "O là trung điểm của mỗi đường chéo nên AC = 2 × OA và BD = 2 × OB; hai tam giác OAB và OCD đối xứng nhau qua O.",
  viDuLoiGiai: {
    cacBuoc: [
      "O là trung điểm hai đường chéo nên AC = 2 × OA = 2 × 4 = 8 (cm) và BD = 2 × OB = 2 × 3 = 6 (cm).",
      "a) Diện tích hình thoi: S = (AC × BD) : 2 = (8 × 6) : 2 = 24 (cm²).",
      "b) Hai tam giác OAB và OCD đối xứng nhau qua O nên chúng bằng nhau, do đó có cùng chu vi và cùng diện tích; mỗi tam giác có diện tích (OA × OB) : 2 = (4 × 3) : 2 = 6 (cm²).",
    ],
    ketLuan: "diện tích hình thoi là 24 cm²; hai tam giác OAB và OCD bằng nhau (cùng chu vi, cùng diện tích 6 cm²).",
  },
  phuongPhapArr: [
    "Dùng tính chất O là trung điểm mỗi đường chéo: đường chéo = 2 × nửa đường chéo.",
    "Các phần đối xứng nhau qua O thì bằng nhau (cùng độ dài, chu vi, diện tích).",
  ],
  saiLamArr: [{
    sai: "Lấy OA (nửa đường chéo) làm luôn cả đường chéo AC.",
    dung: "O là trung điểm nên AC = 2 × OA; phải nhân đôi nửa đường chéo.",
  }],
  ghiNhoArr: ["O là trung điểm mỗi đường chéo ⇒ đường chéo = 2 × nửa đường chéo."],
}));

// ─────────────────────────────────────────────────────────────
// ④ BÀI TẬP TẠI LỚP (4 bài)
// ─────────────────────────────────────────────────────────────
C.push(H.tieuDeMucChinh("④", "Bài tập tại lớp"));

C.push(...H.baiTapTaiLop({
  soBai: 1, mucDo: "NB",
  deBai: "Trong các hình dưới đây, hình nào có tâm đối xứng?",
  coHinh: H.hangHinh([
    { imageBuffer: img("f_bt1_thoi"), rongCm: RG("f_bt1_thoi"), chuThich: "Hình a" },
    { imageBuffer: img("f_bt1_tgd"), rongCm: RG("f_bt1_tgd"), chuThich: "Hình b" },
    { imageBuffer: img("f_bt1_tron"), rongCm: RG("f_bt1_tron"), chuThich: "Hình c" },
    { imageBuffer: img("f_bt1_thangcan"), rongCm: RG("f_bt1_thangcan"), chuThich: "Hình d" },
  ]),
  loiGiaiND: {
    cacBuoc: ["Hình a (hình thoi) và hình c (hình tròn) có tâm đối xứng. Hình b (tam giác đều) và hình d (hình thang cân) không có tâm đối xứng."],
    ketLuan: "các hình có tâm đối xứng là hình a và hình c.",
  },
}));

C.push(...H.baiTapTaiLop({
  soBai: 2, mucDo: "TH",
  deBai: "Chỉ ra tâm đối xứng của hình chữ nhật và của hình lục giác đều dưới đây.",
  coHinh: H.hangHinh([
    { imageBuffer: img("f_bt2_cn_de"), rongCm: RG("f_bt2_cn_de"), chuThich: "Hình chữ nhật" },
    { imageBuffer: img("f_bt2_lg_de"), rongCm: RG("f_bt2_lg_de"), chuThich: "Lục giác đều" },
  ]),
  loiGiaiND: {
    cacBuoc: [
      "Hình chữ nhật: tâm đối xứng là giao điểm hai đường chéo.",
      "Lục giác đều: tâm đối xứng là giao điểm ba đường chéo chính.",
    ],
    ketLuan: "tâm đối xứng lần lượt là giao hai đường chéo (hình chữ nhật) và giao ba đường chéo chính (lục giác đều).",
  },
}));

C.push(...H.baiTapTaiLop({
  soBai: 3, mucDo: "VD",
  deBai: "Trên lưới ô vuông, cho hình chữ L đã tô đậm và điểm O (hình bên). Hãy vẽ thêm để được một hình nhận O làm tâm đối xứng.",
  hinhBenPhai: rp("f_bt3_de"),
  loiGiaiND: {
    cacBuoc: ["Lấy ảnh của mỗi đỉnh qua O (O là trung điểm đoạn nối đỉnh với ảnh của nó, đếm ô), rồi nối lại (phần vẽ thêm màu đỏ)."],
    ketLuan: "hình thu được nhận O làm tâm đối xứng.",
    hinhLoiGiai: { imageBuffer: img("f_bt3_lg"), rongCm: RG("f_bt3_lg") },
  },
}));

C.push(...H.baiTapTaiLop({
  soBai: 4, mucDo: "VD",
  deBai: "Nêu cách gấp một mảnh giấy hình chữ nhật rồi cắt để mở ra được chữ N bằng một nhát cắt.",
  hinhBenPhai: rp("f_bt4_gap"),
  loiGiaiND: {
    cacBuoc: ["Gấp đôi mảnh giấy theo chiều ngang rồi gấp đôi tiếp theo chiều dọc (gấp tư); giao hai nếp gấp là O. Vẽ nửa nét chữ N rồi cắt, mở ra được chữ N."],
    ketLuan: "chữ N có tâm đối xứng O nên chỉ cần một nhát cắt trên tờ gấp tư.",
  },
}));

// ─────────────────────────────────────────────────────────────
// ⑤ BÀI TẬP VỀ NHÀ
// ─────────────────────────────────────────────────────────────
C.push(H.tieuDeMucChinh("⑤", "Bài tập về nhà"));

// PHẦN I — 8 câu trắc nghiệm (KHÔNG hình)
C.push(H.tieuDePhanI(8, 2));
C.push(...H.cauTracNghiem({ soCau: 1, cauHoi: "Hình nào sau đây KHÔNG có tâm đối xứng?",
  dapAn: ["Hình vuông", "Hình tròn", "Tam giác đều", "Hình chữ nhật"] }));
C.push(...H.cauTracNghiem({ soCau: 2, cauHoi: "Chữ cái in hoa nào sau đây có tâm đối xứng?",
  dapAn: ["A", "X", "T", "E"] }));
C.push(...H.cauTracNghiem({ soCau: 3, cauHoi: "Tâm đối xứng của hình bình hành là:",
  dapAn: ["một đỉnh của hình", "trung điểm một cạnh", "giao điểm hai đường chéo", "hình bình hành không có tâm"] }));
C.push(...H.cauTracNghiem({ soCau: 4, cauHoi: "Trong các hình: đoạn thẳng, tam giác đều, đường tròn, hình thang cân, số hình có tâm đối xứng là:",
  dapAn: ["1", "2", "3", "4"] }));
C.push(...H.cauTracNghiem({ soCau: 5, cauHoi: "Khẳng định nào sau đây ĐÚNG?",
  dapAn: [
    "Hình có trục đối xứng thì luôn có tâm đối xứng.",
    "Tam giác đều có tâm đối xứng.",
    "Hình có tâm đối xứng thì luôn có trục đối xứng.",
    "Hình bình hành có tâm đối xứng nhưng nói chung không có trục đối xứng.",
  ] }));
C.push(...H.cauTracNghiem({ soCau: 6, cauHoi: "Tâm đối xứng của hình lục giác đều là giao điểm của:",
  dapAn: ["hai cạnh kề", "ba đường chéo chính", "hai đường chéo phụ", "một đường cao và một cạnh"] }));
C.push(...H.cauTracNghiem({ soCau: 7, cauHoi: "Chữ số nào sau đây có tâm đối xứng?",
  dapAn: ["3", "4", "8", "7"] }));
C.push(...H.cauTracNghiem({ soCau: 8, cauHoi: "Đoạn thẳng AB dài 4 cm nhận điểm O làm tâm đối xứng. Khi đó:",
  dapAn: ["OA = 4 cm", "OA = 2 cm", "OA = 8 cm", "O trùng với A"] }));
C.push(H.bangDapAnPhanI(["C", "B", "C", "B", "D", "B", "C", "B"]));

// PHẦN II — 2 câu Đúng/Sai
C.push(H.tieuDePhanII(2, 4, 2));
C.push(H.para([H.run("Câu 1. ", { bold: true }), H.run("Xét tính đúng, sai của mỗi khẳng định sau:")]));
C.push(H.bangDungSai([
  { menhDe: "Hình vuông có tâm đối xứng.", dung: true },
  { menhDe: "Tam giác đều có tâm đối xứng.", dung: false },
  { menhDe: "Đường tròn có tâm đối xứng là tâm của nó.", dung: true },
  { menhDe: "Hình thang cân có tâm đối xứng.", dung: false },
]));
C.push(H.para([H.run("Câu 2. ", { bold: true }), H.run("Cho hình bình hành ABCD có O là giao điểm hai đường chéo (hình vẽ). Xét tính đúng, sai của mỗi khẳng định:")]));
C.push(...H.hinhVe({ imageBuffer: img("f02_bh"), rongCm: RG("f02_bh"), chuThich: "Hình bình hành ABCD, tâm O" }));
C.push(H.bangDungSai([
  { menhDe: "O là tâm đối xứng của hình bình hành ABCD.", dung: true },
  { menhDe: "O là trung điểm của đường chéo AC.", dung: true },
  { menhDe: "Hình bình hành ABCD có đúng một tâm đối xứng.", dung: true },
  { menhDe: "Hình bình hành ABCD luôn có một trục đối xứng đi qua O.", dung: false },
]));

// PHẦN III — 2 câu trả lời ngắn
C.push(H.tieuDePhanIII(2, 2));
C.push(...H.traLoiNgan({ soCau: 1,
  cauHoi: "Đoạn thẳng AB dài 4 cm nhận điểm O làm tâm đối xứng. Tính độ dài OA.",
  dapAn: "OA = 2 cm (O là trung điểm của AB)." }));
C.push(...H.traLoiNgan({ soCau: 2,
  cauHoi: "Hình thoi ABCD có tâm đối xứng O. Biết AC = 8 cm, BD = 6 cm. Tính diện tích hình thoi ABCD.",
  dapAn: "S = (AC × BD) : 2 = (8 × 6) : 2 = 24 (cm²)." }));

// TỰ LUẬN — 5 bài × 1đ
C.push(H.tieuDeTuLuan(5, 5));
C.push(...H.tuLuanBTVN({
  soBai: 1, mucDo: "VD", diem: 1,
  deBai: "Trên lưới ô vuông, cho phần hình đã tô đậm và điểm O (hình dưới). Hãy vẽ thêm để được một hình nhận O làm tâm đối xứng.",
  hinhBenPhai: rp("f_tl1_de"),
  loiGiaiND: {
    cacBuoc: ["Lấy ảnh X' của mỗi đỉnh X qua O (O là trung điểm XX', đếm ô), rồi nối các ảnh theo thứ tự (phần vẽ thêm màu đỏ)."],
    ketLuan: "hình thu được nhận O làm tâm đối xứng.",
    hinhLoiGiai: { imageBuffer: img("f_tl1_lg"), rongCm: RG("f_tl1_lg") },
  },
}));
C.push(...H.tuLuanBTVN({
  soBai: 2, mucDo: "VD", diem: 1,
  deBai: "Trên lưới ô vuông, cho hình đã tô đậm và điểm O (hình dưới). Hãy vẽ thêm để được một hình nhận O làm tâm đối xứng.",
  hinhBenPhai: rp("f_tl2_de"),
  loiGiaiND: {
    cacBuoc: ["Dựng ảnh của mỗi đỉnh qua O (O là trung điểm đoạn nối đỉnh với ảnh của nó), rồi nối lại (phần vẽ thêm màu đỏ)."],
    ketLuan: "hình thu được nhận O làm tâm đối xứng.",
    hinhLoiGiai: { imageBuffer: img("f_tl2_lg"), rongCm: RG("f_tl2_lg") },
  },
}));
C.push(...H.tuLuanBTVN({
  soBai: 3, mucDo: "VD", diem: 1,
  deBai: "Nêu cách gấp một tờ giấy hình chữ nhật rồi cắt để mở ra được một hình có tâm đối xứng (chẳng hạn chữ H).",
  hinhBenPhai: rp("f_tl3_gap"),
  loiGiaiND: {
    cacBuoc: ["Gấp đôi tờ giấy theo chiều ngang rồi gấp đôi tiếp theo chiều dọc (gấp tư); giao hai nếp gấp là O. Vẽ nửa nét của hình cần cắt rồi cắt, sau đó mở ra."],
    ketLuan: "hình mở ra nhận O (giao hai nếp gấp) làm tâm đối xứng.",
  },
}));
C.push(...H.tuLuanBTVN({
  soBai: 4, mucDo: "VD", diem: 1,
  deBai: "Một mặt bàn hình lục giác đều ABCDEF có đường chéo chính AD = 1,2 m và tâm đối xứng O (hình bên). Tính chu vi mặt bàn.",
  hinhBenPhai: rp("f02_lgd"),
  loiGiaiND: {
    cacBuoc: [
      "O là trung điểm đường chéo chính AD nên OA = AD : 2 = 1,2 : 2 = 0,6 (m).",
      "Với lục giác đều, độ dài cạnh bằng khoảng cách từ tâm đến đỉnh, tức là bằng OA = 0,6 m.",
      "Chu vi mặt bàn: P = 6 × 0,6 = 3,6 (m).",
    ],
    ketLuan: "chu vi mặt bàn là 3,6 m.",
  },
}));
C.push(...H.tuLuanBTVN({
  soBai: 5, mucDo: "VDC", diem: 1,
  deBai: "Hình thoi ABCD có tâm đối xứng O. Biết OA = 6 cm và OB = 4 cm (hình bên).",
  cacCau: ["Tính độ dài AC và BD.", "Tính diện tích hình thoi ABCD."],
  hinhBenPhai: rp("f_tl5_thoi"),
  loiGiaiND: {
    cacBuoc: [
      "a) O là trung điểm mỗi đường chéo nên AC = 2 × OA = 2 × 6 = 12 (cm) và BD = 2 × OB = 2 × 4 = 8 (cm).",
      "b) Diện tích hình thoi: S = (AC × BD) : 2 = (12 × 8) : 2 = 48 (cm²).",
    ],
    ketLuan: "AC = 12 cm, BD = 8 cm và diện tích hình thoi là 48 cm².",
  },
}));

// ─────────────────────────────────────────────────────────────
// XUẤT FILE
// ─────────────────────────────────────────────────────────────
(async () => {
  const doc = H.taoTaiLieu({ soBai: 22, tenBai: "Hình có tâm đối xứng", lop: "Lớp 6", children: C });
  const out = "/mnt/user-data/outputs/BANDUNG__HH6_CH05_B22__L1.docx";
  await H.xuatFile(doc, out);
  console.log("✅ XUẤT OK:", out);
})().catch(e => { console.error(e.message || e); process.exit(1); });
