---
name: render-video
description: Build the final episode video from the chosen cover and the narration. Use after narration and covers are ready.
---
# Видео

1. Картинка для видео — исходник из `cover/flow/` лучшей обложки (без текста), чтобы текст не висел 90 минут.
2. `mkdir -p episodes/EXXX/video && tools/render_video.sh episodes/EXXX/cover/flow/IMG.png episodes/EXXX/audio/episode.mp3 episodes/EXXX/video/episode.mp4`
3. Проверь `ffprobe`: длительность совпадает с аудио, 1920×1080, звук есть.
