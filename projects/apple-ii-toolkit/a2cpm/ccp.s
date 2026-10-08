; ---------------------------------------------------------------
; ccp.s - console command processor ("A>" prompt)
; ---------------------------------------------------------------

ccp_loop:
        ldx #$FF
        txs
        lda #<prompt
        ldy #>prompt
        jsr puts
        lda #80
        sta CMDBUF              ; maximum line length
        lda #10                 ; BDOS read console buffer
        ldx #<CMDBUF
        ldy #>CMDBUF
        jsr bdos
        ldy CMDBUF+1
        lda #0
        sta LINE,y              ; terminate the line
        jsr parse
        jmp ccp_loop

; Uppercase A if it is a-z
fold:
        cmp #'a'
        bcc @r
        cmp #'z'+1
        bcs @r
        sbc #$1F                ; carry clear: subtracts $20
@r:     rts

; ---------------------------------------------------------------
; parse: find the command in the table and dispatch to it.
; Table entry: name (uppercase, 0-terminated), handler address.
; A handler gets argx = index of first argument in LINE.
; ---------------------------------------------------------------
parse:
        ldx #0
@skip:  lda LINE,x
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
@cmp:   lda LINE,x
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
@sp:    lda LINE,x              ; skip spaces before arguments
        cmp #' '
        bne @sd
        inx
        bne @sp
@sd:    stx argx
        jmp (ptr)               ; handler's RTS returns to ccp_loop
@unknown:
        jmp unknown

; Not found anywhere: CP/M prints the word followed by '?'
unknown_msg:
        ldx cmdidx
@l:     lda LINE,x
        beq @q
        cmp #' '
        beq @q
        jsr fold
        jsr putc
        inx
        bne @l
@q:     lda #'?'
        jsr putc
        lda #13
        jmp putc

; ---------------------------------------------------------------
; parsehex: parse hex number at LINE,X into val.
; Returns carry clear on success (X advanced), set if no digits.
; ---------------------------------------------------------------
parsehex:
@sp:    lda LINE,x
        cmp #' '
        bne @go
        inx
        bne @sp
@go:    lda #0
        sta val
        sta val+1
        sta cnt
@dig:   lda LINE,x
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
; Built-in commands
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

; DUMP aaaa - hex dump 64 bytes
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
        lda #':'
        jsr putc
        ldy #0
@byte:  lda #' '
        jsr putc
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

; MEM - show where the program and its work areas live
cmd_mem:
        lda #<msg_mem
        ldy #>msg_mem
        jmp puts

; EXIT - return to ProDOS
cmd_exit:
        jsr MLI
        .byte $65               ; QUIT
        .word quitparms
        rts

quitparms:
        .byte 4,0,0,0,0,0,0

; ---------------------------------------------------------------
; Command table (piece 2 adds DIR, TYPE, ERA, REN, SAVE here)
; ---------------------------------------------------------------
cmdtab:
        .asciiz "HELP"
        .word cmd_help
        .asciiz "VER"
        .word cmd_ver
        .asciiz "CLS"
        .word cmd_cls
        .asciiz "DUMP"
        .word cmd_dump
        .asciiz "DIR"
        .word cmd_dir
        .asciiz "TYPE"
        .word cmd_type
        .asciiz "ERA"
        .word cmd_era
        .asciiz "REN"
        .word cmd_ren
        .asciiz "SAVE"
        .word cmd_save
        .asciiz "MEM"
        .word cmd_mem
        .asciiz "EXIT"
        .word cmd_exit
        .byte 0                 ; end of table

prompt:  .byte 13,"A>",0
banner:  .byte "A2CPM 2.2 (6502 CLONE)",13,"TYPE HELP FOR COMMANDS",13,0
msg_use: .byte "BAD ARGUMENT",13,0
msg_mem: .byte "CCP/BDOS $2000  TPA $0800-$1FFF",13
         .byte "BDOS ENTRY JSR $03C0  WARM BOOT $03C3",13,0
msg_help:
        .byte "HELP        THIS LIST",13
        .byte "VER         SHOW VERSION",13
        .byte "CLS         CLEAR SCREEN",13
        .byte "DUMP AAAA   HEX DUMP 64 BYTES",13
        .byte "DIR         LIST FILES",13
        .byte "TYPE NAME   SHOW A TEXT FILE",13
        .byte "ERA NAME    DELETE A FILE",13
        .byte "REN NEW=OLD RENAME A FILE",13
        .byte "SAVE N NAME SAVE N PAGES OF TPA",13
        .byte "NAME        RUN NAME.COM AT $0800",13
        .byte "MEM         SHOW MEMORY MAP",13
        .byte "EXIT        EXIT TO PRODOS",13,0
