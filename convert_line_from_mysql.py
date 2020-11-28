
import datetime

def convert_line(mysql):
    #mysql = [(1, None, 'Ахметзянов', 'Рушан', datetime.date(2002, 9, 5)), (2, None, 'Ахметзянов', 'ати', datetime.date(1964, 9, 20))]
    """ Функция приобразует данные из в строковый формат"""
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
# mysql = [('Ахметзянов', 'Рушан', datetime.date(2002, 9, 5)), ('Ахметзянов', 'ати', datetime.date(1964, 9, 20))]
# print(convert_line(mysql))