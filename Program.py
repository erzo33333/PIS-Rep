from Classes import Product, Item, Rectangle, Point

def Prooduct_splitting():

    #prod = input('Введите наименование (вместо пробелов ставьте "_"), дату поступления и количество товара\n')
    prod = 'Картошка 12.09.2025 100'

    while '  ' in prod:
        prod = prod.replace('  ', ' ')

    potato_split = prod.split(' ')

    Potato = Product(name=potato_split[0],
                     date=potato_split[1],
                     amount=potato_split[2])

    print(Potato)

def task1():

    rectangle1 = Rectangle(point1=Point(12, 11),
                           point2=Point(7, 23))

    rectangle2 = Rectangle(point1=Point(4, 13),
                           point2=Point(8, 10))

    new_min_x = min(rectangle1.point1.x, rectangle1.point2.x)
    new_min_y = min(rectangle1.point1.y, rectangle1.point2.y)
    new_max_x = max(rectangle1.point1.x, rectangle1.point2.x)
    new_max_y = max(rectangle1.point1.y, rectangle1.point2.y)

    rectangle1.point1 = Point(new_min_x, new_min_y)
    rectangle1.point2 = Point(new_max_x, new_max_y)

    #далее код не дописан 🤷‍♂️

task1()

Prooduct_splitting()