class Data:

    def __init__(self, caf: list):
        self.caf = caf

    def __call__(self, x: int) -> int | float:
        summa = 0
        a_0 = self.caf[0]
        for i in range(1, len(self.caf)):
            summa += x**i * self.caf[i]
        return a_0 + summa


def main():
    data = Data([2, 3, 4])

    print(data(5))


main()
