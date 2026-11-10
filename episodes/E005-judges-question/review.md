# E005 — Review (редактор)

Прочитано: bible, outline, idea, ch01–ch08, style-guide, story-formula, variety, idea.md эпизодов E001–E004, VARIETY.md.

**Lint (`tools/lint_script.py`):** всего 9592 слова, около 61 минуты. Главы 1177–1238 слов, все "ok". Запрещённых штампов линтер не нашёл. Ручной grep: цифр, "$", "%", тире, многоточий, скобок и сокращений (Mr, Mrs, Dr) нет. Единственное клише вне списка: "monkey's uncle" (ch02).

**Сверка чисел с bible, совпадает:** номер на K, T, R и seven four one (ch04, ch07); сорок один кол, счёт растёт 11 → 33 → 41 (ch04); шесть звонков и шесть времён (ch04, ch07 совпадают посимвольно); четырнадцать человек в зале (ch01); одиннадцать шагов (ch01, ch07); часы на четыре минуты медленные (ch01, ch02, ch05, ch08 считают верно). Имена, возраст и родня совпадают с bible; именованных героев восемь, имена на разные буквы. Скрытого владения, чтения документов на празднике и "раскрытия адвокатом" нет. Ферма открыто принадлежит Вере. Реальных людей и брендов в роли злодеев нет.

## Обязательно

1. **Хронология петиции и звонков не сходится (ch01, ch02, ch04).**
   - ch01: "my son Brent had filed it five weeks earlier", и петиция перечисляет "Six calls ... made by Missus Halvorsen over the past weeks".
   - ch04: первый вечер был "five weeks before that morning", а шестой звонок был в пятницу следующей недели, то есть примерно за 3,5 недели до суда.
   - ch02: повестку принёс парень в кепке "four weeks earlier". Выходит, петиция подана раньше, чем сделаны все шесть звонков, которые она перечисляет.
   - Исправление: подать петицию не раньше чем за три недели до суда (в ch01 "three weeks earlier", в ch02 "two weeks earlier, a Thursday"). Тогда последний звонок идёт сразу перед подачей. Или написать "amended petition". Обновить bible. Проверить, что ch03 ("a Tuesday two weeks earlier", визит Imani) и ch05 ("one week before") остаются в порядке.

2. **Арифметика почтового заявления (ch05).**
   - "It was dated six weeks earlier. That was a full week before the first white truck had come up the county road."
   - Сцена в почтовом отделении происходит за неделю до суда, первая машина была за пять недель. Шесть недель назад от сцены — это семь недель до суда, то есть за две недели до машины, а не за одну.
   - Исправление: "seven weeks" и "two weeks", либо "dated seven weeks before the hearing" без второй привязки.

3. **Данни противоречит сам себе про колья (ch04 и ch06).**
   - ch04, первый вечер: "The stakes were not [gone], though he only looked at the ground where I pointed and wrote in his notebook".
   - ch04, показания: "On my fourth visit I noticed orange survey stakes". Тот же сюжет ещё раз в ch06: "I wrote it down, and then the next call came in".
   - Исправление: в ch04 первый вечер Данни не должен видеть колья. Он в темноте смотрит туда, куда показывает Вера, и видит только следы колёс. Либо в показаниях: "I first wrote the stakes down on my fourth visit, ma'am, in daylight".

4. **Судья ни разу не показывает, откуда взялся её вопрос (ch06, ch07).**
   - Судья задаёт вопрос про "permission to enter your mother's land" и связывает это с Брентом. В тексте до этого момента нет ничего, что к этому подводит.
   - Главное: отчёт Imani с кольями и колеями только упомянут как "in the record" (ch06) и нигде не пересказан. Выглядит как удобное совпадение, а не как работа умного судьи.
   - Исправление: в ch06 одной репликой судьи ("The visitor's report notes forty-one survey stakes and fresh tire ruts on the north boundary") и одной строкой про брокерскую работу Брента и Tucker Rand, "interested party". Тогда вопрос в ch07 выглядит выстраданным.

5. **Слушатель не знает, кто такой Tucker Rand (ch01, ch04, ch05, ch07).**
   - Первое упоминание: "His name was Tucker Rand." Без должности и без компании.
   - Summit Row Homes впервые звучит только в ch08. Связь "Basalt Line Surveying нанят Summit Row" нигде не объявлена. В суде есть только "With a developer".
   - Исправление: в ch01 или ch04 одна фраза: "land acquisition director for Summit Row Homes, a developer; he had asked the court to let him sit as an interested party". В ch07 после "Basalt Line Surveying" добавить связь (чётко, но без долгой речи). Можно устами судьи: "And who hired Basalt Line?" — Брент: "Summit Row". Это и есть его "yes".

6. **Показания о смене адреса в суде не используются (ch05, ch06, ch07).**
   - Налоговый пункт петиции остаётся без ответа. Молодой адвокат принёс "written statement" почтмейстера (ch06: "I also asked the postmaster for a written statement"), но он так и не озвучен.
   - Решение в ch07: "no evidence, much less clear and convincing evidence" по всем четырём пунктам, а печка, налог и прогулки в суде не опровергнуты.
   - Улика с семёрками (подделка подписи) повисла, и только в ch08 Брент в голосовой почте извиняется "about the sevens".
   - Исправление: в ch07 после вопроса про разрешение судья коротко берёт заявление почтмейстера из папки молодого адвоката и спрашивает Брента: "Did you file a change of address in your mother's name?" Или одна строка судьи в вердикте: "and the court has read the postmaster's statement". Тогда не повисают ни налог, ни семёрки. Объяснить, откуда Брент знает про печку и соседку (ch02 "Someone had handed him one small true thing"): сейчас это пустая нить.

7. **Перебор повторов чисел: три разных "сорок один" и ещё "одиннадцать" (ch01, ch04, ch05, ch07, ch08).**
   - ch01: "forty-one third graders" (градобой). ch04, ch05, ch07, ch08: сорок один кол. ch08: "counted heads going out, forty-one adults and children, and twenty-two more behind them" (искусственное эхо).
   - Одиннадцать: шаги (ch01, ch07), первые колья (ch04), минуты перерыва (ch06). Для слушателя без текста всё это сливается.
   - Исправление: градобой, например, "thirty-eight third graders". Из ch08 убрать "forty-one" и сказать просто "sixty-three out, and sixty-three in". Первые колья в ch04 — "nine" вместо "eleven" (при нумерации "second stake, first, third" проверить арифметику).

8. **Часы в ch06 противоречат сами себе.**
   - "eleven minutes of recess left by my watch and seven by the courthouse clock". Остаток перерыва — длительность, она одинакова на любых часах. Медленные часы сдвигают показания, а не остаток.
   - Исправление: "with eleven minutes of recess left" без второго числа, либо "the courthouse clock said ten forty-one, and my watch said ten forty-five".

9. **Реальное время в ch06–ch08 не сходится.**
   - Перерыв до 10:55 по часам Веры; в ch08 "The gavel came down at four minutes before noon by my watch". Между возобновлением и приговором показано минут десять-пятнадцать, а не час.
   - Исправление: вердикт около "eleven twenty-one by my watch, seventeen past by the clock". Или добавить сцену. Форма D держится именно на часах, поэтому нельзя оставлять пустой час.

10. **Адвокат Брента ведёт себя нереалистично (ch07).**
    - "He looked at his lawyer, who looked at his shoes." Брент признаёт под присягой соглашение с застройщиком, и его представитель не просит перерыва, не возражает против вопроса, не советует молчать.
    - Исправление: одна реплика адвоката ("Your Honor, I request a moment with my client") и одна реплика судьи ("Denied. The question is simple.") или Брент сам отмахивается от адвоката. Мягкий вариант: адвокат уже возражал в начале ch07, судья его осадила. Добавить в конец сцены короткое "He opened his mouth and the judge raised a finger", тогда его бездействие объяснено.

11. **Данные о номере и "no known contractor" (ch04, ch07).**
    - ch07: у диспетчера на первом звонке есть "registration return ... Basalt Line Surveying". Данни был на первом звонке и спустя три визита пишет "no known contractor" (ch04). Если владелец машины известен с первого дня, шериф мог сопоставить колья с нанятой геодезической фирмой.
    - Это дыра для умной героини: прошло пять недель, а ни она, ни полиция не связали номер с фирмой.
    - Исправление: в ch06 Данни: "The return went to the log, ma'am, nobody put it in front of me." Вере же в ch05 дать причину, почему она не позвонила в Basalt ("I had the letters and no way to ask without tipping them off"). Объяснить, что сделал бы разумный человек.

12. **Атрибуция реплик для одного синтетического голоса (ch07, ch06).**
    - ch07, блок с судьёй и Брентом подряд без тегов: `"Yes, you gave permission."` — `"Yes, Your Honor. Under an agreement. With a developer."` — `"Did you tell your mother about this agreement?"` — `"No."` — `"Did your mother give you authority to speak for her land?"` — `"No," he said`. Слушатель не знает, кто говорит.
    - Исправление: теги "the judge said" / "Brent said" на каждой второй реплике. То же в ch06 (диалог с адвокатом, "Anything.").

## Желательно

1. **Нет реальной угрозы поражения (структура, ch02–ch05).** Судья скептична с первой страницы, Вера спокойна, Imani явно на её стороне, заголовок и ch01 обещают победу. С ch02 по ch05 (около 31 минуты) в зале выступают свидетели Брента, но новая информация идёт в основном из флэшбэков. Улучшение: добавить конкретный срок ("a bed at the supported living place is held until Friday") и момент, где судья на секунду склоняется к Бренту (после показаний про налог). Деньги тоже нигде не названы: ни миллион четыреста тысяч, ни шестьдесят тысяч аванса. Одна строка в ch07 (Tucker или судья: "an advance of sixty thousand dollars") даёт мотив.

2. **Формула глав слишком одинаковая.** Каждая глава 2–6: фраза о зале, флэшбэк на "a Tuesday/Thursday N weeks earlier", возврат ("The courtroom came back to me / around me / I was back in the courtroom with the heater ticking", ch02, ch03, ch04). Разнообразить: одна глава без флэшбэка (например, ch05 целиком в зале и коридоре), одна с возвратом посреди реплики.

3. **Слабый хук конца ch02.** "My son was only on the stove, and he had a long list still to go." Это констатация. Лучше вопрос или угроза, например: Брент берёт из папки конверт с рекламой "supported living" и показывает судье.

4. **Холодное открытие (ch01).** Первые 150 слов: часы против часов, потом три абзаца декораций. Крючок "tries to take your farm" есть, но самая сильная строка ("There were also prowlers. I counted them") только в конце. Идея: добавить её обещанием в самом начале, либо сократить описание зала и поставить "nobody's blaming you" раньше.

5. **Подставка для финала (честная игра).** Крышки от яичных упаковок: в ch01 нигде не видно, что в кармане куртки лежат шесть крышек. Одна фраза про карман в ch01 или ch06 делает ход из ch07 хитростью, а не фокусом. Заодно: Вера в ch06 просит адвоката "не останавливать, когда судья спросит", но у неё нет причин ждать вопроса. Показать, что она догадалась по отчёту Imani или по тому, как судья смотрела на Данни.

6. **Показания судьи без присяги (ch07).** Вера отвечает на вопрос судьи стоя, без присяги, потом ей же передают "evidence". Достаточно слов судьи: "You may be sworn" или "You are under oath as of now".

7. **Повтор списка времён звонков три раза за 10 минут.** ch04 (список), ch07 (Вера повторяет), ch07 (клерк зачитывает журнал). Клерка сократить: "Six entries, and every time matches what Missus Halvorsen said to the minute". Добавить что-то новое (например, что на втором звонке диспетчер сам записал "plate given"). Список на слух утомляет.

8. **Пересечение с E001 и E004.**
   - E001 тоже была "declared incompetent", тоже "leaves the stove on" (E001 idea.md: "tells her doctor she 'leaves the stove on'") и сын-злодей. В E005 печка и сын-злодей снова. Лучше заменить печку другим эпизодом (машина в кювете, незапертая калитка, не та таблетка).
   - Подслушанный разговор в точке поворота (ch05) уже был в E001 (дети делят дом). Подслушка у фонтана очень удобна и мало связана с планом Веры. Желательно, чтобы Вера использовала услышанное (например, спросила судью про "timing"), иначе это декорация.
   - E004 тоже суд/запись, "on the record" и стенограмма. Это терпимо, но следить: не больше одного такого финала подряд.
   - Четыре эпизода из пяти с сыном или невесткой как главным злодеем. Здесь отличает развязка (журнал, свидетель), но тон и ритм похожи на E002.

9. **Любимые обороты.**
   - "like a man ..." и родня: ch01 "like a man waiting for a table at a restaurant"; ch02 "like a man adding rooms to a house he did not own"; ch03 "like a man leading a horse across a creek", "the air of a man arriving at the part he had practiced the most"; ch04 "the air of a man who had put a very large book on a very small shelf"; ch06 "like a man who has set a table"; ch07 "like a man leaving a restaurant when the check is coming". Ресторанная пара (ch01 и ch07) читается как намеренное эхо, остальные оставить два-три, остальное заменить на прямое описание.
   - "casserole" трижды (ch02 конверт "as though it were a casserole he had dropped", ch03 "hot dish", ch06 "holding it as carefully as a person holds a casserole in a church basement").
   - "exactly right" (ch06 Данни, ch08 "which was exactly right").
   - Приём "I want you to understand that", "I should tell you", "I will say plainly", "I do not tell you this to make a sermon of it" (ch04, ch05, ch06, ch08): оставить не больше двух.
   - Счёт: слово "count" около 46 раз на 9,5 тысячи слов, плюс "the way I did with the children". Мотив сильный, но в ch01 (10 раз) и ch08 (8 раз) тяжёлый. Убрать счёт там, где он не двигает сюжет (шаги в финале ch07 уместны; счёт гостей и кольев в ch08 можно сократить на треть).
   - "My young lawyer" около пятнадцати раз; приемлемо, но в ch06 и ch07 дать один раз другое определение ("the young man beside me").
   - "monkey's uncle" (ch02): заменить на более свежее восклицание Pearl.

10. **Многословный ch06.** Это самая "тихая" глава: Lloyd (около 200 слов), болтовня Pearl, кофе. Слова Lloyd повторены в ch06, дважды в ch08 ("you do not own an orchard, you borrow it from the next fellow", "hand it on with the trees in better shape than I found them", последняя фраза ch08 про "the next fellow"). Bible просит упомянуть один-два раза. Оставить в ch06 и один раз в ch08.

11. **Проповедь в ch08.** "because a person who wants to get even does not need three weeks of paper" и "I do not think those two things cancel each other out. I think a person carries both, like a basket of pears on each arm" — второе хорошо, первое лишнее. Концовка в целом тёплая и открытая, вопрос слушателю конкретный и свой.

12. **Реальный топоним.** Medford, Oregon — настоящий город. CLAUDE.md и bible требуют только вымышленные места. Заменить на вымышленный ("Rogue Bend", "Camas Junction"), особенно потому, что с ним связаны брокерская фирма, фирма геодезистов и почтовый ящик, подставленный в подделке. Названия Cascade Valley, Summit Row, Basalt Line очень общие, возможны реальные одноимённые компании; сделать менее ходовыми.

13. **Озвучка.**
   - Слова, которые синтетический голос может исказить: Comice (ch01, ch06), Bosc (много раз), Imani, Okafor, Ocampo, Halvorsen. Проверить на пробной озвучке; при необходимости фонетически "Bosk", "Koh-meess" в тексте не писать, а подобрать замену ("Bosc" оставить, "Comice" упростить до "winter pear").
   - "Sit down," в ch08 с большой буквы и запятой; в прямой речи без кавычек голос прочитает как обычное предложение. Взять в кавычки или переписать косвенной речью.
   - Фраза "Six forty-two. Six fifty-one. Six forty. Seven oh five. Six forty-eight. Six fifty-five." читается как скороговорка из одинаковых слогов (ch07). Лучше соединить в предложение.
   - "K, T, R" и "B, A, S": голос, скорее всего, читает буквы нормально; проверить паузы на запятых.
   - ch05: детали про "crossed sevens" визуальные. На слух нужно прямо назвать Брента: "my son" вместо "I know only one person who does".

14. **Вечерний свет (ch04).** Конец февраля в южном Орегоне: сумерки заканчиваются около 6:20 вечера. Звонки в 6:42–7:05, но Вера пишет номер "in the last light" и видит "light going orange behind the ridge". Для первого вечера допустимо, для седьмых-девятых вечеров (7:05) уже темно. Заменить "last light" на "the beam of my flashlight" или сдвинуть времена. Времена, правда, есть в bible, так что вернее смягчить описание света.

15. **Диспетчер знает голос Веры уже в первый вечер (ch04).** "The dispatcher knew my voice" на первом звонке, при том что "caller known to dispatch" должна быть привычка, возникшая позже. Исправление: "The dispatcher knew my voice from the school years" или перенести фразу на второй звонок.

16. **Постскриптум Брента (ch08).** "I am paying back what I took". Кому и что. Нужна одна ясная строчка: "the sixty thousand dollars". Позволит голосовой почте закрыть нить мотива.

17. **Брент не злодей из мультика: хорошо.** Стыд на Рождество, "pear pie", семёрки, "Okay. Bye, Mom." Tucker Rand тоже сдержан. Единственное замечание: в ch05 Brent и Tucker в коридоре почти дословно проговаривают план ("Once she's under, the timing works ... you have your authority by the end of the month") и повторяют "timing matter" дважды подряд; сократить один из повторов.

## Итог

**Оценка: 7 из 10.** Сильное: ясная форма D, чистый и честный вопрос судьи, героиня действует доказательно (крышки, номер, счёт), нет скрытого владения и нет выступления адвоката, злодей-человек, тёплая открытая концовка. Слабое: хронология петиции и звонков, дыры в связке судья-Брент-застройщик, пассивные средние главы без угрозы поражения, избыток повторов (счёт, "like a man", Lloyd).

**Одно изменение для удержания:** добавить в середину (конец ch04 или ch05) реальную угрозу поражения с цифрами: судья по ходу показаний Брента склоняется к временной опеке, "bed at the supported living place held until Friday", и названа сумма (шестьдесят тысяч аванса, миллион четыреста за землю). Тогда слушатель боится потерять ферму, а вопрос судьи в ch06 становится спасением, а не просто красивой точкой.

## Итог правок (ночная смена)
Все 12 пунктов «Обязательно» и большая часть «Желательно» выполнены (хронология: петиция за три недели до суда; Tucker Rand представлен; показания почтмейстера и заявление использованы; угроза поражения и суммы добавлены; вымышленные названия: Camas Junction, Larch Hollow Land Brokers, Copperleaf Homes; повторы сокращены). Не сделано: разнообразить формулу глав, заменить эпизод с плитой, сменить «Comice». Линтер: 9782 слова ≈ 63 мин, чисто.
