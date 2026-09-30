class Test:
    def __init__(self, elements: list):
        temp = False
        for element in elements:
            if not isinstance(element, (int, float)):
                temp = False
                break
            else:
                temp = True
        if temp:
            self.elements = elements
        else:
            self.elements = None

    def get_attr(self) -> dict:
        return self.__dict__.items()

    def get_average_list(self) -> str:
        result = sum(self.elements) / len(self.elements)
        return f"{result:.2f}"


def main():
    test = Test([1, 60, 3, 4])
    print(test.get_attr())
    print(test.get_average_list())


main()
