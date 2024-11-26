from telebot import TeleBot

bot = TeleBot('7789630083:AAHky2mw6lV8KdTWPSRJK8aIIDLZQ_g7a24')

@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'Привет! Я - Дика, первый бот Дианы😎😎\n\nЕсли ты хочешь...\nАктивировать бота напиши /start\nУзнать новости напиши /news\nУзнать тг Дианы напиши /tg\nУзнать, почему KarDi4045 напиши /why\nУзнать, как у содателя дела напиши /howareyou\nПопращаться напиши /bye')

@bot.message_handler(commands=['news'])
def botic_1(message):
    bot.send_message(message.chat.id, ('{}, ...сегодня новостей нет'.format(message.from_user.first_name)))

@bot.message_handler(commands=['tg'])
def botic_2(message):
    bot.send_message(message.chat.id, '@kardi4045')

@bot.message_handler(commands=['why'])
def botic_3(message):
    bot.send_message(message.chat.id, ('А почему {}?)\n\nОкей, окей😇\n\nПовторюсь, моего создателя зовут Диана (Kar - Каримова). Как-то давным-давно она поняла, что ники её старших братьев в "что-то"грамме были - karvad4040 и karel4041 (Vad - Вадим, El - Эльвир). Она поняла, что её старый ник "dianakarrr" звучит уже не хайпово, решила не отставать и назвалась kardi4045 (потому что 4042, 4043, 4044 были заняты)\n\nЕщё поболтаем?)☺️☺️'.format(message.from_user.first_name)))


@bot.message_handler(commands=['howareyou'])
def botic_4(message):
    bot.send_message(message.chat.id, 'Кажется, она опять готовиться к ЕГЭ.. Думаю, у неё все хорошо. Не будем мешать🤫\n\nА ты чем занимаешься?😎')


@bot.message_handler(commands=['bye'])
def botic_5(message):
    bot.send_message(message.chat.id, ('Пока, {}! Буду ждать тебя тут🙆🏻‍♀️'.format(message.from_user.first_name)))


bot.infinity_polling()