from src.product import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            total_price = self.price * self.quantity + other.price * other.quantity
            return total_price
        else:
            raise TypeError("Можно суммировать только объекты от класса SLawnGrass")
