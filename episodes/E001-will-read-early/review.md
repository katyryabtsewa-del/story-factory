# E001 — отчёт редактора

Прочитано: `idea.md`, `bible.md`, `outline.md`, главы `ch01`–`ch12`, `channel/style-guide.md`, `story-formula.md`, `audience.md`, `brand.md`, `CLAUDE.md`. Это первый эпизод, предыдущих `idea.md` нет, поэтому проверку на сходство с прошлыми эпизодами пропускаю. Номера строк ниже — строки файла главы (строка 1 — заголовок `# ...`).

**Линтер** (`.venv/bin/python tools/lint_script.py episodes/E001-will-read-early/script/ch*.txt`):

```
Total: 14815 words ≈ 95 min
ch01 1251 · ch02 1223 · ch03 1234 · ch04 1221 · ch05 1244 · ch06 1226
ch07 1242 · ch08 1240 · ch09 1240 · ch10 1240 · ch11 1238 · ch12 1216  — все "ok"
```
Штампов, многоточий, тире, цифр, символов, CAPS и абзацев длиннее 160 слов нет; повторов из пяти слов (три и более раз) нет. Но **14 815 слов — это больше потолка формулы (12 500–14 500)** примерно на 315 слов. Сокращение ch01 (см. «Желательно», п. 1) возвращает эпизод в норму.

**Что проверено вручную и в порядке.** Фраза траста в ch07 (строка 47) и ch10 (строка 15) совпадает с библией побайтно. Сходятся возрасты, все дни недели с 27 октября по 24 ноября, промежутки («four days after», «only three days before», «five days», «last Saturday»), суммы (sixty thousand, five thousand two hundred, fifty thousand, eighty-five thousand), счёт стикеров (26+11+4 = 41, в ch12 сняли сорок, один оставили) и кто что знает (Оливия не знает о доле до ch10, Томми не знает о схеме до ch10, Гарольд знает о папке Кевина с 10 ноября). Каждая глава со 2-й начинается с напоминания и кончается крючком. Провисаний дольше десяти минут нет. Расплата публичная, злодей попадает под последствия собственных поступков. Правила CLAUDE.md соблюдены: нет «true story», мата и натурализма; злодеи — конкретные люди. Кавычек внутри кавычек нет. Кроме линтера, я сделал: поиск повторов из четырёх слов, поиск реплик без указания говорящего, прогон трудных слов через фонемизатор Kokoro и тестовый синтез утверждённым голосом B (af_sarah 50% + af_nicole 50%, скорость 0.9).

## Обязательно исправить

1. **ch01, строка 9 (холодное открытие): обещание противоречит сцене расплаты.**
   «My lawyer read it aloud at my own kitchen table, between the turkey and the pie, and only one sentence in it mattered.»
   Проблема: в ch09 (строки 67–71) и ch10 (строка 3: «with three pies cut and the coffee poured») Гарольд читает после того, как пироги уже разрезаны. Первое, что слушатель узнаёт о финале, расходится с тем, что он потом услышит. К тому же «после пирога» — это и есть та минута, когда Бриттани собиралась дать Дайан подписать бумаги (ch08, строка 51).
   Исправление: «My lawyer read it aloud at my own kitchen table, over pie and coffee, and only one sentence in it mattered.»

2. **ch09, строка 43: неверное «his».**
   «Kevin and Brittany had come forty minutes late to Walter's memorial lunch. To hear his will, they came twenty minutes early.»
   Проблема: «his» по грамматике относится к Уолтеру. На слух получается, что они приехали слушать завещание Уолтера, хотя читают завещание (траст) Дайан. Ошибка стоит перед самой кульминацией.
   Исправление: «To hear my will read, they came twenty minutes early.»

3. **ch09, строка 11: логика перевёрнута.**
   «Tommy set out the chairs, counted us off on his fingers, and came up one short.» Следом (строка 13): «"Eight chairs," Tommy said. "Who's the extra?"»
   Проблема: «came up one short» значит «стульев не хватило», а через секунду Томми говорит о лишнем стуле.
   Исправление: «Tommy set out the chairs, counted us off on his fingers, and came out with one chair left over.»

4. **ch12, строки 13 и 25: лодка и долги Кевина появляются впервые только в эпилоге.**
   «In February Kevin sold the boat.» / «Eighty-five thousand dollars... The boat, the credit cards, and a bonus the dealership took back.»
   Проблема: «the boat» с определённым артиклем звучит как то, что слушатель уже знает, а о лодке до сих пор не было ни слова. Долги, главный мотив Кевина, ни разу не намечены в ch01–ch11. Поэтому одиннадцать глав Кевин мотивирован только жадностью и выглядит площе, а апрельская исповедь сообщает новые факты вместо того, чтобы закрывать посеянное. Заодно упущен случай показать, что Дайан-бухгалтер видит больше, чем говорит.
   Исправление: два зерна, около 40 слов.
   — ch01, строка 29, после «in a leased black car about the size of my kitchen»: «He had bought a boat that spring, too, and as far as I know it had been in the water twice.»
   — ch03, после строки 39 («Your father would have asked me first... He always did.»): «I had seen that look across my counter on men whose trucks were about to be repossessed. Whatever Kevin owed, he did not owe it to a car wash.»

5. **ch10, строки 27–39: на слух не связано, почему Кевин проиграл.**
   Фраза траста звучит на 1:30 главы: 44 слова юридического языка. Её простой пересказ («Dead on paper») был в ch07, примерно двадцать минут назад. Дальше идут две с половиной минуты улик, но никто не говорит вслух, что именно они и есть те «attempts», о которых говорит фраза. Простое объяснение («Died before me... you died before your mother») приходит только на 5:15. Очевидное возражение («это было до 3 ноября») за столом не снято: единственное действие Кевина после поправки, свежая доверенность в папке, упомянуто мимоходом («I believe Kevin has brought a fresh copy in that leather folder on the hutch»). Слушатель, который режет лук, может упустить механику.
   Исправление: после четвёртой улики (строка 39), перед «Kevin was on his feet» (строка 41), вставить абзац:
   «Harold took off his glasses. "A lawyer's letter threatening to take Diane before a judge," Harold said. "A false report to her doctor, so the judge would have something to read. And a power of attorney in a folder on that hutch, brought into this house today, three weeks after this sentence was signed. That is an attempt, Kevin. The sentence does not ask whether it worked."»
   Чтобы не набирать слов, можно сократить описание первой улики в строке 27.

6. **ch10: расплату делает адвокат, а не героиня; ружьё с сумочкой не стреляет.**
   Завязка: ch04, строка 43, «I folded that page into my purse next to my checkbook.»; ch08, строка 17, «I put the other in my purse, next to the printout of Brittany's phone call, so the two of them could keep each other company.» В ch10 (строки 25, 31, 39) оба документа достаёт из портфеля Гарольд.
   Проблема: в кульминации Дайан стучит по стакану, встаёт рядом с Оливией и говорит одну фразу Рэйчел. Все документы выкладывает юрист. Формула прямо требует: «Героиня не кричит — она достаёт документ». Деталь с сумочкой, выставленная дважды, пропадает зря.
   Исправление: улики № 2 и № 4 кладёт сама Дайан. Строка 31: «"Second," Harold said, and he looked at me. I opened my purse and laid the printout from my doctor's office on the tablecloth, the one I had carried since October.» Строка 39: «"And fourth," Harold said. I set my doctor's letter down beside the first page myself.» Дальше Гарольд пересказывает содержание, как сейчас. Его реплику «sharper than most forty-year-olds» не трогать: она остаётся его.

7. **ch08, строки 69 и 85; ch09, строка 31; ch10, строка 75: «Mr.» и «Mrs.» дают паузу посреди предложения.**
   «Kevin says Mr. Greene is coming to Thanksgiving» · «Mr. Greene would read some papers at Thanksgiving» · «before Mr. Greene gets here» · «"Her doctor writes that she is sharper than most forty-year-olds, Mrs. Whitaker," Harold said»
   Проблема: токенизатор Kokoro сохраняет точку («Mr. Greene» превращается в `mˈɪstɚ. ɡɹˈiːn`). На тесте утверждённым голосом фраза «Kevin says Mr. Greene is coming to Thanksgiving» получила лишнюю паузу 0,78 секунды сразу после «Mister»; в варианте «Mister Greene» её нет. В ch10 это лучшая реплика Гарольда в кульминации.
   Исправление: в тексте писать «Mister Greene» (3 раза) и «Missus Whitaker» (1 раз). Предлагаю поправить и `style-guide.md`: сейчас он разрешает «Mr., Mrs., Ms.»

8. **ch06, строка 29: «фирменная» фраза повторена (правило style-guide «не чаще одного раза за эпизод»).**
   «I could hear it in her bright voice, the one she saves for waiters.» Первый раз: ch01, строка 3, «the bright, sing-song voice she saves for waiters».
   Исправление (ch06): «I could hear her reading it out loud, the way she had read my house off that tablet.»

## Желательно

1. **ch01, строки 13–31: сцена в коридоре стоит на паузе 4 минуты 20 секунд (с 1:15 до 5:35).** Это главный риск удержания во всём эпизоде. После крючка идут примерно 670 слов знакомства: город, закусочная, стол, смерть Уолтера, Томми, Оливия, Рэйчел, Кевин и Бриттани. Каждый абзац хорош сам по себе, но нового вопроса нет, а сцена в коридоре заморожена, и к ней возвращаются только на строке 33 («So that was my family...»). Именно на пятой минуте фоновый слушатель уходит.
   Исправление: сжать строки 13–31 примерно до 300 слов и держать Дайан в коридоре, у скрипучей половицы. Строка 13 сокращается до имени, возраста, города и Blue Kettle. Из строки 15 оставить одно предложение про стол. Строку 17 (смерть Уолтера) оставить, но короче. Томми, Оливию, Рэйчел, Кевина с Бриттани дать по одному-два предложения: что Дайан видит и слышит из коридора. Сохранить факты, на которые потом ссылается текст: двадцать раскладных стульев из Saint Anne's (ch06, строка 35), «forty minutes late» (ch09, строка 43), «leased black car» (ch03, ch12), «the voice» Кевина (ch02, строка 63), «Mama Di» и то, что Дайан это прозвище терпеть не может. Заодно уйдёт превышение объёма.

2. **ch01, строки 3–9: огранить первые 60 секунд.**
   а) Реплика Бриттани, самая жестокая точка, звучит только на 0:30–0:39. Убрать из строки 3 «and the whole house smelled of baked ham and coffee» и «The den door was half open.» (дверь подразумевается), тогда реплика начнётся примерно на 0:24, а «She won't last five years» прозвучит около 0:30.
   б) «"What about Grandma's sapphire ring?"» (строка 7): на канале, где рассказчица сама бабушка, слушатель решит, что кольцо её собственное. Что оно принадлежало её матери, объяснено только на 5:35. Добавить после реплики: «That ring had been my mother's.»
   в) Обещание «only one sentence in it mattered» хорошее, но абстрактное. Добавить ставку, привязанную к Кевину: «My oldest son brought papers for me to sign after the pie. He took them home unsigned, along with a great deal less than he came for.»

3. **ch10, строки 63 и 71: ставка ни разу не названа в долларах.** «Over a million» из библии в тексте нет нигде. Звучит только «three-forty» за дом. Аудитория любит «квитанции», и «Your share... will go to Olivia» без суммы бьёт слабее.
   Исправление: ch01, строка 5, Бриттани: «...and the house alone is three-forty. With the diner money and Walter's insurance, we're over a million.» Ch10, строка 71: «You can't let a confused old woman hand a third of a million dollars of our money to a sixteen-year-old.» Бриттани не знает, что дом уходит Томми, поэтому её завышенная цифра логична.

4. **ch07, после строки 65: правдоподобие для тех, кто сам оформлял траст.** Слушатель 60+ спросит: траст отзывной, почему бы просто не вычеркнуть Кевина? Ответ в тексте подразумевается, но не произнесён.
   Исправление: «"You could simply cut him out, Diane," Harold said. "But this way, if Kevin loses anything, he'll have done it with his own hands."» Это ещё и тема эпизода.

5. **ch10, после строки 15 (по желанию): подготовить сцену с Томми в ch11.** Сейчас то, что дом уходит Томми, всплывает только ночью («the part Harold had not read aloud», ch11, строка 71). Одна фраза Гарольда создаёт маленький открытый вопрос: «There are other changes on page three, and Diane will tell the people they concern herself.»

6. **Повтор «for thirty-one years»: 12 раз** (ch01 ×2, ch03 ×2, ch04, ch06, ch08, ch09, ch11 ×2, ch12 ×2). Это уже тик. Оставить ch01, строка 13; ch04, строка 31; ch11, строка 27 (письмо Уолтера). В остальных местах убрать или заменить: ch01, строка 41, ch03, строка 19 («I kept the books at the Blue Kettle for thirty-one years.» → «I kept the Blue Kettle's books from the first day to the last.»), ch03, строка 47, ch06, строка 45, ch08, строка 11, ch09, строка 3, ch11, строка 5, ch12, строки 53 и 61 (два раза на последней странице).

7. **Оборот «the way...» 32 раза, из них 7 в ch09.** Переписать хотя бы три в ch09: строка 27 («the way you hold a purse on a city bus»), строка 51 («the way you pat a dog to tell it to stay»), строка 21 («the way he studies an engine») — сравнения оставить, сменить рамку («like a dog he'd told to stay»).

8. **ch09, строка 25: повтор хода «чуть не рассказала Томми».**
   «I nearly told him then. But dinner was five hours away, and I did not want him carrying it one minute longer than he had to.»
   Тот же ход и почти те же слова уже были в ch05, строки 73–81 («I did not want Tommy carrying any part of it»). Кроме того, Рэйчел трижды почти признаётся. Исправление: удалить строку 25. Реплика Томми «You'll tell me when you want to» закрывает сцену лучше.

9. **ch09, строка 63: «carve» шесть раз в четырёх предложениях, а «stood up to carve» повторяется как «carved standing up».**
   Исправление: «Then Kevin stood up to carve. For just a second his hand went to the back of his father's chair, as if he meant to pull it out. Tommy looked at him, and Kevin let go. He had watched his father carve for forty Thanksgivings, and he sawed at that bird until it came apart in rags. We ate it anyway. Gravy forgives a great deal.»

10. **ch12, строка 55: цепочка обрывков против style-guide.**
    «Grand Canyon. Four days. One pie. Two forks.» Фонемизатор ставит четыре точки, то есть четыре понижения интонации подряд; это ровно то «рвано», от которого предостерегает гайд, и на финальной ноте.
    Исправление: «I wrote just one line: Grand Canyon, four days, one pie, two forks.»

11. **ch12, строка 51: «this month» ни к чему не привязан.**
    «And at the start of this month, Olivia and I drove to the Grand Canyon.» Слушателю нигде не сказано, что Дайан рассказывает историю в июне.
    Исправление: «And at the start of June, just a few weeks ago, Olivia and I drove to the Grand Canyon.»

12. **ch09, строка 39: брат за рулём в девять лет.**
    «...that horn did to her exactly what it did when she was six and her big brother was waiting in the car.» Когда Рэйчел было шесть, Кевину было девять.
    Исправление: «...when she was sixteen and her big brother was waiting in the car to drive her to school.»

13. **ch11, строки 51 и 71: Томми сидит на крыльце в ноябрьский холод примерно с пяти вечера до ночи.**
    «Tommy went out to sit on the porch in the cold» → «Tommy came in off the porch with his ears red from the cold» (уже после того, как Гарольд ушёл, а все легли).
    Исправление: строка 51 — «Tommy went out to sit on the porch in the cold, and then found something to fix in the garage.»; строка 71 — «Tommy came in from the garage with his ears red from the cold.»

14. **ch09, строка 51: на слух непонятно, где теперь шампанское.**
    «Brittany moved my cranberry sauce to make room for her champagne.» Холодильник появляется только в строке 67 («Brittany glanced at the refrigerator»).
    Исправление: «Brittany opened my refrigerator and moved my cranberry sauce to make room for her champagne.»

15. **Бриттани однотонна.** Кевину даны долги, раскаяние и человеческий жест; у Бриттани только «Mama Di», таблицы и вспышка, а потом одно предложение про сестру. Чтобы она не стала картонной, хватит одного штриха, например ch12, строка 13: «Olivia said her mother had grown up in a rented trailer and had promised herself she would never be poor again. It did not excuse one sticker. It did explain a few of them.» Если принять, внести в библию.

16. **Две разные «сорок одна»:** 41 стикер (ch02, строка 57; ch12, строка 5 «forty colored dots... I left one») и 41 фотография (ch06, строка 53; ch07, строка 13; ch10, строка 35). На слух легко смешать. Достаточно поменять число фотографий, например на «thirty-eight», в трёх главах и в библии.

17. **Maple Grove Senior Living (ch03, строка 41 и далее): название обычное, такое заведение вполне может существовать.** А показано оно невыгодно: подливка из пакета, «The pie here is terrible». Правило 1 в CLAUDE.md. Перед публикацией проверить поиском; если такое заведение есть, заменить на явно выдуманное название (заодно в обложке и `publish.md`).

18. **ch02, строка 3: «For three weeks» подразумевает, что потом она заговорила.**
    «For three weeks after Walter's memorial lunch, I did not say one word to anybody about the spreadsheet...» Молчит она семь недель, до Гарольда 31 октября. Исправление: «For weeks after Walter's memorial lunch...»

19. **ch12, строка 57: объявление морали.** «I learned something that fall that I would like to pass along.» — эта фраза-вступление сдвигает финал к проповеди. Удалить; следующие три предложения держатся сами.

20. **Список для QC озвучки (текст не трогать, проверить на слух в `qc.md`):** «Olivia» фонемизатор даёт как `ɑːlˈɪviə` («а-ЛИВ-ия»), 56 раз; «Whitaker» как `wˈɪɾeɪkɚ` («Уит-ЭЙ-кер»), 8 раз. Если на слух плохо, добавить замену фонем в `tools/narrate.py`, а не править сценарий. Проверено и в порядке: «Mama Di» (`dˈaɪ`), «meringue», «three-forty», «under S», «under C», «the Who column», «Two fourteen Linden Street».

---

**Оценка: 8/10.** Сильный, чистый текст для голоса: живая Дайан с сухим юмором, точные бытовые детали, честная механика траста, расплата публичная и заслуженная, тёплый финал без проповеди. До 9 мешают: ошибки в ch01, строка 9 и ch09, строки 11 и 43; не посеянные долги Кевина; в кульминации героиня пассивна, а адвокат не проговаривает вслух, почему Кевин проиграл; четырёхминутная пауза в начале.

**Главное изменение для удержания:** сжать ch01, строки 13–31 (знакомство с семьёй, 1:15–5:35) примерно до 300 слов и вернуть слушателя в коридор у двери в кабинет до конца второй минуты. Героев представлять через то, что Дайан видит и слышит из коридора, а не отдельным рассказом. Первые пять минут решают, останется ли фоновый слушатель на девяносто, и сейчас это единственный отрезок эпизода, где история стоит на месте.

## Итог правок
Правки внёс писатель (работа прервалась ночью из-за лимита использования; проверено и дописано утром).
1. ch01: «between the turkey and the pie» → «over pie and coffee». ✅
2. ch09: «To hear his will» исправлено. ✅
3. ch09: «came up one short» исправлено. ✅
4. Долги Кевина посеяны заранее: лодка в ch01, «Whatever Kevin owed, he did not owe it to a car wash» в ch03. ✅
5. ch10: Харольд связывает улики с «тем самым предложением» и подчёркивает, что доверенность принесли сегодня, через три недели после подписания. ✅
6. ch10: Дайан сама кладёт на стол бумаги врача из сумочки. ✅
7. «Mr./Mrs.» → «Mister/Missus»; правило и проверка добавлены в style-guide и линтер. ✅
8. Повтор «the voice she saves for waiters» убран из ch06. ✅
- ch01: вступление с представлением семьи сокращено (глава теперь ~1 000 слов), сцена в коридоре не останавливается надолго. ✅
- «thirty-one years»: 12 → 3 раза. ✅
- Желательно: названа сумма (чуть больше миллиона долларов), Харольд объясняет, почему условие лучше, чем просто вычеркнуть Кевина; название пансионата заменено на выдуманное «Larkspur Commons». ✅
- Итог: ~14 750 слов ≈ 95 минут — на 250 слов выше формулы, оставлено сознательно (финальные главы не режем). Предложение траста в ch07 и ch10 совпадает дословно. Линтер чистый.
