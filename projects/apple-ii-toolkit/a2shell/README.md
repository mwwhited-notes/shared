# A2SHELL

A small shell for the Apple II family (IIe/IIc), written in 6502 assembly.
It runs as a ProDOS 8 SYSTEM file loaded at $2000 and uses the Monitor ROM
for console I/O (GETLN, COUT, HOME, PRBYTE).

## Commands

| Command | Action |
|---|---|
| `HELP` | List commands |
| `VER` | Show version |
| `CLS` | Clear screen |
| `ECHO text` | Print text |
| `PEEK aaaa` | Print the byte at a hex address |
| `POKE aaaa vv` | Write a byte |
| `DUMP aaaa` | Hex dump 64 bytes |
| `CALL aaaa` | JSR to an address |
| `QUIT` | Return to ProDOS |

Commands are case-insensitive. Numbers are hex.

## Build

Requires cc65 (ca65/ld65).

    make            # produces shell.bin (loads at $2000)

To run it, put it on a bootable ProDOS disk image:

1. Start from a ProDOS 8 disk image that has the `PRODOS` file (140K `.po`).
2. Copy `shell.bin` onto it as `SHELL.SYSTEM`, type `$FF`, load address `$2000`
   (AppleCommander: `make disk`, after editing the image name in the Makefile).
3. Boot it in an emulator (AppleWin, MAME apple2c, or Virtual II).
   ProDOS runs the first `*.SYSTEM` file automatically.

## Adding a command

Add a handler that ends with `rts`, then add an entry to `cmdtab`:

    .asciiz "NAME"
    .word cmd_name

On entry, `argx` holds the index into the input buffer (`IN`) of the first
argument; use `parsehex` to read a hex number.

## Next steps

- Directory listing (`CAT`) and file load/run through the ProDOS MLI
- Use the aux 64K for a RAM disk or program buffers
- Replace ProDOS with your own boot sector and disk layer
