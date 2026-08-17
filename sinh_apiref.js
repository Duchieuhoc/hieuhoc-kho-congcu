#!/usr/bin/env node
/* sinh_apiref.js — SINH API_REFERENCE.md TỪ hieuhoc_template.js (introspect)
 * Nguồn chân lý = template. Chạy lại mỗi khi template đổi → API_REF không bao giờ lỗi thời.
 * Dùng: node sinh_apiref.js [đường_dẫn_template] > API_REFERENCE.md
 * Nguyên tắc: KHÔNG chế nội dung — chỉ trích chữ ký + comment mô tả có sẵn trong code.
 */
const fs = require("fs");
const SRC = process.argv[2] || "hieuhoc_template.js";
const code = fs.readFileSync(SRC, "utf8");
const lines = code.split("\n");

// 1) Version template (từ header comment "VERSION: v10.11")
const ver = (code.match(/VERSION:\s*(v[\d.]+)/) || [,"?"])[1];
const verDate = (code.match(/VERSION:\s*v[\d.]+\s*\(([\d-]+)\)/) || [,"?"])[1];

// 2) Bản đồ: tên hàm -> {sig, desc}; và tên -> dòng định nghĩa
//    Lấy nguyên chữ ký bằng cân ngoặc từ "function TEN("
function extractSig(name) {
  const re = new RegExp("^function\\s+" + name + "\\s*\\(", "m");
  const m = re.exec(code);
  if (!m) return null;
  let i = m.index + m[0].length - 1; // tại '('
  let depth = 0, out = "";
  for (; i < code.length; i++) {
    const ch = code[i];
    if (ch === "(") depth++;
    else if (ch === ")") { depth--; if (depth === 0) break; }
    if (depth >= 1 && !(ch === "(" && depth === 1)) out += ch;
  }
  let sig = out.trim();
  // Hàm nhận (p): quét thân lấy p.key + destructure const {..}=p
  if (/^p\b/.test(sig)) {
    const start = code.indexOf("{", i);
    // thân = tới "function " kế tiếp ở đầu dòng, hoặc module.exports
    const rest = code.slice(start);
    const stop = rest.search(/\n(function\s|module\.exports)/);
    const body = stop > 0 ? rest.slice(0, stop) : rest;
    const keys = new Set();
    (body.match(/\bp\.([a-zA-Z_][\w]*)/g) || []).forEach(x => keys.add(x.slice(2)));
    const destr = body.match(/const\s*\{([^}]*)\}\s*=\s*p\b/);
    if (destr) destr[1].split(",").forEach(k => { k = k.trim().split(/[:=]/)[0].trim(); if (k) keys.add(k); });
    if (keys.size) sig = "{ " + [...keys].join(", ") + " }";
  }
  return sig;
}
// Comment mô tả = chuỗi dòng "//" liền ngay trên "function TEN"
function extractDesc(name) {
  const idx = lines.findIndex(l => new RegExp("^function\\s+" + name + "\\s*\\(").test(l));
  if (idx < 0) return "";
  const buf = [];
  for (let j = idx - 1; j >= 0; j--) {
    const t = lines[j].trim();
    if (t.startsWith("//")) buf.unshift(t.replace(/^\/\/\s?/, ""));
    else break;
  }
  // Lọc rác: bỏ chuỗi ký tự kẻ khung/divider (═ ─ ━ = -) dài, gộp khoảng trắng
  const cleaned = buf
    .map(l => l.replace(/[═─━╌╍]{2,}/g, " ").replace(/[=\-]{4,}/g, " ").replace(/\s{2,}/g, " ").trim())
    .filter(Boolean);
  return cleaned.join(" ").trim();
}
function isFunction(name) {
  return new RegExp("^function\\s+" + name + "\\s*\\(", "m").test(code);
}

// 3) Parse khối module.exports giữ nguyên thứ tự + comment mục
const expBlock = code.slice(code.indexOf("module.exports = {"));
const expLines = expBlock.slice(0, expBlock.indexOf("};")).split("\n").slice(1);
const items = []; // {type:'section',text} | {type:'name',name}
for (const raw of expLines) {
  const line = raw.trim();
  if (!line) continue;
  const cm = line.match(/^\/\/\s?(.*)$/);
  if (cm) { items.push({ type: "section", text: cm[1] }); continue; }
  // tách các tên trên cùng dòng
  line.replace(/\/\/.*$/, "").split(",").forEach(tok => {
    const n = tok.trim();
    if (n) items.push({ type: "name", name: n });
  });
}

// 4) Xuất Markdown
const out = [];
out.push(`# API_REFERENCE.md — Tham chiếu nhanh \`hieuhoc_template.js\` (${ver})`);
out.push(`> **Tự sinh** bởi \`sinh_apiref.js\` từ template ${ver} (${verDate}) — KHÔNG sửa tay (sửa sẽ mất khi regen). Cập nhật: chạy lại \`node sinh_apiref.js hieuhoc_template.js > API_REFERENCE.md\`.`);
out.push(`> Bản rút gọn thay template đầy đủ trong Project (tiết kiệm token). AI Soạn GỌI HÀM theo chữ ký dưới; không tự viết OOXML.\n`);

const consts = [];
let curSection = null;
for (const it of items) {
  if (it.type === "section") {
    if (/hằng số/i.test(it.text)) { curSection = "const"; continue; }
    curSection = "fn";
    out.push(`\n## ${it.text}`);
    continue;
  }
  const name = it.name;
  if (isFunction(name)) {
    const sig = extractSig(name);
    const desc = extractDesc(name);
    out.push(`### \`${name}(${sig || ""})\``);
    if (desc) out.push(desc);
  } else {
    consts.push(name); // hằng số / re-export không phải hàm
  }
}
if (consts.length) {
  out.push(`\n## Hằng số & tham chiếu (chỉ đọc)`);
  out.push(consts.map(c => "`" + c + "`").join(" · "));
}

// Thống kê
const nFn = items.filter(i => i.type === "name" && isFunction(i.name)).length;
out.push(`\n---`);
out.push(`*Tự sinh: ${nFn} hàm + ${consts.length} hằng/tham chiếu · template ${ver} (${verDate}) · sinh_apiref.js.*`);

process.stdout.write(out.join("\n") + "\n");
process.stderr.write(`[sinh_apiref] ${nFn} hàm, ${consts.length} hằng — template ${ver}\n`);
