

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能小于0")
        self._radius =  value

c = Circle(5)
c._radius = -5
print(c.area)