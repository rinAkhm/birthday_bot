# Telegam bot not forget birthdays
Telegram bot that records the last name, first name, date of birth, then to remind you of the birthday of your friend, lover or relative.

# Usage
1. Prepare a working directory and execute these commands:
```
git clone https://github.com/rinAkhm/birthday_bot.git
cd birthday_bot

pip install -r requirements.txt
 
echo "API_ID = 
API_HASH = 
BOT_TOKEN = 

REAST_ID = 
DATABASE = 
APLICATION_ID = " > .env
```
2. Register on [telegram.org](https://my.telegram.org/), get a api_id and api_hash then you need create telegram bot at botFather. This [instruction](https://medium.com/@bbsystemscorporation/%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B5-%D1%81-botfather-%D0%B1%D0%BE%D1%82%D0%BE%D0%BC-5c6f74d99a1a)

Now you have `api_id`, `token_bot`, `api_hash` it remains to add to the file `.env` file.

3. For the script to work, you will need to create a cloud database [backendless.com](https://develop.backendless.com) and add data to file .env. 
```
  REAST_ID = "your reast_id" 
  DATABASE = "your name database"
  APLICATION_ID = "your application_id"
```
4. now you can run the script
for example 
```
python birthday.py
```
5. Commands 
```
/help - discription bot 
/add - can add information about a person to the list
/list - send you information about all people
/delete - can delete information about from list
So bot use cron  and can remind you of your birthdays every day at 9:30
```