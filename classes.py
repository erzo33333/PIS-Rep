"""
Модуль, содержащий классы для представления продуктов и магазина.
Использует pydantic для валидации данных.
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from validation import (
    ProductValidation,
    PotatoValidation,
    CarrotValidation,
    BerryValidation
)

class Shop(BaseModel):
    """Модель магазина для управления товарами."""
    goods: list = Field(default=[], description="Список всех товаров в магазине")

    def AddItem(self, product_type, **kwargs):
        """Добавление товара в магазин."""
        types = {
            '1': Potato,
            '2': Carrot,
            '3': Berry
        }

        product_class = types.get(product_type, Product)
        self.goods.append(product_class(**kwargs))

    def RemoveItem(self, index):
        """Удаление товара по индексу."""
        if 0 <= index < len(self.goods):
            self.goods.pop(index)
        else:
            raise IndexError("Товар с таким индексом не найден")

    def __str__(self):
        goods_str = 'Список всех товаров в магазине:\n'
        for i, good in enumerate(self.goods):
            goods_str += f'{i}. {good}\n'
        return goods_str


class Product(BaseModel, ProductValidation):
    """Основная модель, отвечающая за неклассифицированные продукты."""
    name: str = Field(description="Название продукта")
    amount: float = Field(description="Количество продукта")
    calories: int = Field(description="Калорийность продукта")

    def __str__(self):
        return f'Название: {self.name}, Количество:{self.amount}, Калорийность: {self.calories}'


class Item(BaseModel, ABC):
    """Абстрактная модель, дублирующая старую версию Product."""
    name: str = Field(description="Название продукта")
    amount: int = Field(description="Количество продукта")

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления."""


class Potato(Product, PotatoValidation):
    """Модель картошки, наследуемая от Product."""
    isdirty: bool = Field(description="Показатель грязи на картошке")

    def __str__(self):
        return f'Название: {self.name}, Грязь:{self.isdirty}, Количество:{self.amount}, Калорийность: {self.calories}'


class Carrot(Product, CarrotValidation):
    """Модель моркови, наследуемая от Product."""
    length: int = Field(description="Длина моркови")

    def __str__(self):
        return f'Название: {self.name}, Длина:{self.length}, Количество:{self.amount}, Калорийность: {self.calories}'


class Berry(Item, BerryValidation):
    """Модель ягоды, наследуемая от Item."""
    size: int = Field(description="Размер ягоды")

    def __str__(self):
        return f'Название: {self.name}, Количество: {self.amount}, Размер:{self.size}'