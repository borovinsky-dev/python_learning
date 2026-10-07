from threading import Thread

result_list = []


def factorial(number: int) -> None:
    result = 1

    for i in range(1, number + 1):
        result *= i

    result_list.append(result)


def double_factorial(number: int) -> None:
    result = 1

    for i in range(number, 0, -2):
        result *= i

    result_list.append(result)


def fibonacci(number: int) -> None:
    if number == 1 or number == 2:
        result_list.append(1)
        return

    first = 1
    second = 1

    for _ in range(3, number + 1):
        first, second = second, first + second

    result_list.append(second)


def main():
    threads = []

    thread_1 = Thread(target=factorial, args=(5,))
    thread_2 = Thread(target=double_factorial, args=(7,))
    thread_3 = Thread(target=fibonacci, args=(8,))

    threads.extend((thread_1, thread_2, thread_3))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    for thread in threads:
        thread.join()

    print(result_list)


main()
