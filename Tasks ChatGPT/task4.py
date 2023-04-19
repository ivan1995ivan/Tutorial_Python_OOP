'''Создайте класс "Книга", содержащий атрибуты "название" и "автор".
Добавьте метод, который будет выводить информацию о книге в консоль.'''

class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show(self):
        print(self.name, "\n", self.author)

p = Book('book_name', 'Book_author' )
p.show()