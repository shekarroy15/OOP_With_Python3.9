# TODO - Using Abstract class
#

import collections
from abc import abstractmethod, ABC

try:
    collectionsAbc = collections.ABC, abstractmethod()
except AttributeError:
    collectionsAbc = collections


class GraphicSize(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcarea(self):
        pass


class Circle(GraphicSize):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius

    def calcarea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicSize):
    def __init__(self, side):
        super(Square, self).__init__()
        self.side = side

    def calcarea(self):
        return self.side * self.side


sq = Square(4)
print(sq.calcarea())
ci = Circle(23)
print(ci.calcarea())
