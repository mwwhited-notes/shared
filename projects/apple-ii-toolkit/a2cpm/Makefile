AS = ca65
LD = ld65
AC = java -jar AppleCommander.jar
SRC = cpm.s bdos.s ccp.s files.s transient.s

all: cpm.bin

cpm.o: $(SRC)
	$(AS) -o cpm.o -l cpm.lst cpm.s

cpm.bin: cpm.o a2cpm.cfg
	$(LD) -C a2cpm.cfg -o cpm.bin cpm.o

# Copy onto a bootable ProDOS image (shell.po) as CPM.SYSTEM.
disk: cpm.bin
	$(AC) -d cpm.po CPM.SYSTEM || true
	$(AC) -p cpm.po CPM.SYSTEM sys 0x2000 < cpm.bin

# Run the emulator test (needs: pip install py65)
test: cpm.bin
	python3 -I test_harness.py cpm.bin test_script.txt

clean:
	rm -f cpm.o cpm.lst cpm.bin

.PHONY: all disk test clean
