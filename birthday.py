import asyncio
import os
from telethon import TelegramClient, events, Button
from telethon import utils
from dotenv import load_dotenv
import datetime
from convert_line_from_mysql import convert_line
from connect_db import connection_db
import mysql.connector


load_dotenv()
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
mydb = connection_db()
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

# sql = "INSERT INTO birthday (ID, firstname, lastname, date, id_user) VALUES (%s, %s, %s, %s, %s)"
# val = (22, "John", "Highway", "17.11.2020", 50)
# mycursor.execute(sql, val)
# mydb.commit()
#ID, firstname, lastname, date FROM 
# sql = "SELECT  * FROM birthday  WHERE id_user = %s"
# id = ('50',) 
# mycursor.execute(sql, id)
# result = mycursor.fetchall()

# print(result)    


@bot.on(events.NewMessage(pattern='/help'))
async def send_welcome(message):
    user = message.chat.first_name
    me = (await bot.get_me()).first_name
    await message.reply(f'Привет, {user}! Я {me} бот. \nЯ умею запоминать дни рождения , которые ты мне пришлешь.'+ \
     '\nОзнакомиться с функционалом  можно при помощи команды /help' + \
     '\nДля того, чтобы добавить новую запись в список нужно написать команду /add и ответить на вопросы, которые пришлет бот.' + \
     '\nВ конце ты получишь сообщение, что запись успешно добавлена.') 
    raise events.StopPropagation


@bot.on(events.NewMessage(pattern='/add'))
async def add_data(event):
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Давай начнем. Какая фамилия у твоего друга?')
        lastname_ = (await conv.get_response()).raw_text
        while not any(l.isalpha() for l in lastname_.strip(' ')):
            await conv.send_message("Фамилия должно содержать только буквы. Попробуй еще раз!")
            lastname_ = (await conv.get_response()).raw_text

        await conv.send_message('Как зовут его или её?')
        firstname_ = (await conv.get_response()).raw_text
        while not any(n.isalpha() for n in firstname_.strip(' ')):
            await conv.send_message(f"Имя должно содеражать только буквы. Попробуй еще раз!") 
            firstname_ = await (conv.get_response()).raw_text
        
        await conv.send_message(f'Напиши дату рождения в формате "YYYY.MM.DD"')
        date = (await conv.get_response()).raw_text
        while any(d.isalpha() for d in date.strip(' ')):
            await conv.send_message(f'Не верный формат, попробуй еще раз')
            date = await (conv.get_response()).raw_text
                        
        sender = await event.get_sender()
        user = conv.input_chat.user_id
        sql = "INSERT INTO birthday (firstname, lastname, date, id_user) VALUES (%s, %s, %s, %s)"
        val = (lastname_, firstname_, date, user)
        mycursor.execute(sql, val)
        mydb.commit()
        await conv.send_message(f'{sender.first_name}, ваши данные были успешно добавлены!')
        raise events.StopPropagation

      
@bot.on(events.NewMessage(pattern='/list'))
async def show_list(list):
    sender = (list.input_chat.user_id,)
    sql = "SELECT firstname, lastname, date FROM birthday WHERE id_user = %s"
    mycursor.execute(sql, sender)
    result = mycursor.fetchall()
    line_for_message = convert_line(result)
    await list.reply(f'Результат: \n{line_for_message}')
    raise events.StopPropagation
    


@bot.on(events.NewMessage(pattern='/delete'))
async def delete_line(row):
    await row.send_message(f'Введите номер строки, которую хотите удалить')
    id_user = (await row.get_response()).raw_text
    #user = row.chat.user_id
    mycursor = connection_db()
    sql = ('DELETE FROM birthday WHERE ID = %s')
    mycursor.execute(sql,id_user)
    mycursor = connection_db('save')
    await row.reply(f'Запись успешно удалена!')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
    







