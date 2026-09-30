class Test:
    def __init__(self, arg1, arg2):
        if type(arg1) == int and type(arg2) == int:
            print("Сумма чисел при инициализиации объекта")
            self.sum_int = arg1 + arg2
        elif type(arg1) == str and type(arg2) == str:
            print("Сумма строк при инициалзиации объекта")
            self.sum_str = arg1 + arg2
        elif (type(arg1) == int and type(arg2) == str) or (
            type(arg1) == str and type(arg2) == int
        ):
            print("Присваивание атрибутов")
            self.arg1 = arg1
            self.arg2 = arg2
        else:
            print("Странные типы")

    def get_attr(self):
        return self.__dict__.items()


def main():
    test_1 = Test("Дима", "Дима")
    print(test_1.get_attr())
    test_2 = Test(12, "Дима")
    print(test_2.get_attr())
    test_3 = Test(12, 13)
    print(test_3.get_attr())
    test_4 = Test([1, 2, 3], "Дима")
    print(test_4.get_attr())


main()
