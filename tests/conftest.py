import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_unit() -> Product:
    """осуществляет возврат Класс Product"""
    return Product("Iphone 15", "Smartphone", 115450, 2)


@pytest.fixture
def product_category(product_unit) -> Category:
    """осуществляет возврат Класс Сategory"""
    products = [product_unit]
    return Category("Мобильная электроника", "Smartphone", products)
