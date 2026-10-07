from time import sleep
from threading import Thread


def worker_1(n: int):
    print("Worker_1")
    for i in range(n):
        print(i)


def worker_2(n: int):
    print("Worker_2")
    for i in range(n):
        print("поток 2")


def main():

    t1 = Thread(target=worker_1, args=(10,))
    t2 = Thread(target=worker_2, args=(20,))
    t1.start()
    t2.start()
    print("Main дождался")


main()
