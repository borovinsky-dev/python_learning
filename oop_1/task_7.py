# выглядит страшно
class Numbers:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers


def create_object(obj_1: Numbers, obj_2: Numbers) -> Numbers:
    len_long = (
        len(obj_1.numbers)
        if len(obj_1.numbers) > len(obj_2.numbers)
        else (
            len(obj_1.numbers)
            if len(obj_1.numbers) == len(obj_2.numbers)
            else len(obj_2.numbers)
        )
    )

    new_list = []
    for i in range(len_long):
        if len_long == len(obj_1.numbers):
            for i in range(len(obj_2.numbers), len(obj_1.numbers)):
                obj_2.numbers.append(0)

        elif len_long == len(obj_2.numbers):
            for i in range(len(obj_1.numbers), len(obj_2.numbers)):
                obj_1.numbers.append(0)

        new_list.append(obj_1.numbers[i] + obj_2.numbers[i])
    return type("Numbers", (), {"numbers": new_list})


def main():
    obj_1 = Numbers([1, 2, 3, 4])

    obj_2 = Numbers([10, 20])

    result = create_object(obj_1, obj_2)

    print(result.numbers)
    # [11, 22, 3, 4]

    obj_1 = Numbers([1, 2])
    obj_2 = Numbers([10, 20, 30, 40])

    result = create_object(obj_1, obj_2)

    print(result.numbers)
    # [11, 22, 30, 40]

    obj_1 = Numbers([1, 2, 3])
    obj_2 = Numbers([10, 20, 30])

    result = create_object(obj_1, obj_2)


main()
