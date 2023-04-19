import pprint

class Person:
    name: str = 'Liza'
    age: int = 12


l = Person()
l.hair_color = 'blue'
print(getattr(Person, 'hair_color', False))
print(isinstance(l, type), isinstance(l, int), sep= '\n')