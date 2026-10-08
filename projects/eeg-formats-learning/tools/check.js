// Compile every .ksy in a directory to Python with the Kaitai Struct JS compiler.
// Usage: node check.js <ksy_dir> <out_dir>
// Requires kaitai-struct-compiler >= 0.11 (the module is the compiler object itself).
const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const compiler = require('kaitai-struct-compiler');

const [dir, outDir] = process.argv.slice(2);
if (!dir || !outDir) {
  console.error('usage: node check.js <ksy_dir> <out_dir>');
  process.exit(2);
}
fs.mkdirSync(outDir, { recursive: true });

(async () => {
  let failed = 0;
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.ksy')).sort();
  for (const file of files) {
    try {
      const doc = yaml.load(fs.readFileSync(path.join(dir, file), 'utf8'));
      const out = await compiler.compile('python', doc, null, false);
      for (const [name, content] of Object.entries(out)) {
        fs.writeFileSync(path.join(outDir, name), content);
      }
      console.log('OK  ', file);
    } catch (e) {
      failed++;
      console.log('FAIL', file, String(e && e.message ? e.message : e));
    }
  }
  process.exit(failed ? 1 : 0);
})();
