# Цепочка наследования 3 классов
class Alpha:
    def __init__(self: "Alpha", name: str) -> None:
        self.name: str = name

    # Приведение типов (Для функции str по сути, представлять объект в виде строки)
    def __str__(self: "Alpha") -> str:
        return f"ОбЪект c атрибутами: {self.__dict__} класса: {self.__class__.__name__}"

    def show_info(self) -> str:
        result = f"Информация об объекте класса {self.__class__.__name__}\nАтрибуты:"
        for k, v in self.__dict__.items():
            if v is not None:
                result += f"[{k}]:" + "{" f"{v}" + "}"
        return result


class Beta(Alpha):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age: int = age

    def show_info(self: "Beta"):
        print(f"Переопределение класса {self.__class__.__name__}")
        return super().show_info()


class Teta(Beta):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age)
        self.gender = gender

    def show_info(self: "Teta"):
        print(f"Переопределение класса {self.__class__.__name__}")
        return super(Beta, self).show_info()


def main() -> None:
    a = Alpha("Дмитрий")
    print("Работа str приведения типа")
    print(a)
    print(a.show_info())
    b = Beta("Олег", 25)
    print("Работа str приведения типа")
    print(b)
    print(b.show_info())
    c = Teta("Женя", 30, "женский")
    print("Работа str приведения типа")
    print(c)
    print(c.show_info())


if __name__ == "__main__":
    main()
