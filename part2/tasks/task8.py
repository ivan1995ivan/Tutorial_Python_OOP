class Cat:
    age = 2
    breed = 'Bengal'

    def __init__(self, color: str):
        self.color: str  = color

    def meow(self):
        print('MEOW')



tom = Cat('black')
tom.meow()
#
# print(tom.__dict__)
# print(Cat.__dict__)