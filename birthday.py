import asyncio
import os
from telethon import TelegramClient, events
from telethon import utils
from dotenv import load_dotenv
 
load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/help'))
async def send_welcome(message):
    user = message.chat.first_name
    me = (await bot.get_me()).first_name
    await message.reply(f'Привет, {user}! Я {me}. \nЯ умею запоминать дни рождения , которые ты мне пришлешь.'+ \
     '\nОзнакомиться с функционалом  можно при помощи команды /help' + \
     '\nДля того, чтобы добавить новую запись в список нужно написать команду /add и ответить на вопросы, которые пришлет бот.' + \
     '\nВ конце ты получишь сообщение, что запись успешно добавлена.') 
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/add'))
async def registred_data(event):
    async with bot.conversation(event.chat_id) as conv:
        
        await conv.send_message('Давай начнем. Какая фамилия у твоего друга?')
        lastname_ = (await conv.get_response()).raw_text
        while not any(l.isalpha() for l in lastname_.strip(' ')):
            await conv.send_message("Фамилия должно содержать только буквы. Попробуй еще раз!")
            lastname_ = (await conv.get_response()).raw_text
        # запись в бд фамилии 

        await conv.send_message('Как зовут его или её?')
        firstname_ = (await conv.get_response()).raw_text
        while not any(n.isalpha() for n in firstname_.strip(' ')):
            await conv.send_message(f"Имя должно содеражать только буквы. Попробуй еще раз!") 
            firstname_ = await (conv.get_response()).raw_text
        #запись в бд имени 
        
        await conv.send_message(f'Напиши дату рождения в формате "DD.MM.YYYY"')
        date = (await conv.get_response()).raw_text
        #запись в бд
        sender = await event.get_sender()

        #user = conv.sender.first_name #conv._incoming.2.
        await conv.send_message(f'{sender.first_name}, ваши данные были успешно добавлены!')
      

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()














