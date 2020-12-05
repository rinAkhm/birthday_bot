
from datetime import datetime
import json


def convert_line_for_print(respone:'response')->str:
    """ Function return /list with edited message"""
    edited_line = '' 
    count = 0
    text = json.loads(respone.text)
    for row in text:
        count+=1
        date = datetime.strptime(row['date_birthday'], "%d.%m.%Y")  
        edited_line+= '\t{0}. \t{1} \t{2} - {3}\n'.format(count, row['firstname'],row['lastname'], 
                        datetime.strftime(date, '%e %b %Y'))
    return edited_line


def choise_person(respone:'response')->str:
    """Function return message for delete row"""
    edited_line = ''
    text = json.loads(respone.text)
    for row in text:
        edited_line+= 'ID= {0} - {1} {2}\n'.format(row['id'],row['firstname'],row['lastname'])
    return edited_line 


def calc_year(date_birthday:str)->int:
    """Function return number of years the person"""
    return int(datetime.today().strftime('%Y')) - int(date_birthday) 


def reminder(respone_date:'response')->str:
    """Function return message if today is person's birthday"""
    message = '' 
    for row in json.loads(respone_date.text):                
        temp_date = datetime.strptime(row['date_birthday'], '%d.%m.%Y')
        today = datetime.today().strftime('%d.%m')
        date_birthday = datetime.strftime(temp_date, "%d.%m") 
        if today == date_birthday:
            years = datetime.strftime(temp_date, '%Y')
            age = calc_year(years)
            message += "Today is {0}\'s birthday.{1} years old\n".format(row['firstname'],age)
    return message