# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения: stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
# Напишите функцию, которая проверяет эти даты на корректность. Т. е. для каждой даты возвращает True (дата корректна) или False (некорректная дата).

from datetime import datetime
stream = ['2018-04-02', '2018-02-29', '2018-19-02']
# stream = input().split()
def check_format(str_):
    for str_date in str_:
        try:
            valid_date = datetime.strptime(str_date, '%Y-%m-%d')
            print(str_date,'True (дата корректна)')
        except:
            print(str_date,'False (некорректная дата)')

check_format(stream)
