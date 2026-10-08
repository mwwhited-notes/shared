# Apple II toolkit

Three small projects that grew out of one question: how would you build an operating
system with a shell for the Apple IIc, in 6502 assembly, and how do you describe its
disk format precisely enough to test against?

| Folder | What it is | Language | State |
|---|---|---|---|
| `a2shell/` | A tiny command shell that runs as a ProDOS 8 `SYSTEM` file. Starting point. | 6502 asm (ca65) | Assembles. Not run on an Apple II or an Apple II emulator. |
| `a2cpm/` | A CP/M-style OS (command processor, BDOS calls, transient programs) on top of ProDOS files. Grew out of `a2shell`. | 6502 asm (ca65) | Assembles. Tested under a 6502 emulator with mocked ROM and ProDOS. |
| `prodos-ksy/` | Kaitai Struct descriptions of the ProDOS 8 volume and the 2IMG container, plus a generated block-layout diagram page. | KSY, Python | Compiles. Tested on a synthetic image I built, not on real disks. |

## Quick start

    pip install -r requirements.txt        # kaitaistruct, pyyaml, py65
    # assembler: cc65 (ca65 + ld65), e.g. `apt install cc65` or `brew install cc65`

    make -C a2shell                        # -> a2shell/shell.bin
    make -C a2cpm                          # -> a2cpm/cpm.bin
    make -C a2cpm test                     # run a command script in py65
    make -C prodos-ksy test                # needs the Kaitai compiler (kaitai-struct-compiler)
    make -C prodos-ksy test-js             # same, using the npm compiler (needs Node.js)
    make -C prodos-ksy diagram             # rebuild prodos_layout.html

To boot either OS, copy the `.bin` onto a bootable ProDOS 8 disk image as a `.SYSTEM`
file (type `$FF`, load address `$2000`), then start it in an emulator such as AppleWin
or MAME. Each project's own README has the details.

## How the pieces relate

- `a2shell` and `a2cpm` both call the ProDOS Machine Language Interface (MLI at `$BF00`)
  for files, so what they read and write is a ProDOS volume.
- `prodos-ksy/prodos_volume.ksy` describes that volume. Its test builds a small volume in
  Python and parses it back, so it doubles as a check on how the OS code reads directories.
  It is not yet wired to the OS test.
- `prodos-ksy/prodos_layout.html` is generated from the `.ksy` files by `build_diagram.py`,
  so the diagrams follow the specs. Published copy: https://claude.ai/artifact/PkBZTqSKNLsoevsiDkUXLW
  (private to the original owner; the file in this folder is the same page).

## Honest status

- Nothing here has run on real Apple II hardware, or in a full Apple II emulator.
- `a2cpm`'s test uses a harness that fakes the Monitor ROM routines and a handful of MLI
  calls. The fake was written from the same understanding of ProDOS as the code, so it
  cannot catch a shared misunderstanding. The MLI parameter-list layouts and call numbers
  were written from memory of the *ProDOS 8 Technical Reference Manual* and should be
  checked against it.
- The KSY specs were checked against a synthetic image, not against real ProDOS disks.
- Some details are intentionally left raw or incomplete: GS/OS lowercase name flags,
  Finder info in forked files, DOS 3.3 / `.do` images, and the file-type list (common types only).
- Earlier discussion of IIc/IIe memory banking and the 1 MB expansion RAM was from memory,
  and parts of it were flagged as uncertain. Treat register addresses and bank-switch
  details as unverified until checked against the Apple IIc Technical Reference.

## Ideas for next steps

1. Run `a2cpm` in a real emulator (MAME `apple2c` or AppleWin) and fix whatever the mock hid.
2. Add the file-control-block BDOS calls (functions 15 to 22 and 33 to 34), wildcards in
   `ERA` and `REN`, and drive letters.
3. Share data between the OS and the specs: have the test build a volume with the KSY-derived
   layout, then read it with `DIR` and `TYPE` under py65.
4. More specs: DOS 3.3 (VTOC, catalog, track/sector lists), WOZ 2, NIB.
5. Use the IIc's auxiliary 64K for a RAM disk or program buffers.
6. Longer term: replace ProDOS with a boot sector and a disk layer of your own.

**Related:** Originally documented in [projects/project-ideas.md](../project-ideas.md).
Real disk images to test against can come from [apple-ii-disk-archival](../apple-ii-disk-archival/).

See `CLAUDE.md` for working conventions if you open this folder in Claude Code.
