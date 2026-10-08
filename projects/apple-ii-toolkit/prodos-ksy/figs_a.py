"""Figures 1-4: volume map, directory block and chain, 39-byte slots, bit fields."""
from diagram_lib import (svg_open, arrow, curve, text, box, waterfall, bit_strip,
                         segs_from_ksy, esc)
from layout import VOL, entry_rows, total_bytes


def fig_volume_map(uid="1"):
    W, H = 920, 250
    o = [svg_open(W, H, "A ProDOS volume is a row of 512-byte blocks: two boot blocks, "
                  "four chained directory blocks, a bitmap, then file data.", uid)]
    y, h, bw, gap, x0 = 120, 58, 72, 6, 20
    roles = [("0", "boot", ""), ("1", "boot", ""), ("2", "dir", "ptr"), ("3", "dir", "ptr"),
             ("4", "dir", "ptr"), ("5", "dir", "ptr"), ("6", "bitmap", "flag")]
    for i, (n, role, k) in enumerate(roles):
        x = x0 + i * (bw + gap)
        o.append(box(x, y, bw, h, k) if k else f'<rect class="seg" x="{x}" y="{y}" width="{bw}" height="{h}" rx="3"/>')
        o.append(text(x + bw / 2, y + 24, n, "big", "middle"))
        o.append(text(x + bw / 2, y + 44, role, "m", "middle"))
        o.append(text(x + bw / 2, y + h + 20, i * 512, "m", "middle"))
    xd = x0 + 7 * (bw + gap)
    o.append(f'<rect class="seg dash" x="{xd}" y="{y}" width="{W - 20 - xd}" height="{h}" rx="3"/>')
    o.append(text(xd + (W - 20 - xd) / 2, y + 24, "7 … N−1", "big", "middle"))
    o.append(text(xd + (W - 20 - xd) / 2, y + 44, "files · index blocks · subdirectories", "m", "middle"))
    o.append(text(x0 - 2, y + h + 38, "byte offset in the image = block × 512", "m"))
    # pointers leaving the volume header (block 2)
    x2 = x0 + 2 * (bw + gap)
    xb = x0 + 6 * (bw + gap) + bw / 2
    o.append(curve(x2 + 20, y, xb - 8, y, 52, uid))
    o.append(text((x2 + 20 + xb - 8) / 2, y - 62, "volume_header.bit_map_pointer", "name", "middle"))
    xe = xd + 150
    o.append(curve(x2 + 52, y, xe, y, 86, uid))
    o.append(text((x2 + 52 + xe) / 2 + 40, y - 96, "entry.key_pointer, one per file", "name", "middle"))
    o.append("</svg>")
    return "".join(o)


def fig_directory(uid="2"):
    W, H = 920, 470
    o = [svg_open(W, H, "A directory block holds a 4-byte link header and 13 slots of 39 bytes. "
                  "Blocks of one directory are chained by next_ptr and prev_ptr.", uid)]
    x, w, top = 70, 300, 20
    # link row
    o.append(box(x, top, w / 2, 28, "ptr"))
    o.append(box(x + w / 2, top, w / 2, 28, "ptr"))
    o.append(text(x + w / 4, top + 19, "prev_ptr", "name", "middle"))
    o.append(text(x + 3 * w / 4, top + 19, "next_ptr", "name", "middle"))
    o.append(text(x - 10, top + 19, "0", "off", "end"))
    y = top + 34
    for s in range(13):
        off = 4 + 39 * s
        k = "tag" if s == 0 else "text"
        o.append(box(x, y, w, 22, k))
        lab = "slot 1 · header (key block only)" if s == 0 else f"slot {s + 1}"
        o.append(text(x + 10, y + 16, lab, "name"))
        o.append(text(x - 10, y + 16, off, "off", "end"))
        y += 24
    o.append(f'<rect class="seg k-res" x="{x}" y="{y}" width="{w}" height="14" rx="3"/>')
    o.append(text(x + 10, y + 11, "unused", "m"))
    o.append(text(x - 10, y + 11, 511, "off", "end"))
    o.append(text(x + w + 14, 36, "4 bytes", "m"))
    o.append(text(x + w + 14, 62, "13 slots × 39 B = 507 B", "m"))
    o.append(text(x + w + 14, 80, "4 + 507 + 1 = 512", "m"))
    o.append(text(x + w + 14, 98, "key block: slot 1 is the header, 12 file entries follow", "m"))
    o.append(text(x + w + 14, 116, "later blocks: all 13 slots are file entries", "m"))
    # chain
    cx, cy = 490, 190
    o.append(text(cx, cy - 28, "One directory is a chain of blocks", "name"))
    for i, b in enumerate((2, 3, 4, 5)):
        bx = cx + i * 100
        o.append(box(bx, cy, 74, 44, "ptr"))
        o.append(text(bx + 37, cy + 27, f"block {b}", "name", "middle"))
        if i < 3:
            o.append(arrow(bx + 76, cy + 14, bx + 98, cy + 14, uid))
            o.append(arrow(bx + 98, cy + 32, bx + 76, cy + 32, uid))
    o.append(text(cx, cy + 66, "arrows: next_ptr forward, prev_ptr back", "m"))
    o.append(text(cx, cy + 84, "the last block has next_ptr = 0", "m"))
    # subdirectory link
    sy = 340
    o.append(text(cx, sy - 20, "A subdirectory is another chain, entered from a slot", "name"))
    o.append(box(cx, sy, 130, 44, "text"))
    o.append(text(cx + 65, sy + 20, "file entry", "name", "middle"))
    o.append(text(cx + 65, sy + 36, "storage D", "m", "middle"))
    o.append(arrow(cx + 132, sy + 14, cx + 248, sy + 14, uid))
    o.append(text(cx + 190, sy + 6, "key_pointer", "m", "middle"))
    o.append(box(cx + 250, sy, 170, 44, "tag"))
    o.append(text(cx + 335, sy + 20, "subdir key block", "name", "middle"))
    o.append(text(cx + 335, sy + 36, "slot 1 = subdir header", "m", "middle"))
    o.append(arrow(cx + 248, sy + 34, cx + 132, sy + 34, uid))
    o.append(text(cx + 190, sy + 52, "parent_pointer", "m", "middle"))
    o.append("</svg>")
    return "".join(o)


def fig_slot(body, label, uid):
    rows = entry_rows(body)
    assert total_bytes(rows) == 39, (body, total_bytes(rows))
    return waterfall(rows, 39, uid, label)


def fig_bits(uid_a="4a", uid_b="4b"):
    segs, n = segs_from_ksy(VOL, "datetime", msb_first=False)
    assert n == 32
    segs = [(i, s, w, "res" if i.startswith("reserved") else "time") for i, s, w, _ in segs]
    dt = bit_strip(segs, 32, uid_a, "ProDOS date and time as one 32-bit little-endian value: "
                   "day, month and year in bytes 0-1, minute in byte 2, hour in byte 3.")
    segs, n = segs_from_ksy(VOL, "access", msb_first=True)
    assert n == 8
    segs = [(i, s, w, "res" if i.startswith("reserved") else "flag") for i, s, w, _ in segs]
    ac = bit_strip(segs, 8, uid_b, "Access byte: destroy, rename, backup, two reserved bits, "
                   "invisible, write, read.", cell=76, byte_marks=False)
    return dt, ac
