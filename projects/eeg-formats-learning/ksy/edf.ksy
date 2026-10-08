meta:
  id: edf
  title: European Data Format (EDF / EDF+)
  file-extension: edf
  license: CC0-1.0
  endian: le
  encoding: ASCII
doc: |
  EDF: fixed 256-byte ASCII main header, then 256 bytes per signal of
  field-major signal headers, then data records. Each data record holds,
  for every signal in order, `samples_per_record` little-endian int16
  samples.

  Header text fields are space padded. Numeric fields are ASCII; physical
  and digital min/max are kept as strings here (they can be decimals).

  EDF+: `reserved` starts with "EDF+C" (continuous) or "EDF+D"
  (discontinuous). A signal labelled "EDF Annotations" carries
  time-stamped annotation lists (TALs) as ASCII bytes inside its int16
  samples; this file parses those as ordinary samples.

  If num_records is -1 (recording still in progress) records are read
  until end of stream.
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
      - id: version
        type: str
        size: 8
        doc: Always "0       " in EDF.
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
        doc: dd.mm.yy
      - id: start_time
        type: str
        size: 8
        doc: hh.mm.ss
      - id: header_bytes
        type: str
        size: 8
        pad-right: 0x20
        doc: Total header length, 256 + 256 * num_signals.
      - id: reserved
        type: str
        size: 44
        pad-right: 0x20
      - id: num_records
        type: str
        size: 8
        pad-right: 0x20
        doc: Number of data records, -1 if unknown.
      - id: record_duration
        type: str
        size: 8
        pad-right: 0x20
        doc: Duration of one data record in seconds.
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
        doc: Samples per signal in each data record.
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
        type: s2
        repeat: expr
        repeat-expr: _root.header.samples_per_record[sig].to_i
