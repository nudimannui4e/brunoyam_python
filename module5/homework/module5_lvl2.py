# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

class Point:
    """ Уровень 2 """
    def __init__(self, x: int, y: int):
        self.y = y
        self.x = x

    def __add__(self, other):
        """ Сложание координат """
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2
