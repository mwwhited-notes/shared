meta:
  id: eeglab_fdt
  title: EEGLAB .fdt raw data file
  file-extension: fdt
  license: CC0-1.0
  endian: le
doc: |
  An EEGLAB .fdt file is headerless: float32 little-endian values stored
  channel-fastest (MATLAB column-major of a channels x frames matrix).
  The shape comes from the paired .set file (fields nbchan, pnts, trials),
  so it is passed in as parameters. The .set file itself is a MATLAB MAT
  file and is not described here.
params:
  - id: nbchan
    type: u4
    doc: Number of channels (EEG.nbchan).
  - id: n_frames
    type: u4
    doc: Total time points, EEG.pnts * EEG.trials.
seq:
  - id: frames
    type: frame
    repeat: expr
    repeat-expr: n_frames
types:
  frame:
    seq:
      - id: values
        type: f4
        repeat: expr
        repeat-expr: _root.nbchan
