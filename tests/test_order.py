import pytest

from src.order import Order
from src.product import Product


def test_order_creation_and_str():
    product = Product("Samsung S23", "Smartphone", 90000, 3)
    order = Order(product, 3)
    assert order.product == product
    assert order.quantity == 3
    assert order.total_price == 270000
    expected_str = "Заказ: Samsung S23, 90000 руб. Остаток: 3 шт.. Количество: 3.  Итоговая стоимость: 270000"
    assert str(order) == expected_str


def test_order_quantity_exceeds_stock():
    product = Product("Samsung S23", "Smartphone", 90000, 3)
    with pytest.raises(ValueError, match="Количество заказа превышает количество на складе"):
        Order(product, 5)
