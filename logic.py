from classes import Product, Potato, Carrot, Berry
from errors import *

def safe_get(dic: dict, key: str):
    """
    Возвращает значение или бросает ошибку, если ключа нет.
    """
    if key not in dic:
        raise FieldMissingError(f"В исходных данных отсутствует обязательное поле: {key}")
    return dic[key]

def Product_Parsing(pl):
    """
    Функция разделения неклассифицированных продуктов из текстового файла и вывода их в консоль
    """
    allProducts = []
    allProductsString = "\n  Список добавленных продуктов:"

    for product in pl:
        try:
            newobj = Product(name=safe_get(product, 'name'), date=safe_get(product, 'date'), amount=safe_get(product, 'amount'), calories=safe_get(product, 'calories'))
            allProducts.append(newobj)
            allProductsString += f"\n{newobj}"
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении \'{product['name']}\'. {e}.')
        except FieldMissingError as e:
            print(f'\nОшибка при добавлении \'{product}\'. {e}.')

    print(allProductsString)


def Potato_Parsing(pl):
    """
    Функция десериализации картофеля из списка словарей в объекты и вывод их в консоль
    """
    allPotato = []
    allPotatoString = "\n  Список добавленной картошки:"

    for potato in pl:
        try:
            newobj = Potato(name=safe_get(potato, 'name'), isdirty=safe_get(potato, 'isdirty'), date=safe_get(potato, 'date'), amount=safe_get(potato, 'amount'), calories=safe_get(potato, 'calories'))
            allPotato.append(newobj)
            allPotatoString += f"\n{newobj}"
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении \'{potato['name']}\'. {e}.')
        except FieldMissingError as e:
            print(f'\nОшибка при добавлении \'{potato}\'. {e}.')

    print(allPotatoString)


def Carrot_Parsing(cl):
    """
    Функция разделения моркови из текстового файла и вывода её в консоль
    """
    allCarrot = []
    allCarrotString = "\n  Список добавленной моркови:"

    for carrot in cl:
        try:
            newobj = Carrot(name=safe_get(carrot, 'name'), length=safe_get(carrot, 'length'), date=safe_get(carrot, 'date'), amount=safe_get(carrot, 'amount'), calories=safe_get(carrot, 'calories'))
            allCarrot.append(newobj)
            allCarrotString += f"\n{newobj}"
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении \'{carrot['name']}\'. {e}.')
        except FieldMissingError as e:
            print(f'\nОшибка при добавлении \'{carrot}\'. {e}.')

    print(allCarrotString)


def Berry_Parsing(bl):
    """
    Функция разделения ягод из текстового файла и вывода их в консоль
    """
    allBerry = []
    allBerryString = "\n  Список добавленных ягод:"

    for berry in bl:
        try:
            newobj = Berry(name=safe_get(berry, 'name'), size=safe_get(berry,'size'), date=safe_get(berry, 'date'), amount=safe_get(berry, 'amount'))
            allBerry.append(newobj)
            allBerryString += f"\n{newobj}"
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении \'{berry['name']}\'. {e}.')
        except FieldMissingError as e:
            print(f'\nОшибка при добавлении \'{berry}\'. {e}.')

    print(allBerryString)


def AddItem(type, name, special, date, amount, calories=0):
    if type == '1':
        try:
            newobj = Potato(name=name, isdirty=special, date=date, amount=amount, calories=calories)
            return newobj
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении. {e}.')

    elif type == '2':
        try:
            newobj = Carrot(name=name, length=special, date=date, amount=amount, calories=calories)
            return newobj
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении. {e}.')

    elif type == '3':
        try:
            newobj = Berry(name=name, size=special, date=date, amount=amount)
            return newobj
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении. {e}.')

    elif type == '4':
        try:
            newobj = Product(name=name, date=date, amount=amount, calories=calories)
            return newobj
        except (FieldTypeError) as e:
            print(f'\nОшибка при добавлении. {e}.')

    else:
        return f'Невозможно добавить предмет несуществующего типа'
