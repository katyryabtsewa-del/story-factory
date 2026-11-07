---
name: make-cover
description: Write Google Flow prompts for the episode cover, then turn the owner's Flow images into three finished cover variants with title text. Use for every episode.
---
# Обложка

Правила: `channel/titles-and-covers.md`.

**Часть 1 — промпты.** Создай `episodes/EXXX/cover/prompt.md`:
- 2 разные сцены по шаблону из `titles-and-covers.md` (внешность героини и злодеев — строго из `bible.md`), у каждой указана свободная сторона для текста;
- 3 варианта текста на обложку (2–5 слов, дополняют название, а не повторяют).
Отправь владельцу промпты и попроси: сгенерировать в Google Flow по 2 картинки на сцену и загрузить лучшие в `episodes/EXXX/cover/flow/`.

**Часть 2 — готовые обложки** (когда картинки появились):
`.venv/bin/python tools/cover_text.py episodes/EXXX/cover/flow/IMG.png episodes/EXXX/cover/cover_A.png "LINE ONE|LINE TWO" --side left --color yellow`
Сделай 3 варианта (A, B, C): разные картинки и/или тексты. Посмотри каждую обложку (Read) — лица не закрыты текстом, текст читается на маленьком размере.
