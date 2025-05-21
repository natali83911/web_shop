import pytest

from src.product import Product


def test_add_same_class(smartphone1, smartphone2):
    result = smartphone1 + smartphone2
    expected = 1000.0 * 2 + 1500.0 * 3
    assert result == expected


def test_add_non_product_raises(smartphone1):
    with pytest.raises(TypeError, match="Можно суммировать только объекты от класса Smartphone"):
        _ = smartphone1 + 123


def test_add_different_class_raises(smartphone1):
    class OtherProduct(Product):
        pass

    other = OtherProduct("Other", "Desc", 500.0, 1)
    with pytest.raises(TypeError, match="Можно суммировать только объекты от класса Smartphone"):
        _ = smartphone1 + other
