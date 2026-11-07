"""Transcribe narration back to text (QC). usage: qc_transcribe.py AUDIO OUT.txt"""
import os, sys, subprocess
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
import numpy as np
from faster_whisper import WhisperModel

pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", sys.argv[1], "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                     capture_output=True, check=True).stdout
audio = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
model = WhisperModel("small.en", device="cpu", compute_type="int8")
segments, _ = model.transcribe(audio, beam_size=1)
open(sys.argv[2], "w").write(" ".join(s.text.strip() for s in segments) + "\n")
print("transcript saved", sys.argv[2])
