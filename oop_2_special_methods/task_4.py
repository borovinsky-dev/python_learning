# obj + number
# obj - number
# number - obj
# obj * number
# obj / number
class DataObject:
    def __init__(self, number: int | float | complex):
        if type(number) == int or type(number) == float or type(number) == complex:
            self.number = number

    def __add__(self, value: int | float | complex) -> DataObject:
        value = self.validate_value(value)
        return DataObject(self.number + value)

    def __sub__(self, value: int | float | complex) -> DataObject:
        value = self.validate_value(value)
        return DataObject(self.number - value)

    def __rsub__(self, value: int | float | complex) -> DataObject:
        value = self.validate_value(value)
        return DataObject(value - self.number)

    def __mul__(self, value: int | float | complex) -> DataObject:
        value = self.validate_value(value)
        return DataObject(self.number * value)

    def __truediv__(self, value: int | float | complex) -> DataObject:
        value = self.validate_value(value)
        if value == 0:
            raise ZeroDivisionError
        return DataObject(self.number / value)

    def __str__(self) -> str:
        return f"Объект класса {self.__class__.__name__} c атрибутами ({self.__dict__})"

    def __repr__(self):
        return f"{self.__class__.__name__!r}(number={self.number!r})"

    @staticmethod
    def validate_value(value: int | float | complex) -> int | float | complex:
        if type(value) != int and type(value) != float and type(value) != complex:
            print(
                f"Подерживаемые типы: {int.__class__.__name__!r} {float.__class__.__name__!r} {complex.__class__.__name__!r} "
            )
            raise TypeError
        else:
            return value


def main():
    data = DataObject(14.0)
    result = data + 5 - 3 * 2
    print(result)


main()
