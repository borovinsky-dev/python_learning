from threading import Thread, Lock

common_list = [None for i in range(20)]


def even_numbers(common_list) -> None:
    common_list
    letters = get_letters()
    for i in range(len(common_list)):
        if i % 2 == 0:
            common_list[i] = next(letters)


def not_even_numbers(common_list) -> None:
    for i in range(len(common_list)):
        if i % 2 != 0:
            common_list[i] = i


# бесконечный генератор
def get_letters():
    i = 97

    while True:
        yield chr(i)
        i += 1

        if i > 122:
            i = 97


def main():
    global common_list
    th_1 = Thread(target=even_numbers, args=(common_list,))
    th_2 = Thread(target=not_even_numbers, args=(common_list,))
    th_1.start()
    th_2.start()
    th_1.join()
    th_2.join()
    print(common_list)


main()
