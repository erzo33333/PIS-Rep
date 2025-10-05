class Product:
    def __init__(self, name, amount, date):
        self.name = name
        self.date = date
        self.amount = amount

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}'


class Item:
    def __init__(self, name: str, date: str, amount:int):
        self.name = name
        self.date = date
        self.amount = amount

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}'


class Potato(Product):
    def __init__(self, name, amount, date, variety):
        super().__init__(name, amount, date)
        self.variety = variety


class Carrot(Product):
    def __init__(self, name, amount, date, length):
        super().__init__(name, amount, date)
        self.length = length


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f'не задана функция вывода'