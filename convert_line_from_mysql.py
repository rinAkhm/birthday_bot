
import datetime

def convert_from_mysql(mysql):
    #mysql = [(1, None, 'Ахметзянов', 'Рушан', datetime.date(2002, 9, 5)), (2, None, 'Ахметзянов', 'ати', datetime.date(1964, 9, 20))]
    """ Функция приобразует данные из в строковый формат"""
    edited_line = ''
    for i in mysql:
        for j in range (len(i)):
            if j%4 == 0 and j!=0:
                edited_line = edited_line + '{0} \n'.format(str(i[j]))
            elif j%5==0:
                edited_line = edited_line +'{0}. '.format(str(i[j])) 
            else:
                edited_line = edited_line +'{0} '.format(str(i[j])) 
    return edited_line


mysql = [(1, None, 'Ахметзянов', 'Рушан', datetime.date(2002, 9, 5)), (2, None, 'Ахметзянов', 'ати', datetime.date(1964, 9, 20))]
print (select_from_mysql(mysql))