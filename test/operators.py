class Alpha:
    def __init__(self, val):
        self.value = val

    def __eq__(self, val):
        print("Alpha: __eq__")
        return self.value == val

    def __ne__(self, val):
        print("Alpha: __ne__")
        return self.value != val

    def __lt__(self, val):
        print("Alpha: __lt__")
        return self.value < val

    def __ge__(self, val):
        print("Alpha: __ge__")
        return self.value >= val


class Bravo:
    def __init__(self, val):
        self.value = val

    def __eq__(self, val):
        print("Bravo: __eq__")
        return self.value == val


A = Alpha(100)

print("Проверки для A")

print("[01] A == 100:", A == 100)
print("[02] A != 100:", A != 100)
print("[03] 200 == A:", 200 == A)
print("[04] 200 != A:", 200 != A)
print("[05] A < 200:", A < 200)
print("[06] 200 > A:", 200 > A)
print("[07] A >= 200:", A >= 200)
print("[08] 100 <= A:", 100 <= A)


B = Bravo(300)

print("Проверки для B")

print("[09] B == 300:", B == 300)
print("[10] B != 300:", B != 300)
print("[11] 400 == B:", 400 == B)

print("Проверки A и B")

print("[12] A == B:", A == B)
print("[13] B != A:", B != A)
print("[14] A != B:", A != B)


class MyClass:
    # Конструктор
    def __init__(self, val):
        self.value = val

    # Преобразование в строку
    def __str__(self):
        return "Значение: " + str(self.value)

    # Преобразование в логическое значение
    def __bool__(self):
        if type(self.value) == int:
            return True
        else:
            return False

    # Преобразование в целое число
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
