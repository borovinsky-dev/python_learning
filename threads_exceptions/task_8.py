from threading import Thread


class Data:
    def __init__(self):
        self.symbols = []
        self.numbers = []

    def __str__(self) -> str:
        return f"{self.symbols} {self.numbers}"


def fill_numbers(data: Data, count: int):
    for i in range(count):
        data.numbers.append(i)


def fill_symbols(data: Data, count: int):
    letter_code = 97
    for i in range(count):
        data.symbols.append(chr(letter_code))
        letter_code += 1
        if letter_code > 122:
            letter_code = 97


def main():
    data = Data()
    th_numbers = Thread(target=fill_numbers, args=(data, 4))
    th_symbols = Thread(target=fill_symbols, args=(data, 10))
    th_numbers.start()
    th_symbols.start()
    th_numbers.join()
    th_symbols.join()
    print(data)


main()
