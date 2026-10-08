meta:
  id: xdf
  title: Extensible Data Format (XDF), Lab Streaming Layer recordings
  file-extension: xdf
  license: CC0-1.0
  endian: le
  encoding: UTF-8
doc: |
  XDF starts with the magic "XDF:" and is followed by chunks. Each chunk is
  [varlen length][u2 tag][content], where length counts the tag (2 bytes)
  plus the content.

  Varlen integers are a one-byte size (1, 4 or 8) followed by that many
  little-endian bytes.

  Sample chunks are only partly decoded: the channel format and channel
  count live in the stream-header XML, so the per-sample payload is left
  as raw bytes. Each sample is an optional timestamp (flag byte 0 or 8,
  then an f8 if 8) followed by one value per channel.
seq:
  - id: magic
    contents: "XDF:"
  - id: chunks
    type: chunk
    repeat: eos
types:
  varlen_int:
    seq:
      - id: num_bytes
        type: u1
      - id: value
        type:
          switch-on: num_bytes
          cases:
            1: u1
            4: u4
            8: u8
  chunk:
    seq:
      - id: len_chunk
        type: varlen_int
      - id: tag
        type: u2
        enum: chunk_tag
      - id: body
        size: len_chunk.value - 2
        type:
          switch-on: tag
          cases:
            'chunk_tag::file_header': xml_body
            'chunk_tag::stream_header': stream_xml
            'chunk_tag::samples': samples
            'chunk_tag::clock_offset': clock_offset
            'chunk_tag::boundary': boundary
            'chunk_tag::stream_footer': stream_xml
  xml_body:
    seq:
      - id: xml
        type: str
        size-eos: true
  stream_xml:
    seq:
      - id: stream_id
        type: u4
      - id: xml
        type: str
        size-eos: true
  samples:
    seq:
      - id: stream_id
        type: u4
      - id: num_samples
        type: varlen_int
      - id: payload
        size-eos: true
        doc: Needs channel format and count from the stream header XML.
  clock_offset:
    seq:
      - id: stream_id
        type: u4
      - id: collection_time
        type: f8
      - id: offset_value
        type: f8
  boundary:
    seq:
      - id: uuid
        size: 16
        doc: Fixed 16-byte boundary marker.
enums:
  chunk_tag:
    1: file_header
    2: stream_header
    3: samples
    4: clock_offset
    5: boundary
    6: stream_footer
