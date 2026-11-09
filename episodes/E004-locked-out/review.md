# E004 — Review (редактор)

Объём: 11 051 слово, около 71 минуты, 9 глав по 1 190–1 250 слов. Соответствует плану (70 мин). Тире, многоточий, цифр и сокращений типа Mr. нет. Запрещённых штампов из списка нет.

Вердикт: сильное холодное открытие, чистая цепочка «вопрос в конце каждой главы», тёплый финал без проповеди. Проблемы в трёх местах: (1) дыры в логике «почему она не звонит юристу/в полицию» и «покупатель дома»; (2) денежная и юридическая арифметика не закрыта; (3) антагонистка Tessa почти отсутствует на странице (живьём только гл. 1 и гл. 7), середина провисает без внешней угрозы.

## Линт (`tools/lint_script.py`)
Повторяющиеся фразы: «the way i used to» ×5, «for thirty three years i» ×4, «and for the first time» ×3, «for the first time in» ×3, «the bank on water street» ×3. Все подтверждены, плюс ещё повторы, которых линт не ловит (см. п. 12 ниже). Длины глав в норме.

---

## Обязательно исправить

1. **Нет объяснения, почему Loretta не звонит юристу или в полицию (ch01, ch02, ch03).**
   Она 33 года проработала в суде, ей закрыли дом в день похорон, а ни разу не прозвучало «я записана в свидетельстве о праве собственности». В ch01 она лишь говорит «You can't just do this»; право на дом впервые произносится только в ch07 («This house has been owned jointly by my husband and me for nineteen years»). Слушатель 55+ весь первый час будет думать «позвони шерифу». Даже Winnie предлагает шерифа только в ch05.
   Исправление: в ch01 или ch02 одна-две фразы Loretta, например «I knew exactly whose name was on the deed, and I knew a locked door can be opened by a sheriff in an afternoon. But a woman who says "things have to happen quickly" is telling you something, and I wanted to hear what.» Тогда её выдержка читается как умение, а не как пассивность.

2. **Нить «покупатель на дом, закрытие в конце февраля» повисает (ch03, не закрыта ни в ch07, ни в ch08, ни в ch09).**
   ch03: «I have a buyer interested in the house. Closing is the end of February.» и «Somebody had been planning this for a long while.» Читатель ждёт, кто покупатель.
   Исправление: в ch08 Tessa признаётся одной репликой, что покупателя не было (Voss сказал: покажи контракт, и мы подождём), либо покупатель оказывается подставным человеком Lakeshore. Плюс одна фраза Loretta в ch05: ни одна компания по оформлению сделок не закроет сделку без подписи второго собственника.

3. **Логическое противоречие в признании Voss (ch07).**
   «We do the title review after funding, not before, and honestly our notary handles a high volume. We don't verify every signature.» Если проверка титула была после выдачи, Lakeshore увидел Loretta в свидетельстве о праве и всё равно не остановился. Это превращает его из небрежного в сознательно нечестного, но текст так не подаёт. Также настоящий кредитор по ссуде под залог дома обязан был бы зарегистрировать залог, и второе имя всплыло бы.
   Исправление: либо Voss говорит, что залог так и не был зарегистрирован (поэтому Loretta ничего не заметила), либо Cecilia в ch05 или ch06 одной фразой поясняет, что без регистрации «lien» пустой. Заодно в ch09 фраза «the lien they thought they held had been released» станет понятной.

4. **Денежная арифметика не закрыта (ch08, ch09).**
   Loretta вне опасности, но Tessa по-прежнему должна Lakeshore около ста пятидесяти тысяч (сто восемьдесят минус тридцать одна тысяча от Ray). ch09: «The lender would take a loss on the fees and interest» намекает, что основной долг как-то погашен, но не сказано как. Слушатель спросит, откуда деньги.
   Исправление: в ch09 одна фраза: «Tessa's spa building sale and the shop's savings went to the principal, and Lakeshore accepted that and wrote off the rest.» Цифры не обязательны, нужен только факт.

5. **«Sell the spa building» противоречит биографии Tessa (ch08, ch09 против bible и ch05).**
   По bible Happy Tails находится в арендованном здании. Продать можно только то, чем владеешь. В ch05 «ninety-five thousand dollars had gone into the new building», в ch08 «you will sell the spa building», в ch09 «She sold the spa building in April for a little less than she had hoped».
   Исправление: в ch05 одна фраза о том, что второе здание Tessa купила (ссуда пошла на покупку и пристройку), а первое осталось в аренде. Либо в ch08 и ch09 заменить «sell» на «give back the lease on the second building».

6. **Loretta в конце февраля всё ещё живёт у Winnie (ch09).**
   «Cecilia Rowe telephoned me at Winnie's». С ch06 она уже в своём доме (ch06: «I stood in my own kitchen for the first time in twelve days», ch07 и ch08 происходят в доме, поддерживаемом ключом Ray). Но в ch08 она говорит, что писала условия «the night before in Winnie's spare room», что верно для ночи перед встречей.
   Исправление: ch09 «telephoned me at home» или одна фраза, что она вернулась в дом на следующий день после встречи.

7. **Winnie и «двадцать шесть лет» (ch01, ch05).**
   ch01: «Winnie Gault, who has lived across the street from me for twenty-six years» и «the loud whisper she has used for twenty-six years»; ch05 «in twenty-six years I had seen her do twice». Но Loretta переехала на Birchwood Lane при браке 19 лет назад.
   Исправление: «my friend for twenty-six years, and my neighbor across the lane for nineteen of them». Две других фразы можно оставить как дружбу.

8. **Смена дат и дней недели в ch03/ch04: Loretta «решила узнать в среду» без причины (ch03).**
   «I decided I would find out on Wednesday.» Ключ у неё с субботы, банк работает в понедельник, свидетельство о смерти уже в сумке (ch04: «which I had carried in my purse for eleven days»). Задержка выглядит произвольной, а «eleven days» в ch04 уже неточно: в среду пятнадцатого со дня смерти прошло около пятнадцати дней (bible: смерть за одиннадцать дней до похорон одиннадцатого января).
   Исправление: либо в ch03 указать причину (Cecilia принимает посетителей по записи на среду, Gus по вторникам вечером определяет тип ключа), либо перенести банк на вторник. В ch04 заменить «for eleven days» на «for two weeks».

9. **«Seven weeks» не сходится с календарём (ch05).**
   «Over seven weeks he paid thirty-one thousand dollars». Платежи с 11 ноября, семь недель = до 30 декабря, но в ch05 запись от 18 декабря говорит, что сердце сдало, и ch03 говорит, что Ray лежал в больнице. Кто платил из больницы?
   Исправление: «over five weeks» (до госпитализации), либо «until the week they took him in». В bible тоже поправить («mid-November to mid-December» это четыре недели).

10. **Юридическая шероховатость в ch08.**
    «I signed under her, and I wrote the time and the date and the word witnessed.» Loretta одна из сторон соглашения и не может быть свидетелем собственной сделки. Заодно в term two «signed and witnessed» нужен посторонний свидетель.
    Исправление: свидетель Winnie или Cecilia (нотариус банка). Или Loretta пишет «agreed», а statement Tessa позже подписывается у Cecilia.

11. **Название «Happy Tails Resort» (ch02, ch03, ch05, ch07).**
    Style-guide: названия только явно выдуманные и редкие. «Happy Tails» это одно из самых частых названий пансионатов для животных в США, а у нас это бизнес антагонистки. То же относится к «Lakeshore Bridge Funding» (кредитор-злодей, очень общее имя) и «Kessler Estate Services».
    Исправление: заменить на что-то редкое, например «Pinewick Pet Lodge» и «Harrow Bridge Funding». Менять по всем главам и в bible и cover/prompt.md.

12. **Повторы фраз (линт плюс ручной поиск).**
    - «the way I used to»: ch01:37 «wrote things on my steno pad», ch02:19 «read the texts the way I used to read exhibits», ch04:39 «the way I used to number exhibits», ch05:3 «the way I used to read transcripts», ch07:77 «the way I used to stand outside a jury room». Плюс ch03:13 «I did what I used to do when a witness lied». Оставить два (ch02:19 и ch07:77), остальные переписать без «used to».
    - «thirty-three years»: ch01:23, ch02:5, ch02:29, ch06:5, ch06:41, ch07:19, ch09:29 (семь раз). Лимит style-guide 4–5. Убрать в ch01:23, ch06:5 и ch06:41 (где можно сказать «the courtroom»).
    - «for the first time»: ch02:29, ch04:5, ch04:19, ch06:49, ch07:61, ch09:5, ch09:15 (шесть и больше). Оставить ch06:49 и ch09:15, остальные переписать.
    - «the bank on Water Street»: ch04:5, ch05:11, ch07:39, ch08:25. В ch05:11 использовано то же самое здание, где работает Cecilia. Это важно: банк, отказавший Tessa, тот же самый, где Cecilia; она не реагирует. См. п. 14.
    - Красные уши: ch01:41 (чужой слесарь: «his ears were red»), ch02:33 и 39 (Gus), ch06:11, ch09:9. Это фирменная черта Gus, у безымянного слесаря она размывает образ. Убрать у слесаря ch01:41.
    - «bright as a new penny» ch04:39 и ch09:19. Заменить одно.

13. **Исполнитель замка: расхождение между ch01 и ch02.**
    ch01: слесарь из сети из соседнего округа, профессионал, жалеет об «old cylinder». ch02 (Gus): замок «installed backward... A child could slip this with a library card». Нанятый профессионал не ставит замок задом наперёд, а засов («deadbolt») карточкой не открывается (это про язычковый замок). Bible говорит «man Tessa found online».
    Исправление: в ch01 слесарь работал под присмотром Tessa и «was told to use the lock she brought», либо Gus говорит «throw's reversed, a pry bar would take it off in a minute».

## Желательно

14. **Cecilia слишком щедра с чужими данными (ch05).**
    «The lender's money had come into an account at her own branch, and the shop's payments had gone out of another». Сотрудник банка не раскрывает владельцу ячейки данные счёта третьего клиента (Tessa), а в ch04 сама же говорит, что банк «will not discuss it, with anyone». Предложение: Cecilia не называет счетов, а говорит «I cannot discuss anyone's account with you, but I can tell you where a review begins: with the wire records. We have some.» Заодно: Tessa была в её банке, и Cecilia в ch04 знает фамилию Kessler. Одна реакция («I knew her father. I did not know she'd been turned down at my own bank») добавила бы тепла и крючок.

15. **Tessa отсутствует на странице (структура, главный риск удержания).**
    Живьём Tessa только в ch01 и ch07. Между ними четыре главы (ch02–ch06, около 38 минут) только тексты, письмо с подростком и слухи. Сердце эпизода (падчерица и вдова) начинается на 55-й минуте. Предложение: одна короткая сцена лицом к лицу в ch03 или ch06 (Tessa приезжает к Winnie, или Loretta видит её на Route Twenty у питомника и видит, что та плачет в машине). Это же даёт внешнюю угрозу и в середине, где её сейчас нет.

16. **Провис середины (ch05 вторая половина, ch06).**
    После ключевого открытия (ch05) идёт около 12 минут подготовки без внешнего риска (запись, слесарь, текст, нервы). Единственное напряжение внутреннее («what if no words came»). Предложение: поставить часы. Например, в ch06 Voss или Tessa присылает уведомление о показе дома в среду, либо на дверь клеят бумагу о выселении, либо Gus находит следы чужого присутствия у питомника. Один внешний удар на 7-й минуте ch06.

17. **Voss подан слишком удобно, почти как карикатура (ch07).**
    Он выдаёт признание с мотивом «That's the whole business model... People in a hurry don't want questions» почти дословно так, как говорил Ray в ноябре (ch05: «that was between me and my family»), и без сопротивления. Закулисье («exploring opportunities in another state», ch09) происходит за кадром. Предложение: дать ему один момент ума (он замечает, что Loretta сказала «verbatim» и пытается уйти раньше, но говорит последнюю глупость от самоуверенности) и одну человеческую деталь. Тогда «he leaves to consult counsel» перестанет быть мгновенным отступлением.

18. **Ex-machina-ощущение «Ray всё предусмотрел».**
    ch06: цилиндр с биркой «Birchwood» и слова Ray «you never know who'll be locked out of their own house». Это слишком точное пророчество. Предложение: Gus говорит, что Ray держал цилиндр «for when a customer's house is sold and the new owners need old keys to work», а Loretta сама понимает, что пригодится. Или оставить как умышленный жест, но дать Gus сомнение.

19. **Условия соглашения принимаются без торга (ch08).**
    Tessa соглашается на все семь условий за полчаса после письма. Предложение: одно условие, на которое она возражает (церковный подвал или передача магазина Gus), и Loretta уступает или нет. Это придаёт «bittersweet» вес.

20. **Тема сказана трижды (ch02, ch08, ch09).**
    Ray: «She's mad at the calendar»; Tessa: «I called you Dad's wife because if I called you anything else, it meant she was really gone»; Loretta: «a language of closed doors and flattened vowels... I had been too busy being right». Плюс в ch08 Loretta говорит «I worked it out about year four», а в ch09 «for nineteen years I finished Tessa's sentences in my own head, and I had every one of them wrong». Это противоречие. Предложение: оставить реплику Tessa (самая живая) и в ch09 сократить моральный абзац до двух предложений («I will tell you what I learned... and then I will stop» это почти проповедь, три «I learned»).

21. **Сюжетные мелочи.**
    - ch01: где машина Loretta? Она приехала на ней домой, потом села к Winnie, и машина больше не упоминается. Одна фраза в ch02 («Gus drove my car over from the curb»).
    - ch02: «I'd have come last night but I didn't know». Gus на похоронах не упоминается; если был, это звучит странно.
    - ch06: «Winnie... turned up Wednesday evening with a thirty-foot orange cord», но Loretta живёт у неё. Заменить «turned up» на «produced». Также ch06 даёт две «Wednesday» с разным смыслом (15 и 22 января); указать «the Wednesday before».
    - ch07: «Mind the boxes» (в доме нет коробок; мешки в подвале у Winnie).
    - ch07: Voss «took his card from the table», но карточку он оставлял в щели в ch03.
    - ch07: встреча 9:58 до 10:41 (43 минуты), а на странице около 8. Либо «ten twelve», либо не указывать.
    - ch03/ch02: три сообщения, третье в 23:15 (ch02), в ch03 «Saturday, eleven at night, three texts». Сгладить.
    - ch08/ch04: завещание в ячейке не проходит через «probate»; одна фраза про регистрацию не нужна, но сказать «I took the will to the clerk» убрало бы вопрос.

22. **Схожесть с прошлыми эпизодами.**
    По осям разнообразия отличается хорошо (злодей, место, сцена, форма B, горько-сладкий тон, героиня). Но два пересечения стоит осознавать: (а) механизм «дом уже записан на неё, бумаги против дома недействительны» близок к E002 (мошенническая попытка рефинансирования дома, оформленного на героиню); (б) «письмо покойного мужа, которое получает злодей» близко к E001 (письмо мужа). Различия достаточные (бумаги не читаются вслух, нет адвоката, нет праздника), но в VARIETY.md стоит пометить «дом в её имени» как использованный дважды, и в следующих двух эпизодах его не повторять.

23. **Озвучка (voice-readiness).**
    - Омографы, которые синтетический голос может прочитать неверно: ch07:79 «the slow tearing of the seal» («tearing» может прозвучать как «слеза»; заменить на «ripping»); прошедшее «read» в ch03:31 «I read it twice», ch05:3 «I read my husband's notebook the way I used to read transcripts» (в одной фразе два «read» с разной формой), ch08:11 «I read the notebook». Проверить в озвучке и при ошибке переписать на «went through».
    - Имена: «Pelletier» (ch02:33) и «Gault» (ch01:31) могут исказиться. Проверить на пробе.
    - Атрибуция диалога ясная; в ch07 два длинных обмена без тегов (Voss и Loretta), но там только два говорящих, читается.
    - Цифры, даты, время словами везде. Заголовок «Box 417» (в таймкодах) оставить цифрами нельзя, если он попадёт в озвучку: если заголовок не озвучивается, всё в порядке.
    - Много сравнений «like a ...» и «the way a ...» (ch01:5 «like a new tooth», «like a hymnal»; ch03:11, 47; ch04:21, 23; ch07:61; ch08:7, 53; ch09:25): почти в каждом абзаце. Для слуха это утомляет. Сократить на треть.

24. **Правила CLAUDE.md.**
    Вымысел, без «true story»; реальных людей и злодейских брендов нет (проверить, что в описании будет дисклеймер). «Stenograph» в тексте как нарицательное слово; в bible это марка (заглавная). Нейтрально, не злодейская. «Eisenhower administration» и «Lake Erie» нейтральны. Насилия и мата нет. Нарушений нет.

---

## Оценка
**7,5 из 10.** Крепкая конструкция, тёплый голос героини, хороший «замковый» мотив от первой до последней страницы. Не хватает внешнего давления в середине и живого присутствия антагонистки; несколько логических дыр можно закрыть пятью-шестью фразами.

## Одно изменение, которое сильнее всего повысит удержание
Вывести Tessa на страницу в середине (ch03 или ch06) и поставить на её плечи видимые часы: приезд «покупателя» или бумага от Lakeshore с датой. Сейчас между ch01 и ch07 героиня борется с призраком, а слушатель ждёт сцены, ради которой пришёл. Одна живая встреча (плюс закрытие нити «покупатель») убирает провис и делает письмо Ray в ch07 ударом, а не просто развязкой.


---

## Fixes applied (правки по review)

Объём после правок: 11 398 слов, главы 1 225–1 285 слов (lint: ошибок нет, повторов нет).

Обязательные (1–13), все сделаны:
1. ch01: Loretta прямо говорит, что её имя в свидетельстве о праве собственности, что шериф открыл бы дверь за день, но это вечер похорон, снег, никто не станет слушать, и она хочет сперва понять, почему Tessa торопится. Формальное заявление под запись осталось в ch07.
2. «Покупатель»: ch05 Loretta понимает, что покупателя не было (конец февраля это срок foreclosure, назначенный Larkmoor), и что ни одна title company не закрыла бы сделку без подписи второго собственника; ch08 Tessa признаёт одной репликой. Voss в ch06 по телефону поддерживает «sale» только в рассказе Tessa.
3. Voss: Larkmoor выдал деньги по слову Tessa и печати нотариуса, title work «позже»; «we lend against the house, who signs is between the family». Cecilia в ch06 проверила реестр: залог не зарегистрирован, пустая бумага. Ray в ch05 записал тот же разговор, Loretta хочет, чтобы фраза прозвучала «where it counted».
4. Деньги: ch08 (пятый пункт) и ch09: залог недействителен, Larkmoor не может тронуть дом; Tessa должна то, что реально получила (сто восемьдесят тысяч минус тридцать одна тысяча Ray), как личный долг по плану выплат, составленному с консультантом кредитного союза; Larkmoor списывает комиссии и проценты.
5. «Sell the spa building» убрано: Foxglove арендует здание, Tessa отдаёт аренду второго здания и закрывает spa wing (ch05, ch08, ch09, bible, outline).
6. Winnie: друг двадцать шесть лет (познакомились в здании суда), соседка девятнадцать (ch01).
7. Loretta возвращается домой пятнадцатого февраля; Cecilia звонит «at home» (ch09).
8. Банк в среду: сертифицированные копии свидетельства о смерти приходят в среду по почте (ch03, ch04); «eleven days in my purse» убрано.
9. Платежи: «семь недель» с первой недели ноября до двадцать третьего декабря; скорая двадцать четвёртого, Ray умер тридцать первого декабря (ch05, bible).
10. Свидетели: Gus и Cecilia (ch08); Loretta только сторона; заявление Tessa подписывается у Cecilia.
11. Названия: Foxglove Pet Lodge и Larkmoor Bridge Funding везде (главы, bible, outline). «Kessler Estate Services» оставлено: это шаблонный бланк Tessa, заведомо поддельное название.
12. Повторы: «used to» осталось два раза, «thirty-three years» три, «for the first time» два, красные уши слесаря убраны, «new penny» один.
13. Замок: слесарь поставил дешёвый замок Tessa по её настоянию (ch01); Gus говорит про девятнадцатидолларовый замок и короткие винты, лом снимет за минуту; «library card» убрано.

Желательные: сделаны 14 (Cecilia не раскрывает счета, реакция на отказ Tessa), 15 и 16 (новая сцена Tessa и Loretta в магазине в ch06 с часами на стене, «thirty-eight days» и показом дома в четверг в полдень), 17 (Voss замечает «verbatim», привычка к мятным конфетам), 18 (цилиндр Ray теперь просто запасной, без пророчества), 20 (мораль в ch09 сокращена до двух предложений, противоречие про «year four» убрано), 21 (машина, Gus, «produced», коробки, визитка, время «ten twelve», три сообщения, завещание у register of wills), 22 (заметка в VARIETY.md), 23 («tearing» заменено на «ripping»).
Не сделано: 19 (торг по условиям), часть 23 (проверка произношения Pelletier и Gault, омографы «read» в ch03 и ch08, сокращение сравнений «like a» на треть сделано лишь частично).
