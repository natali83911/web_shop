import pytest

from src.category import Category
from src.exceptions import ZeroProductQuantity
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


def test_category_str(category, products_list):
    total_quantity = sum(p.quantity for p in products_list)
    expected_str = f"{category.name}, количество продуктов: {total_quantity} шт."
    assert str(category) == expected_str


def test_category_str_empty():
    empty_category = Category("Пустая категория", "Нет товаров", [])
    expected_str = f"{empty_category.name}, количество продуктов: 0 шт."
    assert str(empty_category) == expected_str


def test_middle_price(category, category_empty_list):
    assert category.middle_price() == 85150
    assert category_empty_list.middle_price() == 0


def test_custom_exception(capsys, category):
    assert len(category.products_list) == 3

    product_add1 = Product("Samsung S23", "Smartphone", 90000, 0)
    try:
        category.add_product(product_add1)
    except ZeroProductQuantity:
        pass
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Ошибка: Товар с нулевым количеством не может быть добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"

    product_add2 = Product("Samsung S23", "Smartphone", 90000, 5)
    try:
        category.add_product(product_add2)
    except ZeroProductQuantity:
        pass
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-2]
        == "Товар 'Samsung S23' успешно добавлен в категорию (обновлено количество)"
    )
