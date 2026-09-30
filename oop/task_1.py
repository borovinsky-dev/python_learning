# Очень простое задание, ничего интересного
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_attr(self: User) -> tuple:
        return f"[{self.name}] [{self.age}]"


def main():

    user = User("Дима", 26)
    print(user.get_attr())


main()
