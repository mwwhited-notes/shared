meta:
  id: brainvision_eeg
  title: BrainVision .eeg binary data (multiplexed)
  file-extension: eeg
  license: CC0-1.0
  endian: le
doc: |
  The BrainVision .eeg file is headerless. Its layout is defined by the
  text header (.vhdr, INI-style, not described here). This description
  covers DataOrientation=MULTIPLEXED with BinaryFormat INT_16 or
  IEEE_FLOAT_32, little-endian. VECTORIZED orientation and other binary
  formats are not covered.

  For INT_16 data, multiply by each channel's resolution from the
  [Channel Infos] section of the .vhdr to get physical units.
params:
  - id: n_channels
    type: u4
    doc: NumberOfChannels from the .vhdr.
  - id: n_points
    type: u4
    doc: Number of time points (file size / bytes per value / channels).
  - id: is_float
    type: bool
    doc: true for IEEE_FLOAT_32, false for INT_16.
seq:
  - id: frames
    type: frame
    repeat: expr
    repeat-expr: n_points
types:
  frame:
    seq:
      - id: values
        type:
          switch-on: _root.is_float
          cases:
            true: f4
            false: s2
        repeat: expr
        repeat-expr: _root.n_channels
