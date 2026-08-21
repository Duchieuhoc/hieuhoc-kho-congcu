// ═══════════════════════════════════════════════════════════════════════════
// gop_chuong.js — NỐI CHƯƠNG BẰNG GHÉP MẢNH MANIFEST (không dựng manifest tay)
// ---------------------------------------------------------------------------
// Quét 1 thư mục chương chứa các gói bài/đề/tổng-kết, mỗi gói mang sẵn
// `00_MANIFEST_MANH.json` mô tả section CỦA CHÍNH NÓ (đường dẫn TƯƠNG ĐỐI).
// Tool: gom mảnh → giải đường dẫn về tuyệt đối → TỰ dựng tờ phân chương →
// XẾP thứ tự chuẩn (bìa · bài theo số · tổng kết · đề 45 A/B · đề 90 A/B) →
// gọi noi_tai_lieu.js. Logo bìa = logo_hieuhoc.png trong kho (PNG thật, 20f).
//
// CÁCH DÙNG
//   node gop_chuong.js <thư_mục_chương> [out.docx]
//   (mặc định out = /mnt/user-data/outputs/TONGHOP_<ma>_GV.docx,
//    với <ma> lấy từ 00_CHUONG.json — tên chuẩn để lưu thư mục Ban_Dung)
//
// CÂY THƯ MỤC CHƯƠNG
//   <chương>/
//     00_CHUONG.json           { "ma":"HH6_CH04", "lop":"TOÁN 6", "tenChuong":"CHƯƠNG IV. ..." }
//     B18/ 00_MANIFEST_MANH.json + build_b18.js + fig/*.png
//     B19/ ... · B20/ ... · TONGKET/ ... · DE45/ ... · DE90/ ...
//
// MẢNH MANIFEST (00_MANIFEST_MANH.json) — mô tả section gói tự đóng góp:
//   { "nhom":"bai"|"tongket"|"de", "thoiluong":45|90 (chỉ đề),
//     "sections":[
//       // BÀI:      { "loai":"buildBai", "script":"build_bXX.js", "soBai":18,
//       //             "tenBai":"...", "lop":"Lớp 6" }
//       // TỔNG KẾT: { "loai":"buildDe", "capture":"document",
//       //             "script":"make_bang.js", "headerTitle":"Tổng kết chương IV" }
//       // ĐỀ:       { "loai":"buildDe", "bo":"A"|"B", "script":"build_deXX_A.js",
//       //             "headerTitle":"..." }
//       // ẢNH:      { "loai":"anh", "png":"sodo.png", "tieuDe":"...", "rongCm":12 }
//     ]
//   }
//   · Đường dẫn (script/cwd/png/stage.fromGlob) TƯƠNG ĐỐI so với thư mục gói.
//   · script phải theo §8 QUY_UOC_GIAO_FILE (ảnh qua __dirname/fig/, xuất qua
//     cửa template, mỗi đề 1 file A/B). stage[] chỉ dùng khi buộc phải vá gói cũ.
//
// TỰ SUY TỜ PHÂN CHƯƠNG: danhSachBai ← các section buildBai (sắp theo soBai);
//   coTongKet ← có nhóm "tongket"; co45/co90 ← có đề thoiluong 45/90.
// ═══════════════════════════════════════════════════════════════════════════
const fs   = require('fs');
const path = require('path');
const { noiTaiLieu } = require('./noi_tai_lieu.js');

const KHO  = __dirname;
const LOGO = path.join(KHO, 'logo_hieuhoc.png');   // PNG thật (mốc 20f)

function docChuongDir(chuongDir) {
  const cfgPath = path.join(chuongDir, '00_CHUONG.json');
  if (!fs.existsSync(cfgPath)) throw new Error(`[gop_chuong] thiếu 00_CHUONG.json ở ${chuongDir}`);
  const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
  if (!cfg.lop || !cfg.tenChuong) throw new Error('[gop_chuong] 00_CHUONG.json cần "lop" và "tenChuong"');
  return cfg;
}

// gom mảnh từ mọi gói con có 00_MANIFEST_MANH.json
function gomManh(chuongDir) {
  const manh = [];
  for (const name of fs.readdirSync(chuongDir).sort()) {
    const dir = path.join(chuongDir, name);
    if (!fs.statSync(dir).isDirectory()) continue;
    const fp = path.join(dir, '00_MANIFEST_MANH.json');
    if (!fs.existsSync(fp)) continue;
    const f = JSON.parse(fs.readFileSync(fp, 'utf8'));
    f.__base = dir; f.__ten = name;
    manh.push(f);
  }
  if (!manh.length) throw new Error(`[gop_chuong] không thấy gói nào có 00_MANIFEST_MANH.json trong ${chuongDir}`);
  return manh;
}

// giải 1 section: đường dẫn tương đối → tuyệt đối; gắn nhãn nhóm để xếp thứ tự
function giaiSection(s, f) {
  const base = f.__base;
  const sec = Object.assign({}, s);
  if (sec.script) sec.script = path.resolve(base, sec.script);
  sec.cwd = sec.cwd ? path.resolve(base, sec.cwd) : base;
  if (sec.png) sec.png = path.resolve(base, sec.png);
  if (Array.isArray(sec.stage))
    sec.stage = sec.stage.map(st => ({
      fromGlob: path.resolve(base, st.fromGlob),
      toDir:    path.isAbsolute(st.toDir) ? st.toDir : path.resolve(base, st.toDir),
      suffix:   st.suffix || '',
    }));
  sec.__nhom = f.nhom;
  sec.__thoiluong = f.thoiluong;
  sec.__bo = s.bo;
  sec.__goi = f.__ten;
  return sec;
}

// khoá xếp thứ tự chuẩn của chương
function khoaThuTu(s) {
  if (typeof s.thutu === 'number') return s.thutu;              // override thủ công nếu có
  if (s.loai === 'buildBai')    return 100 + (s.soBai || 0);    // bài theo số
  if (s.__nhom === 'tongket')   return 500;                     // tổng kết
  if (s.__nhom === 'de')        return 600 + (s.__thoiluong || 0) + (s.__bo === 'B' ? 0.5 : 0); // 45A<45B<90A<90B
  return 999;
}

async function gopChuong(chuongDir, out) {
  chuongDir = path.resolve(chuongDir);
  const cfg = docChuongDir(chuongDir);
  const manh = gomManh(chuongDir);

  const secs = [];
  for (const f of manh) for (const s of (f.sections || [])) secs.push(giaiSection(s, f));

  // tự dựng tờ phân chương từ nội dung gom được
  const bai   = secs.filter(s => s.loai === 'buildBai').sort((a, b) => (a.soBai||0) - (b.soBai||0));
  const has45 = secs.some(s => s.__nhom === 'de' && s.__thoiluong === 45);
  const has90 = secs.some(s => s.__nhom === 'de' && s.__thoiluong === 90);
  const hasTK = secs.some(s => s.__nhom === 'tongket');
  const phanChuong = {
    loai: 'phanChuong', logo: LOGO, lop: cfg.lop, tenChuong: cfg.tenChuong,
    danhSachBai: bai.map(s => ({ soBai: s.soBai, ten: s.tenBai })),
    coTongKet: hasTK, co45: has45, co90: has90,
  };

  secs.sort((a, b) => khoaThuTu(a) - khoaThuTu(b));

  if (!out) {
    let base;
    if (cfg.ma) {
      base = `TONGHOP_${cfg.ma}_GV`;                          // file tổng: tên phẳng 1 gạch
    } else {
      const slug = (cfg.tenChuong.match(/CHƯƠNG\s+([IVXLC0-9]+)/i) || [, 'X'])[1];
      const mon  = cfg.lop.replace(/\s+/g, '');
      base = `TONGHOP_${mon}_CH${slug}_GV`;
    }
    out = `/mnt/user-data/outputs/${base}.docx`;
  }

  console.log(`📑 Ghép chương: ${cfg.tenChuong}`);
  console.log(`   ${bai.length} bài${hasTK ? ' + tổng kết' : ''}${has45 ? ' + đề 45' : ''}${has90 ? ' + đề 90' : ''}  → ${secs.length + 1} section`);
  return noiTaiLieu({ out, sections: [phanChuong, ...secs] });
}

module.exports = { gopChuong };

// CLI
if (require.main === module) {
  const dir = process.argv[2], out = process.argv[3];
  if (!dir) { console.error('Dùng: node gop_chuong.js <thư_mục_chương> [out.docx]'); process.exit(1); }
  gopChuong(dir, out).catch(e => { console.error('❌ LỖI GHÉP CHƯƠNG:', e.message, '\n', e.stack); process.exit(1); });
}
