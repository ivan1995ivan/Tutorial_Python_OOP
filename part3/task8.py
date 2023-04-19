class A:

    def add(self, a, b):
        return a+b


A.x = 5
A.y = 'hello'

print(A.add(A(), 24, -17.4))
