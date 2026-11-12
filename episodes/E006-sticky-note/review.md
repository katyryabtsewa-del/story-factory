# E006 — review.md (редактор, свежий взгляд)

Проверено: bible.md, outline.md, idea.md, ch01–ch08 (перечитаны после правок писателя: версии от 22:01, файлы стабильны), style-guide, story-formula, VARIETY.md, idea.md эпизодов E001–E005.
Номера строк ниже относятся к файлам `script/chNN.txt` в текущем виде.

## Линт (`tools/lint_script.py`)
- Всего 9423 слова (около 60 минут). Главы: 1187 / 1195 / 1190 / 1187 / 1196 / 1121 / 1164 / 1183, все в норме. ch06 (1115–1121) у нижней границы, ch08 больше не перерастает (теперь 1183).
- Длинных абзацев (больше 160 слов) линт больше не показывает.
- Повторы пятисловных фраз: «on the eighteenth of november» x4, «the eighteenth of november i» x4, «at the back of the» x3, «the back of the room» x3.
- Ручная проверка: CAPS-слов нет (записка теперь обычным регистром), многоточий и тире нет, сокращений (Mr, Mrs, Dr, St) нет, цифр, «$», «%» нет, ремарок в скобках нет. Запрещённых штампов из style-guide нет. «Let's get ahead of it» встречается 3 раза (ch01, ch04, ch06), лимит пять соблюдён.
- Правило CLAUDE.md: только вымысел, настоящих людей и брендов в роли злодеев нет, графики нет. Диклеймера в тексте нет, он нужен только в описании (publish-pack).

---

## Обязательно исправить

1. **ch07 L3 против ch06 L53: в каком кармане телефон.** ch06: «In the left pocket I put Earl's button ... In the right pocket I put the telephone.» ch07: «with a recording running in my left pocket». Исправление: в ch07 поставить «right pocket».

2. **ch01 L27 против L45: ручка.** L27: «I laid the pen on the table as if it were nothing at all.» L45: «Curtis's pen was still in my fist, and I set it in the cup holder as if it were evidence.» Исправление: либо в L27 она ручку не кладёт («I set the pen down on my knee»), либо в L41 добавить «I took the pen along without noticing», и тогда L45 станет логичной (и забавной).

3. **ch07 L59 и ch08 L5: «lien released and recorded».** Закрытия не было, значит залога (deed of trust) никто не регистрировал, освобождать нечего. ch07: «the lien is being released and recorded as of this call». ch08: «The loan was voided and the lien released». Исправление: ch07 «The application is withdrawn, and no lien will be recorded against this property»; ch08 «The loan was canceled before a single dollar moved».

4. **ch07 L35: время фото неоднозначно.** «They discharged me at ten past three. Fern Albright took that picture at twelve minutes after, in the parking lot.» Слушатель услышит 3:22, а в ch06 L33 на снимке 3:12. Исправление: «at twelve minutes past three».

5. **ch02 L19: арифметика возраста.** «When I signed the shop's first lease, I was thirty ... I have signed that way for forty years.» Ей 71, магазин работал 41 год и закрыт четыре года назад, значит открылся, когда ей было 26 (45 лет назад), а метка («forty years») появилась позже. Исправление: «When I signed the shop's lease renewal, I was thirty-one» (или «a few years into the shop»), метка сорок лет остаётся. Тогда ch07 L51 «For forty years» тоже верно.

6. **ch03 L45 против дат: свидетельская строка.** «He told Mister Teague that Missus Brandt signed the witness line.» Диктовка 20 ноября, штамп 21 ноября, а Nicole подписала свидетеля только 2 декабря (ch05, ch04 L65). Как Мариссоль узнала о строке, которой 20–21 ноября ещё не было? Сразу после этого фото оригинала (ch04 L65, девять вечера того же дня) приходит от Hatch: как он за день достал подшитый оригинал? Исправление: в ch03 «He told Mister Teague that his wife would sign the witness line, and on the second of December she did. I saw the page come back with her name on it»; в ch04 одной фразой: Мариссоль сфотографировала страницу в картотеке и отправила Hatch (или Hatch получил ордер).

7. **ch04 L3–L35 и ch06 L25: алиби скрыто от Fern и Hatch (нечестный приём).** Fern возила Josie на операцию 18 ноября и сделала снимок «Pirate». Когда Josie рассказывает ей «the whole of it», Fern обязана сразу сказать «Josie, the eighteenth was your eye». Hatch, ищущий доказательства, тоже спросил бы «where were you that day?». Сейчас скрытность работает на сюрприз слушателя, но выглядит искусственно, и Josie перестаёт быть умной и становится «рассказчиком с припрятанной картой». Исправление: в ch04 Fern хлопает себя по лбу, Hatch спрашивает про бумаги и просит «hold it back, don't show anyone, let him tell his version first» (эта реплика уже есть в ch06 L41, перенести сюда). В ch06 сцена с выпиской остаётся, но как показ Мариссоль и смех. Слушатель по-прежнему узнаёт дату операции только в ch06 (ch05 L11 уже намекает: «the nineteenth of November, the evening after my eye surgery»).

8. **ch06 L37: почему Curtis выбрал именно 18 ноября.** «Curtis knew I was having my eye done sometime in the fall ... he never asked which Tuesday.» Но Curtis живёт с Николь, Николь принесла суп 19-го, а бумагу он диктовал 20-го, то есть он знал о дне операции, когда задним числом вписывал 18-е. Читатель-юрист заметит. Исправление: добавить в ch06 (или ch03), что операция была назначена на 25 ноября и перенесена на 18-е из-за отмены другого пациента; Josie сказала Nicole по телефону вечером, Nicole приехала на следующий день с супом, а Curtis был в Нашвилле на семинаре. Тогда реплика «he picked the day Mister Teague's calendar was empty» становится логичной.

9. **ch03 L31: «Someone studied my checks» и при этом нет метки.** Если подделывали по чекам, где метка стоит на каждом, она бы попала в копию. Исправление: Curtis скопировал подпись со скана или факса (формы пенсии, бланк почтовой пересылки), где метка «small as an eyelash» пропала. Реплика Josie: «He worked from a copy of a copy, and a knot that small does not survive a photocopier.»

10. **Претекст «Medicare housekeeping» (ch01 L5, ch02 L7) не объяснён, а Josie умная.** Почему для бумаг Medicare нужен нотариус и титульная контора, и почему «окно закрывается в конце недели» (окно общей регистрации в Medicare осенью), и Josie, 71 год, на Medicare давно, не удивляется? Исправление: одна фраза в ch01 до L5: «He had told me on the telephone that the supplement company wanted my forms notarized, and I had learned long ago that people who say a thing twice are not sure of it.» И в ch02 L7 убрать «Medicare window», заменить на «the supplement forms are due Friday».

11. **Кем работает Curtis, в тексте не сказано.** По bible он «financial adviser, Pike and Brandt Financial». Слово «financial» нет ни в одной главе, а это объясняет и его доверие у Josie, и умение вести заём. Исправление: ch01 L5 или ch02 L23: «Curtis, who told people for a living how to look after their money».

12. **Что Nicole знала о займе (ch01, ch07 L11).** В ch01 Curtis при Nicole называет пачку «Medicare housekeeping». В ch07 при Nicole же говорит «We're closing a loan on the house. We talked about it, remember?» и Nicole не реагирует. Либо Nicole знала о займе (тогда ложь про Medicare при ней странна), либо не знала (тогда в ch07 это должна быть вспышка). Исправление: в ch07 после L11 добавить реакцию Nicole («A loan, Curtis? You said paperwork»), а в ch05 L19 Nicole уточнить, что ей сказали «Mom's affairs, tidy up».

13. **ch08 L9 против L25: сроки.** «for six weeks after» (Nicole в спальне), а переезд «at the end of March» (почти десять недель с 16 января). Исправление: «for ten weeks after». Заодно ch08 L11: «because waiting ... has no purpose except to stay out of her way» нескладно, лучше «because all the waiting asks of you is that you stay out of her way».

14. **ch07 L25 против ch03 L17: Мариссоль и швабра.** Она «never left [her desk]» весь день 18-го, но «I mopped the stairs twice». Исправление: «I mopped the front mat twice» (мат у стола) или «I mopped the entry twice, and I could see the door from the mop bucket». Плюс посадить дождь заранее: в ch06 Josie вспоминает, что на фото Fern асфальт мокрый («the parking lot was shining»), тогда её вопрос «was it raining» в ch07 L21 выглядит как расставленная ловушка, а не удача.

15. **Печатное фото (ch06 L41, ch07 L33).** Fern показывает фото на телефоне (ch06 L33), Hatch «slid the packet and the photograph into a clear envelope», в ch07 Nicole берёт «the photograph with both hands». Где распечатали? Исправление: «Fern's drugstore print» одной фразой в ch06, или Hatch говорит «I'll have a print made by morning».

16. **Звонок Tri-County (ch05 L37–L47) пропал в ch06 и в ch08.** В ch06 за столом никто не упоминает, что Josie только что слышала мотив и срок (212 тысяч, 1 февраля). В ch08 запись из кармана и сама эта улика не названы, хотя именно она (и запись заёмщика) основа обвинения. Исправление: в ch06 Josie пересказывает звонок, Hatch: «That's motive, and a date.» В ch08 L5 одна фраза: «My own telephone, the one in my pocket, had heard every word.»

17. **Роль Gordon-подозрения (ch06 L49) никуда не ведёт.** «Mister Teague knows someone talked ... He looked at me a long time.» В ch07 Gordon ведёт себя, как будто ничего не знает. Либо снять ночное сообщение, либо использовать (см. раздел «Что улучшит удержание»).

---

## Желательно

**Структура и темп**
1. **Развязка Curtis слишком короткая (ch07 L55–L69).** Публичное падение есть и заслуженное (кредитор на громкой связи, нотариус, дочь), но сам Curtis теряет лицо одной репликой («Let's not do this here»). Аудитория этой ниши ждёт чуть большего. Добавить беат: пока Josie ждёт, на телефоне Curtis вспыхивает «Tri-County», он сбрасывает, Hatch замечает; или Nicole говорит ему тихо одну фразу («You let me sign it»). Не кричать.
2. **Середина идёт «по рельсам».** После ch04 (план) всё срабатывает ровно так, как придумал Hatch: никто не сопротивляется, Gordon подозревает и молчит, Curtis не пробует запасной ход. Один настоящий сбой в ch06–ch07 сильно поднимет напряжение (см. итог ниже).
3. **Эскалация по формуле (три волны).** Первая волна (ch02: почта, таблетки, термостат, церковь) и вторая (ch04: ветчина, брошюра, ключи) есть, третья по существу сам заём. Волна два скромная; можно добавить ещё одну мелочь, которая касается денег (например, Curtis «случайно» приносит бланк смены адреса для пенсии).
4. **ch08 открывается тремя абзацами сводки фактов** (L5–L7) и только потом сцены. Для аудиорассказа лучше начать с Nicole в дверях или с Fern и пирогом, а факты (обвинение, комиссия Gordon, заём) рассыпать по сценам. Слёзы Nicole на пятое утро (L13–L23) хороши и сдержанны, это лучшее место главы.
5. **Название ch07 «Page Four of Four»** ничему в главе не соответствует (страница четыре упоминается только в ch01). Переименовать («Look Under the R») или добавить в ch07 реплику Josie про страницу четыре.
6. **Josie усилила страх Nicole собственными «забывчивыми» трюками (холодильник, ch04 L43), и в ch08 никто это не признаёт.** Одна строка в ch08 L17 («I am sorry about the glasses in the refrigerator, too») добавит моральной глубины и теплоты без проповеди.
7. **Earl's button (ch06 L53) посажен и не сработал.** В ch07 она могла бы сжать пуговицу в кармане, когда Curtis называет голубое церковное платье; или в ch08 положить пуговицу в коробку рядом с запиской. Без выплаты деталь выглядит забытой.
8. **Метка в финале.** Мотив tick/knot прошёл через ch02–ch07, а в ch08 звучит только «I knotted the end of it». Красиво: Josie выписывает Nicole квитанцию за пальто и ставит метку, Nicole впервые её замечает.

**Правдоподобие**
9. **Сильнейшая улика не использована:** Мариссоль печатала бумагу 20 ноября, а в ней сказано, что Josie подписала 18-го (ch03 L15: «Curtis said that you had signed already»). Бумаги, о которой «подписано», в тот день ещё не существовало. Вставить Мариссоль одну фразу: «But I typed it on Thursday, Missus Ledbetter. How could you have signed it on Tuesday?»
10. **Квитанция Мариссоль (ch03 L25).** «It said Ledbetter Alterations at the top», а ателье закрыто четыре года назад (ch02 L17), и квитанция двухлетней давности. Исправление: «from the last of my old receipt books» (и у Josie тогда есть повод помнить). Заодно: bible называет её «three-year-old receipt», idea тоже; в тексте «two years old», это согласовано с замужеством, оставить так, но не забыть при публикации описания.
11. **Josie не узнаёт Мариссоль,** хотя ту невесту («rush, bridal gown») она подгоняла два года назад. Она «замечает всё». Одна строка в ch03 L5: «I did not know her face under the parka until she took out the folder. A bride looks different when she is not standing on a stool.»
12. **Кому принадлежала квитанция в среду-пятницу.** ch04 L3: «Marisol's receipt in my cardigan pocket»; в ch04 L21 она её кладёт на стол Hatch; в ch06 L51 Josie пишет Мариссоль «Bring your receipt»; в ch07 L47 Мариссоль «kept a receipt». Одной фразой в ch04 Hatch фотографирует обе бумаги и отдаёт, а Josie возвращает оригинал Мариссоль в четверг.
13. **Юридические мелочи в общих чертах.** «district attorney» (ch08 L5) в Теннесси «district attorney general»; допустимо оставить «prosecutor». Реплика кредитора (ch07 L27) про личное явление подписанта 18 ноября неестественна для кредитора, он проверяет сам договор, а не доверенность. Приемлемо, но можно смягчить: «we also need the notary to confirm the identity of the borrower.»
14. **Curtis в ch05 L39–L43** излишне откровенен (громкая связь в доме цели, «the old girl signs», «estate planning»). Правдоподобно только потому, что он считает её спящей; добавить, что он прошёл на кухню и прикрыл дверь, но «the door to the kitchen stood open, because it always does», и он этого не заметил. Тогда его самоуверенность читается как характер, а не удобство сюжета.
15. **ch01 L33:** Nicole «we looked this morning» подразумевает, что они обыскивали дом утром, а Josie приехала на своём Buick отдельно. Одна фраза о том, кто приехал на чём.

**Повторы**
16. **ch03 L3 почти дословно повторяет ch02 L37** («ice in her hair», «garment bag over her arm»), а ch03 и ch04 оба начинаются «On Wednesday morning». Переформулировать ch03 L3 («Marisol Vega came in out of the cold ... ») и ch04 L3 («By ten that same Wednesday»).
17. **«hardest»: четыре раза** (ch05 L29, L31; ch08 L11, L17), плюс «second hardest» в ch08. Оставить ch05 как главный, в ch08 заменить («it cost me more than anything that month»).
18. **Сравнения «like a man ...»**: ch04 L51, ch06 L7, ch07 L55, ch07 L61 (+ ch08 «a man who»). И в целом сравнений из мира шитья и «как ...» много (like a pin x3+, like a knot, like a stitch, like a quilt, like a carpenter's rule, like a kettle). Оставить по одному на главу, особенно срезать в ch07.
19. **«seven weeks»** в ch03 L33 и ch07 L61. От 21 ноября до 16 января почти восемь; во втором случае «for two months».
20. **«Remember that.» (ch02 L21)** прямой посыл к слушателю, слишком похоже на подсказку. Убрать, оставить «nobody would notice it unless they were looking».
21. **«Pirate»/«pen»/«glasses»** заходят много раз; это мотивы, но «Josie, hon» (9 раз) и «hon» (13 раз) у Curtis, Josie и Nicole звучат одинаково. Оставить «hon» только Curtis и Josie.

**Озвучка**
22. **«louvered door»** (ch06 L7, ch07 L21, L63): сомнительное произношение. Заменить на «slatted door».
23. **Буква «r»** («under the last r», ch02 L29, ch03, ch07 L49, L51) ТТС может прочитать как «are» (особенно в «Look under the r»). Протестировать на озвучке; запасной вариант «under the last letter».
24. **ch07 L41:** «'Mama,' she whispered. 'The nineteenth. You were. I did.'» Обрывки непонятны на слух. Исправление: «Mama,» she whispered. «The nineteenth. You were in that chair, and I did bring the soup.»
25. **ch06 L49–L51:** сообщения Мариссоль и ответ Josie даны без кавычек и без глагола («the message said»). Добавить «she wrote» / «I wrote back», чтобы голос не склеил с повествованием.
26. **ch07 L35** длинное предложение с числами (одиннадцать, полвторого, четверть третьего, три десять, три двенадцать подряд); для слуха фоном трудно. Разбить на два абзаца или убрать «checked in at eleven».

**Разнообразие и имена**
27. **Сходство с E004:** январь, форма B, поддельная ссуда под залог дома, частный кредитор, соседка-союзница, частичное примирение. Злодей и механизм расплаты разные (зять с алиби и меткой против падчерицы с банковской ячейкой), так что формально «шаблонным» эпизод не считается. Но VARIETY.md стоит отметить: в следующих двух эпизодах не брать «поддельная доверенность/ссуда» и «долг частному кредитору» как мотив. Сцена звонка Tri-County (ch05) прямо перекликается с Dale Voss из E004; сделать её короче.
28. **Тема «семья считает, что она выживает из ума»** уже была в E001 (недееспособна) и E005 (иск о недееспособности), теперь в E006 (шутки про память, брошюра о скрининге). Это уже третий эпизод из шести. Здесь подана мягче, но в новых идеях избегать.
29. **Имена.** «Cumberland Home Lending» и «Tri-County Bridge Capital» слишком обычные (правило style-guide о редких названиях). Предложить «Harlan Ridge Lending» и «Dunmore Bridge Capital». «Dottie» (ch04 L13) девятый именованный персонаж при лимите восемь; заменить на «my cousin». Буквы имён различаются (J, E, N, C, G, M, F, H), это хорошо.
30. **Расхождение с bible:** переадресация почты в тексте в декабре (ch02 L23), в bible в начале января. Текстовая версия логичнее (до заявки на заём), поправить bible, не текст.
31. **Концовка.** Мораль «in two sentences, because I do not care for sermons» (ch08 L45) объявляет проповедь и всё же её произносит; вторая фраза про очки сильная, первую («People who love you can be badly wrong ...») можно сократить или убрать. Вопрос слушателю хорош и конкретен, откуда слушают тоже.

## Что хорошо (оставить)
Холодное открытие (первые 230 слов дают унижение при чужих людях, записку и обещание). Концовки глав все с крючками (ch01 «It was not on the courthouse square», ch02 «I need a hem», ch03 «Missus Brandt is your daughter», ch04 фото свидетельской строки, ch05 игла, ch06 «I only hope I remember why»). Nicole использована, а не злодейка («Mom»/«Mama» работают). Curtis не мультяшный (мягкий, вежливый, голос почти не повышает). Юмор сухой («Earl was a lineman. He thought everybody was a wire.»). Дни недели и даты в календаре 2025–2026 сошлись (18 ноября вторник, 2 декабря вторник, 13 января вторник, 16 января пятница, 1 февраля воскресенье, 23 ноября воскресенье). Пауза в ch08 «It was enough for a Wednesday» совпадает с пятым утром после пятницы.

## Оценка
**7 из 10.** Крепкий, тёплый, чистый по языку сценарий с отличным началом и хорошим финалом. Минусы: несколько мелких ошибок непрерывности (карман, ручка, время фото, возраст) и несколько дыр правдоподобия вокруг даты 18 ноября (скрытое алиби, выбор даты, метка на подделке) и вокруг претекста с Medicare; развязка Curtis короткая, а середина идёт без сопротивления.

## Одно изменение, которое лучше всего поднимет удержание
Добавить в ch06–ch07 один настоящий сбой плана: использовать ночное сообщение Мариссоль («Mister Teague knows someone talked»). Пусть Gordon предупредит Curtis, и в пятницу Curtis придёт с запасным ходом, например с готовым письмом от «клиники памяти» и с предложением перенести подписание, или Gordon за столом внезапно «вспоминает», что подпись была в среду. Josie тогда выигрывает не по расписанию Hatch, а на ходу (дождь, метка, выписка), и сцена закрытия впервые становится опасной, а не демонстрацией. Дальше развязка Curtis (п. 1 из «Желательно») получает больше веса.
