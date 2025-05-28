from src.category import Category
from src.order import Order
from src.product import Product

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая программу при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())

    product = Product("Ноутбук", "Игровой", 70000, 3)

    # Создаем заказ с ненулевым количеством
    try:
        order1 = Order(product, 2)
        print(order1)
    except Exception as e:
        print("Ошибка при создании order1:", e)

    # Создаем заказ с нулевым количеством
    try:
        order2 = Order(product, 0)
    except Exception as e:
        print("Ошибка при создании order2:", e)
