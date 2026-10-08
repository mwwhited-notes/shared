; ---------------------------------------------------------------
; A2SHELL - a tiny shell for the Apple II family (IIe/IIc)
; Runs as a ProDOS 8 SYSTEM file loaded at $2000.
; Assembler: ca65 (cc65 suite)
; ---------------------------------------------------------------

        .setcpu "6502"

; --- Monitor ROM entry points -----------------------------------
COUT    = $FDED         ; print char in A (high bit set)
CROUT   = $FD8E         ; print carriage return
GETLN   = $FD6A         ; read line to $0200, X = length
HOME    = $FC58         ; clear screen
PRBYTE  = $FDDA         ; print A as two hex digits
PROMPT  = $33           ; prompt character location
IN      = $0200         ; GETLN input buffer
MLI     = $BF00         ; ProDOS 8 machine language interface

; --- Zero page (free user locations) ----------------------------
val     = $06           ; 16-bit parsed value
addr    = $08           ; 16-bit working address
cnt     = $EB
cmdidx  = $EC
tmp     = $ED
ptr     = $FA           ; command table pointer
ptr2    = $FC           ; string pointer
argx    = $FE           ; index of first argument in IN

        .segment "CODE"

; ---------------------------------------------------------------
start:
        cld
        jsr HOME
        lda #<banner
        ldy #>banner
        jsr puts
main:
        lda #'>'|$80
        sta PROMPT
        jsr GETLN
        lda #0
        sta IN,x                ; replace trailing CR with terminator
        jsr strip               ; clear high bits in the line
        jsr parse
        jmp main

; Clear the high bit of every character in the input line
strip:
        ldx #0
@l:     lda IN,x
        beq @d
        and #$7F
        sta IN,x
        inx
        bne @l
@d:     rts

; Uppercase A if it is a-z
fold:
        cmp #'a'
        bcc @r
        cmp #'z'+1
        bcs @r
        sbc #$1F                ; carry clear: subtracts $20
@r:     rts

; Print zero-terminated string; A = low, Y = high
puts:
        sta ptr2
        sty ptr2+1
        ldy #0
@l:     lda (ptr2),y
        beq @d
        ora #$80
        jsr COUT
        iny
        bne @l
        inc ptr2+1
        bne @l
@d:     rts

; ---------------------------------------------------------------
; parse: find the command in the table and dispatch to it.
; Table entry: name (uppercase, 0-terminated), handler address.
; A handler gets argx = index of first argument in IN.
; ---------------------------------------------------------------
parse:
        ldx #0
@skip:  lda IN,x
        beq @empty
        cmp #' '
        bne @got
        inx
        bne @skip
@empty: rts
@got:   stx cmdidx
        lda #<cmdtab
        sta ptr
        lda #>cmdtab
        sta ptr+1
@next:  ldy #0
        lda (ptr),y
        beq @unknown            ; end of table
        ldx cmdidx
@cmp:   lda IN,x
        jsr fold
        sta tmp
        lda (ptr),y
        beq @nameend
        cmp tmp
        bne @nomatch
        inx
        iny
        bne @cmp
@nameend:
        lda tmp                 ; input word must end here
        beq @match
        cmp #' '
        beq @match
@nomatch:
@scan:  lda (ptr),y             ; advance Y to name terminator
        beq @atz
        iny
        bne @scan
@atz:   iny                     ; skip terminator and 2-byte address
        iny
        iny
        tya
        clc
        adc ptr
        sta ptr
        bcc @next
        inc ptr+1
        bne @next
@match: iny                     ; Y -> handler low byte
        lda (ptr),y
        pha
        iny
        lda (ptr),y
        sta ptr+1
        pla
        sta ptr
@sp:    lda IN,x                ; skip spaces before arguments
        cmp #' '
        bne @sd
        inx
        bne @sp
@sd:    stx argx
        jmp (ptr)               ; handler's RTS returns to main loop
@unknown:
        lda #<msg_unk
        ldy #>msg_unk
        jmp puts

; ---------------------------------------------------------------
; parsehex: parse hex number at IN,X into val.
; Returns carry clear on success (X advanced), set if no digits.
; ---------------------------------------------------------------
parsehex:
@sp:    lda IN,x
        cmp #' '
        bne @go
        inx
        bne @sp
@go:    lda #0
        sta val
        sta val+1
        sta cnt
@dig:   lda IN,x
        cmp #'0'
        bcc @end
        cmp #'9'+1
        bcc @num
        and #$DF                ; fold to uppercase
        cmp #'A'
        bcc @end
        cmp #'F'+1
        bcs @end
        sbc #'A'-10-1           ; carry clear: A - 'A' + 10
        jmp @add
@num:   sec
        sbc #'0'
@add:   asl val
        rol val+1
        asl val
        rol val+1
        asl val
        rol val+1
        asl val
        rol val+1
        ora val
        sta val
        inc cnt
        inx
        jmp @dig
@end:   lda cnt
        beq @none
        clc
        rts
@none:  sec
        rts

; ---------------------------------------------------------------
; Commands
; ---------------------------------------------------------------
usage:
        lda #<msg_use
        ldy #>msg_use
        jmp puts

cmd_help:
        lda #<msg_help
        ldy #>msg_help
        jmp puts

cmd_ver:
        lda #<banner
        ldy #>banner
        jmp puts

cmd_cls:
        jmp HOME

cmd_echo:
        ldx argx
@l:     lda IN,x
        beq @d
        ora #$80
        jsr COUT
        inx
        bne @l
@d:     jmp CROUT

cmd_peek:
        ldx argx
        jsr parsehex
        bcs usage
        ldy #0
        lda (val),y
        jsr PRBYTE
        jmp CROUT

cmd_poke:
        ldx argx
        jsr parsehex
        bcs usage
        lda val
        sta addr
        lda val+1
        sta addr+1
        jsr parsehex
        bcs usage
        lda val
        ldy #0
        sta (addr),y
        rts

cmd_dump:
        ldx argx
        jsr parsehex
        bcs usage
        lda val
        sta addr
        lda val+1
        sta addr+1
        lda #8                  ; 8 lines of 8 bytes
        sta cnt
@line:  lda addr+1
        jsr PRBYTE
        lda addr
        jsr PRBYTE
        lda #':'|$80
        jsr COUT
        ldy #0
@byte:  lda #' '|$80
        jsr COUT
        lda (addr),y
        jsr PRBYTE
        iny
        cpy #8
        bne @byte
        jsr CROUT
        lda addr
        clc
        adc #8
        sta addr
        bcc @nc
        inc addr+1
@nc:    dec cnt
        bne @line
        rts

cmd_call:
        ldx argx
        jsr parsehex
        bcs @bad
        jsr @go
        rts
@bad:   jmp usage
@go:    jmp (val)

cmd_quit:
        jsr MLI
        .byte $65               ; QUIT
        .word quitparms
        rts

quitparms:
        .byte 4,0,0,0,0,0,0

; ---------------------------------------------------------------
; Data
; ---------------------------------------------------------------
cmdtab:
        .asciiz "HELP"
        .word cmd_help
        .asciiz "VER"
        .word cmd_ver
        .asciiz "CLS"
        .word cmd_cls
        .asciiz "ECHO"
        .word cmd_echo
        .asciiz "PEEK"
        .word cmd_peek
        .asciiz "POKE"
        .word cmd_poke
        .asciiz "DUMP"
        .word cmd_dump
        .asciiz "CALL"
        .word cmd_call
        .asciiz "QUIT"
        .word cmd_quit
        .byte 0                 ; end of table

banner: .byte "A2SHELL 0.1",13,"TYPE HELP FOR COMMANDS",13,0
msg_unk:.byte "UNKNOWN COMMAND",13,0
msg_use:.byte "BAD ARGUMENT",13,0
msg_help:
        .byte "HELP        THIS LIST",13
        .byte "VER         SHOW VERSION",13
        .byte "CLS         CLEAR SCREEN",13
        .byte "ECHO TEXT   PRINT TEXT",13
        .byte "PEEK AAAA   READ A BYTE",13
        .byte "POKE AAAA VV  WRITE A BYTE",13
        .byte "DUMP AAAA   HEX DUMP 64 BYTES",13
        .byte "CALL AAAA   JSR TO ADDRESS",13
        .byte "QUIT        EXIT TO PRODOS",13,0
