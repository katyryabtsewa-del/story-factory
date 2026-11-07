#!/usr/bin/env bash
# One-time setup on a fresh machine: Python env, voice model, cover font. Safe to re-run.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=$(command -v python3.12 || command -v python3.11 || command -v python3)
[ -x .venv/bin/python ] || "$PY" -m venv .venv
.venv/bin/pip install -q --upgrade pip
.venv/bin/pip install -q kokoro-onnx soundfile numpy faster-whisper yt-dlp pillow
mkdir -p models/kokoro assets/fonts
BASE=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "models/kokoro/$f" ] || curl -sSL -o "models/kokoro/$f" "$BASE/$f"
done
# Anton (SIL Open Font License) for cover text; falls back to DejaVu Sans Bold if unavailable
[ -s assets/fonts/Anton-Regular.ttf ] || curl -sSLf -o assets/fonts/Anton-Regular.ttf \
  https://github.com/google/fonts/raw/main/ofl/anton/Anton-Regular.ttf || echo "Anton font not downloaded, using fallback"
command -v ffmpeg >/dev/null || echo "WARNING: ffmpeg is not installed (apt-get install -y ffmpeg)"
echo "setup done"
