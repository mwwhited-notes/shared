AS = ca65
LD = ld65
AC = java -jar AppleCommander.jar

all: shell.bin

shell.o: shell.s
	$(AS) -o shell.o -l shell.lst shell.s

shell.bin: shell.o a2shell.cfg
	$(LD) -C a2shell.cfg -o shell.bin shell.o

# Put the shell on a ProDOS disk image that already contains
# PRODOS (the boot file). ProDOS runs the first *.SYSTEM file it finds.
disk: shell.bin
	$(AC) -d shell.po SHELL.SYSTEM || true
	$(AC) -p shell.po SHELL.SYSTEM sys 0x2000 < shell.bin

clean:
	rm -f shell.o shell.lst shell.bin

.PHONY: all disk clean
