#!/usr/bin/env python3
"""Parse test.po and test.2mg with the compiled specs and check the values.
Usage: python3 test_ksy.py   (after: make build; python3 make_test_image.py)"""
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here / "build"))
from kaitaistruct import KaitaiStream  # noqa: E402
from prodos_volume import ProdosVolume  # noqa: E402
from prodos_2img import Prodos2img  # noqa: E402

ok = True


def check(label, got, want):
    global ok
    good = got == want
    ok &= good
    print(("PASS " if good else "FAIL ") + label + ("" if good else f"  got={got!r} want={want!r}"))


def all_entries(block):
    """Walk the directory chain; yield active file entries."""
    while block:
        for e in block.entries:
            if e.storage_nibble != 0:
                yield e
        block = block.next_block


vol = ProdosVolume.from_file(str(here / "test.po"))
hdr = vol.volume_header
check("volume name", hdr.volume_name, "TESTVOL")
check("total blocks", hdr.total_blocks, 280)
check("bitmap pointer", hdr.bit_map_pointer, 6)
check("entry length / per block", (hdr.entry_length, hdr.entries_per_block), (39, 13))
check("volume created date", (hdr.created.full_year, hdr.created.month, hdr.created.day,
                              hdr.created.hour, hdr.created.minute), (2024, 1, 2, 3, 4))

entries = {e.body.file_name: e for e in all_entries(vol.root_block)}
check("chain finds 5 files", sorted(entries), ["BIG.BIN", "FORKED", "HELLO.TXT", "SUB", "TREE.DAT"])

h = entries["HELLO.TXT"]
check("hello storage", h.storage_type, ProdosVolume.StorageType.seedling)
check("hello type", h.body.file_type, ProdosVolume.FileType.text)
check("hello eof", h.body.eof, 6)
check("hello data", h.body.contents.seedling_data, b"HELLO\r")
check("hello created", (h.body.created.full_year, h.body.created.month, h.body.created.day,
                        h.body.created.hour, h.body.created.minute), (2024, 3, 15, 10, 30))
check("hello modified", (h.body.last_modified.full_year, h.body.last_modified.month,
                         h.body.last_modified.day, h.body.last_modified.hour,
                         h.body.last_modified.minute), (2025, 12, 1, 23, 59))
a = h.body.access
check("hello access r/w/rename/destroy", (a.read_enable, a.write_enable, a.rename_enable,
                                         a.destroy_enable, a.backup_needed, a.invisible),
      (True, True, True, True, False, False))

b = entries["BIG.BIN"]
check("big storage", b.storage_type, ProdosVolume.StorageType.sapling)
check("big eof 24-bit", b.body.eof, 1200)
check("big aux (load addr)", b.body.aux_type, 0x2000)
ptrs = b.body.contents.sapling_index.pointers
check("big ptr0 -> 9, 512 bytes", (ptrs[0].block_number, len(ptrs[0].data)), (9, 512))
check("big ptr1 is a hole", (ptrs[1].block_number, ptrs[1].data), (0, None))
check("big ptr2 -> 10", ptrs[2].block_number, 10)
check("big ptr0 content", ptrs[0].data[:4], bytes([0, 1, 2, 3]))
check("big ptr2 content", ptrs[2].data[:8], b"TAILTAIL")

t = entries["TREE.DAT"]
check("tree storage", t.storage_type, ProdosVolume.StorageType.tree)
check("tree type", t.body.file_type, ProdosVolume.FileType.applesoft_program)
mi = t.body.contents.master_index
check("tree master ptr0 -> 14", mi.pointers[0].block_number, 14)
check("tree data", mi.pointers[0].index.pointers[0].data[:8], b"TREEDATA")
ta = t.body.access
check("tree access read-only", (ta.read_enable, ta.write_enable, ta.destroy_enable), (True, False, False))

s = entries["SUB"]
check("sub storage", s.storage_type, ProdosVolume.StorageType.subdirectory)
sd = s.body.subdirectory
sh = sd.header.body
check("sub header name", sh.dir_name, "SUB")
check("sub header parent ptr/entry/len", (sh.parent_pointer, sh.parent_entry_number,
                                          sh.parent_entry_length), (3, 2, 39))
check("sub header storage", sd.header.storage_type, ProdosVolume.StorageType.subdirectory_header)
note = sd.entries[0]
check("note name + data", (note.body.file_name, note.body.contents.seedling_data),
      ("NOTE.TXT", b"A NOTE\r"))

slot = vol.root_block.entries[2]  # the deliberately deleted entry
check("deleted slot is empty_body", (slot.storage_type, type(slot.body).__name__),
      (ProdosVolume.StorageType.deleted, "EmptyBody"))
check("unused slots in key block", sum(e.storage_nibble == 0 for e in vol.root_block.entries), 10)

f = entries["FORKED"]
check("forked storage", f.storage_type, ProdosVolume.StorageType.extended)
x = f.body.extended
check("forked data fork", (x.data_fork.eof, x.data_fork.contents.seedling_data), (5, b"DATA!"))
check("forked resource fork", (x.resource_fork.eof, x.resource_fork.contents.seedling_data), (4, b"RSRC"))

free = vol.bitmap.free
check("bitmap length", len(free), 280)
check("bitmap used 0-18, free after", (free[0], free[18], free[19], free[279]),
      (False, False, True, True))
check("bitmap free count", sum(free), 280 - 19)

# --- 2IMG wrapper -----------------------------------------------------
img = Prodos2img.from_file(str(here / "test.2mg"))
check("2img magic/creator", (img.header.magic, img.header.creator), (b"2IMG", "TEST"))
check("2img format", img.header.image_format, Prodos2img.ImageFormat.prodos_order)
check("2img flags", (img.header.flags.locked, img.header.flags.volume_number_valid,
                     img.header.flags.dos_volume_number), (True, True, 5))
check("2img blocks/offset", (img.header.prodos_blocks, img.header.data_offset), (280, 64))
check("2img volume name", img.volume.volume_header.volume_name, "TESTVOL")
inner = {e.body.file_name: e for e in all_entries(img.volume.root_block)}
check("2img nested file data", inner["HELLO.TXT"].body.contents.seedling_data, b"HELLO\r")
check("2img subdir via wrapper", inner["SUB"].body.subdirectory.entries[0].body.file_name, "NOTE.TXT")

print("\nALL PASSED" if ok else "\nFAILURES")
sys.exit(0 if ok else 1)
