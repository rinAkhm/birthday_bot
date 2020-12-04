
import datetime
import json

def convert_line_for_print(text):
    """ Fuction return edited message"""
    edited_line = '' 
    #{'___class': 'birthday', 'date_birthday': '17.112020', 'firstname': 'hello', 'lastname': 'itsme'}
    count = 0

    # for i in range(len(text))
    for line in range(len(text)):
        word += text.json()[line]
    print (word)
            # if i[j]%2 == 0 and i[j]!=0:
            #     pass
            # #edited_line = edited_line + '{0}-{1}-{2}\n'.format((date[8:10]),(date[5:7]),(date[0:4]))
            # if i%3==0:
            #     edited_line = edited_line + [i]['firstname']
            # else:
            #     pass
            # #edited_line = edited_line +'{0} '.format(str(i[j])) 
    return edited_line


# def convert_line_for_delete(mysql):
#     """ Fuction return edited message"""
#     edited_line = ''
#     for list_ in mysql:
#         for tuple_ in range (len(list_)):
#             if tuple_%2 == 0 and tuple_!=0:
#                 edited_line = edited_line + '/ user ID = {0}\n'.format(list_[tuple_]) 
#             else:
#                 edited_line = edited_line +'{0} '.format(list_[tuple_])
#     return edited_line


if __name__ == "__main__":
    text = [{'___class': 'birthday', 'date_birthday': '17.112020', 'firstname': 'hello', 'lastname': 'itsme'}]


    convert_line_for_print(text)