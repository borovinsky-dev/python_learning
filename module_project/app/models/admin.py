from app.models.user import User


class Admin(User):
    """Тестовый класс админ"""

    def __init__(
        self, name: str, age: int, email: str, permessions: set, role: bool = True
    ):
        super().__init__(name, age, email)
        # Тут роль была выбрана булевой, для себя, по сути это должен быть объект
        self.role = role
        self.permessions = permessions

    def has_permession(self, permession: str) -> bool:
        """Определить какие функции у админа есть"""
        for perm in self.permessions:
            if perm == permession:
                return True
        return False


def main():
    admin = Admin(
        "Admin",
        20,
        "@gmail.com",
        {"create", "delete"},
    )
    print(admin.has_permession("create"))


if __name__ == "__main__":
    print("Прямой запуск класса Admin")
    main()
