class Car:
    speed = 90.0
    color = 'red'


print(Car.speed, Car.color, sep='\n')
del Car.speed
print(Car.__dict__)