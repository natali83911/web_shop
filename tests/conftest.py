import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def product_unit() -> Product:
    """осуществляет возврат Класс Product"""
    return Product("Iphone 15", "Smartphone", 115450, 2)


@pytest.fixture
def product_unit_2() -> Product:
    """Второй продукт для теста сложения"""
    return Product("Samsung S23", "Smartphone", 90000, 3)


@pytest.fixture
def product_category(product_unit) -> Category:
    """осуществляет возврат Класс Сategory"""
    products = [product_unit]
    return Category("Мобильная электроника", "Smartphone", products)


@pytest.fixture
def products_list():
    return [
        Product("Iphone 15", "Smartphone", 115450, 2),
        Product("Samsung S23", "Smartphone", 90000, 3),
        Product("Xiaomi Mi", "Smartphone", 50000, 5),
    ]


@pytest.fixture
def category(products_list):
    return Category("Мобильная электроника", "Смартфоны", products_list)


@pytest.fixture
def product_category_for_iter(product_unit, product_unit_2) -> Category:
    """Фикстура возвращает категорию с двумя продуктами"""
    products = [product_unit, product_unit_2]
    return Category("Мобильная электроника", "Smartphone", products)


@pytest.fixture
def smartphone1():
    return Smartphone("Phone1", "Desc1", 1000.0, 2, "A", "Model1", "64GB", "Black")


@pytest.fixture
def smartphone2():
    return Smartphone("Phone2", "Desc2", 1500.0, 3, "B", "Model2", "128GB", "White")


@pytest.fixture
def grass1():
    return LawnGrass("Grass1", "Desc1", 10.0, 5, "CountryA", "7 days", "Green")


@pytest.fixture
def grass2():
    return LawnGrass("Grass2", "Desc2", 15.0, 3, "CountryB", "10 days", "Light Green")


@pytest.fixture
def category_empty_list():
    return Category("Мобильная электроника", "Смартфоны", [])
