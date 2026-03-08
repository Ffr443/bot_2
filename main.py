import os
import random
import sqlite3 as sql
import telebot as tBot
import src.shablon_bot as shablon_bot
import src.zakaz_bot as zakaz_bot
from threading import Thread
from telebot import types
import time


username = ''
status = ''

p = Thread(target=zakaz_bot.start_bot)
s = Thread(target=shablon_bot.start_bot)


bot = tBot.TeleBot('6348191193:AAEU8-wPWAk_WT22JEvzXqzx3hrp3-3XzBU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['admin'])
def admin(message):
    mark = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Список пользователей', callback_data='user_list')
    btn2 = types.InlineKeyboardButton('Лаунчер ботов', callback_data='launcher')

    mark.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Ваши действия:', reply_markup=mark)


@bot.message_handler(commands=['launcher'])
def launch(message):
    mark = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Вкл', callback_data='on')
    btn2 = types.InlineKeyboardButton('Выкл', callback_data='off')
    mark.row(btn1, btn2)

    bot.send_message(message.chat.id, 'Вкл/Выкл?', reply_markup=mark)


@bot.callback_query_handler(func=lambda callback: True)
def call(callback):
    conn = sql.connect('src/users.sql')
    cur = conn.cursor()

    if callback.data == 'user_list':
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        info = ''
        n = 0

        for el in users:
            n += 1
            info += f'''{n})ID: {el[0]}
Имя: {el[1]}
Username: {el[2]}\n'''
        bot.send_message(callback.message.chat.id, info)
    elif callback.data == 'launcher':
        bot.send_message(callback.message.chat.id, 'Отправь /launcher')
    elif callback.data == 'on':
        bot.send_message(callback.message.chat.id, 'Готово!')
        s.start()
        p.start()
        s.join()
        p.join()
    elif callback.data == 'off':
        s.exit()
        p.exit()
    else:
        bot.send_message(callback.message.chat.id, 'Ты чего это тут шалишь? Взломать меня хотел лошок петушок')
        bot.kick_chat_member(callback.message.id, callback.message.from_user.id)


print('Main online')


bot.infinity_polling()
