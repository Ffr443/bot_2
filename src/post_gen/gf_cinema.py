b = ''
b1 = ''
b2 = ''
b3 = ''
b4 = ''
b5 = ''
b6 = ''
b7 = ''
b8 = ''
b9 = ''
b10 = ''


def a(message, bot):
    def a10():
        bot.send_message(message.chat.id, 'Отправь фильм')
        bot.register_next_step_handler(message, a1)

    def a1(message):
        global b10
        b10 = message.video.file_id
        bot.send_message(message.chat.id, 'Введи название')
        bot.register_next_step_handler(message, a2)

    def a2(message):
        global b
        b = message.text
        bot.send_message(message.chat.id, 'Введи жанры через #')
        bot.register_next_step_handler(message, a3)

    def a3(message):
        global b1
        b1 = message.text
        bot.send_message(message.chat.id, 'Введи качество фильма')
        bot.register_next_step_handler(message, a4)

    def a4(message):
        global b2
        b2 = message.text
        bot.send_message(message.chat.id, 'Введи озвучку файла')
        bot.register_next_step_handler(message, a5)

    def a5(message):
        global b3
        b3 = message.text
        bot.send_message(message.chat.id, 'Введи описание')
        bot.register_next_step_handler(message, a9)

    def a9(message):
        global b1, b2, b3, b4
        b7 = message.text
        b8 = f'''<b>Название:</b> {b}
        
<b>Жанр:</b> {b1}

<b>Качество:</b> {b2}

<b>Озвучка:</b> {b3}

<b>Описание:</b> {b4}'''

        bot.send_video(message.chat.id, b10, caption=b8, parse_mode='HTML')
        bot.send_video(-1001944039273, b10, caption=b8, parse_mode='HTML')

    a10()
