from threading import Thread
from threading import Lock, Condition, active_count, enumerate
from time import sleep

buffer = []

lock = Lock()


# класс производит данные
class Producer(Thread):

    def __init__(self, buffer: list, lock: Lock) -> None:
        super().__init__()
        self.buffer = buffer
        self.lock = lock

    def run(self) -> None:
        self.generate_data()

    def generate_data(self) -> None:
        for i in range(20):
            sleep(0.25)
            self.lock.acquire()
            self.buffer.append(i)
            print(f"Producer добавил: {i}")
            self.lock.release()


class Consumer(Thread):
    def __init__(self, buffer: list, lock: Lock):
        # инициализация для базового класса
        super().__init__()
        self.buffer = buffer
        self.lock = lock

    def run(self):
        self.get_data()

    def get_data(self) -> None:
        for _ in range(20):
            self.lock.acquire()

            if self.buffer:
                value = self.buffer.pop(0)
                print(f"Consumer прочитал: {value}")

            self.lock.release()

            sleep(0.25)


def main():
    pr = Producer(buffer, lock)
    cons = Consumer(buffer, lock)
    pr.start()
    print(f"число активных потоков: {active_count()}")

    cons.start()
    print(f"число активных потоков: {active_count()}")
    pr.join()
    cons.join()
    print(f"число активных потоков: {active_count()}")
    print(enumerate())


main()
