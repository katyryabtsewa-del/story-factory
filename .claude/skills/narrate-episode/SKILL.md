---
name: narrate-episode
description: Voice the episode with the approved channel voice, master the audio and verify it against the script. Use after the script is edited.
---
# Озвучка

Голос утверждён владельцем: `channel/voice.md`. Параметры в `tools/narrate.py` и `tools/master.sh` не менять.

1. `mkdir -p episodes/EXXX/audio`
2. `.venv/bin/python tools/narrate.py episodes/EXXX/audio/raw.wav episodes/EXXX/script/ch*.txt` (~20–25 минут на 90 минут аудио; запускать в фоне).
3. `tools/master.sh episodes/EXXX/audio/raw.wav episodes/EXXX/audio/episode.mp3`, затем скопируй `raw.chapters.json` в `audio/chapters.json`.
4. Проверка: `.venv/bin/python tools/qc_transcribe.py episodes/EXXX/audio/episode.mp3 episodes/EXXX/audio/transcript.txt`, затем `.venv/bin/python tools/qc_compare.py episodes/EXXX/audio/transcript.txt episodes/EXXX/script/ch*.txt > episodes/EXXX/qc.md`.
5. Если в `qc.md` есть пропуски или искажения — поправь текст в этих местах (обычно странное слово, имя или число) и переозвучь только эти главы, затем собери заново. Сходство должно быть ≥97%.
6. Удали `raw.wav` после успешной сборки.
