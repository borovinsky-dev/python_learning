from app.models.user import User
from app.services.user_service import UserService
from app.models.admin import Admin


def main() -> None:
    user = User("Дима", 20, "@gmail.com")

    admin = Admin(
        "Admin",
        25,
        "admin@gmail.com",
        {"create", "delete"},
    )

    service = UserService()

    service.add_user(user)

    print(user)
    print(user.is_adult())

    print(admin)
    print(admin.has_permession("create"))

    print(service.users)


main()
