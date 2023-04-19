''""""Создайте класс "Rectangle", который будет содержать атрибуты "ширина" и "высота",
 а также методы "площадь", который будет возвращать площадь прямоугольника, и "периметр",
  который будет возвращать периметр прямоугольника."""''

class Rectangle:
    width = 10
    height = 30

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2*self.width + 2*self.height


r = Rectangle()


print(r.square())
print(r.perimeter())
