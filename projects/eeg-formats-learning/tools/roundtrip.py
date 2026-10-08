import struct, sys, io
sys.path.insert(0, sys.argv[1])
from kaitaistruct import KaitaiStream

import edf, bdf, fif, xdf, eeglab_fdt, brainvision_eeg


def pad(s, n):
    return s.ljust(n).encode("ascii")


def build_header(ver, ns, nrec, spr, labels):
    h = ver
    h += pad("patient", 80) + pad("rec", 80) + b"01.01.26" + b"12.00.00"
    h += pad(str(256 + 256 * ns), 8) + pad("", 44) + pad(str(nrec), 8) + pad("1", 8) + pad(str(ns), 4)
    for lab in labels: h += pad(lab, 16)
    h += pad("", 80 * ns)
    h += pad("uV", 8) * ns + pad("-100", 8) * ns + pad("100", 8) * ns
    h += pad("-32768", 8) * ns + pad("32767", 8) * ns
    h += pad("", 80 * ns)
    h += pad(str(spr), 8) * ns
    h += pad("", 32 * ns)
    return h


# EDF: 2 signals, 3 records, 4 samples each
ns, nrec, spr = 2, 3, 4
data = b""
vals = []
for r in range(nrec):
    for s in range(ns):
        row = [r * 100 + s * 10 + i - 5 for i in range(spr)]
        vals.append(row)
        data += struct.pack("<%dh" % spr, *row)
blob = build_header(pad("0", 8), ns, nrec, spr, ["Fp1", "Fp2"]) + data
e = edf.Edf(KaitaiStream(io.BytesIO(blob)))
assert e.header.num_signals_int == 2 and e.header.label == ["Fp1", "Fp2"], e.header.label
got = [list(sb.samples) for rec in e.records_known for sb in rec.signals]
assert got == vals, (got, vals)
print("EDF ok: labels", e.header.label, "records", len(e.records_known))

# EDF with unknown record count (-1) -> read to EOF
blob2 = build_header(pad("0", 8), ns, -1, spr, ["A", "B"]) + data
e2 = edf.Edf(KaitaiStream(io.BytesIO(blob2)))
assert len(e2.records_until_eof) == nrec
print("EDF (-1 records) ok:", len(e2.records_until_eof), "records")

# BDF: 24-bit samples incl. negatives
bvals = [-8388608, -1, 0, 1, 8388607, 123456, -123456, 42]
bdata = b"".join(struct.pack("<i", v)[:3] for v in bvals)
bblob = build_header(b"\xffBIOSEMI", 2, 1, 4, ["C3", "Status"]) + bdata
b = bdf.Bdf(KaitaiStream(io.BytesIO(bblob)))
bgot = [s.value for sb in b.records_known[0].signals for s in sb.samples]
assert bgot == bvals, bgot
print("BDF ok:", bgot)

# FIF: file_id tag + one raw data buffer tag
idtag = struct.pack(">iiii", 100, 31, 20, 0) + struct.pack(">iIIii", 0x00010002, 1, 2, 1700000000, 5)
buf = struct.pack(">iiii", 300, 16, 8, -1) + struct.pack(">ff", 1.5, -2.5)
f = fif.Fif(KaitaiStream(io.BytesIO(idtag + buf)))
assert f.tags[0].kind == fif.Fif.FiffKind.file_id
assert f.tags[0].data.version == 0x00010002 and f.tags[0].data.time_secs == 1700000000
assert f.tags[1].kind == fif.Fif.FiffKind.data_buffer and f.tags[1].base_type == 16
print("FIF ok: tags", len(f.tags))

# XDF: header chunk + stream header + clock offset
def chunk(tag, content, nb=1):
    body = struct.pack("<H", tag) + content
    ln = len(body)
    if nb == 1:
        return bytes([1, ln]) + body
    return bytes([4]) + struct.pack("<I", ln) + body

xml = b"<info><version>1.0</version></info>"
xblob = b"XDF:" + chunk(1, xml) + chunk(2, struct.pack("<I", 7) + b"<info/>")
xblob += chunk(4, struct.pack("<Idd", 7, 12.5, 0.001))
xblob += chunk(3, struct.pack("<I", 7) + bytes([1, 2]) + b"\x00" + struct.pack("<f", 1.0), nb=4)
x = xdf.Xdf(KaitaiStream(io.BytesIO(xblob)))
assert x.chunks[0].body.xml == xml.decode()
assert x.chunks[1].body.stream_id == 7
assert abs(x.chunks[2].body.collection_time - 12.5) < 1e-9
assert x.chunks[3].body.num_samples.value == 2 and x.chunks[3].body.stream_id == 7
print("XDF ok: chunks", [c.tag.name for c in x.chunks])

# EEGLAB .fdt: 3 channels x 4 frames
fv = [float(i) for i in range(12)]
fd = eeglab_fdt.EeglabFdt(3, 4, KaitaiStream(io.BytesIO(struct.pack("<12f", *fv))))
assert [v for fr in fd.frames for v in fr.values] == fv
print("EEGLAB fdt ok")

# BrainVision .eeg int16 and float32
iv = list(range(-6, 6))
bi = brainvision_eeg.BrainvisionEeg(3, 4, False, KaitaiStream(io.BytesIO(struct.pack("<12h", *iv))))
assert [v for fr in bi.frames for v in fr.values] == iv
bf = brainvision_eeg.BrainvisionEeg(3, 4, True, KaitaiStream(io.BytesIO(struct.pack("<12f", *fv))))
assert [v for fr in bf.frames for v in fr.values] == fv
print("BrainVision eeg ok (int16 and float32)")
