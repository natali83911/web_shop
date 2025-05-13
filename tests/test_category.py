import pytest

from src.category import Category
from src.product import Product


def test_product_category(product_category: Category) -> None:
    """Проверка имеющегося вывода продукта"""

    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count >= 1
    assert Category.product_count >= 1


def test_wrong_product_category(product_category: Category) -> None:
    """Проверка вывода отсутствующего продукта"""

    assert product_category.name != "Игровые консоли и игры"
    assert product_category.description != "PlayStation 5 "
    assert Category.category_count != 5
    assert Category.product_count != 0


def test_add_product_increases_count(product_category: Category) -> None:
    """Проверка добавления нового продукта и увеличения счётчика"""
    initial_count = Category.product_count
    new_product = Product("Samsung Galaxy S23", "Flagship smartphone", 180000, 5)
    product_category.add_product(new_product)
    assert Category.product_count == initial_count + 1
    assert new_product in product_category.products_list


def test_add_existing_product_updates_quantity_and_price(product_category: Category, product_unit: Product) -> None:
    """Проверка обновления количества и цены при добавлении существующего продукта"""
    initial_count = Category.product_count
    initial_quantity = product_unit.quantity
    # Создаём продукт с тем же именем, но другим количеством и ценой
    duplicate_product = Product("Iphone 15", "Smartphone", 120000, 3)
    product_category.add_product(duplicate_product)
    for prod in product_category.products_list:
        if prod.name == "Iphone 15":
            assert prod.quantity == initial_quantity + 3
            # Цена должна быть максимальной из старой и новой
            assert prod.price == max(product_unit.price, 120000)
            break
    else:
        pytest.fail("Продукт Iphone 15 не найден в категории")

    # Количество продуктов в категории не должно измениться при обновлении существующего товара
    assert Category.product_count == initial_count


def test_add_product_type_check(product_category: Category) -> None:
    """Проверка, что добавлять можно только объекты Product"""
    with pytest.raises(TypeError):
        product_category.add_product("не продукт")  # строка вместо объекта Product


def test_can_add_product(product_category: Category, product_unit: Product) -> None:
    """Проверка метода can_add_product"""
    assert product_category.can_add_product(product_unit) is True
    assert product_category.can_add_product("строка") is False
    assert product_category.can_add_product(123) is False


def test_products_property_returns_string(product_category: Category) -> None:
    """Проверка строкового свойства products"""
    products_str = product_category.products
    for product in product_category.products_list:
        assert product.name in products_str
        assert str(product.price) in products_str
        assert str(product.quantity) in products_str


def test_products_list_property_returns_list(product_category: Category) -> None:
    """Проверка, что products_list возвращает список объектов Product"""
    products_list = product_category.products_list
    assert isinstance(products_list, list)
    assert all(isinstance(prod, Product) for prod in products_list)
