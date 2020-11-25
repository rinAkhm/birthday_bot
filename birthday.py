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

# @bot.on(events.NewMessage(pattern='/start'))
# async def start(event):
#     """Send a message when the command /start is issued."""
#     await event.respond('Right now the reminder is set to 8:00 pm')
#     raise events.StopPropagation
 
# @bot.on(events.NewMessage(pattern="Yup"))
# @bot.on(events.NewMessage(pattern="/doit"))
# async def reflect(event):

#     async with bot.conversation(event.chat_id) as conv:
#         await conv.send_message('Lesson of the day?')
#         q_1 = (await conv.get_response()).raw_text

#         await conv.send_message('One thing I want to change?')
#         q_2 = (await conv.get_response()).raw_text
        
#         await conv.send_message('Am I getting closer to my goals?')
#         q_3 = (await conv.get_response()).raw_text

#         await conv.send_message('Well done!')
#         await conv.send_message(f'Quote of the day: \n {quotes.get_quote()}')

#         to_gg_sheets.append_record([q_1,q_2,q_3])


# @bot.on(events.NewMessage())
# async def send_welcome(event):
    # me = bot.get_entity('me')
    # print(utils.get_display_name(me))
@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    me = event.chat_id
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Hi!')
        hello = await (conv.get_response())

        await conv.send_message('Please tell me your name ')
        name = (await conv.get_response()).raw_text
        
        while not any(x.isalpha() for x in name):
            await conv.send_message("Your name didn't have any letters! Try again")
            name = (await conv.get_response()).raw_text
        await conv.send_message(f'Thanks, {name}!')
        # await conv.send_message('Thanks {}!'.format(name))

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
  
    


