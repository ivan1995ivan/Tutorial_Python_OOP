'''Создайте класс "Человек", содержащий атрибуты "имя" и "возраст".
 Добавьте метод, который будет выводить информацию о человеке в консоль.
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, "\n", self.age)

p = Person('Peter', '23' )
p.show()