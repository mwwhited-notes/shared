# CLAUDE.md

Learning project on EEG file formats, lossless storage and time synchronization (overnight studies with video). Read `README.md` first for the conversation summary and file index.

## Layout
- `ksy/` Kaitai Struct descriptions (EDF, BDF, FIF, XDF, EEGLAB .fdt, BrainVision .eeg)
- `tools/` `run_checks.sh` compiles every `.ksy` and parses synthetic files (needs node, python3, `pip install kaitaistruct`)
- `docs/` topic notes; `docs/04-canonical-format-design.md` is the draft custom format

## Conventions
- Keep the confidence tags: **[tested]**, **[found]**, **[memory]**. Do not upgrade a [memory] claim without checking a source.
- After editing any `.ksy`, run `tools/run_checks.sh`.
- `.ksy` files describe byte layout only. Text formats (.vhdr, .vmrk), MATLAB `.set` and BIDS are intentionally not covered.
- Do not present anything here as clinical or medical-device guidance.

## Likely next tasks
See "Open questions and next steps" in `README.md`.
