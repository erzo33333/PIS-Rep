class Product:
    """
    Основной класс, отвечающий за неклассифицированные продукты
    """
    def __init__(self, name, amount, date, calories):
        self.name = name
        self.date = date
        self.amount = amount
        self.calories = calories

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Item:
    """
    Класс, дублирующий Product
    """
    def __init__(self, name: str, date: str, amount:int):
        self.name = name
        self.amount = amount
        self.date = date

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество:{self.amount}'


class Potato(Product):
    """
    Класс картошки, наслдуемый от Product
    """
    def __init__(self, name, isdirty, amount, date, calories):
        super().__init__(name, amount, date, calories)
        self.isdirty = isdirty

    def __str__(self):
        return f'Название: {self.name}, Грязь:{self.isdirty}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Carrot(Product):
    """
    Класс моркови, наслдуемый от Product
    """
    def __init__(self, name, length, amount, date, calories):
        super().__init__(name, amount, date, calories)
        self.length = length

    def __str__(self):
        return f'Название: {self.name}, Длина:{self.length}, Дата:{self.date}, Количество:{self.amount}, Калорийность: {self.calories}'


class Berry(Item):
    """
    Класс ягоды, наслдуемый от Item
    """
    def __init__(self, name, size, amount, date):
        super().__init__(name, date, amount)
        self.size = size

    def __str__(self):
        return f'Название: {self.name}, Дата:{self.date}, Количество: {self.amount}, Размер:{self.size}'