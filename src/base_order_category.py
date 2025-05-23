from abc import ABC, abstractmethod


class BaseOrderCategory(ABC):
    """Абстрактный класс, для оформления продукта заказа."""

    @abstractmethod
    def __str__(self) -> str:
        pass
