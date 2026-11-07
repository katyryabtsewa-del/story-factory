---
name: publish-pack
description: Prepare everything needed to upload the episode to YouTube — title, description with chapters, tags, pinned comment and an upload checklist. Use when the video is ready.
---
# Пакет для загрузки

Создай `episodes/EXXX/publish.md`:
1. **Название** — из `idea.md` (≤100 символов) + 2 запасных варианта.
2. **Описание** (английский): 2–3 предложения-крючка без спойлера развязки → вопрос к слушателю → таймкоды глав (`.venv/bin/python tools/chapters.py episodes/EXXX/audio/chapters.json`, первая строка обязательно `00:00`) → дисклеймер из `channel/brand.md` → 3–5 хэштегов (#familystories #revengestory #audiostory …).
3. **Теги** (до 500 символов): тематические, без имён конкурентов.
4. **Закреплённый комментарий** — вопрос по моральной дилемме истории.
5. **Чек-лист загрузки для владельца** (по-русски):
   - загрузить `video/episode.mp4`, вставить название, описание, теги;
   - Altered or synthetic content → **Yes**;
   - обложка: Test & Compare → загрузить `cover_A/B/C`;
   - аудитория: не для детей; язык видео — English;
   - конечная заставка + плейлист канала;
   - расписание: ближайший день 7–9 утра ET.
