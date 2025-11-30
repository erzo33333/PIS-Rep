import pytest
from classes import Product, Potato, Carrot, Berry
from errors import FieldTypeError

def test_product_ok():
    p = Product("Огурец", 100, "01.01.2025", 15)
    assert p.name == "Огурец"

def test_product_wrong_amount():
    with pytest.raises(FieldTypeError):
        Product("Огурец", -10, "01.01.2025", 15)

def test_carrot_wrong_length():
    with pytest.raises(FieldTypeError):
        Carrot("Морковь", -5, 100, "01.01.2025", 40)

def test_berry_wrong_size():
    with pytest.raises(FieldTypeError):
        Berry("Арбуз", 0, 50, "01.01.2025")
