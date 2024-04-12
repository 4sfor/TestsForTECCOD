import math


class Point:
    # инициализация
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # получить позицию
    def get_position(self):
        return self.x, self.y

    # смена позиции
    def change_position(self, x, y):
        self.x = x
        self.y = y

    # расстояние между точками
    def get_distance(self, other_object):
        distance = math.sqrt((other_object.x - self.x) ** 2 + (other_object.y - self.y) ** 2)
        return distance
