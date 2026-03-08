name = ''
tip = ''
version = ''
mass = ''
android = ''
lang = ''
cash = ''
network = ''
description = ''
logo = ''
msg = ''


def a(message, bot):
    def photo():
        bot.send_message(message.chat.id, 'Отправь лого')
        bot.register_next_step_handler(message, nAme)

    def nAme(message):
        global logo
        logo = message.photo[0].file_id

        bot.send_message(message.chat.id, 'Введи название')
        bot.register_next_step_handler(message, janr)

    def janr(message):
        global name
        name = message.text

        bot.send_message(message.chat.id, 'Введи жанры через #')
        bot.register_next_step_handler(message, ver)

    def ver(message):
        global tip
        tip = message.text
        bot.send_message(message.chat.id, 'Введите версию игры')
        bot.register_next_step_handler(message, massa)

    def massa(message):
        global version
        version = message.text
        bot.send_message(message.chat.id, 'Введите вес игры')
        bot.register_next_step_handler(message, andro)

    def andro(message):
        global mass
        mass = message.text
        bot.send_message(message.chat.id, 'Введите андроид для игры')
        bot.register_next_step_handler(message, langs)

    def langs(message):
        global android
        android = message.text
        bot.send_message(message.chat.id, 'Введите языки')
        bot.register_next_step_handler(message, kesh)

    def kesh(message):
        global lang
        lang = message.text
        bot.send_message(message.chat.id, 'Введите информацию про кеш')
        bot.register_next_step_handler(message, netw)

    def netw(message):
        global cash
        cash = message.text
        bot.send_message(message.chat.id, 'Введите инфу инета')
        bot.register_next_step_handler(message, desc)

    def desc(message):
        global network
        network = message.text
        bot.send_message(message.chat.id, 'Введите описание')
        bot.register_next_step_handler(message, send)

    def send(message):
        global description, msg, logo
        description = message.text
        msg = f'''<b>Название:</b> {name}

<b>Жанр:</b> {tip}

<b>Версия:</b> {version}

<b>Вес:</b> {mass}

<b>Требуемая версия Android:</b> {android}

<b>Языки:</b> {lang}

<b>Кеш:</b> {cash}

<b>Интернет</b> {network}

<b>Описание:</b> {description}'''

        bot.send_photo(message.chat.id, logo, caption=msg, parse_mode='HTML')

        bot.send_photo(-1001944039273, logo, caption=msg, parse_mode='HTML')

    photo()
