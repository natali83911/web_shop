from src.base_order_category import BaseOrderCategory
from src.exceptions import ZeroProductQuantity


class Order(BaseOrderCategory):
    """Класс для оформления заказа"""

    def __init__(self, product, quantity):
        try:
            if quantity == 0:
                raise ZeroProductQuantity()
            self.product = product
            self.quantity = quantity
            if product.quantity < self.quantity:
                raise ValueError("Количество заказа превышает количество на складе")
            self.total_price = product.price * quantity
            print(f"Заказ на товар '{product.name}' успешно создан.")
        except ZeroProductQuantity as e:
            print(f"Ошибка: {e}")
            raise
        finally:
            print("Обработка создания заказа завершена.")

    def __str__(self):
        return f"Заказ: {self.product} Количество: {self.quantity}.  Итоговая стоимость: {self.total_price}"
