'''Создайте класс "Круг",
содержащий атрибут "радиус". Добавьте методы,
 которые будут вычислять площадь и длину окружности.'''
import math

class Circle:

    def __init__(self, r):
        self.r = r

    def square(self):
        return math.pi*self.r**2

    def length(self):
        return 2*math.pi*self.r
c = Circle(56)

print("Square: ",  c.square())
print('Lenght: ', c.length())