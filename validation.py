from errors import FieldTypeError, FieldMissingError
from typing import Union, Dict, Type

def safe_get(dic: dict, key: str):
    """Возвращает значение или бросает ошибку, если ключа нет."""
    if key not in dic:
        raise FieldMissingError(f"Отсутствует обязательное поле: {key}")
    return dic[key]


def validate_name(name):
    if not isinstance(name, str) or not name:
        raise FieldTypeError("Поле 'name' должно быть непустой строкой")

def validate_amount(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise FieldTypeError("Поле 'amount' должно быть неотрицательным числом")

def validate_date(date):
    # Улучшаем валидацию: не только длина, но и тип.
    if not isinstance(date, str) or len(date) != 10:
        raise FieldTypeError("Поле 'date' должно быть строкой в корректном формате")

def validate_calories(calories):
    if not isinstance(calories, int) or calories < 0:
        raise FieldTypeError("Поле 'calories' должно быть неотрицательным целым числом")

def validate_length(length):
    if not isinstance(length, int) or length <= 0:
        raise FieldTypeError("Поле 'length' (длина) должно быть положительным целым числом")

def validate_isdirty(isdirty):
    if not isinstance(isdirty, bool):
        raise FieldTypeError("Поле 'isdirty' (грязь) должно быть булевым значением")

def validate_size(size):
    if not isinstance(size, int) or size <= 0:
        raise FieldTypeError("Поле 'size' (размер) должно быть положительным целым числом")