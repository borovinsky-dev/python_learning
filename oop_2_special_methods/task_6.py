class DataObject:
    def __init__(self, data: list):
        if type(data) != list:
            raise TypeError
        self.data = data

    def __setattr__(self, name, data) -> object | None:
        result_list = []
        if name == "data":
            for element in data:
                if type(element) == str:
                    result_list.append(element)

            object.__setattr__(self, name, result_list)
        else:
            object.__setattr__(self, name, data)

    def __getattr__(self, name):
        if name == "first_letters":
            data = object.__getattribute__(self, "data")

            result = ""

            for element in data:
                result += element[0]

            return result

        raise AttributeError(f"Атрибут {name!r} не существует")

    def __getattribute__(self, name):
        print(f"Запрос атрибута: {name}")
        return super().__getattribute__(name)


def main():
    ob = DataObject(["Fdfg", 1, 12.0, "sdff"])
    print(ob.data)
    print(ob.first_letters)


main()
