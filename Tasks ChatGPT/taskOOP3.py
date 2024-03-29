'''Реализуйте класс Vehicle (Транспортное средство), который имеет следующие атрибуты:

make (марка) - строка, обязательный атрибут
model (модель) - строка, обязательный атрибут
year (год выпуска) - целое число, обязательный атрибут
weight (вес) - целое число, необязательный атрибут (по умолчанию 0)
Также реализуйте методы:

display_info (вывод информации) - выводит информацию о транспортном средстве в следующем формате:
 Марка: <make>, Модель: <model>, Год выпуска: <year>, Вес: <weight>
get_age (возраст) - возвращает количество лет, прошедших с момента выпуска транспортного средства.
Для вычисления возраста использовать текущий год (можно использовать модуль datetime).
Напишите класс Car (Автомобиль), который наследует класс Vehicle.
Класс Car должен иметь дополнительный атрибут
num_doors (количество дверей) - целое число, обязательный атрибут.

Также реализуйте методы:

display_info (вывод информации) - выводит информацию об автомобиле в следующем формате:
Марка: <make>, Модель: <model>, Год выпуска: <year>, Вес: <weight>, Количество дверей: <num_doors>
get_age (возраст) - возвращает количество лет, прошедших с момента выпуска автомобиля.
Для вычисления возраста использовать текущий год (можно использовать модуль datetime).'''
from datetime import datetime, date


class Vehicle:
    def __init__(self, make, model, year, weight=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def display_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}, Вес: {self.weight}')

    def get_age(self):
        y = datetime.now()
        return int(y.strftime("%Y"))-self.year


class Car(Vehicle):

    def __init__(self, make, model, year, num_doors, weight=0,):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors

    def display_info(self):
        print(f'Марка: {self.make}, Модель: {self.model}, Год выпуска: {self.year}, Вес: {self.weight}, \
Количество дверей: {self.num_doors}')


v1 = Vehicle("Audi", "A3", 2015, 1500)
v1.display_info() # Выводит "Марка: Audi, Модель: A3, Год выпуска: 2015, Вес: 1500"
print(v1.get_age()) # Выводит количество лет, например 7

c1 = Car("Ford", "Focus", 2010, num_doors=4)
c1.display_info() # Выводит "Марка: Ford, Модель: Focus, Год выпуска: 2010, Вес: 0, Количество дверей: 4"
print(c1.get_age()) # Выводит количество лет, например 12