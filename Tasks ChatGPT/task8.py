'''Создайте класс Dog с атрибутами name, breed и color.
Создайте метод bark() для вывода в консоль звука, который издает собака при лаем.
Создайте подкласс ServiceDog с атрибутом is_working, который будет указывать, находится ли собака на службе.
 Добавьте метод work() для вывода в консоль информации о том, находится ли собака на службе.'''


class Dog:
    def __init__(self, name, bread, color ):
        self.name = name
        self.bread = bread
        self.color = color

    def bark(self):
        print('Gav!!!')

class ServiceDog(Dog):
    def __init__(self, name, bread, color, is_working: bool):
        super().__init__(name, bread, color,)
        self.is_working = is_working

    def work(self):
        if self.is_working:
            print('Dog is working')


rex = ServiceDog('Rex', 'boxer', 'black', True)
rex.bark()
rex.work()