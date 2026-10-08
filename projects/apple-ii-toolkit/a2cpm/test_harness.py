#!/usr/bin/env python3
"""Run cpm.bin in a 6502 emulator (py65) with mocked Apple II Monitor ROM
routines and a tiny fake ProDOS MLI, then feed it a script of commands."""
import sys
from py65.devices.mpu6502 import MPU

LOAD = 0x2000
bin_path = sys.argv[1] if len(sys.argv) > 1 else "cpm.bin"
script = [l.rstrip("\n") for l in open(sys.argv[2])] if len(sys.argv) > 2 else []

m = MPU()
mem = m.memory
data = open(bin_path, "rb").read()
for i, b in enumerate(data):
    mem[LOAD + i] = b

out = []
lines = list(script)
files = {  # fake ProDOS volume
    "HELLO.TXT": b"HELLO FROM A2CPM\rSECOND LINE\r",
    "TEST.COM": bytes([0xA2, 0x58, 0xA9, 0x02, 0x20, 0xC0, 0x03, 0x60]),  # ldx #'X'; lda #2; jsr BDOS; rts
}
handles = {}
PREFIX = b"/TEST/"

def word(a): return mem[a] | (mem[a + 1] << 8)

def rts():
    sp = m.sp
    m.pc = ((mem[0x100 + ((sp + 1) & 0xFF)] | (mem[0x100 + ((sp + 2) & 0xFF)] << 8)) + 1) & 0xFFFF
    m.sp = (sp + 2) & 0xFF

def dir_block():
    blk = bytearray(512)
    ents = [bytes([0xF0 | 4]) + b"TEST" + bytes(34)]  # volume header
    for n in files:
        e = bytearray(39)
        e[0] = 0x10 | len(n)
        e[1:1 + len(n)] = n.encode()
        ents.append(bytes(e))
    for i, e in enumerate(ents):
        blk[4 + 39 * i:4 + 39 * i + 39] = e
    return bytes(blk)

def pname(addr):
    n = mem[addr]
    return bytes(mem[addr + 1 + i] for i in range(n)).decode()

def mli():
    sp = m.sp
    ret = (mem[0x100 + ((sp + 1) & 0xFF)] | (mem[0x100 + ((sp + 2) & 0xFF)] << 8)) + 1
    m.sp = (sp + 2) & 0xFF
    call, parms = mem[ret], word(ret + 1)
    m.pc = ret + 3
    err = 0
    if call == 0xC7:  # GET_PREFIX
        a = word(parms + 1)
        mem[a] = len(PREFIX)
        for i, c in enumerate(PREFIX): mem[a + 1 + i] = c
    elif call == 0xC8:  # OPEN
        name = pname(word(parms + 1))
        if name.upper() == "/TEST":
            handles[1] = ["DIR", 0]
            mem[parms + 5] = 1
        elif name in files:
            h = max(handles or [1]) + 1
            handles[h] = [name, 0]
            mem[parms + 5] = h
        else:
            err = 0x46
    elif call == 0xCA:  # READ
        h = handles[mem[parms + 1]]
        buf, req = word(parms + 2), word(parms + 4)
        content = dir_block() if h[0] == "DIR" else files[h[0]]
        chunk = content[h[1]:h[1] + req]
        if not chunk: err = 0x4C
        else:
            for i, c in enumerate(chunk): mem[buf + i] = c
            h[1] += len(chunk)
            mem[parms + 6] = len(chunk) & 0xFF
            mem[parms + 7] = len(chunk) >> 8
    elif call == 0xCB:  # WRITE
        h = handles[mem[parms + 1]]
        buf, req = word(parms + 2), word(parms + 4)
        files[h[0]] = bytes(mem[buf + i] for i in range(req))
    elif call == 0xCC:  # CLOSE
        handles.pop(mem[parms + 1], None)
    elif call == 0xC1:  # DESTROY
        n = pname(word(parms + 1))
        if n in files: del files[n]
        else: err = 0x46
    elif call == 0xC2:  # RENAME
        o, n = pname(word(parms + 1)), pname(word(parms + 3))
        if o in files: files[n] = files.pop(o)
        else: err = 0x46
    elif call == 0xC0:  # CREATE
        files[pname(word(parms + 1))] = b""
    elif call == 0x65:  # QUIT
        out.append("<QUIT>"); raise SystemExit
    else:
        out.append("<MLI %02X?>" % call)
    if err:
        m.a = err
        m.p |= 1
    else:
        m.a = 0
        m.p &= ~1

def cout(): out.append(chr(m.a & 0x7F).replace("\r", "\n"))
def getln():
    line = lines.pop(0) if lines else None
    if line is None: out.append("<EOF>"); raise SystemExit
    out.append("%s\n" % line)
    for i, c in enumerate(line): mem[0x200 + i] = ord(c) | 0x80
    mem[0x200 + len(line)] = 0x8D
    m.x = len(line)

hooks = {
    0xFDED: cout,
    0xFD8E: lambda: out.append("\n"),
    0xFC58: lambda: None,
    0xFDDA: lambda: out.append("%02X" % m.a),
    0xFD6A: getln,
}
m.pc = LOAD
steps = 0
try:
    while steps < 3_000_000:
        pc = m.pc
        if pc in hooks:
            hooks[pc](); rts()
        elif pc == 0xBF00:
            mli()
        else:
            m.step()
        steps += 1
except SystemExit:
    pass
print("".join(out))
print("--- files now:", sorted(files))
