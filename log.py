#иморт библиотек
import os
import pandas as pd
import datetime

#декоратор
def logs(func):
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        #Имя пользователя
        user = os.getlogin()
        #Имя функции
        function_name = func.__name__
        #Дата вызова(strftime)
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        #Время вызова
        time = datetime.datetime.now().strftime("%H:%M:%S")
        
        #Проверяем существует ли такой файл
        if os.path.exists("logs.csv"):
            #если да - читаем
            file = pd.read_csv('logs.csv')
            #Количество строк в файле
            id = len(file)
            #добавляем новую строку
            new_row = pd.DataFrame({'id': [id],'pc_username': [user],'function_name': [function_name],'Date in date.month.year': [date],'Time': [time]})
            #теперь ее в csv
            new_row.to_csv('logs.csv', mode='a', header=False, index=False)
            
        return result #возвращаем
    return wrapper
