#Нужные библиотеки
import os
import pandas as pd
import datetime

#Декоратор
def logs(func):
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        #Имя пользователя
        user = os.getlogin()
        #Имя функции
        function_name = func.__name__
        #Дата вызова(strftime брала на паре с инета, ссылку не могу найти))
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        #Время вызова
        time = datetime.datetime.now().strftime("%H:%M:%S")
        
        #Проверяем существует ли такой файл
        if os.path.exists("logs.csv"):
            #Существует-читаем
            file = pd.read_csv('logs.csv')
            #Количество строк в файле, чтобы определить следующий id
            id = len(file)
            #Новая строка со всеми данными
            new_row = pd.DataFrame({'id': [id],'pc_username': [user],'function_name': [function_name],'Date in date.month.year': [date],'Time': [time]})
            #Добавляем ее в csv
            new_row.to_csv('logs.csv', mode='a', header=False, index=False)

        else:
            #Если не существует-то записываем новую строку с нулевым id
            df = pd.DataFrame({'id': [0],'pc_username': [user],'function_name': [function_name], 'Date in date.month.year': [date],'Time': [time]})
            #Сохраняем
            df.to_csv('logs.csv', index=False)

        return result
    return wrapper