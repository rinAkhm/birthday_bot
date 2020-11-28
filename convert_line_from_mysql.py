
import datetime

def convert_line_for_print(mysql):
    #mysql = [(1, None, 'Ахметзянов', 'Рушан', datetime.date(2002, 9, 5)), (2, None, 'Ахметзянов', 'ати', datetime.date(1964, 9, 20))]
    """ Fuction return edited message"""
    edited_line = ''
    count = 0
    for i in mysql:
        count+=1
        for j in range (len(i)):
            if j%2 == 0 and j!=0:
                date = str(i[j])
                edited_line = edited_line + '{0}-{1}-{2}\n'.format((date[8:10]),(date[5:7]),(date[0:4]))
            elif j%3==0:
                edited_line = edited_line +'{0}. {1} '.format(count,str(i[j])) 
            else:
                edited_line = edited_line +'{0} '.format(str(i[j])) 
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