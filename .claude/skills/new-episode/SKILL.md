---
name: new-episode
description: Make a complete new episode for the channel, from idea to an upload-ready package, stopping at the owner's checkpoints. Use when the owner asks for a new episode, story or video.
---
# Новый эпизод: весь цикл

Веди владельца по шагам. Пиши ему по-русски, коротко. Контент — на английском.

0. Если нет `.venv/` или `models/kokoro/` — запусти `bash tools/setup.sh`.
1. **Идея.** Если в `ideas/backlog.md` нет свежих идей со статусом 💡 и оценкой ≥16 — выполни скилл `generate-ideas`. Покажи владельцу 3–5 лучших идей одной таблицей.
   **СТОП: владелец выбирает идею** (или просит поправить). Отметь её ✅.
2. Создай папку `episodes/EXXX-slug/` (следующий номер, slug из 3–5 слов названия) и `idea.md`.
3. Выполни `write-episode`, затем `edit-episode`.
4. Выполни `make-cover` до шага с промптами — отдай владельцу промпты для Google Flow.
   **СТОП: владелец загружает картинки из Flow** в `episodes/EXXX/cover/flow/`.
   Пока ждёшь — выполни `narrate-episode` (он не зависит от обложки).
5. Доделай `make-cover` (тексты на обложках), затем `render-video` и `publish-pack`.
6. Отправь владельцу видео, 3 обложки и `publish.md` (SendUserFile), в сообщении — что проверить и как загрузить.
   **СТОП: владелец смотрит и загружает.** После загрузки отметь идею 📺 в `ideas/backlog.md`.
7. Закоммить всё (кроме тяжёлых файлов — их отсекает .gitignore) и запушь.
