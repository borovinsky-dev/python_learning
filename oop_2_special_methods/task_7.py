class IndexObject:
    def __init__(self, numbers_1: list[int | float], numbers_2: list[int | float]):
        IndexObject.validate_attributes(numbers_1, numbers_2)
        self.numbers_1 = numbers_1
        self.numbers_2 = numbers_2

    def __getitem__(self, key) -> int | float:
        new_numbers_1 = self.numbers_1.copy()
        new_numbers_2 = self.numbers_2.copy()

        if len(self.numbers_1) > len(self.numbers_2):
            for _ in range(len(self.numbers_1) - len(self.numbers_2)):
                new_numbers_2.append(0)
            return new_numbers_1[key] + new_numbers_2[key]
        elif len(self.numbers_1) < len(self.numbers_2):
            for _ in range(len(self.numbers_2) - len(self.numbers_1)):
                new_numbers_1.append(0)
            return new_numbers_1[key] + new_numbers_2[key]
        else:
            return new_numbers_1[key] + new_numbers_2[key]

    @staticmethod
    def validate_attributes(numbers_1, numbers_2) -> None:
        if numbers_1 == None or numbers_2 == None:
            raise TypeError
        elif type(numbers_1) != list or type(numbers_2) != list:
            raise TypeError
        elif any(type(element) not in (int, float) for element in numbers_1) or any(
            type(element) not in (int, float) for element in numbers_2
        ):
            raise TypeError("Элементы должны быть int или float")


def main():
    obj = IndexObject([10, 20, 30, 40], [1, 2])

    print(obj[0])  # 11
    print(obj[1])  # 22
    print(obj[2])  # 30
    print(obj[3])  # 40

    print("-" * 20)

    obj = IndexObject([10, 20], [1, 2, 3, 4])

    print(obj[0])  # 11
    print(obj[1])  # 22
    print(obj[2])  # 3
    print(obj[3])  # 4

    print("-" * 20)

    obj = IndexObject([1.5, 2.5, 3.5], [10, 20, 30])

    print(obj[0])  # 11.5
    print(obj[1])  # 22.5
    print(obj[2])  # 33.5


main()
