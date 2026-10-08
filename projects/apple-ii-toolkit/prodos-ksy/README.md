# ProDOS formats in Kaitai Struct

| File | Describes |
|---|---|
| `prodos_volume.ksy` | A ProDOS 8 volume: boot blocks, volume directory chain, volume/subdirectory headers, file entries, seedling/sapling/tree data, extended (forked) files, volume bitmap, dates, access flags, file types |
| `prodos_2img.ksy` | The 2IMG container header; parses the payload as a ProDOS volume when the format is ProDOS order |

## Using it

    make build      # compile to Python in ./build
    make test       # build a synthetic volume and check 46 parsed values

    from prodos_volume import ProdosVolume
    vol = ProdosVolume.from_file("disk.po")
    print(vol.volume_header.volume_name, vol.volume_header.total_blocks)

    blk = vol.root_block
    while blk:                                  # follow the directory chain
        for e in blk.entries:
            if e.storage_nibble != 0:           # skip inactive slots
                print(e.body.file_name, e.storage_type, e.body.eof)
        blk = blk.next_block

Subdirectories: `entry.body.subdirectory` (storage type `subdirectory`) is
another `dir_block` whose `header` is the subdirectory header.

File data: `entry.body.contents` has `seedling_data`, `sapling_index` or
`master_index`, depending on the storage type. Index entries give `data`
(512 bytes, or `None` for a hole). Concatenate the blocks, filling holes
with zeros, and cut at `eof`. Forked files: `entry.body.extended` has
`data_fork` and `resource_fork`, each with its own `contents`.

## Notes and limits

- Volumes only. A 140K `.do`/`.dsk` file is DOS-sector-ordered, so its blocks
  are not contiguous and cannot be described as a flat KSY sequence; convert
  it to ProDOS order (`.po`) first.
- Block numbers are 16-bit, so the volume is at most 65535 blocks.
- The `bitmap` is parsed bit by bit and is large on big volumes; it is only
  read if you access it.
- Filename case bits (Tech Note #8) are exposed as `case_bits`, not applied.
- In extended key blocks the bytes after each fork mini-entry (the Finder
  info records) are left as raw bytes.
- File type enum covers the common ProDOS 8 and GS/OS types, not every type
  Apple ever assigned. Unknown values still parse and appear as plain ints.
- Checked with the JavaScript build of the compiler 0.11.0, generating
  Python, against a synthetic image made by `make_test_image.py`. It has not
  been run against real-world disk images.
