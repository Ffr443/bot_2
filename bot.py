import asyncio
import telebot
from telebot.async_telebot import AsyncTeleBot
import difflib
import json
import datetime

API_TOKEN = '7135501225:AAHcNOZIwYNkqEXE3JMWwjU2pRXAY9AJb64'

bot = AsyncTeleBot(API_TOKEN)
Admins = ["2081653463", "6067700910", "6559971529"]
Spam_Dict = ["вирты", "виртуальную ", "пабг", "голда ", "аккаунт", "акк", "виртuальную", "валюту"]
Whitelist = ["обмен", "обменяю", "продажа", "продам", "торг", "куплю", "купить", "набор", "покупка", "обман", "скам",
             "семью", "семья", "фама", "фаму", "заскамил", "обманул", "кинул", "кидок", "скамер", "мошенник", "чс"]

LOG_FILE = "deleted_messages.json"

async def log_deleted_message(reason, message):
    log_entry = {
        "deleted_info": reason,
        "content_message": {
            "message_id": message.message_id,
            "from_user": {
                "id": message.from_user.id,
                "username": message.from_user.username,
                "first_name": message.from_user.first_name,
                "last_name": message.from_user.last_name
            },
            "chat": {
                "id": message.chat.id,
                "title": message.chat.title,
                "type": message.chat.type
            },
            "date": message.date,
            "text": message.text
        }
    }
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

async def process_message(message):
    is_admin = False
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admin in chat_admins:
        if admin.user.id == message.from_user.id:
            is_admin = True
            break
    if not is_admin:
        is_spam = True
        sentence = str(message.text).lower()
        word_list = sentence.split()
        topic_id = message.message_thread_id if message.is_topic_message else 1

        # Проверка на наличие "https", "/", "t.me" и "@"
        if "https" in sentence or "/" in sentence or "t.me" in sentence or "@" in sentence:
            await bot.delete_message(message.chat.id, message.message_id)
            answer = await bot.send_message(message.chat.id, f"Сообщение содержащее ссылку от @{message.from_user.username} удалено")
            await asyncio.sleep(3)
            await bot.delete_message(answer.chat.id, answer.message_id)
            await log_deleted_message("Ссылка", message)
            return

        if topic_id == 1:
            for word in word_list:
                if difflib.get_close_matches(word, Spam_Dict, n=1, cutoff=0.8):
                    await bot.delete_message(message.chat.id, message.message_id)
                    answer = await bot.send_message(message.chat.id, f"Сообщение со спамом от @{message.from_user.username} удалено")
                    await asyncio.sleep(3)
                    await bot.delete_message(answer.chat.id, answer.message_id)
                    await log_deleted_message("Спам", message)
                    break
        else:
            for word in word_list:
                if difflib.get_close_matches(word, Whitelist, n=1, cutoff=0.8):
                    is_spam = False
                elif difflib.get_close_matches(word, Spam_Dict, n=1, cutoff=0.8):
                    await bot.delete_message(message.chat.id, message.message_id)
                    answer = await bot.send_message(message.chat.id, f"Сообщение от @{message.from_user.username} удалено")
                    await asyncio.sleep(3)
                    await bot.delete_message(answer.chat.id, answer.message_id)
                    await log_deleted_message("Спам", message)
                    break
            if is_spam:
                await bot.delete_message(message.chat.id, message.message_id)
                answer = await bot.send_message(message.chat.id, f"Сообщение со спамом от @{message.from_user.username} удалено")
                await asyncio.sleep(30)
                await bot.delete_message(answer.chat.id, answer.message_id)
                await log_deleted_message("Спам", message)

@bot.message_handler(func=lambda message: True)
async def get_id_command_handler(message):
    asyncio.create_task(process_message(message))

async def main():
    await bot.polling(none_stop=True)

if __name__ == "__main__":
    asyncio.run(main())
