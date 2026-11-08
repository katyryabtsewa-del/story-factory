# Названия и обложки

## Название (до 100 символов, лучше 70–95)
Формула: **первое лицо + конкретная сцена унижения + намёк на расплату**, часто два предложения.
- My Daughter-in-Law Banned Me From Christmas. Three Days Later, She Found Out Who Owns Her Building.
- At My 70th Birthday, My Son Handed Me a Nursing Home Brochure. He Didn't Know I'd Sold the House.
- My Stepdaughter Changed the Locks During My Husband's Funeral. She Forgot About the Safe Deposit Box.
Правила: конкретика (кто, где, что сделал), без «A story that touches the soul», без «true story», без CAPS целиком (можно 1–2 слова).

## Обложка 1280×720 — стиль конкурентов (ОСНОВНОЙ, утверждён владельцем)
Слева тёмная панель (половина кадра) с **крупным текстом на 40–50 слов**: пересказ завязки от первого лица, белый текст с жёлтыми выделениями ключевых фраз, обрыв на «...» (крючок). Справа лицо героини. Инструмент: `tools/cover_panel.py BASE.png OUT.png "текст [[жёлтый]] текст..." [--flip]` (флаг `--flip`, если героиня на картинке слева). Текст — только то, что реально есть в истории, без выдумок. Картинки в Flow/Higgsfield: героиня крупно **справа**, улыбка или спокойный взгляд, без текста на картинке.
Старый стиль (короткая надпись 2–5 слов, `tools/cover_text.py`) владельцу не понравился: «выглядит ужасно, не цепляет».

## Обложка 1280×720 — старый стиль (не использовать)
- Фотореалистичная сцена: героиня 60–72 лет крупно, спокойное «знающее» лицо или сдержанные слёзы; злодей(и) на заднем плане — самодовольные, растерянные или в шоке.
- Обстановка из сюжета: кухня, крыльцо, праздничный стол, офис адвоката, церковь.
- Тёплый свет, высокая контрастность, лица крупно — обложку смотрят на телефоне и TV.
- **Текст добавляем сами** (`tools/cover_text.py`): 2–5 слов, 1–2 строки, жёлтый или белый с чёрной обводкой, на свободной стороне кадра. Текст не повторяет название, а дополняет: «HE FORGOT ONE THING», «SHE OWNS THE BUILDING».
- В Flow просить **без текста на картинке** и оставить свободное место слева или справа.

## Шаблон промпта для Google Flow
```
Photorealistic cinematic still, 16:9. [SCENE: e.g. a festive dinner table in a warm suburban American kitchen].
In the foreground on the [right] side: a [68]-year-old American woman with [silver bob haircut, cardigan, reading glasses on a chain],
calm knowing expression, slight smile, looking directly at the camera.
In the background, slightly out of focus: [her son in his forties and his wife], [smug / shocked] expressions.
Warm golden evening light, shallow depth of field, high contrast, rich colors, sharp faces.
Empty space on the [left] third of the frame for a title. No text, no letters, no watermark.
```
Делать 3–4 картинки, выбрать 2–3 лучших → три варианта обложки для теста YouTube «Test & Compare».
