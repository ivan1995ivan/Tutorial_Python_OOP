
''''Создайте класс Person, который будет иметь следующие атрибуты:

name - имя человека
age - возраст человека
Также класс Person должен содержать следующий классовый атрибут:

total_persons - количество созданных объектов класса Person
И классовый метод:

display_total_persons() - выводит в консоль количество созданных объектов класса Person
В классе Person реализуйте метод __init__, который принимает name и age, и устанавливает
соответствующие атрибуты.'''


class Person:
    total_persons = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_persons += 1

    @classmethod
    def display_total_persons(cls):
        print(f'Total persons: {Person.total_persons}')

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
Person.display_total_persons()