
from datetime import datetime, timedelta
import datetime as DT
import json
import time

def convert_line_for_print(respone):
    """ Fuction return /list with edited message"""
    edited_line = '' 
    #{'___class': 'birthday', 'date_birthday': '17.112020', 'firstname': 'hello', 'lastname': 'itsme'}
    count = 0
    text = json.loads(respone.text)
    for row in text:
        count+=1
        edited_line+= '{0}. {1} {2} {3}\n'.format(count,row['firstname'],row['lastname'], row['date_birthday'])
    return edited_line


def convert_line_for_delete(respone):
    """ Fuction return IdObject for delete row"""
    edited_line = ''
    count = 0
    text = json.loads(respone.text)
    for row in text:
        count+=1
        edited_line+= '{0}\n'.format(row['objectId'])
    return edited_line


def choise_person(respone):
    """ Fuction return IdObject for delete row"""
    edited_line = ''
    count = 0
    text = json.loads(respone.text)
    for row in text:
        edited_line+= 'ID= {0} - {1} {2}\n'.format(row['id'],row['firstname'],row['lastname'])
    return edited_line

