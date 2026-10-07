def print_bounded_numbers(number_1: int, number_2: int) -> None:
    try:
        for i in range(number_1, number_2 + 1):
            print(i)
    except TypeError as e:
        print(f"Описание ошибки: {e}")


def main():
    print_bounded_numbers(2, "10")


main()
