
from datetime import datetime, timedelta
import datetime as DT
import json
import time

def convert_line_for_print(respone):
    """ Fuction return /list with edited message"""
    edited_line = '' 
    count = 0
    text = json.loads(respone.text)
    for row in text:
        count+=1
        date = str(row['date_birthday'])[0:10] # берем срез 
        temp_date = datetime.fromtimestamp(int(date)).strftime('%d-%m-%Y') #преобразуем в формат datetime
        date_birthday = datetime.strptime(temp_date, '%d-%m-%Y')+ timedelta(days=1)
        edited_line+= '\t{0}. \t{1} \t{2} - \t{3}\n'.format(count, row['firstname'],row['lastname'], 
                    datetime.strftime(date_birthday, '%e %B %Y'))
    return edited_line


def choise_person(respone):
    """ Fuction return IdObject for delete row"""
    edited_line = ''
    text = json.loads(respone.text)
    for row in text:
        edited_line+= 'ID= {0} - {1} {2}\n'.format(row['id'],row['firstname'],row['lastname'])
    return edited_line

