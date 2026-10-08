#!/usr/bin/env python3
"""Build a small synthetic ProDOS volume (and a 2IMG-wrapped copy) that
exercises every structure in prodos_volume.ksy: seedling, sapling (with a
hole), tree, subdirectory, deleted entry, bitmap, dates and access bits.
Writes test.po and test.2mg next to this script."""
import struct
from pathlib import Path

BLOCKS = 280
img = bytearray(BLOCKS * 512)


def put(block, data, off=0):
    img[block * 512 + off:block * 512 + off + len(data)] = data


def pdate(y, mo, d, h, mi):
    word = ((y % 100) << 9) | (mo << 5) | d
    return struct.pack("<HBB", word, mi, h)


def name15(n):
    return n.encode().ljust(15, b"\0")


def file_entry(storage, name, ftype, key, used, eof, aux, header, access=0xC3):
    e = bytearray()
    e.append((storage << 4) | len(name))
    e += name15(name)
    e.append(ftype)
    e += struct.pack("<HH", key, used)
    e += struct.pack("<HB", eof & 0xFFFF, eof >> 16)
    e += pdate(2024, 3, 15, 10, 30)
    e += bytes([0, 0, access])
    e += struct.pack("<H", aux)
    e += pdate(2025, 12, 1, 23, 59)
    e += struct.pack("<H", header)
    assert len(e) == 39, len(e)
    return bytes(e)


def dir_header(kind, name, count, extra):
    h = bytearray()
    h.append((kind << 4) | len(name))
    h += name15(name)
    h += bytes([0x75 if kind == 0xE else 0]) + bytes(7)
    h += pdate(2024, 1, 2, 3, 4)
    h += bytes([0, 0, 0xC3, 39, 13])
    h += struct.pack("<H", count)
    h += extra
    assert len(h) == 39, len(h)
    return bytes(h)


def dir_block(prev, nxt, header, entries):
    b = bytearray(512)
    b[0:4] = struct.pack("<HH", prev, nxt)
    slots = ([header] if header else []) + entries
    for i, s in enumerate(slots):
        b[4 + 39 * i:4 + 39 * i + 39] = s
    return bytes(b)


def index_block(ptrs):
    b = bytearray(512)
    for i, p in enumerate(ptrs):
        b[i] = p & 0xFF
        b[256 + i] = p >> 8
    return bytes(b)


# --- boot blocks ----------------------------------------------------
put(0, bytes([1]) + b"BOOT")

# --- files ----------------------------------------------------------
put(7, b"HELLO\r")                                     # seedling data
put(8, index_block([9, 0, 10]))                        # sapling index (hole)
put(9, bytes(range(256)) * 2)
put(10, b"TAIL" * 44)                                  # 176 bytes used
put(12, b"A NOTE\r")                                   # file inside SUB
put(13, index_block([14]))                             # tree master index
put(14, index_block([15]))
put(15, b"TREEDATA" * 12)                              # 96 bytes

hello = file_entry(1, "HELLO.TXT", 0x04, 7, 1, 6, 0, 2)
big = file_entry(2, "BIG.BIN", 0x06, 8, 3, 1200, 0x2000, 2)
sub = file_entry(13, "SUB", 0x0F, 11, 1, 512, 0, 2)
tree = file_entry(3, "TREE.DAT", 0xFC, 13, 3, 96, 0, 2, access=0x21)
deleted = bytes(39)

# extended (forked) file: key block 16, data fork block 17, resource fork 18
put(17, b"DATA!")
put(18, b"RSRC")
ext = bytearray(512)
ext[0:8] = struct.pack("<BHHHB", 1, 17, 1, 5, 0)        # data fork mini-entry
ext[256:264] = struct.pack("<BHHHB", 1, 18, 1, 4, 0)    # resource fork mini-entry
put(16, bytes(ext))
forked = file_entry(5, "FORKED", 0xB3, 16, 3, 9, 0, 2)

# volume directory: 4 blocks chained 2-3-4-5, entries spread across them
vol_hdr = dir_header(0xF, "TESTVOL", 5, struct.pack("<HH", 6, BLOCKS))
put(2, dir_block(0, 3, vol_hdr, [hello, big, deleted]))
put(3, dir_block(2, 4, None, [sub]))
put(4, dir_block(3, 5, None, [tree]))
put(5, dir_block(4, 0, None, [forked]))

# subdirectory key block (block 11) holding NOTE.TXT
sub_hdr = dir_header(0xE, "SUB", 1, struct.pack("<HBB", 3, 2, 39))
note = file_entry(1, "NOTE.TXT", 0x04, 12, 1, 7, 0, 11)
put(11, dir_block(0, 0, sub_hdr, [note]))

# bitmap (block 6): blocks 0-18 used, everything else free
bm = bytearray(512)
for blk in range(19, BLOCKS):
    bm[blk // 8] |= 0x80 >> (blk % 8)
put(6, bytes(bm))

here = Path(__file__).resolve().parent
(here / "test.po").write_bytes(bytes(img))

# --- 2IMG wrapper -----------------------------------------------------
hdr = b"2IMG" + b"TEST" + struct.pack(
    "<HHIIIIIIIII", 64, 1, 1, 0x80000000 | 0x100 | 5, BLOCKS, 64,
    len(img), 0, 0, 0, 0) + bytes(16)
assert len(hdr) == 64, len(hdr)
(here / "test.2mg").write_bytes(hdr + bytes(img))
print("wrote test.po and test.2mg")
