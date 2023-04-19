import random
from pprint import pprint
from random import randrange

class Boy:
    age = 15
    height = 160


arr = [Boy() for _ in range(5)]
index = randrange(0, 5)
arr[index].height = 165
#print(arr[index].__dict__)
arr_height = [arr[index].height for index in range(5)]
pprint(arr_height)

