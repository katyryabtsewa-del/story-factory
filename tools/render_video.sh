#!/usr/bin/env bash
# Build the episode video: cover image with a slow, seamless zoom loop + narration.
# Encodes only a 40-second loop, then repeats it for the whole audio (fast even for 90 minutes).
# usage: render_video.sh IMAGE AUDIO OUT.mp4
set -euo pipefail
IMG=$1; AUDIO=$2; OUT=$3
TMP=$(mktemp -d)
FPS=24; HALF=20; FRAMES=$((FPS * HALF))
ffmpeg -loglevel error -y -loop 1 -i "$IMG" -t $HALF \
  -vf "scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='1+0.05*on/$FRAMES':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=$FRAMES:s=1920x1080:fps=$FPS" \
  -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -g $((FPS * 4)) "$TMP/in.mp4"
ffmpeg -loglevel error -y -i "$TMP/in.mp4" -vf reverse -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -g $((FPS * 4)) "$TMP/out.mp4"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$AUDIO")
printf "file '%s'\nfile '%s'\n" "$TMP/in.mp4" "$TMP/out.mp4" > "$TMP/pair.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$TMP/pair.txt" -c copy "$TMP/loop.mp4"
# repeat the 40-second loop enough times to cover the audio, then cut exactly to the audio length
N=$(python3 -c "import math; print(math.ceil($DUR / $((HALF * 2))) + 1)")
for i in $(seq 1 "$N"); do echo "file '$TMP/loop.mp4'"; done > "$TMP/list.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$TMP/list.txt" -i "$AUDIO" -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 160k -t "$DUR" -movflags +faststart "$OUT"
rm -rf "$TMP"
echo "video saved: $OUT"
