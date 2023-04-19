import math

class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def calc_square(self):
        return math.pi * self.radius**2

c = Circumference(3.4)
print(c.calc_square())