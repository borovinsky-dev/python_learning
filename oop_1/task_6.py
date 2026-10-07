# тоже создание объектов
class Test:
    def __init__(self, value: int):
        # проверки типов опустим
        self.value = value

    def create_list_objects(self, count: int) -> list:
        result = []
        k = 0
        for i in range(count):
            if k % 2 != 0:
                test = Test(value=k)
                result.append(test)
            k += 1
        return result


def main():
    test = Test(1)
    print(test.create_list_objects(8))


main()
