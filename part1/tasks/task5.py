# class A:
#     x = 15
#
#
# a = A()
# a.y = 'hello'
# print(A.__dict__, a.__dict__, sep='\n')
# setattr(A, 'x', 12478)
# print(a.x)
import math
import operator


class Circle:
    r = 5.0


class Rectangle:
    width = 5.0
    height = 7.0


print(math.pi*Circle.r**2)
print()
print(Rectangle.width*Rectangle.height)



