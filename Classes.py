class Product:
    def __init__(self, name, amount, date, calories):
        self.name = name
        self.date = date
        self.amount = amount
        self.calories = calories

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Item:
    def __init__(self, name: str, date: str, amount:int):
        self.name = name
        self.amount = amount
        self.date = date

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}'


class Potato(Product):
    def __init__(self, name, variety, amount, date, calories):
        super().__init__(name, amount, date, calories)
        self.variety = variety

    def __str__(self):
        return f'Название: {self.name}, Сорт:{self.variety}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Carrot(Product):
    def __init__(self, name, length, amount, date, calories):
        super().__init__(name, amount, date, calories)
        self.length = length

    def __str__(self):
        return f'Название: {self.name}, Длина:{self.length}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Berry(Item):
    def __init__(self, name, size, amount, date):
        super().__init__(name, date, amount)
        self.size = size

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество: {self.amount}, Размер:{self.size}'


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