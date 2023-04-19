class Cat:
    age = 2
    bread = 'Bengal'


tom = Cat()
setattr(tom, 'age', 1)
print(getattr(Cat, 'bread'), getattr(Cat, 'age'), sep='\n')
print()
print(tom.__dict__, tom.age)
