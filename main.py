import telebot
from telebot import types

from com_library_people import com_library_people

bot = telebot.TeleBot('5459381624:AAGmF0vM4LO1zviQjPpE3OjsoMSs5Lj6bG0')


@bot.message_handler(commands=['start'])
def com_start(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот поможет вам подготовиться к ЕГЭ по истории.\n'
                                      'Чтобы ознакомиться со всем функционалом введите: /help')


@bot.message_handler(commands=['help'])
def com_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but0 = types.KeyboardButton("/help")
    but01 = types.KeyboardButton("/library_date")
    but02 = types.KeyboardButton("/library_people")
    but03 = types.KeyboardButton("/literature")
    but04 = types.KeyboardButton("/website")
    but05 = types.KeyboardButton("/start")
    markup.add(but0, but01, but02, but03, but04, but05)
    bot.send_message(message.chat.id, 'Что умеет бот?\n'
                                      'При вводе любой даты выдает событие, которое произошло в Росии в это время.\n'
                                      'Просто введите любую дату. Например: 1941 \n'
                                      'Без  "." ,  ";"  или любых букв на конце!\n'
                                      '/library_date - команда, что позволит ознакомить со справочным материалом бота\n'
                                      '/library_people - команда, что позволит ознакомиться со всеми правителями России с самого её основания\n'
                                      '/literature - команда для просмотра полезной литературы\n'
                                      '/website - команда для просмотра нужных сайтов для подготовки к ЕГЭ\n'
                                      '/start - команда, чтобы начать работу с ботом!\n'
                                      '/help - помощь по командам.', reply_markup=markup)


@bot.message_handler(commands=['library_people'])
def com_library_people1(message):
    com_library_people(message)


@bot.callback_query_handler(func=lambda c: c.data == 'button1')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Рюрик(862-879)\n'
                                                  'Родоначальник царской династии Рюриковичей. Пришел по призыву на славянскую землю с братьями. Княжил в Новгороде.')


@bot.callback_query_handler(func=lambda c: c.data == 'button2')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Олег «Вещий»(879-912)\n'
                                                  'Захватил Киев, Любеч, Смоленск. Провозгласил Киев "матерью русских городов". Завоевал племенной союз древлян,\n'
                                                  ' северян, радимичей. Ходил на Константинополь, покорив его, заключил выгодный торговый договор с Византией.')


@bot.callback_query_handler(func=lambda c: c.data == 'button3')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Игорь Рюрикович(912-945)\n'
                                                  'Ходил, как и Олег на Византию. Заключил менее выгодный договор с греками'
                                                  '(в отличии от Олега). Обложил древлян тяжёлой данью, за большие поборы '
                                                  'был убит древлянами.')


@bot.callback_query_handler(func=lambda c: c.data == 'button4')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Княгиня Ольга(945-962)\n'
                                                  'Отомстила "жестоко" древлянам за убийство мужа. Установила погосты и правильные дани(уроки)\n'
                                                  ' на Руси. Одна из первых приняла христианскую веру.')


@bot.callback_query_handler(func=lambda c: c.data == 'button5')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Святослав Игоревич(962-972)\n'
                                                  'Уничтожил хазарский каганат. Покорил вятичей, вел успешные войны против'
                                                  ' Византии и приближенных ей болгар. Разделил земли между сыновьями: '
                                                  'Ярополком, Олегом и Владимиром, что привело в дальнейшем к междоусобию. '
                                                  'Из-за предательства убит печенегами (Куря, князь печенегов, приказал '
                                                  'сделать из его черепа кубок, инкрустированный золотом, и распивал из '
                                                  'него напитки).')


@bot.callback_query_handler(func=lambda c: c.data == 'button6')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярополк I Святославич(972-980)\n'
                                                  'Был, как и мать - христианином. Убил из-за расприй брата Олега (князя древлян), '
                                                  'пытался так же убить брата Владимира (князя Новгородского). '
                                                  'Но Владимир собрал войска и одолел Ярополка.')


@bot.callback_query_handler(func=lambda c: c.data == 'button7')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Владимир Святославич «Святой»(980-1015)\n'
                                                  ' Убил брата Ярополка ⁠I и стал единоличным правителем Руси. Вел '
                                                  'войны, взял Перемышль, Нервен и др. города. Захватил ятвягов,'
                                                  ' радимичей и восставших вятичей, воевал с волжскими булгарами. '
                                                  'Был крещен в 988г. и в дальнейшем крестил Русь. Искоренял язычество,'
                                                  ' строил часовни, а также знаменитый каменный собор Успения Богородицы.')


@bot.callback_query_handler(func=lambda c: c.data == 'button8')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Святополк I Владимирович «Окаянный»(1015-1019)\n'
                                                  'Захватил киевский стол по смерти Владимира. Начал кровавые'
                                                  ' междоусобные войны с братьями (за что получил прозвище Окаянный). '
                                                  'После смерти Святополка, междоусобие Ярослава с братом Мстиславом '
                                                  'продолжалось до 1036г.')


@bot.callback_query_handler(func=lambda c: c.data == 'button9')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярослав I Владимирович «Мудрый»(1019-1054)\n'
                                                  'После войн с братьями стал единоличным правителем Руси. '
                                                  'Был построен великолепный Софийский собор, несколько других '
                                                  'церквей, новая крепость и Золотые Ворота. Издал свод законов '
                                                  '"Русская правда". Пытался установить независимость Русской Церкви '
                                                  'от Константинополя(Константинопольским патриархом  не была признана '
                                                  'независимость). Расширял западные русские границы.')


@bot.callback_query_handler(func=lambda c: c.data == 'button10')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав I Ярославич(1054-1068)\n'
                                                  'Междоусобные войны. Набеги на Русь половцев. водил Русь на поляков.')


@bot.callback_query_handler(func=lambda c: c.data == 'button11')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Всеслав Брячиславич(1068-1069)\n'
                                                  'Единственный представитель полоцкой ветви Рюриковичей на киевском великокняжеском престоле.')


@bot.callback_query_handler(func=lambda c: c.data == 'button12')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав I Ярославич(1069-1073)\n'
                                                  'Междоусобные войны. Набеги на Русь половцев. водил Русь на поляков.')


@bot.callback_query_handler(func=lambda c: c.data == 'button13')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Святослав Ярославич(1073-1076)\n'
                                                  'Участник "триумвирата". Ходил с братьями на тюркские племена '
                                                  'и победил их. Является заказчиком двух "Изборников Святослава", '
                                                  'переписанных для него в 1073 и 1076 годах.')


@bot.callback_query_handler(func=lambda c: c.data == 'button14')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав I Ярославич(1076-1078)\n'
                                                  'Междоусобные войны. Набеги на Русь половцев. Водил Русь на поляков.')


@bot.callback_query_handler(func=lambda c: c.data == 'button15')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Андрей Юрьевич «Боголюбский»(1169-1174)\n'
                                                  'Помогал своему отцу Юрию Долгорукому в борьбе за Киев. Перенёс '
                                                  'столицу во Владимир, превратив Киевское княжество в удел. '
                                                  'Строил города и храмы. Перенёс из Киева икону, писанную Евангелистом '
                                                  'Лукой. Икона под именем Владимирской иконы Божьей Матери стала'
                                                  ' святыней Суздальской земли. ')


@bot.callback_query_handler(func=lambda c: c.data == 'button16')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Всеволод I Ярославич(1078-1093)\n'
                                                  'Междоусобья и набеги половцев. Отдал Чернигов сыну Владимиру.')


@bot.callback_query_handler(func=lambda c: c.data == 'button17')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Святополк II(1093-1113)\n'
                                                  ' В 1094 году заключил мир с половцами и взял в жёны дочь половецкого '
                                                  'хана. Междоусобья.')


@bot.callback_query_handler(func=lambda c: c.data == 'button18')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Владимир Всеволодович «Мономах»(1113-1125)\n'
                                                  'Прекратил смуты.  Строил города. Водворил суд и порядок. Создал '
                                                  'знаменитое "Поучение",а  также наиболее полный свод законов.'
                                                  ' При нём на Руси установилась тишина. ')


@bot.callback_query_handler(func=lambda c: c.data == 'button19')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Владимир Всеволодович «Мономах»(1125-1132)\n'
                                                  'Женился на шведской принцессе Христине. Вместе с братом '
                                                  'Ярополком охраняли торговый пути из Балтики в Азов. '
                                                  'Захватил князей Полоцких(чтобы исключить любые помехи) и выслал их '
                                                  'в Констатинополь. Провел успешную войну против литовцев.')


@bot.callback_query_handler(func=lambda c: c.data == 'button20')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярополк II Владимирович(1132-1139)\n'
                                                  'Междоусобья и раздоры между Мономаховичами и Ольговичами. '
                                                  'Возвращение половцев.')


@bot.callback_query_handler(func=lambda c: c.data == 'button21')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Всеволод II Ольгович(1139-1146)\n'
                                                  'Захватил Киев после смерти Ярополка II.')


@bot.callback_query_handler(func=lambda c: c.data == 'button22')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Игорь Ольгович(1146-1146)\n'
                                                  'Представитель династии Ольговичей — ветви Рюриковичей, '
                                                  'происходящей от Олега Святославича. Князь Новгород-Северский')


@bot.callback_query_handler(func=lambda c: c.data == 'button23')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав II Мстиславич(1146-1149)\n'
                                                  'Потомок дома Мономаховичей. Захватил Киев, нарушив право '
                                                  'старшинства своего дяди Юрия Долгорукого.')


@bot.callback_query_handler(func=lambda c: c.data == 'button24')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Юрий I Владимирович «Долгорукий»(1149-1151)\n'
                                                  'Боролся с Изяславом за Киев.В период его правления '
                                                  'Владимиро-Суздальское княжество процветало. Основал Москву, '
                                                  'Юрьев, Переславль, Дмитров. Воздвигал много храмов.')


@bot.callback_query_handler(func=lambda c: c.data == 'button25')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав II Мстиславич(1151-1154)\n'
                                                  'второй сын Мстислава Великого, внук Владимира Мономаха, великий '
                                                  'князь Киевский (1146-1149, 1150, 1151-1154), князь Волынский. '
                                                  'В борьбе за верховную власть противостоял Ольговичам, Давыдовичам '
                                                  'и своему дяде Юрию Долгорукому.')


@bot.callback_query_handler(func=lambda c: c.data == 'button26')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ростислав Мстиславич(1154-1155)\n'
                                                  'Вёл борьбу за сохранение престола при поддержке Мстислава II. '
                                                  'Мстислав II вновь занял киевский престол по смерти Ростислава, '
                                                  'но Андрей Боголюбский разграбил Киев и сделал столицей Владимир. ')


@bot.callback_query_handler(func=lambda c: c.data == 'button27')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Юрий I Владимирович «Долгорукий»(1155-1157)\n'
                                                  'В период его правления Владимиро-Суздальское княжество '
                                                  'процветало. Основал Москву, Юрьев, Переславль,Дмитров. '
                                                  'Воздвигал много храмов.')


@bot.callback_query_handler(func=lambda c: c.data == 'button28')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Изяслав III Давидович(1157-1159)\n'
                                                  'черниговский князь и Великий князь киевский (1155 год, '
                                                  'с 1157 по 1158 год, 1161),  сын черниговского князя Давыда '
                                                  'Святославича и княгини Феодосии.')


@bot.callback_query_handler(func=lambda c: c.data == 'button29')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ростислав Мстиславич(1159-1167)\n'
                                                  'Вёл борьбу за сохранение престола при поддержке Мстислава II. '
                                                  'Мстислав II вновь занял киевский престол по смерти Ростислава, '
                                                  'но Андрей Боголюбский разграбил Киев и сделал столицей Владимир.')


@bot.callback_query_handler(func=lambda c: c.data == 'button30')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Мстислав Изяславович(1167-1169\n'
                                                  'Междоусобие. Построен на Волыни Мстиславов храм.')


@bot.callback_query_handler(func=lambda c: c.data == 'button31')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Юрьевич(1174-1175)\n'
                                                  'Пришёл к власти в результате борьбы между Владимиром и Суздалем. '
                                                  'Победил Владимир.')


@bot.callback_query_handler(func=lambda c: c.data == 'button32')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярополк III Ростиславич(1175-1175)\n'
                                                  'Междоусобия.Был ослеплен и отпущен, по преданию чудом прозрел '
                                                  'после усердной молитвы в церкви святых Бориса и Глеба на Смядине.')


@bot.callback_query_handler(func=lambda c: c.data == 'button33')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Юрьевич(1175-1176)\n'
                                                  'Пришёл к власти в результате борьбы между Владимиром и Суздалем. '
                                                  'Победил Владимир.')


@bot.callback_query_handler(func=lambda c: c.data == 'button34')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Всеволод III Юрьевич "Большое Гнездо"(1176-1212)\n'
                                                  'Утвердил первенство Суздальской земли и г. Владимира. Подчинил '
                                                  'города Рязань, Муром, Новгород, Пронск, Псков и Смоленск. После '
                                                  'его смерти начался распад Суздальского княжества.')


@bot.callback_query_handler(func=lambda c: c.data == 'button35')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Константин Всеволодович «Добрый»(1212-1218)\n'
                                                  'ПЗаложил соборную церковь в Ростове, оставил после себя библиотеку'
                                                  ' (которая увеличивалась при его сыне Васильке). Летописцы называют '
                                                  'его добрым, щедрым, не помрачившим ума своего. Владел несколькими '
                                                  'языками, ценил искусство.')


@bot.callback_query_handler(func=lambda c: c.data == 'button36')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярослав II Всеволодович(1238-1246)\n'
                                                  'После смерти брата Юрия Ярослав явился из Киева, где княжил, '
                                                  'в разорённый Владимир. Первым из русских князей получил ярлык '
                                                  'на княжение от хана. С татарами не ссорился. С Литвой воевал.')


@bot.callback_query_handler(func=lambda c: c.data == 'button37')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Святослав Всеволодович(1246-1247)\n'
                                                  'Dеликий князь владимирский, сын Всеволода Юрьевича Большое Гнездо, '
                                                  'и Марии Шварновны Чешской, в крещении Гавриил.')


@bot.callback_query_handler(func=lambda c: c.data == 'button38')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Ярославич «Храбрый»(1247-1248)\n'
                                                  'Четвертый сын великого князя киевского и владимирского Ярослава '
                                                  'Второго Всеволодовича. Матерью его была Ростислава-Феодосия '
                                                  'Мстиславовна (в иночестве получила имя Евфросиния), дочь Мстислава '
                                                  'Мстиславича, великого князя новгородского и Галицкого.')


@bot.callback_query_handler(func=lambda c: c.data == 'button39')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Андрей Ярославич(1249-1252)\n'
                                                  'третий из восьми сыновей великого князя Ярослава II Всеволодовича '
                                                  'и Ростиславы Мстиславны Смоленской,  великий князь владимирский '
                                                  '(1248—1252), князь суздальский (1256—1264).')


@bot.callback_query_handler(func=lambda c: c.data == 'button40')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Александр Ярославич «Невский»(1252-1263)\n'
                                                  'Победил шведов на Неве в 1240, Ливонских рыцарей — на Чудском озере '
                                                  'в 1242, остановив шествие католицизма. Заботился о всей Руси. '
                                                  'Не позволял монголам устраивать погромы русских городов.')


@bot.callback_query_handler(func=lambda c: c.data == 'button41')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Ярослав III Ярославич\n'
                                                  'Следовал примерам отца и брата - с татарами не ссорился. '
                                                  'При нём татары приняли магометанство.')


@bot.callback_query_handler(func=lambda c: c.data == 'button42')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Василий Ярославич(1272-1276)\n'
                                                  'Созвал собор епископов для восстановления церковных уставов.')


@bot.callback_query_handler(func=lambda c: c.data == 'button43')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Дмитрий Александрович(1276-1283)\n'
                                                  'Князь новгородский и переяславль-залесский, великий князь'
                                                  ' владимирский, сын Александра Невского. Родился около 1250 года. '
                                                  'Сын великого князя Владимирского Александра Ярославича Невского и '
                                                  'его жены Александры, дочери полоцкого князя Брячислава Васильковича.')


@bot.callback_query_handler(func=lambda c: c.data == 'button44')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Андрей Александрович(1283-1284)\n'
                                                  'Для России того времени князь Андрей Александрович был худшим из '
                                                  'возможных князей. Русь нуждалась в стойком, терпеливом, умном и '
                                                  'мудром правителем. Андрей этими качествами не обладал.')


@bot.callback_query_handler(func=lambda c: c.data == 'button45')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Дмитрий Александрович(1284-1293)\n'
                                                  'Князь новгородский и переяславль-залесский, великий князь'
                                                  ' владимирский, сын Александра Невского. Родился около 1250 года. '
                                                  'Сын великого князя Владимирского Александра Ярославича Невского и '
                                                  'его жены Александры, дочери полоцкого князя Брячислава Васильковича.')


@bot.callback_query_handler(func=lambda c: c.data == 'button46')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Андрей Александрович(1293-1304)\n'
                                                  'Для России того времени князь Андрей Александрович был худшим из '
                                                  'возможных князей. Русь нуждалась в стойком, терпеливом, умном и '
                                                  'мудром правителем. Андрей этими качествами не обладал.')


@bot.callback_query_handler(func=lambda c: c.data == 'button47')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Ярославич «Святой»(1304-1317)\n'
                                                  'Получил ярлык на великое княжение от хана. По доносу князя '
                                                  'московского Юрия замучен в Орде.')


@bot.callback_query_handler(func=lambda c: c.data == 'button48')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Юрий III Данилович(1317-1322)\n'
                                                  'Получил ярлык на великое княжение от хана. Присоединил к Москве '
                                                  'Коломну и Можайск.')


@bot.callback_query_handler(func=lambda c: c.data == 'button49')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Дмитрий Михайлович «Грозные очи»(1322-1326)\n'
                                                  'сын Михаила Ярославича Тверского и Анны Дмитриевны Ростовской, '
                                                  'известной как Анна Кашинская, великий князь Тверской (1318—1326) и '
                                                  'великий князь Владимирский (1322—1326). Участвовал в борьбе отца '
                                                  'против Юрия Даниловича московского.')


@bot.callback_query_handler(func=lambda c: c.data == 'button50')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Александр Михайлович(1326-1327)\n'
                                                  'Получил ярлык на великое княжение от хана. За позволение '
                                                  'тверичанам убить ханских послов, был заменён на Иоанна '
                                                  'Калиту и убит.')


@bot.callback_query_handler(func=lambda c: c.data == 'button51')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Иоанн I Данилович «Калита(1328-1340)»\n'
                                                  'Получил ярлык на великое княжение от хана. Сделал Москву не только могущественным княжеством, но и культурныи, '
                                                  'религиозным центром. Собирал Русь под московским княжеством. Скупал '
                                                  'города и земли. Строил церковные храмы. Раздавал деньги бедным из своего мешка, '
                                                  'котрый был всегда при нем,за что получил прозвище Калита.')


@bot.callback_query_handler(func=lambda c: c.data == 'button52')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Семен Иоаннович «Гордый(1340-1353)»\n'
                                                  'На Руси, как и его отец, продолжал поддерживать мир и покой. Был дружен с Ордой, но грозен с русскими князьями, за что '
                                                  'получил прозвище Гордый. Отделил Псков от Новгорода( тем самым ухудшив союз между городами).')


@bot.callback_query_handler(func=lambda c: c.data == 'button53')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Иоанн II Иоаннович «Красный»(1353-1359)\n'
                                                  'Получил ярлык на великое княжение от хана. Имел сильную поддержку в лице митрополита Алексия. Правление Ивана II '
                                                  'считается периодом относительного ослабления Москвы и усиления его противников.')


@bot.callback_query_handler(func=lambda c: c.data == 'button54')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Алексей Федорович Бяконт (митрополит) (1359-1368)\n'
                                                  'Помогал, поддерживать и наставлял Ивана Красного. После его смерти, воспитывал его сына Дмитрия Донского.')


@bot.callback_query_handler(func=lambda c: c.data == 'button55')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Дмитрий Иоаннович «Донской»(1368-1389)\n'
                                                  'ервый построил после пожара белокаменный Кремль. Воевал с Тверью, Рязанью, Литвой, ходил на '
                                                  'казанские земли и сделал их своими данниками. Победил татар на Куликовом '
                                                  'поле в 1380г. Положил начало освобождению Руси от татарского ига. '
                                                  'Установил порядок престо наследия от отца к сыну.')


@bot.callback_query_handler(func=lambda c: c.data == 'button56')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Василий I Дмитриевич(1389-1425)\n'
                                                  'Продолжал дело собирания Руси. Получил в свое распоряжение от хана города Городец, Мещера, Таруса, Муром, '
                                                  'а также Нижний Новгород. Заставил Новгород платить народную '
                                                  'дань, как и его отцу. Перенёс Владимирскую икону Божьей Матери '
                                                  'в Москву.  Отбивал нашествия татар. Оборонял Московскую Русь от Литвы.')


@bot.callback_query_handler(func=lambda c: c.data == 'button57')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Софья Витовотна(1425-1432)\n'
                                                  'Когда умер Василий I, Василий II был еще ребенком. Софья Витовотна, мама Василия II, '
                                                  'воспитывала его в течении 7 лет, пока он не взошел на трон.')


@bot.callback_query_handler(func=lambda c: c.data == 'button58')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Василий II Васильевич "Темный"(1432-1462)\n'
                                                  'В Период его правления Московское государство стало факстически независимым от власти татар. '
                                                  'Московская церковь обрела независимость от власти '
                                                  'константинопольского патриарха. Уничтожил все уделы,'
                                                  ' кроме Твери, Рязани, Новгорода и Пскова.')


@bot.callback_query_handler(func=lambda c: c.data == 'button59')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Иоанн III Васильевич "Великий"(1462-1505)\n'
                                                  'Продолжил дело собирания Руси: подчинил Москве - Верею и Белоозеро, часть Рязани, Новгород, Тверь, Вятку. '
                                                  'В княжение Иоанна III, в 1480г свергнуто татаро-монгольское иго. '
                                                  'Создан свод законов- Судебник. Стал использовать выражения "Государь '
                                                  'Всея Руси". Любил искусство и архитектуру:были построены– Успенский '
                                                  'собор в Кремле (построен в 1475-1479гг. Аристотелем Фиорованти), '
                                                  'Благовещенский собор (построен псковскими мастерами 1482-1489гг.) и '
                                                  'Грановитая палата(созданная итальянцами в 1473-1491гг.)')


@bot.callback_query_handler(func=lambda c: c.data == 'button60')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Василий III Иоаннович(1505-1533)\n'
                                                  'Завершил собирание Руси: подчинив Москве Псков, оставшуюся часть Рязани, Смоленск, Северский удел. '
                                                  'Установил самодержавие. Покончил с удельно-вечевой системой. '
                                                  'Возводил много церквей, включая собор Архангела Михаила в Московском Кремле.')


@bot.callback_query_handler(func=lambda c: c.data == 'button61')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Елена Васильевна Глинская(1533-1548)\n'
                                                  'Воспитывала сына Ивана, пока он был маленьким. Фактическим правителем был фаворит Елены Телепнёв-Оболенский.')


@bot.callback_query_handler(func=lambda c: c.data == 'button62')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Иоанн IV Васильевич «Грозный»(1548-1584)\n'
                                                  'Первым из государей принял на себя титул Царя. Был выпущен новый Судебник. Введена выборность местной власти.'
                                                  'Заключил выгодный торговый договор с Англией, привел в Россию '
                                                  'иностранных специалистов. Присоединил к России Казань и Астрахань, '
                                                  'колонизировал Сибирь. Ввёл опричнину в 1565 и сам ее отменил в 1572. '
                                                  'Была открыта впервые типография, для печати книг. Вёл войны с Ливонией '
                                                  'и Крымом. Отверг предложения папы ввести католичество.')


@bot.callback_query_handler(func=lambda c: c.data == 'button63')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Федор Иоаннович «Блаженный»(1584-1598)\n'
                                                  'Был царём только по имени, фактически правил Борис Годунов. Построены '
                                                  'города по Волге - Саратов, Самара, Царицын, крепости Воронеж и Пелым, '
                                                  'города Тобольск и Томск в Сибири,⁠ а также Смоленскую крепостную стену, '
                                                  'которую стали называть «каменным ожерельем Земли русской». Принят Закон '
                                                  'о закрепощении крестьян. Войны с шведами и крымскими татарами.')


@bot.callback_query_handler(func=lambda c: c.data == 'button64')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Борис Федорович Годунов(1598-1605)\n'
                                                  'Избран царём на Земским соборе. Вёл колонизацию Сибири, строил там '
                                                  'города. Заботился об образовании и благополучии народа.')


@bot.callback_query_handler(func=lambda c: c.data == 'button65')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Борис Федорович Годунов(1598-1605)\n'
                                                  'Избран царём на Земским соборе. Вёл колонизацию Сибири, строил там города. '
                                                  'Заботился об образовании и благополучии народа.')


@bot.callback_query_handler(func=lambda c: c.data == 'button66')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Лжедмитрий I (Отрепьев Григорий)(1605-1606)\n'
                                                  'Из всех самозванцев Смутного времени Лжедмитрий I оставил в истории самый '
                                                  'глубокий след. Выдавая себя за якобы чудом спасшегося сына Ивана Грозного, '
                                                  'на самом деле погибшего в Угличе, он одно время даже восседал на троне в Кремле.')


@bot.callback_query_handler(func=lambda c: c.data == 'button67')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Василий Иоаннович Шуйский(1606-1610)\n'
                                                  'После смерти Бориса Годунова Василий Шуйский попытался организовать '
                                                  'государственный переворот в свою пользу, но у него ничего не вышло. '
                                                  'Тогда он затаился и стал ждать удобного времени при дворе Лжедмитрия I')


@bot.callback_query_handler(func=lambda c: c.data == 'button68')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Семибоярщина(1610-1610)\n'
                                                  'Причиной начала семибоярщины послужило поражение войск Василия Шуйского '
                                                  'и приглашенных им по Выборгскому договору союзных шведских войск Якоба '
                                                  'Делагарди, понесённое от войск Речи Посполитой в битве при Клушино (24 '
                                                  'июня (4 июля) 1610 года и последовавшее за этим насильственное смещение '
                                                  'Царя Василия Шуйского.')


@bot.callback_query_handler(func=lambda c: c.data == 'button69')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Владислав IV Сигизмундович Ваза(1610-1612)\n'
                                                  'Владислав IV Ваза всегда относился к военным делам как к самым важным и был известен как умелый военачальник.')


@bot.callback_query_handler(func=lambda c: c.data == 'button70')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Федорович "Кроткий"(1613-1645)\n'
                                                  'Заключил Столбовский мир с Швецией, а также невыгодное перемирие с '
                                                  'Речью Посполитой.  Установил мир и порядок в государстве. '
                                                  'Организовал сбор налогов. Посылал казаков осваивать Сибирь( открывали реки,'
                                                  ' озеро Байкал, строили города). Заботился о просвещении народа.')


@bot.callback_query_handler(func=lambda c: c.data == 'button71')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Алексей Михайлович "Тишайший"(1645-1676)\n'
                                                  'Из-за больших налогов на соль случились бунты. Раскол в церкви после '
                                                  'церковных реформ. Попытка перевести с серебряных денег на медные '
                                                  'закончились провалом. В войнах с Речью Посполитой возвращены России - '
                                                  'Смоленск, Черниговские земли, Стародубские, Северские земли и Левобережная '
                                                  'Украина. Продолжалось колонизационное движение в Сибирь. Основаны города в Сибири: Иркутск, Нерчинск.'
                                                  'В 1667г. был построен первый корабль "ОРЕЛ". Подавил Народные волнения под предводительством Степана Разина.')


@bot.callback_query_handler(func=lambda c: c.data == 'button72')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Федор Алексеевич(1676-1682)\n'
                                                  'Уничтожил местничество, были сожжены разрядные книги. Было введено '
                                                  'подворное обложение прямыми налогами, что обременило итак бедный '
                                                  'народ. Создал проект по созданию первой Славяно-греко-латинской '
                                                  'академии в Москве (запущенной в 1687г). Провел успешную войну с '
                                                  'Турцией (после чего был заключен Бахчисарайский мир, где Россия '
                                                  'присоединяла себе левобережную Украину и Киев с округой). Строил '
                                                  'красивые каменные здания в Москве, для защиты от пожаров.')


@bot.callback_query_handler(func=lambda c: c.data == 'button73')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Софья Алексеевна(1682-1689)\n'
                                                  'При Софье был заключен выгодный для России «Вечный мир» с Польшей. '
                                                  '27 августа 1689г. был заключен невыгодный для России Нерчинский '
                                                  'договор (первый русско-китайский договор). В 1687 и 1689 под '
                                                  'руководством фаворита Софьи Василия Голицына были предприняты '
                                                  'неудачные походы против крымских татар.')


@bot.callback_query_handler(func=lambda c: c.data == 'button74')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Петр I Алексеевич "Великий"(1689-1725)\n'
                                                  'После возвращения из Европы( Великое посольство) начал преобразования в'
                                                  ' армии, был создан военный флот. Отвоевал у турок крепость Азов, '
                                                  'построил крепость Таганрок. В 1703г. основал Санкт-Петербург. Для выхода'
                                                  ' к Балтийскому морю вёл Северную войну со Швецией, закончил её '
                                                  'окончательной победой в Полтавской битве, в честь этого в 1721г. принял '
                                                  'титул Отца Отечества, Императора Всероссийского, Петра Великого. Открывал'
                                                  ' математические, навигационные, артиллерийские, инженерные и медицинские '
                                                  'школы. Установил начало Нового Года с 1 января, а не 1 сентября.')


@bot.callback_query_handler(func=lambda c: c.data == 'button75')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Екатерина I(1725-1727)\n'
                                                  'Во время ее правления был учрежден Верховный Тайный Совет, который '
                                                  'в основном и правил страной. Утвердила господство России в Закавказье. '
                                                  'Учредила Академию наук. Заключила Венский союзный договор, ставший '
                                                  'основой русско-австрийского военно-политического альянса.')


@bot.callback_query_handler(func=lambda c: c.data == 'button76')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Петр II Алексеевич(1727-1730)\n'
                                                  'За малолетством и ленью царя управлял страной Меньшиков, после '
                                                  'его свержения - Долгоруков. Уменьшились поборы с людей. Процветала '
                                                  'коррупция и казнокрадство. Армия была в упадке, строительство кораблей прекратилось.')


@bot.callback_query_handler(func=lambda c: c.data == 'button77')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Анна Иоанновна(1730-1740)\n'
                                                  'Распустив Верховный Тайный совет, восстановила Сенат, '
                                                  'вернув ему главенствующую роль. Было создано новое учебное учреждение - '
                                                  'Кадетский корпус. Велась война с Францией за "польское наследство", '
                                                  'вследствии чего Россия получила контроль над Польшей. Велась Русско-турецкая '
                                                  'война (1735-1739гг.), где после заключения невыгодного Белградского '
                                                  'мирного договора был взят Азов, но запрещалось иметь флот на Чёрном море, '
                                                  'крепости Очаков, Кинбурн, Хотин, Яссы были возвращенны Турции.')


@bot.callback_query_handler(func=lambda c: c.data == 'button78')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Анна Леопольдовна(1740-1741)\n'
                                                  'Являлась регентом Иван VI Антоновича. Была свергнута в '
                                                  'результате дворцового переворота, приведшего на престол Елизавету Петровну.')


@bot.callback_query_handler(func=lambda c: c.data == 'button79')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Елизавета Петровна(1741-1761)\n'
                                                  'Дочь Петра Великого вступила на престол с помощью Преображенского полка. '
                                                  '  Отменила смертную казнь. Отправляла экспедиции: на освоение земель '
                                                  'на юге Урала, исследованием Камчатки. Открыла в 1755г. Московский '
                                                  'университет, гимназии в Москве и Казани, Академию художеств в 1757г.. '
                                                  'Россия участвовала в Семилетней войне 1756-1763гг.')


@bot.callback_query_handler(func=lambda c: c.data == 'button80')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Петр III Федорович(1761-1762)\n'
                                                  'Отдал Пруссии все земли занятые русскими войсками в семилетней войне. '
                                                  'Ликвидировал Тайною канцелярию. Проводил изъятие церковных земель. '
                                                  'Издал “Манифест о вольности дворянства”, который давал право '
                                                  'не служить вообще.')


@bot.callback_query_handler(func=lambda c: c.data == 'button81')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Екатерина II Алексеевна "Великая"(1762-1796)\n'
                                                  'Провела реформы в Великом Сенате. Подавила восстание Емельяна '
                                                  'Пугачева - (крестьянская война 1773г.-1775г.). Уничтожила '
                                                  'Запорожскую Сечь. Занималась образованием в стране. Был основан в 1764г. '
                                                  'Государственный Музей Эрмитаж. Приказада делать прививки от оспы, '
                                                  'первоначально, опробовав ее на себе. Участвовала в раздели Речи '
                                                  'Посполитой (было присоединено 460 тыс. км² и 6,5 млн человек). '
                                                  'Была одержана победа над Османской империей, в результате мирного '
                                                  'договора России отошел весь Крым, Азов, а также Россия получила право '
                                                  'вести торговлю и обладать военным флотом на Чёрном море.')


@bot.callback_query_handler(func=lambda c: c.data == 'button81')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Павел Петрович(1796-1801)\n'
                                                  'Принял закон о престолонаследии, отныне женщины фактически были '
                                                  'отстранены от наследования российского престола. Сильно ограничил '
                                                  'дворянские права. Облегчил положение крестьян- запрещалось работать '
                                                  'крестьянам в воскресенье, а барщину сократил до 4 дней в неделю. Вел '
                                                  'борьба с Великой Французской Революцией- запрещено ввозить иностранные '
                                                  'книги, нельзя было обучаться за границей, вводилась строгая цензура, '
                                                  'французская одежда была в не закона.')


@bot.callback_query_handler(func=lambda c: c.data == 'button82')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Александр I Павлович "Благословенный"(1801-1825)\n'
                                                  'Была открыта граница с Европой, можно было ввозить зарубежный товар. '
                                                  '20 февраля 1803 года издал "Указ о вольных хлебопашцах" '
                                                  '(за свою волю крестьяне должны были выплачивать выкуп или '
                                                  'исполнять повинности).  Основал университеты в Петербурге, Казани и '
                                                  'Харькове, царскосельский лицей. После Русско-турецкой войны 1806г.-1812г.'
                                                  ' присоеденил Бессарабию и часть областей Закавказья. После Русско-шведской '
                                                  'войны 1808г.-1809г. присоеденил всю Финляндию и Аландские острова. '
                                                  'Была одержана победа в Отечественной войне 1812 года. В 1813 году '
                                                  'состоялся заграничный поход русской армии, освободивший европейские '
                                                  'страны от господства Наполеона. За это получил прозвище "Благословенного,'
                                                  ' великодушного держав восстановителя".')


@bot.callback_query_handler(func=lambda c: c.data == 'button83')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Николай I Павлович"(1825-1855)\n'
                                                  'Подавил восстание Декабристов в 1825 году. Облегчил жизнь '
                                                  'крепостных крестьян. При Николаем I происходила промышленная '
                                                  'революция: развивалась текстильная и сахарна промышленность, '
                                                  'производились станки, инструменты, изготавливались изделия из металла, '
                                                  'дерева, стекла, фарфора, кожи и др. Запустилось производство паровозов, '
                                                  'строились железные дороги. Началось интенсивное строительство шоссейных '
                                                  'дорог с твёрдым покрытием. Ввел Россию в ненужную Крымскую Войну '
                                                  '(1853г.-1856г.), которая была проиграна.')


@bot.callback_query_handler(func=lambda c: c.data == 'button84')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Александр II Николаевич(1855-1881)\n'
                                                  'Провел военную реформу, университетскую, финансовую, городскую, '
                                                  'судебную реформу. Упразднил военные поселения в 1857г. Отменил '
                                                  'крепостное право в 1861г. С 1860 годов в стране начался экономический '
                                                  'кризис, единственное, что быстро развивалось - это железнодорожная '
                                                  'отрасль. Было подавлено Польское восстание, после начали предприниматься '
                                                  'меры по русификации Польши. В царствование Александра II '
                                                  'были присоединены Средняя Азия, Северный Кавказ, Дальний Восток, '
                                                  'Бессарабия, Батуми. Была продана Аляска. Обменял Курильские острова '
                                                  'у Японии на Сахалин.')


@bot.callback_query_handler(func=lambda c: c.data == 'button85')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Александр III Александрович "Миротворец"(1881-1894)\n'
                                                  'Убрал страну с либерального направления. Провел контрреформы, возвысив '
                                                  'дворянство и опустив крестьянский класс. Ухудшил судопроизводство, что '
                                                  'привело к произволу в судебных делах. Жестко стеснял права евреев. '
                                                  'Выросла плата за обучение, положил конец развитию женского Высшего '
                                                  'образования. Открыл Крестьянский (1882г.) и Дворянский (1885г.) банк. '
                                                  'Ударными темпами развивалась промышленность. За поддержание европейского'
                                                  ' мира Александр III получил прозвище Миротворец.')


@bot.callback_query_handler(func=lambda c: c.data == 'button86')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Николай II Александрович(1894-1917)\n'
                                                  'Занимались проблемой неграмотности населения, конечной целью которой '
                                                  'было обеспечение начального образования всему населению Российской '
                                                  'империи. Достигнуты выдающиея результаты в естественнонаучном и '
                                                  'инженерном образовании. Был введен золотой стандарт рубля, что '
                                                  'укрепило внешний и внутренний курс рубля, улучшило инвестиционный '
                                                  'климат в стране. Царствование Николая II являлось периодом '
                                                  'экономического роста страны. Проиграна Русско-японская война '
                                                  '1904-1905гг. Неудачно велась Первая мировая война. Войны истощили '
                                                  'страну и население. Был свергнут с власти в результате февральской '
                                                  'революции 1917г.')


@bot.callback_query_handler(func=lambda c: c.data == 'button87')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Владимир Ильич Ульянов (Ленин)(1917-1924)\n'
                                                  'Российский революционер, крупный теоретик марксизма, советский '
                                                  'политический и государственный деятель, создатель Российской '
                                                  'социал-демократической рабочей партии (большевиков), главный '
                                                  'организатор и руководитель Октябрьской революции 1917 года в России, '
                                                  'первый председатель Совета народных комиссаров РСФСР и Совета '
                                                  'народных комиссаров СССР, создатель первого в мировой истории '
                                                  'социалистического государства.')


@bot.callback_query_handler(func=lambda c: c.data == 'button88')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Иосиф Виссарионович Сталин(1924-1953)\n'
                                                  'настоящая фамилия — Джугашви́ли,  российский революционер, '
                                                  'советский политический, государственный, военный и партийный '
                                                  'деятель. С 3 апреля 1922 по 10 февраля 1934 года — генеральный '
                                                  'секретарь, затем — секретарь ЦК ВКП(б) (с 1952 г. — КПСС), с 19 '
                                                  'декабря 1930 года, после занятия должности Вячеславым Молотовым '
                                                  'председателя Совета народных комиссаров СССР вместо Алексея Рыкова, '
                                                  'фактический руководитель СССР.')


@bot.callback_query_handler(func=lambda c: c.data == 'button89')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Никита Сергеевич Хрущев(1953-1964)\n'
                                                  'В 1918 году Хрущёв вступил в партию большевиков. Участвовал в '
                                                  'Гражданской войне. В 1918 году возглавил отряд Красной гвардии в '
                                                  'Рутченково, затем политкомиссар 2-го батальона 74-го полка 9-й '
                                                  'стрелковой дивизии Красной Армии на Царицынском фронте. По окончании '
                                                  'армейской партийной школы в сентябре 1920 года был назначен инструктором '
                                                  'политотдела 9-й Кубанской армии, участвовал в войне в Грузии. '
                                                  'После окончания войны находится на хозяйственной и партийной работе. '
                                                  'Летом 1920 года стал политическим руководителем, заместителем '
                                                  'управляющего Рутченковского рудника в Донбассе.')


@bot.callback_query_handler(func=lambda c: c.data == 'button90')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Леонид Ильич Брежнев(1964-1982)\n'
                                                  'Председатель Президиума Верховного Совета СССР в 1960—1964 и '
                                                  '1977—1982 годах. Первый секретарь ЦК КПСС в 1964—1966 годах. '
                                                  'Генеральный секретарь ЦК КПСС с 1966 по 1982 год. Председатель '
                                                  'Бюро ЦК КПСС по РСФСР с 1964 по 1966 год.')


@bot.callback_query_handler(func=lambda c: c.data == 'button91')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Юрий Владимирович Андропов(1982-1984)\n'
                                                  'После смерти Л. И. Брежнева, последовавшей 10 ноября 1982 года, '
                                                  'с 12 ноября 1982 года Юрий Андропов сменил его на посту '
                                                  'Генерального секретаря ЦК КПСС, став официальным лидером '
                                                  'Советского Союза. Во время своего недолгого (15 месяцев, '
                                                  'или 1 год и 98 дней, или 463 дня) пребывания в должности '
                                                  'Андропов предпринял ряд мер, направленных на устранение коррупции '
                                                  'партийно-государственного аппарата, на повышение экономической '
                                                  'эффективности социалистической системы.')


@bot.callback_query_handler(func=lambda c: c.data == 'button92')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Константин Устинович Черненко(1984-1985)\n'
                                                  '13 февраля 1984 года на пленуме ЦК КПСС К. У. Черненко единогласно был '
                                                  'выбран Генеральным секретарём ЦК КПСС. За избрание Константина '
                                                  'Устиновича проголосовал и М. С. Горбачев. В августе 1983 года на'
                                                  ' отдыхе Черненко тяжело отравился копчёной рыбой, которую прислал '
                                                  'ему министр внутренних дел СССР Виталий Федорчук[15], и поэтому '
                                                  'значительную часть своего правления провёл в Центральной клинической '
                                                  'больнице, где иногда даже проводились заседания Политбюро ЦК КПСС.')


@bot.callback_query_handler(func=lambda c: c.data == 'button93')
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, 'Михаил Сергеевич Горбачёв(1985-1991)\n'
                                                  'Масштабная попытка реформирования советской системы («Перестройка»). '
                                                  'Введение в СССР политики гласности, свободы слова и печати, '
                                                  'демократических выборов, реформирования социалистической экономики '
                                                  'в направлении рыночной модели хозяйствования (концепция экономических'
                                                  ' реформ 1987 года предполагала вхождение в рыночные отношения в '
                                                  'отдалённом будущем), которая привела к глубокому экономическому кризису.')


@bot.message_handler(commands=['website'])
def com_website(message):
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Решу ЕГЭ по истории:', url='https://hist-ege.sdamgia.ru')
    but2 = types.InlineKeyboardButton('Яндекс репетитор по истории:',
                                      url='https://yandex.ru/tutor/subject/?subject_id=10')
    but3 = types.InlineKeyboardButton('Бингоскул история:', url='https://bingoschool.ru/ege/history/tasks/')
    but4 = types.InlineKeyboardButton('Банк ФИПИ по истории:',
                                      url='https://fipi.ru/ege/otkrytyy-bank-zadaniy-ege#!/tab/173765699-7')
    but5 = types.InlineKeyboardButton('ЭкзаменRU история:', url='https://www.examen.ru/tests/ege/istoriya/')
    markup.add(but1, but2, but3, but4, but5)
    bot.send_message(message.chat.id, 'Перейти на сайты:', reply_markup=markup)


@bot.message_handler(commands=['literature'])
def com_literature(message):
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('Всеобщая история. И.А. Кольцов, А.М. Судариков, М.А. Дмитриева:',
                                      url='http://elib.rshu.ru/files_books/pdf/rid_36ce89acd89d4848be5ef476c3249e43.pdf')
    but2 = types.InlineKeyboardButton(
        'История России для технических вузов. Под редакцией М.Н. Зуева и А.А. Чернобаева',
        url='https://static.my-shop.ru/product/pdf/202/2011362.pdf')
    but3 = types.InlineKeyboardButton(
        'Кириллов В.В. История России: учебное пособие. М.: Юрайт-издат., 2007 -661 С. – (Основы наук)',
        url='https://static.my-shop.ru/product/pdf/219/2180499.pdf')
    markup.add(but1, but2, but3)
    bot.send_message(message.chat.id, 'Полезная литература:', reply_markup=markup)


@bot.message_handler(commands=['library_date'])
def com_library_date(message):
    inMurkup = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton("ЕГЭ по истории 2022 Артасов 30 вариантов", callback_data='book1')
    but2 = types.InlineKeyboardButton("ЕГЭ по истории 2022 Артасов 10 вариантов", callback_data='book2')
    but3 = types.InlineKeyboardButton("ЕГЭ по истории 2019 И.В. Курукин 32 варианта", callback_data='book3')
    but4 = types.InlineKeyboardButton("ЕГЭ по истории 2016 И.В. Курукин 20 вариантов", callback_data='book4')
    but5 = types.InlineKeyboardButton("Я сдам ЕГЭ по истории 2018", callback_data='book5')
    inMurkup.add(but1, but2, but3, but4, but5)
    bot.send_message(message.chat.id, "Решебники на любой вкус", reply_markup=inMurkup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'book1':
                doc = open('book1.pdf', 'rb')
                bot.send_document(call.message.chat.id, doc)
            elif call.data == 'book2':
                doc = open('book2.pdf', 'rb')
                bot.send_document(call.message.chat.id, doc)
            elif call.data == 'book3':
                doc = open('book3.pdf', 'rb')
                bot.send_document(call.message.chat.id, doc)
            elif call.data == 'book4':
                doc = open('book4.pdf', 'rb')
                bot.send_document(call.message.chat.id, doc)
            elif call.data == 'book5':
                doc = open('book5.pdf', 'rb')
                bot.send_document(call.message.chat.id, doc)
            # удаляем инлайновую клаву
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Решебники на любой вкус",
                                  reply_markup=None)
            # Создаём уведомление
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text='Приятного чтения!')
    except Exception as e:
        print(repr(e))


@bot.message_handler()
def mode_first2(message):
    data = message.text
    count = 0
    if message.text != '':
        with open('date.txt', 'rt', encoding='utf-8') as file:
            for index, line in enumerate(file):
                if data in line:
                    while line[:4] == data or line[:3] == data:
                        bot.send_message(message.chat.id, line)
                        count += 1
                        break
    if count == 0:
        bot.send_message(message.chat.id, 'Упс! Я ничего не нашёл(')


bot.polling(none_stop=True)
