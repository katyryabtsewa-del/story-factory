---
name: make-cover
description: Write Google Flow prompts for the episode cover, then turn the owner's Flow images into three finished cover variants with title text. Use for every episode.
---
# Обложка

Правила: `channel/titles-and-covers.md`.

**Источник картинок (решение владельца, ноябрь 2026: пока оставляем как есть):**
- **Higgsfield — по умолчанию, в том числе ночью:** `generate_image_batch`, модель `gpt_image_2_6` (≈0,25 кредита за картинку), 2 сцены × 2 картинки ≈ 1 кредит; **не больше 10 кредитов на эпизод**. Перед первой генерацией в разговоре — `get_preferences`. Готовые `result_url` скачай `curl` в `cover/flow/` (хост картинок разрешён в среде).
- **Google Flow** — по просьбе владельца: если в локальной сессии есть Chrome, скилл `flow-images`; иначе владелец генерирует сама по промптам из `prompt.md`.

**Часть 1 — промпты.** Создай `episodes/EXXX/cover/prompt.md`:
- 2 разные сцены по шаблону из `titles-and-covers.md` (внешность героини и злодеев — строго из `bible.md`), у каждой указана свободная сторона для текста;
- 3 варианта текста на обложку: 40–50 слов от первого лица, пересказ завязки, 1–2 жёлтые выделенные фразы, обрыв на «...»; только факты из истории.
**Картинки внутри видео (смена кадров) — по решению владельца, сейчас ВЫКЛЮЧЕНО.** Если владелец включит: добавь в `prompt.md` 5 сцен (`cover/scenes/s01.png … s05.png`, без текста, 16:9, та же героиня и стиль, по одной на 1–2 главы; ≈+1,25 кредита в Higgsfield) и собери видео `tools/render_scenes.py`.

**Часть 2 — готовые обложки** (когда картинки появились):
`.venv/bin/python tools/cover_panel.py episodes/EXXX/cover/flow/IMG.png episodes/EXXX/cover/cover_A.png "текст [[жёлтый]] текст..."` (стиль конкурентов — см. `channel/titles-and-covers.md`; `--flip`, если героиня слева)
Сделай 3 варианта (A, B, C): разные картинки и/или тексты. Посмотри каждую обложку (Read) — лица не закрыты текстом, текст читается на маленьком размере.
