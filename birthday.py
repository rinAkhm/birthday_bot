import asyncio
import os
from telethon import TelegramClient, events
from telethon import utils 
from telethon import sync


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
token = os.getenv('BOT_TOKEN')



bot = TelegramClient('session', 2451630, 'b66dee9617bb120c360cf425be242617').start(bot_token='869898595:AAFHVn9B6zA1VCxKj1T8psT0Snns8K7lZAY')


@bot.on(events.NewMessage())
async def send_welcome(event):
    me = bot.get_entity('me') #384511665
    print(utils.get_display_name(me))
    with event.conversation(chat_id) as conv:
        bot.send_message('Hi!')
        hello = conv.get_response()

        conv.send_message('Please tell me your name')
        name = conv.get_response().raw_text
        while not any(x.isalpha() for x in name):
            conv.send_message("Your name didn't have any letters! Try again")
            name = conv.get_response().raw_text

        conv.send_message('Thanks {}!'.format(name))
# me= bot.get_entity('me')
# print(utils.get_display_name(me))
# msg = 'hello'
# bot.send_message(msg, me)


# @bot.on(events.NewMessage)
# async def all(event):
#     try:
#         print(event.message)
#     except Exception as e:



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
  
    


