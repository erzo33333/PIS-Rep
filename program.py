from classes import Product, Potato, Carrot, Berry
from logic import *
import os

shop = Shop()

shop_acceptance_list = []

ProductList = [{'name': "Баклажан", 'date':"01.11.2025", 'amount':10, 'calories':50},
               {'name': "Фейхоа", 'date':"01.11.2025", 'amount':3, 'calories':59},
               {'name': "Огурец", 'date':"08.11.2025", 'amount':320, 'calories':15}]

PotatoList = [{'name': "Красная картошка",'isdirty':True, 'date':"04.09.2025", 'amount':250, 'calories':70},
              {'name': "Белая картошка", 'isdirty':False, 'date':"03.09.2025", 'amount':300, 'calories':77},
              {'name': "Синяя картошка", 'isdirty':None, 'date':"22.10.2025", 'amount':50, 'calories':80}]

CarrotList = [{'name': "Анастасия", 'length':23, 'date':"30.08.2025", 'amount':140, 'calories':40},
              {'name': "Московская Зимняя", 'length':14, 'date':"17.09.2025", 'amount':100, 'calories':39},
              {'name': "Самсон", 'length':20, 'date':"11.10.2025", 'amount':97, 'calories':42}]

BerryList = [{'name': "Арбуз", 'size':37, 'date':"07.08.2025", 'amount':104},
             {'name': "Малина", 'size':1, 'date':"24.08.2025", 'amount':22},
             {'name': "Банан", 'size':20, 'date':"29.08.2025", 'amount':95}]


while True:
    os.system('cls')
    case = input('1. Добавить продукт\n'
                 '2. Добавить готовый список продуктов\n'
                 '3. Посмотреть список проуктов\n'
                 'Выберите действие: ')
    print('\n')

    if case == '1':
        type = input('1. Картофель\n'
                     '2. Морковь\n'
                     '3. Ягоды\n'
                     '4. Другой продукт\n'
                     'Выберите тип продукта для добавления: ')

    elif case == '2':
        print(222)

    elif case == '3':
        print(333)

    else:
        print('мимо')