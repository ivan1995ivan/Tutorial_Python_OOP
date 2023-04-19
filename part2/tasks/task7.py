# class Person:
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#
# p1 = Person('Trevor', 15)
# p2 = Person('Liza', 22)
#
# print(p1.name, p2.name)
# print(p1.age, p2.age)


class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b= b
        self.c = c

    def check_equals(self):
        return self.a == self.b or self.b == self.c or self.a == self.c

t = Triangle(1, 23, 23.0)
print('equals' if t.check_equals() else 'no equals')