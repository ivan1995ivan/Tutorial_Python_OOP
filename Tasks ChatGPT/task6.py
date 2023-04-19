'''Создайте класс Shape с методом area(), который должен возвращать площадь фигуры.
Создайте подклассы Rectangle, Square и Triangle,
 которые будут наследовать метод area() и переопределять его для каждой из этих фигур.'''

import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def area(self):
        return self.l*self.h


class Square(Shape):
    def __init__(self, n):
        self.n = n

    def area(self):
        return self.n**2


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


patrat = Square(7)
print(patrat.area())
triangle = Triangle(88, 99, 80)
print(triangle.area())





