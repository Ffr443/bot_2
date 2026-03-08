logo = ''
names = ''

year = ''
tip = ''
version = ''
publisher = ''
developer = ''
lang = ''
voicing = ''
tablet = ''
reqs = ''

description = ''

file = ''


def a(message, bot):
    def photo():
        bot.send_message(message.chat.id, 'Скинь лого')
        bot.register_next_step_handler(message, name)

    def name(message):
        global logo
        logo = message.photo[0].file_id
        bot.send_message(message.chat.id, 'Введи название')
        bot.register_next_step_handler(message, age)

    def age(message):
        global names
        names = message.text
        bot.send_message(message.chat.id, 'Введи год выхода')
        bot.register_next_step_handler(message, janr)

    def janr(message):
        global year
        year = message.text
        bot.send_message(message.chat.id, 'Введи жанры')
        bot.register_next_step_handler(message, publics)

    def publics(message):
        global tip
        tip = message.text
        bot.send_message(message.chat.id, 'Введи издателя')
        bot.register_next_step_handler(message, develop)

    def develop(message):
        global publisher
        publisher = message.text
        bot.send_message(message.chat.id, 'Введи разраба(ов)')
        bot.register_next_step_handler(message, vers)

    def vers(message):
        global tip
        tip = message.text
        bot.send_message(message.chat.id, 'Введи версию')
        bot.register_next_step_handler(message, language)

    def language(message):
        global version
        version = message.text

        bot.send_message(message.chat.id, 'Введи языки')
        bot.register_next_step_handler(message, voice)

    def voice(message):
        global lang
        lang = message.text
        bot.send_message(message.chat.id, 'Введи озвучку')
        bot.register_next_step_handler(message, tabl)

    def tabl(message):
        global voicing
        voicing = message.text
        bot.send_message(message.chat.id, 'Введи таблетку')
        bot.register_next_step_handler(message, requirements)

    def requirements(message):
        global tablet
        tablet = message.text

        bot.send_message(message.chat.id, 'Введи системки')
        bot.register_next_step_handler(message, dec)

    def dec(message):
        global reqs
        reqs = message.text
        bot.send_message(message.chat.id, 'Введи описание')
        bot.register_next_step_handler(message, send)

    def send(message):
        global description
        description = message.text

        msg = f'''<b>Год выхода:</b> {year}
<b>Жанр:</b> {tip}
<b>Издатель:</b> {publisher}
<b>Разработчик:</b> {developer}
<b>Версия:</b> {version}
<b>Язык:</b> {lang}
<b>Озвучка:</b> {voicing}
<b>Таблетка:</b> {tablet}

<b>Системные требования:</b> {reqs}'''

        bot.send_photo(message.chat.id, logo, caption=names, parse_mode='HTML')
        bot.send_message(message.chat.id, msg, parse_mode='HTML')
        bot.send_message(message.chat.id, description, parse_mode='HTML')

        bot.send_photo(-1001944039273, logo, caption=names, parse_mode='HTML')
        bot.send_message(-1001944039273, msg, parse_mode='HTML')
        bot.send_message(-1001944039273, description, parse_mode='HTML')

    photo()
