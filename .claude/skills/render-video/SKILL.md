---
name: render-video
description: Build the final episode video from the chosen cover and the narration. Use after narration and covers are ready.
---
# Видео

1. Картинка для видео — исходник из `cover/flow/` лучшей обложки (без текста), чтобы текст не висел 90 минут.
2. `mkdir -p episodes/EXXX/video && tools/render_video.sh episodes/EXXX/cover/flow/IMG.png episodes/EXXX/audio/episode.mp3 episodes/EXXX/video/episode.mp4`
3. Проверь `ffprobe`: длительность совпадает с аудио, 1920×1080, звук есть.

4. Фоновую картинку (без текста) сохрани как `cover/background.png` — она хранится в git. Тогда видео в любой момент собирается заново: `tools/rebuild_video.sh episodes/EXXX-slug`.

**Картинки, которые сменяются (по умолчанию, если есть `cover/scenes/`):**
`python3 tools/render_scenes.py episodes/EXXX/cover/scenes episodes/EXXX/audio/episode.mp3 episodes/EXXX/audio/chapters.json episodes/EXXX/video/episode.mp4`
Картинки (`s01.png`, `s02.png`, …) меняются на границах глав, у каждой свой медленный зум. Сцены лежат в git (как `cover/background.png`), поэтому видео всегда можно пересобрать. Если сцен нет — один фон, как выше (`render_video.sh`), и пометка «ФОН ВРЕМЕННЫЙ» в `night-report.md`.
