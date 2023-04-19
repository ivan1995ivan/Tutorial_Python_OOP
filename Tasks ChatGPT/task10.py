'''Напишите класс Book c атрибутами title, author, publisher, и методом info(),
 который выводит информацию о книге в формате "Название: {название},
 Автор: {автор}, Издательство: {издательство}".

Затем создайте подкласс Ebook, который наследует атрибуты и методы родительского класса Book,
 а также имеет дополнительный атрибут format и переопределяет метод info() таким образом,
  чтобы включать информацию о формате книги в вывод.

Используйте классы для создания объектов книг и электронных книг,
 и вызовите метод info() для каждого объекта, чтобы проверить, что все работает корректно.'''


class Book:

    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Издательство: {self.publisher}")


class Ebook(Book):
    def __init__(self, title, author, publisher, format):
        super().__init__(title, author, publisher)
        self.format = format

    def info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Издательство: {self.publisher}, Формат: {self.format}")

