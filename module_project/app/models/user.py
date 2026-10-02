class User:
    """Класс User представляет пользователей"""

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self: "User") -> str:
        return f"[Имя: {self.name } Возраст: {self.age} Почта:{self.email}]"

    def is_adult(self: "User") -> bool:
        return True if self.age >= 18 else False


def main():

    user = User("Дима", 18, "@gmail.com")
    print(user.is_adult())


if __name__ == "__main__":
    print("Прямой запуск класса User")
    main()
