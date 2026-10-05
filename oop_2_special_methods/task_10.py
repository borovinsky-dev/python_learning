class Fibonachi:
    def __init__(self, bound: int):
        self.bound = bound

    def __iter__(self):
        a = 0
        b = 1
        for i in range(1, self.bound):
            a, b = b, a + b
            yield b
