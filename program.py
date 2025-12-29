"""
Модуль исполнения программы в иде консольного приложения.
Рекомендуется запускать в термнале.
"""
import os
from msvcrt import getch
from keyboard import wait
from classes import Shop, Product, Potato, Carrot, Berry

shop = Shop()

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
            if not shop.goods:
                print("В магазине нет товаров")
            else:
                print(shop)

        case '0':
            run = False
            break

        case _:
            print('Неправильно выбрано действие')

    print('\nНажмите пробел, чтобы продолжить')
    wait('space')
    getch()