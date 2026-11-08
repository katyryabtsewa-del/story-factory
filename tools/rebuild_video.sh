#!/usr/bin/env bash
# Rebuild an episode's video from files stored in git (narration mp3 + background image).
# usage: rebuild_video.sh episodes/E001-will-read-early   -> writes <episode>/video/episode.mp4
set -euo pipefail
E=${1%/}
BG=$(ls "$E"/cover/flow/*.png "$E"/cover/background.png 2>/dev/null | head -1)
[ -f "$E/audio/episode.mp3" ] || { echo "no audio in git for $E"; exit 1; }
[ -n "$BG" ] || { echo "no background image in $E/cover"; exit 1; }
mkdir -p "$E/video"
"$(dirname "$0")/render_video.sh" "$BG" "$E/audio/episode.mp3" "$E/video/episode.mp4"
