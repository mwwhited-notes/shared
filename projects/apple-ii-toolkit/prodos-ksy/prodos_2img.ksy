meta:
  id: prodos_2img
  title: 2IMG disk image container (Apple II)
  file-extension:
    - 2mg
    - 2img
  license: CC0-1.0
  ks-version: 0.9
  endian: le
  imports:
    - prodos_volume
doc: |
  The 2IMG container, a 64-byte header placed in front of a raw Apple II
  disk image. It is most often used to wrap ProDOS-order images for
  emulators (it also holds DOS 3.3-order and NIB images). When
  `header.image_format` is `prodos_order`, `volume` parses the payload as a
  ProDOS volume.

  Reference: the 2IMG format description by Apple II emulator authors
  (Brutal Deluxe / Apple2.org.za "2IMG" specification).

seq:
  - id: header
    type: header
    size: 64

instances:
  volume:
    pos: header.data_offset
    size: 'header.data_length != 0 ? header.data_length : header.prodos_blocks * 512'
    type: prodos_volume
    if: header.image_format == image_format::prodos_order
    doc: The ProDOS volume stored in the image.
  data:
    pos: header.data_offset
    size: header.data_length
    if: header.image_format != image_format::prodos_order
    doc: Raw payload for DOS-order and NIB images.
  comment:
    pos: header.comment_offset
    size: header.comment_length
    type: str
    encoding: UTF-8
    if: header.comment_offset != 0 and header.comment_length != 0
  creator_data:
    pos: header.creator_data_offset
    size: header.creator_data_length
    if: header.creator_data_offset != 0 and header.creator_data_length != 0

types:
  header:
    seq:
      - id: magic
        contents: '2IMG'
      - id: creator
        type: str
        size: 4
        encoding: ASCII
        doc: |
          Four-character ID of the program that made the image, such as
          "WOOF" (Sweet16), "XGS!" (XGS), "CTKG" (Catakig), "ShIm"
          (Sheppy's ImageMaker).
      - id: header_size
        type: u2
        doc: Size of this header, normally 64.
      - id: version
        type: u2
        doc: Version of the 2IMG format, normally 1.
      - id: image_format
        type: u4
        enum: image_format
      - id: flags
        type: flags
      - id: prodos_blocks
        type: u4
        doc: Number of 512-byte blocks. Used for ProDOS-order images, else 0.
      - id: data_offset
        type: u4
        doc: Offset of the disk data from the start of the file.
      - id: data_length
        type: u4
        doc: Length of the disk data in bytes.
      - id: comment_offset
        type: u4
        doc: Offset of an optional comment, or 0.
      - id: comment_length
        type: u4
      - id: creator_data_offset
        type: u4
        doc: Offset of optional creator-specific data, or 0.
      - id: creator_data_length
        type: u4
      - id: reserved
        size: 16

  flags:
    meta:
      bit-endian: le
    seq:
      - id: dos_volume_number
        type: b8
        doc: DOS 3.3 volume number (1-254). Meaningful only if `volume_number_valid`.
      - id: volume_number_valid
        type: b1
      - id: reserved
        type: b22
      - id: locked
        type: b1
        doc: Image is write-protected.

enums:
  image_format:
    0: dos_order
    1: prodos_order
    2: nib
