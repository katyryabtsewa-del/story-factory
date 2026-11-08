---
name: write-episode
description: Write the full script of a chosen episode (story bible, outline, chapters) following the channel formula and style. Use after an idea is chosen.
---
# Сценарий эпизода

Вход: папка `episodes/EXXX-slug/` с `idea.md`.
Обязательно прочитай: `channel/story-formula.md`, `channel/style-guide.md`, `channel/audience.md`.

1. **Паспорт** `bible.md`: героиня (имя, возраст 60–72, город и штат, кем работала, муж), злодей(и), союзники; у каждого — возраст, отношение к героине, 2–3 черты, манера речи. Хронология с годами, все суммы денег, адреса, названия мест. Максимум 8 именованных персонажей, имена на разные буквы.
2. **План** `outline.md`: число глав по длине из `idea.md` (по умолчанию 60 минут = 8 глав, таблица в `story-formula.md`). Для каждой: название (2–5 слов, английский), 3–6 событий, чем кончается (крючок), целевой объём 1 100–1 200 слов. Проверь скелет из `story-formula.md`.
3. **Главы.** Пиши через агента `writer` партиями по 4 главы (60 минут — две партии: 1–4 и 5–8; 95 минут — три). Каждой партии передай пути к `bible.md`, `outline.md`, правилам канала и **полный текст последней написанной главы**. Файлы: `script/ch01.txt` … с первой строкой `# Chapter title`.
4. Прогони `.venv/bin/python tools/lint_script.py episodes/EXXX/script/ch*.txt`. Если итог вне диапазона слов для выбранной длины (`story-formula.md`) или есть ошибки — исправь (через `writer`) до чистого отчёта.
