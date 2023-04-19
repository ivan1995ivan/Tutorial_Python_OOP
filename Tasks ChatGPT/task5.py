'''Создайте класс Person с атрибутами name и age. Добавьте метод get_age()
для получения возраста человека. Создайте подкласс Employee с атрибутом salary.
 Добавьте метод get_salary() для получения зарплаты работника.'''


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Employee(Person):
    salary = 5000

    def get_salary(self):
        return Employee.salary

# Tom = Person('Tom', 43)
# print(Tom.get_age())


Tom = Employee('Tom', 43)
print(Tom.get_age())
print(Tom.get_salary())