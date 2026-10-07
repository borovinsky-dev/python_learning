class MyError(Exception):
    def __init__(self):
        self.values = []

    def __add__(self, val):
        self.values.append(val)
        return self


# Функция для возбуждения исключения
def getMyError(n):
    try:
        if n <= 1:
            # Возбуждение исключения
            raise MyError

        # Рекурсивный вызов функции
        getMyError(n - 1)

    except MyError as error:
        # Изменение объекта исключения
        raise error + n


# Функция для создания списка
def getList(n):
    try:
        # Вызов функции, возбуждающей исключение
        getMyError(n)

    except MyError as error:
        # Получение списка из объекта исключения
        return error.values


# Проверка работы:
A = getList(10)
print(A)

B = getList(7.5)
print(B)


class UserError(Exception):
    def __init__(self):
        self.values = []

    def __add__(self, value):
        self.values.append(value)
        return self


class MyClassRecursion:

    def recursion(self, unicode: int):
        try:
            symbol = chr(unicode)

            if unicode == ord("z"):
                raise UserError

            self.recursion(unicode + 1)

        except UserError as error:
            raise error + symbol


a = MyClassRecursion()

try:
    a.recursion(ord("a"))
except UserError as error:
    print(error.values)
