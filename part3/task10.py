class A:

    def __init__(self, x):
        self.x = x
        self.y = 'default'


a = A(23)
print(a.__dict__)