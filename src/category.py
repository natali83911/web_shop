from src.product import Product


class Category:
    """Класс категория"""

    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product) -> None:
        """Метод для добавления товаров в категорию"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты от класса Product или его подклассов")

        # Проверка на существующий товар
        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return

        self.__products.append(product)
        Category.product_count += 1

    def can_add_product(self, product) -> bool:
        """Проверка возможности добавления продукта"""
        return issubclass(type(product), Product)

    @property
    def products_list(self):
        return self.__products
