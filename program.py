from classes import Product, Potato, Carrot, Berry, Shop
import os
from keyboard import wait
from msvcrt import getch

shop = Shop()

ProductList = [{'name': "Баклажан", 'amount':10, 'calories':50},
               {'name': "Фейхоа", 'amount':3, 'calories':59},
               {'name': "Огурец", 'amount':320, 'calories':15}]

PotatoList = [{'name': "Красная картошка",'isdirty':True, 'amount':250, 'calories':70},
              {'name': "Белая картошка", 'isdirty':False, 'amount':300, 'calories':77},
              {'name': "Синяя картошка", 'isdirty':False, 'amount':50, 'calories':80}]

CarrotList = [{'name': "Анастасия", 'length':23, 'amount':140, 'calories':40},
              {'name': "Московская Зимняя", 'length':14, 'amount':100, 'calories':39},
              {'name': "Самсон", 'length':20, 'amount':97, 'calories':42}]

BerryList = [{'name': "Арбуз", 'size':37, 'amount':104},
             {'name': "Малина", 'size':1, 'amount':22},
             {'name': "Банан", 'size':20, 'amount':95}]



run = True
while run:
    os.system('cls')
    chose = input('Выберете действие:\n'
          '1. Добавить товар\n'
          '2. Удалить товар\n'
          '3. Посмотреть список товаров\n'
          '0. Завершить работу\n')

    match (chose):
        case '1':
            try:
                addtype = input('Введите тип товара для добавления:\n'
                                '1. Картофель\n'
                                '2. Морковь\n'
                                '3. Ягода\n'
                                '* Другое\n')

                if addtype == '1':
                    addname = input('Название: ')
                    addamount = input('Количество: ')
                    addisdirty = input('Грязь: ')
                    addcalories = input('Калорийность: ')
                    shop.AddItem(addtype, name=addname, amount=addamount, calories=addcalories, isdirty=addisdirty)

                elif addtype == '2':
                    addname = input('Название: ')
                    addamount = input('Количество: ')
                    addlength = input('Длина: ')
                    addcalories = input('Калорийность: ')
                    shop.AddItem(addtype, name=addname, amount=addamount, calories=addcalories, length=addlength)

                elif addtype == '3':
                    addname = input('Название: ')
                    addamount = input('Количество: ')
                    addsize = input('Размер: ')
                    shop.AddItem(addtype, name=addname, amount=addamount, size=addsize)

                else:
                    addname = input('Название: ')
                    addamount = input('Количество: ')
                    addcalories = input('Калорийность: ')
                    shop.AddItem(addtype, name=addname, amount=addamount, calories=addcalories)

                print('Успешно добавлено!')
            except ValueError as e:
                print(f'Ошибка: {e}')

        case '2':
            try:
                if not shop.goods:
                    print("В магазине нет товаров для удаления")
                else:
                    print(shop)
                    index = int(input('Введите индекс товара для удаления: '))
                    shop.RemoveItem(index)
                    print('Удаление прошло успешно!')
            except (ValueError, IndexError) as e:
                print(f'Ошибка при удалении: {e}')

        case '3':
            print(shop)

        case '0':
            run = False
            break

        case _:
            print('Неправильно выбрано действие')

    print('\nНажмите пробел, чтобы продолжить')
    wait('space')
    getch()