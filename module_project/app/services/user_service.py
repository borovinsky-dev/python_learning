from app.models.user import User


class UserService:
    def __init__(self):
        self.users: list["User"] = []

    def add_user(self, user: "User") -> None:
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, email: str) -> None:
        for user in self.users:
            if user.email == email:
                del user

    def find_by_email(self, email: str) -> "User" | None:
        for user in self.users:
            if user.email == email:
                return user


def main() -> None:
    service = UserService()
    user = User("Новый User", 15, "@gmail.com")
    service.add_user(user)


if __name__ == "__main__":
    print("Прямой запуск класса UserService")
    main()
