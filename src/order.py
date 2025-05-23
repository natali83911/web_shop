from src.base_order_category import BaseOrderCategory


class Order(BaseOrderCategory):
    """Класс для оформления заказа"""

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        if product.quantity < self.quantity:
            raise ValueError("Количество заказа превышает количество на складе")
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Заказ: {self.product}. Количество: {self.quantity}.  Итоговая стоимость: {self.total_price}"
