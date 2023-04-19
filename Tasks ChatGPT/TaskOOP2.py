'''Создайте класс Animal, который будет иметь атрибуты name, age, species, sound.
Класс должен иметь метод make_sound(), который будет выводить на экран звук животного.

Создайте класс Dog, который наследует класс Animal.
Добавьте атрибут breed и переопределите метод make_sound(), чтобы он выводил звук лая.

Создайте класс Cat, который наследует класс Animal.
Добавьте атрибут color и переопределите метод make_sound(), чтобы он выводил звук мяуканья.

Создайте класс Zoo, который будет хранить список животных.
Класс должен иметь методы add_animal() и remove_animal(), чтобы добавлять и удалять животных из списка.
Класс также должен иметь метод show_animals(),
 который будет выводить список всех животных в зоопарке и вызывать метод make_sound() каждого животного.'''


class Animal:
    def __init__(self, name, age, species, sound):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, age, species, sound, bread):
        super().__init__(name, age, species, sound)
        self.bread = bread

    def make_sound(self):
        super().make_sound()
        print('GAV')


class Cat(Animal):
    def __init__(self, name, age, species, sound, color):
        super().__init__(name, age, species, sound)
        self.color = color

    def make_sound(self):
        super().make_sound()
        print('MEOW')

class Zoo:
    def __init__(self, list_zoo=None):
        self.list_zoo = list_zoo or []

    def add_animal(self, animal):
        self.list_zoo.append(animal)

    def remove_animal(self, animal):
        self.list_zoo.remove(animal)

    def show_animals(self):
        for animal in self.list_zoo:
            print(f"{animal.name}, {animal.age} year(s) old, {animal.species}")
            animal.make_sound()



dog = Dog('Rex', 22, 'Dog','woof','dvorneaga')
cat = Cat('Whiskers', 1, 'Cat', 'Purr', 'Calico')
parrot = Animal('Polly', 3, 'Parrot', 'Squawk')

zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(parrot)

zoo.show_animals()

zoo.remove_animal(dog)
zoo.show_animals()
