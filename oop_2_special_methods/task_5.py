# __eq__
# __ne__
# __lt__
# __le__
# __gt__
# __ge__
class DataObject:

    def __init__(self, objects: list) -> None:
        if type(objects) != list:
            print("Необходимо передать в качестве аргумента список")
            raise TypeError

        for object in objects:
            if type(object) not in (int, float):
                print("Список должен быть числовым")
                raise TypeError

        self.is_len_obj(objects)
        self.objects = objects

    def __eq__(self, other) -> bool:
        if type(other) == list:
            return self.objects[0] == other[0]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[0] == value[0]

        return False

    def __ne__(self, other) -> bool:
        if type(other) == list:
            return self.objects[1] != other[1]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[1] != value[1]

        return True

    def __lt__(self, other) -> bool:
        if type(other) == list:
            return self.objects[2] < other[2]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[2] < value[2]

        return False

    def __le__(self, other) -> bool:
        if type(other) == list:
            return self.objects[3] <= other[3]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[3] <= value[3]

        return False

    def __gt__(self, other) -> bool:
        if type(other) == list:
            return self.objects[4] > other[4]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[4] > value[4]

        return False

    def __ge__(self, other) -> bool:
        if type(other) == list:
            return self.objects[5] >= other[5]

        for value in other.__dict__.values():
            if type(value) == list:
                return self.objects[5] >= value[5]

        return False

    @staticmethod
    def is_len_obj(numbers: list) -> bool:
        if len(numbers) < 6:
            print("Длина должна быть не меньше 6")
            raise ValueError

        return True


def main():
    obj1 = DataObject([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

    obj2 = DataObject([10, 25, 35, 35, 45, 65, 70, 15, 95, 90, 100, 130])

    obj3 = DataObject([5, 30, 20, 50, 60, 55, 80, 70, 100, 80, 120, 110])

    long_obj = DataObject(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    )

    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    print("=== obj1 и obj2 ===")
    print("obj1 == obj2:", obj1 == obj2)
    print("obj1 != obj2:", obj1 != obj2)
    print("obj1 < obj2:", obj1 < obj2)
    print("obj1 <= obj2:", obj1 <= obj2)
    print("obj1 > obj2:", obj1 > obj2)
    print("obj1 >= obj2:", obj1 >= obj2)

    print("\n=== obj1 и numbers ===")
    print("obj1 == numbers:", obj1 == numbers)
    print("obj1 != numbers:", obj1 != numbers)
    print("obj1 < numbers:", obj1 < numbers)
    print("obj1 <= numbers:", obj1 <= numbers)
    print("obj1 > numbers:", obj1 > numbers)
    print("obj1 >= numbers:", obj1 >= numbers)

    print("\n=== Проверка длинного объекта ===")
    print("Длина long_obj:", len(long_obj.objects))

    print("\n=== Проверка слишком короткого списка ===")
    try:
        bad_obj = DataObject([1, 2, 3, 4, 5])
    except ValueError:
        print("bad_obj не создан — проверка длины работает")


main()
