import math


class Point:
    """Класс для работы с координатами"""

    def __init__(self, x: float, y: float) -> None:
        """Инициализирует атрибуты объекта"""
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        """метод объекта класса для переопределения координат"""
        self.x = x
        self.y = y

    def reset(self):
        """Метод для сброса сзначений"""
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_object: "Point") -> float:
        """Высисляет координаты"""
        dist_x = abs(self.x - other_object.x)
        dist_y = abs(self.y - other_object.y)
        return math.sqrt(dist_x**2 + dist_y**2)


def main():
    pass


if main == "__main__":
    main()
