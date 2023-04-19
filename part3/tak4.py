import math
import pprint

class Computer:
    age: int = 5
    price: int = 200
    size: str = 'big'

print(getattr(Computer, 'sdf', str(math.pi)))
pprint.pprint(Computer.__dict__)
del Computer.price
delattr(Computer, 'size')
print(Computer.__dict__)