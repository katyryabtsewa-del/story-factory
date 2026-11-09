---
name: night-shift
description: Unattended nightly production run — take the next idea the owner queued and make a complete, upload-ready episode by morning. Used by the scheduled nightly task; also when the owner asks to "make the next episode without me".
---
# Ночная смена

Владелец спит. **Ничего не спрашивай** и не жди ответа: решения принимай сам по правилам канала. Не меняй сетевые настройки среды и разрешения. Пиши владельцу по-русски, коротко.

0. **Подготовка.** Если репозитория нет в рабочей папке — его нет в сессии: запиши это в ответ и остановись. `git pull`. Если нет `.venv/` или `models/kokoro/` — `bash tools/setup.sh`.
1. **Какую историю делать.** В `ideas/backlog.md` возьми идею со статусом ✅ с наименьшим номером, для которой ещё нет папки в `episodes/` (сверь по `episodes/*/idea.md`). Длина — из столбца/пометки идеи, иначе 60 минут.
   - Если такой идеи нет: выполни `generate-ideas` (если свежих 💡 с оценкой ≥16 меньше пяти), закоммить, и напиши владельцу: «Очередь пуста — выберите 3–7 идей (номера) и я сделаю их в следующие ночи». Остановись.
2. Отметь идею 🎬, создай `episodes/EXXX-slug/` и `idea.md` (с `Length: … min`). Номер EXXX — следующий после максимального в `episodes/` **на `main`**. **Сразу запушь отметку 🎬 и папку с `idea.md` в `main`** (`git fetch origin main && git rebase origin/main && git push origin HEAD:main`): так следующая смена и любой другой чат видят, что идея занята.
3. `write-episode` → `edit-episode`. Коммить и пушь после каждого шага (если сессию прервёт лимит, работа не пропадёт). Пушь и в свою ветку, и в `main` (та же команда `git push origin HEAD:main` после rebase): эпизоды должны лежать в `main`, а не только в ветке сессии.
4. `narrate-episode` (в фоне), параллельно обложки:
   - `make-cover` в варианте **Higgsfield**: `generate_image_batch`, модель `gpt_image_2_6`, 2 сцены × 2 картинки (≈1 кредит). **Жёсткий потолок — 10 кредитов на эпизод.** Скачай картинки в `cover/flow/`, посмотри их, сделай `cover_A/B/C`.
5. `render-video` → `publish-pack`.
6. Если какой-то шаг не удался — запиши причину в `episodes/EXXX/night-report.md` и сделай всё, что возможно без него.
7. Закоммить и запушь в свою ветку **и в `main`** (в `main` идут только файлы эпизода и `ideas/backlog.md`; в backlog статус идеи оставь 🎬 до загрузки владельцем). Отправь владельцу (SendUserFile) `video/episode.mp4`, три обложки и `publish.md`. Итоговое сообщение: название, длина, что проверить, сколько кредитов Higgsfield ушло.
