"""Figures 5-7: file data trees, index block layout, forked files, 2IMG."""
from diagram_lib import (svg_open, arrow, curve, text, box, waterfall, bit_strip,
                         segs_from_ksy, esc)
from layout import VOL, IMG, fields, total_bytes


def blk(x, y, w, h, k, l1, l2=None, dash=False):
    cls = f"seg k-{k}" if k else "seg"
    if dash:
        cls += " dash"
    o = f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>'
    if l2:
        o += text(x + w / 2, y + h / 2 - 2, l1, "name", "middle")
        o += text(x + w / 2, y + h / 2 + 14, l2, "m", "middle")
    else:
        o += text(x + w / 2, y + h / 2 + 5, l1, "name", "middle")
    return o


def fan(x1, y1, x2, y2, uid):
    return (f'<path class="ar" fill="none" d="M{x1} {y1} C{x1 + 34} {y1} {x2 - 34} {y2} {x2} {y2}" '
            f'marker-end="url(#ah{uid})"/>')


def fig_storage(uid="5"):
    W, H = 920, 560
    o = [svg_open(W, H, "Seedling files keep one data block, sapling files add an index block of "
                  "256 pointers, tree files add a master index of up to 128 index blocks.", uid)]
    ex, ew, eh = 20, 130, 46
    # --- seedling
    y = 36
    o.append(text(20, y - 12, "seedling · storage 1 · up to 512 bytes", "name"))
    o.append(blk(ex, y, ew, eh, "text", "file entry", "key_pointer"))
    o.append(arrow(ex + ew + 2, y + 23, 258, y + 23, uid))
    o.append(blk(260, y, 120, eh, "", "data block", "512 B"))
    o.append(text(410, y + 27, "contents.seedling_data", "m"))
    # --- sapling: index block fans out to data blocks
    y0 = 130
    o.append(text(20, y0 - 12, "sapling · storage 2 · up to 256 blocks = 128 KB", "name"))
    o.append(blk(ex, y0 + 58, ew, eh, "text", "file entry", "key_pointer"))
    o.append(arrow(ex + ew + 2, y0 + 81, 258, y0 + 81, uid))
    o.append(blk(260, y0 + 58, 120, eh, "ptr", "index block", "256 pointers"))
    stack = [("data", "pointers[0]", False), ("hole", "pointers[1] = 0", True),
             ("…", "up to pointers[255]", True)]
    for n, (a_, b_, dsh) in enumerate(stack):
        yy = y0 + n * 58 * 1 + (0 if n == 0 else 0)
        yy = y0 + n * 58
        o.append(blk(450, yy, 150, eh, "", a_, b_, dash=dsh))
        o.append(fan(382, y0 + 81, 448, yy + 23, uid))
    o.append(text(620, y0 + 81, "contents.sapling_index.pointers[i].data", "m"))
    # --- tree
    y0 = 350
    o.append(text(20, y0 - 12, "tree · storage 3 · up to 128 × 256 blocks = 16 MB", "name"))
    o.append(blk(ex, y0 + 45, ew, eh, "text", "file entry", "key_pointer"))
    o.append(arrow(ex + ew + 2, y0 + 68, 258, y0 + 68, uid))
    o.append(blk(260, y0 + 45, 120, eh, "ptr", "master index", "128 pointers"))
    for j, yy in enumerate((y0, y0 + 90)):
        o.append(blk(450, yy, 110, eh, "ptr", "index block", f"pointers[{j}]"))
        o.append(fan(382, y0 + 68, 448, yy + 23, uid))
        for k, xx in enumerate((640, 724, 808)):
            lab = "…" if k == 2 else "data"
            o.append(blk(xx, yy, 70, eh, "", lab, None, dash=(k == 2)))
        o.append(arrow(562, yy + 23, 638, yy + 23, uid))
    o.append(text(20, y0 + 150, "contents.master_index.pointers[i].index.pointers[j].data", "m"))
    o.append(text(20, 538, "A pointer of 0 is a hole: the block was never written and reads as 512 zero bytes.", "m"))
    o.append("</svg>")
    return "".join(o)


def fig_index_block(uid="5b"):
    W, H = 920, 190
    o = [svg_open(W, H, "An index block stores 256 low bytes, then 256 high bytes. Block number i is "
                  "hi[i] × 256 + lo[i].", uid)]
    x0, w = 20, 880
    half = w / 2
    o.append(box(x0, 36, half, 40, "ptr"))
    o.append(box(x0 + half, 36, half, 40, "size"))
    o.append(text(x0 + half / 2 + 40, 61, "lo[0] … lo[255]", "name", "middle"))
    o.append(text(x0 + half * 1.5 + 40, 61, "hi[0] … hi[255]", "name", "middle"))
    for t, lab, an in ((0, "byte 0", "start"), (256, "256", "middle"), (512, "511", "end")):
        o.append(text(x0 + (t / 512) * w, 24, lab, "m", an))
    xl, xh = x0 + 80, x0 + half + 80
    o.append(f'<rect class="seg k-ptr" x="{xl}" y="36" width="8" height="40"/>')
    o.append(f'<rect class="seg k-size" x="{xh}" y="36" width="8" height="40"/>')
    o.append(f'<path class="ar" fill="none" d="M{xl + 4} 78 L{xl + 4} 118 L{x0 + 378} 118" marker-end="url(#ah{uid})"/>')
    o.append(f'<path class="ar" fill="none" d="M{xh + 4} 78 L{xh + 4} 118 L{x0 + 502} 118" marker-end="url(#ah{uid})"/>')
    o.append(blk(x0 + 380, 100, 120, 36, "", "block_number"))
    o.append(text(xl + 10, 96, "lo[i]", "m"))
    o.append(text(xh + 10, 96, "hi[i]", "m"))
    o.append(text(x0 + 536, 123, "block_number = (hi << 8) | lo", "name")); o.append(text(x0 + 536, 140, "lo[i] and hi[i] share the same index i", "m"))
    o.append(text(x0, 170, "Same split layout in the master index block; only its first 128 entries are used.", "m"))
    o.append("</svg>")
    return "".join(o)


def fig_extended(uid="6"):
    W, H = 920, 150
    o = [svg_open(W, H, "An extended key block holds an 8-byte mini-entry for the data fork at offset 0 "
                  "and for the resource fork at offset 256.", uid)]
    x0, w, sc = 20, 880, 880 / 512
    parts = [(0, 8, "tag", "data_fork"), (8, 248, "res", "data_fork_info · 248 B"),
             (256, 8, "tag", "resource_fork"), (264, 248, "res", "resource_fork_info · 248 B")]
    for off, n, k, lab in parts:
        x = x0 + off * sc
        o.append(box(f"{x:.1f}", 50, f"{n * sc:.1f}", 40, k))
        if n > 100:
            o.append(text(x + n * sc / 2, 75, lab, "m", "middle"))
    for off, lab in ((0, "data_fork"), (256, "resource_fork")):
        x = x0 + off * sc
        o.append(f'<line class="grid" x1="{x:.1f}" y1="38" x2="{x:.1f}" y2="50"/>')
        o.append(text(x, 30, f"{lab} · mini-entry at byte {off}", "name"))
    for t in (0, 256, 512):
        x = x0 + t * sc
        o.append(text(x, 112, t, "off", "start" if t == 0 else ("end" if t == 512 else "middle")))
    o.append(text(x0, 138, "Finder info bytes after each mini-entry are kept as raw bytes in the spec.", "m"))
    o.append("</svg>")
    rows = fields(VOL, "fork_entry")
    assert total_bytes(rows) == 8
    return "".join(o), waterfall(rows, 8, uid + "b", "The 8-byte fork mini-entry: storage type, key pointer, "
                                 "blocks used and a 24-bit end of file.", W=920, track=430, ticks=list(range(9)))


def fig_2img_layout(uid="7"):
    W, H = 920, 230
    o = [svg_open(W, H, "A 2IMG file is a 64-byte header followed by the disk data, then an optional "
                  "comment and creator data, located by offsets in the header.", uid)]
    y, h = 120, 52
    segs = [(20, 120, "ptr", "header", "64 B"), (144, 460, "", "disk data", "prodos_volume"),
            (608, 140, "", "comment", "optional"), (752, 148, "", "creator data", "optional")]
    for x, w, k, a, b in segs:
        dash = a in ("comment", "creator data")
        o.append(blk(x, y, w, h, k, a, b, dash=dash))
    o.append(curve(80, y, 374, y, 70, uid))
    o.append(text(210, 20, "data_offset, data_length", "name", "middle"))
    o.append(curve(110, y, 678, y, 90, uid))
    o.append(text(420, 38, "comment_offset, comment_length", "name", "middle"))
    o.append(curve(130, y, 826, y, 108, uid))
    o.append(text(620, 56, "creator_data_offset, creator_data_length", "name", "middle"))
    o.append(text(144, y + h + 22, "prodos_blocks × 512 bytes", "m"))
    o.append(text(20, y + h + 22 + 0, "0", "off"))
    o.append(text(20, 214, "A data_length of 0 is treated as prodos_blocks × 512 by the spec.", "m"))
    o.append("</svg>")
    return "".join(o)


def fig_2img_header(uid="7b"):
    rows = fields(IMG, "header")
    assert total_bytes(rows) == 64, total_bytes(rows)
    return waterfall(rows, 64, uid, "The 64-byte 2IMG header, field by field.", ticks=[0, 8, 16, 24, 32, 40, 48, 56, 64])


def fig_2img_flags(uid="7c"):
    segs, n = segs_from_ksy(IMG, "flags", msb_first=False)
    assert n == 32
    segs = [(i, s, w, "res" if i.startswith("reserved") else "flag") for i, s, w, _ in segs]
    return bit_strip(segs, 32, uid, "2IMG flags: DOS volume number in bits 0-7, volume-valid in "
                     "bit 8, locked in bit 31.", byte_marks=True)
