b = ''
b1 = ''
b2 = ''
b3 = ''
b4 = ''
ph = ''


def a(message, bot):
    def plan():
        bot.send_message(message.chat.id, 'Скинь лого')
        bot.register_next_step_handler(message, a1)

    def a1(message):
        global ph
        ph = message.photo[0].file_id
        bot.send_message(message.chat.id, 'Введи название')
        bot.register_next_step_handler(message, a2)

    def a2(message):
        global b
        b = message.text
        bot.send_message(message.chat.id, 'Введите тип')
        bot.register_next_step_handler(message, a3)

    def a3(message):
        global b1
        b1 = message.text
        bot.send_message(message.chat.id, 'Введите версию')
        bot.register_next_step_handler(message, a4)

    def a4(message):
        global b2
        b2 = message.text
        bot.send_message(message.chat.id, 'Введите язык интерфейса')
        bot.register_next_step_handler(message, a5)

    def a5(message):
        global b3
        b3 = message.text
        bot.send_message(message.chat.id, 'Взлом есть?')
        bot.register_next_step_handler(message, a6)

    def a6(message):
        global b4
        b4 = message.text
        bot.send_message(message.chat.id, 'Введите описание')
        bot.register_next_step_handler(message, a8)

    def a8(message):
        b5 = message.text
        b6 = f'''<b>Название:</b> {b}

<b>Тип:</b> {b1}

<b>Версия:</b> {b2}

<b>Язык:</b> {b3}

<b>Требуемая разрядность:</b> 32/64бит

<b>Взлом: </b> {b4}

<b>Описание:</b> {b5}'''
        bot.send_photo(message.chat.id, ph, caption=b6, parse_mode='HTML')
        bot.send_photo(-1001944039273, ph, caption=b6, parse_mode='HTML')

    plan()
