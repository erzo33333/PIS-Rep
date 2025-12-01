from validation import *
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

class Shop(BaseModel):
    """Модель магазина"""
    goods:list = Field(default=[], description="Список всех товаров в магазине")

    def AddItem(self, type, **kwargs):
        """Добавление товара"""
        types = {'1': Potato,
                 '2': Carrot,
                 '3': Berry}

        if type in types:
            product_class = types[type]
        else:
            product_class = Product

        self.goods.append(product_class(**kwargs))

    def RemoveItem(self, index):
        """Удаление товара по индексу"""
        if 0 <= index < len(self.goods):
            self.goods.pop(index)
        else:
            raise IndexError("Товар с таким индексом не найден")

    def __str__(self):
        goods_str = 'Список всех товаров в магазине:\n'
        for i in range(len(self.goods)):
            goods_str += f'{i}. {self.goods[i]}\n'
        return f'{goods_str}'

class Product(BaseModel, ProductValidation):
    """Основная модель, отвечающая за неклассифицированные продукты"""
    name:str = Field(description="Название продукта")
    amount: float = Field(description="Количество продукта")
    calories: int = Field(description="Калорийность продукта")

    def __str__(self):
        return f'Название: {self.name}, Количество:{self.amount}, Калорийность: {self.calories}'


class Item(BaseModel, ABC):
    """Модель, дублирующая старую версию Product"""
    name:str = Field(description="Название продукта")
    amount: int = Field(description="Количество продукта")
    @abstractmethod
    def __str__(self): pass


class Potato(Product, PotatoValidation):
    """Модель картошки, наслдуемая от Product"""

    isdirty: bool = Field(description="Показатель грязи на картошке")

    def __str__(self):
        return f'Название: {self.name}, Грязь:{self.isdirty}, Количество:{self.amount}, Калорийность: {self.calories}'


class Carrot(Product, CarrotValidation):
    """Модель моркови, наслдуемая от Product"""
    length: int = Field(description="Длина моркови")

    def __str__(self):
        return f'Название: {self.name}, Длина:{self.length}, Количество:{self.amount}, Калорийность: {self.calories}'


class Berry(Item, BerryValidation):
    """Модель ягоды, наслдуемая от Item"""
    size:int = Field(description="Размер ягоды")

    def __str__(self):
        return f'Название: {self.name}, Количество: {self.amount}, Размер:{self.size}'