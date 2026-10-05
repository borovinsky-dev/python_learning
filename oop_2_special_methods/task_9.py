class ObjectIter:
    def __init__(self, count: int):
        self.count = count

    def __iter__(self):
        for i in range(self.count):
            if i % 2 != 0:
                yield i


def main():
    obj = ObjectIter(10)

    for value in obj:
        print(value)


main()
