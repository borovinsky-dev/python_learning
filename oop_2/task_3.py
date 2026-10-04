class DataCollection:
    def __init__(self, data: list[object]):
        self.data = data

    # перегрузка метода сложения
    def __add__(self, object: object) -> DataCollection:
        if type(object) == int:
            new_list = self.data.copy()
            for i in range(len(new_list)):
                if type(new_list[i]) == int:
                    new_list[i] = new_list[i] + object
            new_data = DataCollection(new_list)
        else:
            list_attr_object = []
            for _, v in object.__dict__.items():
                if isinstance(v, list):
                    list_attr_object.extend(v)
            new_data = DataCollection(self.data + list_attr_object)
        return new_data

    # еще одна перегрузка метода сложения
    def __radd__(self, value: int) -> DataCollection:
        if type(value) != int:
            raise TypeError
        new_list = self.data.copy()
        for i in range(len(new_list)):
            if type(new_list[i]) == int:
                new_list[i] = new_list[i] + value
        new_object = DataCollection(new_list)
        return new_object

    def __str__(self) -> str:
        return f"{self.data}"


class TestCollection:
    def __init__(self, data: list[object]):
        self.data = data


def main():

    data = DataCollection([1, "asd", 2.0])
    data_1 = TestCollection(["adsfd", 6, 0])
    print(data + data_1)
    print(3 + data)
    print(data + 3)


main()
