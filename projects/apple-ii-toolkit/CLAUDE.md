# CLAUDE.md

Guidance for working in this repository. See `README.md` for the overview.

## Layout

- `a2shell/`   shell.s (single file). Assembler config `a2shell.cfg` links at `$2000`.
- `a2cpm/`     cpm.s includes bdos.s, ccp.s, files.s, transient.s. Config `a2cpm.cfg`.
- `prodos-ksy/` `.ksy` specs, a synthetic-image builder and tests, and the diagram generator.

## Commands

    make -C a2shell
    make -C a2cpm            # builds cpm.bin
    make -C a2cpm test       # py65 harness, prints the session transcript
    make -C prodos-ksy test  # or test-js without the JVM compiler
    make -C prodos-ksy diagram

Tools: cc65 (ca65, ld65), Python 3 with `kaitaistruct`, `pyyaml`, `py65`, and either
`kaitai-struct-compiler` or Node.js.

## Conventions

- 6502 code is ca65 syntax, `.setcpu "6502"` (no 65C02 instructions, so it runs on a plain
  IIe too). Keep branches short; ca65 reports "Range error" for a branch over 127 bytes, and
  the fix used so far is to branch over a `jmp`.
- Strings are 7-bit ASCII in the source. Anything sent to the Monitor `COUT` routine needs
  the high bit set, and `putc` in `bdos.s` does that. Text read through `GETLN` comes back
  with the high bit set and is stripped by `strip`/the console-buffer routine.
- Zero page: the code uses `$06-$09`, `$E7-$F5`, `$FA-$FE`. Check before adding more.
- Memory map for a2cpm: CCP/BDOS at `$2000`, program area `$0800-$1FFF`, ProDOS file buffer
  `$4000`, block buffer `$4400`, pathnames `$4700` and `$4800`. The binary must stay below `$4000`.
- KSY: a parsed `.ksy` file is the source of truth for field offsets. `layout.py` reads the
  `.ksy` files to build the diagrams, and the diagram build asserts struct sizes, so edit the
  spec and rebuild rather than editing the HTML.
- `prodos_volume.ksy` threads the volume stream through types as a `vol_io` parameter, so the
  type works when embedded in 2IMG. Keep that pattern when adding pointer-following types.

## Verification expectations

- A passing `make -C a2cpm test` shows the code agrees with the test harness, not that it
  works on a real machine. When behavior depends on the ROM or ProDOS, say what was checked
  and what was not, and prefer testing in an Apple II emulator.
- Hardware and ProDOS details here were written from memory. Verify addresses, MLI parameter
  layouts and file formats against Apple's manuals before relying on them.
- Do not report the KSY specs as validated against real disks; they are tested on a synthetic image.

## Good first tasks

See "Ideas for next steps" in `README.md`.
