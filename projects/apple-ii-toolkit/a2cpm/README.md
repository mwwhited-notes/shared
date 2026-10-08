# A2CPM

A CP/M-style operating system for the Apple IIe/IIc, in 6502 assembly (ca65).
It runs as a ProDOS 8 `CPM.SYSTEM` file at $2000 and uses ProDOS for the disk,
so files are ordinary ProDOS files. It is a clone of CP/M's *structure* (CCP +
BDOS + TPA), not a binary-compatible one: real CP/M programs need an 8080/Z80.

## Layout

| Part | Where | Role |
|---|---|---|
| CCP | `ccp.s` | `A>` prompt, command parser, built-ins |
| BDOS | `bdos.s` | numbered system calls |
| Files | `files.s` | DIR, TYPE, ERA, REN via the ProDOS MLI |
| Programs | `transient.s` | loads `NAME.COM`, SAVE, entry vectors |
| TPA | $0800-$1FFF | transient program area (6K) |
| Command tail | $0380 | length byte, text, 0 (also the default DMA) |
| BDOS entry | $03C0 | `jsr $03C0` |
| Warm boot | $03C3 | `jmp $03C3` |

## Commands

`DIR`, `TYPE name`, `ERA name`, `REN new=old`, `SAVE n name` (n = pages from
$0800, decimal), `DUMP aaaa` (hex), `MEM`, `VER`, `CLS`, `HELP`, `EXIT`.
Anything else is loaded as `NAME.COM` into the TPA and run with `JSR $0800`;
a program returns to the CCP with `RTS`.

## BDOS calls

Call `jsr $03C0` with A = function, X/Y = parameter low/high; result in A.

| Fn | Action |
|---|---|
| 0 | warm boot |
| 1 | console input with echo |
| 2 | console output, character in X |
| 9 | print string at X/Y ended by `$` |
| 10 | read console buffer at X/Y: [max][length returned][text] |
| 11 | console status (255 = key waiting) |
| 12 | version (returns $22) |
| 25 | current disk |
| 26 | set DMA address |

## Build and test

    make          # cpm.bin, loads at $2000 (needs cc65)
    make test     # runs it in a 6502 emulator against a fake ProDOS (needs py65)
    make disk     # copy to a ProDOS image with AppleCommander

Boot it by copying `cpm.bin` onto a bootable ProDOS 8 image as `CPM.SYSTEM`
(type $FF, load address $2000) and starting it in an emulator.

## Not done yet

FCB-based file calls (BDOS 15-22, 33-34), drive letters other than A:, user
areas, and CP/M wildcards in ERA/REN. The 8080 emulation needed to run real
CP/M programs is not started.
