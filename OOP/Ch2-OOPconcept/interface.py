from abc import ABC, abstractmethod


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicSize(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcarea(self):
        pass


class Circle(GraphicSize, JSONify):
    def toJSON(self):
        return f"{{\"area\" : {str(self.calcarea())}}}"

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
print(ci.toJSON())
