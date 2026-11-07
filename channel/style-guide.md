# Стиль текста (пишем для голоса, а не для глаз)

## Как голос читает лучше всего (проверено на образцах)
- Полные, нормальные предложения разной длины. Голос сам делает естественные паузы на точках и запятых.
- **Не** рубить текст на цепочки обрывков («He did it over coffee. In my own kitchen.») — звучит рвано.
- **Не** использовать многоточия «...» и частые тире «—» для пауз — голос делает странные паузы. Вместо тире — запятая или новое предложение.
- Абзацы по 3–6 предложений. Пустая строка между абзацами.

## Язык
- Живой американский английский, от первого лица, прошедшее время.
- Сокращения умеренно и естественно: I'd, didn't, that's — но не в каждом предложении.
- Голос один на всех персонажей, поэтому в диалоге **всегда ясно, кто говорит**: «"Mom," he said, "...".». Реплики короткие.
- 5–8 именованных персонажей максимум, имена начинаются с разных букв (Linda, Mark, Jessica, Walter…). Злодея называть по имени чаще, чем «he».

## Технические правила для озвучки
- Числа и даты словами: «sixty-eight», «nineteen seventy-nine», «four hundred thousand dollars». Никаких «$», «%», «&», «#».
- Без аббревиатур, кроме Mr., Mrs., Ms. Писать «Doctor Patel», «Saint Louis», «Avenue».
- Без CAPS, без эмодзи, без ремарок в скобках, без заголовков внутри текста главы.
- Первая строка файла главы — `# Chapter title` (не озвучивается, идёт в таймкоды).

## Запрещённые штампы (ИИ-клише) — проверяются `tools/lint_script.py`
little did I know · a testament to · tapestry · in that moment · I let out a breath I didn't know I was holding · the silence was deafening · sent shivers down my spine · every fiber of my being · a wave of (relief/anger…) washed over · I couldn't help but · palpable · delve · navigate (в переносном смысле) · journey (в переносном смысле) · it's worth noting · a mix of · the weight of (his words…) · unspoken · her eyes sparkled · my heart pounded in my chest · time stood still · and just like that · little did they know.
Любая «фирменная» фраза — не чаще одного раза за эпизод.
