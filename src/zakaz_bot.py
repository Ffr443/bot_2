import telebot
from telebot import types
import os

tip = ''
marks = ''
admin = ''
zakazs_chan_id = -1002104013970
mes = 0
cloud_id = -1002012204005
my_id = 6565465251
def start_bot():
    print('zakazs online')
    global admin
    
    bot = telebot.TeleBot('6428217862:AAG2q-SlY8t7t32ZmbN7RcXG-gGq98yrmlw')

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

    @bot.message_handler(commands=['ask'])
    def mm(message):
        global mes
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Да', callback_data='yeah')
        btn2 = types.InlineKeyboardButton('Нет', callback_data='no')
        mark.row(btn1, btn2)

        mes = bot.send_message(message.from_user.id, 'Ты прочитал списки в закрепах каналов?', reply_markup=mark)

    def ask(message):
        global mes
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Игру/Программу на телефон', callback_data='mobileGame')
        btn2 = types.InlineKeyboardButton('Игру на ПК', callback_data='PCGame')
        btn3 = types.InlineKeyboardButton('Программу на ПК', callback_data='PCProg')
        btn4 = types.InlineKeyboardButton('Фильм', callback_data='cinema')

        mark.row(btn1, btn4)
        mark.row(btn2, btn3)

        bot.edit_message_text('Что вы хотите заказать?', message.chat.id, mes.message_id, reply_markup=mark)

    def send_to_admins(message):
        global zakazs_chan_id
        s = message.text
        global tip
        username = f'@{message.from_user.username}' if message.from_user.username is not None else 'У ишака нет юзернейма'
        mes = f'''#новый_заказ
#{tip}
От: {message.from_user.first_name}
Юзернейм: {username}
ID заказчика: {message.from_user.id}
{s}'''

        bot.send_message(message.chat.id, 'Готово!')
        bot.send_message(zakazs_chan_id, mes, parse_mode='HTML')

    @bot.message_handler(commands=['callback'])
    def clb(message):
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1', callback_data='one')
        btn2 = types.InlineKeyboardButton('2', callback_data='two')
        btn3 = types.InlineKeyboardButton('3', callback_data='three')
        btn4 = types.InlineKeyboardButton('4', callback_data='four')
        btn5 = types.InlineKeyboardButton('5', callback_data='five')

        mark.row(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, '''Оууу, вы решили оценить наш труд?\n
Тогда, поставьте нашему коллективу
оценку от одного до пяти:''', reply_markup=mark)

    def send_callback(message):
        mem = message.text
        sss = f'''#новый_отзыв от {message.from_user.username}
ID этого пользователя: {message.from_user.id}
Оценка: {marks}
Текст отзыва: {mem}'''
        bot.send_message(-1001908182534, sss, parse_mode='HTML')
        bot.send_message(message.chat.id, 'Готово!')

    @bot.message_handler(commands=['get_game'])
    def games(message):
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Day\'s gone', callback_data='dayu')
        btn2 = types.InlineKeyboardButton('Last of us', callback_data='last')
        btn3 = types.InlineKeyboardButton('God of war', callback_data='godof')
        btn4 = types.InlineKeyboardButton('Marvel\'s spider man', callback_data='spider')
        btn5 = types.InlineKeyboardButton('Horizon zero dawn', callback_data='horizonzero')
        btn6 = types.InlineKeyboardButton('Miles Morales spider man', callback_data='milesmorales')
        mark.row(btn1, btn3)
        mark.row(btn2, btn5)
        mark.row(btn4, btn6)
        bot.send_message(message.chat.id, 'выбери игру:', reply_markup=mark)

    @bot.callback_query_handler(func=lambda callback: True)
    def clb(callback):
        global admin
        global marks
        global tip
        global mes
        global daysgone
        global cloud_id
        global my_id
        cha = callback.message.chat.id

        if callback.data == 'mobileGame':
            bot.edit_message_text('Напишите полное название игры/программы', cha, mes.message_id)
            tip = 'мобила'
            bot.register_next_step_handler(callback.message, send_to_admins)
        elif callback.data == 'yeah':
            ask(callback.message)
        elif callback.data == 'no':
            bot.edit_message_text('Тогда не пудри мне мозги,\n иди и прочитай!!!', cha, mes.message_id)
            spiski = f'''Игры на пк:
<a href="https://t.me/PC_GF/3889">Список_1</a>\n
<a href="https://t.me/PC_GF/3890">Список_2</a>\n
<a href="https://t.me/PC_GF/3891">Список_3</a>\n
<a href="https://t.me/PC_GF/3892">Список_4</a>\n
Проги на пк:
<a href="https://t.me/GF_progs/10">Список_1</a>\n
Игры/проги на мобилу:
<a href="https://t.me/GF_Mobile/4">Список_1</a>\n
Кино:
<a href="https://t.me/gf_mf/7">Список_1</a>\n'''

            bot.send_message(cha, spiski, parse_mode='HTML')
        elif callback.data == 'PCGame':
            bot.edit_message_text('Напишите полное название игры', cha, mes.message_id)
            tip = 'пк_игра'
            bot.register_next_step_handler(callback.message, send_to_admins)
        elif callback.data == 'PCProg':
            bot.edit_message_text('Напишите полное название Программы', cha, mes.message_id)
            tip = 'пк_прога'
            bot.register_next_step_handler(callback.message, send_to_admins)
        elif callback.data == 'cinema':
            bot.edit_message_text('Напишите полное название фильма', cha, mes.message_id)
            tip = 'фильм'
            bot.register_next_step_handler(callback.message, send_to_admins)
        elif callback.data == 'one':
            marks = 'Одна звезда'
            bot.send_message(callback.message.chat.id, '''Можете объяснить нам, что такого мы сделали,
Что вам не понравилось?''')
            bot.register_next_step_handler(callback.message, send_callback)
        elif callback.data == 'two':
            marks = 'Две звезды'
            bot.send_message(callback.message.chat.id, '''Что по вашему мы делаем не так?
Пожалуйста, опишите наш минус''')
            bot.register_next_step_handler(callback.message, send_callback)
        elif callback.data == 'three':
            marks = 'Три звезды'
            bot.send_message(callback.message.chat.id, '''Что бы вы сделали для улучшения канала(ов)?
Напишите своё предложение''')
            bot.register_next_step_handler(callback.message, send_callback)
        elif callback.data == 'four':
            marks = 'Четыре звезды'
            bot.send_message(callback.message.chat.id, '''Спасибо за хороший отзыв!
Отправьте пожелания и идеи сообщением ниже''')
            bot.register_next_step_handler(callback.message, send_callback)
        elif callback.data == 'five':
            marks = 'Пять звёзд'
            bot.send_message(callback.message.chat.id, '''Спасибо что вы, так цените наш труд!!!
Мы бы хотели чтобы вы написали нам что именно нравится именно вам''')
            bot.register_next_step_handler(callback.message, send_callback)
        elif callback.data == 'dayu':
            i = 2
            bot.delete_message(cha, callback.message.message_id)
            while i < 28:
                bot.forward_message(callback.message.chat.id, cloud_id, i)
                i += 1
            # bot.send_message(my_id, f'day\'s gone запросил {message.from_user.first_name}')
        elif callback.data == 'last':
            # opovesheniye(callback.message, 'last of us')
            i = 28
            bot.delete_message(cha, callback.message.message_id)
            while i < 50:
                bot.forward_message(cha, cloud_id, i)
                i += 1
            # bot.send_message(my_id, f'last of us запросил {message.from_user.first_name}'
        elif callback.data == 'godof':
            # opovesheniye(callback.message, 'god of war')
            i = 50
            bot.delete_message(cha, callback.message.message_id)
            while i < 64:
                bot.forward_message(cha, cloud_id, i)
                i += 1
            # bot.send_message(my_id, f'god of war запросил {message.from_user.first_name}')
        elif callback.data == 'spider':
            # opovesheniye(callback.message, 'spider man')
            i = 64
            bot.delete_message(cha, callback.message.message_id)
            while i < 90:
                bot.forward_message(cha, cloud_id, i)
                i += 1
        elif callback.data == 'horizonzero':
            # opovesheniye(callback.message, 'horizon zero dawn')
            i = 90
            bot.delete_message(cha, callback.message.message_id)
            while i < 111:
                bot.forward_message(cha, cloud_id, i)
                i +=1
        elif callback.data == 'milesmorales':
            i = 111
            bot.delete_message(cha, callback.message.message_id)
            while i < 130:
                bot.forward_message(cha, cloud_id, i)
                i += 1

    bot.infinity_polling()


def stop_bot():
    print('zakaz offline')
    exit()
