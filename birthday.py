import asyncio
import os
from telethon import TelegramClient, events, Button
from telethon import utils
from dotenv import load_dotenv
import datetime
from convert_line_from_mysql import convert_line_for_print
#from convert_line_from_mysql import convert_line_for_delete
import requests
import json


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


@bot.on(events.NewMessage(pattern='/help'))
async def send_welcome(message):
    """ This function can send discription information"""
    user = message.chat.first_name
    me = (await bot.get_me()).first_name
    await message.reply(f'Привет, {user}! Я {me} бот. \nI can remember the birthdays'+ \
     '\n/delete - command will delete entries' + \
     '\n/list - command will show your entries'  + \
     '\n/add - command will add new entries') 
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

        await conv.send_message(f'Send your date of birth in the format <DD. MM. YYYY>')
        date = (await conv.get_response()).raw_text
        while  any(d.isalpha() for d in date.strip(' ')):
            await conv.send_message(f'Not correct format, let\'s you try agan')
            date = (await conv.get_response()).raw_text
                        
        sender = await event.get_sender()
        user = conv.input_chat.user_id
        url = f"https://api.backendless.com/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}"
        user_text ={
            "firstname":f"{firstname_}",
            "lastname":f"{lastname_}",
            "date_birthday":f"{date}",
            "user_id":f"{user}"
            }
        text_for_message = requests.post(url, json=user_text)
        await conv.send_message(f'{sender.first_name}, Your data was added successfully!')
        raise events.StopPropagation

      
@bot.on(events.NewMessage(pattern='/list'))
async def show_list(list):
    """This fuction can send message with all your persons"""
    sender = list.input_chat.user_id
    url = f"https://api.backendless.com/{APLICATION_ID}/{REAST_ID}/data/{DATABASE}?where=user_id%20%3D%20'{sender}'&property=date_birthday&property=lastname&property=firstname"
    response = requests.request('GET',url)
    text_from_db = ''
    # i=0
    # a = json.loads( response.text)
    if not response.json():
        await list.reply(f'List is empty!')
    else:
        text_from_db= convert_line_for_print(response)
    await list.reply(f'Result: \n{text_from_db}')
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/delete'))
async def delete_line(event):
    """This function can delete row with information about person from list """
    async with bot.conversation(event.chat_id) as rows:
        await rows.send_message(f'Are you want delete entries? You need Then you need to enter the last name of the person from the list')
        lastname_ = (await rows.get_response()).raw_text
        sql = "SELECT firstname, lastname, ID FROM birthday WHERE lastname = %s"
        # mycursor.execute(sql, lastname_)
        # search_by_lastname = mycursor.fetchall()
        # edited_text = convert_line_for_delete(search_by_lastname) 
        if len(search_by_lastname)==1:
            sql = "DELETE FROM birthday WHERE lastname = %s"
            mycursor.execute(sql,lastname_)
            mydb.commit()
            await rows.send_message(f'Ваша запись успешно удалена!')
            raise events.StopPropagation
        elif len(search_by_lastname)==0:
            await rows.send_message(f'В списке нет такой фамилии')
        else:
            await rows.send_message('Вот что мне удалсь найти по данной фамилии из списка:\n{0}\n'.format(edited_text)+\
                                '\nДля того, чтобы удалить нужного человека отправь его или её ID')
            user_id = ((await rows.get_response()).raw_text,)
            sql = "DELETE FROM birthday WHERE ID = %s"
            mycursor.execute(sql, user_id)
            mydb.commit()
            await rows.send_message(f'Ваша запись успешно удалена!')
            raise events.StopPropagation


def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
    







