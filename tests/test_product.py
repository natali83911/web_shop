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
