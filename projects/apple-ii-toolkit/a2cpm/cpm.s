; ---------------------------------------------------------------
; A2CPM - a CP/M-style operating system for the Apple IIe/IIc
; Runs as a ProDOS 8 SYSTEM file loaded at $2000.
; Assembler: ca65 (cc65 suite)
; ---------------------------------------------------------------

        .setcpu "6502"

; --- Monitor ROM entry points -----------------------------------
COUT    = $FDED         ; print char in A (high bit set)
CROUT   = $FD8E         ; print carriage return
RDKEY   = $FD0C         ; wait for key, A = key (high bit set)
GETLN   = $FD6A         ; read line to $0200, X = length
HOME    = $FC58         ; clear screen
PRBYTE  = $FDDA         ; print A as two hex digits
KBD     = $C000         ; keyboard data / strobe
PROMPT  = $33           ; GETLN prompt character
IN      = $0200         ; GETLN input buffer
MLI     = $BF00         ; ProDOS 8 machine language interface

; --- Work areas -------------------------------------------------
CMDBUF  = $0300         ; console buffer: max, length, text
LINE    = CMDBUF+2      ; text of the command line
pathbuf = $4700         ; length-prefixed ProDOS pathname (64 bytes)
TAIL    = $0380         ; command tail for transient programs
BDOSVEC = $03C0         ; JMP bdos
BOOTVEC = $03C3         ; JMP ccp_loop (warm boot)
TPA     = $0800         ; transient program area
TPASIZE = $1800         ; 6K
IOBUF   = $4000         ; 1K ProDOS file buffer (page aligned)
DATABUF = $4400         ; 512-byte block buffer
PATH2   = $4800         ; second pathname (REN)

; --- Zero page (free user locations) ----------------------------
val     = $06           ; 16-bit parsed value
addr    = $08           ; 16-bit working address
cnt     = $EB
cmdidx  = $EC
entleft = $E8
cmdend  = $E7
col     = $E9
tmp     = $ED
bpar    = $EE           ; BDOS parameter ("DE")
dma     = $F0           ; DMA address
curdisk = $F2
fn      = $F3
savx    = $F4
savy    = $F5
ptr     = $FA           ; command table pointer
ptr2    = $FC           ; string pointer
argx    = $FE           ; index of first argument in LINE

        .segment "CODE"

start:
        cld
        lda #0
        sta curdisk
        jsr setvectors
        jsr HOME
        lda #<banner
        ldy #>banner
        jsr puts
        jmp ccp_loop

        .include "bdos.s"
        .include "ccp.s"
        .include "files.s"
        .include "transient.s"
