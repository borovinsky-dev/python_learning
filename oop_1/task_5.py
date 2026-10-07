# тот же самый
class Test:
    def __init__(self):
        self.name = "Dima"
        self.age = 25
        self.count = 10
        self.city = "Minsk"


def create_object(obj):
    namespace = {}
    for key, value in obj.__dict__.items():
        if type(obj.__dict__[key]) == int:
            namespace[key] = value
    new_object = type("NewClass", (), namespace)
    return new_object


def main():
    test = Test()
    print(create_object(Test()).__dict__)


main()
