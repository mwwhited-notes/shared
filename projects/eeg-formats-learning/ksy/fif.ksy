meta:
  id: fif
  title: FIFF (Neuromag / Elekta / MEGIN), used by MNE-Python
  file-extension: fif
  license: CC0-1.0
  endian: be
doc: |
  FIFF is a flat stream of tags. Each tag has a 16-byte big-endian header
  (kind, type, size, next) followed by `size` bytes of data. Block
  structure (raw data, measurement info, etc.) is expressed by
  BLOCK_START / BLOCK_END tags rather than by the byte layout.

  `next`: 0 means the next tag follows immediately, -1 means no further
  tag, a positive value is an absolute file offset of the next tag.

  The type field's low 16 bits are the base type (see fiff_type); the
  upper bits encode matrix and sparse-matrix variants. Only the first
  tag, FILE_ID, is decoded here; other payloads are left as bytes because
  their meaning depends on kind and type.

  Constants are written from memory; verify against MNE-Python's
  mne/_fiff/constants.py before relying on them.
seq:
  - id: tags
    type: tag
    repeat: eos
types:
  tag:
    seq:
      - id: kind
        type: s4
        enum: fiff_kind
      - id: type_code
        type: u4
      - id: size
        type: s4
      - id: next
        type: s4
      - id: data
        size: size
        type:
          switch-on: kind
          cases:
            'fiff_kind::file_id': id_struct
            _: raw_bytes
    instances:
      base_type:
        value: type_code & 0xffff
      matrix_flags:
        value: type_code & 0xffff0000
  id_struct:
    seq:
      - id: version
        type: s4
        doc: Major version in high 16 bits, minor in low 16 bits.
      - id: machine_id
        type: u4
        repeat: expr
        repeat-expr: 2
      - id: time_secs
        type: s4
      - id: time_usecs
        type: s4
  raw_bytes:
    seq:
      - id: bytes
        size-eos: true
enums:
  fiff_kind:
    100: file_id
    101: dir_pointer
    102: dir
    103: block_id
    104: block_start
    105: block_end
    200: nchan
    201: sfreq
    300: data_buffer
  fiff_type:
    0: void
    1: byte
    2: short
    3: int
    4: float
    5: double
    6: julian
    7: ushort
    8: uint
    9: ulong
    10: string
    11: long
    30: ch_info_struct
    31: id_struct
    32: dir_entry_struct
    33: dig_point_struct
    34: ch_pos_struct
    35: coord_trans_struct
