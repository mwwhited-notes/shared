"""Read field offsets and sizes straight from the .ksy files, so the diagram
page cannot drift from the specs."""
from pathlib import Path
import yaml

HERE = Path(__file__).resolve().parent
VOL = yaml.safe_load((HERE / "prodos_volume.ksy").read_text())
IMG = yaml.safe_load((HERE / "prodos_2img.ksy").read_text())

FIXED = {"u1": 8, "u2": 16, "u4": 32, "s1": 8, "s2": 16, "s4": 32}


def fixed_bits(spec, types, f):
    """Size in bits of one seq field, or None if it depends on the data."""
    t = f.get("type")
    if "contents" in f:
        return len(f["contents"]) * 8
    if "size" in f and isinstance(f["size"], int):
        return f["size"] * 8
    if isinstance(t, str):
        if t in FIXED:
            return FIXED[t]
        if t.startswith("b") and t[1:].isdigit():
            return int(t[1:])
        base = t.split("(")[0]
        if base in types:
            return type_bits(spec, types, base)
    return None


def type_bits(spec, types, name):
    total = 0
    for f in types[name].get("seq", []):
        b = fixed_bits(spec, types, f)
        if b is None:
            return None
        total += b
    return total


def fields(spec, name, base_bits=0):
    """Rows for one type: id, offset (bits), size (bits), type label, doc."""
    types = spec["types"]
    rows, off = [], 0
    for f in types[name]["seq"]:
        b = fixed_bits(spec, types, f)
        t = f.get("type", "bytes")
        if isinstance(t, dict):
            t = "variant"
        label = f"{t}" + (f" ×{f['repeat-expr']}" if "repeat-expr" in f else "")
        if "enum" in f:
            label += f" ({f['enum']})"
        rows.append(dict(id=f["id"], off=base_bits + off, bits=b, type=label,
                         doc=(f.get("doc") or "").strip().split("\n")[0]))
        off += b or 0
    return rows


def entry_rows(body):
    """Rows of the 39-byte directory slot: nibble byte + 38-byte body."""
    rows = [
        dict(id="storage_type", off=0, bits=4, type="b4", doc="high nibble"),
        dict(id="name_length", off=4, bits=4, type="b4", doc="low nibble"),
    ]
    rows += fields(VOL, body, 8)
    return rows


def total_bytes(rows):
    return sum(r["bits"] for r in rows) / 8


if __name__ == "__main__":
    for body in ("volume_header_body", "subdirectory_header_body", "file_entry_body"):
        r = entry_rows(body)
        print(body, total_bytes(r), "bytes")
        for x in r:
            print(f"  {x['off']/8:5.1f} {x['bits']/8:5.1f} {x['id']:22s} {x['type']}")
    for n, spec in (("datetime", VOL), ("access", VOL), ("fork_entry", VOL)):
        print(n, total_bytes(fields(spec, n)))
    print("2img header", total_bytes(fields(IMG, "header")), "flags",
          total_bytes(fields(IMG, "flags")))
