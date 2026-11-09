#!/usr/bin/env python3
"""Build an episode video whose picture changes at chapter boundaries.

usage: render_scenes.py SCENES_DIR AUDIO.mp3 CHAPTERS.json OUT.mp4 [--half 20]

SCENES_DIR holds 2-8 images (png/jpg), taken in name order (s01.png, s02.png, ...).
Each picture gets a slow, seamless zoom loop (like render_video.sh) with a different
direction (center / left / right), and the pictures are spread over the audio so
that changes happen on chapter starts. The first picture covers chapter 1 and so on.
Requires ffmpeg/ffprobe. 1280x720, 24 fps.
"""
import glob, json, math, os, subprocess, sys, tempfile

FPS = 24


def run(cmd):
    subprocess.run(cmd, check=True)


def probe_duration(path):
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path])
    return float(out.decode().strip())


def scene_boundaries(starts, n, total):
    """Pick n+1 boundaries (first 0, last total) snapped to chapter starts."""
    if len(starts) >= n:
        idx = [round(k * len(starts) / n) for k in range(n)]
        b = [starts[i] if i < len(starts) else total for i in idx]
        b[0] = 0.0
    else:  # fewer chapters than pictures: split evenly
        b = [total * k / n for k in range(n)]
    return b + [total]


X_EXPR = {
    0: "iw/2-(iw/zoom/2)",        # centre
    1: "iw*0.33-(iw/zoom/2)",     # drift to the left third
    2: "iw*0.67-(iw/zoom/2)",     # drift to the right third
}


def make_loop(img, k, half, tmp):
    frames = FPS * half
    x = X_EXPR[k % 3]
    vf = (f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,"
          f"zoompan=z='1+0.05*on/{frames}':x='{x}':y='ih/2-(ih/zoom/2)':d={frames}:s=1280x720:fps={FPS}")
    a, b = f"{tmp}/a{k}.mp4", f"{tmp}/b{k}.mp4"
    enc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", "30", "-pix_fmt", "yuv420p", "-g", str(FPS)]
    run(["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-i", img, "-t", str(half), "-vf", vf, *enc, a])
    run(["ffmpeg", "-loglevel", "error", "-y", "-i", a, "-vf", "reverse", *enc, b])
    pair = f"{tmp}/pair{k}.txt"
    open(pair, "w").write(f"file '{a}'\nfile '{b}'\n")
    loop = f"{tmp}/loop{k}.mp4"
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", pair, "-c", "copy", loop])
    return loop


def make_scene(loop, k, seconds, half, tmp):
    n = math.ceil(seconds / (2 * half)) + 1
    lst = f"{tmp}/list{k}.txt"
    open(lst, "w").write("".join(f"file '{loop}'\n" for _ in range(n)))
    out = f"{tmp}/scene{k}.mp4"
    run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", "-t", f"{seconds:.3f}", out])
    return out


def main():
    args = [a for a in sys.argv[1:]]
    half = 20
    if "--half" in args:
        i = args.index("--half")
        half = int(args[i + 1])
        del args[i:i + 2]
    if len(args) != 4:
        sys.exit(__doc__)
    scenes_dir, audio, chapters, out = args
    imgs = sorted(p for p in glob.glob(os.path.join(scenes_dir, "*")) if p.lower().endswith((".png", ".jpg", ".jpeg")))
    if not imgs:
        sys.exit(f"no images in {scenes_dir}")
    total = probe_duration(audio)
    starts = [c["start"] for c in json.load(open(chapters))]
    bounds = scene_boundaries(starts, len(imgs), total)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        scenes = []
        for k, img in enumerate(imgs):
            secs = bounds[k + 1] - bounds[k]
            print(f"scene {k + 1}/{len(imgs)}: {os.path.basename(img)} {bounds[k]:.0f}s-{bounds[k + 1]:.0f}s", flush=True)
            loop = make_loop(img, k, half, tmp)
            scenes.append(make_scene(loop, k, secs, half, tmp))
        lst = f"{tmp}/all.txt"
        open(lst, "w").write("".join(f"file '{s}'\n" for s in scenes))
        run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", audio,
             "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
             "-t", f"{total:.3f}", "-movflags", "+faststart", out])
    print(f"video saved: {out}")


if __name__ == "__main__":
    main()
