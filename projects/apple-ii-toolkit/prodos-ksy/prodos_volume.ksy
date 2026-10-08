meta:
  id: prodos_volume
  title: Apple ProDOS 8 volume (block device / ProDOS-order disk image)
  file-extension:
    - po
    - hdv
  license: CC0-1.0
  ks-version: 0.9
  endian: le
  bit-endian: be
doc: |
  A ProDOS 8 volume as a flat sequence of 512-byte blocks, as found in
  ".po" (ProDOS-order 140K floppy), ".hdv" and similar hard-disk images, and
  as the payload of a 2IMG container (see prodos_2img.ksy).

  Block map:
    0-1   boot code
    2-5   volume directory (a chain of directory blocks linked by pointers)
    6..   volume bitmap (location given by the volume header; 1 bit = free)

  Everything is addressed by 16-bit block numbers (block * 512 = byte
  offset), so a volume holds at most 65535 blocks (32 MB).

  How to walk the catalog: read `root_block`. Its `header` is the volume
  header and its `entries` are file entries. Follow `next_block` for the
  rest of the volume directory. A file entry with storage type
  `subdirectory` has a `subdirectory` instance whose `header` is the
  subdirectory header, and so on recursively.

  How to read a file: `contents` of a file entry gives the data blocks.
  Seedling files expose `seedling_data`. Sapling files expose a
  `sapling_index` whose 256 `pointers` each give one block of `data`.
  Tree files expose a `master_index` of up to 128 index blocks. A block
  number of 0 inside an index block is a hole (all zero bytes). Concatenate
  the blocks and cut the result at `eof`.

  Source: ProDOS 8 Technical Reference Manual (chapter 4, "ProDOS File
  Organization"), ProDOS 8 Technical Note #25 (extended files) and
  Technical Note #8 (GS/OS filename case bits).

seq:
  - id: boot_blocks
    size: 1024
    type: boot_blocks
  - id: root_block
    size: 512
    type: dir_block(true, _io)

instances:
  volume_header:
    value: root_block.header.body.as<volume_header_body>
    doc: Convenience alias for the volume header.
  bitmap:
    pos: volume_header.bit_map_pointer * 512
    type: volume_bitmap(volume_header.total_blocks)
    doc: |
      One entry per block of the volume. true = block is free. Block 0 is
      the most significant bit of the first byte.

types:
  boot_blocks:
    doc: |
      Blocks 0 and 1. Block 0 begins with the number of sectors to load
      (normally 1); the rest is 6502 boot code.
    seq:
      - id: sector_count
        type: u1
      - id: code
        size: 1023

  # ---------------------------------------------------------------
  # Directories
  # ---------------------------------------------------------------
  dir_block:
    doc: |
      One 512-byte directory block: two link pointers and 13 entries of 39
      bytes. In the first (key) block of a directory, entry 1 is the
      directory header and 12 file entries follow.
    params:
      - id: is_key
        type: bool
      - id: vol_io
        type: io
    seq:
      - id: prev_ptr
        type: u2
        doc: Previous block in the directory chain, 0 in the key block.
      - id: next_ptr
        type: u2
        doc: Next block in the directory chain, 0 in the last block.
      - id: header
        type: entry(vol_io)
        size: 39
        if: is_key
      - id: entries
        type: entry(vol_io)
        size: 39
        repeat: expr
        repeat-expr: 'is_key ? 12 : 13'
      - id: unused
        size: 1
    instances:
      next_block:
        pos: next_ptr * 512
        io: vol_io
        size: 512
        type: dir_block(false, vol_io)
        if: next_ptr != 0

  entry:
    doc: |
      A 39-byte directory slot. The high nibble of the first byte is the
      storage type; it says whether the rest is a volume header, a
      subdirectory header, a file entry, or an inactive (deleted) slot.
    params:
      - id: vol_io
        type: io
    seq:
      - id: storage_nibble
        type: b4
      - id: name_length
        type: b4
        doc: Length of the name (1-15). 0 for an inactive slot.
      - id: body
        size: 38
        type:
          switch-on: storage_nibble
          cases:
            15: volume_header_body
            14: subdirectory_header_body
            0: empty_body
            _: file_entry_body(vol_io)
    instances:
      storage_type:
        value: storage_nibble
        enum: storage_type

  empty_body:
    doc: Remains of a deleted entry. The contents are stale and unreliable.
    seq:
      - id: raw
        size-eos: true

  volume_header_body:
    seq:
      - id: volume_name_raw
        size: 15
        type: str
        encoding: ASCII
      - id: reserved
        size: 8
      - id: created
        type: datetime
      - id: version
        type: u1
        doc: ProDOS version that created the volume (0 for 1.x-2.x).
      - id: min_version
        type: u1
        doc: Oldest ProDOS version that can access the volume (0).
      - id: access
        type: access
      - id: entry_length
        type: u1
        doc: Always 39 ($27).
      - id: entries_per_block
        type: u1
        doc: Always 13 ($0D).
      - id: file_count
        type: u2
        doc: Number of active entries in this directory, not counting the header.
      - id: bit_map_pointer
        type: u2
        doc: First block of the volume bitmap.
      - id: total_blocks
        type: u2
        doc: Number of blocks on the volume.
    instances:
      volume_name:
        value: volume_name_raw.substring(0, _parent.name_length)
      case_bits:
        value: (version << 8) | min_version
        doc: |
          GS/OS lowercase flags (Tech Note #8). If bit 15 is set, bits
          14..0 mark characters 1..15 of the name as lowercase.

  subdirectory_header_body:
    seq:
      - id: dir_name_raw
        size: 15
        type: str
        encoding: ASCII
      - id: reserved
        size: 8
        doc: The first byte is normally $75.
      - id: created
        type: datetime
      - id: version
        type: u1
      - id: min_version
        type: u1
      - id: access
        type: access
      - id: entry_length
        type: u1
      - id: entries_per_block
        type: u1
      - id: file_count
        type: u2
      - id: parent_pointer
        type: u2
        doc: Key block of the directory that holds this subdirectory's entry.
      - id: parent_entry_number
        type: u1
        doc: Index of that entry within its block (1-13).
      - id: parent_entry_length
        type: u1
        doc: Entry length of the parent directory (39).
    instances:
      dir_name:
        value: dir_name_raw.substring(0, _parent.name_length)

  file_entry_body:
    doc: |
      File entry (seedling, sapling, tree, extended, Pascal area, or
      subdirectory). The storage type is in the parent `entry`.
    params:
      - id: vol_io
        type: io
    seq:
      - id: file_name_raw
        size: 15
        type: str
        encoding: ASCII
      - id: file_type
        type: u1
        enum: file_type
      - id: key_pointer
        type: u2
        doc: |
          Seedling: the data block. Sapling: the index block. Tree: the
          master index block. Extended: the extended key block.
          Subdirectory: its key block.
      - id: blocks_used
        type: u2
        doc: Blocks used by the file, including index blocks.
      - id: eof_low
        type: u2
      - id: eof_high
        type: u1
      - id: created
        type: datetime
      - id: version
        type: u1
      - id: min_version
        type: u1
      - id: access
        type: access
      - id: aux_type
        type: u2
        doc: For BIN files this is the load address; for TXT, the record length.
      - id: last_modified
        type: datetime
      - id: header_pointer
        type: u2
        doc: Key block of the directory that contains this entry.
    instances:
      file_name:
        value: file_name_raw.substring(0, _parent.name_length)
      eof:
        value: (eof_high << 16) | eof_low
        doc: Length of the file in bytes (24 bits).
      case_bits:
        value: (version << 8) | min_version
        doc: GS/OS lowercase flags, same layout as in the volume header.
      contents:
        type: fork_data(_parent.storage_nibble, key_pointer, eof, vol_io)
        doc: Data of a seedling, sapling or tree file.
      extended:
        pos: key_pointer * 512
        io: vol_io
        size: 512
        type: extended_key_block(vol_io)
        if: _parent.storage_nibble == 5
        doc: GS/OS forked file. Holds the data fork and the resource fork.
      subdirectory:
        pos: key_pointer * 512
        io: vol_io
        size: 512
        type: dir_block(true, vol_io)
        if: _parent.storage_nibble == 13

  # ---------------------------------------------------------------
  # File data
  # ---------------------------------------------------------------
  fork_data:
    doc: |
      Access to the blocks of one fork, selected by storage type
      (1 = seedling, 2 = sapling, 3 = tree). Only the instance that
      matches the storage type is present.
    params:
      - id: storage
        type: u1
      - id: key_pointer
        type: u2
      - id: eof
        type: u4
      - id: vol_io
        type: io
    instances:
      seedling_data:
        pos: key_pointer * 512
        io: vol_io
        size: 'eof > 512 ? 512 : eof'
        if: storage == 1
      sapling_index:
        pos: key_pointer * 512
        io: vol_io
        size: 512
        type: index_block(vol_io)
        if: storage == 2
      master_index:
        pos: key_pointer * 512
        io: vol_io
        size: 512
        type: master_index_block(vol_io)
        if: storage == 3

  index_block:
    doc: |
      Index block: 256 block numbers. The low bytes are stored in the first
      256 bytes and the high bytes in the second 256 bytes.
    params:
      - id: vol_io
        type: io
    seq:
      - id: pointers
        type: block_ptr(_index, vol_io)
        repeat: expr
        repeat-expr: 256

  master_index_block:
    doc: |
      Master index block of a tree file. Same split layout as an index
      block, but only the first 128 pointers are used (128 index blocks x
      256 blocks x 512 bytes = 16 MB, the largest ProDOS file).
    params:
      - id: vol_io
        type: io
    seq:
      - id: pointers
        type: index_ptr(_index, vol_io)
        repeat: expr
        repeat-expr: 128

  block_ptr:
    doc: One entry of an index block, pointing at a data block.
    params:
      - id: idx
        type: u4
      - id: vol_io
        type: io
    instances:
      lo:
        pos: idx
        io: _parent._io
        type: u1
      hi:
        pos: idx + 256
        io: _parent._io
        type: u1
      block_number:
        value: (hi << 8) | lo
        doc: 0 means the block is not allocated (a hole of zero bytes).
      data:
        pos: block_number * 512
        io: vol_io
        size: 512
        if: block_number != 0

  index_ptr:
    doc: One entry of a master index block, pointing at an index block.
    params:
      - id: idx
        type: u4
      - id: vol_io
        type: io
    instances:
      lo:
        pos: idx
        io: _parent._io
        type: u1
      hi:
        pos: idx + 256
        io: _parent._io
        type: u1
      block_number:
        value: (hi << 8) | lo
      index:
        pos: block_number * 512
        io: vol_io
        size: 512
        type: index_block(vol_io)
        if: block_number != 0

  extended_key_block:
    doc: |
      Key block of an extended (forked) file, Technical Note #25. Holds a
      mini-entry for the data fork at offset 0 and for the resource fork at
      offset 256. The bytes after each mini-entry carry the Finder info
      records and are left opaque here.
    params:
      - id: vol_io
        type: io
    seq:
      - id: data_fork
        type: fork_entry(vol_io)
      - id: data_fork_info
        size: 248
      - id: resource_fork
        type: fork_entry(vol_io)
      - id: resource_fork_info
        size: 248

  fork_entry:
    params:
      - id: vol_io
        type: io
    seq:
      - id: storage
        type: u1
        doc: 1 = seedling, 2 = sapling, 3 = tree.
      - id: key_pointer
        type: u2
      - id: blocks_used
        type: u2
      - id: eof_low
        type: u2
      - id: eof_high
        type: u1
    instances:
      eof:
        value: (eof_high << 16) | eof_low
      contents:
        type: fork_data(storage, key_pointer, eof, vol_io)

  # ---------------------------------------------------------------
  # Bitmap, dates, access
  # ---------------------------------------------------------------
  volume_bitmap:
    params:
      - id: total_blocks
        type: u4
    seq:
      - id: free
        type: b1
        repeat: expr
        repeat-expr: total_blocks

  datetime:
    doc: |
      ProDOS date and time, 4 bytes. The date word is
      yyyyyyym mmmddddd and the time is two bytes, minute then hour.
      All zero means "no date".
    meta:
      bit-endian: le
    seq:
      - id: day
        type: b5
      - id: month
        type: b4
      - id: year
        type: b7
        doc: Years since 1900, mod 100.
      - id: minute
        type: b6
      - id: reserved_minute
        type: b2
      - id: hour
        type: b5
      - id: reserved_hour
        type: b3
    instances:
      is_set:
        value: day != 0 or month != 0 or year != 0
      full_year:
        value: 'year < 40 ? 2000 + year : 1900 + year'
        doc: ProDOS 8 2.x convention - 0-39 mean 2000-2039, 40-99 mean 1940-1999.

  access:
    doc: Access flags for a file or directory.
    meta:
      bit-endian: be
    seq:
      - id: destroy_enable
        type: b1
      - id: rename_enable
        type: b1
      - id: backup_needed
        type: b1
      - id: reserved
        type: b2
      - id: invisible
        type: b1
      - id: write_enable
        type: b1
      - id: read_enable
        type: b1

enums:
  storage_type:
    0: deleted
    1: seedling
    2: sapling
    3: tree
    4: pascal_area
    5: extended
    13: subdirectory
    14: subdirectory_header
    15: volume_header

  file_type:
    0x00: typeless
    0x01: bad_blocks
    0x02: pascal_code
    0x03: pascal_text
    0x04: text
    0x05: pascal_data
    0x06: binary
    0x07: font
    0x08: graphics_screen
    0x09: business_basic_program
    0x0a: business_basic_data
    0x0b: word_processor
    0x0c: sos_system
    0x0f: directory
    0x19: appleworks_database
    0x1a: appleworks_word_processor
    0x1b: appleworks_spreadsheet
    0xb0: gsos_source
    0xb1: gsos_object
    0xb2: gsos_library
    0xb3: gsos_s16_application
    0xb4: gsos_runtime_library
    0xb5: gsos_shell_script
    0xb6: gsos_permanent_init
    0xb7: gsos_temporary_init
    0xb8: gsos_new_desk_accessory
    0xb9: gsos_classic_desk_accessory
    0xba: gsos_tool
    0xbb: gsos_device_driver
    0xbc: gsos_load_file
    0xbd: gsos_file_system_translator
    0xc0: gsos_paintbrush
    0xc1: gsos_super_hires_picture
    0xc8: gsos_font
    0xe0: gsos_library_archive
    0xef: pascal_area
    0xf0: prodos_command
    0xf1: user_defined_1
    0xf2: user_defined_2
    0xf3: user_defined_3
    0xf4: user_defined_4
    0xf5: user_defined_5
    0xf6: user_defined_6
    0xf7: user_defined_7
    0xf8: user_defined_8
    0xfa: integer_basic_program
    0xfb: integer_basic_variables
    0xfc: applesoft_program
    0xfd: applesoft_variables
    0xfe: relocatable_code
    0xff: system_file
