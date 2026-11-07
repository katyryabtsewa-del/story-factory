---
name: edit-episode
description: Independent editorial review of an episode script for continuity, pacing, clichés and voice-readiness, then apply fixes. Use after write-episode, before narration.
---
# Редактура

1. Вызови агента `editor` (у него чистая память — это важно): передай пути к `bible.md`, `outline.md`, `script/`, `channel/style-guide.md`, `channel/story-formula.md`, предыдущим `episodes/*/idea.md`. Он пишет `review.md`.
2. Исправь все пункты «обязательно» в `review.md` (сам или через `writer`), пункты «желательно» — по здравому смыслу.
3. Снова `tools/lint_script.py` — отчёт должен быть чистым. Допиши итог в конец `review.md`.
