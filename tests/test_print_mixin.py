from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Iphone 15", "Smartphone", 115450, 2)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, Smartphone, 115450, 2)"

    Smartphone("Phone1", "Desc1", 1000.0, 2, "A", "Model1", "64GB", "Black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Phone1, Desc1, 1000.0, 2)"

    LawnGrass("Grass1", "Desc1", 10.0, 5, "CountryA", "7 days", "Green")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Grass1, Desc1, 10.0, 5)"
