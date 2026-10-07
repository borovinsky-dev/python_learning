from re import match
from threading import Thread
from time import sleep


class MyThread(Thread):
    # Можно добавить объект, который при вызове __call__ возвращает функцию
    def __init__(self, target=None, bound=None) -> None:

        if target == None and bound == None:
            raise TypeError(
                "Необходимо передать параметры инициализации классу MyThread"
            )
        elif target != None and bound == None:
            self.error_validation_target(target)
            self.mode = "target"
            self.target = target
        elif target == None and bound != None:
            self.error_validation_bound(bound)
            self.mode = "bound"
            self.bound = bound
        else:
            self.error_validation_target(target)
            self.error_validation_bound(bound)
            self.mode = "both"
            self.target = target
            self.bound = bound
            # Инициализация базового класса Thread при создании объекта
            super().__init__(target=target)

    # запускается при старте потока obj.start
    def run(self) -> str:
        match self.mode:
            case "target":
                # вызываю у родителя thread инициализатор для выполнения target
                super().run()
            case "bound":
                self.calculate()
            case "both":
                t1 = Thread(target=self.target)
                t2 = Thread(target=self.calculate)
                t1.start()
                t2.start()
                t1.join()
                t2.join()

    def calculate(self) -> int:
        current_result = ""
        summa = 0
        for i in range(self.bound + 1):
            current_result += str(summa) + "\t"
            print(current_result)
            sleep(2)
            summa += i**2
        return summa

    # Статические метод, чтобы не использовать self
    @staticmethod
    def error_validation_target(target):
        if not callable(target):
            raise Exception(
                "Объект не является функцией либо не"
                " имеет специальный метод __call__"
            )

    @staticmethod
    def error_validation_bound(bound: int):
        if type(bound) != int:
            raise TypeError("Объект не int")


def first_worker():
    for i in range(5):
        print(f"[TARGET] шаг {i}")
        sleep(1)


def second_worker():
    for i in range(5):
        print(f"[SECOND] шаг {i}")
        sleep(1.5)


def main():
    print("\n=== TARGET ===")
    t1 = MyThread(target=first_worker)
    t1.start()
    t1.join()

    print("\n=== BOUND ===")
    t2 = MyThread(bound=5)
    t2.start()
    t2.join()

    print("\n=== BOTH ===")
    t3 = MyThread(target=second_worker, bound=5)
    t3.start()
    t3.join()

    print("\n=== MAIN FINISHED ===")


if __name__ == "__main__":
    print("Прямой запуск модуля")
    main()
