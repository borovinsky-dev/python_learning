from threading import Thread
from threading import Lock
from time import sleep

global_count = 0
lock = Lock()


def worker():
    lock.acquire()
    count = 0
    while count < 20:
        global global_count
        global_count += 1
        count += 1
    lock.release()


def run_threads(count_threads: int = 5):
    if count_threads == 5:
        threads = []
        for i in range(5):
            print(f"Поток {i+1} начал работу")
            thread = Thread(target=worker)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()


def main():
    run_threads()

    print(global_count)


main()
