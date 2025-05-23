# Web_shop

## Описание
 В этом проекте реализованы классы:
1. Product - представляет товар с атрибутами:
   name - название товара,
   description - описание,
   price - цена,
   quantity - количество на складе.

2. Category - представляет категорию товаров с атрибутами:
   name - название категории,
   description - описание,
   products - список объектов Product в категории.

   Класс Category содержит два атрибута класса:
   - category_count - общее количество созданных категорий,
   - product_count - общее количество товаров во всех категориях.
   - Эти атрибуты автоматически обновляются при создании новых объектов Category.

3. Smartphone - класс-наследник Product, добавлены атрибуты:
   efficiency - производительность 
   model - модель 
   memory - объем встроенной памяти
   color - цвет 

4. LawnGrass - класс-наследник Product, добавлены атрибуты:
   country - страна-производитель 
   germination_period - срок прорастания    
   color - цвет  

- Классы `LawnGrass` и `Smartphone` наследуются от `Product` и расширяют функциональность.
- Категории позволяют группировать продукты и отслеживать их количество.
- Перегружен оператор `+` для сложения стоимости продуктов одного типа.

5. CategoryIterator - Перебирает товары одной категории и возвращает очередной товар категории

6. Order - класс для вывода оформления заказа

7. BaseProduct, BaseOrderCategory - базовые классы для классов Product, Order, Category 

## Структура проекта
~~~
project_root/
│
├── src/
│   ├── base_order_category.py   # Класс базовый для классов Category, Order и их наследников
│   ├── base_product.py          # Класс базовый для класса Product и его наследников
│   ├── order.py                 # Класс Order для формирования заказа
│   ├── product.py               # Класс Product
│   ├── category.py              # Класс Category
│   ├── category_iterator        # Класс CategoryIterator
│   ├── smartphone               # Класс Smartphone
│   ├── lawn_grass               # Класс LawnGrass
│   └── utils.py                 # Функция загрузки из JSON
│
├── tests/
│   └── test_product.py          # Тесты
│   ├── test_category.py
│   ├── test_smartphone
│   ├── test_lawn_grass
│   ├── test_order
│   └── test_category_iterator
├── data/
│   └── products.json            # JSON с данными
│
└── README.md

~~~

## Как использовать
Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone git@github.com:natali83911/web_shop.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd web_shop
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    poetry add --group lint flake8
    poetry add --group lint mypy
    poetry add --group lint black
    poetry add --group lint isort
    poetry add --group dev pytest
        
    ```
## Инициализация объектов вручную
~~~
product1 = Product('Product1', 'Description1', 10.0, 5)
product2 = Product('Product2', 'Description2', 20.0, 3)

category = Category('Category1', 'Category description', [product1, product2])

print(category.name)  # Category1
print(Category.category_count)  # 1
print(Category.product_count)   # 2

grass = LawnGrass('Газонная трава', 'Описание', 15.0, 10, 'Россия', '7 дней', 'Зеленый')
phone = Smartphone('Samsung Galaxy S23', 'Флагман', 90000, 5, 'A+', 'S23', '256GB', 'Черный')

# Создание категории и добавление продуктов
category_grass = Category('Газонная трава', 'Категория газонной травы', [grass])
category_smartphones = Category('Смартфоны', 'Категория смартфонов', [phone])

print(category_grass.name) # Газонная трава
print(Category.category_count) # Количество категорий
print(Category.product_count) # Количество продуктов
~~~
Загрузка данных из JSON
~~~
from src.utils import create_object_from_json

categories = create_object_from_json('path/to/products.json')

for category in categories:
    print(f"Категория: {category.name}, товаров: {len(category.products)}")
    
iterator = CategoryIterator(category)

    for product in iterator:
        print(product)
~~~
## Тестирование
В проекте используются тесты, написанные с использованием `pytest`. Для запуска тестов выполните следующие шаги:

1. **Убедитесь, что установлены все зависимости (см. раздел "Установка").**
2. **Активируйте виртуальное окружение Poetry:**
~~~
    poetry env activate    
~~~
3. **Запустите тесты с помощью команды `pytest`:**
~~~
    pytest tests    
~~~

## Зависимости

Проект использует следующие зависимости:
*   Python 3.12.4
*   Poetry (для управления зависимостями)
*   pytest (для тестов)