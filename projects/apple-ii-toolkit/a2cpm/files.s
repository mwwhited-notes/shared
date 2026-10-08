; ---------------------------------------------------------------
; files.s - file commands on top of the ProDOS 8 MLI
; ---------------------------------------------------------------

.macro MLICALL code, parms
        jsr MLI
        .byte code
        .addr parms
.endmacro

; --- Report a ProDOS error code (A) -----------------------------
mlierr:
        cmp #$44
        beq @nf
        cmp #$45
        beq @nf
        cmp #$46
        beq @nf
        pha
        lda #<msg_err
        ldy #>msg_err
        jsr puts
        pla
        jsr PRBYTE
        jmp CROUT
@nf:    lda #<msg_nofile
        ldy #>msg_nofile
        jmp puts

; --- copyname: copy a filename from LINE,X to the length-prefixed
;     buffer at (addr). Stops at space, '=' or end of line.
;     On return X is at the terminator; carry set if name length >= 1.
copyname:
        lda #0
        sta cnt
@l:     lda LINE,x
        beq @e
        cmp #' '
        beq @e
        cmp #'='
        beq @e
        jsr fold
        ldy cnt
        iny
        sta (addr),y
        inx
        inc cnt
        lda cnt
        cmp #63
        bne @l
@e:     ldy #0
        lda cnt
        sta (addr),y
        cmp #1
        rts

; --- getname: argument -> pathbuf. Carry set if a name was given.
getname:
        lda #<pathbuf
        sta addr
        lda #>pathbuf
        sta addr+1
        ldx argx
        jmp copyname

; --- DIR: list files in the current ProDOS prefix, 4 per line ----
cmd_dir:
        MLICALL $C7, getprefix_p
        bcs mlierr
        ldx pathbuf
        bne @hasp
        jmp @noprefix
@hasp:  lda pathbuf,x           ; drop trailing '/'
        cmp #'/'
        bne @open
        dec pathbuf
@open:  MLICALL $C8, open_p
        bcs mlierr
        lda open_p+5
        sta read_p+1
        sta close_p+1
        lda #0
        sta col
@blk:   MLICALL $CA, read_p
        bcs @done               ; EOF ($4C) or error ends the listing
        lda #<(DATABUF+4)
        sta addr
        lda #>(DATABUF+4)
        sta addr+1
        lda #13
        sta entleft
@ent:   ldy #0
        lda (addr),y
        and #$F0
        beq @skip               ; inactive entry
        cmp #$E0
        beq @skip               ; volume directory header
        cmp #$F0
        beq @skip               ; subdirectory header
        lda (addr),y
        and #$0F
        sta cnt                 ; name length
        tax
        ldy #1
@nm:    cpx #0
        beq @pad
        lda (addr),y
        jsr putc
        iny
        dex
        jmp @nm
@pad:   inc col
        lda col
        cmp #4
        bne @spc
        lda #0
        sta col
        jsr CROUT
        jmp @skip
@spc:   lda #16                 ; pad the name out to 16 columns
        sec
        sbc cnt
        tax
@sp:    lda #' '
        jsr putc
        dex
        bne @sp
@skip:  lda addr
        clc
        adc #39
        sta addr
        bcc @nc
        inc addr+1
@nc:    dec entleft
        bne @ent
        jmp @blk
@done:  lda col
        beq @cl
        jsr CROUT
@cl:    MLICALL $CC, close_p
        rts
@noprefix:
        lda #<msg_nopfx
        ldy #>msg_nopfx
        jmp puts

; --- MLI parameter lists ----------------------------------------
getprefix_p:
        .byte 1
        .addr pathbuf
open_p: .byte 3
        .addr pathbuf
        .addr IOBUF
        .byte 0                 ; ref_num returned here
read_p: .byte 4
        .byte 0                 ; ref_num
        .addr DATABUF
        .word 512
        .word 0                 ; bytes transferred
close_p:
        .byte 1
        .byte 0

msg_err:   .byte "I/O ERROR $",0
msg_nopfx: .byte "NO PREFIX SET",13,0
msg_nofile: .byte "NO FILE",13,0

; --- TYPE name: display a text file ------------------------------
cmd_type:
        jsr getname
        bcs @go
        jmp usage
@go:    MLICALL $C8, open_p
        bcc @opened
        jmp mlierr
@opened:
        lda open_p+5
        sta read_p+1
        sta close_p+1
@blk:   MLICALL $CA, read_p
        bcs @done               ; EOF or error
        lda read_p+6
        sta val
        lda read_p+7
        sta val+1
        lda #<DATABUF
        sta addr
        lda #>DATABUF
        sta addr+1
@ch:    lda val
        ora val+1
        beq @blk
        ldy #0
        lda (addr),y
        cmp #$1A                ; CP/M end-of-file mark
        beq @done
        jsr putc
        inc addr
        bne @n1
        inc addr+1
@n1:    lda val
        bne @n2
        dec val+1
@n2:    dec val
        lda KBD                 ; any key stops the listing
        bpl @ch
        bit $C010               ; clear the strobe
@done:  MLICALL $CC, close_p
        rts

; --- ERA name: delete a file -------------------------------------
cmd_era:
        jsr getname
        bcs @go
        jmp usage
@go:    MLICALL $C1, destroy_p
        bcc @ok
        jmp mlierr
@ok:    rts

; --- REN new=old: rename a file ----------------------------------
cmd_ren:
        lda #<PATH2
        sta addr
        lda #>PATH2
        sta addr+1
        ldx argx
        jsr copyname            ; new name
        bcc @bad
        lda LINE,x
        cmp #'='
        bne @bad
        inx
        lda #<pathbuf
        sta addr
        lda #>pathbuf
        sta addr+1
        jsr copyname            ; old name
        bcc @bad
        MLICALL $C2, rename_p
        bcc @ok
        jmp mlierr
@ok:    rts
@bad:   jmp usage

destroy_p:
        .byte 1
        .addr pathbuf
rename_p:
        .byte 2
        .addr pathbuf
        .addr PATH2
