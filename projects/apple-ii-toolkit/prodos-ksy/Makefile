# Needs the Kaitai Struct compiler (https://kaitai.io) and: pip install kaitaistruct pyyaml
KSC ?= kaitai-struct-compiler

build: prodos_volume.ksy prodos_2img.ksy
	$(KSC) -t python --outdir build prodos_volume.ksy prodos_2img.ksy

# No JVM compiler? Use the npm build of the compiler (needs Node.js).
build-js: prodos_volume.ksy prodos_2img.ksy
	cd tools && npm install --no-audit --no-fund
	node tools/ksc.js python build prodos_volume.ksy
	node tools/ksc.js python build prodos_2img.ksy

test: build
	python3 make_test_image.py
	python3 test_ksy.py

test-js: build-js
	python3 make_test_image.py
	python3 test_ksy.py

# Rebuild the diagram page from the .ksy files
diagram:
	python3 build_diagram.py

clean:
	rm -rf build test.po test.2mg __pycache__ tools/node_modules

.PHONY: build build-js test test-js diagram clean
