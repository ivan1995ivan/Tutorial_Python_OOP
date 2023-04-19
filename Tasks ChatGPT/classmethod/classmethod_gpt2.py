'''Напишите класс Rectangle, который имеет атрибуты width и height (ширина и высота соответственно),
и метод calculate_area, который возвращает площадь прямоугольника.
Также напишите метод класса from_square, который принимает один аргумент side,
создает объект Rectangle и возвращает его,
где width и height равны значению side. Используйте декоратор @classmethod для создания метода from_square.'''


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)


r1 = Rectangle(3, 4)
print(r1.calculate_area())

r2 = Rectangle.from_square(5)
print(r2.calculate_area())

