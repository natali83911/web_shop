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
 category_count - общее количество созданных категорий,
 product_count - общее количество товаров во всех категориях.
 Эти атрибуты автоматически обновляются при создании новых объектов Category.

3. CategoryIterator - Перебирает товары одной категории и возвращает очередной товар категории

## Структура проекта
~~~
project_root/
│
├── src/
│   ├── product.py               # Класс Product
│   ├── category.py              # Класс Category
    ├── category_iterator        # Класс CategoryIterator
│   └── utils.py                 # Функция загрузки из JSON
│
├── tests/
│   └── test_product.py          # Тесты
│   ├── test_category.py
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