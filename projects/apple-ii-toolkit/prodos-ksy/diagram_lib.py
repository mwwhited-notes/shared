"""SVG helpers for the ProDOS layout page. Colors come from CSS classes on the
page (k-ptr, k-text, ...), so every drawing follows the light/dark theme."""
import html
from layout import fields, VOL, IMG

MONO_W = 7.4  # approx glyph width of the 12px mono face, for label fitting


def esc(s):
    return html.escape(str(s), quote=True)


SIZE_IDS = {"blocks_used", "eof_low", "eof_high", "file_count", "total_blocks",
            "entry_length", "entries_per_block", "prodos_blocks", "data_length",
            "comment_length", "creator_data_length"}


def kind(r):
    i, t = r["id"], r["type"]
    if i.startswith("reserved"):
        return "res"
    if "pointer" in i or i.endswith("_ptr") or i.endswith("_offset"):
        return "ptr"
    if t.startswith("str"):
        return "text"
    if t.startswith("datetime") or i in ("created", "last_modified"):
        return "time"
    if t.startswith("access") or t.startswith("flags"):
        return "flag"
    if i in SIZE_IDS:
        return "size"
    return "tag"


def svg_open(w, h, label, uid):
    return (f'<svg class="fig" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}" '
            f'style="max-width:{w}px;min-width:min({w}px,760px)">'
            f'<defs><marker id="ah{uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" '
            f'fill="currentColor"/></marker></defs>')


def arrow(x1, y1, x2, y2, uid, cls="ar"):
    return (f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'marker-end="url(#ah{uid})"/>')


def curve(x1, y1, x2, y2, rise, uid, cls="ar"):
    """Arrow that leaves (x1,y1) upward, arcs by `rise`, lands on (x2,y2)."""
    cy = min(y1, y2) - rise
    return (f'<path class="{cls}" fill="none" d="M{x1} {y1} C{x1} {cy} {x2} {cy} {x2} {y2}" '
            f'marker-end="url(#ah{uid})"/>')


def text(x, y, s, cls="t", anchor="start"):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    return f'<text class="{cls}" x="{x}" y="{y}"{a}>{esc(s)}</text>'


def box(x, y, w, h, k, rx=3, extra=""):
    return f'<rect class="seg k-{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"{extra}/>'


def size_label(bits):
    if bits is None:
        return "var"
    if bits < 8:
        return f"{bits} bit" + ("s" if bits != 1 else "")
    b = bits // 8
    return f"{b} B"


# ---------------------------------------------------------------
# Struct "waterfall": one row per field, bar placed at its byte offset
# ---------------------------------------------------------------
def waterfall(rows, total, uid, label, W=920, track=430, ticks=None):
    X0, rh, top = 78, 26, 30
    sc = track / total
    h = top + rh * len(rows) + 8
    out = [svg_open(W, h, label, uid)]
    ticks = ticks or sorted({0, total, *range(0, total + 1, 8 if total <= 64 else 64)})
    for t in ticks:
        x = X0 + t * sc
        out.append(f'<line class="grid" x1="{x:.1f}" y1="{top - 6}" x2="{x:.1f}" y2="{h - 6}"/>')
        out.append(text(f"{x:.1f}", top - 12, t, "m", "middle"))
    out.append(text(X0 - 12, top - 12, "byte", "m", "end"))
    for n, r in enumerate(rows):
        y = top + n * rh
        bits = r["bits"] or 0
        if r["off"] % 8 == 0:
            out.append(text(X0 - 12, y + 16, r["off"] // 8, "off", "end"))
        x = X0 + r["off"] / 8 * sc
        w = max(bits / 8 * sc, 2.5)
        k = kind(r)
        out.append(box(f"{x:.1f}", y + 3, f"{w:.1f}", rh - 7, k))
        out.append(text(X0 + track + 16, y + 16, r["id"], "name"))
        out.append(text(W - 6, y + 16, f'{r["type"]} · {size_label(r["bits"])}', "m", "end"))
    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------
# Bit strips (MSB on the left)
# ---------------------------------------------------------------
def short(n):
    for suf in ("_enable", "_needed"):
        n = n.replace(suf, "")
    return n.replace("dos_volume_number", "dos_volume_number")


def bit_strip(segs, nbits, uid, label, cell=27, x0=10, rows_label=None, byte_marks=True):
    """segs: list of (id, start_bit, nbits, kind) with bit 0 = least significant."""
    top, bh = 26, 34
    W = x0 * 2 + nbits * cell
    below = 54 if byte_marks else 40
    H = top + bh + below
    out = [svg_open(W, H, label, uid)]
    for sid, start, n, k in sorted(segs, key=lambda s: -s[1]):
        x = x0 + (nbits - start - n) * cell
        w = n * cell
        out.append(box(x, top, w, bh, k))
        hi, lo = start + n - 1, start
        out.append(text(x + w / 2, top - 8, f"{hi}" if hi == lo else f"{hi}–{lo}", "m", "middle"))
        nm = short(sid)
        est = len(nm) * MONO_W
        if sid.startswith("reserved"):
            nm = "reserved" if est + 6 > w else nm
            nm = "rsvd" if len(nm) * MONO_W + 6 > w else nm
        if len(nm) * MONO_W + 6 <= w:
            out.append(text(x + w / 2, top + 21, nm, "name", "middle"))
        else:
            tx = min(max(x + w / 2, x0 + est / 2), W - x0 - est / 2)
            out.append(f'<line class="grid" x1="{x + w / 2}" y1="{top + bh}" x2="{x + w / 2}" y2="{top + bh + 10}"/>')
            out.append(text(tx, top + bh + 24, nm, "name", "middle"))
    if byte_marks:
        for b in range(nbits // 8):
            x = x0 + (nbits - 8 * (b + 1)) * cell
            out.append(f'<line class="grid" x1="{x}" y1="{top - 2}" x2="{x}" y2="{top + bh + 2}"/>')
            out.append(text(x + 4 * cell, H - 8, f"byte {b}", "m", "middle"))
    out.append("</svg>")
    return "".join(out)


def segs_from_ksy(spec, tname, msb_first):
    """Bit positions from the ksy's declared field order and widths."""
    rows = fields(spec, tname)
    total = sum(r["bits"] for r in rows)
    segs, pos = [], 0
    for r in rows:
        n = r["bits"]
        start = (total - pos - n) if msb_first else pos
        segs.append((r["id"], start, n, kind(r)))
        pos += n
    return segs, total
