import telebot
from telebot import types
from src.post_gen import gf_mobile, gf_pc_prog, gf_cinema, gf_pc_game
import os


def start_bot():
    print('shablons online')
    
    bot = telebot.TeleBot('6492907465:AAEJurC3-1vyB2yr-QTawkEjINNgDdAz8OQ')

    @bot.message_handler(commands=['generate'])
    def gen(message):
        mark = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton('Мобилы', callback_data='Мобилы')
        btn2 = types.InlineKeyboardButton('Пк прога', callback_data='Пк прога')
        btn3 = types.InlineKeyboardButton('Пк игра', callback_data='Пк игра')
        btn4 = types.InlineKeyboardButton('Фильм', callback_data='Фильм')

        mark.row(btn1, btn2)
        mark.row(btn3, btn4)

        bot.send_message(message.chat.id, 'Какой шаблон использовать?', reply_markup=mark)

    @bot.callback_query_handler(func=lambda callback: True)
    def on_click(callback):
        if callback.data == 'Мобилы':
            gf_mobile.a(callback.message, bot)
        elif callback.data == 'Пк прога':
            gf_pc_prog.a(callback.message, bot)
        elif callback.data == 'Пк игра':
            gf_pc_game.a(callback.message, bot)
        elif callback.data == 'Фильм':
            gf_cinema.a(callback.message, bot)

    bot.infinity_polling()


def stop_bot():
    print('shablon offline')
    exit()
