// ═══════════════════════════════════════════════════════════════════════════
// noi_tai_lieu.js — CÔNG CỤ NỐI TÀI LIỆU CHUẨN (manifest-driven)
// ---------------------------------------------------------------------------
// Gộp nhiều bài/đề/ảnh + tờ phân chương → 1 .docx nhiều section, header/footer
// đúng loại, số trang tự chạy. docx-lib tự cấp rId/tên ảnh duy nhất nên KHÔNG
// cần prefix ảnh (khác hẳn ghép nhị phân). Bake guard xmllint trước khi ghi.
//
// CÁCH DÙNG
//   node noi_tai_lieu.js <manifest.json>
//   const { noiTaiLieu } = require('./noi_tai_lieu.js'); await noiTaiLieu(manifest)
//
// MANIFEST (JSON)
// {
//   "out": "/mnt/user-data/outputs/....docx",
//   "sections": [
//     // 1) Tờ phân chương (mẫu chuẩn toPhanChuong)
//     { "loai":"phanChuong", "logo":"<png thật>", "lop":"TOÁN 6",
//       "tenChuong":"CHƯƠNG VIII. ...",
//       "danhSachBai":[{"soBai":32,"ten":"..."}, ...],
//       "coTongKet":true, "co45":true, "co90":true },
//
//     // 2) Bài học — chạy build script, bắt children qua taoTaiLieu
//     { "loai":"buildBai", "script":"<.../build_bXX.js>", "cwd":"<thư mục chạy>",
//       "soBai":32, "tenBai":"...", "lop":"Lớp 6",
//       "stage":[{"fromGlob":"<.../fig/*.png>","toDir":"/tmp","suffix":"-1"}] },  // tuỳ chọn: vá script đọc ảnh lệch quy ước
//
//     // 3) Đề kiểm tra — build script; nếu script dựng `new Document` trực tiếp
//     //    (bản cũ) đặt "capture":"document"; nếu qua taoTaiLieuDeKT thì bỏ.
//     { "loai":"buildDe", "script":"<.../build_XX.js>", "cwd":"<...>",
//       "headerTitle":"Đề kiểm tra ... (Đề A)", "capture":"document" },
//
//     // 4) Ảnh 1 trang (vd sơ đồ tổng kết TikZ→PNG)
//     { "loai":"anh", "png":"<...png>", "tieuDe":"SƠ ĐỒ TỔNG KẾT ...",
//       "headerTitle":"Tổng kết chương ...", "rongCm":12 }
//   ]
// }
//
// GHI CHÚ
//   - "cwd" đặt = thư mục để `readFileSync('fig/..')` trong script trỏ đúng.
//     Script đọc ảnh theo __dirname thì cwd không quan trọng.
//   - Ảnh DỌC (cao>rộng): đặt rongCm nhỏ để chiều cao ≤ ~20cm, tránh tràn trang.
//   - logo phải là PNG THẬT (không phải JPEG đội đuôi .png) — tool sẽ chặn nếu sai.
// ═══════════════════════════════════════════════════════════════════════════
const path = require('path');
const fs   = require('fs');
const Module = require('module');
const { execFileSync } = require('child_process');

const KHO      = __dirname;
const TEMPLATE = path.join(KHO, 'hieuhoc_template.js');

// ── nạp template + docx MỘT lần, patch cửa bắt ───────────────────────────────
const H    = require(TEMPLATE);
const docx = require('docx');
const { Document, Packer, SectionType, Paragraph, TextRun, AlignmentType } = docx;

const _captured = [];
H.taoTaiLieu     = ({ soBai, tenBai, lop, children }) => { _captured.push({ kind:'bai', soBai, tenBai, lop, children }); return { __cap:true }; };
H.taoTaiLieuDeKT = ({ tenDe, children })              => { _captured.push({ kind:'de', tenDe, children });            return { __cap:true }; };
H.xuatFile       = async () => '/dev/null';

// ── require hook: template + docx → 1 instance kho (để patch có hiệu lực) ─────
const DOCX_PATH = require.resolve('docx');
const _origResolve = Module._resolveFilename;
Module._resolveFilename = function (request, parent, ...rest) {
  if (request === './hieuhoc_template.js' || request.endsWith('/hieuhoc_template.js')) return TEMPLATE;
  if (request === 'docx') return DOCX_PATH;
  return _origResolve.call(this, request, parent, ...rest);
};
process.on('unhandledRejection', e => { console.error('⚠️ unhandledRejection:', e && e.message); });

// ── CaptureDoc cho script dựng `new Document` trực tiếp (đề bản cũ) ───────────
const _RealDocument = docx.Document;
function _makeCaptureDoc(tenDe) {
  return class {
    constructor(opts) {
      const secs = (opts && opts.sections) || [];
      _captured.push({ kind:'de', tenDe, children: secs.flatMap(s => s.children || []) });
    }
  };
}

// ── stage: copy ảnh vá quy ước (vd script đọc /tmp/{name}{suffix}.png) ────────
function _runStage(stage) {
  if (!Array.isArray(stage)) return;
  for (const st of stage) {
    const dir = path.dirname(st.fromGlob);
    const rx  = new RegExp('^' + path.basename(st.fromGlob).replace(/\./g, '\\.').replace(/\*/g, '.*') + '$');
    for (const f of fs.readdirSync(dir)) {
      if (!rx.test(f)) continue;
      const ext = path.extname(f), base = path.basename(f, ext);
      fs.copyFileSync(path.join(dir, f), path.join(st.toDir, base + (st.suffix || '') + ext));
    }
  }
}

// ── nạp 1 build script trong đúng cwd (+ tráo Document nếu cần bắt) ───────────
function _napScript(scriptPath, cwdDir, deTitleForDoc) {
  const truoc = process.cwd();
  process.chdir(cwdDir);
  if (deTitleForDoc) docx.Document = _makeCaptureDoc(deTitleForDoc);
  try { require(scriptPath); }
  finally { docx.Document = _RealDocument; process.chdir(truoc); }
}

// ── guard: docx well-formed (bake §3 — xmllint mọi .xml) ─────────────────────
function _validateDocx(buf) {
  const AdmZip = require('adm-zip');
  const zip = new AdmZip(buf);
  const tmp = fs.mkdtempSync(path.join(require('os').tmpdir(), 'noikt_'));
  const loi = [];
  for (const e of zip.getEntries()) {
    if (!e.entryName.endsWith('.xml')) continue;
    const p = path.join(tmp, path.basename(e.entryName));
    fs.writeFileSync(p, e.getData());
    try { execFileSync('xmllint', ['--noout', p], { stdio: 'pipe' }); }
    catch (err) { loi.push(`${e.entryName}: ${(err.stderr || '').toString().trim() || 'malformed'}`); }
  }
  fs.rmSync(tmp, { recursive: true, force: true });
  if (loi.length) throw new Error('[GUARD XML] docx có XML hỏng:\n  ' + loi.join('\n  '));
}

// ── ENGINE ───────────────────────────────────────────────────────────────────
async function noiTaiLieu(manifest) {
  const secProps = { page: { size: H.PAGE_SIZE, margin: H.PAGE_MARGIN }, type: SectionType.NEXT_PAGE };
  const sections = [];

  for (const sec of manifest.sections) {
    switch (sec.loai) {

      case 'phanChuong': {
        const logoBuffer = fs.readFileSync(sec.logo);
        if (logoBuffer[0] === 0xFF && logoBuffer[1] === 0xD8)
          throw new Error(`[LOGO] "${sec.logo}" là JPEG (đội đuôi .png). Cần PNG thật (toPhanChuong ép type:"png").`);
        const children = H.toPhanChuong({
          logoBuffer, lop: sec.lop, tenChuong: sec.tenChuong, danhSachBai: sec.danhSachBai,
          coTongKet: !!sec.coTongKet, co45: sec.co45 !== false, co90: sec.co90 !== false,
        });
        sections.push({ properties: { page: secProps.page }, headers: { default: H.headerRong() }, footers: { default: H.footerTPC() }, children });
        break;
      }

      case 'buildBai': {
        _runStage(sec.stage);
        const before = _captured.length;
        _napScript(sec.script, sec.cwd);
        await new Promise(r => setTimeout(r, 60));
        const cap = _captured[_captured.length - 1];
        if (_captured.length === before || cap.kind !== 'bai')
          throw new Error(`[buildBai] không bắt được children: ${sec.script}`);
        const { header, footer } = H.headerFooterBaiHoc({
          soBai: sec.soBai ?? cap.soBai, tenBai: sec.tenBai ?? cap.tenBai, lop: sec.lop ?? cap.lop ?? 'Lớp 6',
        });
        sections.push({ properties: secProps, headers: { default: header }, footers: { default: footer }, children: cap.children });
        break;
      }

      case 'buildDe': {
        _runStage(sec.stage);
        const before = _captured.length;
        _napScript(sec.script, sec.cwd, sec.capture === 'document' ? (sec.headerTitle || 'Đề kiểm tra') : null);
        await new Promise(r => setTimeout(r, 60));
        const cap = _captured[_captured.length - 1];
        if (_captured.length === before || cap.kind !== 'de')
          throw new Error(`[buildDe] không bắt được children: ${sec.script}`);
        const { header, footer } = H.headerFooterDeKT({ tenDe: sec.headerTitle || cap.tenDe });
        sections.push({ properties: secProps, headers: { default: header }, footers: { default: footer }, children: cap.children });
        break;
      }

      case 'anh': {
        const png = fs.readFileSync(sec.png);
        const ratio = png.readUInt32BE(16) / png.readUInt32BE(20);   // w/h từ IHDR
        const children = [];
        if (sec.tieuDe) children.push(new Paragraph({
          alignment: AlignmentType.CENTER, spacing: { before: 0, after: 120 },
          children: [new TextRun({ text: sec.tieuDe, font: H.TNR, size: H.SZ_TITLE_BAI, bold: true, color: H.C_RED })],
        }));
        children.push(...H.hinhVe({ imageBuffer: png, rongCm: sec.rongCm || 12, tiLeGoc: ratio, chuThich: sec.chuThich }));
        const { header, footer } = H.headerFooterDeKT({ tenDe: sec.headerTitle || sec.tieuDe || 'Tài liệu' });
        sections.push({ properties: secProps, headers: { default: header }, footers: { default: footer }, children });
        break;
      }

      default:
        throw new Error(`[noiTaiLieu] loại section lạ: ${sec.loai}`);
    }
    console.log(`  ✓ ${sec.loai}${sec.soBai ? ' '+sec.soBai : ''}`);
  }

  const doc = new Document({ sections, styles: { default: { document: { run: { font: H.TNR, size: H.SZ_CONTENT } } } } });
  let buf = await Packer.toBuffer(doc);
  buf = H.patchDocPrIds(buf);          // vá docPr id toàn cục
  _validateDocx(buf);                  // GUARD: chặn nếu XML hỏng
  fs.mkdirSync(path.dirname(manifest.out), { recursive: true });
  fs.writeFileSync(manifest.out, buf);
  console.log(`✅ NỐI XONG → ${manifest.out}  (${sections.length} section, XML sạch)`);
  return { out: manifest.out, soSection: sections.length };
}

module.exports = { noiTaiLieu };

// CLI
if (require.main === module) {
  const mf = process.argv[2];
  if (!mf) { console.error('Dùng: node noi_tai_lieu.js <manifest.json>'); process.exit(1); }
  const manifest = JSON.parse(fs.readFileSync(mf, 'utf8'));
  noiTaiLieu(manifest).catch(e => { console.error('❌ LỖI NỐI:', e.message, '\n', e.stack); process.exit(1); });
}
