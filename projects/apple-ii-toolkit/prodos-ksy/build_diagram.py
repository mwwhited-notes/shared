#!/usr/bin/env python3
"""Build prodos_layout.html: block layout diagrams generated from the .ksy specs."""
from pathlib import Path
import figs_a as A
import figs_b as B

HERE = Path(__file__).resolve().parent

CSS = """
/* Layout concept: a reference sheet. One column, each figure in a bordered scroll
   frame, struct rows placed on a shared byte ruler. Color marks what a field is. */
:root{
  --bg:#f4f6f9; --surface:#ffffff; --fg:#18202c; --fg2:#3a4556; --muted:#5a6678; --line:#cbd2dc;
  --c-ptr:#2a68d6; --c-text:#1b8758; --c-time:#a8690f; --c-flag:#7547c9; --c-size:#c23d5b; --c-tag:#566274;
  --sans:"Public Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"DM Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0e131a; --surface:#151b24; --fg:#e7ebf1; --fg2:#c3ccd9; --muted:#97a3b4; --line:#2c3643;
    --c-ptr:#6fa3ff; --c-text:#4fd096; --c-time:#e2ab4d; --c-flag:#b090f2; --c-size:#f27d95; --c-tag:#93a0b2;
    color-scheme:dark;
  }
}
:root[data-theme="dark"]{
  --bg:#0e131a; --surface:#151b24; --fg:#e7ebf1; --fg2:#c3ccd9; --muted:#97a3b4; --line:#2c3643;
  --c-ptr:#6fa3ff; --c-text:#4fd096; --c-time:#e2ab4d; --c-flag:#b090f2; --c-size:#f27d95; --c-tag:#93a0b2;
  color-scheme:dark;
}
body{background:var(--bg);color:var(--fg);font:15px/1.55 var(--sans);padding-inline:16px;padding-block:28px 56px}
main{max-width:980px;margin-inline:auto;display:flex;flex-direction:column;gap:44px}
h1{font-size:clamp(28px,5vw,40px);line-height:1.1;margin:0 0 10px;font-weight:700;letter-spacing:-.01em;text-wrap:balance}
h2{font-size:22px;margin:0 0 4px;font-weight:700;text-wrap:balance}
h3{font-size:14px;margin:18px 0 8px;font-weight:600;letter-spacing:.02em}
p{margin:0;max-width:68ch}
.lede{color:var(--fg2);font-size:16px}
.mono{font-family:var(--mono);font-size:.92em}
nav{display:flex;flex-wrap:wrap;gap:6px 8px;margin-top:16px}
nav a{font:500 12px var(--mono);padding:5px 10px;border:1px solid var(--line);border-radius:999px;color:var(--fg2);text-decoration:none;background:var(--surface)}
nav a:hover,nav a:focus-visible{border-color:var(--fg2);outline:none}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:18px;font:12px var(--mono);color:var(--fg2)}
.legend span{display:inline-flex;align-items:center;gap:7px}
.legend i{width:16px;height:12px;border-radius:2px;border:1.2px solid var(--line);display:inline-block}
section{display:flex;flex-direction:column;gap:12px;scroll-margin-top:16px}
figure{margin:0;display:flex;flex-direction:column;gap:8px;min-width:0}
.scroll{overflow-x:auto;border:1px solid var(--line);border-radius:6px;background:var(--surface);padding:10px 12px}
figcaption{color:var(--muted);font-size:13px;max-width:78ch}
dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 20px;margin:4px 0 0;font-size:14px}
dt{font:500 12.5px/1.7 var(--mono);color:var(--fg)}
dd{margin:0;color:var(--fg2);min-width:0}
@media (max-width:560px){dl{grid-template-columns:1fr;gap:0}dd{margin-bottom:8px}}
footer{color:var(--muted);font-size:13px;border-top:1px solid var(--line);padding-top:14px}
/* svg drawing */
svg.fig{display:block;width:100%;min-width:760px;height:auto;color:var(--fg2)}
svg text{font-family:var(--mono);font-size:12px;fill:var(--fg)}
svg text.m,svg text.off{fill:var(--muted)}
svg text.name{font-weight:500}
svg text.big{font-size:20px;font-weight:500}
.seg{fill:var(--surface);stroke:var(--line);stroke-width:1.3}
.seg.k-ptr{fill:color-mix(in srgb,var(--c-ptr) 22%,var(--surface));stroke:var(--c-ptr)}
.seg.k-text{fill:color-mix(in srgb,var(--c-text) 22%,var(--surface));stroke:var(--c-text)}
.seg.k-time{fill:color-mix(in srgb,var(--c-time) 24%,var(--surface));stroke:var(--c-time)}
.seg.k-flag{fill:color-mix(in srgb,var(--c-flag) 22%,var(--surface));stroke:var(--c-flag)}
.seg.k-size{fill:color-mix(in srgb,var(--c-size) 20%,var(--surface));stroke:var(--c-size)}
.seg.k-tag{fill:color-mix(in srgb,var(--c-tag) 20%,var(--surface));stroke:var(--c-tag)}
.seg.k-res{fill:transparent;stroke:var(--muted);stroke-dasharray:4 3}
.seg.dash{fill:transparent;stroke:var(--muted);stroke-dasharray:5 4}
.grid{stroke:var(--line);stroke-width:1}
.ar{stroke:currentColor;stroke-width:1.4;fill:none}
.legend .k-ptr{background:color-mix(in srgb,var(--c-ptr) 22%,var(--surface));border-color:var(--c-ptr)}
.legend .k-text{background:color-mix(in srgb,var(--c-text) 22%,var(--surface));border-color:var(--c-text)}
.legend .k-time{background:color-mix(in srgb,var(--c-time) 24%,var(--surface));border-color:var(--c-time)}
.legend .k-flag{background:color-mix(in srgb,var(--c-flag) 22%,var(--surface));border-color:var(--c-flag)}
.legend .k-size{background:color-mix(in srgb,var(--c-size) 20%,var(--surface));border-color:var(--c-size)}
.legend .k-tag{background:color-mix(in srgb,var(--c-tag) 20%,var(--surface));border-color:var(--c-tag)}
.legend .k-res{border-style:dashed;border-color:var(--muted)}
"""


def fig(svg, caption):
    return f'<figure><div class="scroll">{svg}</div><figcaption>{caption}</figcaption></figure>'


def notes(pairs):
    return "<dl>" + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in pairs) + "</dl>"


def section(sid, title, intro, *parts):
    return (f'<section id="{sid}"><div><h2>{title}</h2><p>{intro}</p></div>'
            + "".join(parts) + "</section>")


def build():
    dt, ac = A.fig_bits()
    ext_strip, ext_fork = B.fig_extended()
    s = []
    s.append(section(
        "volume", "The volume",
        "A ProDOS volume is a row of 512-byte blocks. Everything else, including the directory, the "
        "free-space bitmap and every file, is found by block number.",
        fig(A.fig_volume_map(), "Blocks 0 to 6 of a typical floppy image. Two pointers do most of the work: "
            "the volume header locates the bitmap, and each file entry locates the file."),
        notes([
            ("block size", "512 bytes. Block numbers are 16 bits, so a volume has at most 65,535 blocks (32 MB)."),
            ("blocks 0–1", "Boot code. The first byte is the number of sectors to load."),
            ("blocks 2–5", "The volume directory. Block 2 is the key block; the others follow through next_ptr."),
            ("bitmap", "One bit per block, 1 = free, block 0 in the top bit of byte 0. One bitmap block covers "
                       "4,096 blocks, so a 280-block floppy needs one."),
        ])))
    s.append(section(
        "directories", "Directories",
        "Volume and subdirectories share one structure: a chain of 512-byte blocks, each cut into 13 slots.",
        fig(A.fig_directory(), "Left: the 512 bytes of one directory block with the byte offset of each slot. "
            "Right: how blocks chain together, and how a subdirectory entry leads to a second chain."),
        notes([
            ("slot size", "39 bytes. Slot 1 of the key block is the header, so the key block holds 12 file entries."),
            ("deleted", "A slot whose storage type is 0 is free. The rest of its bytes are stale, so the spec keeps them raw."),
            ("end of chain", "next_ptr = 0. The key block has prev_ptr = 0."),
        ])))
    s.append(section(
        "slots", "Directory slots",
        "The high nibble of byte 0 says what a 39-byte slot is. Bars show where each field sits across the slot.",
        '<h3>Volume header · storage type F</h3>',
        fig(A.fig_slot("volume_header_body", "", "3a"),
            "Slot 1 of the volume directory key block. bit_map_pointer and total_blocks drive the bitmap."),
        '<h3>Subdirectory header · storage type E</h3>',
        fig(A.fig_slot("subdirectory_header_body", "", "3b"),
            "Slot 1 of a subdirectory key block. The last three fields lead back to the entry in the parent."),
        '<h3>File entry · storage types 1–5 and D</h3>',
        fig(A.fig_slot("file_entry_body", "", "3c"),
            "Any other slot. The end-of-file length is 24 bits, split across eof_low and eof_high."),
        notes([
            ("key_pointer", "Storage 1: the data block. 2: the index block. 3: the master index block. "
                            "5: the extended key block. D: the subdirectory key block."),
            ("eof", "(eof_high << 16) | eof_low, up to 16,777,215 bytes."),
            ("header_pointer", "Key block of the directory that holds this entry."),
            ("case_bits", "version and min_version together carry the GS/OS lowercase flags for the name."),
        ])))
    s.append(section(
        "bits", "Dates and access",
        "Two small bit-packed fields appear in every header and file entry.",
        fig(dt, "created and last_modified. Read the four bytes as one little-endian 32-bit value; "
            "the numbers above each field are bit positions."),
        fig(ac, "The access byte. A set bit grants the permission, except backup, which marks a file "
                "changed since its last backup."),
        notes([
            ("date", "year 7 bits · month 4 · day 5. The spec reads years 0–39 as 2000–2039 and 40–99 as 1940–1999."),
            ("none", "All zero means no date was recorded."),
            ("time", "Minute and hour sit in separate bytes with unused top bits."),
        ])))
    s.append(section(
        "data", "File data",
        "The storage type decides how many pointers lie between a file entry and its data.",
        fig(B.fig_storage(), "Three ways to reach the data. The mono text under each row is the path to read it "
            "with the generated parser."),
        fig(B.fig_index_block(), "Index blocks split each 16-bit pointer across two halves so a pointer can be "
            "fetched without shifting a 2-byte table."),
        notes([
            ("seedling", "At most one block. The spec exposes seedling_data, cut to eof."),
            ("sapling", "One index block of 256 pointers, so up to 131,072 bytes."),
            ("tree", "A master index of up to 128 index blocks, so up to 16,777,216 bytes."),
            ("holes", "Pointer 0 means no block. Treat it as 512 zero bytes when joining the blocks."),
        ])))
    s.append(section(
        "forks", "Forked files",
        "GS/OS files with a data fork and a resource fork use storage type 5.",
        fig(ext_strip, "The extended key block is one 512-byte block with a mini-entry for each fork."),
        fig(ext_fork, "Each fork reuses the seedling, sapling and tree scheme: storage and key_pointer say where "
            "its data starts.")))
    s.append(section(
        "twoimg", "2IMG wrapper",
        "Many emulators store a ProDOS image inside a 2IMG file. The header says where the disk data starts.",
        fig(B.fig_2img_layout(), "File layout. The disk data is parsed as the prodos_volume described above."),
        fig(B.fig_2img_header(), "The 64-byte header. Offsets are from the start of the file."),
        fig(B.fig_2img_flags(), "Flags. Bit 8 says the DOS volume number in bits 0 to 7 is valid; "
            "bit 31 marks the image write-protected.")))
    body = "\n".join(s)
    legend = "".join(f'<span><i class="k-{k}"></i>{t}</span>' for k, t in (
        ("ptr", "pointer or offset"), ("text", "name text"), ("time", "date and time"),
        ("flag", "flags"), ("size", "count or length"), ("tag", "type or version"), ("res", "reserved")))
    nav = "".join(f'<a href="#{i}">{t}</a>' for i, t in (
        ("volume", "volume"), ("directories", "directories"), ("slots", "slots"), ("bits", "dates · access"),
        ("data", "file data"), ("forks", "forks"), ("twoimg", "2IMG")))
    return f"""<title>ProDOS Block Layout</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Public+Sans:wght@400;600;700&display=swap">
<style>{CSS}</style>
<main>
<header>
<h1>ProDOS Block Layout</h1>
<p class="lede">Where each field sits in a ProDOS 8 volume and in the 2IMG file that often wraps it. Offsets and sizes are read from <span class="mono">prodos_volume.ksy</span> and <span class="mono">prodos_2img.ksy</span> when this page is built.</p>
<nav aria-label="Sections">{nav}</nav>
<div class="legend" aria-label="Color key">{legend}</div>
</header>
{body}
<footer>Struct totals are asserted at build time: 39 bytes per directory slot, 64 for the 2IMG header, 8 for a fork mini-entry, 4 for a date.</footer>
</main>
"""


if __name__ == "__main__":
    out = HERE / "prodos_layout.html"
    out.write_text(build())
    print("wrote", out, out.stat().st_size, "bytes")
