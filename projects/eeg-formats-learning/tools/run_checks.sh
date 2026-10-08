#!/usr/bin/env bash
# Compile all ../ksy/*.ksy to Python, then parse small synthetic files with the generated parsers.
# Needs: node/npm, python3, and `pip install kaitaistruct`.
set -euo pipefail
cd "$(dirname "$0")"
npm install --no-audit --no-fund >/dev/null
OUT="$(mktemp -d)"
node check.js ../ksy "$OUT"
python3 roundtrip.py "$OUT"
rm -rf "$OUT"
