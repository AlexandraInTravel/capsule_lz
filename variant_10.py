#это бибилиотеки для работы с данными, системой, графиками, датами
import getpass
import datetime 
import pandas as pd
import os
import matplotlib.pyplot as plt
from log import logs

class Oil(): #класс оил
    @logs
    def __init__(self): 
        self.Crude_DataFrame = pd.read_csv('crude-oil-price.csv') #здесь загружаем файлы
        self.Brent_DataFrame = pd.read_csv('BrentOilPrices.xls')

    def gr(self):
        for i in range(0, len(self.Crude_DataFrame)): #Цикл по всем строкам таблицы Crude
            d_str = self.Crude_DataFrame.loc[i, 'date']
            self.Crude_DataFrame.loc[i, 'date'] = d_str[0 : 10]

        for i in range(0, 3200): #изменение дат
            str1 = self.Brent_DataFrame.loc[i, 'date']
            data1 = str1.split('-')
            y = '19' + data1[2]
            m = data1[1]
            d = data1[0]
            if m == 'Jan': m = "01"
            elif m == 'Feb': m = "02"
            elif m == 'Mar': m = "03"
            elif m == 'Apr': m = "04"
            elif m == 'May': m = "05"
            elif m == 'Jun': m = "06"
            elif m == 'Jul': m = "07"
            elif m == 'Aug': m = "08"
            elif m == 'Sep': m = "09"
            elif m == 'Oct': m = "10"
            elif m == 'Nov': m = "11"
            elif m == 'Dec': m = "12"
            self.Brent_DataFrame.loc[i, 'date'] = datetime.date(int(y), int(m), int(d)) #заменяем

        for i in range(3200, 8360):
            str11 = self.Brent_DataFrame.loc[i, 'date']
            data1 = str11.split('-')
            y = '20' + data1[2]
            m = data1[1]
            d = data1[0]
            if m == 'Jan': m = "01"
            elif m == 'Feb': m = "02"
            elif m == 'Mar': m = "03"
            elif m == 'Apr': m = "04"
            elif m == 'May': m = "05"
            elif m == 'Jun': m = "06"
            elif m == 'Jul': m = "07"
            elif m == 'Aug': m = "08"
            elif m == 'Sep': m = "09"
            elif m == 'Oct': m = "10"
            elif m == 'Nov': m = "11"
            elif m == 'Dec': m = "12"
            self.Brent_DataFrame.loc[i, 'date'] = datetime.date(int(y), int(m), int(d))

        for i in range(8360, len(self.Brent_DataFrame)):
            str2 = self.Brent_DataFrame.loc[i, 'date']
            data2 = str2.split(' ')
            m = data2[0]
            d = data2[1][0:2]
            y = data2[2]
            if m == 'Jan': m = "01"
            elif m == 'Feb': m = "02"
            elif m == 'Mar': m = "03"
            elif m == 'Apr': m = "04"
            elif m == 'May': m = "05"
            elif m == 'Jun': m = "06"
            elif m == 'Jul': m = "07"
            elif m == 'Aug': m = "08"
            elif m == 'Sep': m = "09"
            elif m == 'Oct': m = "10"
            elif m == 'Nov': m = "11"
            elif m == 'Dec': m = "12"
            self.Brent_DataFrame.loc[i, 'date'] = datetime.date(int(y), int(m), int(d))

        self.merged_DataFrame = pd.concat([self.Brent_DataFrame, self.Crude_DataFrame], axis=0) #объединение двух таблиц
        print(self.merged_DataFrame) #вывод

        x_axis = self.merged_DataFrame['date'].tolist() #это даты для оси X
        y_price1 = self.merged_DataFrame['price1'].tolist() #цены первой нефти для оси Y
        y_price2 = self.merged_DataFrame['price2'].tolist() #цены второй нефти для оси Y
        plt.plot(x_axis, y_price1, label='Crude') #здесь строим график
        plt.plot(x_axis, y_price2, label='Brent')
        plt.title('Стоимость барреля нефти')
        plt.legend()
        plt.show()

    def __del__(self): #деструктор
        print("del done")

