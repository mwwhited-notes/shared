; ---------------------------------------------------------------
; transient.s - load and run transient programs, and SAVE
;
; Memory map:
;   $0800-$1FFF  TPA (transient program area, 6K)
;   $0380        command tail: length byte, text, 0
;   $03C0        BDOS entry vector (JMP bdos)
;   $03C3        warm boot vector (JMP ccp_loop)
;   $2000-       CCP + BDOS
; A program is entered with JSR $0800 and returns to the CCP with RTS.
; ---------------------------------------------------------------

; --- Install the entry vectors (called once at start-up) --------
setvectors:
        lda #$4C                ; JMP opcode
        sta BDOSVEC
        sta BOOTVEC
        lda #<bdos
        sta BDOSVEC+1
        lda #>bdos
        sta BDOSVEC+2
        lda #<ccp_loop
        sta BOOTVEC+1
        lda #>ccp_loop
        sta BOOTVEC+2
        lda #<TAIL              ; default DMA = command tail
        sta dma
        lda #>TAIL
        sta dma+1
        rts

; --- unknown: try to run NAME.COM from disk ---------------------
unknown:
        lda #<pathbuf
        sta addr
        lda #>pathbuf
        sta addr+1
        ldx cmdidx
        jsr copyname            ; command word -> pathbuf
        stx cmdend              ; X is at the end of the word
        ldy pathbuf
@dot:   lda pathbuf,y           ; has an extension already?
        cmp #'.'
        beq @haveext
        dey
        bne @dot
        ldx pathbuf             ; no: append ".COM"
        cpx #59
        bcs @fail
        ldy #0
@ap:    lda dotcom,y
        sta pathbuf+1,x
        inx
        iny
        cpy #4
        bne @ap
        stx pathbuf
@haveext:
        MLICALL $C8, open_p
        bcs @fail
        lda open_p+5
        sta tread_p+1
        sta close_p+1
        MLICALL $CA, tread_p
        php                     ; remember the read result
        pha
        MLICALL $CC, close_p
        pla
        plp
        bcs @readerr
        jsr settail
        jsr TPA                 ; run the program
        jmp ccp_loop
@readerr:
        cmp #$4C                ; EOF just means a short file: fine
        beq @short
        jmp mlierr
@short: jsr settail
        jsr TPA
        jmp ccp_loop
@fail:  jmp unknown_msg

; --- settail: copy the text after the command word to TAIL ------
settail:
        ldx cmdend
@sp:    lda LINE,x
        cmp #' '
        bne @go
        inx
        bne @sp
@go:    ldy #0
@c:     lda LINE,x
        sta TAIL+1,y
        beq @d
        inx
        iny
        cpy #62
        bne @c
        lda #0
        sta TAIL+1,y
@d:     sty TAIL
        rts

; --- parsedec: decimal number at LINE,X -> val (8 bit)
;     Carry set if at least one digit was found.
parsedec:
        lda #0
        sta val
        sta cnt
@d:     lda LINE,x
        sec
        sbc #'0'
        cmp #10
        bcs @e
        sta tmp
        lda val
        asl
        sta val+1               ; val*2
        asl
        asl                     ; val*8
        clc
        adc val+1
        clc
        adc tmp
        sta val
        inc cnt
        inx
        jmp @d
@e:     lda cnt
        cmp #1
        rts

; --- SAVE n name: write n 256-byte pages from the TPA to a file
cmd_save:
        ldx argx
        jsr parsedec
        bcs @num
        jmp usage
@num:   lda val
        beq @badn
        cmp #24+1               ; the TPA is 24 pages
        bcc @okn
@badn:  jmp usage
@okn:   sta wr_p+5              ; request count, high byte
@sk:    lda LINE,x              ; skip spaces
        cmp #' '
        bne @nm
        inx
        bne @sk
@nm:    lda #<pathbuf
        sta addr
        lda #>pathbuf
        sta addr+1
        jsr copyname
        bcs @have
        jmp usage
@have:  MLICALL $C1, destroy_p  ; replace an existing file; ignore errors
        MLICALL $C0, create_p
        bcc @made
        jmp mlierr
@made:  MLICALL $C8, open_p
        bcc @op
        jmp mlierr
@op:    lda open_p+5
        sta wr_p+1
        sta close_p+1
        MLICALL $CB, wr_p
        php
        pha
        MLICALL $CC, close_p
        pla
        plp
        bcc @done
        jmp mlierr
@done:  rts

dotcom: .byte ".COM"

tread_p:
        .byte 4
        .byte 0                 ; ref_num
        .addr TPA
        .word TPASIZE
        .word 0
wr_p:   .byte 4
        .byte 0                 ; ref_num
        .addr TPA
        .word 0                 ; request count (set by SAVE)
        .word 0
create_p:
        .byte 7
        .addr pathbuf
        .byte $C3               ; access: destroy, rename, write, read
        .byte $06               ; file type BIN
        .word TPA               ; aux type = load address
        .byte $01               ; seedling file
        .word 0                 ; create date
        .word 0                 ; create time
