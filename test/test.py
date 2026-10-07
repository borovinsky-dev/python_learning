class Alpha:
    def __init__(self, num):
        self.code = num

    def show(self):
        print("Класс Alpha:", self.code)


class Bravo(Alpha):
    def show(self):
        print("Класс Bravo:", self.code)
        super().show()


class Charlie(Alpha):
    def show(self):
        print("Класс Charlie:", self.code)
        super(Charlie, self).show()


class Delta(Bravo, Charlie):
    def show(self):
        print("Класс Delta:", self.code)

        super().show()

        Charlie.show(self)

        super(Bravo, self).show()


def display(MyClass):
    print("Порядок разрешения для", MyClass.__name__, ":")

    k = 1
    for cls in MyClass.__mro__:
        print(f"[{k}] {cls.__name__}")
        k += 1


display(Alpha)
A = Alpha(100)
A.show()

display(Bravo)
B = Bravo(200)
B.show()

display(Charlie)
C = Charlie(300)
C.show()

display(Delta)
D = Delta(400)
D.show()
