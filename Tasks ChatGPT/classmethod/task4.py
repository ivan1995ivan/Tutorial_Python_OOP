'''Напишите класс User, который имеет атрибуты name, age и email
(имя, возраст и электронная почта соответственно),
и метод display_info,
который выводит информацию о пользователе в формате "Имя: <name>, Возраст: <age>, Email: <email>".

Также напишите метод класса from_input_string,
который принимает один аргумент input_string в формате "name,age,email"
и создает объект User с соответствующими значениями атрибутов,
разбивая строку на части по символу ",".
Используйте декоратор @classmethod для создания метода from_input_string.'''


class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}, Email: {self.email}')

    @classmethod
    def from_input_string(cls, input_string):
        c = input_string.split(',')
        return cls(name=c[0], age=c[1], email=c[2])


user1 = User("Alice", 25, "alice@example.com")
user1.display_info() # выводит "Имя: Alice, Возраст: 25, Email: alice@example.com"

user2 = User.from_input_string("Bob,30,bob@example.com")
user2.display_info() # выводит "Имя: Bob, Возраст: 30, Email: bob@example.com"

