class DataObject:
    # конструктор для определения объектов независимо от параметров
    def __init__(
        self,
        integer: int | str | float,
        text: int | str | float,
        number: int | str | float,
    ) -> None:

        self.integer = None
        self.text = None
        self.number = None
        # Определяем первый аргумент
        if type(integer) == int:
            self.integer = integer
        elif type(integer) == str:
            self.text = integer
        elif type(integer) == float:
            self.number = integer
        # Определяем второй аргумент
        if type(text) == str:
            self.text = text
        elif type(text) == int:
            self.integer = text
        elif type(text) == float:
            self.number = text
        # Определяем третий аргумент
        if type(number) == float:
            self.number = number
        elif type(number) == int:
            self.integer = number
        elif type(number) == str:
            self.text = number
        # проверка на то, чтобы были только те аргументы, которые есть
        if self.integer is None or self.text is None or self.number is None:
            raise TypeError("Нужно передать один int, один str и один float")

    def __int__(self) -> int:

        return self.integer

    def __float__(self) -> float:
        return self.number

    def __str__(self) -> str:
        return self.text

    def __bool__(self) -> bool:
        return (
            True
            if self.integer != 0 and self.text != "" and self.number != 0
            else False
        )

    def __repr__(self) -> str:
        return f"(DataObject={self.integer!r} {self.text!r} {self.number!r})"
