; ---------------------------------------------------------------
; bdos.s - CP/M-style BDOS for the Apple II (6502)
;
; Calling convention (the 6502 analogue of CP/M's C and DE):
;     A = function number, X/Y = parameter low/high ("DE")
;     result returned in A
; Call with:  jsr BDOS_ENTRY
; ---------------------------------------------------------------

; --- Output one 7-bit character, preserving X and Y. LF is ignored
;     because the Apple screen already advances on CR.
putc:
        and #$7F
        cmp #$0A
        beq @r
        ora #$80
        stx savx
        sty savy
        jsr COUT
        ldx savx
        ldy savy
@r:     rts

; --- Print zero-terminated string; A = low, Y = high
puts:
        sta ptr2
        sty ptr2+1
        ldy #0
@l:     lda (ptr2),y
        beq @d
        jsr putc
        iny
        bne @l
        inc ptr2+1
        bne @l
@d:     rts

; --- BDOS dispatcher --------------------------------------------
bdos:
        sta fn
        stx bpar
        sty bpar+1
        ldx #0
@find:  lda bdostab,x
        cmp #$FF
        beq @none
        cmp fn
        beq @found
        inx
        inx
        inx
        bne @find
@none:  lda #0
        rts
@found: lda bdostab+1,x
        sta ptr
        lda bdostab+2,x
        sta ptr+1
        jmp (ptr)               ; handler's RTS returns to the caller

; --- f0: system reset (warm boot) -------------------------------
f_reset:
        jmp ccp_loop

; --- f1: console input with echo --------------------------------
f_conin:
        jsr RDKEY
        pha
        jsr COUT
        pla
        and #$7F
        rts

; --- f2: console output, character in "E" (X on entry) ----------
f_conout:
        lda bpar
        jsr putc
        rts

; --- f9: print string terminated by '$' -------------------------
f_prstr:
        ldy #0
@l:     lda (bpar),y
        cmp #'$'
        beq @d
        jsr putc
        iny
        bne @l
        inc bpar+1
        bne @l
@d:     rts

; --- f10: read console buffer -----------------------------------
; Buffer layout: [0]=max length, [1]=length returned, [2..]=text
f_rdbuf:
        lda #$A0                ; GETLN prompt: a space
        sta PROMPT
        jsr GETLN               ; X = length, text at $0200
        ldy #0
        lda (bpar),y            ; caller's maximum
        cmp #254
        bcc @cap
        lda #253
@cap:   sta tmp
        cpx tmp
        bcc @ok
        beq @ok
        ldx tmp
@ok:    stx cnt
        ldy #1
        txa
        sta (bpar),y            ; store length
        ldx #0
@cp:    cpx cnt
        beq @d
        txa
        clc
        adc #2
        tay
        lda IN,x
        and #$7F
        sta (bpar),y
        inx
        bne @cp
@d:     lda cnt
        rts

; --- f11: console status (255 = key waiting) --------------------
f_const:
        lda KBD
        bpl @no
        lda #$FF
        rts
@no:    lda #0
        rts

; --- f12: return version number (2.2) ---------------------------
f_ver:
        lda #$22
        rts

; --- f25: return current disk (0 = A:) --------------------------
f_curdsk:
        lda curdisk
        rts

; --- f26: set DMA address ---------------------------------------
f_setdma:
        lda bpar
        sta dma
        lda bpar+1
        sta dma+1
        rts

; Table entries: function number, handler address. $FF ends the list.
bdostab:
        .byte 0
        .word f_reset
        .byte 1
        .word f_conin
        .byte 2
        .word f_conout
        .byte 9
        .word f_prstr
        .byte 10
        .word f_rdbuf
        .byte 11
        .word f_const
        .byte 12
        .word f_ver
        .byte 25
        .word f_curdsk
        .byte 26
        .word f_setdma
        .byte $FF
