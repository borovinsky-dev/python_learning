import math


def equation(a: int | float) -> int | float:
    try:
        if a == 0:
            return -1

        if a == 1:
            raise ValueError("При A = 1 уравнение не имеет решения")

        return math.sin(a) / (a * (a - 1))

    except ValueError as e:
        print(f"Описание ошибки: {e}")
        return 0


def main():
    try:
        a = float(input("Введите A: "))
        print(f"x = {equation(a)}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")


main()
