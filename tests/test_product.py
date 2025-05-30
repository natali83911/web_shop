from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


def test_product_unit(product_unit: Product) -> None:
    """Проверка имеющегося вывода продукта"""

    assert product_unit.name == "Iphone 15"
    assert product_unit.description == "Smartphone"
    assert product_unit.price == 115450
    assert product_unit.quantity == 2


def test_wrong_product_unit(product_unit: Product) -> None:
    """Проверка вывода отсутствующего продукта"""

    assert not product_unit.name == "Nokia 5.1 Plus"
    assert not product_unit.description == "TA-1105 Blue"
    assert not product_unit.price == 3500
    assert not product_unit.quantity == 1


def test_product_init_zero_quantity():
    product = Product("Телефон", "Смартфон", 1000.0, 0)
    assert product.quantity == 0


def test_product_init_negative_quantity_raises():
    with pytest.raises(ValueError) as exc:
        Product("Телефон", "Смартфон", 1000.0, -1)
    assert str(exc.value) == "Товар с нулевым количеством не может быть добавлен"


def test_new_product_add_and_update():
    products_list = []
    data1 = {"name": "Samsung Galaxy S23", "description": "Flagship", "price": 180000.0, "quantity": 5}
    data2 = {"name": "Samsung Galaxy S23", "description": "Flagship", "price": 190000.0, "quantity": 3}
    data3 = {"name": "Iphone 15", "description": "Smartphone", "price": 115450.0, "quantity": 2}

    p1 = Product.new_product(products_list, data1)
    assert p1.name == "Samsung Galaxy S23"
    assert p1.quantity == 5
    assert p1.price == 180000.0
    assert len(products_list) == 1

    p2 = Product.new_product(products_list, data2)
    assert p2 is p1
    assert p2.quantity == 8
    assert p2.price == 190000.0
    assert len(products_list) == 1

    p3 = Product.new_product(products_list, data3)
    assert p3.name == "Iphone 15"
    assert p3.quantity == 2
    assert len(products_list) == 2


def test_price_setter_positive(product_unit: Product):
    product_unit.price = 200000
    assert product_unit.price == 200000


def test_price_setter_zero_or_negative(product_unit: Product, capsys):
    product_unit.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_unit.price == 115450  # цена не изменилась

    product_unit.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product_unit.price == 115450  # цена не изменилась


def test_price_setter_lower_price_confirm_yes(product_unit: Product):
    with patch("builtins.input", return_value="y"):
        product_unit.price = 100000
    assert product_unit.price == 100000


def test_price_setter_lower_price_confirm_no(product_unit: Product, capsys):
    with patch("builtins.input", return_value="n"):
        product_unit.price = 100000
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product_unit.price == 115450  # цена не изменилась


def test_category_initialization(product_category: Category) -> None:
    assert product_category.name == "Мобильная электроника"
    assert product_category.description == "Smartphone"
    assert Category.category_count >= 1
    assert Category.product_count >= 1


def test_add_product_increases_count(product_category: Category) -> None:
    initial_count = Category.product_count
    new_product = Product("Samsung Galaxy S23", "Flagship smartphone", 180000, 5)
    product_category.add_product(new_product)
    assert Category.product_count == initial_count + 1
    assert new_product in product_category.products_list


def test_products_property_returns_string(product_category: Category) -> None:
    products_str = product_category.products
    for product in product_category.products_list:
        assert product.name in products_str
        assert str(product.price) in products_str
        assert str(product.quantity) in products_str


def test_products_list_property_returns_list(product_category: Category) -> None:
    products_list = product_category.products_list
    assert isinstance(products_list, list)
    assert all(isinstance(prod, Product) for prod in products_list)


def test_str_product(product_unit):
    expected_str = "Iphone 15, 115450 руб. Остаток: 2 шт."
    assert str(product_unit) == expected_str


def test_add_products(product_unit, product_unit_2):
    expected_total = product_unit.price * product_unit.quantity + product_unit_2.price * product_unit_2.quantity
    assert product_unit + product_unit_2 == expected_total


def test_add_invalid_type(product_unit):
    # сложение с не Product возникает TypeError
    with pytest.raises(TypeError):
        product_unit + 10


def test_category_products_count(product_category, product_unit):
    # категория содержит правильный продукт
    assert product_unit in product_category.products_list
    # строковое представление категории (если реализован __str__)
    total_quantity = sum(p.quantity for p in product_category.products_list)
    expected_str = f"{product_category.name}, количество продуктов: {total_quantity} шт."
    assert str(product_category) == expected_str
