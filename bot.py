import time
from aiogram import Bot, Dispatcher, types, F
import asyncio

API_TOKEN = '7135501225:AAHcNOZIwYNkqEXE3JMWwjU2pRXAY9AJb64'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
Admins = ["2081653463", "6067700910", "6559971529"]
Spam_Dict = ["вирты","виртуальную ","пабг","голда ","аккаунт","акк", "набор","виртuальную", "валютu"]
Whitelist = ["обмен","обменяю", "продажа", "продам", "торг","куплю","купить","покупка","обман","скам","семью", "семья", "фама", "фаму", "заскамил","обманул","кинул", "кидок","скамер","мошенник","чс"]

@dp.message(F.text)
async def get_id_command_handler(message: types.Message):
    is_admin = False
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admin in chat_admins:
        if admin.user.id == message.from_user.id:
            is_admin = True
            break
    if is_admin == False:
        is_spam = True
        sentence = str(message.text).lower()
        word_list = sentence.split()
        topic_id = message.message_thread_id if message.is_topic_message else 1
        if topic_id == 1:
            for i in range(len(word_list)):
                if word_list[i] in Spam_Dict: 
                    await message.delete()
                    answer = await message.answer("Сообщение удалено")
                    await bot.delete_message(answer.chat.id, answer.message_id)
        else:
            for i in range(len(word_list)):
                if word_list[i] in Whitelist:
                    is_spam = False
                elif word_list[i] in Spam_Dict:
                    await message.delete()
                    answer = await message.answer("Сообщение удалено")
                    time.sleep(3)
                    await bot.delete_message(answer.chat.id, answer.message_id)
            if is_spam != False:
                await message.delete()
                answer = await message.answer("Сообщение удалено")
                time.sleep(30)
                await bot.delete_message(answer.chat.id, answer.message_id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())