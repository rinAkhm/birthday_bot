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

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(message):
    user = message.chat.first_name
    me = (await bot.get_me()).username
    await message.reply(f'Привет, {user}! \nЯ {me} бот могу хранить информацию о дня рождениях твоих знакомых.') 
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/add'))
async def registred_data(event):
    async with bot.conversation(event.chat_id) as conv:
        
        await conv.send_message('Напиши Фамилию')
        lastname_ = (await conv.get_response()).raw_text
        while not any(l.isalpha() for l in lastname_.strip(' ')):
            await conv.send_message("Фамилия должно содержать только буквы. Попробуй еще раз!")
            lastname_ = (await conv.get_response()).raw_text
        # запись в бд фамилии 

        await conv.send_message('Теперь напиши Имя')
        firstname_ = (await conv.get_response()).raw_text
        while not any(n.isalpha() for n in firstname_.strip(' ')):
            await conv.send_message(f"Имя должно содеражать только буквы. Попробуй еще раз!") 
            firstname_ = await (conv.get_response()).raw_text
        #запись в бд имени 
        
        await conv.send_message(f'Напиши дату рождения в виде "17.11.1995"')
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






















#     # conv.send_message('Hi!')
#     # hello = conv.get_response()

#     # conv.send_message('Please tell me your name')
#     # name = conv.get_response().raw_text
#     # while not any(x.isalpha() for x in name):
#     #     conv.send_message("Your name didn't have any letters! Try again")
#     #     name = conv.get_response().raw_text

#     # conv.send_message('Thanks {}!'.format(name))


# @bot.on(events.NewMessage(pattern='/r'))
# async def registred(event):
#     await event.respond("Напиши свою фамилию:" )
#     lastname = event.get_response().raw_text
#     print(lastname)



# #     await find_new_message(event)
    
  

# # @bot.on(events.NewMessage)
# # async def find_new_message(event):
# #     msg = await event.message.message
# #     print(msg)
# #     return msg
    


# def main():
#     """Start the bot."""
#     bot.run_until_disconnected()

# if __name__ == '__main__':
#     main()
  
    


