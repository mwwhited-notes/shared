// Minimal CLI around the JS Kaitai compiler: node ksc.js <lang> <outdir> <file.ksy>
const fs = require("fs");
const path = require("path");
const YAML = require("yaml");
const compiler = require("kaitai-struct-compiler");

const [lang, outdir, file] = process.argv.slice(2);
const dir = path.dirname(path.resolve(file));
const importer = {
  importYaml(name, mode) {
    const p = path.join(dir, name + ".ksy");
    return Promise.resolve(YAML.parse(fs.readFileSync(p, "utf8")));
  },
};
const ksy = YAML.parse(fs.readFileSync(file, "utf8"));
compiler.compile(lang, ksy, importer, false).then(
  (files) => {
    fs.mkdirSync(outdir, { recursive: true });
    for (const [name, text] of Object.entries(files)) {
      fs.writeFileSync(path.join(outdir, name), text);
      console.log("wrote", name);
    }
  },
  (err) => {
    console.error("COMPILE ERROR:", err && err.message ? err.message : err);
    process.exit(1);
  }
);
