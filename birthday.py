import asyncio
import os
from telethon import TelegramClient, events, Button, sync
from telethon import utils
from dotenv import load_dotenv
import datetime
from convert_line_from_mysql import convert_line_for_print, choise_person, reminder
import requests
import json
import aiocron
import logging


load_dotenv()
'""date for telegram"'
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

"""date for connect backendless"""
REAST_ID = os.getenv('REAST_ID')
DATABASE = os.getenv('DATABASE')
APLICATION_ID = os.getenv('APLICATION_ID')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
DOMAIN ='https://api.backendless.com'

@bot.on(events.NewMessage(pattern='/help'))
async def send_welcome(message):
    """ This function can send discription information"""
    user = message.chat.first_name
    me = (await bot.get_me()).first_name
    await message.reply(f'Привет, {user}! Я {me} бот. \nI can remember the birthdays'+ \
     '\n\t/delete - command will delete entries' + \
     '\n\t/list - command will show your entries'  + \
     '\n\t/add - command will add new entries' +\
     '\n\t I can also remind you of your birthdays every day at 9:30'   ) 
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/add'))
async def add_data(event):
    """This function can add new person to list"""
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Let\'s get started. What is his or her name?')
        firstname_ = (await conv.get_response()).raw_text
        while not any(n.isalpha() for n in firstname_.strip(' ')):
            await conv.send_message(f"last name need have only letters! Tru again!") 
            firstname_ = (await conv.get_response()).raw_text
        
        await conv.send_message('Now write your last name')
        lastname_ = (await conv.get_response()).raw_text
        while not any(l.isalpha() for l in lastname_.strip(' ')):
            await conv.send_message("last name need have only letters! Tru again")
            lastname_ = (await conv.get_response()).raw_text

        await conv.send_message(f'Send your date of birth in the format <DD.MM.YYYY>')
        date = (await conv.get_response()).raw_text
        while  any(d.isalpha() for d in date.strip(' ')):
            await conv.send_message(f'Not correct format, let\'s you try agan')
            date = (await conv.get_response()).raw_text
                        
        sender = await event.get_sender()
        user = conv.input_chat.user_id
        id_person = 0
        id_person+=1
        url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}"
        user_text ={
            "firstname":f"{firstname_}",
            "lastname":f"{lastname_}",
            "date_birthday":f"{date}",
            "user_id":f"{user}",
            "id":id_person
            }
        text_for_message = requests.post(url, json=user_text)
        await conv.send_message(f'{sender.first_name}, Your data was added successfully!')
        raise events.StopPropagation

      
@bot.on(events.NewMessage(pattern='/list'))
async def show_list(list):
    """This fuction can send message with all your persons"""
    sender = list.input_chat.user_id
    url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}?where=user_id%20%3D%20'{sender}'&property=date_birthday&property=lastname&property=firstname"
    response = requests.request('GET',url)
    text_from_db = ''
    async with bot.conversation(list.chat_id) as conv:
        conv.parse_mode = None
        if not response.json():
            await conv.send_message(f'List is empty!')
        else:
            text_from_db= convert_line_for_print(response)
        await conv.send_message(f'Here\'s what I could find: \n{text_from_db}')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/delete'))
async def delete_line(event):
    """This function can delete row with information about person from list """
    async with bot.conversation(event.chat_id) as rows:
        await rows.send_message(f'Are you want delete entries? You need to enter the last name of the person from the list')
        lastname_ = (await rows.get_response()).raw_text
        url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}?where=lastname%3D'{lastname_}'"
        response = requests.request('GET', url)
        edited_text = ''
        if len(json.loads(response.text))==1:
            url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/bulk/{DATABASE}?where=lastname%3D'{lastname_}'"
            requests.delete(url)
            await rows.send_message(f'Your record was successfully deleted!')
        elif len(json.loads(response.text))>1:
            edited_text = choise_person(response)
            await rows.send_message(f'I found:\n{edited_text}')
            id_person = (await rows.get_response()).raw_text
            url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/bulk/{DATABASE}?where=id%3D{id_person}"
            requests.delete(url)
            await rows.send_message(f'Your record was successfully deleted!')
        else:
            await rows.send_message(f'Not found this last name')
        raise events.StopPropagation

time = '30 9 * * *'
@aiocron.crontab(time)
async def attime():
    logging.basicConfig(filename='file.log', level=logging.INFO, format="%(levelname)s %(asctime)s %(message)s")
    users_bot = set()
    url = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}?property=user_id"
    response_user_id = requests.request('GET',url)
    for user_id in json.loads(response_user_id.text):
        users_bot.add(int(user_id['user_id']))
    for user in users_bot:
        sort_by_user = f"{DOMAIN}/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}?where=user_id%3D'{user}'&property=date_birthday&property=firstname"
        response_date = requests.request('GET',sort_by_user)
        message = reminder(response_date)
        if message!=None and len(message)!=0:
            try:
                entity = await bot.get_entity(user)
                await bot.send_message(entity, message)
            except Exception as e:
                error = "{0} - user_id = {1}".format(e,user)
                logging.error(error)

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
