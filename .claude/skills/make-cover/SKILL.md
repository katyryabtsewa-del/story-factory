---
name: make-cover
description: Write Google Flow prompts for the episode cover, then turn the owner's Flow images into three finished cover variants with title text. Use for every episode.
---
# Обложка

Правила: `channel/titles-and-covers.md`.

**Два варианта источника картинок:**
- **Google Flow (бесплатно, руками владельца)** — по умолчанию днём.
- **Higgsfield (ночью или по просьбе владельца)** — `generate_image_batch`, модель `gpt_image_2_6` (≈0,25 кредита за картинку), 2 сцены × 2 картинки; **не больше 10 кредитов на эпизод**. Перед первой генерацией в разговоре — `get_preferences`. Готовые `result_url` скачай `curl` в `cover/flow/` (хост картинок разрешён в среде).

**Часть 1 — промпты.** Создай `episodes/EXXX/cover/prompt.md`:
- 2 разные сцены по шаблону из `titles-and-covers.md` (внешность героини и злодеев — строго из `bible.md`), у каждой указана свободная сторона для текста;
- 3 варианта текста на обложку: 40–50 слов от первого лица, пересказ завязки, 1–2 жёлтые выделенные фразы, обрыв на «...»; только факты из истории.
Отправь владельцу промпты и попроси: сгенерировать в Google Flow по 2 картинки на сцену и загрузить лучшие в `episodes/EXXX/cover/flow/`.

**Часть 2 — готовые обложки** (когда картинки появились):
`.venv/bin/python tools/cover_panel.py episodes/EXXX/cover/flow/IMG.png episodes/EXXX/cover/cover_A.png "текст [[жёлтый]] текст..."` (стиль конкурентов — см. `channel/titles-and-covers.md`; `--flip`, если героиня слева)
Сделай 3 варианта (A, B, C): разные картинки и/или тексты. Посмотри каждую обложку (Read) — лица не закрыты текстом, текст читается на маленьком размере.
