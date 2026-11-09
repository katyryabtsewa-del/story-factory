---
name: flow-images
description: Generate the cover and in-video scene pictures for an episode in Google Flow (Nano Banana) through the owner's own Chrome, then build the three covers and the scene-changing video. Use in a LOCAL session (on the owner's computer, Claude in Chrome connected); never in the cloud night shift.
---
# Картинки в Google Flow через Chrome (локальная сессия)

**Правила владельца:** картинки только в Google Flow (Nano Banana, бесплатно). **Higgsfield не использовать.** Ничего не публиковать и не загружать на YouTube — только генерировать и скачивать картинки.

## 0. Подготовка (один раз в папке проекта)
1. Папка — это репозиторий `story-factory` (`git pull`, чтобы были последние эпизоды). Прочитай `CLAUDE.md`.
2. Нужны `python3` с Pillow (`pip install pillow`) и `ffmpeg`. Тяжёлую настройку голоса (`tools/setup.sh`) не запускай — она нужна только для озвучки.
3. Нужен Chrome с расширением Claude in Chrome (инструменты `mcp__claude-in-chrome__*`; прочитай скилл `anthropic-skills:chrome-browser`). Если инструментов Chrome нет — скажи владельцу и остановись, не подменяй.

## 1. Какой эпизод
Бери эпизод, который назвал владелец, иначе — самый новый в `episodes/`, где в `night-report.md` написано «ЖДУТ FLOW» или нет `cover/scenes/`. Прочитай его `idea.md`, `bible.md` (внешность героев — строго оттуда) и `cover/prompt.md`. Если в `prompt.md` нет 5 сцен для видео — напиши их сам по `outline.md`: по одной на 1–2 главы, разные места и моменты, без текста на картинке, 16:9, одна и та же героиня и стиль.

## 2. Генерация в Flow
1. `tabs_context_mcp`, затем **новая вкладка**: `https://labs.google/fx/tools/flow` (владелец уже вошла в Google). Если просит вход, оплату или согласие — остановись и попроси владельца сделать это самой.
2. Новый проект, тип — картинки, модель Nano Banana, формат 16:9. Если интерфейс изменился — ориентируйся по странице.
3. Для каждого промпта: вставь, сгенерируй, выбери лучший вариант, **посмотри результат** (лица не искажены, нет текста на картинке, героиня похожа на описание в `bible.md`). Плохой — перегенерируй (не больше 3 попыток на сцену).
4. Скачай картинки:
   - обложки (2 сцены × 2 варианта) → `episodes/EXXX/cover/flow/` (в git не хранится);
   - 5 картинок для видео → `episodes/EXXX/cover/scenes/s01.png … s05.png` (**в git хранится**; сжать до ≤1,5 МБ, если больше).
5. Закрой вкладки, которые открыла. Диалоги браузера (alert/confirm) не вызывай.

## 3. Сборка
1. Обложки: `python3 tools/cover_panel.py episodes/EXXX/cover/flow/IMG.png episodes/EXXX/cover/cover_A.png "текст [[жёлтый]] текст..."` для трёх вариантов A/B/C (тексты из `publish.md` / `prompt.md`; `--flip`, если героиня слева). Посмотри каждую (Read): лица не закрыты, текст читается.
2. Фон без текста для запасного рендера: `cp` лучшую сцену в `cover/background.png`.
3. Видео со сменой картинок (аудио `audio/episode.mp3` лежит в git):
   `python3 tools/render_scenes.py episodes/EXXX/cover/scenes episodes/EXXX/audio/episode.mp3 episodes/EXXX/audio/chapters.json episodes/EXXX/video/episode.mp4`
   Проверь `ffprobe`: длительность равна аудио, 1280×720.
4. Закоммить (`cover/*.png`, `cover/scenes/*`), `git push origin HEAD:main` (перед этим `git pull --rebase`). Видео (`.mp4`) в git не коммитится.
5. Покажи владельцу: три обложки и путь к `video/episode.mp4` (локальный файл на её компьютере). Напомни: «Altered or synthetic content → Yes» и что публикует она сама.
