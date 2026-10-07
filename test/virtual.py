class Alpha:
    def display(self):
        print("Класс Alpha")
        print("code:", self.code)

    def show(self):
        self.display()


class Bravo(Alpha):
    def display(self):
        print("Класс Bravo")
        print("name:", self.name)


A = Alpha()
A.code = 123

B = Bravo()
B.name = "B"

A.show()
B.show()
