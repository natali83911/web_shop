from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для класса Product"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass

    @abstractmethod
    def __add__(self, other) -> float | int:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
