class ZeroProductQuantity(Exception):

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        super().__init__(message)
