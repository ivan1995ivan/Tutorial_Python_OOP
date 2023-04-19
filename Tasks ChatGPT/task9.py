'''Напишите класс Person, у которого есть атрибуты name, age и address.
Создайте метод greet(), который выводит на экран сообщение приветствия,
содержащее имя, возраст и адрес объекта типа Person.

Создайте объект person1 класса Person и вызовите метод greet().'''


class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        print('Hello ' + self.name + ' ' + 'your age is ' + str(self.age) + ' ' + 'your address is ' + self.address)


person1 = Person('Peter', 56 , 'KIEV, str. Hreschatik, 1 ')
person1.greet()




