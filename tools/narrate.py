"""Narrate an episode with the approved channel voice (Kokoro, voice B).

Each chapter file: first line '# Chapter title' (not narrated), then paragraphs.
The voice was approved as a continuous take, so text is NEVER split into single
sentences: whole paragraphs are grouped into ~1500-character blocks, each block is
read in one call. Writes OUT.wav and OUT.chapters.json (chapter start times).

usage: narrate.py OUT.wav CH01.txt [CH02.txt ...]
"""
import sys, json, pathlib
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODEL = ROOT / "models" / "kokoro"
VOICE_MIX = [("af_sarah", 0.5), ("af_nicole", 0.5)]   # approved voice B — do not change
SPEED = 0.9
BLOCK_CHARS = 1500
BLOCK_PAUSE = 0.35     # seconds between blocks inside a chapter
CHAPTER_PAUSE = 1.6    # seconds between chapters
SR = 24000

def read_chapter(path):
    lines = pathlib.Path(path).read_text().strip().splitlines()
    title = lines[0][2:].strip() if lines and lines[0].startswith("# ") else pathlib.Path(path).stem
    body = "\n".join(lines[1:] if lines and lines[0].startswith("# ") else lines)
    paragraphs = [" ".join(p.split()) for p in body.split("\n\n") if p.strip()]
    return title, paragraphs

def blocks_of(paragraphs):
    blocks, cur = [], ""
    for p in paragraphs:
        if cur and len(cur) + len(p) > BLOCK_CHARS:
            blocks.append(cur); cur = p
        else:
            cur = f"{cur} {p}".strip()
    return blocks + ([cur] if cur else [])

def main():
    out_path, chapter_files = sys.argv[1], sys.argv[2:]
    k = Kokoro(str(MODEL / "kokoro-v1.0.onnx"), str(MODEL / "voices-v1.0.bin"))
    style = sum(k.get_voice_style(v) * w for v, w in VOICE_MIX)
    audio, chapters, t = [], [], 0.0
    for ci, path in enumerate(chapter_files):
        title, paragraphs = read_chapter(path)
        chapters.append({"title": title, "start": round(t, 2)})
        for b in blocks_of(paragraphs):
            samples, _ = k.create(b, voice=style, speed=SPEED, lang="en-us")
            gap = np.zeros(int(BLOCK_PAUSE * SR), np.float32)
            audio += [samples.astype(np.float32), gap]
            t += (len(samples) + len(gap)) / SR
        if ci < len(chapter_files) - 1:
            gap = np.zeros(int(CHAPTER_PAUSE * SR), np.float32)
            audio.append(gap); t += len(gap) / SR
        print(f"chapter {ci + 1}/{len(chapter_files)} done: {title}", flush=True)
    sf.write(out_path, np.concatenate(audio), SR)
    json.dump(chapters, open(out_path.rsplit(".", 1)[0] + ".chapters.json", "w"), indent=1)
    print(f"saved {out_path}: {t / 60:.1f} min, {len(chapters)} chapters")

if __name__ == "__main__":
    main()
