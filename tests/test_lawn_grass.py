import pytest

from src.product import Product


def test_add_same_class(grass1, grass2):
    result = grass1 + grass2
    expected = 10.0 * 5 + 15.0 * 3
    assert result == expected


def test_add_non_product_raises(grass1):
    with pytest.raises(TypeError, match="Можно суммировать только объекты от класса SLawnGrass"):
        _ = grass1 + 123


def test_add_different_class_raises(grass1):
    class OtherProduct(Product):
        pass

    other = OtherProduct("Other", "Desc", 20.0, 2)
    with pytest.raises(TypeError, match="Можно суммировать только объекты от класса SLawnGrass"):
        _ = grass1 + other
