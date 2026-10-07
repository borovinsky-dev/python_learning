def summa(*k: int | float) -> int | float:
    try:
        summa = 0
        for i in k:
            summa += i
        return summa

    except TypeError as e:

        print(f"Типа ошибки: {e}, типы должны быть целочисленными для сложения")
        list_k = list(k)
        for i in range(len(list_k)):
            if type(list_k[i]) == str:
                list_k[i] = int(list_k[i])
        return sum(list_k)


def main():
    print(summa(1, 2, 3, "5"))


main()
