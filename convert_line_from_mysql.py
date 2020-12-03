
import datetime
import json

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


def convert_line_for_delete(mysql):
    """ Fuction return edited message"""
    edited_line = ''
    for list_ in mysql:
        for tuple_ in range (len(list_)):
            if tuple_%2 == 0 and tuple_!=0:
                edited_line = edited_line + '/ user ID = {0}\n'.format(list_[tuple_]) 
            else:
                edited_line = edited_line +'{0} '.format(list_[tuple_])
    return edited_line


if __name__ == "__main__":
    text = [{'___class': 'birthday', 'date_birthday': '17.112020', 'firstname': 'hello', 'lastname': 'itsme'}]


    convert_line_for_print(text)