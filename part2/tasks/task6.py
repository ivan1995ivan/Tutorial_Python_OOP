class Person:
    age = 18

    def __init__(self, x, y):
        self.height = x
        self.name = y


p = Person(179, 'Jacob')
print(p.__dict__)
