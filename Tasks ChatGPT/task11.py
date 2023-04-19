'''Напишите класс Rectangle для представления прямоугольника.
У этого класса должны быть атрибуты width и height для представления размеров прямоугольника.
 Реализуйте методы get_area() для вычисления площади и get_perimeter() для вычисления периметра прямоугольника.
 Напишите дополнительно метод is_square(), который будет возвращать True,
 если данный прямоугольник является квадратом, и False в противном случае.'''


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2*self.width + 2*self.height

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False
