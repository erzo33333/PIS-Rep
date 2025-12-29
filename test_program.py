"""
Модуль тестирования всей программы.
Использует pytest.
"""
import pytest
from classes import Product, Potato, Carrot, Berry, Shop
from validation import ProductValidation, PotatoValidation, CarrotValidation, BerryValidation


class TestValidation:
    """Тесты валидации"""

    def test_product_validation_success(self):
        """Тест успешной валидации Product"""
        product = Product(name="Тест", amount=10.5, calories=100)
        assert product.name == "Тест"
        assert product.amount == 10.5
        assert product.calories == 100

    def test_product_validation_failure(self):
        """Тест неудачной валидации Product"""
        with pytest.raises(ValueError):
            Product(name="", amount=10, calories=100)

        with pytest.raises(ValueError):
            Product(name="Тест", amount=0, calories=100)

        with pytest.raises(ValueError):
            Product(name="Тест", amount=10, calories=0)

    def test_potato_validation_success(self):
        """Тест успешной валидации Potato"""
        potato = Potato(name="Картошка", amount=5.0, calories=80, isdirty=True)
        assert potato.name == "Картошка"
        assert potato.isdirty == True

    def test_potato_validation_failure(self):
        """Тест неудачной валидации Potato"""
        with pytest.raises(ValueError):
            Potato(name="Картошка", amount=5, calories=80, isdirty="не булево")

    def test_carrot_validation_success(self):
        """Тест успешной валидации Carrot"""
        carrot = Carrot(name="Морковь", amount=3.0, calories=40, length=15)
        assert carrot.length == 15

    def test_carrot_validation_failure(self):
        """Тест неудачной валидации Carrot"""
        with pytest.raises(ValueError):
            Carrot(name="Морковь", amount=3, calories=40, length="не число")

    def test_berry_validation_success(self):
        """Тест успешной валидации Berry"""
        berry = Berry(name="Клубника", amount=10, size=2)
        assert berry.size == 2
        assert berry.amount == 10

    def test_berry_validation_failure(self):
        """Тест неудачной валидации Berry"""
        with pytest.raises(ValueError):
            Berry(name="Клубника", amount=10, size=0)


class TestShop:
    """Тесты магазина"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.shop = Shop()

    def test_shop_initialization(self):
        """Тест инициализации магазина"""
        assert self.shop.goods == []

    def test_add_item_to_shop(self):
        """Тест добавления товара в магазин"""
        initial_count = len(self.shop.goods)

        self.shop.AddItem('1', name="Картошка", amount=5.0, calories=80, isdirty=True)

        assert len(self.shop.goods) == initial_count + 1
        assert isinstance(self.shop.goods[0], Potato)

    def test_remove_item_success(self):
        """Тест успешного удаления товара"""
        self.shop.AddItem('1', name="Картошка", amount=5.0, calories=80, isdirty=True)
        initial_count = len(self.shop.goods)

        self.shop.RemoveItem(0)

        assert len(self.shop.goods) == initial_count - 1

    def test_remove_item_failure(self):
        """Тест неудачного удаления товара"""
        with pytest.raises(IndexError):
            self.shop.RemoveItem(0)

        with pytest.raises(IndexError):
            self.shop.RemoveItem(999)

    def test_shop_str_representation(self):
        """Тест строкового представления магазина"""
        self.shop.AddItem('1', name="Картошка", amount=5.0, calories=80, isdirty=True)

        shop_str = str(self.shop)
        assert "Список всех товаров в магазине" in shop_str
        assert "Картошка" in shop_str


class TestIntegration:
    """Интеграционные тесты"""

    def test_complete_workflow(self):
        """Тест полного рабочего процесса"""
        shop = Shop()

        shop.AddItem('1', name="Картошка", amount=5.0, calories=80, isdirty=True)
        shop.AddItem('2', name="Морковь", amount=3.0, calories=40, length=15)
        shop.AddItem('3', name="Клубника", amount=10, size=2)
        shop.AddItem('4', name="Яблоко", amount=7.0, calories=52)

        assert len(shop.goods) == 4
        assert isinstance(shop.goods[0], Potato)
        assert isinstance(shop.goods[1], Carrot)
        assert isinstance(shop.goods[2], Berry)
        assert isinstance(shop.goods[3], Product)

        shop.RemoveItem(1)
        assert len(shop.goods) == 3
        assert isinstance(shop.goods[1], Berry)

        shop_str = str(shop)
        assert "Картошка" in shop_str
        assert "Клубника" in shop_str
        assert "Яблоко" in shop_str
