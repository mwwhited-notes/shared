meta:
  id: bdf
  title: BioSemi Data Format (BDF / BDF+)
  file-extension: bdf
  license: CC0-1.0
  endian: le
  encoding: ASCII
doc: |
  BDF is EDF with a different identification byte string and 24-bit
  little-endian two's-complement samples instead of 16-bit. Header layout,
  field widths and the data record structure are otherwise identical to
  EDF. See edf.ksy for field notes.

  A signal labelled "Status" typically carries trigger bits in the low
  bits of each 24-bit sample.
seq:
  - id: header
    type: header
  - id: records_known
    type: record
    repeat: expr
    repeat-expr: header.num_records_int
    if: header.num_records_int >= 0
  - id: records_until_eof
    type: record
    repeat: eos
    if: header.num_records_int < 0
types:
  header:
    seq:
      - id: magic
        contents: [0xff, "BIOSEMI"]
        doc: Byte 0xFF followed by "BIOSEMI".
      - id: patient_id
        type: str
        size: 80
        pad-right: 0x20
      - id: recording_id
        type: str
        size: 80
        pad-right: 0x20
      - id: start_date
        type: str
        size: 8
      - id: start_time
        type: str
        size: 8
      - id: header_bytes
        type: str
        size: 8
        pad-right: 0x20
      - id: reserved
        type: str
        size: 44
        pad-right: 0x20
        doc: Starts with "24BIT" in BioSemi files.
      - id: num_records
        type: str
        size: 8
        pad-right: 0x20
      - id: record_duration
        type: str
        size: 8
        pad-right: 0x20
      - id: num_signals
        type: str
        size: 4
        pad-right: 0x20
      - id: label
        type: str
        size: 16
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: transducer
        type: str
        size: 80
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: physical_dimension
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: physical_min
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: physical_max
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: digital_min
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: digital_max
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: prefiltering
        type: str
        size: 80
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: samples_per_record
        type: str
        size: 8
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
      - id: signal_reserved
        type: str
        size: 32
        pad-right: 0x20
        repeat: expr
        repeat-expr: num_signals_int
    instances:
      num_signals_int:
        value: num_signals.to_i
      num_records_int:
        value: num_records.to_i
  record:
    seq:
      - id: signals
        type: signal_block(_index)
        repeat: expr
        repeat-expr: _root.header.num_signals_int
  signal_block:
    params:
      - id: sig
        type: u4
    seq:
      - id: samples
        type: s24le
        repeat: expr
        repeat-expr: _root.header.samples_per_record[sig].to_i
  s24le:
    seq:
      - id: b0
        type: u1
      - id: b1
        type: u1
      - id: b2
        type: u1
    instances:
      unsigned:
        value: '(b2 << 16) | (b1 << 8) | b0'
      value:
        value: 'unsigned >= 0x800000 ? unsigned - 0x1000000 : unsigned'
        doc: Sign-extended 24-bit sample.
