import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        return (
            f"{self.__class__.__name__}: "
            f"Area={self.area():.2f}, Perimeter={self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r**2)

    def perimeter(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2

        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


Shapes = [Circle(10), Rectangle(5, 10), Triangle(3, 3, 3)]

for shape in Shapes:
    print(shape.describe())
