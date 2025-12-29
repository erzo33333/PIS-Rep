"""
Модуль, содержащий классы для валидации.
Использует pydantic для валидации.
"""
from pydantic import field_validator

class GeneralValidationProperties:
    """Базовый класс валидации"""
    @field_validator('name', mode='before')
    def validate_name(cls, v):
        """Валидация названия"""
        if isinstance(v, str) and len(v) > 0:
            return v
        else:
            raise ValueError("Имя должно быть непустой строкой")

    @field_validator('amount', mode='after')
    def validate_amount(cls, v):
        """Валидация количества"""
        if isinstance(v, (float, int)) and v > 0:
            return v
        else:
            raise ValueError("Количество товара должно быть положительным числом")


class ProductValidation(GeneralValidationProperties):
    """Валидация стандартного товара"""
    @field_validator('calories', mode='after')
    def validate_calories(cls, v):
        """Валидация калллорий"""
        if isinstance(v, int) and v > 0:
            return v
        else:
            raise ValueError("Калорийность должна быть целым положительным числом")


class PotatoValidation(GeneralValidationProperties):
    """Валидация аттрибутов картофеля"""
    @field_validator('calories', mode='after')
    def validate_calories(cls, v):
        """Валидация калорий"""
        if isinstance(v, int) and v > 0:
            return v
        else:
            raise ValueError("Калорийность должна быть целым положительным числом")

    @field_validator('isdirty', mode='after')
    def validate_isdirty(cls, v):
        """Валидация загрязнённсти"""
        if isinstance(v, bool):
            return v
        else:
            raise ValueError("Показатель грязи должен быть True, False")


class CarrotValidation(GeneralValidationProperties):
    """Валидация аттрибутов моркови"""
    @field_validator('calories', mode='after')
    def validate_calories(cls, v):
        """Валидация калорий"""
        if isinstance(v, int) and v > 0:
            return v
        else:
            raise ValueError("Калорийность должна быть целым положительным числом")

    @field_validator('length', mode='after')
    def validate_length(cls, v):
        """Валидация длины"""
        if isinstance(v, int):
            return v
        else:
            raise ValueError("Длина должа быть целым положительным числом")

class BerryValidation(GeneralValidationProperties):
    """Класс валидации аттрибутов ягод"""
    @field_validator('size', mode='after')
    def validate_size(cls, v):
        """Валидация размера"""
        if isinstance(v, int) and v > 0:
            return v
        else:
            raise ValueError("Размер должен быть целым положительным числом")